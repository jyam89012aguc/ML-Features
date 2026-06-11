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
def _f50_quality_composite(roic, fcf, revenue, w):
    fcf_yield = fcf / revenue.replace(0, np.nan)
    return roic.rolling(w, min_periods=max(1, w // 2)).mean() + fcf_yield.rolling(w, min_periods=max(1, w // 2)).mean()


def _f50_low_vol_high_growth(closeadj, revenue, w):
    vol = closeadj.pct_change().rolling(w, min_periods=max(1, w // 2)).std()
    growth = revenue.pct_change(w)
    return growth / vol.replace(0, np.nan)


def _f50_idiosyncratic_alpha_score(roic, fcf, ebitdamargin, w):
    return (roic.rolling(w, min_periods=max(1, w // 2)).mean()
            + ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
            + (fcf / fcf.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)) - 1.0)



def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_raw_base_v001_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_mean_base_v002_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_std_base_v003_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_z_base_v004_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_42d_raw_base_v005_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_42d_mean_base_v006_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_42d_std_base_v007_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_42d_z_base_v008_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_raw_base_v009_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_mean_base_v010_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_std_base_v011_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_z_base_v012_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_raw_base_v013_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_mean_base_v014_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_std_base_v015_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_z_base_v016_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_189d_raw_base_v017_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_189d_mean_base_v018_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_189d_std_base_v019_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_189d_z_base_v020_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 189)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_raw_base_v021_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_mean_base_v022_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_std_base_v023_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_z_base_v024_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_378d_raw_base_v025_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_378d_mean_base_v026_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 378)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_378d_std_base_v027_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 378)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_378d_z_base_v028_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 378)
    result = _z(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_raw_base_v029_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_mean_base_v030_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_std_base_v031_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_z_base_v032_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_21d_raw_base_v033_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_21d_mean_base_v034_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_21d_std_base_v035_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_21d_z_base_v036_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_42d_raw_base_v037_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_42d_mean_base_v038_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_42d_std_base_v039_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_42d_z_base_v040_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_63d_raw_base_v041_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_63d_mean_base_v042_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_63d_std_base_v043_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_63d_z_base_v044_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_126d_raw_base_v045_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_126d_mean_base_v046_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 126)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_126d_std_base_v047_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_126d_z_base_v048_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_189d_raw_base_v049_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_189d_mean_base_v050_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 189)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_189d_std_base_v051_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 189)
    result = _std(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_189d_z_base_v052_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 189)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_252d_raw_base_v053_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_252d_mean_base_v054_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_252d_std_base_v055_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_252d_z_base_v056_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_378d_raw_base_v057_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_378d_mean_base_v058_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 378)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_378d_std_base_v059_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 378)
    result = _std(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_378d_z_base_v060_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 378)
    result = _z(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_504d_raw_base_v061_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_504d_mean_base_v062_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_504d_std_base_v063_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 504)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_lvhg_504d_z_base_v064_signal(closeadj, revenue):
    base = _f50_low_vol_high_growth(closeadj, revenue, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_ialpha_21d_raw_base_v065_signal(roic, fcf, ebitdamargin, closeadj):
    base = _f50_idiosyncratic_alpha_score(roic, fcf, ebitdamargin, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_ialpha_21d_mean_base_v066_signal(roic, fcf, ebitdamargin, closeadj):
    base = _f50_idiosyncratic_alpha_score(roic, fcf, ebitdamargin, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_ialpha_21d_std_base_v067_signal(roic, fcf, ebitdamargin, closeadj):
    base = _f50_idiosyncratic_alpha_score(roic, fcf, ebitdamargin, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_ialpha_21d_z_base_v068_signal(roic, fcf, ebitdamargin, closeadj):
    base = _f50_idiosyncratic_alpha_score(roic, fcf, ebitdamargin, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_ialpha_42d_raw_base_v069_signal(roic, fcf, ebitdamargin, closeadj):
    base = _f50_idiosyncratic_alpha_score(roic, fcf, ebitdamargin, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_ialpha_42d_mean_base_v070_signal(roic, fcf, ebitdamargin, closeadj):
    base = _f50_idiosyncratic_alpha_score(roic, fcf, ebitdamargin, 42)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_ialpha_42d_std_base_v071_signal(roic, fcf, ebitdamargin, closeadj):
    base = _f50_idiosyncratic_alpha_score(roic, fcf, ebitdamargin, 42)
    result = _std(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_ialpha_42d_z_base_v072_signal(roic, fcf, ebitdamargin, closeadj):
    base = _f50_idiosyncratic_alpha_score(roic, fcf, ebitdamargin, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_ialpha_63d_raw_base_v073_signal(roic, fcf, ebitdamargin, closeadj):
    base = _f50_idiosyncratic_alpha_score(roic, fcf, ebitdamargin, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_ialpha_63d_mean_base_v074_signal(roic, fcf, ebitdamargin, closeadj):
    base = _f50_idiosyncratic_alpha_score(roic, fcf, ebitdamargin, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_ialpha_63d_std_base_v075_signal(roic, fcf, ebitdamargin, closeadj):
    base = _f50_idiosyncratic_alpha_score(roic, fcf, ebitdamargin, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_raw_base_v001_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_mean_base_v002_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_std_base_v003_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_z_base_v004_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_42d_raw_base_v005_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_42d_mean_base_v006_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_42d_std_base_v007_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_42d_z_base_v008_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_raw_base_v009_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_mean_base_v010_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_std_base_v011_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_z_base_v012_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_raw_base_v013_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_mean_base_v014_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_std_base_v015_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_z_base_v016_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_189d_raw_base_v017_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_189d_mean_base_v018_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_189d_std_base_v019_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_189d_z_base_v020_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_raw_base_v021_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_mean_base_v022_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_std_base_v023_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_z_base_v024_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_378d_raw_base_v025_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_378d_mean_base_v026_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_378d_std_base_v027_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_378d_z_base_v028_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_raw_base_v029_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_mean_base_v030_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_std_base_v031_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_z_base_v032_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_21d_raw_base_v033_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_21d_mean_base_v034_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_21d_std_base_v035_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_21d_z_base_v036_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_42d_raw_base_v037_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_42d_mean_base_v038_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_42d_std_base_v039_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_42d_z_base_v040_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_63d_raw_base_v041_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_63d_mean_base_v042_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_63d_std_base_v043_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_63d_z_base_v044_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_126d_raw_base_v045_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_126d_mean_base_v046_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_126d_std_base_v047_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_126d_z_base_v048_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_189d_raw_base_v049_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_189d_mean_base_v050_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_189d_std_base_v051_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_189d_z_base_v052_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_252d_raw_base_v053_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_252d_mean_base_v054_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_252d_std_base_v055_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_252d_z_base_v056_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_378d_raw_base_v057_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_378d_mean_base_v058_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_378d_std_base_v059_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_378d_z_base_v060_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_504d_raw_base_v061_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_504d_mean_base_v062_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_504d_std_base_v063_signal,
    f50cda_f50_cd_idiosyncratic_alpha_lvhg_504d_z_base_v064_signal,
    f50cda_f50_cd_idiosyncratic_alpha_ialpha_21d_raw_base_v065_signal,
    f50cda_f50_cd_idiosyncratic_alpha_ialpha_21d_mean_base_v066_signal,
    f50cda_f50_cd_idiosyncratic_alpha_ialpha_21d_std_base_v067_signal,
    f50cda_f50_cd_idiosyncratic_alpha_ialpha_21d_z_base_v068_signal,
    f50cda_f50_cd_idiosyncratic_alpha_ialpha_42d_raw_base_v069_signal,
    f50cda_f50_cd_idiosyncratic_alpha_ialpha_42d_mean_base_v070_signal,
    f50cda_f50_cd_idiosyncratic_alpha_ialpha_42d_std_base_v071_signal,
    f50cda_f50_cd_idiosyncratic_alpha_ialpha_42d_z_base_v072_signal,
    f50cda_f50_cd_idiosyncratic_alpha_ialpha_63d_raw_base_v073_signal,
    f50cda_f50_cd_idiosyncratic_alpha_ialpha_63d_mean_base_v074_signal,
    f50cda_f50_cd_idiosyncratic_alpha_ialpha_63d_std_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_CD_IDIOSYNCRATIC_ALPHA_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")

    cols = {"closeadj": closeadj, "ebitdamargin": ebitdamargin, "fcf": fcf, "revenue": revenue, "roic": roic}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f50_quality_composite", "_f50_low_vol_high_growth", "_f50_idiosyncratic_alpha_score")
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
    print(f"OK f50_cd_idiosyncratic_alpha_base_001_075_claude: {n_features} features pass")
