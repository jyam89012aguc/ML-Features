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


def f40tic_f40_textile_input_cost_sensitivity_correv_5d_base_v001_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_10d_base_v002_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_21d_base_v003_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_42d_base_v004_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_63d_base_v005_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_126d_base_v006_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_189d_base_v007_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_252d_base_v008_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_378d_base_v009_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_correv_504d_base_v010_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_5d_base_v011_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 5)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_10d_base_v012_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 10)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_21d_base_v013_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_42d_base_v014_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_63d_base_v015_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_126d_base_v016_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_189d_base_v017_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_252d_base_v018_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_378d_base_v019_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsens_504d_base_v020_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_5d_base_v021_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 5)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_10d_base_v022_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 10)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_21d_base_v023_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_42d_base_v024_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_63d_base_v025_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_126d_base_v026_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_189d_base_v027_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_252d_base_v028_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_378d_base_v029_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthru_504d_base_v030_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvz_63d_base_v031_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvz_126d_base_v032_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _z(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvz_189d_base_v033_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _z(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvz_252d_base_v034_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvz_378d_base_v035_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _z(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvz_504d_base_v036_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _z(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensz_63d_base_v037_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensz_126d_base_v038_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _z(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensz_189d_base_v039_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _z(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensz_252d_base_v040_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensz_378d_base_v041_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _z(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensz_504d_base_v042_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _z(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruz_63d_base_v043_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruz_126d_base_v044_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _z(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruz_189d_base_v045_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _z(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruz_252d_base_v046_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruz_378d_base_v047_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _z(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruz_504d_base_v048_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _z(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_21d_base_v049_signal(cor, revenue, grossmargin, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 21) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_63d_base_v050_signal(cor, revenue, grossmargin, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 63) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_126d_base_v051_signal(cor, revenue, grossmargin, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 126) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_189d_base_v052_signal(cor, revenue, grossmargin, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 189) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_252d_base_v053_signal(cor, revenue, grossmargin, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 252) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvxgm_504d_base_v054_signal(cor, revenue, grossmargin, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _mean(d, 504) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensema_10d_base_v055_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _ema(d, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensema_21d_base_v056_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensema_63d_base_v057_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _ema(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensema_126d_base_v058_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _ema(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensema_252d_base_v059_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensema_504d_base_v060_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _ema(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruema_10d_base_v061_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _ema(d, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruema_21d_base_v062_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruema_63d_base_v063_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _ema(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruema_126d_base_v064_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _ema(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruema_252d_base_v065_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruema_504d_base_v066_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _ema(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvdiff_63d_base_v067_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = d.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvdiff_252d_base_v068_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = d.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxgm_63d_base_v069_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensxgm_252d_base_v070_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 252)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruxrev_252d_base_v071_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthruxgm_252d_base_v072_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 252)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_corrvstd_252d_base_v073_signal(cor, revenue, closeadj):
    d = _f40_cor_to_revenue(cor, revenue)
    result = _std(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_mgnsensstd_252d_base_v074_signal(grossmargin, cor, closeadj):
    d = _f40_margin_input_sensitivity(grossmargin, cor, 63)
    result = _std(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40tic_f40_textile_input_cost_sensitivity_passthrustd_252d_base_v075_signal(grossmargin, cor, revenue, closeadj):
    d = _f40_pass_through_score(grossmargin, cor, revenue, 63)
    result = _std(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40tic_f40_textile_input_cost_sensitivity_correv_5d_base_v001_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_10d_base_v002_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_21d_base_v003_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_42d_base_v004_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_63d_base_v005_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_126d_base_v006_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_189d_base_v007_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_252d_base_v008_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_378d_base_v009_signal,
    f40tic_f40_textile_input_cost_sensitivity_correv_504d_base_v010_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_5d_base_v011_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_10d_base_v012_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_21d_base_v013_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_42d_base_v014_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_63d_base_v015_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_126d_base_v016_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_189d_base_v017_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_252d_base_v018_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_378d_base_v019_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsens_504d_base_v020_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_5d_base_v021_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_10d_base_v022_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_21d_base_v023_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_42d_base_v024_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_63d_base_v025_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_126d_base_v026_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_189d_base_v027_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_252d_base_v028_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_378d_base_v029_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthru_504d_base_v030_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvz_63d_base_v031_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvz_126d_base_v032_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvz_189d_base_v033_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvz_252d_base_v034_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvz_378d_base_v035_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvz_504d_base_v036_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensz_63d_base_v037_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensz_126d_base_v038_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensz_189d_base_v039_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensz_252d_base_v040_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensz_378d_base_v041_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensz_504d_base_v042_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruz_63d_base_v043_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruz_126d_base_v044_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruz_189d_base_v045_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruz_252d_base_v046_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruz_378d_base_v047_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruz_504d_base_v048_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_21d_base_v049_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_63d_base_v050_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_126d_base_v051_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_189d_base_v052_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_252d_base_v053_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvxgm_504d_base_v054_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensema_10d_base_v055_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensema_21d_base_v056_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensema_63d_base_v057_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensema_126d_base_v058_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensema_252d_base_v059_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensema_504d_base_v060_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruema_10d_base_v061_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruema_21d_base_v062_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruema_63d_base_v063_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruema_126d_base_v064_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruema_252d_base_v065_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruema_504d_base_v066_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvdiff_63d_base_v067_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvdiff_252d_base_v068_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxgm_63d_base_v069_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensxgm_252d_base_v070_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruxrev_252d_base_v071_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthruxgm_252d_base_v072_signal,
    f40tic_f40_textile_input_cost_sensitivity_corrvstd_252d_base_v073_signal,
    f40tic_f40_textile_input_cost_sensitivity_mgnsensstd_252d_base_v074_signal,
    f40tic_f40_textile_input_cost_sensitivity_passthrustd_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_TEXTILE_INPUT_COST_SENSITIVITY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f40_textile_input_cost_sensitivity_001_075_claude: {n_features} features pass")
