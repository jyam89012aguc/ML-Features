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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f062_intang_burden(intangibles, assets):
    return intangibles / assets.replace(0, np.nan).abs()


# 21d mean of intang_burden scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_mean_21d_base_v001_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of intang_burden scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_mean_63d_base_v002_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of intang_burden scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_mean_126d_base_v003_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of intang_burden scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_mean_252d_base_v004_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of intang_burden scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_mean_504d_base_v005_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of amort_intensity scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_mean_21d_base_v006_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of amort_intensity scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_mean_63d_base_v007_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of amort_intensity scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_mean_126d_base_v008_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of amort_intensity scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_mean_252d_base_v009_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of amort_intensity scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_mean_504d_base_v010_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of intang_yoy_chg scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_mean_21d_base_v011_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of intang_yoy_chg scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_mean_63d_base_v012_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of intang_yoy_chg scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_mean_126d_base_v013_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of intang_yoy_chg scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_mean_252d_base_v014_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of intang_yoy_chg scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_mean_504d_base_v015_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of intang_decline_flag scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_mean_21d_base_v016_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of intang_decline_flag scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_mean_63d_base_v017_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of intang_decline_flag scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_mean_126d_base_v018_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of intang_decline_flag scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_mean_252d_base_v019_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of intang_decline_flag scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_mean_504d_base_v020_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of opex_impair_proxy scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_mean_21d_base_v021_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of opex_impair_proxy scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_mean_63d_base_v022_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of opex_impair_proxy scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_mean_126d_base_v023_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of opex_impair_proxy scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_mean_252d_base_v024_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of opex_impair_proxy scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_mean_504d_base_v025_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of amort_to_opex_proxy scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_mean_21d_base_v026_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of amort_to_opex_proxy scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_mean_63d_base_v027_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of amort_to_opex_proxy scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_mean_126d_base_v028_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of amort_to_opex_proxy scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_mean_252d_base_v029_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of amort_to_opex_proxy scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_mean_504d_base_v030_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of intang_minus_equity scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_mean_21d_base_v031_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of intang_minus_equity scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_mean_63d_base_v032_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of intang_minus_equity scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_mean_126d_base_v033_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of intang_minus_equity scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_mean_252d_base_v034_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of intang_minus_equity scaled by closeadj
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_mean_504d_base_v035_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_median_63d_base_v036_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_median_252d_base_v037_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_median_504d_base_v038_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_median_63d_base_v039_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_median_252d_base_v040_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_median_504d_base_v041_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_median_63d_base_v042_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_median_252d_base_v043_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_median_504d_base_v044_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_median_63d_base_v045_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_median_252d_base_v046_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_median_504d_base_v047_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_median_63d_base_v048_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_median_252d_base_v049_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_median_504d_base_v050_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_median_63d_base_v051_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_median_252d_base_v052_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_median_504d_base_v053_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_median_63d_base_v054_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_median_252d_base_v055_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_median_504d_base_v056_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_rmax_252d_base_v057_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_rmax_504d_base_v058_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_rmax_252d_base_v059_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_rmax_504d_base_v060_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_rmax_252d_base_v061_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_rmax_504d_base_v062_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_rmax_252d_base_v063_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_rmax_504d_base_v064_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_rmax_252d_base_v065_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_rmax_504d_base_v066_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_rmax_252d_base_v067_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_rmax_504d_base_v068_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_rmax_252d_base_v069_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_rmax_504d_base_v070_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_rmin_252d_base_v071_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_rmin_504d_base_v072_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_rmin_252d_base_v073_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_rmin_504d_base_v074_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_rmin_252d_base_v075_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

