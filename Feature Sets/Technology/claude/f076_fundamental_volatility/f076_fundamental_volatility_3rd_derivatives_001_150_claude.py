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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f076_vol(s, w):
    return s.rolling(w, min_periods=max(1, w//2)).std()


# 21d acceleration of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_accel_21d_3d_v001_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_accel_63d_3d_v002_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_accel_126d_3d_v003_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_accel_252d_3d_v004_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_accel_21d_3d_v005_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_accel_63d_3d_v006_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_accel_126d_3d_v007_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_accel_252d_3d_v008_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_accel_21d_3d_v009_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_accel_63d_3d_v010_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_accel_126d_3d_v011_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_accel_252d_3d_v012_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_accel_21d_3d_v013_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_accel_63d_3d_v014_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_accel_126d_3d_v015_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_accel_252d_3d_v016_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_accel_21d_3d_v017_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_accel_63d_3d_v018_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_accel_126d_3d_v019_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_accel_252d_3d_v020_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_accel_21d_3d_v021_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_accel_63d_3d_v022_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_accel_126d_3d_v023_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_accel_252d_3d_v024_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_accel_21d_3d_v025_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_accel_63d_3d_v026_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_accel_126d_3d_v027_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_accel_252d_3d_v028_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_slopez_21d_z126_3d_v029_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_slopez_63d_z252_3d_v030_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_slopez_126d_z252_3d_v031_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_slopez_252d_z504_3d_v032_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_slopez_21d_z126_3d_v033_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_slopez_63d_z252_3d_v034_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_slopez_126d_z252_3d_v035_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_slopez_252d_z504_3d_v036_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_slopez_21d_z126_3d_v037_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_slopez_63d_z252_3d_v038_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_slopez_126d_z252_3d_v039_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_slopez_252d_z504_3d_v040_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_slopez_21d_z126_3d_v041_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_slopez_63d_z252_3d_v042_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_slopez_126d_z252_3d_v043_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_slopez_252d_z504_3d_v044_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_slopez_21d_z126_3d_v045_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_slopez_63d_z252_3d_v046_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_slopez_126d_z252_3d_v047_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_slopez_252d_z504_3d_v048_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_slopez_21d_z126_3d_v049_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_slopez_63d_z252_3d_v050_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_slopez_126d_z252_3d_v051_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_slopez_252d_z504_3d_v052_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_slopez_21d_z126_3d_v053_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_slopez_63d_z252_3d_v054_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_slopez_126d_z252_3d_v055_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_slopez_252d_z504_3d_v056_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_jerk_21d_3d_v057_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_jerk_63d_3d_v058_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_jerk_126d_3d_v059_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_jerk_21d_3d_v060_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_jerk_63d_3d_v061_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_jerk_126d_3d_v062_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_jerk_21d_3d_v063_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_jerk_63d_3d_v064_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_jerk_126d_3d_v065_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_jerk_21d_3d_v066_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_jerk_63d_3d_v067_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_jerk_126d_3d_v068_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_jerk_21d_3d_v069_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_jerk_63d_3d_v070_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_jerk_126d_3d_v071_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_jerk_21d_3d_v072_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_jerk_63d_3d_v073_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_jerk_126d_3d_v074_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_jerk_21d_3d_v075_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_jerk_63d_3d_v076_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_jerk_126d_3d_v077_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_vol_252 smoothed over 252d
def f076fvl_f076_fundamental_volatility_rev_vol_252_smoothaccel_63d_sm252_3d_v078_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_vol_252 smoothed over 504d
def f076fvl_f076_fundamental_volatility_rev_vol_252_smoothaccel_252d_sm504_3d_v079_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_vol_252 smoothed over 252d
def f076fvl_f076_fundamental_volatility_ocf_vol_252_smoothaccel_63d_sm252_3d_v080_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_vol_252 smoothed over 504d
def f076fvl_f076_fundamental_volatility_ocf_vol_252_smoothaccel_252d_sm504_3d_v081_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_vol_252 smoothed over 252d
def f076fvl_f076_fundamental_volatility_rnd_vol_252_smoothaccel_63d_sm252_3d_v082_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_vol_252 smoothed over 504d
def f076fvl_f076_fundamental_volatility_rnd_vol_252_smoothaccel_252d_sm504_3d_v083_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ni_vol_252 smoothed over 252d
def f076fvl_f076_fundamental_volatility_ni_vol_252_smoothaccel_63d_sm252_3d_v084_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ni_vol_252 smoothed over 504d
def f076fvl_f076_fundamental_volatility_ni_vol_252_smoothaccel_252d_sm504_3d_v085_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of opinc_vol_252 smoothed over 252d
def f076fvl_f076_fundamental_volatility_opinc_vol_252_smoothaccel_63d_sm252_3d_v086_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of opinc_vol_252 smoothed over 504d
def f076fvl_f076_fundamental_volatility_opinc_vol_252_smoothaccel_252d_sm504_3d_v087_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_cv_504 smoothed over 252d
def f076fvl_f076_fundamental_volatility_rev_cv_504_smoothaccel_63d_sm252_3d_v088_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_cv_504 smoothed over 504d
def f076fvl_f076_fundamental_volatility_rev_cv_504_smoothaccel_252d_sm504_3d_v089_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of stability_score smoothed over 252d
def f076fvl_f076_fundamental_volatility_stability_score_smoothaccel_63d_sm252_3d_v090_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of stability_score smoothed over 504d
def f076fvl_f076_fundamental_volatility_stability_score_smoothaccel_252d_sm504_3d_v091_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_accelz_21d_z252_3d_v092_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_accelz_63d_z504_3d_v093_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_accelz_21d_z252_3d_v094_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_accelz_63d_z504_3d_v095_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_accelz_21d_z252_3d_v096_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_accelz_63d_z504_3d_v097_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_accelz_21d_z252_3d_v098_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_accelz_63d_z504_3d_v099_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_accelz_21d_z252_3d_v100_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_accelz_63d_z504_3d_v101_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_accelz_21d_z252_3d_v102_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_accelz_63d_z504_3d_v103_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_accelz_21d_z252_3d_v104_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of stability_score
def f076fvl_f076_fundamental_volatility_stability_score_accelz_63d_z504_3d_v105_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_vol_252 (raw count, no price scaling)
def f076fvl_f076_fundamental_volatility_rev_vol_252_signflip_63d_3d_v106_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_vol_252 (raw count, no price scaling)
def f076fvl_f076_fundamental_volatility_rev_vol_252_signflip_252d_3d_v107_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_vol_252 (raw count, no price scaling)
def f076fvl_f076_fundamental_volatility_ocf_vol_252_signflip_63d_3d_v108_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_vol_252 (raw count, no price scaling)
def f076fvl_f076_fundamental_volatility_ocf_vol_252_signflip_252d_3d_v109_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rnd_vol_252 (raw count, no price scaling)
def f076fvl_f076_fundamental_volatility_rnd_vol_252_signflip_63d_3d_v110_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rnd_vol_252 (raw count, no price scaling)
def f076fvl_f076_fundamental_volatility_rnd_vol_252_signflip_252d_3d_v111_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ni_vol_252 (raw count, no price scaling)
def f076fvl_f076_fundamental_volatility_ni_vol_252_signflip_63d_3d_v112_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ni_vol_252 (raw count, no price scaling)
def f076fvl_f076_fundamental_volatility_ni_vol_252_signflip_252d_3d_v113_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in opinc_vol_252 (raw count, no price scaling)
def f076fvl_f076_fundamental_volatility_opinc_vol_252_signflip_63d_3d_v114_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in opinc_vol_252 (raw count, no price scaling)
def f076fvl_f076_fundamental_volatility_opinc_vol_252_signflip_252d_3d_v115_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_cv_504 (raw count, no price scaling)
def f076fvl_f076_fundamental_volatility_rev_cv_504_signflip_63d_3d_v116_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_cv_504 (raw count, no price scaling)
def f076fvl_f076_fundamental_volatility_rev_cv_504_signflip_252d_3d_v117_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in stability_score (raw count, no price scaling)
def f076fvl_f076_fundamental_volatility_stability_score_signflip_63d_3d_v118_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in stability_score (raw count, no price scaling)
def f076fvl_f076_fundamental_volatility_stability_score_signflip_252d_3d_v119_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_vol_252 normalized by 252d range
def f076fvl_f076_fundamental_volatility_rev_vol_252_rngaccel_63d_r252_3d_v120_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_vol_252 normalized by 504d range
def f076fvl_f076_fundamental_volatility_rev_vol_252_rngaccel_252d_r504_3d_v121_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_vol_252 normalized by 252d range
def f076fvl_f076_fundamental_volatility_ocf_vol_252_rngaccel_63d_r252_3d_v122_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_vol_252 normalized by 504d range
def f076fvl_f076_fundamental_volatility_ocf_vol_252_rngaccel_252d_r504_3d_v123_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_vol_252 normalized by 252d range
def f076fvl_f076_fundamental_volatility_rnd_vol_252_rngaccel_63d_r252_3d_v124_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_vol_252 normalized by 504d range
def f076fvl_f076_fundamental_volatility_rnd_vol_252_rngaccel_252d_r504_3d_v125_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ni_vol_252 normalized by 252d range
def f076fvl_f076_fundamental_volatility_ni_vol_252_rngaccel_63d_r252_3d_v126_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ni_vol_252 normalized by 504d range
def f076fvl_f076_fundamental_volatility_ni_vol_252_rngaccel_252d_r504_3d_v127_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of opinc_vol_252 normalized by 252d range
def f076fvl_f076_fundamental_volatility_opinc_vol_252_rngaccel_63d_r252_3d_v128_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of opinc_vol_252 normalized by 504d range
def f076fvl_f076_fundamental_volatility_opinc_vol_252_rngaccel_252d_r504_3d_v129_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_cv_504 normalized by 252d range
def f076fvl_f076_fundamental_volatility_rev_cv_504_rngaccel_63d_r252_3d_v130_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_cv_504 normalized by 504d range
def f076fvl_f076_fundamental_volatility_rev_cv_504_rngaccel_252d_r504_3d_v131_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of stability_score normalized by 252d range
def f076fvl_f076_fundamental_volatility_stability_score_rngaccel_63d_r252_3d_v132_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of stability_score normalized by 504d range
def f076fvl_f076_fundamental_volatility_stability_score_rngaccel_252d_r504_3d_v133_signal(revenue, closeadj):
    base = -_f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_cumslope_21d_3d_v134_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_cumslope_63d_3d_v135_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_vol_252
def f076fvl_f076_fundamental_volatility_rev_vol_252_cumslope_252d_3d_v136_signal(revenue, closeadj):
    base = _f076_vol(revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_cumslope_21d_3d_v137_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_cumslope_63d_3d_v138_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ocf_vol_252
def f076fvl_f076_fundamental_volatility_ocf_vol_252_cumslope_252d_3d_v139_signal(ncfo, closeadj):
    base = _f076_vol(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_cumslope_21d_3d_v140_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_cumslope_63d_3d_v141_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rnd_vol_252
def f076fvl_f076_fundamental_volatility_rnd_vol_252_cumslope_252d_3d_v142_signal(rnd, closeadj):
    base = _f076_vol(rnd, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_cumslope_21d_3d_v143_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_cumslope_63d_3d_v144_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ni_vol_252
def f076fvl_f076_fundamental_volatility_ni_vol_252_cumslope_252d_3d_v145_signal(netinc, closeadj):
    base = _f076_vol(netinc, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_cumslope_21d_3d_v146_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_cumslope_63d_3d_v147_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of opinc_vol_252
def f076fvl_f076_fundamental_volatility_opinc_vol_252_cumslope_252d_3d_v148_signal(opinc, closeadj):
    base = _f076_vol(opinc, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_cumslope_21d_3d_v149_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_cv_504
def f076fvl_f076_fundamental_volatility_rev_cv_504_cumslope_63d_3d_v150_signal(revenue, closeadj):
    base = _f076_vol(revenue, 504) / revenue.rolling(504, min_periods=126).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

