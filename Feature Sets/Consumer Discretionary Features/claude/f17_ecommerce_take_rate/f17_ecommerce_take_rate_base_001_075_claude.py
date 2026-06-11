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
def _f17_take_rate_proxy(gp, revenue):
    return gp / revenue.replace(0, np.nan)


def _f17_take_rate_trend(grossmargin, w):
    return grossmargin - grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()


def _f17_take_rate_uplift(gp, revenue, w):
    tr = gp / revenue.replace(0, np.nan)
    return tr - tr.rolling(w, min_periods=max(1, w // 2)).mean()


def f17etr_f17_ecommerce_take_rate_takerate_xclmean_21d_base_v001_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr * _mean(closeadj, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_xclmean_63d_base_v002_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr * _mean(closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_xclmean_126d_base_v003_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr * _mean(closeadj, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_xclmean_189d_base_v004_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr * _mean(closeadj, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_xclmean_252d_base_v005_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr * _mean(closeadj, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_xclmean_378d_base_v006_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr * _mean(closeadj, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rmean_21d_base_v007_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _mean(tr, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rmean_63d_base_v008_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _mean(tr, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rmean_126d_base_v009_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _mean(tr, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rmean_189d_base_v010_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _mean(tr, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rmean_252d_base_v011_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _mean(tr, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rmean_378d_base_v012_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _mean(tr, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rstd_21d_base_v013_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _std(tr, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rstd_63d_base_v014_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _std(tr, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rstd_126d_base_v015_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _std(tr, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rstd_189d_base_v016_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _std(tr, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rstd_252d_base_v017_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _std(tr, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rstd_378d_base_v018_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _std(tr, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_z_21d_base_v019_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _z(tr, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_z_63d_base_v020_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _z(tr, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_z_126d_base_v021_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _z(tr, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_z_189d_base_v022_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _z(tr, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_z_252d_base_v023_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _z(tr, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_z_378d_base_v024_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _z(tr, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_diff_21d_base_v025_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr - tr.shift(21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_diff_63d_base_v026_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr - tr.shift(63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_diff_126d_base_v027_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr - tr.shift(126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_diff_189d_base_v028_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr - tr.shift(189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_diff_252d_base_v029_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr - tr.shift(252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_diff_378d_base_v030_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr - tr.shift(378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_raw_21d_base_v031_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = tt
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_raw_63d_base_v032_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = tt
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_raw_126d_base_v033_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = tt
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_raw_189d_base_v034_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = tt
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_raw_252d_base_v035_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 252)
    base = tt
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_raw_378d_base_v036_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 378)
    base = tt
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_rmean_21d_base_v037_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = _mean(tt, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_rmean_63d_base_v038_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = _mean(tt, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_rmean_126d_base_v039_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = _mean(tt, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_rmean_189d_base_v040_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = _mean(tt, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_rmean_252d_base_v041_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 252)
    base = _mean(tt, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_rmean_378d_base_v042_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 378)
    base = _mean(tt, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_absx_21d_base_v043_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = tt.abs() * np.sign(tt)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_absx_63d_base_v044_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = tt.abs() * np.sign(tt)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_absx_126d_base_v045_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = tt.abs() * np.sign(tt)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_absx_189d_base_v046_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = tt.abs() * np.sign(tt)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_absx_252d_base_v047_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 252)
    base = tt.abs() * np.sign(tt)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_absx_378d_base_v048_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 378)
    base = tt.abs() * np.sign(tt)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_z_21d_base_v049_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = _z(tt, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_z_63d_base_v050_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = _z(tt, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_z_126d_base_v051_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = _z(tt, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_z_189d_base_v052_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = _z(tt, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_z_252d_base_v053_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 252)
    base = _z(tt, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_z_378d_base_v054_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 378)
    base = _z(tt, 756)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_sq_21d_base_v055_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = tt * tt.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_sq_63d_base_v056_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = tt * tt.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_sq_126d_base_v057_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = tt * tt.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_sq_189d_base_v058_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = tt * tt.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_sq_252d_base_v059_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 252)
    base = tt * tt.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_sq_378d_base_v060_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 378)
    base = tt * tt.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_raw_21d_base_v061_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_raw_63d_base_v062_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_raw_126d_base_v063_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_raw_189d_base_v064_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_raw_252d_base_v065_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 252)
    base = tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_raw_378d_base_v066_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 378)
    base = tu
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rmean_21d_base_v067_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = _mean(tu, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rmean_63d_base_v068_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = _mean(tu, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rmean_126d_base_v069_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = _mean(tu, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rmean_189d_base_v070_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = _mean(tu, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rmean_252d_base_v071_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 252)
    base = _mean(tu, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rmean_378d_base_v072_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 378)
    base = _mean(tu, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_z_21d_base_v073_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = _z(tu, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_z_63d_base_v074_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = _z(tu, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_z_126d_base_v075_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = _z(tu, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17etr_f17_ecommerce_take_rate_takerate_xclmean_21d_base_v001_signal,
    f17etr_f17_ecommerce_take_rate_takerate_xclmean_63d_base_v002_signal,
    f17etr_f17_ecommerce_take_rate_takerate_xclmean_126d_base_v003_signal,
    f17etr_f17_ecommerce_take_rate_takerate_xclmean_189d_base_v004_signal,
    f17etr_f17_ecommerce_take_rate_takerate_xclmean_252d_base_v005_signal,
    f17etr_f17_ecommerce_take_rate_takerate_xclmean_378d_base_v006_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rmean_21d_base_v007_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rmean_63d_base_v008_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rmean_126d_base_v009_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rmean_189d_base_v010_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rmean_252d_base_v011_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rmean_378d_base_v012_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rstd_21d_base_v013_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rstd_63d_base_v014_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rstd_126d_base_v015_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rstd_189d_base_v016_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rstd_252d_base_v017_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rstd_378d_base_v018_signal,
    f17etr_f17_ecommerce_take_rate_takerate_z_21d_base_v019_signal,
    f17etr_f17_ecommerce_take_rate_takerate_z_63d_base_v020_signal,
    f17etr_f17_ecommerce_take_rate_takerate_z_126d_base_v021_signal,
    f17etr_f17_ecommerce_take_rate_takerate_z_189d_base_v022_signal,
    f17etr_f17_ecommerce_take_rate_takerate_z_252d_base_v023_signal,
    f17etr_f17_ecommerce_take_rate_takerate_z_378d_base_v024_signal,
    f17etr_f17_ecommerce_take_rate_takerate_diff_21d_base_v025_signal,
    f17etr_f17_ecommerce_take_rate_takerate_diff_63d_base_v026_signal,
    f17etr_f17_ecommerce_take_rate_takerate_diff_126d_base_v027_signal,
    f17etr_f17_ecommerce_take_rate_takerate_diff_189d_base_v028_signal,
    f17etr_f17_ecommerce_take_rate_takerate_diff_252d_base_v029_signal,
    f17etr_f17_ecommerce_take_rate_takerate_diff_378d_base_v030_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_raw_21d_base_v031_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_raw_63d_base_v032_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_raw_126d_base_v033_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_raw_189d_base_v034_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_raw_252d_base_v035_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_raw_378d_base_v036_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_rmean_21d_base_v037_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_rmean_63d_base_v038_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_rmean_126d_base_v039_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_rmean_189d_base_v040_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_rmean_252d_base_v041_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_rmean_378d_base_v042_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_absx_21d_base_v043_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_absx_63d_base_v044_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_absx_126d_base_v045_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_absx_189d_base_v046_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_absx_252d_base_v047_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_absx_378d_base_v048_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_z_21d_base_v049_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_z_63d_base_v050_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_z_126d_base_v051_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_z_189d_base_v052_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_z_252d_base_v053_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_z_378d_base_v054_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_sq_21d_base_v055_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_sq_63d_base_v056_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_sq_126d_base_v057_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_sq_189d_base_v058_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_sq_252d_base_v059_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_sq_378d_base_v060_signal,
    f17etr_f17_ecommerce_take_rate_truplift_raw_21d_base_v061_signal,
    f17etr_f17_ecommerce_take_rate_truplift_raw_63d_base_v062_signal,
    f17etr_f17_ecommerce_take_rate_truplift_raw_126d_base_v063_signal,
    f17etr_f17_ecommerce_take_rate_truplift_raw_189d_base_v064_signal,
    f17etr_f17_ecommerce_take_rate_truplift_raw_252d_base_v065_signal,
    f17etr_f17_ecommerce_take_rate_truplift_raw_378d_base_v066_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rmean_21d_base_v067_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rmean_63d_base_v068_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rmean_126d_base_v069_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rmean_189d_base_v070_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rmean_252d_base_v071_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rmean_378d_base_v072_signal,
    f17etr_f17_ecommerce_take_rate_truplift_z_21d_base_v073_signal,
    f17etr_f17_ecommerce_take_rate_truplift_z_63d_base_v074_signal,
    f17etr_f17_ecommerce_take_rate_truplift_z_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FECOMMERCE_TAKE_RATE_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f17_take_rate_proxy", "_f17_take_rate_trend", "_f17_take_rate_uplift",)
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
    print(f"OK f17_ecommerce_take_rate_base_001_075_claude: {n_features} features pass")
