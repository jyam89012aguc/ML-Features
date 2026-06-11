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
def _f077_signflip(s, n):
    return (np.sign(s) != np.sign(s.shift(n))).astype(float)


# 21d acceleration of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_accel_21d_3d_v001_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_accel_63d_3d_v002_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_accel_126d_3d_v003_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_accel_252d_3d_v004_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_accel_21d_3d_v005_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_accel_63d_3d_v006_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_accel_126d_3d_v007_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_accel_252d_3d_v008_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_accel_21d_3d_v009_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_accel_63d_3d_v010_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_accel_126d_3d_v011_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_accel_252d_3d_v012_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ni_signflip
def f077rch_f077_regime_change_ni_signflip_accel_21d_3d_v013_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ni_signflip
def f077rch_f077_regime_change_ni_signflip_accel_63d_3d_v014_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ni_signflip
def f077rch_f077_regime_change_ni_signflip_accel_126d_3d_v015_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ni_signflip
def f077rch_f077_regime_change_ni_signflip_accel_252d_3d_v016_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_accel_21d_3d_v017_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_accel_63d_3d_v018_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_accel_126d_3d_v019_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_accel_252d_3d_v020_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_accel_21d_3d_v021_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_accel_63d_3d_v022_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_accel_126d_3d_v023_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_accel_252d_3d_v024_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of regime_score
def f077rch_f077_regime_change_regime_score_accel_21d_3d_v025_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of regime_score
def f077rch_f077_regime_change_regime_score_accel_63d_3d_v026_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of regime_score
def f077rch_f077_regime_change_regime_score_accel_126d_3d_v027_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of regime_score
def f077rch_f077_regime_change_regime_score_accel_252d_3d_v028_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_slopez_21d_z126_3d_v029_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_slopez_63d_z252_3d_v030_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_slopez_126d_z252_3d_v031_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_slopez_252d_z504_3d_v032_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_slopez_21d_z126_3d_v033_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_slopez_63d_z252_3d_v034_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_slopez_126d_z252_3d_v035_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_slopez_252d_z504_3d_v036_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_slopez_21d_z126_3d_v037_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_slopez_63d_z252_3d_v038_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_slopez_126d_z252_3d_v039_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_slopez_252d_z504_3d_v040_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ni_signflip
def f077rch_f077_regime_change_ni_signflip_slopez_21d_z126_3d_v041_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ni_signflip
def f077rch_f077_regime_change_ni_signflip_slopez_63d_z252_3d_v042_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ni_signflip
def f077rch_f077_regime_change_ni_signflip_slopez_126d_z252_3d_v043_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ni_signflip
def f077rch_f077_regime_change_ni_signflip_slopez_252d_z504_3d_v044_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_slopez_21d_z126_3d_v045_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_slopez_63d_z252_3d_v046_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_slopez_126d_z252_3d_v047_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_slopez_252d_z504_3d_v048_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_slopez_21d_z126_3d_v049_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_slopez_63d_z252_3d_v050_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_slopez_126d_z252_3d_v051_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_slopez_252d_z504_3d_v052_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of regime_score
def f077rch_f077_regime_change_regime_score_slopez_21d_z126_3d_v053_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of regime_score
def f077rch_f077_regime_change_regime_score_slopez_63d_z252_3d_v054_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of regime_score
def f077rch_f077_regime_change_regime_score_slopez_126d_z252_3d_v055_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of regime_score
def f077rch_f077_regime_change_regime_score_slopez_252d_z504_3d_v056_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_jerk_21d_3d_v057_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_jerk_63d_3d_v058_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_jerk_126d_3d_v059_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_jerk_21d_3d_v060_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_jerk_63d_3d_v061_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_jerk_126d_3d_v062_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_jerk_21d_3d_v063_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_jerk_63d_3d_v064_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_jerk_126d_3d_v065_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ni_signflip
def f077rch_f077_regime_change_ni_signflip_jerk_21d_3d_v066_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ni_signflip
def f077rch_f077_regime_change_ni_signflip_jerk_63d_3d_v067_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ni_signflip
def f077rch_f077_regime_change_ni_signflip_jerk_126d_3d_v068_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_jerk_21d_3d_v069_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_jerk_63d_3d_v070_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_jerk_126d_3d_v071_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_jerk_21d_3d_v072_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_jerk_63d_3d_v073_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_jerk_126d_3d_v074_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of regime_score
def f077rch_f077_regime_change_regime_score_jerk_21d_3d_v075_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of regime_score
def f077rch_f077_regime_change_regime_score_jerk_63d_3d_v076_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of regime_score
def f077rch_f077_regime_change_regime_score_jerk_126d_3d_v077_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_growth_signflip smoothed over 252d
def f077rch_f077_regime_change_rev_growth_signflip_smoothaccel_63d_sm252_3d_v078_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_growth_signflip smoothed over 504d
def f077rch_f077_regime_change_rev_growth_signflip_smoothaccel_252d_sm504_3d_v079_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_signflip smoothed over 252d
def f077rch_f077_regime_change_ocf_signflip_smoothaccel_63d_sm252_3d_v080_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_signflip smoothed over 504d
def f077rch_f077_regime_change_ocf_signflip_smoothaccel_252d_sm504_3d_v081_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of fcf_signflip smoothed over 252d
def f077rch_f077_regime_change_fcf_signflip_smoothaccel_63d_sm252_3d_v082_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of fcf_signflip smoothed over 504d
def f077rch_f077_regime_change_fcf_signflip_smoothaccel_252d_sm504_3d_v083_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ni_signflip smoothed over 252d
def f077rch_f077_regime_change_ni_signflip_smoothaccel_63d_sm252_3d_v084_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ni_signflip smoothed over 504d
def f077rch_f077_regime_change_ni_signflip_smoothaccel_252d_sm504_3d_v085_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of opinc_signflip smoothed over 252d
def f077rch_f077_regime_change_opinc_signflip_smoothaccel_63d_sm252_3d_v086_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of opinc_signflip smoothed over 504d
def f077rch_f077_regime_change_opinc_signflip_smoothaccel_252d_sm504_3d_v087_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_step_change smoothed over 252d
def f077rch_f077_regime_change_rnd_step_change_smoothaccel_63d_sm252_3d_v088_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_step_change smoothed over 504d
def f077rch_f077_regime_change_rnd_step_change_smoothaccel_252d_sm504_3d_v089_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of regime_score smoothed over 252d
def f077rch_f077_regime_change_regime_score_smoothaccel_63d_sm252_3d_v090_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of regime_score smoothed over 504d
def f077rch_f077_regime_change_regime_score_smoothaccel_252d_sm504_3d_v091_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_accelz_21d_z252_3d_v092_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_accelz_63d_z504_3d_v093_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_accelz_21d_z252_3d_v094_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_accelz_63d_z504_3d_v095_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_accelz_21d_z252_3d_v096_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_accelz_63d_z504_3d_v097_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ni_signflip
def f077rch_f077_regime_change_ni_signflip_accelz_21d_z252_3d_v098_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ni_signflip
def f077rch_f077_regime_change_ni_signflip_accelz_63d_z504_3d_v099_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_accelz_21d_z252_3d_v100_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_accelz_63d_z504_3d_v101_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_accelz_21d_z252_3d_v102_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_accelz_63d_z504_3d_v103_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of regime_score
def f077rch_f077_regime_change_regime_score_accelz_21d_z252_3d_v104_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of regime_score
def f077rch_f077_regime_change_regime_score_accelz_63d_z504_3d_v105_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_growth_signflip (raw count, no price scaling)
def f077rch_f077_regime_change_rev_growth_signflip_signflip_63d_3d_v106_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_growth_signflip (raw count, no price scaling)
def f077rch_f077_regime_change_rev_growth_signflip_signflip_252d_3d_v107_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_signflip (raw count, no price scaling)
def f077rch_f077_regime_change_ocf_signflip_signflip_63d_3d_v108_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_signflip (raw count, no price scaling)
def f077rch_f077_regime_change_ocf_signflip_signflip_252d_3d_v109_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in fcf_signflip (raw count, no price scaling)
def f077rch_f077_regime_change_fcf_signflip_signflip_63d_3d_v110_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in fcf_signflip (raw count, no price scaling)
def f077rch_f077_regime_change_fcf_signflip_signflip_252d_3d_v111_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ni_signflip (raw count, no price scaling)
def f077rch_f077_regime_change_ni_signflip_signflip_63d_3d_v112_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ni_signflip (raw count, no price scaling)
def f077rch_f077_regime_change_ni_signflip_signflip_252d_3d_v113_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in opinc_signflip (raw count, no price scaling)
def f077rch_f077_regime_change_opinc_signflip_signflip_63d_3d_v114_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in opinc_signflip (raw count, no price scaling)
def f077rch_f077_regime_change_opinc_signflip_signflip_252d_3d_v115_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rnd_step_change (raw count, no price scaling)
def f077rch_f077_regime_change_rnd_step_change_signflip_63d_3d_v116_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rnd_step_change (raw count, no price scaling)
def f077rch_f077_regime_change_rnd_step_change_signflip_252d_3d_v117_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in regime_score (raw count, no price scaling)
def f077rch_f077_regime_change_regime_score_signflip_63d_3d_v118_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in regime_score (raw count, no price scaling)
def f077rch_f077_regime_change_regime_score_signflip_252d_3d_v119_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_growth_signflip normalized by 252d range
def f077rch_f077_regime_change_rev_growth_signflip_rngaccel_63d_r252_3d_v120_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_growth_signflip normalized by 504d range
def f077rch_f077_regime_change_rev_growth_signflip_rngaccel_252d_r504_3d_v121_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_signflip normalized by 252d range
def f077rch_f077_regime_change_ocf_signflip_rngaccel_63d_r252_3d_v122_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_signflip normalized by 504d range
def f077rch_f077_regime_change_ocf_signflip_rngaccel_252d_r504_3d_v123_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_signflip normalized by 252d range
def f077rch_f077_regime_change_fcf_signflip_rngaccel_63d_r252_3d_v124_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_signflip normalized by 504d range
def f077rch_f077_regime_change_fcf_signflip_rngaccel_252d_r504_3d_v125_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ni_signflip normalized by 252d range
def f077rch_f077_regime_change_ni_signflip_rngaccel_63d_r252_3d_v126_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ni_signflip normalized by 504d range
def f077rch_f077_regime_change_ni_signflip_rngaccel_252d_r504_3d_v127_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of opinc_signflip normalized by 252d range
def f077rch_f077_regime_change_opinc_signflip_rngaccel_63d_r252_3d_v128_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of opinc_signflip normalized by 504d range
def f077rch_f077_regime_change_opinc_signflip_rngaccel_252d_r504_3d_v129_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_step_change normalized by 252d range
def f077rch_f077_regime_change_rnd_step_change_rngaccel_63d_r252_3d_v130_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_step_change normalized by 504d range
def f077rch_f077_regime_change_rnd_step_change_rngaccel_252d_r504_3d_v131_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of regime_score normalized by 252d range
def f077rch_f077_regime_change_regime_score_rngaccel_63d_r252_3d_v132_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of regime_score normalized by 504d range
def f077rch_f077_regime_change_regime_score_rngaccel_252d_r504_3d_v133_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_cumslope_21d_3d_v134_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_cumslope_63d_3d_v135_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_cumslope_252d_3d_v136_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_cumslope_21d_3d_v137_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_cumslope_63d_3d_v138_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_cumslope_252d_3d_v139_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_cumslope_21d_3d_v140_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_cumslope_63d_3d_v141_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_cumslope_252d_3d_v142_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ni_signflip
def f077rch_f077_regime_change_ni_signflip_cumslope_21d_3d_v143_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ni_signflip
def f077rch_f077_regime_change_ni_signflip_cumslope_63d_3d_v144_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ni_signflip
def f077rch_f077_regime_change_ni_signflip_cumslope_252d_3d_v145_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_cumslope_21d_3d_v146_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_cumslope_63d_3d_v147_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_cumslope_252d_3d_v148_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_cumslope_21d_3d_v149_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_cumslope_63d_3d_v150_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

