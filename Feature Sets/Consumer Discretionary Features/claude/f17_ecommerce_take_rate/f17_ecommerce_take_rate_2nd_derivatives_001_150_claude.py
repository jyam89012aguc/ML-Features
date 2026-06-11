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
def _f17_take_rate_proxy(gp, revenue):
    return gp / revenue.replace(0, np.nan)


def _f17_take_rate_trend(grossmargin, w):
    return grossmargin - grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()


def _f17_take_rate_uplift(gp, revenue, w):
    tr = gp / revenue.replace(0, np.nan)
    return tr - tr.rolling(w, min_periods=max(1, w // 2)).mean()


def f17etr_f17_ecommerce_take_rate_takerate_xclmean_21d_slope_v001_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr * _mean(closeadj, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_xclmean_63d_slope_v002_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr * _mean(closeadj, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_xclmean_126d_slope_v003_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr * _mean(closeadj, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_xclmean_189d_slope_v004_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr * _mean(closeadj, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_xclmean_252d_slope_v005_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr * _mean(closeadj, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_xclmean_378d_slope_v006_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr * _mean(closeadj, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rmean_21d_slope_v007_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _mean(tr, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rmean_63d_slope_v008_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _mean(tr, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rmean_126d_slope_v009_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _mean(tr, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rmean_189d_slope_v010_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _mean(tr, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rmean_252d_slope_v011_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _mean(tr, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rmean_378d_slope_v012_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _mean(tr, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rstd_21d_slope_v013_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _std(tr, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rstd_63d_slope_v014_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _std(tr, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rstd_126d_slope_v015_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _std(tr, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rstd_189d_slope_v016_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _std(tr, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rstd_252d_slope_v017_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _std(tr, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_rstd_378d_slope_v018_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _std(tr, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_z_21d_slope_v019_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _z(tr, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_z_63d_slope_v020_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _z(tr, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_z_126d_slope_v021_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _z(tr, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_z_189d_slope_v022_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _z(tr, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_z_252d_slope_v023_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _z(tr, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_z_378d_slope_v024_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = _z(tr, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_diff_21d_slope_v025_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr - tr.shift(21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_diff_63d_slope_v026_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr - tr.shift(63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_diff_126d_slope_v027_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr - tr.shift(126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_diff_189d_slope_v028_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr - tr.shift(189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_diff_252d_slope_v029_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr - tr.shift(252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_takerate_diff_378d_slope_v030_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr - tr.shift(378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_raw_21d_slope_v031_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = tt
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_raw_63d_slope_v032_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = tt
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_raw_126d_slope_v033_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = tt
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_raw_189d_slope_v034_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = tt
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_raw_252d_slope_v035_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 252)
    base = tt
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_raw_378d_slope_v036_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 378)
    base = tt
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_rmean_21d_slope_v037_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = _mean(tt, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_rmean_63d_slope_v038_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = _mean(tt, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_rmean_126d_slope_v039_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = _mean(tt, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_rmean_189d_slope_v040_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = _mean(tt, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_rmean_252d_slope_v041_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 252)
    base = _mean(tt, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_rmean_378d_slope_v042_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 378)
    base = _mean(tt, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_absx_21d_slope_v043_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = tt.abs() * np.sign(tt)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_absx_63d_slope_v044_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = tt.abs() * np.sign(tt)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_absx_126d_slope_v045_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = tt.abs() * np.sign(tt)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_absx_189d_slope_v046_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = tt.abs() * np.sign(tt)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_absx_252d_slope_v047_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 252)
    base = tt.abs() * np.sign(tt)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_absx_378d_slope_v048_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 378)
    base = tt.abs() * np.sign(tt)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_z_21d_slope_v049_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = _z(tt, 63)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_z_63d_slope_v050_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = _z(tt, 126)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_z_126d_slope_v051_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = _z(tt, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_z_189d_slope_v052_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = _z(tt, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_z_252d_slope_v053_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 252)
    base = _z(tt, 504)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_z_378d_slope_v054_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 378)
    base = _z(tt, 756)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_sq_21d_slope_v055_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = tt * tt.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_sq_63d_slope_v056_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = tt * tt.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_sq_126d_slope_v057_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = tt * tt.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_sq_189d_slope_v058_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = tt * tt.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_sq_252d_slope_v059_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 252)
    base = tt * tt.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trtrend_sq_378d_slope_v060_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 378)
    base = tt * tt.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_raw_21d_slope_v061_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = tu
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_raw_63d_slope_v062_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = tu
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_raw_126d_slope_v063_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = tu
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_raw_189d_slope_v064_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = tu
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_raw_252d_slope_v065_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 252)
    base = tu
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_raw_378d_slope_v066_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 378)
    base = tu
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rmean_21d_slope_v067_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = _mean(tu, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rmean_63d_slope_v068_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = _mean(tu, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rmean_126d_slope_v069_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = _mean(tu, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rmean_189d_slope_v070_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = _mean(tu, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rmean_252d_slope_v071_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 252)
    base = _mean(tu, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rmean_378d_slope_v072_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 378)
    base = _mean(tu, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_z_21d_slope_v073_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = _z(tu, 63)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_z_63d_slope_v074_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = _z(tu, 126)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_z_126d_slope_v075_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = _z(tu, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_z_189d_slope_v076_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = _z(tu, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_z_252d_slope_v077_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 252)
    base = _z(tu, 504)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_z_378d_slope_v078_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 378)
    base = _z(tu, 756)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_sq_21d_slope_v079_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = tu * tu.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_sq_63d_slope_v080_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = tu * tu.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_sq_126d_slope_v081_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = tu * tu.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_sq_189d_slope_v082_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = tu * tu.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_sq_252d_slope_v083_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 252)
    base = tu * tu.abs()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_sq_378d_slope_v084_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 378)
    base = tu * tu.abs()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rstd_21d_slope_v085_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = _std(tu, 21)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rstd_63d_slope_v086_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = _std(tu, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rstd_126d_slope_v087_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = _std(tu, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rstd_189d_slope_v088_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = _std(tu, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rstd_252d_slope_v089_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 252)
    base = _std(tu, 252)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_truplift_rstd_378d_slope_v090_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 378)
    base = _std(tu, 378)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trxtu_mul_10d_slope_v091_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tu = _f17_take_rate_uplift(gp, revenue, 10)
    base = tr * tu
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trxtu_mul_21d_slope_v092_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = tr * tu
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trxtu_mul_42d_slope_v093_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tu = _f17_take_rate_uplift(gp, revenue, 42)
    base = tr * tu
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trxtu_mul_63d_slope_v094_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = tr * tu
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trxtu_mul_126d_slope_v095_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = tr * tu
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trxtu_mul_189d_slope_v096_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = tr * tu
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_ttptu_sum_10d_slope_v097_signal(grossmargin, gp, revenue, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 10)
    tu = _f17_take_rate_uplift(gp, revenue, 10)
    base = tt + tu
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_ttptu_sum_21d_slope_v098_signal(grossmargin, gp, revenue, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = tt + tu
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_ttptu_sum_42d_slope_v099_signal(grossmargin, gp, revenue, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 42)
    tu = _f17_take_rate_uplift(gp, revenue, 42)
    base = tt + tu
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_ttptu_sum_63d_slope_v100_signal(grossmargin, gp, revenue, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = tt + tu
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_ttptu_sum_126d_slope_v101_signal(grossmargin, gp, revenue, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = tt + tu
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_ttptu_sum_189d_slope_v102_signal(grossmargin, gp, revenue, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = tt + tu
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trmtt_diff_10d_slope_v103_signal(gp, revenue, grossmargin, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tt = _f17_take_rate_trend(grossmargin, 10)
    base = tr - tt
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trmtt_diff_21d_slope_v104_signal(gp, revenue, grossmargin, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = tr - tt
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trmtt_diff_42d_slope_v105_signal(gp, revenue, grossmargin, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tt = _f17_take_rate_trend(grossmargin, 42)
    base = tr - tt
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trmtt_diff_63d_slope_v106_signal(gp, revenue, grossmargin, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = tr - tt
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trmtt_diff_126d_slope_v107_signal(gp, revenue, grossmargin, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = tr - tt
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trmtt_diff_189d_slope_v108_signal(gp, revenue, grossmargin, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = tr - tt
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_mxs_10d_slope_v109_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 10)
    base = _mean(tu, 10) * _std(tu, 10)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_mxs_21d_slope_v110_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = _mean(tu, 21) * _std(tu, 21)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_mxs_42d_slope_v111_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 42)
    base = _mean(tu, 42) * _std(tu, 42)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_mxs_63d_slope_v112_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = _mean(tu, 63) * _std(tu, 63)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_mxs_126d_slope_v113_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = _mean(tu, 126) * _std(tu, 126)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_mxs_189d_slope_v114_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = _mean(tu, 189) * _std(tu, 189)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trdiff_smooth_10d_slope_v115_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr.diff(10).rolling(10, min_periods=max(1,10//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trdiff_smooth_21d_slope_v116_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr.diff(21).rolling(21, min_periods=max(1,21//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trdiff_smooth_42d_slope_v117_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr.diff(42).rolling(42, min_periods=max(1,42//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trdiff_smooth_63d_slope_v118_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr.diff(63).rolling(63, min_periods=max(1,63//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trdiff_smooth_126d_slope_v119_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr.diff(126).rolling(126, min_periods=max(1,126//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_trdiff_smooth_189d_slope_v120_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = tr.diff(189).rolling(189, min_periods=max(1,189//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_ema_10d_slope_v121_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 10)
    base = tt.ewm(span=10, min_periods=max(1, 10//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_ema_21d_slope_v122_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = tt.ewm(span=21, min_periods=max(1, 21//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_ema_42d_slope_v123_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 42)
    base = tt.ewm(span=42, min_periods=max(1, 42//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_ema_63d_slope_v124_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = tt.ewm(span=63, min_periods=max(1, 63//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_ema_126d_slope_v125_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = tt.ewm(span=126, min_periods=max(1, 126//2)).mean()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_ema_189d_slope_v126_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = tt.ewm(span=189, min_periods=max(1, 189//2)).mean()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_range_10d_slope_v127_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 10)
    base = tu.rolling(10, min_periods=max(1, 10//2)).max() - tu.rolling(10, min_periods=max(1, 10//2)).min()
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_range_21d_slope_v128_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = tu.rolling(21, min_periods=max(1, 21//2)).max() - tu.rolling(21, min_periods=max(1, 21//2)).min()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_range_42d_slope_v129_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 42)
    base = tu.rolling(42, min_periods=max(1, 42//2)).max() - tu.rolling(42, min_periods=max(1, 42//2)).min()
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_range_63d_slope_v130_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = tu.rolling(63, min_periods=max(1, 63//2)).max() - tu.rolling(63, min_periods=max(1, 63//2)).min()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_range_126d_slope_v131_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = tu.rolling(126, min_periods=max(1, 126//2)).max() - tu.rolling(126, min_periods=max(1, 126//2)).min()
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_range_189d_slope_v132_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = tu.rolling(189, min_periods=max(1, 189//2)).max() - tu.rolling(189, min_periods=max(1, 189//2)).min()
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tr_dmed_10d_slope_v133_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = (tr - tr.rolling(10, min_periods=max(1, 10//2)).median())
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tr_dmed_21d_slope_v134_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = (tr - tr.rolling(21, min_periods=max(1, 21//2)).median())
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tr_dmed_42d_slope_v135_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = (tr - tr.rolling(42, min_periods=max(1, 42//2)).median())
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tr_dmed_63d_slope_v136_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = (tr - tr.rolling(63, min_periods=max(1, 63//2)).median())
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tr_dmed_126d_slope_v137_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = (tr - tr.rolling(126, min_periods=max(1, 126//2)).median())
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tr_dmed_189d_slope_v138_signal(gp, revenue, closeadj):
    tr = _f17_take_rate_proxy(gp, revenue)
    base = (tr - tr.rolling(189, min_periods=max(1, 189//2)).median())
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_iqr_10d_slope_v139_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 10)
    base = tt.rolling(10, min_periods=max(1, 10//2)).quantile(0.75) - tt.rolling(10, min_periods=max(1, 10//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_iqr_21d_slope_v140_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 21)
    base = tt.rolling(21, min_periods=max(1, 21//2)).quantile(0.75) - tt.rolling(21, min_periods=max(1, 21//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_iqr_42d_slope_v141_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 42)
    base = tt.rolling(42, min_periods=max(1, 42//2)).quantile(0.75) - tt.rolling(42, min_periods=max(1, 42//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_iqr_63d_slope_v142_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 63)
    base = tt.rolling(63, min_periods=max(1, 63//2)).quantile(0.75) - tt.rolling(63, min_periods=max(1, 63//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_iqr_126d_slope_v143_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 126)
    base = tt.rolling(126, min_periods=max(1, 126//2)).quantile(0.75) - tt.rolling(126, min_periods=max(1, 126//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tt_iqr_189d_slope_v144_signal(grossmargin, closeadj):
    tt = _f17_take_rate_trend(grossmargin, 189)
    base = tt.rolling(189, min_periods=max(1, 189//2)).quantile(0.75) - tt.rolling(189, min_periods=max(1, 189//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_iqr_10d_slope_v145_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 10)
    base = tu.rolling(10, min_periods=max(1, 10//2)).quantile(0.75) - tu.rolling(10, min_periods=max(1, 10//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_iqr_21d_slope_v146_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 21)
    base = tu.rolling(21, min_periods=max(1, 21//2)).quantile(0.75) - tu.rolling(21, min_periods=max(1, 21//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_iqr_42d_slope_v147_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 42)
    base = tu.rolling(42, min_periods=max(1, 42//2)).quantile(0.75) - tu.rolling(42, min_periods=max(1, 42//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_iqr_63d_slope_v148_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 63)
    base = tu.rolling(63, min_periods=max(1, 63//2)).quantile(0.75) - tu.rolling(63, min_periods=max(1, 63//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_iqr_126d_slope_v149_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 126)
    base = tu.rolling(126, min_periods=max(1, 126//2)).quantile(0.75) - tu.rolling(126, min_periods=max(1, 126//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_pct(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f17etr_f17_ecommerce_take_rate_tu_iqr_189d_slope_v150_signal(gp, revenue, closeadj):
    tu = _f17_take_rate_uplift(gp, revenue, 189)
    base = tu.rolling(189, min_periods=max(1, 189//2)).quantile(0.75) - tu.rolling(189, min_periods=max(1, 189//2)).quantile(0.25)
    base_val = base * closeadj
    result = _slope_diff_norm(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17etr_f17_ecommerce_take_rate_takerate_xclmean_21d_slope_v001_signal,
    f17etr_f17_ecommerce_take_rate_takerate_xclmean_63d_slope_v002_signal,
    f17etr_f17_ecommerce_take_rate_takerate_xclmean_126d_slope_v003_signal,
    f17etr_f17_ecommerce_take_rate_takerate_xclmean_189d_slope_v004_signal,
    f17etr_f17_ecommerce_take_rate_takerate_xclmean_252d_slope_v005_signal,
    f17etr_f17_ecommerce_take_rate_takerate_xclmean_378d_slope_v006_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rmean_21d_slope_v007_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rmean_63d_slope_v008_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rmean_126d_slope_v009_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rmean_189d_slope_v010_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rmean_252d_slope_v011_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rmean_378d_slope_v012_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rstd_21d_slope_v013_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rstd_63d_slope_v014_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rstd_126d_slope_v015_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rstd_189d_slope_v016_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rstd_252d_slope_v017_signal,
    f17etr_f17_ecommerce_take_rate_takerate_rstd_378d_slope_v018_signal,
    f17etr_f17_ecommerce_take_rate_takerate_z_21d_slope_v019_signal,
    f17etr_f17_ecommerce_take_rate_takerate_z_63d_slope_v020_signal,
    f17etr_f17_ecommerce_take_rate_takerate_z_126d_slope_v021_signal,
    f17etr_f17_ecommerce_take_rate_takerate_z_189d_slope_v022_signal,
    f17etr_f17_ecommerce_take_rate_takerate_z_252d_slope_v023_signal,
    f17etr_f17_ecommerce_take_rate_takerate_z_378d_slope_v024_signal,
    f17etr_f17_ecommerce_take_rate_takerate_diff_21d_slope_v025_signal,
    f17etr_f17_ecommerce_take_rate_takerate_diff_63d_slope_v026_signal,
    f17etr_f17_ecommerce_take_rate_takerate_diff_126d_slope_v027_signal,
    f17etr_f17_ecommerce_take_rate_takerate_diff_189d_slope_v028_signal,
    f17etr_f17_ecommerce_take_rate_takerate_diff_252d_slope_v029_signal,
    f17etr_f17_ecommerce_take_rate_takerate_diff_378d_slope_v030_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_raw_21d_slope_v031_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_raw_63d_slope_v032_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_raw_126d_slope_v033_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_raw_189d_slope_v034_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_raw_252d_slope_v035_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_raw_378d_slope_v036_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_rmean_21d_slope_v037_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_rmean_63d_slope_v038_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_rmean_126d_slope_v039_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_rmean_189d_slope_v040_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_rmean_252d_slope_v041_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_rmean_378d_slope_v042_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_absx_21d_slope_v043_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_absx_63d_slope_v044_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_absx_126d_slope_v045_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_absx_189d_slope_v046_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_absx_252d_slope_v047_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_absx_378d_slope_v048_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_z_21d_slope_v049_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_z_63d_slope_v050_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_z_126d_slope_v051_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_z_189d_slope_v052_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_z_252d_slope_v053_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_z_378d_slope_v054_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_sq_21d_slope_v055_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_sq_63d_slope_v056_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_sq_126d_slope_v057_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_sq_189d_slope_v058_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_sq_252d_slope_v059_signal,
    f17etr_f17_ecommerce_take_rate_trtrend_sq_378d_slope_v060_signal,
    f17etr_f17_ecommerce_take_rate_truplift_raw_21d_slope_v061_signal,
    f17etr_f17_ecommerce_take_rate_truplift_raw_63d_slope_v062_signal,
    f17etr_f17_ecommerce_take_rate_truplift_raw_126d_slope_v063_signal,
    f17etr_f17_ecommerce_take_rate_truplift_raw_189d_slope_v064_signal,
    f17etr_f17_ecommerce_take_rate_truplift_raw_252d_slope_v065_signal,
    f17etr_f17_ecommerce_take_rate_truplift_raw_378d_slope_v066_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rmean_21d_slope_v067_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rmean_63d_slope_v068_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rmean_126d_slope_v069_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rmean_189d_slope_v070_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rmean_252d_slope_v071_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rmean_378d_slope_v072_signal,
    f17etr_f17_ecommerce_take_rate_truplift_z_21d_slope_v073_signal,
    f17etr_f17_ecommerce_take_rate_truplift_z_63d_slope_v074_signal,
    f17etr_f17_ecommerce_take_rate_truplift_z_126d_slope_v075_signal,
    f17etr_f17_ecommerce_take_rate_truplift_z_189d_slope_v076_signal,
    f17etr_f17_ecommerce_take_rate_truplift_z_252d_slope_v077_signal,
    f17etr_f17_ecommerce_take_rate_truplift_z_378d_slope_v078_signal,
    f17etr_f17_ecommerce_take_rate_truplift_sq_21d_slope_v079_signal,
    f17etr_f17_ecommerce_take_rate_truplift_sq_63d_slope_v080_signal,
    f17etr_f17_ecommerce_take_rate_truplift_sq_126d_slope_v081_signal,
    f17etr_f17_ecommerce_take_rate_truplift_sq_189d_slope_v082_signal,
    f17etr_f17_ecommerce_take_rate_truplift_sq_252d_slope_v083_signal,
    f17etr_f17_ecommerce_take_rate_truplift_sq_378d_slope_v084_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rstd_21d_slope_v085_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rstd_63d_slope_v086_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rstd_126d_slope_v087_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rstd_189d_slope_v088_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rstd_252d_slope_v089_signal,
    f17etr_f17_ecommerce_take_rate_truplift_rstd_378d_slope_v090_signal,
    f17etr_f17_ecommerce_take_rate_trxtu_mul_10d_slope_v091_signal,
    f17etr_f17_ecommerce_take_rate_trxtu_mul_21d_slope_v092_signal,
    f17etr_f17_ecommerce_take_rate_trxtu_mul_42d_slope_v093_signal,
    f17etr_f17_ecommerce_take_rate_trxtu_mul_63d_slope_v094_signal,
    f17etr_f17_ecommerce_take_rate_trxtu_mul_126d_slope_v095_signal,
    f17etr_f17_ecommerce_take_rate_trxtu_mul_189d_slope_v096_signal,
    f17etr_f17_ecommerce_take_rate_ttptu_sum_10d_slope_v097_signal,
    f17etr_f17_ecommerce_take_rate_ttptu_sum_21d_slope_v098_signal,
    f17etr_f17_ecommerce_take_rate_ttptu_sum_42d_slope_v099_signal,
    f17etr_f17_ecommerce_take_rate_ttptu_sum_63d_slope_v100_signal,
    f17etr_f17_ecommerce_take_rate_ttptu_sum_126d_slope_v101_signal,
    f17etr_f17_ecommerce_take_rate_ttptu_sum_189d_slope_v102_signal,
    f17etr_f17_ecommerce_take_rate_trmtt_diff_10d_slope_v103_signal,
    f17etr_f17_ecommerce_take_rate_trmtt_diff_21d_slope_v104_signal,
    f17etr_f17_ecommerce_take_rate_trmtt_diff_42d_slope_v105_signal,
    f17etr_f17_ecommerce_take_rate_trmtt_diff_63d_slope_v106_signal,
    f17etr_f17_ecommerce_take_rate_trmtt_diff_126d_slope_v107_signal,
    f17etr_f17_ecommerce_take_rate_trmtt_diff_189d_slope_v108_signal,
    f17etr_f17_ecommerce_take_rate_tu_mxs_10d_slope_v109_signal,
    f17etr_f17_ecommerce_take_rate_tu_mxs_21d_slope_v110_signal,
    f17etr_f17_ecommerce_take_rate_tu_mxs_42d_slope_v111_signal,
    f17etr_f17_ecommerce_take_rate_tu_mxs_63d_slope_v112_signal,
    f17etr_f17_ecommerce_take_rate_tu_mxs_126d_slope_v113_signal,
    f17etr_f17_ecommerce_take_rate_tu_mxs_189d_slope_v114_signal,
    f17etr_f17_ecommerce_take_rate_trdiff_smooth_10d_slope_v115_signal,
    f17etr_f17_ecommerce_take_rate_trdiff_smooth_21d_slope_v116_signal,
    f17etr_f17_ecommerce_take_rate_trdiff_smooth_42d_slope_v117_signal,
    f17etr_f17_ecommerce_take_rate_trdiff_smooth_63d_slope_v118_signal,
    f17etr_f17_ecommerce_take_rate_trdiff_smooth_126d_slope_v119_signal,
    f17etr_f17_ecommerce_take_rate_trdiff_smooth_189d_slope_v120_signal,
    f17etr_f17_ecommerce_take_rate_tt_ema_10d_slope_v121_signal,
    f17etr_f17_ecommerce_take_rate_tt_ema_21d_slope_v122_signal,
    f17etr_f17_ecommerce_take_rate_tt_ema_42d_slope_v123_signal,
    f17etr_f17_ecommerce_take_rate_tt_ema_63d_slope_v124_signal,
    f17etr_f17_ecommerce_take_rate_tt_ema_126d_slope_v125_signal,
    f17etr_f17_ecommerce_take_rate_tt_ema_189d_slope_v126_signal,
    f17etr_f17_ecommerce_take_rate_tu_range_10d_slope_v127_signal,
    f17etr_f17_ecommerce_take_rate_tu_range_21d_slope_v128_signal,
    f17etr_f17_ecommerce_take_rate_tu_range_42d_slope_v129_signal,
    f17etr_f17_ecommerce_take_rate_tu_range_63d_slope_v130_signal,
    f17etr_f17_ecommerce_take_rate_tu_range_126d_slope_v131_signal,
    f17etr_f17_ecommerce_take_rate_tu_range_189d_slope_v132_signal,
    f17etr_f17_ecommerce_take_rate_tr_dmed_10d_slope_v133_signal,
    f17etr_f17_ecommerce_take_rate_tr_dmed_21d_slope_v134_signal,
    f17etr_f17_ecommerce_take_rate_tr_dmed_42d_slope_v135_signal,
    f17etr_f17_ecommerce_take_rate_tr_dmed_63d_slope_v136_signal,
    f17etr_f17_ecommerce_take_rate_tr_dmed_126d_slope_v137_signal,
    f17etr_f17_ecommerce_take_rate_tr_dmed_189d_slope_v138_signal,
    f17etr_f17_ecommerce_take_rate_tt_iqr_10d_slope_v139_signal,
    f17etr_f17_ecommerce_take_rate_tt_iqr_21d_slope_v140_signal,
    f17etr_f17_ecommerce_take_rate_tt_iqr_42d_slope_v141_signal,
    f17etr_f17_ecommerce_take_rate_tt_iqr_63d_slope_v142_signal,
    f17etr_f17_ecommerce_take_rate_tt_iqr_126d_slope_v143_signal,
    f17etr_f17_ecommerce_take_rate_tt_iqr_189d_slope_v144_signal,
    f17etr_f17_ecommerce_take_rate_tu_iqr_10d_slope_v145_signal,
    f17etr_f17_ecommerce_take_rate_tu_iqr_21d_slope_v146_signal,
    f17etr_f17_ecommerce_take_rate_tu_iqr_42d_slope_v147_signal,
    f17etr_f17_ecommerce_take_rate_tu_iqr_63d_slope_v148_signal,
    f17etr_f17_ecommerce_take_rate_tu_iqr_126d_slope_v149_signal,
    f17etr_f17_ecommerce_take_rate_tu_iqr_189d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FECOMMERCE_TAKE_RATE_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f17_ecommerce_take_rate_2nd_derivatives_001_150_claude: {n_features} features pass")
