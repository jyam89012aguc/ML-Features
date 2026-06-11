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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)

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


def f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_21d_jerk_v001_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r * _mean(closeadj, 21)
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_63d_jerk_v002_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r * _mean(closeadj, 63)
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_126d_jerk_v003_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r * _mean(closeadj, 126)
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_189d_jerk_v004_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r * _mean(closeadj, 189)
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_252d_jerk_v005_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r * _mean(closeadj, 252)
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_378d_jerk_v006_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r * _mean(closeadj, 378)
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rmean_21d_jerk_v007_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _mean(s2r, 21)
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rmean_63d_jerk_v008_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _mean(s2r, 63)
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rmean_126d_jerk_v009_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _mean(s2r, 126)
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rmean_189d_jerk_v010_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _mean(s2r, 189)
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rmean_252d_jerk_v011_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _mean(s2r, 252)
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rmean_378d_jerk_v012_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _mean(s2r, 378)
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rstd_21d_jerk_v013_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _std(s2r, 21)
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rstd_63d_jerk_v014_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _std(s2r, 63)
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rstd_126d_jerk_v015_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _std(s2r, 126)
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rstd_189d_jerk_v016_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _std(s2r, 189)
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rstd_252d_jerk_v017_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _std(s2r, 252)
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_rstd_378d_jerk_v018_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _std(s2r, 378)
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_z_21d_jerk_v019_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _z(s2r, 63)
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_z_63d_jerk_v020_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _z(s2r, 126)
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_z_126d_jerk_v021_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _z(s2r, 252)
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_z_189d_jerk_v022_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _z(s2r, 378)
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_z_252d_jerk_v023_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _z(s2r, 504)
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_z_378d_jerk_v024_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = _z(s2r, 756)
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_diff_21d_jerk_v025_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r - s2r.shift(21)
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_diff_63d_jerk_v026_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r - s2r.shift(63)
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_diff_126d_jerk_v027_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r - s2r.shift(126)
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_diff_189d_jerk_v028_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r - s2r.shift(189)
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_diff_252d_jerk_v029_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r - s2r.shift(252)
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_sgnarev_diff_378d_jerk_v030_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r - s2r.shift(378)
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_raw_21d_jerk_v031_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = ce
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_raw_63d_jerk_v032_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = ce
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_raw_126d_jerk_v033_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = ce
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_raw_189d_jerk_v034_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = ce
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_raw_252d_jerk_v035_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 252)
    base = ce
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_raw_378d_jerk_v036_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 378)
    base = ce
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_rmean_21d_jerk_v037_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = _mean(ce, 21)
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_rmean_63d_jerk_v038_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = _mean(ce, 63)
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_rmean_126d_jerk_v039_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = _mean(ce, 126)
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_rmean_189d_jerk_v040_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = _mean(ce, 189)
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_rmean_252d_jerk_v041_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 252)
    base = _mean(ce, 252)
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_rmean_378d_jerk_v042_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 378)
    base = _mean(ce, 378)
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_z_21d_jerk_v043_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = _z(ce, 63)
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_z_63d_jerk_v044_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = _z(ce, 126)
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_z_126d_jerk_v045_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = _z(ce, 252)
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_z_189d_jerk_v046_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = _z(ce, 378)
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_z_252d_jerk_v047_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 252)
    base = _z(ce, 504)
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_z_378d_jerk_v048_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 378)
    base = _z(ce, 756)
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_sq_21d_jerk_v049_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = ce * ce.abs()
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_sq_63d_jerk_v050_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = ce * ce.abs()
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_sq_126d_jerk_v051_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = ce * ce.abs()
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_sq_189d_jerk_v052_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = ce * ce.abs()
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_sq_252d_jerk_v053_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 252)
    base = ce * ce.abs()
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_sq_378d_jerk_v054_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 378)
    base = ce * ce.abs()
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_absx_21d_jerk_v055_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = ce.abs() * np.sign(ce)
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_absx_63d_jerk_v056_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = ce.abs() * np.sign(ce)
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_absx_126d_jerk_v057_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = ce.abs() * np.sign(ce)
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_absx_189d_jerk_v058_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = ce.abs() * np.sign(ce)
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_absx_252d_jerk_v059_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 252)
    base = ce.abs() * np.sign(ce)
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cacef_absx_378d_jerk_v060_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 378)
    base = ce.abs() * np.sign(ce)
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_raw_21d_jerk_v061_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = ml
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_raw_63d_jerk_v062_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = ml
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_raw_126d_jerk_v063_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = ml
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_raw_189d_jerk_v064_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = ml
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_raw_252d_jerk_v065_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 252)
    base = ml
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_raw_378d_jerk_v066_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 378)
    base = ml
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rmean_21d_jerk_v067_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = _mean(ml, 21)
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rmean_63d_jerk_v068_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = _mean(ml, 63)
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rmean_126d_jerk_v069_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = _mean(ml, 126)
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rmean_189d_jerk_v070_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = _mean(ml, 189)
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rmean_252d_jerk_v071_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 252)
    base = _mean(ml, 252)
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rmean_378d_jerk_v072_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 378)
    base = _mean(ml, 378)
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_z_21d_jerk_v073_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = _z(ml, 63)
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_z_63d_jerk_v074_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = _z(ml, 126)
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_z_126d_jerk_v075_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = _z(ml, 252)
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_z_189d_jerk_v076_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = _z(ml, 378)
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_z_252d_jerk_v077_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 252)
    base = _z(ml, 504)
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_z_378d_jerk_v078_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 378)
    base = _z(ml, 756)
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_sq_21d_jerk_v079_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = ml * ml.abs()
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_sq_63d_jerk_v080_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = ml * ml.abs()
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_sq_126d_jerk_v081_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = ml * ml.abs()
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_sq_189d_jerk_v082_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = ml * ml.abs()
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_sq_252d_jerk_v083_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 252)
    base = ml * ml.abs()
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_sq_378d_jerk_v084_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 378)
    base = ml * ml.abs()
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rstd_21d_jerk_v085_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = _std(ml, 21)
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rstd_63d_jerk_v086_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = _std(ml, 63)
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rstd_126d_jerk_v087_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = _std(ml, 126)
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rstd_189d_jerk_v088_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = _std(ml, 189)
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rstd_252d_jerk_v089_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 252)
    base = _std(ml, 252)
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_mktlev_rstd_378d_jerk_v090_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 378)
    base = _std(ml, 378)
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rxce_mul_10d_jerk_v091_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ce = _f18_cac_efficiency(sgna, revenue, 10)
    base = s2r * ce
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rxce_mul_21d_jerk_v092_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = s2r * ce
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rxce_mul_42d_jerk_v093_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ce = _f18_cac_efficiency(sgna, revenue, 42)
    base = s2r * ce
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rxce_mul_63d_jerk_v094_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = s2r * ce
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rxce_mul_126d_jerk_v095_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = s2r * ce
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rxce_mul_189d_jerk_v096_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = s2r * ce
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cemml_diff_10d_jerk_v097_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 10)
    ml = _f18_marketing_leverage(sgna, revenue, 10)
    base = ce - ml
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cemml_diff_21d_jerk_v098_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = ce - ml
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cemml_diff_42d_jerk_v099_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 42)
    ml = _f18_marketing_leverage(sgna, revenue, 42)
    base = ce - ml
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cemml_diff_63d_jerk_v100_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = ce - ml
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cemml_diff_126d_jerk_v101_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = ce - ml
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_cemml_diff_189d_jerk_v102_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = ce - ml
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rpml_sum_10d_jerk_v103_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ml = _f18_marketing_leverage(sgna, revenue, 10)
    base = s2r + ml
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rpml_sum_21d_jerk_v104_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = s2r + ml
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rpml_sum_42d_jerk_v105_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ml = _f18_marketing_leverage(sgna, revenue, 42)
    base = s2r + ml
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rpml_sum_63d_jerk_v106_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = s2r + ml
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rpml_sum_126d_jerk_v107_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = s2r + ml
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2rpml_sum_189d_jerk_v108_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = s2r + ml
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_msstd_10d_jerk_v109_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 10)
    base = _mean(ce, 10) - _std(ce, 10)
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_msstd_21d_jerk_v110_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = _mean(ce, 21) - _std(ce, 21)
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_msstd_42d_jerk_v111_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 42)
    base = _mean(ce, 42) - _std(ce, 42)
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_msstd_63d_jerk_v112_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = _mean(ce, 63) - _std(ce, 63)
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_msstd_126d_jerk_v113_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = _mean(ce, 126) - _std(ce, 126)
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_msstd_189d_jerk_v114_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = _mean(ce, 189) - _std(ce, 189)
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dsmooth_10d_jerk_v115_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r.diff(10).rolling(10, min_periods=max(1,10//2)).mean()
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dsmooth_21d_jerk_v116_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r.diff(21).rolling(21, min_periods=max(1,21//2)).mean()
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dsmooth_42d_jerk_v117_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r.diff(42).rolling(42, min_periods=max(1,42//2)).mean()
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dsmooth_63d_jerk_v118_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r.diff(63).rolling(63, min_periods=max(1,63//2)).mean()
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dsmooth_126d_jerk_v119_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r.diff(126).rolling(126, min_periods=max(1,126//2)).mean()
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dsmooth_189d_jerk_v120_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = s2r.diff(189).rolling(189, min_periods=max(1,189//2)).mean()
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_ema_10d_jerk_v121_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 10)
    base = ce.ewm(span=10, min_periods=max(1, 10//2)).mean()
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_ema_21d_jerk_v122_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = ce.ewm(span=21, min_periods=max(1, 21//2)).mean()
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_ema_42d_jerk_v123_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 42)
    base = ce.ewm(span=42, min_periods=max(1, 42//2)).mean()
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_ema_63d_jerk_v124_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = ce.ewm(span=63, min_periods=max(1, 63//2)).mean()
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_ema_126d_jerk_v125_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = ce.ewm(span=126, min_periods=max(1, 126//2)).mean()
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_ema_189d_jerk_v126_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = ce.ewm(span=189, min_periods=max(1, 189//2)).mean()
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_range_10d_jerk_v127_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 10)
    base = ml.rolling(10, min_periods=max(1, 10//2)).max() - ml.rolling(10, min_periods=max(1, 10//2)).min()
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_range_21d_jerk_v128_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = ml.rolling(21, min_periods=max(1, 21//2)).max() - ml.rolling(21, min_periods=max(1, 21//2)).min()
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_range_42d_jerk_v129_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 42)
    base = ml.rolling(42, min_periods=max(1, 42//2)).max() - ml.rolling(42, min_periods=max(1, 42//2)).min()
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_range_63d_jerk_v130_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = ml.rolling(63, min_periods=max(1, 63//2)).max() - ml.rolling(63, min_periods=max(1, 63//2)).min()
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_range_126d_jerk_v131_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = ml.rolling(126, min_periods=max(1, 126//2)).max() - ml.rolling(126, min_periods=max(1, 126//2)).min()
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_range_189d_jerk_v132_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = ml.rolling(189, min_periods=max(1, 189//2)).max() - ml.rolling(189, min_periods=max(1, 189//2)).min()
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dmed_10d_jerk_v133_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = (s2r - s2r.rolling(10, min_periods=max(1, 10//2)).median())
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dmed_21d_jerk_v134_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = (s2r - s2r.rolling(21, min_periods=max(1, 21//2)).median())
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dmed_42d_jerk_v135_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = (s2r - s2r.rolling(42, min_periods=max(1, 42//2)).median())
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dmed_63d_jerk_v136_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = (s2r - s2r.rolling(63, min_periods=max(1, 63//2)).median())
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dmed_126d_jerk_v137_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = (s2r - s2r.rolling(126, min_periods=max(1, 126//2)).median())
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_s2r_dmed_189d_jerk_v138_signal(sgna, revenue, closeadj):
    s2r = _f18_sga_to_revenue(sgna, revenue)
    base = (s2r - s2r.rolling(189, min_periods=max(1, 189//2)).median())
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_iqr_10d_jerk_v139_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 10)
    base = ce.rolling(10, min_periods=max(1, 10//2)).quantile(0.75) - ce.rolling(10, min_periods=max(1, 10//2)).quantile(0.25)
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_iqr_21d_jerk_v140_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 21)
    base = ce.rolling(21, min_periods=max(1, 21//2)).quantile(0.75) - ce.rolling(21, min_periods=max(1, 21//2)).quantile(0.25)
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_iqr_42d_jerk_v141_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 42)
    base = ce.rolling(42, min_periods=max(1, 42//2)).quantile(0.75) - ce.rolling(42, min_periods=max(1, 42//2)).quantile(0.25)
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_iqr_63d_jerk_v142_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 63)
    base = ce.rolling(63, min_periods=max(1, 63//2)).quantile(0.75) - ce.rolling(63, min_periods=max(1, 63//2)).quantile(0.25)
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_iqr_126d_jerk_v143_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 126)
    base = ce.rolling(126, min_periods=max(1, 126//2)).quantile(0.75) - ce.rolling(126, min_periods=max(1, 126//2)).quantile(0.25)
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ce_iqr_189d_jerk_v144_signal(sgna, revenue, closeadj):
    ce = _f18_cac_efficiency(sgna, revenue, 189)
    base = ce.rolling(189, min_periods=max(1, 189//2)).quantile(0.75) - ce.rolling(189, min_periods=max(1, 189//2)).quantile(0.25)
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_iqr_10d_jerk_v145_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 10)
    base = ml.rolling(10, min_periods=max(1, 10//2)).quantile(0.75) - ml.rolling(10, min_periods=max(1, 10//2)).quantile(0.25)
    base_val = base * closeadj
    result = _jerk(base_val, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_iqr_21d_jerk_v146_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 21)
    base = ml.rolling(21, min_periods=max(1, 21//2)).quantile(0.75) - ml.rolling(21, min_periods=max(1, 21//2)).quantile(0.25)
    base_val = base * closeadj
    result = _jerk(base_val, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_iqr_42d_jerk_v147_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 42)
    base = ml.rolling(42, min_periods=max(1, 42//2)).quantile(0.75) - ml.rolling(42, min_periods=max(1, 42//2)).quantile(0.25)
    base_val = base * closeadj
    result = _jerk(base_val, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_iqr_63d_jerk_v148_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 63)
    base = ml.rolling(63, min_periods=max(1, 63//2)).quantile(0.75) - ml.rolling(63, min_periods=max(1, 63//2)).quantile(0.25)
    base_val = base * closeadj
    result = _jerk(base_val, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_iqr_126d_jerk_v149_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 126)
    base = ml.rolling(126, min_periods=max(1, 126//2)).quantile(0.75) - ml.rolling(126, min_periods=max(1, 126//2)).quantile(0.25)
    base_val = base * closeadj
    result = _jerk(base_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f18dce_f18_digital_cac_efficiency_ml_iqr_189d_jerk_v150_signal(sgna, revenue, closeadj):
    ml = _f18_marketing_leverage(sgna, revenue, 189)
    base = ml.rolling(189, min_periods=max(1, 189//2)).quantile(0.75) - ml.rolling(189, min_periods=max(1, 189//2)).quantile(0.25)
    base_val = base * closeadj
    result = _jerk(base_val, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_21d_jerk_v001_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_63d_jerk_v002_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_126d_jerk_v003_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_189d_jerk_v004_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_252d_jerk_v005_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_xclmean_378d_jerk_v006_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rmean_21d_jerk_v007_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rmean_63d_jerk_v008_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rmean_126d_jerk_v009_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rmean_189d_jerk_v010_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rmean_252d_jerk_v011_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rmean_378d_jerk_v012_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rstd_21d_jerk_v013_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rstd_63d_jerk_v014_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rstd_126d_jerk_v015_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rstd_189d_jerk_v016_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rstd_252d_jerk_v017_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_rstd_378d_jerk_v018_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_z_21d_jerk_v019_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_z_63d_jerk_v020_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_z_126d_jerk_v021_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_z_189d_jerk_v022_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_z_252d_jerk_v023_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_z_378d_jerk_v024_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_diff_21d_jerk_v025_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_diff_63d_jerk_v026_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_diff_126d_jerk_v027_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_diff_189d_jerk_v028_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_diff_252d_jerk_v029_signal,
    f18dce_f18_digital_cac_efficiency_sgnarev_diff_378d_jerk_v030_signal,
    f18dce_f18_digital_cac_efficiency_cacef_raw_21d_jerk_v031_signal,
    f18dce_f18_digital_cac_efficiency_cacef_raw_63d_jerk_v032_signal,
    f18dce_f18_digital_cac_efficiency_cacef_raw_126d_jerk_v033_signal,
    f18dce_f18_digital_cac_efficiency_cacef_raw_189d_jerk_v034_signal,
    f18dce_f18_digital_cac_efficiency_cacef_raw_252d_jerk_v035_signal,
    f18dce_f18_digital_cac_efficiency_cacef_raw_378d_jerk_v036_signal,
    f18dce_f18_digital_cac_efficiency_cacef_rmean_21d_jerk_v037_signal,
    f18dce_f18_digital_cac_efficiency_cacef_rmean_63d_jerk_v038_signal,
    f18dce_f18_digital_cac_efficiency_cacef_rmean_126d_jerk_v039_signal,
    f18dce_f18_digital_cac_efficiency_cacef_rmean_189d_jerk_v040_signal,
    f18dce_f18_digital_cac_efficiency_cacef_rmean_252d_jerk_v041_signal,
    f18dce_f18_digital_cac_efficiency_cacef_rmean_378d_jerk_v042_signal,
    f18dce_f18_digital_cac_efficiency_cacef_z_21d_jerk_v043_signal,
    f18dce_f18_digital_cac_efficiency_cacef_z_63d_jerk_v044_signal,
    f18dce_f18_digital_cac_efficiency_cacef_z_126d_jerk_v045_signal,
    f18dce_f18_digital_cac_efficiency_cacef_z_189d_jerk_v046_signal,
    f18dce_f18_digital_cac_efficiency_cacef_z_252d_jerk_v047_signal,
    f18dce_f18_digital_cac_efficiency_cacef_z_378d_jerk_v048_signal,
    f18dce_f18_digital_cac_efficiency_cacef_sq_21d_jerk_v049_signal,
    f18dce_f18_digital_cac_efficiency_cacef_sq_63d_jerk_v050_signal,
    f18dce_f18_digital_cac_efficiency_cacef_sq_126d_jerk_v051_signal,
    f18dce_f18_digital_cac_efficiency_cacef_sq_189d_jerk_v052_signal,
    f18dce_f18_digital_cac_efficiency_cacef_sq_252d_jerk_v053_signal,
    f18dce_f18_digital_cac_efficiency_cacef_sq_378d_jerk_v054_signal,
    f18dce_f18_digital_cac_efficiency_cacef_absx_21d_jerk_v055_signal,
    f18dce_f18_digital_cac_efficiency_cacef_absx_63d_jerk_v056_signal,
    f18dce_f18_digital_cac_efficiency_cacef_absx_126d_jerk_v057_signal,
    f18dce_f18_digital_cac_efficiency_cacef_absx_189d_jerk_v058_signal,
    f18dce_f18_digital_cac_efficiency_cacef_absx_252d_jerk_v059_signal,
    f18dce_f18_digital_cac_efficiency_cacef_absx_378d_jerk_v060_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_raw_21d_jerk_v061_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_raw_63d_jerk_v062_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_raw_126d_jerk_v063_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_raw_189d_jerk_v064_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_raw_252d_jerk_v065_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_raw_378d_jerk_v066_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rmean_21d_jerk_v067_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rmean_63d_jerk_v068_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rmean_126d_jerk_v069_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rmean_189d_jerk_v070_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rmean_252d_jerk_v071_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rmean_378d_jerk_v072_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_z_21d_jerk_v073_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_z_63d_jerk_v074_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_z_126d_jerk_v075_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_z_189d_jerk_v076_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_z_252d_jerk_v077_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_z_378d_jerk_v078_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_sq_21d_jerk_v079_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_sq_63d_jerk_v080_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_sq_126d_jerk_v081_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_sq_189d_jerk_v082_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_sq_252d_jerk_v083_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_sq_378d_jerk_v084_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rstd_21d_jerk_v085_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rstd_63d_jerk_v086_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rstd_126d_jerk_v087_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rstd_189d_jerk_v088_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rstd_252d_jerk_v089_signal,
    f18dce_f18_digital_cac_efficiency_mktlev_rstd_378d_jerk_v090_signal,
    f18dce_f18_digital_cac_efficiency_s2rxce_mul_10d_jerk_v091_signal,
    f18dce_f18_digital_cac_efficiency_s2rxce_mul_21d_jerk_v092_signal,
    f18dce_f18_digital_cac_efficiency_s2rxce_mul_42d_jerk_v093_signal,
    f18dce_f18_digital_cac_efficiency_s2rxce_mul_63d_jerk_v094_signal,
    f18dce_f18_digital_cac_efficiency_s2rxce_mul_126d_jerk_v095_signal,
    f18dce_f18_digital_cac_efficiency_s2rxce_mul_189d_jerk_v096_signal,
    f18dce_f18_digital_cac_efficiency_cemml_diff_10d_jerk_v097_signal,
    f18dce_f18_digital_cac_efficiency_cemml_diff_21d_jerk_v098_signal,
    f18dce_f18_digital_cac_efficiency_cemml_diff_42d_jerk_v099_signal,
    f18dce_f18_digital_cac_efficiency_cemml_diff_63d_jerk_v100_signal,
    f18dce_f18_digital_cac_efficiency_cemml_diff_126d_jerk_v101_signal,
    f18dce_f18_digital_cac_efficiency_cemml_diff_189d_jerk_v102_signal,
    f18dce_f18_digital_cac_efficiency_s2rpml_sum_10d_jerk_v103_signal,
    f18dce_f18_digital_cac_efficiency_s2rpml_sum_21d_jerk_v104_signal,
    f18dce_f18_digital_cac_efficiency_s2rpml_sum_42d_jerk_v105_signal,
    f18dce_f18_digital_cac_efficiency_s2rpml_sum_63d_jerk_v106_signal,
    f18dce_f18_digital_cac_efficiency_s2rpml_sum_126d_jerk_v107_signal,
    f18dce_f18_digital_cac_efficiency_s2rpml_sum_189d_jerk_v108_signal,
    f18dce_f18_digital_cac_efficiency_ce_msstd_10d_jerk_v109_signal,
    f18dce_f18_digital_cac_efficiency_ce_msstd_21d_jerk_v110_signal,
    f18dce_f18_digital_cac_efficiency_ce_msstd_42d_jerk_v111_signal,
    f18dce_f18_digital_cac_efficiency_ce_msstd_63d_jerk_v112_signal,
    f18dce_f18_digital_cac_efficiency_ce_msstd_126d_jerk_v113_signal,
    f18dce_f18_digital_cac_efficiency_ce_msstd_189d_jerk_v114_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dsmooth_10d_jerk_v115_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dsmooth_21d_jerk_v116_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dsmooth_42d_jerk_v117_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dsmooth_63d_jerk_v118_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dsmooth_126d_jerk_v119_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dsmooth_189d_jerk_v120_signal,
    f18dce_f18_digital_cac_efficiency_ce_ema_10d_jerk_v121_signal,
    f18dce_f18_digital_cac_efficiency_ce_ema_21d_jerk_v122_signal,
    f18dce_f18_digital_cac_efficiency_ce_ema_42d_jerk_v123_signal,
    f18dce_f18_digital_cac_efficiency_ce_ema_63d_jerk_v124_signal,
    f18dce_f18_digital_cac_efficiency_ce_ema_126d_jerk_v125_signal,
    f18dce_f18_digital_cac_efficiency_ce_ema_189d_jerk_v126_signal,
    f18dce_f18_digital_cac_efficiency_ml_range_10d_jerk_v127_signal,
    f18dce_f18_digital_cac_efficiency_ml_range_21d_jerk_v128_signal,
    f18dce_f18_digital_cac_efficiency_ml_range_42d_jerk_v129_signal,
    f18dce_f18_digital_cac_efficiency_ml_range_63d_jerk_v130_signal,
    f18dce_f18_digital_cac_efficiency_ml_range_126d_jerk_v131_signal,
    f18dce_f18_digital_cac_efficiency_ml_range_189d_jerk_v132_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dmed_10d_jerk_v133_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dmed_21d_jerk_v134_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dmed_42d_jerk_v135_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dmed_63d_jerk_v136_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dmed_126d_jerk_v137_signal,
    f18dce_f18_digital_cac_efficiency_s2r_dmed_189d_jerk_v138_signal,
    f18dce_f18_digital_cac_efficiency_ce_iqr_10d_jerk_v139_signal,
    f18dce_f18_digital_cac_efficiency_ce_iqr_21d_jerk_v140_signal,
    f18dce_f18_digital_cac_efficiency_ce_iqr_42d_jerk_v141_signal,
    f18dce_f18_digital_cac_efficiency_ce_iqr_63d_jerk_v142_signal,
    f18dce_f18_digital_cac_efficiency_ce_iqr_126d_jerk_v143_signal,
    f18dce_f18_digital_cac_efficiency_ce_iqr_189d_jerk_v144_signal,
    f18dce_f18_digital_cac_efficiency_ml_iqr_10d_jerk_v145_signal,
    f18dce_f18_digital_cac_efficiency_ml_iqr_21d_jerk_v146_signal,
    f18dce_f18_digital_cac_efficiency_ml_iqr_42d_jerk_v147_signal,
    f18dce_f18_digital_cac_efficiency_ml_iqr_63d_jerk_v148_signal,
    f18dce_f18_digital_cac_efficiency_ml_iqr_126d_jerk_v149_signal,
    f18dce_f18_digital_cac_efficiency_ml_iqr_189d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FDIGITAL_CAC_EFFICIENCY_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f18_digital_cac_efficiency_3rd_derivatives_001_150_claude: {n_features} features pass")
