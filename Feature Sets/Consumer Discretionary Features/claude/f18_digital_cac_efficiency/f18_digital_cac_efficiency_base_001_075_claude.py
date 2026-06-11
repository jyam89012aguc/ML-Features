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
def _f18_sga_to_revenue(sgna, revenue):
    return sgna / revenue.replace(0, np.nan)


def _f18_cac_efficiency(sgna, revenue, w):
    rg = revenue.pct_change(periods=w)
    sg = sgna.pct_change(periods=w)
    return rg - sg


def _f18_marketing_leverage(sgna, revenue, w):
    s2r = sgna / revenue.replace(0, np.nan)
    return s2r - s2r.rolling(w, min_periods=max(1, w // 2)).mean()


def f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_21d_base_v001_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r * _mean(closeadj, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_63d_base_v002_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r * _mean(closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_126d_base_v003_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r * _mean(closeadj, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_189d_base_v004_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r * _mean(closeadj, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_252d_base_v005_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r * _mean(closeadj, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_378d_base_v006_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r * _mean(closeadj, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rmean_21d_base_v007_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _mean(s2r, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rmean_63d_base_v008_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _mean(s2r, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rmean_126d_base_v009_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _mean(s2r, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rmean_189d_base_v010_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _mean(s2r, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rmean_252d_base_v011_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _mean(s2r, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rmean_378d_base_v012_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _mean(s2r, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rstd_21d_base_v013_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _std(s2r, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rstd_63d_base_v014_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _std(s2r, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rstd_126d_base_v015_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _std(s2r, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rstd_189d_base_v016_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _std(s2r, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rstd_252d_base_v017_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _std(s2r, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rstd_378d_base_v018_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _std(s2r, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_z_21d_base_v019_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _z(s2r, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_z_63d_base_v020_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _z(s2r, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_z_126d_base_v021_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _z(s2r, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_z_189d_base_v022_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _z(s2r, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_z_252d_base_v023_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _z(s2r, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_z_378d_base_v024_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _z(s2r, 756)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_diff_21d_base_v025_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r - s2r.shift(21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_diff_63d_base_v026_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r - s2r.shift(63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_diff_126d_base_v027_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r - s2r.shift(126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_diff_189d_base_v028_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r - s2r.shift(189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_diff_252d_base_v029_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r - s2r.shift(252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_diff_378d_base_v030_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r - s2r.shift(378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_raw_21d_base_v031_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = ce
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_raw_63d_base_v032_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = ce
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_raw_126d_base_v033_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = ce
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_raw_189d_base_v034_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = ce
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_raw_252d_base_v035_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 252)
    base = ce
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_raw_378d_base_v036_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 378)
    base = ce
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_rmean_21d_base_v037_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = _mean(ce, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_rmean_63d_base_v038_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = _mean(ce, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_rmean_126d_base_v039_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = _mean(ce, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_rmean_189d_base_v040_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = _mean(ce, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_rmean_252d_base_v041_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 252)
    base = _mean(ce, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_rmean_378d_base_v042_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 378)
    base = _mean(ce, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_z_21d_base_v043_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = _z(ce, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_z_63d_base_v044_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = _z(ce, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_z_126d_base_v045_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = _z(ce, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_z_189d_base_v046_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = _z(ce, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_z_252d_base_v047_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 252)
    base = _z(ce, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_z_378d_base_v048_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 378)
    base = _z(ce, 756)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_sq_21d_base_v049_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = ce * ce.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_sq_63d_base_v050_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = ce * ce.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_sq_126d_base_v051_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = ce * ce.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_sq_189d_base_v052_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = ce * ce.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_sq_252d_base_v053_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 252)
    base = ce * ce.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_sq_378d_base_v054_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 378)
    base = ce * ce.abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_absx_21d_base_v055_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = ce.abs() * np.sign(ce)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_absx_63d_base_v056_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = ce.abs() * np.sign(ce)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_absx_126d_base_v057_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = ce.abs() * np.sign(ce)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_absx_189d_base_v058_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = ce.abs() * np.sign(ce)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_absx_252d_base_v059_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 252)
    base = ce.abs() * np.sign(ce)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_absx_378d_base_v060_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 378)
    base = ce.abs() * np.sign(ce)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_raw_21d_base_v061_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_raw_63d_base_v062_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_raw_126d_base_v063_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_raw_189d_base_v064_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_raw_252d_base_v065_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 252)
    base = ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_raw_378d_base_v066_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 378)
    base = ml
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rmean_21d_base_v067_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = _mean(ml, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rmean_63d_base_v068_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = _mean(ml, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rmean_126d_base_v069_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = _mean(ml, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rmean_189d_base_v070_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = _mean(ml, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rmean_252d_base_v071_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 252)
    base = _mean(ml, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rmean_378d_base_v072_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 378)
    base = _mean(ml, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_z_21d_base_v073_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = _z(ml, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_z_63d_base_v074_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = _z(ml, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_z_126d_base_v075_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = _z(ml, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_21d_base_v001_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_63d_base_v002_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_126d_base_v003_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_189d_base_v004_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_252d_base_v005_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_378d_base_v006_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rmean_21d_base_v007_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rmean_63d_base_v008_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rmean_126d_base_v009_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rmean_189d_base_v010_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rmean_252d_base_v011_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rmean_378d_base_v012_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rstd_21d_base_v013_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rstd_63d_base_v014_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rstd_126d_base_v015_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rstd_189d_base_v016_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rstd_252d_base_v017_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rstd_378d_base_v018_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_z_21d_base_v019_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_z_63d_base_v020_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_z_126d_base_v021_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_z_189d_base_v022_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_z_252d_base_v023_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_z_378d_base_v024_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_diff_21d_base_v025_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_diff_63d_base_v026_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_diff_126d_base_v027_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_diff_189d_base_v028_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_diff_252d_base_v029_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_diff_378d_base_v030_signal,
    f18dce_f18_digital_cac_efficiency_cacef_raw_21d_base_v031_signal,
    f18dce_f18_digital_cac_efficiency_cacef_raw_63d_base_v032_signal,
    f18dce_f18_digital_cac_efficiency_cacef_raw_126d_base_v033_signal,
    f18dce_f18_digital_cac_efficiency_cacef_raw_189d_base_v034_signal,
    f18dce_f18_digital_cac_efficiency_cacef_raw_252d_base_v035_signal,
    f18dce_f18_digital_cac_efficiency_cacef_raw_378d_base_v036_signal,
    f18dce_f18_digital_cac_efficiency_cacef_rmean_21d_base_v037_signal,
    f18dce_f18_digital_cac_efficiency_cacef_rmean_63d_base_v038_signal,
    f18dce_f18_digital_cac_efficiency_cacef_rmean_126d_base_v039_signal,
    f18dce_f18_digital_cac_efficiency_cacef_rmean_189d_base_v040_signal,
    f18dce_f18_digital_cac_efficiency_cacef_rmean_252d_base_v041_signal,
    f18dce_f18_digital_cac_efficiency_cacef_rmean_378d_base_v042_signal,
    f18dce_f18_digital_cac_efficiency_cacef_z_21d_base_v043_signal,
    f18dce_f18_digital_cac_efficiency_cacef_z_63d_base_v044_signal,
    f18dce_f18_digital_cac_efficiency_cacef_z_126d_base_v045_signal,
    f18dce_f18_digital_cac_efficiency_cacef_z_189d_base_v046_signal,
    f18dce_f18_digital_cac_efficiency_cacef_z_252d_base_v047_signal,
    f18dce_f18_digital_cac_efficiency_cacef_z_378d_base_v048_signal,
    f18dce_f18_digital_cac_efficiency_cacef_sq_21d_base_v049_signal,
    f18dce_f18_digital_cac_efficiency_cacef_sq_63d_base_v050_signal,
    f18dce_f18_digital_cac_efficiency_cacef_sq_126d_base_v051_signal,
    f18dce_f18_digital_cac_efficiency_cacef_sq_189d_base_v052_signal,
    f18dce_f18_digital_cac_efficiency_cacef_sq_252d_base_v053_signal,
    f18dce_f18_digital_cac_efficiency_cacef_sq_378d_base_v054_signal,
    f18dce_f18_digital_cac_efficiency_cacef_absx_21d_base_v055_signal,
    f18dce_f18_digital_cac_efficiency_cacef_absx_63d_base_v056_signal,
    f18dce_f18_digital_cac_efficiency_cacef_absx_126d_base_v057_signal,
    f18dce_f18_digital_cac_efficiency_cacef_absx_189d_base_v058_signal,
    f18dce_f18_digital_cac_efficiency_cacef_absx_252d_base_v059_signal,
    f18dce_f18_digital_cac_efficiency_cacef_absx_378d_base_v060_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_raw_21d_base_v061_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_raw_63d_base_v062_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_raw_126d_base_v063_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_raw_189d_base_v064_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_raw_252d_base_v065_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_raw_378d_base_v066_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rmean_21d_base_v067_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rmean_63d_base_v068_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rmean_126d_base_v069_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rmean_189d_base_v070_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rmean_252d_base_v071_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rmean_378d_base_v072_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_z_21d_base_v073_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_z_63d_base_v074_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_z_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FDIGITAL_CAC_EFFICIENCY_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f18_sga_to_revenue", "_f18_cac_efficiency", "_f18_marketing_leverage",)
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
    print(f"OK f18_digital_cac_efficiency_base_001_075_claude: {n_features} features pass")
