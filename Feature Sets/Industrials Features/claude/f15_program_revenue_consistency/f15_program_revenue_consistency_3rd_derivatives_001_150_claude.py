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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    denom = s.shift(w).abs().replace(0, np.nan)
    return s.diff(periods=w) / denom


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives (f15 program_revenue_consistency) =====
def _f15_revenue_cv(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / m.replace(0, np.nan).abs()


def _f15_program_smoothness(revenue, w):
    diff = revenue.diff().abs()
    return diff.rolling(w, min_periods=max(1, w // 2)).mean() / revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan).abs()


def _f15_revenue_predictability(revenue, w):
    rg = revenue.pct_change(periods=max(1, w // 4))
    sd = rg.rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / (1.0 + sd.replace(0, np.nan))


def prc_f15_program_revenue_consistency_revcv_5d_scaledc_jerk5_v001_signal(closeadj, revenue, deferredrev):
    base = ((_f15_revenue_cv(revenue, 5))) * (closeadj)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_5d_meanmc_jerk5_v002_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_revenue_cv(revenue, 5)), 5)) * (_mean(closeadj, 21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_5d_stdc_jerk10_v003_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_revenue_cv(revenue, 5)), 5)) * (closeadj)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_5d_emamc_jerk10_v004_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_revenue_cv(revenue, 5)), 5)) * (_mean(closeadj, 21))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_5d_zc_jerk21_v005_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_revenue_cv(revenue, 5)), 5)) * (closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_5d_logmeanmc_jerk21_v006_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_revenue_cv(revenue, 5)), 5).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_5d_sqrtsignc_jerk63_v007_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_revenue_cv(revenue, 5)) * np.sqrt((_f15_revenue_cv(revenue, 5)).abs())) * (closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_5d_diffxclosemc_jerk63_v008_signal(closeadj, revenue, deferredrev):
    base = (((_f15_revenue_cv(revenue, 5)).diff(periods=max(1, 5 // 3)))) * (_mean(closeadj, 21))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_10d_scaledc_jerk126_v009_signal(closeadj, revenue, deferredrev):
    base = ((_f15_revenue_cv(revenue, 10))) * (closeadj)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_10d_meanmc_jerk126_v010_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_revenue_cv(revenue, 10)), 10)) * (_mean(closeadj, 21))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_10d_stdc_jerk252_v011_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_revenue_cv(revenue, 10)), 10)) * (closeadj)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_10d_emamc_jerk252_v012_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_revenue_cv(revenue, 10)), 10)) * (_mean(closeadj, 21))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_10d_logmeanc_jerk5_v013_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_revenue_cv(revenue, 10)), 10).abs())) * (closeadj)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_10d_sqrtsignmc_jerk5_v014_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_revenue_cv(revenue, 10)) * np.sqrt((_f15_revenue_cv(revenue, 10)).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_10d_diffxclosec_jerk10_v015_signal(closeadj, revenue, deferredrev):
    base = (((_f15_revenue_cv(revenue, 10)).diff(periods=max(1, 10 // 3)))) * (closeadj)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_21d_scaledmc_jerk10_v016_signal(closeadj, revenue, deferredrev):
    base = ((_f15_revenue_cv(revenue, 21))) * (_mean(closeadj, 21))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_21d_meanc_jerk21_v017_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_revenue_cv(revenue, 21)), 21)) * (closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_21d_stdmc_jerk21_v018_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_revenue_cv(revenue, 21)), 21)) * (_mean(closeadj, 21))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_21d_emac_jerk63_v019_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_revenue_cv(revenue, 21)), 21)) * (closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_21d_zmc_jerk63_v020_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_revenue_cv(revenue, 21)), 21)) * (_mean(closeadj, 21))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_21d_logmeanc_jerk126_v021_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_revenue_cv(revenue, 21)), 21).abs())) * (closeadj)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_21d_sqrtsignmc_jerk126_v022_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_revenue_cv(revenue, 21)) * np.sqrt((_f15_revenue_cv(revenue, 21)).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_21d_diffxclosec_jerk252_v023_signal(closeadj, revenue, deferredrev):
    base = (((_f15_revenue_cv(revenue, 21)).diff(periods=max(1, 21 // 3)))) * (closeadj)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_42d_scaledmc_jerk252_v024_signal(closeadj, revenue, deferredrev):
    base = ((_f15_revenue_cv(revenue, 42))) * (_mean(closeadj, 21))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_42d_stdc_jerk5_v025_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_revenue_cv(revenue, 42)), 42)) * (closeadj)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_42d_emamc_jerk5_v026_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_revenue_cv(revenue, 42)), 42)) * (_mean(closeadj, 21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_42d_zc_jerk10_v027_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_revenue_cv(revenue, 42)), 42)) * (closeadj)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_42d_logmeanmc_jerk10_v028_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_revenue_cv(revenue, 42)), 42).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_42d_sqrtsignc_jerk21_v029_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_revenue_cv(revenue, 42)) * np.sqrt((_f15_revenue_cv(revenue, 42)).abs())) * (closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_42d_diffxclosemc_jerk21_v030_signal(closeadj, revenue, deferredrev):
    base = (((_f15_revenue_cv(revenue, 42)).diff(periods=max(1, 42 // 3)))) * (_mean(closeadj, 21))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_63d_scaledc_jerk63_v031_signal(closeadj, revenue, deferredrev):
    base = ((_f15_revenue_cv(revenue, 63))) * (closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_63d_meanmc_jerk63_v032_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_revenue_cv(revenue, 63)), 63)) * (_mean(closeadj, 21))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_63d_stdc_jerk126_v033_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_revenue_cv(revenue, 63)), 63)) * (closeadj)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_63d_emamc_jerk126_v034_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_revenue_cv(revenue, 63)), 63)) * (_mean(closeadj, 21))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_63d_zc_jerk252_v035_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_revenue_cv(revenue, 63)), 63)) * (closeadj)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_63d_logmeanmc_jerk252_v036_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_revenue_cv(revenue, 63)), 63).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_63d_diffxclosec_jerk5_v037_signal(closeadj, revenue, deferredrev):
    base = (((_f15_revenue_cv(revenue, 63)).diff(periods=max(1, 63 // 3)))) * (closeadj)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_126d_scaledmc_jerk5_v038_signal(closeadj, revenue, deferredrev):
    base = ((_f15_revenue_cv(revenue, 126))) * (_mean(closeadj, 21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_126d_meanc_jerk10_v039_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_revenue_cv(revenue, 126)), 126)) * (closeadj)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_126d_stdmc_jerk10_v040_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_revenue_cv(revenue, 126)), 126)) * (_mean(closeadj, 21))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_126d_emac_jerk21_v041_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_revenue_cv(revenue, 126)), 126)) * (closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_126d_zmc_jerk21_v042_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_revenue_cv(revenue, 126)), 126)) * (_mean(closeadj, 21))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_126d_logmeanc_jerk63_v043_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_revenue_cv(revenue, 126)), 126).abs())) * (closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_126d_sqrtsignmc_jerk63_v044_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_revenue_cv(revenue, 126)) * np.sqrt((_f15_revenue_cv(revenue, 126)).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_126d_diffxclosec_jerk126_v045_signal(closeadj, revenue, deferredrev):
    base = (((_f15_revenue_cv(revenue, 126)).diff(periods=max(1, 126 // 3)))) * (closeadj)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_252d_scaledmc_jerk126_v046_signal(closeadj, revenue, deferredrev):
    base = ((_f15_revenue_cv(revenue, 252))) * (_mean(closeadj, 21))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_252d_meanc_jerk252_v047_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_revenue_cv(revenue, 252)), 252)) * (closeadj)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_252d_stdmc_jerk252_v048_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_revenue_cv(revenue, 252)), 252)) * (_mean(closeadj, 21))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_252d_zc_jerk5_v049_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_revenue_cv(revenue, 252)), 252)) * (closeadj)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_252d_logmeanmc_jerk5_v050_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_revenue_cv(revenue, 252)), 252).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_252d_sqrtsignc_jerk10_v051_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_revenue_cv(revenue, 252)) * np.sqrt((_f15_revenue_cv(revenue, 252)).abs())) * (closeadj)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revcv_252d_diffxclosemc_jerk10_v052_signal(closeadj, revenue, deferredrev):
    base = (((_f15_revenue_cv(revenue, 252)).diff(periods=max(1, 252 // 3)))) * (_mean(closeadj, 21))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_5d_scaledc_jerk21_v053_signal(closeadj, revenue, deferredrev):
    base = ((_f15_program_smoothness(revenue, 5))) * (closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_5d_meanmc_jerk21_v054_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_program_smoothness(revenue, 5)), 5)) * (_mean(closeadj, 21))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_5d_stdc_jerk63_v055_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_program_smoothness(revenue, 5)), 5)) * (closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_5d_emamc_jerk63_v056_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_program_smoothness(revenue, 5)), 5)) * (_mean(closeadj, 21))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_5d_zc_jerk126_v057_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_program_smoothness(revenue, 5)), 5)) * (closeadj)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_5d_logmeanmc_jerk126_v058_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_program_smoothness(revenue, 5)), 5).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_5d_sqrtsignc_jerk252_v059_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_program_smoothness(revenue, 5)) * np.sqrt((_f15_program_smoothness(revenue, 5)).abs())) * (closeadj)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_5d_diffxclosemc_jerk252_v060_signal(closeadj, revenue, deferredrev):
    base = (((_f15_program_smoothness(revenue, 5)).diff(periods=max(1, 5 // 3)))) * (_mean(closeadj, 21))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_10d_meanc_jerk5_v061_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_program_smoothness(revenue, 10)), 10)) * (closeadj)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_10d_stdmc_jerk5_v062_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_program_smoothness(revenue, 10)), 10)) * (_mean(closeadj, 21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_10d_emac_jerk10_v063_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_program_smoothness(revenue, 10)), 10)) * (closeadj)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_10d_zmc_jerk10_v064_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_program_smoothness(revenue, 10)), 10)) * (_mean(closeadj, 21))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_10d_logmeanc_jerk21_v065_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_program_smoothness(revenue, 10)), 10).abs())) * (closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_10d_sqrtsignmc_jerk21_v066_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_program_smoothness(revenue, 10)) * np.sqrt((_f15_program_smoothness(revenue, 10)).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_10d_diffxclosec_jerk63_v067_signal(closeadj, revenue, deferredrev):
    base = (((_f15_program_smoothness(revenue, 10)).diff(periods=max(1, 10 // 3)))) * (closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_21d_scaledmc_jerk63_v068_signal(closeadj, revenue, deferredrev):
    base = ((_f15_program_smoothness(revenue, 21))) * (_mean(closeadj, 21))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_21d_meanc_jerk126_v069_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_program_smoothness(revenue, 21)), 21)) * (closeadj)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_21d_stdmc_jerk126_v070_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_program_smoothness(revenue, 21)), 21)) * (_mean(closeadj, 21))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_21d_emac_jerk252_v071_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_program_smoothness(revenue, 21)), 21)) * (closeadj)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_21d_zmc_jerk252_v072_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_program_smoothness(revenue, 21)), 21)) * (_mean(closeadj, 21))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_21d_sqrtsignc_jerk5_v073_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_program_smoothness(revenue, 21)) * np.sqrt((_f15_program_smoothness(revenue, 21)).abs())) * (closeadj)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_21d_diffxclosemc_jerk5_v074_signal(closeadj, revenue, deferredrev):
    base = (((_f15_program_smoothness(revenue, 21)).diff(periods=max(1, 21 // 3)))) * (_mean(closeadj, 21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_42d_scaledc_jerk10_v075_signal(closeadj, revenue, deferredrev):
    base = ((_f15_program_smoothness(revenue, 42))) * (closeadj)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_42d_meanmc_jerk10_v076_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_program_smoothness(revenue, 42)), 42)) * (_mean(closeadj, 21))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_42d_stdc_jerk21_v077_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_program_smoothness(revenue, 42)), 42)) * (closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_42d_emamc_jerk21_v078_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_program_smoothness(revenue, 42)), 42)) * (_mean(closeadj, 21))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_42d_zc_jerk63_v079_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_program_smoothness(revenue, 42)), 42)) * (closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_42d_logmeanmc_jerk63_v080_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_program_smoothness(revenue, 42)), 42).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_42d_sqrtsignc_jerk126_v081_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_program_smoothness(revenue, 42)) * np.sqrt((_f15_program_smoothness(revenue, 42)).abs())) * (closeadj)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_42d_diffxclosemc_jerk126_v082_signal(closeadj, revenue, deferredrev):
    base = (((_f15_program_smoothness(revenue, 42)).diff(periods=max(1, 42 // 3)))) * (_mean(closeadj, 21))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_63d_scaledc_jerk252_v083_signal(closeadj, revenue, deferredrev):
    base = ((_f15_program_smoothness(revenue, 63))) * (closeadj)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_63d_meanmc_jerk252_v084_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_program_smoothness(revenue, 63)), 63)) * (_mean(closeadj, 21))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_63d_emac_jerk5_v085_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_program_smoothness(revenue, 63)), 63)) * (closeadj)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_63d_zmc_jerk5_v086_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_program_smoothness(revenue, 63)), 63)) * (_mean(closeadj, 21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_63d_logmeanc_jerk10_v087_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_program_smoothness(revenue, 63)), 63).abs())) * (closeadj)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_63d_sqrtsignmc_jerk10_v088_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_program_smoothness(revenue, 63)) * np.sqrt((_f15_program_smoothness(revenue, 63)).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_63d_diffxclosec_jerk21_v089_signal(closeadj, revenue, deferredrev):
    base = (((_f15_program_smoothness(revenue, 63)).diff(periods=max(1, 63 // 3)))) * (closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_126d_scaledmc_jerk21_v090_signal(closeadj, revenue, deferredrev):
    base = ((_f15_program_smoothness(revenue, 126))) * (_mean(closeadj, 21))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_126d_meanc_jerk63_v091_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_program_smoothness(revenue, 126)), 126)) * (closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_126d_stdmc_jerk63_v092_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_program_smoothness(revenue, 126)), 126)) * (_mean(closeadj, 21))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_126d_emac_jerk126_v093_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_program_smoothness(revenue, 126)), 126)) * (closeadj)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_126d_zmc_jerk126_v094_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_program_smoothness(revenue, 126)), 126)) * (_mean(closeadj, 21))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_126d_logmeanc_jerk252_v095_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_program_smoothness(revenue, 126)), 126).abs())) * (closeadj)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_126d_sqrtsignmc_jerk252_v096_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_program_smoothness(revenue, 126)) * np.sqrt((_f15_program_smoothness(revenue, 126)).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_252d_scaledc_jerk5_v097_signal(closeadj, revenue, deferredrev):
    base = ((_f15_program_smoothness(revenue, 252))) * (closeadj)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_252d_meanmc_jerk5_v098_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_program_smoothness(revenue, 252)), 252)) * (_mean(closeadj, 21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_252d_stdc_jerk10_v099_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_program_smoothness(revenue, 252)), 252)) * (closeadj)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_252d_emamc_jerk10_v100_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_program_smoothness(revenue, 252)), 252)) * (_mean(closeadj, 21))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_252d_zc_jerk21_v101_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_program_smoothness(revenue, 252)), 252)) * (closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_252d_logmeanmc_jerk21_v102_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_program_smoothness(revenue, 252)), 252).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_252d_sqrtsignc_jerk63_v103_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_program_smoothness(revenue, 252)) * np.sqrt((_f15_program_smoothness(revenue, 252)).abs())) * (closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_smooth_252d_diffxclosemc_jerk63_v104_signal(closeadj, revenue, deferredrev):
    base = (((_f15_program_smoothness(revenue, 252)).diff(periods=max(1, 252 // 3)))) * (_mean(closeadj, 21))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_5d_scaledc_jerk126_v105_signal(closeadj, revenue, deferredrev):
    base = ((_f15_revenue_predictability(revenue, 5))) * (closeadj)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_5d_meanmc_jerk126_v106_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_revenue_predictability(revenue, 5)), 5)) * (_mean(closeadj, 21))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_5d_stdc_jerk252_v107_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_revenue_predictability(revenue, 5)), 5)) * (closeadj)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_5d_emamc_jerk252_v108_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_revenue_predictability(revenue, 5)), 5)) * (_mean(closeadj, 21))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_5d_logmeanc_jerk5_v109_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_revenue_predictability(revenue, 5)), 5).abs())) * (closeadj)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_5d_sqrtsignmc_jerk5_v110_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_revenue_predictability(revenue, 5)) * np.sqrt((_f15_revenue_predictability(revenue, 5)).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_5d_diffxclosec_jerk10_v111_signal(closeadj, revenue, deferredrev):
    base = (((_f15_revenue_predictability(revenue, 5)).diff(periods=max(1, 5 // 3)))) * (closeadj)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_10d_scaledmc_jerk10_v112_signal(closeadj, revenue, deferredrev):
    base = ((_f15_revenue_predictability(revenue, 10))) * (_mean(closeadj, 21))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_10d_meanc_jerk21_v113_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_revenue_predictability(revenue, 10)), 10)) * (closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_10d_stdmc_jerk21_v114_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_revenue_predictability(revenue, 10)), 10)) * (_mean(closeadj, 21))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_10d_emac_jerk63_v115_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_revenue_predictability(revenue, 10)), 10)) * (closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_10d_zmc_jerk63_v116_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_revenue_predictability(revenue, 10)), 10)) * (_mean(closeadj, 21))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_10d_logmeanc_jerk126_v117_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_revenue_predictability(revenue, 10)), 10).abs())) * (closeadj)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_10d_sqrtsignmc_jerk126_v118_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_revenue_predictability(revenue, 10)) * np.sqrt((_f15_revenue_predictability(revenue, 10)).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_10d_diffxclosec_jerk252_v119_signal(closeadj, revenue, deferredrev):
    base = (((_f15_revenue_predictability(revenue, 10)).diff(periods=max(1, 10 // 3)))) * (closeadj)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_21d_scaledmc_jerk252_v120_signal(closeadj, revenue, deferredrev):
    base = ((_f15_revenue_predictability(revenue, 21))) * (_mean(closeadj, 21))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_21d_stdc_jerk5_v121_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_revenue_predictability(revenue, 21)), 21)) * (closeadj)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_21d_emamc_jerk5_v122_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_revenue_predictability(revenue, 21)), 21)) * (_mean(closeadj, 21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_21d_zc_jerk10_v123_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_revenue_predictability(revenue, 21)), 21)) * (closeadj)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_21d_logmeanmc_jerk10_v124_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_revenue_predictability(revenue, 21)), 21).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_21d_sqrtsignc_jerk21_v125_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_revenue_predictability(revenue, 21)) * np.sqrt((_f15_revenue_predictability(revenue, 21)).abs())) * (closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_21d_diffxclosemc_jerk21_v126_signal(closeadj, revenue, deferredrev):
    base = (((_f15_revenue_predictability(revenue, 21)).diff(periods=max(1, 21 // 3)))) * (_mean(closeadj, 21))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_42d_scaledc_jerk63_v127_signal(closeadj, revenue, deferredrev):
    base = ((_f15_revenue_predictability(revenue, 42))) * (closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_42d_meanmc_jerk63_v128_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_revenue_predictability(revenue, 42)), 42)) * (_mean(closeadj, 21))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_42d_stdc_jerk126_v129_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_revenue_predictability(revenue, 42)), 42)) * (closeadj)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_42d_emamc_jerk126_v130_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_revenue_predictability(revenue, 42)), 42)) * (_mean(closeadj, 21))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_42d_zc_jerk252_v131_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_revenue_predictability(revenue, 42)), 42)) * (closeadj)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_42d_logmeanmc_jerk252_v132_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_revenue_predictability(revenue, 42)), 42).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_42d_diffxclosec_jerk5_v133_signal(closeadj, revenue, deferredrev):
    base = (((_f15_revenue_predictability(revenue, 42)).diff(periods=max(1, 42 // 3)))) * (closeadj)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_63d_scaledmc_jerk5_v134_signal(closeadj, revenue, deferredrev):
    base = ((_f15_revenue_predictability(revenue, 63))) * (_mean(closeadj, 21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_63d_meanc_jerk10_v135_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_revenue_predictability(revenue, 63)), 63)) * (closeadj)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_63d_stdmc_jerk10_v136_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_revenue_predictability(revenue, 63)), 63)) * (_mean(closeadj, 21))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_63d_emac_jerk21_v137_signal(closeadj, revenue, deferredrev):
    base = (_ema((_f15_revenue_predictability(revenue, 63)), 63)) * (closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_63d_zmc_jerk21_v138_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_revenue_predictability(revenue, 63)), 63)) * (_mean(closeadj, 21))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_63d_logmeanc_jerk63_v139_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_revenue_predictability(revenue, 63)), 63).abs())) * (closeadj)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_63d_sqrtsignmc_jerk63_v140_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_revenue_predictability(revenue, 63)) * np.sqrt((_f15_revenue_predictability(revenue, 63)).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_63d_diffxclosec_jerk126_v141_signal(closeadj, revenue, deferredrev):
    base = (((_f15_revenue_predictability(revenue, 63)).diff(periods=max(1, 63 // 3)))) * (closeadj)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_126d_scaledmc_jerk126_v142_signal(closeadj, revenue, deferredrev):
    base = ((_f15_revenue_predictability(revenue, 126))) * (_mean(closeadj, 21))
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_126d_meanc_jerk252_v143_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_revenue_predictability(revenue, 126)), 126)) * (closeadj)
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_126d_stdmc_jerk252_v144_signal(closeadj, revenue, deferredrev):
    base = (_std((_f15_revenue_predictability(revenue, 126)), 126)) * (_mean(closeadj, 21))
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_126d_zc_jerk5_v145_signal(closeadj, revenue, deferredrev):
    base = (_z((_f15_revenue_predictability(revenue, 126)), 126)) * (closeadj)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_126d_logmeanmc_jerk5_v146_signal(closeadj, revenue, deferredrev):
    base = (np.log1p(_mean((_f15_revenue_predictability(revenue, 126)), 126).abs())) * (_mean(closeadj, 21))
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_126d_sqrtsignc_jerk10_v147_signal(closeadj, revenue, deferredrev):
    base = (np.sign(_f15_revenue_predictability(revenue, 126)) * np.sqrt((_f15_revenue_predictability(revenue, 126)).abs())) * (closeadj)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_126d_diffxclosemc_jerk10_v148_signal(closeadj, revenue, deferredrev):
    base = (((_f15_revenue_predictability(revenue, 126)).diff(periods=max(1, 126 // 3)))) * (_mean(closeadj, 21))
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_252d_scaledc_jerk21_v149_signal(closeadj, revenue, deferredrev):
    base = ((_f15_revenue_predictability(revenue, 252))) * (closeadj)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def prc_f15_program_revenue_consistency_revpred_252d_meanmc_jerk21_v150_signal(closeadj, revenue, deferredrev):
    base = (_mean((_f15_revenue_predictability(revenue, 252)), 252)) * (_mean(closeadj, 21))
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    prc_f15_program_revenue_consistency_revcv_5d_scaledc_jerk5_v001_signal,
    prc_f15_program_revenue_consistency_revcv_5d_meanmc_jerk5_v002_signal,
    prc_f15_program_revenue_consistency_revcv_5d_stdc_jerk10_v003_signal,
    prc_f15_program_revenue_consistency_revcv_5d_emamc_jerk10_v004_signal,
    prc_f15_program_revenue_consistency_revcv_5d_zc_jerk21_v005_signal,
    prc_f15_program_revenue_consistency_revcv_5d_logmeanmc_jerk21_v006_signal,
    prc_f15_program_revenue_consistency_revcv_5d_sqrtsignc_jerk63_v007_signal,
    prc_f15_program_revenue_consistency_revcv_5d_diffxclosemc_jerk63_v008_signal,
    prc_f15_program_revenue_consistency_revcv_10d_scaledc_jerk126_v009_signal,
    prc_f15_program_revenue_consistency_revcv_10d_meanmc_jerk126_v010_signal,
    prc_f15_program_revenue_consistency_revcv_10d_stdc_jerk252_v011_signal,
    prc_f15_program_revenue_consistency_revcv_10d_emamc_jerk252_v012_signal,
    prc_f15_program_revenue_consistency_revcv_10d_logmeanc_jerk5_v013_signal,
    prc_f15_program_revenue_consistency_revcv_10d_sqrtsignmc_jerk5_v014_signal,
    prc_f15_program_revenue_consistency_revcv_10d_diffxclosec_jerk10_v015_signal,
    prc_f15_program_revenue_consistency_revcv_21d_scaledmc_jerk10_v016_signal,
    prc_f15_program_revenue_consistency_revcv_21d_meanc_jerk21_v017_signal,
    prc_f15_program_revenue_consistency_revcv_21d_stdmc_jerk21_v018_signal,
    prc_f15_program_revenue_consistency_revcv_21d_emac_jerk63_v019_signal,
    prc_f15_program_revenue_consistency_revcv_21d_zmc_jerk63_v020_signal,
    prc_f15_program_revenue_consistency_revcv_21d_logmeanc_jerk126_v021_signal,
    prc_f15_program_revenue_consistency_revcv_21d_sqrtsignmc_jerk126_v022_signal,
    prc_f15_program_revenue_consistency_revcv_21d_diffxclosec_jerk252_v023_signal,
    prc_f15_program_revenue_consistency_revcv_42d_scaledmc_jerk252_v024_signal,
    prc_f15_program_revenue_consistency_revcv_42d_stdc_jerk5_v025_signal,
    prc_f15_program_revenue_consistency_revcv_42d_emamc_jerk5_v026_signal,
    prc_f15_program_revenue_consistency_revcv_42d_zc_jerk10_v027_signal,
    prc_f15_program_revenue_consistency_revcv_42d_logmeanmc_jerk10_v028_signal,
    prc_f15_program_revenue_consistency_revcv_42d_sqrtsignc_jerk21_v029_signal,
    prc_f15_program_revenue_consistency_revcv_42d_diffxclosemc_jerk21_v030_signal,
    prc_f15_program_revenue_consistency_revcv_63d_scaledc_jerk63_v031_signal,
    prc_f15_program_revenue_consistency_revcv_63d_meanmc_jerk63_v032_signal,
    prc_f15_program_revenue_consistency_revcv_63d_stdc_jerk126_v033_signal,
    prc_f15_program_revenue_consistency_revcv_63d_emamc_jerk126_v034_signal,
    prc_f15_program_revenue_consistency_revcv_63d_zc_jerk252_v035_signal,
    prc_f15_program_revenue_consistency_revcv_63d_logmeanmc_jerk252_v036_signal,
    prc_f15_program_revenue_consistency_revcv_63d_diffxclosec_jerk5_v037_signal,
    prc_f15_program_revenue_consistency_revcv_126d_scaledmc_jerk5_v038_signal,
    prc_f15_program_revenue_consistency_revcv_126d_meanc_jerk10_v039_signal,
    prc_f15_program_revenue_consistency_revcv_126d_stdmc_jerk10_v040_signal,
    prc_f15_program_revenue_consistency_revcv_126d_emac_jerk21_v041_signal,
    prc_f15_program_revenue_consistency_revcv_126d_zmc_jerk21_v042_signal,
    prc_f15_program_revenue_consistency_revcv_126d_logmeanc_jerk63_v043_signal,
    prc_f15_program_revenue_consistency_revcv_126d_sqrtsignmc_jerk63_v044_signal,
    prc_f15_program_revenue_consistency_revcv_126d_diffxclosec_jerk126_v045_signal,
    prc_f15_program_revenue_consistency_revcv_252d_scaledmc_jerk126_v046_signal,
    prc_f15_program_revenue_consistency_revcv_252d_meanc_jerk252_v047_signal,
    prc_f15_program_revenue_consistency_revcv_252d_stdmc_jerk252_v048_signal,
    prc_f15_program_revenue_consistency_revcv_252d_zc_jerk5_v049_signal,
    prc_f15_program_revenue_consistency_revcv_252d_logmeanmc_jerk5_v050_signal,
    prc_f15_program_revenue_consistency_revcv_252d_sqrtsignc_jerk10_v051_signal,
    prc_f15_program_revenue_consistency_revcv_252d_diffxclosemc_jerk10_v052_signal,
    prc_f15_program_revenue_consistency_smooth_5d_scaledc_jerk21_v053_signal,
    prc_f15_program_revenue_consistency_smooth_5d_meanmc_jerk21_v054_signal,
    prc_f15_program_revenue_consistency_smooth_5d_stdc_jerk63_v055_signal,
    prc_f15_program_revenue_consistency_smooth_5d_emamc_jerk63_v056_signal,
    prc_f15_program_revenue_consistency_smooth_5d_zc_jerk126_v057_signal,
    prc_f15_program_revenue_consistency_smooth_5d_logmeanmc_jerk126_v058_signal,
    prc_f15_program_revenue_consistency_smooth_5d_sqrtsignc_jerk252_v059_signal,
    prc_f15_program_revenue_consistency_smooth_5d_diffxclosemc_jerk252_v060_signal,
    prc_f15_program_revenue_consistency_smooth_10d_meanc_jerk5_v061_signal,
    prc_f15_program_revenue_consistency_smooth_10d_stdmc_jerk5_v062_signal,
    prc_f15_program_revenue_consistency_smooth_10d_emac_jerk10_v063_signal,
    prc_f15_program_revenue_consistency_smooth_10d_zmc_jerk10_v064_signal,
    prc_f15_program_revenue_consistency_smooth_10d_logmeanc_jerk21_v065_signal,
    prc_f15_program_revenue_consistency_smooth_10d_sqrtsignmc_jerk21_v066_signal,
    prc_f15_program_revenue_consistency_smooth_10d_diffxclosec_jerk63_v067_signal,
    prc_f15_program_revenue_consistency_smooth_21d_scaledmc_jerk63_v068_signal,
    prc_f15_program_revenue_consistency_smooth_21d_meanc_jerk126_v069_signal,
    prc_f15_program_revenue_consistency_smooth_21d_stdmc_jerk126_v070_signal,
    prc_f15_program_revenue_consistency_smooth_21d_emac_jerk252_v071_signal,
    prc_f15_program_revenue_consistency_smooth_21d_zmc_jerk252_v072_signal,
    prc_f15_program_revenue_consistency_smooth_21d_sqrtsignc_jerk5_v073_signal,
    prc_f15_program_revenue_consistency_smooth_21d_diffxclosemc_jerk5_v074_signal,
    prc_f15_program_revenue_consistency_smooth_42d_scaledc_jerk10_v075_signal,
    prc_f15_program_revenue_consistency_smooth_42d_meanmc_jerk10_v076_signal,
    prc_f15_program_revenue_consistency_smooth_42d_stdc_jerk21_v077_signal,
    prc_f15_program_revenue_consistency_smooth_42d_emamc_jerk21_v078_signal,
    prc_f15_program_revenue_consistency_smooth_42d_zc_jerk63_v079_signal,
    prc_f15_program_revenue_consistency_smooth_42d_logmeanmc_jerk63_v080_signal,
    prc_f15_program_revenue_consistency_smooth_42d_sqrtsignc_jerk126_v081_signal,
    prc_f15_program_revenue_consistency_smooth_42d_diffxclosemc_jerk126_v082_signal,
    prc_f15_program_revenue_consistency_smooth_63d_scaledc_jerk252_v083_signal,
    prc_f15_program_revenue_consistency_smooth_63d_meanmc_jerk252_v084_signal,
    prc_f15_program_revenue_consistency_smooth_63d_emac_jerk5_v085_signal,
    prc_f15_program_revenue_consistency_smooth_63d_zmc_jerk5_v086_signal,
    prc_f15_program_revenue_consistency_smooth_63d_logmeanc_jerk10_v087_signal,
    prc_f15_program_revenue_consistency_smooth_63d_sqrtsignmc_jerk10_v088_signal,
    prc_f15_program_revenue_consistency_smooth_63d_diffxclosec_jerk21_v089_signal,
    prc_f15_program_revenue_consistency_smooth_126d_scaledmc_jerk21_v090_signal,
    prc_f15_program_revenue_consistency_smooth_126d_meanc_jerk63_v091_signal,
    prc_f15_program_revenue_consistency_smooth_126d_stdmc_jerk63_v092_signal,
    prc_f15_program_revenue_consistency_smooth_126d_emac_jerk126_v093_signal,
    prc_f15_program_revenue_consistency_smooth_126d_zmc_jerk126_v094_signal,
    prc_f15_program_revenue_consistency_smooth_126d_logmeanc_jerk252_v095_signal,
    prc_f15_program_revenue_consistency_smooth_126d_sqrtsignmc_jerk252_v096_signal,
    prc_f15_program_revenue_consistency_smooth_252d_scaledc_jerk5_v097_signal,
    prc_f15_program_revenue_consistency_smooth_252d_meanmc_jerk5_v098_signal,
    prc_f15_program_revenue_consistency_smooth_252d_stdc_jerk10_v099_signal,
    prc_f15_program_revenue_consistency_smooth_252d_emamc_jerk10_v100_signal,
    prc_f15_program_revenue_consistency_smooth_252d_zc_jerk21_v101_signal,
    prc_f15_program_revenue_consistency_smooth_252d_logmeanmc_jerk21_v102_signal,
    prc_f15_program_revenue_consistency_smooth_252d_sqrtsignc_jerk63_v103_signal,
    prc_f15_program_revenue_consistency_smooth_252d_diffxclosemc_jerk63_v104_signal,
    prc_f15_program_revenue_consistency_revpred_5d_scaledc_jerk126_v105_signal,
    prc_f15_program_revenue_consistency_revpred_5d_meanmc_jerk126_v106_signal,
    prc_f15_program_revenue_consistency_revpred_5d_stdc_jerk252_v107_signal,
    prc_f15_program_revenue_consistency_revpred_5d_emamc_jerk252_v108_signal,
    prc_f15_program_revenue_consistency_revpred_5d_logmeanc_jerk5_v109_signal,
    prc_f15_program_revenue_consistency_revpred_5d_sqrtsignmc_jerk5_v110_signal,
    prc_f15_program_revenue_consistency_revpred_5d_diffxclosec_jerk10_v111_signal,
    prc_f15_program_revenue_consistency_revpred_10d_scaledmc_jerk10_v112_signal,
    prc_f15_program_revenue_consistency_revpred_10d_meanc_jerk21_v113_signal,
    prc_f15_program_revenue_consistency_revpred_10d_stdmc_jerk21_v114_signal,
    prc_f15_program_revenue_consistency_revpred_10d_emac_jerk63_v115_signal,
    prc_f15_program_revenue_consistency_revpred_10d_zmc_jerk63_v116_signal,
    prc_f15_program_revenue_consistency_revpred_10d_logmeanc_jerk126_v117_signal,
    prc_f15_program_revenue_consistency_revpred_10d_sqrtsignmc_jerk126_v118_signal,
    prc_f15_program_revenue_consistency_revpred_10d_diffxclosec_jerk252_v119_signal,
    prc_f15_program_revenue_consistency_revpred_21d_scaledmc_jerk252_v120_signal,
    prc_f15_program_revenue_consistency_revpred_21d_stdc_jerk5_v121_signal,
    prc_f15_program_revenue_consistency_revpred_21d_emamc_jerk5_v122_signal,
    prc_f15_program_revenue_consistency_revpred_21d_zc_jerk10_v123_signal,
    prc_f15_program_revenue_consistency_revpred_21d_logmeanmc_jerk10_v124_signal,
    prc_f15_program_revenue_consistency_revpred_21d_sqrtsignc_jerk21_v125_signal,
    prc_f15_program_revenue_consistency_revpred_21d_diffxclosemc_jerk21_v126_signal,
    prc_f15_program_revenue_consistency_revpred_42d_scaledc_jerk63_v127_signal,
    prc_f15_program_revenue_consistency_revpred_42d_meanmc_jerk63_v128_signal,
    prc_f15_program_revenue_consistency_revpred_42d_stdc_jerk126_v129_signal,
    prc_f15_program_revenue_consistency_revpred_42d_emamc_jerk126_v130_signal,
    prc_f15_program_revenue_consistency_revpred_42d_zc_jerk252_v131_signal,
    prc_f15_program_revenue_consistency_revpred_42d_logmeanmc_jerk252_v132_signal,
    prc_f15_program_revenue_consistency_revpred_42d_diffxclosec_jerk5_v133_signal,
    prc_f15_program_revenue_consistency_revpred_63d_scaledmc_jerk5_v134_signal,
    prc_f15_program_revenue_consistency_revpred_63d_meanc_jerk10_v135_signal,
    prc_f15_program_revenue_consistency_revpred_63d_stdmc_jerk10_v136_signal,
    prc_f15_program_revenue_consistency_revpred_63d_emac_jerk21_v137_signal,
    prc_f15_program_revenue_consistency_revpred_63d_zmc_jerk21_v138_signal,
    prc_f15_program_revenue_consistency_revpred_63d_logmeanc_jerk63_v139_signal,
    prc_f15_program_revenue_consistency_revpred_63d_sqrtsignmc_jerk63_v140_signal,
    prc_f15_program_revenue_consistency_revpred_63d_diffxclosec_jerk126_v141_signal,
    prc_f15_program_revenue_consistency_revpred_126d_scaledmc_jerk126_v142_signal,
    prc_f15_program_revenue_consistency_revpred_126d_meanc_jerk252_v143_signal,
    prc_f15_program_revenue_consistency_revpred_126d_stdmc_jerk252_v144_signal,
    prc_f15_program_revenue_consistency_revpred_126d_zc_jerk5_v145_signal,
    prc_f15_program_revenue_consistency_revpred_126d_logmeanmc_jerk5_v146_signal,
    prc_f15_program_revenue_consistency_revpred_126d_sqrtsignc_jerk10_v147_signal,
    prc_f15_program_revenue_consistency_revpred_126d_diffxclosemc_jerk10_v148_signal,
    prc_f15_program_revenue_consistency_revpred_252d_scaledc_jerk21_v149_signal,
    prc_f15_program_revenue_consistency_revpred_252d_meanmc_jerk21_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_PROGRAM_REVENUE_CONSISTENCY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "deferredrev": deferredrev,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f15_revenue_cv", "_f15_program_smoothness", "_f15_revenue_predictability",)
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
    print(f"OK f15_program_revenue_consistency_3rd_derivatives_001_150_claude: {n_features} features pass")
