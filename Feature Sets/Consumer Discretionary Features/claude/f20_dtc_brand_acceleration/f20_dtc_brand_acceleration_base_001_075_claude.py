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
def _f20_dtc_growth_signature(revenue, grossmargin, w):
    rg = revenue.pct_change(periods=w)
    gm = grossmargin - grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return rg * gm


def _f20_brand_acceleration(revenue, w):
    rg = revenue.pct_change(periods=w)
    return rg - rg.rolling(w, min_periods=max(1, w // 2)).mean()


def _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, w):
    rg = revenue.pct_change(periods=w)
    gm = grossmargin - grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    em = ebitdamargin - ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return rg * (gm + em)


def f20dba_f20_dtc_brand_acceleration_dtcsig_raw_21d_base_v001_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 21)
    base = ds
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_raw_63d_base_v002_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 63)
    base = ds
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_raw_126d_base_v003_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 126)
    base = ds
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_raw_189d_base_v004_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 189)
    base = ds
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_raw_252d_base_v005_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 252)
    base = ds
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_raw_378d_base_v006_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 378)
    base = ds
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_21d_base_v007_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 21)
    base = _mean(ds, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_63d_base_v008_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 63)
    base = _mean(ds, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_126d_base_v009_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 126)
    base = _mean(ds, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_189d_base_v010_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 189)
    base = _mean(ds, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_252d_base_v011_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 252)
    base = _mean(ds, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_378d_base_v012_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 378)
    base = _mean(ds, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_21d_base_v013_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 21)
    base = _std(ds, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_63d_base_v014_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 63)
    base = _std(ds, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_126d_base_v015_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 126)
    base = _std(ds, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_189d_base_v016_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 189)
    base = _std(ds, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_252d_base_v017_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 252)
    base = _std(ds, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_378d_base_v018_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 378)
    base = _std(ds, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_z_21d_base_v019_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 21)
    base = _z(ds, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_z_63d_base_v020_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 63)
    base = _z(ds, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_z_126d_base_v021_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 126)
    base = _z(ds, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_z_189d_base_v022_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 189)
    base = _z(ds, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_z_252d_base_v023_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 252)
    base = _z(ds, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_z_378d_base_v024_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 378)
    base = _z(ds, 756)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_diff_21d_base_v025_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 21)
    base = ds - ds.shift(21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_diff_63d_base_v026_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 63)
    base = ds - ds.shift(63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_diff_126d_base_v027_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 126)
    base = ds - ds.shift(126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_diff_189d_base_v028_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 189)
    base = ds - ds.shift(189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_diff_252d_base_v029_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 252)
    base = ds - ds.shift(252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_diff_378d_base_v030_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 378)
    base = ds - ds.shift(378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_raw_21d_base_v031_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 21)
    base = ba
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_raw_63d_base_v032_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 63)
    base = ba
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_raw_126d_base_v033_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 126)
    base = ba
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_raw_189d_base_v034_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 189)
    base = ba
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_raw_252d_base_v035_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 252)
    base = ba
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_raw_378d_base_v036_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 378)
    base = ba
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_rmean_21d_base_v037_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 21)
    base = _mean(ba, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_rmean_63d_base_v038_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 63)
    base = _mean(ba, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_rmean_126d_base_v039_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 126)
    base = _mean(ba, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_rmean_189d_base_v040_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 189)
    base = _mean(ba, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_rmean_252d_base_v041_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 252)
    base = _mean(ba, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_rmean_378d_base_v042_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 378)
    base = _mean(ba, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_z_21d_base_v043_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 21)
    base = _z(ba, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_z_63d_base_v044_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 63)
    base = _z(ba, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_z_126d_base_v045_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 126)
    base = _z(ba, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_z_189d_base_v046_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 189)
    base = _z(ba, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_z_252d_base_v047_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 252)
    base = _z(ba, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_z_378d_base_v048_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 378)
    base = _z(ba, 756)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_sq_21d_base_v049_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 21)
    base = ba * ba.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_sq_63d_base_v050_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 63)
    base = ba * ba.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_sq_126d_base_v051_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 126)
    base = ba * ba.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_sq_189d_base_v052_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 189)
    base = ba * ba.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_sq_252d_base_v053_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 252)
    base = ba * ba.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_sq_378d_base_v054_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 378)
    base = ba * ba.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_absx_21d_base_v055_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 21)
    base = ba.abs() * np.sign(ba)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_absx_63d_base_v056_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 63)
    base = ba.abs() * np.sign(ba)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_absx_126d_base_v057_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 126)
    base = ba.abs() * np.sign(ba)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_absx_189d_base_v058_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 189)
    base = ba.abs() * np.sign(ba)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_absx_252d_base_v059_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 252)
    base = ba.abs() * np.sign(ba)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_absx_378d_base_v060_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 378)
    base = ba.abs() * np.sign(ba)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_raw_21d_base_v061_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 21)
    base = qs
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_raw_63d_base_v062_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 63)
    base = qs
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_raw_126d_base_v063_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 126)
    base = qs
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_raw_189d_base_v064_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 189)
    base = qs
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_raw_252d_base_v065_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 252)
    base = qs
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_raw_378d_base_v066_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 378)
    base = qs
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_21d_base_v067_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 21)
    base = _mean(qs, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_63d_base_v068_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 63)
    base = _mean(qs, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_126d_base_v069_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 126)
    base = _mean(qs, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_189d_base_v070_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 189)
    base = _mean(qs, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_252d_base_v071_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 252)
    base = _mean(qs, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_378d_base_v072_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 378)
    base = _mean(qs, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_z_21d_base_v073_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 21)
    base = _z(qs, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_z_63d_base_v074_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 63)
    base = _z(qs, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_z_126d_base_v075_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 126)
    base = _z(qs, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20dba_f20_dtc_brand_acceleration_dtcsig_raw_21d_base_v001_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_raw_63d_base_v002_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_raw_126d_base_v003_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_raw_189d_base_v004_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_raw_252d_base_v005_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_raw_378d_base_v006_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_21d_base_v007_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_63d_base_v008_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_126d_base_v009_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_189d_base_v010_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_252d_base_v011_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_378d_base_v012_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_21d_base_v013_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_63d_base_v014_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_126d_base_v015_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_189d_base_v016_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_252d_base_v017_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_378d_base_v018_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_z_21d_base_v019_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_z_63d_base_v020_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_z_126d_base_v021_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_z_189d_base_v022_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_z_252d_base_v023_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_z_378d_base_v024_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_diff_21d_base_v025_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_diff_63d_base_v026_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_diff_126d_base_v027_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_diff_189d_base_v028_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_diff_252d_base_v029_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_diff_378d_base_v030_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_raw_21d_base_v031_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_raw_63d_base_v032_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_raw_126d_base_v033_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_raw_189d_base_v034_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_raw_252d_base_v035_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_raw_378d_base_v036_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_rmean_21d_base_v037_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_rmean_63d_base_v038_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_rmean_126d_base_v039_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_rmean_189d_base_v040_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_rmean_252d_base_v041_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_rmean_378d_base_v042_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_z_21d_base_v043_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_z_63d_base_v044_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_z_126d_base_v045_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_z_189d_base_v046_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_z_252d_base_v047_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_z_378d_base_v048_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_sq_21d_base_v049_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_sq_63d_base_v050_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_sq_126d_base_v051_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_sq_189d_base_v052_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_sq_252d_base_v053_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_sq_378d_base_v054_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_absx_21d_base_v055_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_absx_63d_base_v056_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_absx_126d_base_v057_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_absx_189d_base_v058_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_absx_252d_base_v059_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_absx_378d_base_v060_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_raw_21d_base_v061_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_raw_63d_base_v062_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_raw_126d_base_v063_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_raw_189d_base_v064_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_raw_252d_base_v065_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_raw_378d_base_v066_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_21d_base_v067_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_63d_base_v068_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_126d_base_v069_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_189d_base_v070_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_252d_base_v071_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_378d_base_v072_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_z_21d_base_v073_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_z_63d_base_v074_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_z_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FDTC_BRAND_ACCELERATION_REGISTRY_001_075 = REGISTRY


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
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "sgna": sgna, "opex": opex,
        "gp": gp, "workingcapital": workingcapital,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f20_dtc_growth_signature", "_f20_brand_acceleration", "_f20_dtc_quality_score",)
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
    print(f"OK f20_dtc_brand_acceleration_base_001_075_claude: {n_features} features pass")
