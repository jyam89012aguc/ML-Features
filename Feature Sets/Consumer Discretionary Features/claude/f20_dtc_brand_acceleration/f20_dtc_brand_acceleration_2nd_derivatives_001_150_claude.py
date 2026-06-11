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


def f20dba_f20_dtc_brand_acceleration_dtcsig_raw_21d_slope_v001_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 21)
    base = ds
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_raw_63d_slope_v002_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 63)
    base = ds
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_raw_126d_slope_v003_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 126)
    base = ds
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_raw_189d_slope_v004_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 189)
    base = ds
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_raw_252d_slope_v005_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 252)
    base = ds
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_raw_378d_slope_v006_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 378)
    base = ds
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_21d_slope_v007_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 21)
    base = _mean(ds, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_63d_slope_v008_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 63)
    base = _mean(ds, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_126d_slope_v009_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 126)
    base = _mean(ds, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_189d_slope_v010_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 189)
    base = _mean(ds, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_252d_slope_v011_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 252)
    base = _mean(ds, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_378d_slope_v012_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 378)
    base = _mean(ds, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_21d_slope_v013_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 21)
    base = _std(ds, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_63d_slope_v014_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 63)
    base = _std(ds, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_126d_slope_v015_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 126)
    base = _std(ds, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_189d_slope_v016_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 189)
    base = _std(ds, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_252d_slope_v017_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 252)
    base = _std(ds, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_378d_slope_v018_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 378)
    base = _std(ds, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_z_21d_slope_v019_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 21)
    base = _z(ds, 63)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_z_63d_slope_v020_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 63)
    base = _z(ds, 126)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_z_126d_slope_v021_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 126)
    base = _z(ds, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_z_189d_slope_v022_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 189)
    base = _z(ds, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_z_252d_slope_v023_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 252)
    base = _z(ds, 504)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_z_378d_slope_v024_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 378)
    base = _z(ds, 756)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_diff_21d_slope_v025_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 21)
    base = ds - ds.shift(21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_diff_63d_slope_v026_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 63)
    base = ds - ds.shift(63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_diff_126d_slope_v027_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 126)
    base = ds - ds.shift(126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_diff_189d_slope_v028_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 189)
    base = ds - ds.shift(189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_diff_252d_slope_v029_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 252)
    base = ds - ds.shift(252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcsig_diff_378d_slope_v030_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 378)
    base = ds - ds.shift(378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_raw_21d_slope_v031_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 21)
    base = ba
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_raw_63d_slope_v032_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 63)
    base = ba
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_raw_126d_slope_v033_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 126)
    base = ba
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_raw_189d_slope_v034_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 189)
    base = ba
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_raw_252d_slope_v035_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 252)
    base = ba
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_raw_378d_slope_v036_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 378)
    base = ba
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_rmean_21d_slope_v037_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 21)
    base = _mean(ba, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_rmean_63d_slope_v038_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 63)
    base = _mean(ba, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_rmean_126d_slope_v039_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 126)
    base = _mean(ba, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_rmean_189d_slope_v040_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 189)
    base = _mean(ba, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_rmean_252d_slope_v041_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 252)
    base = _mean(ba, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_rmean_378d_slope_v042_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 378)
    base = _mean(ba, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_z_21d_slope_v043_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 21)
    base = _z(ba, 63)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_z_63d_slope_v044_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 63)
    base = _z(ba, 126)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_z_126d_slope_v045_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 126)
    base = _z(ba, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_z_189d_slope_v046_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 189)
    base = _z(ba, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_z_252d_slope_v047_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 252)
    base = _z(ba, 504)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_z_378d_slope_v048_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 378)
    base = _z(ba, 756)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_sq_21d_slope_v049_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 21)
    base = ba * ba.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_sq_63d_slope_v050_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 63)
    base = ba * ba.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_sq_126d_slope_v051_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 126)
    base = ba * ba.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_sq_189d_slope_v052_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 189)
    base = ba * ba.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_sq_252d_slope_v053_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 252)
    base = ba * ba.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_sq_378d_slope_v054_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 378)
    base = ba * ba.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_absx_21d_slope_v055_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 21)
    base = ba.abs() * np.sign(ba)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_absx_63d_slope_v056_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 63)
    base = ba.abs() * np.sign(ba)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_absx_126d_slope_v057_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 126)
    base = ba.abs() * np.sign(ba)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_absx_189d_slope_v058_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 189)
    base = ba.abs() * np.sign(ba)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_absx_252d_slope_v059_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 252)
    base = ba.abs() * np.sign(ba)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_brandacc_absx_378d_slope_v060_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 378)
    base = ba.abs() * np.sign(ba)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_raw_21d_slope_v061_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 21)
    base = qs
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_raw_63d_slope_v062_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 63)
    base = qs
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_raw_126d_slope_v063_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 126)
    base = qs
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_raw_189d_slope_v064_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 189)
    base = qs
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_raw_252d_slope_v065_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 252)
    base = qs
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_raw_378d_slope_v066_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 378)
    base = qs
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_21d_slope_v067_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 21)
    base = _mean(qs, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_63d_slope_v068_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 63)
    base = _mean(qs, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_126d_slope_v069_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 126)
    base = _mean(qs, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_189d_slope_v070_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 189)
    base = _mean(qs, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_252d_slope_v071_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 252)
    base = _mean(qs, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_378d_slope_v072_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 378)
    base = _mean(qs, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_z_21d_slope_v073_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 21)
    base = _z(qs, 63)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_z_63d_slope_v074_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 63)
    base = _z(qs, 126)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_z_126d_slope_v075_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 126)
    base = _z(qs, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_z_189d_slope_v076_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 189)
    base = _z(qs, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_z_252d_slope_v077_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 252)
    base = _z(qs, 504)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_z_378d_slope_v078_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 378)
    base = _z(qs, 756)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_sq_21d_slope_v079_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 21)
    base = qs * qs.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_sq_63d_slope_v080_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 63)
    base = qs * qs.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_sq_126d_slope_v081_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 126)
    base = qs * qs.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_sq_189d_slope_v082_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 189)
    base = qs * qs.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_sq_252d_slope_v083_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 252)
    base = qs * qs.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_sq_378d_slope_v084_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 378)
    base = qs * qs.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rstd_21d_slope_v085_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 21)
    base = _std(qs, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rstd_63d_slope_v086_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 63)
    base = _std(qs, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rstd_126d_slope_v087_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 126)
    base = _std(qs, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rstd_189d_slope_v088_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 189)
    base = _std(qs, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rstd_252d_slope_v089_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 252)
    base = _std(qs, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dtcqual_rstd_378d_slope_v090_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 378)
    base = _std(qs, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dsxba_mul_10d_slope_v091_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 10)
    ba = _f20_brand_acceleration(revenue, 10)
    base = ds * ba
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dsxba_mul_21d_slope_v092_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 21)
    ba = _f20_brand_acceleration(revenue, 21)
    base = ds * ba
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dsxba_mul_42d_slope_v093_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 42)
    ba = _f20_brand_acceleration(revenue, 42)
    base = ds * ba
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dsxba_mul_63d_slope_v094_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 63)
    ba = _f20_brand_acceleration(revenue, 63)
    base = ds * ba
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dsxba_mul_126d_slope_v095_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 126)
    ba = _f20_brand_acceleration(revenue, 126)
    base = ds * ba
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dsxba_mul_189d_slope_v096_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 189)
    ba = _f20_brand_acceleration(revenue, 189)
    base = ds * ba
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dspqs_sum_10d_slope_v097_signal(revenue, grossmargin, ebitdamargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 10)
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 10)
    base = ds + qs
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dspqs_sum_21d_slope_v098_signal(revenue, grossmargin, ebitdamargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 21)
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 21)
    base = ds + qs
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dspqs_sum_42d_slope_v099_signal(revenue, grossmargin, ebitdamargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 42)
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 42)
    base = ds + qs
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dspqs_sum_63d_slope_v100_signal(revenue, grossmargin, ebitdamargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 63)
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 63)
    base = ds + qs
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dspqs_sum_126d_slope_v101_signal(revenue, grossmargin, ebitdamargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 126)
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 126)
    base = ds + qs
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_dspqs_sum_189d_slope_v102_signal(revenue, grossmargin, ebitdamargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 189)
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 189)
    base = ds + qs
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_bamqs_diff_10d_slope_v103_signal(revenue, grossmargin, ebitdamargin, closeadj):
    ba = _f20_brand_acceleration(revenue, 10)
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 10)
    base = ba - qs
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_bamqs_diff_21d_slope_v104_signal(revenue, grossmargin, ebitdamargin, closeadj):
    ba = _f20_brand_acceleration(revenue, 21)
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 21)
    base = ba - qs
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_bamqs_diff_42d_slope_v105_signal(revenue, grossmargin, ebitdamargin, closeadj):
    ba = _f20_brand_acceleration(revenue, 42)
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 42)
    base = ba - qs
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_bamqs_diff_63d_slope_v106_signal(revenue, grossmargin, ebitdamargin, closeadj):
    ba = _f20_brand_acceleration(revenue, 63)
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 63)
    base = ba - qs
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_bamqs_diff_126d_slope_v107_signal(revenue, grossmargin, ebitdamargin, closeadj):
    ba = _f20_brand_acceleration(revenue, 126)
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 126)
    base = ba - qs
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_bamqs_diff_189d_slope_v108_signal(revenue, grossmargin, ebitdamargin, closeadj):
    ba = _f20_brand_acceleration(revenue, 189)
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 189)
    base = ba - qs
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_mxs_10d_slope_v109_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 10)
    base = _mean(ds, 10) * _std(ds, 10)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_mxs_21d_slope_v110_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 21)
    base = _mean(ds, 21) * _std(ds, 21)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_mxs_42d_slope_v111_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 42)
    base = _mean(ds, 42) * _std(ds, 42)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_mxs_63d_slope_v112_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 63)
    base = _mean(ds, 63) * _std(ds, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_mxs_126d_slope_v113_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 126)
    base = _mean(ds, 126) * _std(ds, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_mxs_189d_slope_v114_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 189)
    base = _mean(ds, 189) * _std(ds, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ba_dsmooth_10d_slope_v115_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 10)
    base = ba.diff(10).rolling(10, min_periods=max(1,10//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ba_dsmooth_21d_slope_v116_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 21)
    base = ba.diff(21).rolling(21, min_periods=max(1,21//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ba_dsmooth_42d_slope_v117_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 42)
    base = ba.diff(42).rolling(42, min_periods=max(1,42//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ba_dsmooth_63d_slope_v118_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 63)
    base = ba.diff(63).rolling(63, min_periods=max(1,63//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ba_dsmooth_126d_slope_v119_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 126)
    base = ba.diff(126).rolling(126, min_periods=max(1,126//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ba_dsmooth_189d_slope_v120_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 189)
    base = ba.diff(189).rolling(189, min_periods=max(1,189//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_ema_10d_slope_v121_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 10)
    base = ds.ewm(span=10, min_periods=max(1, 10//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_ema_21d_slope_v122_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 21)
    base = ds.ewm(span=21, min_periods=max(1, 21//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_ema_42d_slope_v123_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 42)
    base = ds.ewm(span=42, min_periods=max(1, 42//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_ema_63d_slope_v124_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 63)
    base = ds.ewm(span=63, min_periods=max(1, 63//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_ema_126d_slope_v125_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 126)
    base = ds.ewm(span=126, min_periods=max(1, 126//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_ema_189d_slope_v126_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 189)
    base = ds.ewm(span=189, min_periods=max(1, 189//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_qs_range_10d_slope_v127_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 10)
    base = qs.rolling(10, min_periods=max(1, 10//2)).max() - qs.rolling(10, min_periods=max(1, 10//2)).min()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_qs_range_21d_slope_v128_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 21)
    base = qs.rolling(21, min_periods=max(1, 21//2)).max() - qs.rolling(21, min_periods=max(1, 21//2)).min()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_qs_range_42d_slope_v129_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 42)
    base = qs.rolling(42, min_periods=max(1, 42//2)).max() - qs.rolling(42, min_periods=max(1, 42//2)).min()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_qs_range_63d_slope_v130_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 63)
    base = qs.rolling(63, min_periods=max(1, 63//2)).max() - qs.rolling(63, min_periods=max(1, 63//2)).min()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_qs_range_126d_slope_v131_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 126)
    base = qs.rolling(126, min_periods=max(1, 126//2)).max() - qs.rolling(126, min_periods=max(1, 126//2)).min()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_qs_range_189d_slope_v132_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 189)
    base = qs.rolling(189, min_periods=max(1, 189//2)).max() - qs.rolling(189, min_periods=max(1, 189//2)).min()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ba_dmed_10d_slope_v133_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 10)
    base = (ba - ba.rolling(10, min_periods=max(1, 10//2)).median())
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ba_dmed_21d_slope_v134_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 21)
    base = (ba - ba.rolling(21, min_periods=max(1, 21//2)).median())
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ba_dmed_42d_slope_v135_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 42)
    base = (ba - ba.rolling(42, min_periods=max(1, 42//2)).median())
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ba_dmed_63d_slope_v136_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 63)
    base = (ba - ba.rolling(63, min_periods=max(1, 63//2)).median())
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ba_dmed_126d_slope_v137_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 126)
    base = (ba - ba.rolling(126, min_periods=max(1, 126//2)).median())
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ba_dmed_189d_slope_v138_signal(revenue, closeadj):
    ba = _f20_brand_acceleration(revenue, 189)
    base = (ba - ba.rolling(189, min_periods=max(1, 189//2)).median())
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_iqr_10d_slope_v139_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 10)
    base = ds.rolling(10, min_periods=max(1, 10//2)).quantile(0.75) - ds.rolling(10, min_periods=max(1, 10//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_iqr_21d_slope_v140_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 21)
    base = ds.rolling(21, min_periods=max(1, 21//2)).quantile(0.75) - ds.rolling(21, min_periods=max(1, 21//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_iqr_42d_slope_v141_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 42)
    base = ds.rolling(42, min_periods=max(1, 42//2)).quantile(0.75) - ds.rolling(42, min_periods=max(1, 42//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_iqr_63d_slope_v142_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 63)
    base = ds.rolling(63, min_periods=max(1, 63//2)).quantile(0.75) - ds.rolling(63, min_periods=max(1, 63//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_iqr_126d_slope_v143_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 126)
    base = ds.rolling(126, min_periods=max(1, 126//2)).quantile(0.75) - ds.rolling(126, min_periods=max(1, 126//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_ds_iqr_189d_slope_v144_signal(revenue, grossmargin, closeadj):
    ds = _f20_dtc_growth_signature(revenue, grossmargin, 189)
    base = ds.rolling(189, min_periods=max(1, 189//2)).quantile(0.75) - ds.rolling(189, min_periods=max(1, 189//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_qs_iqr_10d_slope_v145_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 10)
    base = qs.rolling(10, min_periods=max(1, 10//2)).quantile(0.75) - qs.rolling(10, min_periods=max(1, 10//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_qs_iqr_21d_slope_v146_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 21)
    base = qs.rolling(21, min_periods=max(1, 21//2)).quantile(0.75) - qs.rolling(21, min_periods=max(1, 21//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_qs_iqr_42d_slope_v147_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 42)
    base = qs.rolling(42, min_periods=max(1, 42//2)).quantile(0.75) - qs.rolling(42, min_periods=max(1, 42//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_qs_iqr_63d_slope_v148_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 63)
    base = qs.rolling(63, min_periods=max(1, 63//2)).quantile(0.75) - qs.rolling(63, min_periods=max(1, 63//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_qs_iqr_126d_slope_v149_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 126)
    base = qs.rolling(126, min_periods=max(1, 126//2)).quantile(0.75) - qs.rolling(126, min_periods=max(1, 126//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f20dba_f20_dtc_brand_acceleration_qs_iqr_189d_slope_v150_signal(revenue, grossmargin, ebitdamargin, closeadj):
    qs = _f20_dtc_quality_score(revenue, grossmargin, ebitdamargin, 189)
    base = qs.rolling(189, min_periods=max(1, 189//2)).quantile(0.75) - qs.rolling(189, min_periods=max(1, 189//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20dba_f20_dtc_brand_acceleration_dtcsig_raw_21d_slope_v001_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_raw_63d_slope_v002_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_raw_126d_slope_v003_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_raw_189d_slope_v004_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_raw_252d_slope_v005_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_raw_378d_slope_v006_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_21d_slope_v007_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_63d_slope_v008_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_126d_slope_v009_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_189d_slope_v010_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_252d_slope_v011_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rmean_378d_slope_v012_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_21d_slope_v013_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_63d_slope_v014_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_126d_slope_v015_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_189d_slope_v016_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_252d_slope_v017_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_rstd_378d_slope_v018_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_z_21d_slope_v019_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_z_63d_slope_v020_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_z_126d_slope_v021_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_z_189d_slope_v022_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_z_252d_slope_v023_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_z_378d_slope_v024_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_diff_21d_slope_v025_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_diff_63d_slope_v026_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_diff_126d_slope_v027_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_diff_189d_slope_v028_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_diff_252d_slope_v029_signal,
    f20dba_f20_dtc_brand_acceleration_dtcsig_diff_378d_slope_v030_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_raw_21d_slope_v031_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_raw_63d_slope_v032_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_raw_126d_slope_v033_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_raw_189d_slope_v034_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_raw_252d_slope_v035_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_raw_378d_slope_v036_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_rmean_21d_slope_v037_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_rmean_63d_slope_v038_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_rmean_126d_slope_v039_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_rmean_189d_slope_v040_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_rmean_252d_slope_v041_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_rmean_378d_slope_v042_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_z_21d_slope_v043_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_z_63d_slope_v044_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_z_126d_slope_v045_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_z_189d_slope_v046_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_z_252d_slope_v047_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_z_378d_slope_v048_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_sq_21d_slope_v049_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_sq_63d_slope_v050_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_sq_126d_slope_v051_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_sq_189d_slope_v052_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_sq_252d_slope_v053_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_sq_378d_slope_v054_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_absx_21d_slope_v055_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_absx_63d_slope_v056_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_absx_126d_slope_v057_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_absx_189d_slope_v058_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_absx_252d_slope_v059_signal,
    f20dba_f20_dtc_brand_acceleration_brandacc_absx_378d_slope_v060_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_raw_21d_slope_v061_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_raw_63d_slope_v062_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_raw_126d_slope_v063_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_raw_189d_slope_v064_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_raw_252d_slope_v065_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_raw_378d_slope_v066_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_21d_slope_v067_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_63d_slope_v068_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_126d_slope_v069_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_189d_slope_v070_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_252d_slope_v071_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rmean_378d_slope_v072_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_z_21d_slope_v073_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_z_63d_slope_v074_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_z_126d_slope_v075_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_z_189d_slope_v076_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_z_252d_slope_v077_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_z_378d_slope_v078_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_sq_21d_slope_v079_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_sq_63d_slope_v080_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_sq_126d_slope_v081_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_sq_189d_slope_v082_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_sq_252d_slope_v083_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_sq_378d_slope_v084_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rstd_21d_slope_v085_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rstd_63d_slope_v086_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rstd_126d_slope_v087_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rstd_189d_slope_v088_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rstd_252d_slope_v089_signal,
    f20dba_f20_dtc_brand_acceleration_dtcqual_rstd_378d_slope_v090_signal,
    f20dba_f20_dtc_brand_acceleration_dsxba_mul_10d_slope_v091_signal,
    f20dba_f20_dtc_brand_acceleration_dsxba_mul_21d_slope_v092_signal,
    f20dba_f20_dtc_brand_acceleration_dsxba_mul_42d_slope_v093_signal,
    f20dba_f20_dtc_brand_acceleration_dsxba_mul_63d_slope_v094_signal,
    f20dba_f20_dtc_brand_acceleration_dsxba_mul_126d_slope_v095_signal,
    f20dba_f20_dtc_brand_acceleration_dsxba_mul_189d_slope_v096_signal,
    f20dba_f20_dtc_brand_acceleration_dspqs_sum_10d_slope_v097_signal,
    f20dba_f20_dtc_brand_acceleration_dspqs_sum_21d_slope_v098_signal,
    f20dba_f20_dtc_brand_acceleration_dspqs_sum_42d_slope_v099_signal,
    f20dba_f20_dtc_brand_acceleration_dspqs_sum_63d_slope_v100_signal,
    f20dba_f20_dtc_brand_acceleration_dspqs_sum_126d_slope_v101_signal,
    f20dba_f20_dtc_brand_acceleration_dspqs_sum_189d_slope_v102_signal,
    f20dba_f20_dtc_brand_acceleration_bamqs_diff_10d_slope_v103_signal,
    f20dba_f20_dtc_brand_acceleration_bamqs_diff_21d_slope_v104_signal,
    f20dba_f20_dtc_brand_acceleration_bamqs_diff_42d_slope_v105_signal,
    f20dba_f20_dtc_brand_acceleration_bamqs_diff_63d_slope_v106_signal,
    f20dba_f20_dtc_brand_acceleration_bamqs_diff_126d_slope_v107_signal,
    f20dba_f20_dtc_brand_acceleration_bamqs_diff_189d_slope_v108_signal,
    f20dba_f20_dtc_brand_acceleration_ds_mxs_10d_slope_v109_signal,
    f20dba_f20_dtc_brand_acceleration_ds_mxs_21d_slope_v110_signal,
    f20dba_f20_dtc_brand_acceleration_ds_mxs_42d_slope_v111_signal,
    f20dba_f20_dtc_brand_acceleration_ds_mxs_63d_slope_v112_signal,
    f20dba_f20_dtc_brand_acceleration_ds_mxs_126d_slope_v113_signal,
    f20dba_f20_dtc_brand_acceleration_ds_mxs_189d_slope_v114_signal,
    f20dba_f20_dtc_brand_acceleration_ba_dsmooth_10d_slope_v115_signal,
    f20dba_f20_dtc_brand_acceleration_ba_dsmooth_21d_slope_v116_signal,
    f20dba_f20_dtc_brand_acceleration_ba_dsmooth_42d_slope_v117_signal,
    f20dba_f20_dtc_brand_acceleration_ba_dsmooth_63d_slope_v118_signal,
    f20dba_f20_dtc_brand_acceleration_ba_dsmooth_126d_slope_v119_signal,
    f20dba_f20_dtc_brand_acceleration_ba_dsmooth_189d_slope_v120_signal,
    f20dba_f20_dtc_brand_acceleration_ds_ema_10d_slope_v121_signal,
    f20dba_f20_dtc_brand_acceleration_ds_ema_21d_slope_v122_signal,
    f20dba_f20_dtc_brand_acceleration_ds_ema_42d_slope_v123_signal,
    f20dba_f20_dtc_brand_acceleration_ds_ema_63d_slope_v124_signal,
    f20dba_f20_dtc_brand_acceleration_ds_ema_126d_slope_v125_signal,
    f20dba_f20_dtc_brand_acceleration_ds_ema_189d_slope_v126_signal,
    f20dba_f20_dtc_brand_acceleration_qs_range_10d_slope_v127_signal,
    f20dba_f20_dtc_brand_acceleration_qs_range_21d_slope_v128_signal,
    f20dba_f20_dtc_brand_acceleration_qs_range_42d_slope_v129_signal,
    f20dba_f20_dtc_brand_acceleration_qs_range_63d_slope_v130_signal,
    f20dba_f20_dtc_brand_acceleration_qs_range_126d_slope_v131_signal,
    f20dba_f20_dtc_brand_acceleration_qs_range_189d_slope_v132_signal,
    f20dba_f20_dtc_brand_acceleration_ba_dmed_10d_slope_v133_signal,
    f20dba_f20_dtc_brand_acceleration_ba_dmed_21d_slope_v134_signal,
    f20dba_f20_dtc_brand_acceleration_ba_dmed_42d_slope_v135_signal,
    f20dba_f20_dtc_brand_acceleration_ba_dmed_63d_slope_v136_signal,
    f20dba_f20_dtc_brand_acceleration_ba_dmed_126d_slope_v137_signal,
    f20dba_f20_dtc_brand_acceleration_ba_dmed_189d_slope_v138_signal,
    f20dba_f20_dtc_brand_acceleration_ds_iqr_10d_slope_v139_signal,
    f20dba_f20_dtc_brand_acceleration_ds_iqr_21d_slope_v140_signal,
    f20dba_f20_dtc_brand_acceleration_ds_iqr_42d_slope_v141_signal,
    f20dba_f20_dtc_brand_acceleration_ds_iqr_63d_slope_v142_signal,
    f20dba_f20_dtc_brand_acceleration_ds_iqr_126d_slope_v143_signal,
    f20dba_f20_dtc_brand_acceleration_ds_iqr_189d_slope_v144_signal,
    f20dba_f20_dtc_brand_acceleration_qs_iqr_10d_slope_v145_signal,
    f20dba_f20_dtc_brand_acceleration_qs_iqr_21d_slope_v146_signal,
    f20dba_f20_dtc_brand_acceleration_qs_iqr_42d_slope_v147_signal,
    f20dba_f20_dtc_brand_acceleration_qs_iqr_63d_slope_v148_signal,
    f20dba_f20_dtc_brand_acceleration_qs_iqr_126d_slope_v149_signal,
    f20dba_f20_dtc_brand_acceleration_qs_iqr_189d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FDTC_BRAND_ACCELERATION_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f20_dtc_brand_acceleration_2nd_derivatives_001_150_claude: {n_features} features pass")
