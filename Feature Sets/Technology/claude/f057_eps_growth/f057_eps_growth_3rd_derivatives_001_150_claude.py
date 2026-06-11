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
def _f057_eps_chg(eps, n):
    return eps.diff(periods=n)


# 21d acceleration of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_accel_21d_3d_v001_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_accel_63d_3d_v002_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_accel_126d_3d_v003_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_accel_252d_3d_v004_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_accel_21d_3d_v005_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_accel_63d_3d_v006_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_accel_126d_3d_v007_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_accel_252d_3d_v008_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_accel_21d_3d_v009_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_accel_63d_3d_v010_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_accel_126d_3d_v011_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_accel_252d_3d_v012_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_accel_21d_3d_v013_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_accel_63d_3d_v014_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_accel_126d_3d_v015_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_accel_252d_3d_v016_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_accel_21d_3d_v017_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_accel_63d_3d_v018_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_accel_126d_3d_v019_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_accel_252d_3d_v020_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_accel_21d_3d_v021_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_accel_63d_3d_v022_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_accel_126d_3d_v023_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_accel_252d_3d_v024_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_accel_21d_3d_v025_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_accel_63d_3d_v026_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_accel_126d_3d_v027_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_accel_252d_3d_v028_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_slopez_21d_z126_3d_v029_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_slopez_63d_z252_3d_v030_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_slopez_126d_z252_3d_v031_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_slopez_252d_z504_3d_v032_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_slopez_21d_z126_3d_v033_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_slopez_63d_z252_3d_v034_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_slopez_126d_z252_3d_v035_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_slopez_252d_z504_3d_v036_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_slopez_21d_z126_3d_v037_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_slopez_63d_z252_3d_v038_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_slopez_126d_z252_3d_v039_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_slopez_252d_z504_3d_v040_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_slopez_21d_z126_3d_v041_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_slopez_63d_z252_3d_v042_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_slopez_126d_z252_3d_v043_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_slopez_252d_z504_3d_v044_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_slopez_21d_z126_3d_v045_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_slopez_63d_z252_3d_v046_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_slopez_126d_z252_3d_v047_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_slopez_252d_z504_3d_v048_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_slopez_21d_z126_3d_v049_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_slopez_63d_z252_3d_v050_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_slopez_126d_z252_3d_v051_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_slopez_252d_z504_3d_v052_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_slopez_21d_z126_3d_v053_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_slopez_63d_z252_3d_v054_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_slopez_126d_z252_3d_v055_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_slopez_252d_z504_3d_v056_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_jerk_21d_3d_v057_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_jerk_63d_3d_v058_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_jerk_126d_3d_v059_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_jerk_21d_3d_v060_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_jerk_63d_3d_v061_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_jerk_126d_3d_v062_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_jerk_21d_3d_v063_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_jerk_63d_3d_v064_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_jerk_126d_3d_v065_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_jerk_21d_3d_v066_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_jerk_63d_3d_v067_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_jerk_126d_3d_v068_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_jerk_21d_3d_v069_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_jerk_63d_3d_v070_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_jerk_126d_3d_v071_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_jerk_21d_3d_v072_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_jerk_63d_3d_v073_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_jerk_126d_3d_v074_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_jerk_21d_3d_v075_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_jerk_63d_3d_v076_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_jerk_126d_3d_v077_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of eps_qoq_chg smoothed over 252d
def f057epg_f057_eps_growth_eps_qoq_chg_smoothaccel_63d_sm252_3d_v078_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of eps_qoq_chg smoothed over 504d
def f057epg_f057_eps_growth_eps_qoq_chg_smoothaccel_252d_sm504_3d_v079_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of eps_yoy_chg smoothed over 252d
def f057epg_f057_eps_growth_eps_yoy_chg_smoothaccel_63d_sm252_3d_v080_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of eps_yoy_chg smoothed over 504d
def f057epg_f057_eps_growth_eps_yoy_chg_smoothaccel_252d_sm504_3d_v081_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of eps_pct_y smoothed over 252d
def f057epg_f057_eps_growth_eps_pct_y_smoothaccel_63d_sm252_3d_v082_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of eps_pct_y smoothed over 504d
def f057epg_f057_eps_growth_eps_pct_y_smoothaccel_252d_sm504_3d_v083_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of epsdil_yoy_chg smoothed over 252d
def f057epg_f057_eps_growth_epsdil_yoy_chg_smoothaccel_63d_sm252_3d_v084_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of epsdil_yoy_chg smoothed over 504d
def f057epg_f057_eps_growth_epsdil_yoy_chg_smoothaccel_252d_sm504_3d_v085_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of eps_signflip smoothed over 252d
def f057epg_f057_eps_growth_eps_signflip_smoothaccel_63d_sm252_3d_v086_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of eps_signflip smoothed over 504d
def f057epg_f057_eps_growth_eps_signflip_smoothaccel_252d_sm504_3d_v087_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of eps_5y_cagr smoothed over 252d
def f057epg_f057_eps_growth_eps_5y_cagr_smoothaccel_63d_sm252_3d_v088_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of eps_5y_cagr smoothed over 504d
def f057epg_f057_eps_growth_eps_5y_cagr_smoothaccel_252d_sm504_3d_v089_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of eps_narrow_loss smoothed over 252d
def f057epg_f057_eps_growth_eps_narrow_loss_smoothaccel_63d_sm252_3d_v090_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of eps_narrow_loss smoothed over 504d
def f057epg_f057_eps_growth_eps_narrow_loss_smoothaccel_252d_sm504_3d_v091_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_accelz_21d_z252_3d_v092_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_accelz_63d_z504_3d_v093_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_accelz_21d_z252_3d_v094_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_accelz_63d_z504_3d_v095_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_accelz_21d_z252_3d_v096_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_accelz_63d_z504_3d_v097_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_accelz_21d_z252_3d_v098_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_accelz_63d_z504_3d_v099_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_accelz_21d_z252_3d_v100_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_accelz_63d_z504_3d_v101_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_accelz_21d_z252_3d_v102_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_accelz_63d_z504_3d_v103_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_accelz_21d_z252_3d_v104_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_accelz_63d_z504_3d_v105_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in eps_qoq_chg (raw count, no price scaling)
def f057epg_f057_eps_growth_eps_qoq_chg_signflip_63d_3d_v106_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in eps_qoq_chg (raw count, no price scaling)
def f057epg_f057_eps_growth_eps_qoq_chg_signflip_252d_3d_v107_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in eps_yoy_chg (raw count, no price scaling)
def f057epg_f057_eps_growth_eps_yoy_chg_signflip_63d_3d_v108_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in eps_yoy_chg (raw count, no price scaling)
def f057epg_f057_eps_growth_eps_yoy_chg_signflip_252d_3d_v109_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in eps_pct_y (raw count, no price scaling)
def f057epg_f057_eps_growth_eps_pct_y_signflip_63d_3d_v110_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in eps_pct_y (raw count, no price scaling)
def f057epg_f057_eps_growth_eps_pct_y_signflip_252d_3d_v111_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in epsdil_yoy_chg (raw count, no price scaling)
def f057epg_f057_eps_growth_epsdil_yoy_chg_signflip_63d_3d_v112_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in epsdil_yoy_chg (raw count, no price scaling)
def f057epg_f057_eps_growth_epsdil_yoy_chg_signflip_252d_3d_v113_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in eps_signflip (raw count, no price scaling)
def f057epg_f057_eps_growth_eps_signflip_signflip_63d_3d_v114_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in eps_signflip (raw count, no price scaling)
def f057epg_f057_eps_growth_eps_signflip_signflip_252d_3d_v115_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in eps_5y_cagr (raw count, no price scaling)
def f057epg_f057_eps_growth_eps_5y_cagr_signflip_63d_3d_v116_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in eps_5y_cagr (raw count, no price scaling)
def f057epg_f057_eps_growth_eps_5y_cagr_signflip_252d_3d_v117_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in eps_narrow_loss (raw count, no price scaling)
def f057epg_f057_eps_growth_eps_narrow_loss_signflip_63d_3d_v118_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in eps_narrow_loss (raw count, no price scaling)
def f057epg_f057_eps_growth_eps_narrow_loss_signflip_252d_3d_v119_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_qoq_chg normalized by 252d range
def f057epg_f057_eps_growth_eps_qoq_chg_rngaccel_63d_r252_3d_v120_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_qoq_chg normalized by 504d range
def f057epg_f057_eps_growth_eps_qoq_chg_rngaccel_252d_r504_3d_v121_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_yoy_chg normalized by 252d range
def f057epg_f057_eps_growth_eps_yoy_chg_rngaccel_63d_r252_3d_v122_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_yoy_chg normalized by 504d range
def f057epg_f057_eps_growth_eps_yoy_chg_rngaccel_252d_r504_3d_v123_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_pct_y normalized by 252d range
def f057epg_f057_eps_growth_eps_pct_y_rngaccel_63d_r252_3d_v124_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_pct_y normalized by 504d range
def f057epg_f057_eps_growth_eps_pct_y_rngaccel_252d_r504_3d_v125_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of epsdil_yoy_chg normalized by 252d range
def f057epg_f057_eps_growth_epsdil_yoy_chg_rngaccel_63d_r252_3d_v126_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of epsdil_yoy_chg normalized by 504d range
def f057epg_f057_eps_growth_epsdil_yoy_chg_rngaccel_252d_r504_3d_v127_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_signflip normalized by 252d range
def f057epg_f057_eps_growth_eps_signflip_rngaccel_63d_r252_3d_v128_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_signflip normalized by 504d range
def f057epg_f057_eps_growth_eps_signflip_rngaccel_252d_r504_3d_v129_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_5y_cagr normalized by 252d range
def f057epg_f057_eps_growth_eps_5y_cagr_rngaccel_63d_r252_3d_v130_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_5y_cagr normalized by 504d range
def f057epg_f057_eps_growth_eps_5y_cagr_rngaccel_252d_r504_3d_v131_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of eps_narrow_loss normalized by 252d range
def f057epg_f057_eps_growth_eps_narrow_loss_rngaccel_63d_r252_3d_v132_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of eps_narrow_loss normalized by 504d range
def f057epg_f057_eps_growth_eps_narrow_loss_rngaccel_252d_r504_3d_v133_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_cumslope_21d_3d_v134_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_cumslope_63d_3d_v135_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_cumslope_252d_3d_v136_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_cumslope_21d_3d_v137_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_cumslope_63d_3d_v138_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_cumslope_252d_3d_v139_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_cumslope_21d_3d_v140_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_cumslope_63d_3d_v141_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_cumslope_252d_3d_v142_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_cumslope_21d_3d_v143_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_cumslope_63d_3d_v144_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_cumslope_252d_3d_v145_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_cumslope_21d_3d_v146_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_cumslope_63d_3d_v147_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_cumslope_252d_3d_v148_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_cumslope_21d_3d_v149_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_cumslope_63d_3d_v150_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

