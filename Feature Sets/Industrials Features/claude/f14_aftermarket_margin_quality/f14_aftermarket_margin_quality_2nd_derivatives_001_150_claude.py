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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    denom = s.shift(w).abs().replace(0, np.nan)
    return s.diff(periods=w) / denom


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives (f14 aftermarket_margin_quality) =====
def _f14_margin_durability(grossmargin, w):
    m = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    return m / (sd.replace(0, np.nan).abs() + 0.001)


def _f14_margin_floor(ebitdamargin, w):
    return ebitdamargin.rolling(w, min_periods=max(1, w // 2)).quantile(0.10)


def _f14_margin_stability(grossmargin, ebitdamargin, w):
    sd_g = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    sd_e = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / (1.0 + sd_g + sd_e)


def amq_f14_aftermarket_margin_quality_mdur_5d_mn_slpct5_v001_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 5)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_10d_mn_slpct10_v002_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 10)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_21d_mn_slpct21_v003_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 21)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_42d_mn_slpct63_v004_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 42)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_63d_mn_slpct126_v005_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 63)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_126d_mn_slpct252_v006_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 126)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_252d_mn_slpct5_v007_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 252)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_5d_mn_slpct10_v008_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 5)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_10d_mn_slpct21_v009_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 10)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_21d_mn_slpct63_v010_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 21)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_42d_mn_slpct126_v011_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 42)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_63d_mn_slpct252_v012_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 63)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_126d_mn_slpct5_v013_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 126)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_252d_mn_slpct10_v014_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 252)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_5d_mn_slpct21_v015_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 5)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_10d_mn_slpct63_v016_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 10)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_21d_mn_slpct126_v017_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 21)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_42d_mn_slpct252_v018_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 42)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_63d_mn_slpct5_v019_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 63)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_126d_mn_slpct10_v020_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 126)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_252d_mn_slpct21_v021_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 252)
    base = _mean(p, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_5d_sd_slpct63_v022_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 5)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_10d_sd_slpct126_v023_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 10)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_21d_sd_slpct252_v024_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 21)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_42d_sd_slpct5_v025_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 42)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_63d_sd_slpct10_v026_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 63)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_126d_sd_slpct21_v027_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 126)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_252d_sd_slpct63_v028_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 252)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_5d_sd_slpct126_v029_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 5)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_10d_sd_slpct252_v030_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 10)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_21d_sd_slpct5_v031_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 21)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_42d_sd_slpct10_v032_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 42)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_63d_sd_slpct21_v033_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 63)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_126d_sd_slpct63_v034_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 126)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_252d_sd_slpct126_v035_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 252)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_5d_sd_slpct252_v036_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 5)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_10d_sd_slpct5_v037_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 10)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_21d_sd_slpct10_v038_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 21)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_42d_sd_slpct21_v039_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 42)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_63d_sd_slpct63_v040_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 63)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_126d_sd_slpct126_v041_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 126)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_252d_sd_slpct252_v042_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 252)
    base = _std(p, 42) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_5d_em_slpct5_v043_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 5)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_10d_em_slpct10_v044_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 10)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_21d_em_slpct21_v045_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 21)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_42d_em_slpct63_v046_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 42)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_63d_em_slpct126_v047_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 63)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_126d_em_slpct252_v048_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 126)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_252d_em_slpct5_v049_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 252)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_5d_em_slpct10_v050_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 5)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_10d_em_slpct21_v051_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 10)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_21d_em_slpct63_v052_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 21)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_42d_em_slpct126_v053_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 42)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_63d_em_slpct252_v054_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 63)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_126d_em_slpct5_v055_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 126)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_252d_em_slpct10_v056_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 252)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_5d_em_slpct21_v057_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 5)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_10d_em_slpct63_v058_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 10)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_21d_em_slpct126_v059_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 21)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_42d_em_slpct252_v060_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 42)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_63d_em_slpct5_v061_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 63)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_126d_em_slpct10_v062_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 126)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_252d_em_slpct21_v063_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 252)
    base = _ema(p, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_5d_zlc_slpct63_v064_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 5)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_10d_zlc_slpct126_v065_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 10)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_21d_zlc_slpct252_v066_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 21)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_42d_zlc_slpct5_v067_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 42)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_63d_zlc_slpct10_v068_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 63)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_126d_zlc_slpct21_v069_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 126)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_252d_zlc_slpct63_v070_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 252)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_5d_zlc_slpct126_v071_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 5)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_10d_zlc_slpct252_v072_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 10)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_21d_zlc_slpct5_v073_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 21)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_42d_zlc_slpct10_v074_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 42)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_63d_zlc_slpct21_v075_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 63)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_126d_zlc_slpct63_v076_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 126)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_252d_zlc_slpct126_v077_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 252)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_5d_zlc_slpct252_v078_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 5)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_10d_zlc_slpct5_v079_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 10)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_21d_zlc_slpct10_v080_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 21)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_42d_zlc_slpct21_v081_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 42)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_63d_zlc_slpct63_v082_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 63)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_126d_zlc_slpct126_v083_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 126)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_252d_zlc_slpct252_v084_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 252)
    base = _z(p, 21) * (np.log1p(closeadj.abs()) + closeadj * 0.01)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_5d_lmn_slpct5_v085_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 5)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_10d_lmn_slpct10_v086_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 10)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_21d_lmn_slpct21_v087_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 21)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_42d_lmn_slpct63_v088_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 42)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_63d_lmn_slpct126_v089_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 63)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_126d_lmn_slpct252_v090_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 126)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_252d_lmn_slpct5_v091_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 252)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_5d_lmn_slpct10_v092_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 5)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_10d_lmn_slpct21_v093_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 10)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_21d_lmn_slpct63_v094_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 21)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_42d_lmn_slpct126_v095_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 42)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_63d_lmn_slpct252_v096_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 63)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_126d_lmn_slpct5_v097_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 126)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_252d_lmn_slpct10_v098_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 252)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_5d_lmn_slpct21_v099_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 5)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_10d_lmn_slpct63_v100_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 10)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_21d_lmn_slpct126_v101_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 21)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_42d_lmn_slpct252_v102_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 42)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_63d_lmn_slpct5_v103_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 63)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_126d_lmn_slpct10_v104_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 126)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_252d_lmn_slpct21_v105_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 252)
    base = np.log1p(_mean(p, 63).abs()) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_5d_ssq_slpct63_v106_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 5)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_10d_ssq_slpct126_v107_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 10)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_21d_ssq_slpct252_v108_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 21)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_42d_ssq_slpct5_v109_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 42)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_63d_ssq_slpct10_v110_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 63)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_126d_ssq_slpct21_v111_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 126)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_252d_ssq_slpct63_v112_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 252)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_5d_ssq_slpct126_v113_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 5)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_10d_ssq_slpct252_v114_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 10)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_21d_ssq_slpct5_v115_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 21)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_42d_ssq_slpct10_v116_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 42)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_63d_ssq_slpct21_v117_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 63)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_126d_ssq_slpct63_v118_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 126)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_252d_ssq_slpct126_v119_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 252)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_5d_ssq_slpct252_v120_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 5)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_10d_ssq_slpct5_v121_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 10)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_21d_ssq_slpct10_v122_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 21)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_42d_ssq_slpct21_v123_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 42)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_63d_ssq_slpct63_v124_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 63)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_126d_ssq_slpct126_v125_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 126)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_252d_ssq_slpct252_v126_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 252)
    diff = p - _mean(p, 126)
    base = np.sign(diff) * np.sqrt(diff.abs()) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_5d_dxe_slpct5_v127_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 5)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_10d_dxe_slpct10_v128_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 10)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_21d_dxe_slpct21_v129_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 21)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_42d_dxe_slpct63_v130_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 42)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_63d_dxe_slpct126_v131_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 63)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_126d_dxe_slpct252_v132_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 126)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_252d_dxe_slpct5_v133_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 252)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_5d_dxe_slpct10_v134_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_floor(ebitdamargin, 5)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_10d_dxe_slpct21_v135_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_floor(ebitdamargin, 10)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_21d_dxe_slpct63_v136_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_floor(ebitdamargin, 21)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_42d_dxe_slpct126_v137_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_floor(ebitdamargin, 42)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_63d_dxe_slpct252_v138_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_floor(ebitdamargin, 63)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_126d_dxe_slpct5_v139_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_floor(ebitdamargin, 126)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_252d_dxe_slpct10_v140_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_floor(ebitdamargin, 252)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_5d_dxe_slpct21_v141_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 5)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_10d_dxe_slpct63_v142_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 10)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_21d_dxe_slpct126_v143_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 21)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_42d_dxe_slpct252_v144_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 42)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_63d_dxe_slpct5_v145_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 63)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_126d_dxe_slpct10_v146_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 126)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_252d_dxe_slpct21_v147_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 252)
    ev = (1.0 + grossmargin) / (1.0 + _mean(grossmargin, 63))
    base = _diff(p, 252) * ev * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mdur_252d_em15_slpct63_v148_signal(closeadj, grossmargin):
    p = _f14_margin_durability(grossmargin, 252)
    base = _ema(p, 84) * (closeadj ** 1.5 + 1.0)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mfloor_252d_dmlc2_slpct126_v149_signal(closeadj, ebitdamargin):
    p = _f14_margin_floor(ebitdamargin, 252)
    base = (p - _mean(p, 252)) * (np.log1p(closeadj.abs()) ** 2)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def amq_f14_aftermarket_margin_quality_mstab_252d_zclc_slpct252_v150_signal(closeadj, ebitdamargin, grossmargin):
    p = _f14_margin_stability(grossmargin, ebitdamargin, 252)
    base = _z(p, 126) * (closeadj * np.log1p(closeadj.abs()))
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    amq_f14_aftermarket_margin_quality_mdur_5d_mn_slpct5_v001_signal,
    amq_f14_aftermarket_margin_quality_mdur_10d_mn_slpct10_v002_signal,
    amq_f14_aftermarket_margin_quality_mdur_21d_mn_slpct21_v003_signal,
    amq_f14_aftermarket_margin_quality_mdur_42d_mn_slpct63_v004_signal,
    amq_f14_aftermarket_margin_quality_mdur_63d_mn_slpct126_v005_signal,
    amq_f14_aftermarket_margin_quality_mdur_126d_mn_slpct252_v006_signal,
    amq_f14_aftermarket_margin_quality_mdur_252d_mn_slpct5_v007_signal,
    amq_f14_aftermarket_margin_quality_mfloor_5d_mn_slpct10_v008_signal,
    amq_f14_aftermarket_margin_quality_mfloor_10d_mn_slpct21_v009_signal,
    amq_f14_aftermarket_margin_quality_mfloor_21d_mn_slpct63_v010_signal,
    amq_f14_aftermarket_margin_quality_mfloor_42d_mn_slpct126_v011_signal,
    amq_f14_aftermarket_margin_quality_mfloor_63d_mn_slpct252_v012_signal,
    amq_f14_aftermarket_margin_quality_mfloor_126d_mn_slpct5_v013_signal,
    amq_f14_aftermarket_margin_quality_mfloor_252d_mn_slpct10_v014_signal,
    amq_f14_aftermarket_margin_quality_mstab_5d_mn_slpct21_v015_signal,
    amq_f14_aftermarket_margin_quality_mstab_10d_mn_slpct63_v016_signal,
    amq_f14_aftermarket_margin_quality_mstab_21d_mn_slpct126_v017_signal,
    amq_f14_aftermarket_margin_quality_mstab_42d_mn_slpct252_v018_signal,
    amq_f14_aftermarket_margin_quality_mstab_63d_mn_slpct5_v019_signal,
    amq_f14_aftermarket_margin_quality_mstab_126d_mn_slpct10_v020_signal,
    amq_f14_aftermarket_margin_quality_mstab_252d_mn_slpct21_v021_signal,
    amq_f14_aftermarket_margin_quality_mdur_5d_sd_slpct63_v022_signal,
    amq_f14_aftermarket_margin_quality_mdur_10d_sd_slpct126_v023_signal,
    amq_f14_aftermarket_margin_quality_mdur_21d_sd_slpct252_v024_signal,
    amq_f14_aftermarket_margin_quality_mdur_42d_sd_slpct5_v025_signal,
    amq_f14_aftermarket_margin_quality_mdur_63d_sd_slpct10_v026_signal,
    amq_f14_aftermarket_margin_quality_mdur_126d_sd_slpct21_v027_signal,
    amq_f14_aftermarket_margin_quality_mdur_252d_sd_slpct63_v028_signal,
    amq_f14_aftermarket_margin_quality_mfloor_5d_sd_slpct126_v029_signal,
    amq_f14_aftermarket_margin_quality_mfloor_10d_sd_slpct252_v030_signal,
    amq_f14_aftermarket_margin_quality_mfloor_21d_sd_slpct5_v031_signal,
    amq_f14_aftermarket_margin_quality_mfloor_42d_sd_slpct10_v032_signal,
    amq_f14_aftermarket_margin_quality_mfloor_63d_sd_slpct21_v033_signal,
    amq_f14_aftermarket_margin_quality_mfloor_126d_sd_slpct63_v034_signal,
    amq_f14_aftermarket_margin_quality_mfloor_252d_sd_slpct126_v035_signal,
    amq_f14_aftermarket_margin_quality_mstab_5d_sd_slpct252_v036_signal,
    amq_f14_aftermarket_margin_quality_mstab_10d_sd_slpct5_v037_signal,
    amq_f14_aftermarket_margin_quality_mstab_21d_sd_slpct10_v038_signal,
    amq_f14_aftermarket_margin_quality_mstab_42d_sd_slpct21_v039_signal,
    amq_f14_aftermarket_margin_quality_mstab_63d_sd_slpct63_v040_signal,
    amq_f14_aftermarket_margin_quality_mstab_126d_sd_slpct126_v041_signal,
    amq_f14_aftermarket_margin_quality_mstab_252d_sd_slpct252_v042_signal,
    amq_f14_aftermarket_margin_quality_mdur_5d_em_slpct5_v043_signal,
    amq_f14_aftermarket_margin_quality_mdur_10d_em_slpct10_v044_signal,
    amq_f14_aftermarket_margin_quality_mdur_21d_em_slpct21_v045_signal,
    amq_f14_aftermarket_margin_quality_mdur_42d_em_slpct63_v046_signal,
    amq_f14_aftermarket_margin_quality_mdur_63d_em_slpct126_v047_signal,
    amq_f14_aftermarket_margin_quality_mdur_126d_em_slpct252_v048_signal,
    amq_f14_aftermarket_margin_quality_mdur_252d_em_slpct5_v049_signal,
    amq_f14_aftermarket_margin_quality_mfloor_5d_em_slpct10_v050_signal,
    amq_f14_aftermarket_margin_quality_mfloor_10d_em_slpct21_v051_signal,
    amq_f14_aftermarket_margin_quality_mfloor_21d_em_slpct63_v052_signal,
    amq_f14_aftermarket_margin_quality_mfloor_42d_em_slpct126_v053_signal,
    amq_f14_aftermarket_margin_quality_mfloor_63d_em_slpct252_v054_signal,
    amq_f14_aftermarket_margin_quality_mfloor_126d_em_slpct5_v055_signal,
    amq_f14_aftermarket_margin_quality_mfloor_252d_em_slpct10_v056_signal,
    amq_f14_aftermarket_margin_quality_mstab_5d_em_slpct21_v057_signal,
    amq_f14_aftermarket_margin_quality_mstab_10d_em_slpct63_v058_signal,
    amq_f14_aftermarket_margin_quality_mstab_21d_em_slpct126_v059_signal,
    amq_f14_aftermarket_margin_quality_mstab_42d_em_slpct252_v060_signal,
    amq_f14_aftermarket_margin_quality_mstab_63d_em_slpct5_v061_signal,
    amq_f14_aftermarket_margin_quality_mstab_126d_em_slpct10_v062_signal,
    amq_f14_aftermarket_margin_quality_mstab_252d_em_slpct21_v063_signal,
    amq_f14_aftermarket_margin_quality_mdur_5d_zlc_slpct63_v064_signal,
    amq_f14_aftermarket_margin_quality_mdur_10d_zlc_slpct126_v065_signal,
    amq_f14_aftermarket_margin_quality_mdur_21d_zlc_slpct252_v066_signal,
    amq_f14_aftermarket_margin_quality_mdur_42d_zlc_slpct5_v067_signal,
    amq_f14_aftermarket_margin_quality_mdur_63d_zlc_slpct10_v068_signal,
    amq_f14_aftermarket_margin_quality_mdur_126d_zlc_slpct21_v069_signal,
    amq_f14_aftermarket_margin_quality_mdur_252d_zlc_slpct63_v070_signal,
    amq_f14_aftermarket_margin_quality_mfloor_5d_zlc_slpct126_v071_signal,
    amq_f14_aftermarket_margin_quality_mfloor_10d_zlc_slpct252_v072_signal,
    amq_f14_aftermarket_margin_quality_mfloor_21d_zlc_slpct5_v073_signal,
    amq_f14_aftermarket_margin_quality_mfloor_42d_zlc_slpct10_v074_signal,
    amq_f14_aftermarket_margin_quality_mfloor_63d_zlc_slpct21_v075_signal,
    amq_f14_aftermarket_margin_quality_mfloor_126d_zlc_slpct63_v076_signal,
    amq_f14_aftermarket_margin_quality_mfloor_252d_zlc_slpct126_v077_signal,
    amq_f14_aftermarket_margin_quality_mstab_5d_zlc_slpct252_v078_signal,
    amq_f14_aftermarket_margin_quality_mstab_10d_zlc_slpct5_v079_signal,
    amq_f14_aftermarket_margin_quality_mstab_21d_zlc_slpct10_v080_signal,
    amq_f14_aftermarket_margin_quality_mstab_42d_zlc_slpct21_v081_signal,
    amq_f14_aftermarket_margin_quality_mstab_63d_zlc_slpct63_v082_signal,
    amq_f14_aftermarket_margin_quality_mstab_126d_zlc_slpct126_v083_signal,
    amq_f14_aftermarket_margin_quality_mstab_252d_zlc_slpct252_v084_signal,
    amq_f14_aftermarket_margin_quality_mdur_5d_lmn_slpct5_v085_signal,
    amq_f14_aftermarket_margin_quality_mdur_10d_lmn_slpct10_v086_signal,
    amq_f14_aftermarket_margin_quality_mdur_21d_lmn_slpct21_v087_signal,
    amq_f14_aftermarket_margin_quality_mdur_42d_lmn_slpct63_v088_signal,
    amq_f14_aftermarket_margin_quality_mdur_63d_lmn_slpct126_v089_signal,
    amq_f14_aftermarket_margin_quality_mdur_126d_lmn_slpct252_v090_signal,
    amq_f14_aftermarket_margin_quality_mdur_252d_lmn_slpct5_v091_signal,
    amq_f14_aftermarket_margin_quality_mfloor_5d_lmn_slpct10_v092_signal,
    amq_f14_aftermarket_margin_quality_mfloor_10d_lmn_slpct21_v093_signal,
    amq_f14_aftermarket_margin_quality_mfloor_21d_lmn_slpct63_v094_signal,
    amq_f14_aftermarket_margin_quality_mfloor_42d_lmn_slpct126_v095_signal,
    amq_f14_aftermarket_margin_quality_mfloor_63d_lmn_slpct252_v096_signal,
    amq_f14_aftermarket_margin_quality_mfloor_126d_lmn_slpct5_v097_signal,
    amq_f14_aftermarket_margin_quality_mfloor_252d_lmn_slpct10_v098_signal,
    amq_f14_aftermarket_margin_quality_mstab_5d_lmn_slpct21_v099_signal,
    amq_f14_aftermarket_margin_quality_mstab_10d_lmn_slpct63_v100_signal,
    amq_f14_aftermarket_margin_quality_mstab_21d_lmn_slpct126_v101_signal,
    amq_f14_aftermarket_margin_quality_mstab_42d_lmn_slpct252_v102_signal,
    amq_f14_aftermarket_margin_quality_mstab_63d_lmn_slpct5_v103_signal,
    amq_f14_aftermarket_margin_quality_mstab_126d_lmn_slpct10_v104_signal,
    amq_f14_aftermarket_margin_quality_mstab_252d_lmn_slpct21_v105_signal,
    amq_f14_aftermarket_margin_quality_mdur_5d_ssq_slpct63_v106_signal,
    amq_f14_aftermarket_margin_quality_mdur_10d_ssq_slpct126_v107_signal,
    amq_f14_aftermarket_margin_quality_mdur_21d_ssq_slpct252_v108_signal,
    amq_f14_aftermarket_margin_quality_mdur_42d_ssq_slpct5_v109_signal,
    amq_f14_aftermarket_margin_quality_mdur_63d_ssq_slpct10_v110_signal,
    amq_f14_aftermarket_margin_quality_mdur_126d_ssq_slpct21_v111_signal,
    amq_f14_aftermarket_margin_quality_mdur_252d_ssq_slpct63_v112_signal,
    amq_f14_aftermarket_margin_quality_mfloor_5d_ssq_slpct126_v113_signal,
    amq_f14_aftermarket_margin_quality_mfloor_10d_ssq_slpct252_v114_signal,
    amq_f14_aftermarket_margin_quality_mfloor_21d_ssq_slpct5_v115_signal,
    amq_f14_aftermarket_margin_quality_mfloor_42d_ssq_slpct10_v116_signal,
    amq_f14_aftermarket_margin_quality_mfloor_63d_ssq_slpct21_v117_signal,
    amq_f14_aftermarket_margin_quality_mfloor_126d_ssq_slpct63_v118_signal,
    amq_f14_aftermarket_margin_quality_mfloor_252d_ssq_slpct126_v119_signal,
    amq_f14_aftermarket_margin_quality_mstab_5d_ssq_slpct252_v120_signal,
    amq_f14_aftermarket_margin_quality_mstab_10d_ssq_slpct5_v121_signal,
    amq_f14_aftermarket_margin_quality_mstab_21d_ssq_slpct10_v122_signal,
    amq_f14_aftermarket_margin_quality_mstab_42d_ssq_slpct21_v123_signal,
    amq_f14_aftermarket_margin_quality_mstab_63d_ssq_slpct63_v124_signal,
    amq_f14_aftermarket_margin_quality_mstab_126d_ssq_slpct126_v125_signal,
    amq_f14_aftermarket_margin_quality_mstab_252d_ssq_slpct252_v126_signal,
    amq_f14_aftermarket_margin_quality_mdur_5d_dxe_slpct5_v127_signal,
    amq_f14_aftermarket_margin_quality_mdur_10d_dxe_slpct10_v128_signal,
    amq_f14_aftermarket_margin_quality_mdur_21d_dxe_slpct21_v129_signal,
    amq_f14_aftermarket_margin_quality_mdur_42d_dxe_slpct63_v130_signal,
    amq_f14_aftermarket_margin_quality_mdur_63d_dxe_slpct126_v131_signal,
    amq_f14_aftermarket_margin_quality_mdur_126d_dxe_slpct252_v132_signal,
    amq_f14_aftermarket_margin_quality_mdur_252d_dxe_slpct5_v133_signal,
    amq_f14_aftermarket_margin_quality_mfloor_5d_dxe_slpct10_v134_signal,
    amq_f14_aftermarket_margin_quality_mfloor_10d_dxe_slpct21_v135_signal,
    amq_f14_aftermarket_margin_quality_mfloor_21d_dxe_slpct63_v136_signal,
    amq_f14_aftermarket_margin_quality_mfloor_42d_dxe_slpct126_v137_signal,
    amq_f14_aftermarket_margin_quality_mfloor_63d_dxe_slpct252_v138_signal,
    amq_f14_aftermarket_margin_quality_mfloor_126d_dxe_slpct5_v139_signal,
    amq_f14_aftermarket_margin_quality_mfloor_252d_dxe_slpct10_v140_signal,
    amq_f14_aftermarket_margin_quality_mstab_5d_dxe_slpct21_v141_signal,
    amq_f14_aftermarket_margin_quality_mstab_10d_dxe_slpct63_v142_signal,
    amq_f14_aftermarket_margin_quality_mstab_21d_dxe_slpct126_v143_signal,
    amq_f14_aftermarket_margin_quality_mstab_42d_dxe_slpct252_v144_signal,
    amq_f14_aftermarket_margin_quality_mstab_63d_dxe_slpct5_v145_signal,
    amq_f14_aftermarket_margin_quality_mstab_126d_dxe_slpct10_v146_signal,
    amq_f14_aftermarket_margin_quality_mstab_252d_dxe_slpct21_v147_signal,
    amq_f14_aftermarket_margin_quality_mdur_252d_em15_slpct63_v148_signal,
    amq_f14_aftermarket_margin_quality_mfloor_252d_dmlc2_slpct126_v149_signal,
    amq_f14_aftermarket_margin_quality_mstab_252d_zclc_slpct252_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_AFTERMARKET_MARGIN_QUALITY_REGISTRY_SLOPE_001_150 = REGISTRY
F14_AFTERMARKET_MARGIN_QUALITY_REGISTRY_SLOPE_001_150 = REGISTRY

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
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "deferredrev": deferredrev,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f14_margin_durability", "_f14_margin_floor", "_f14_margin_stability",)
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
    print(f"OK f14_aftermarket_margin_quality_2nd_derivatives_001_150_claude: {n_features} features pass")
