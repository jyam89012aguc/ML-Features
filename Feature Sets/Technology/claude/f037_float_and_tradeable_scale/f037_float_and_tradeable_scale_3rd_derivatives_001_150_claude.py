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
def _f037_dollar_vol(volume, close):
    return volume * close


# 21d acceleration of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_accel_21d_3d_v001_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_accel_63d_3d_v002_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_accel_126d_3d_v003_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_accel_252d_3d_v004_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_accel_21d_3d_v005_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_accel_63d_3d_v006_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_accel_126d_3d_v007_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_accel_252d_3d_v008_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_accel_21d_3d_v009_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_accel_63d_3d_v010_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_accel_126d_3d_v011_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_accel_252d_3d_v012_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_accel_21d_3d_v013_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_accel_63d_3d_v014_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_accel_126d_3d_v015_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_accel_252d_3d_v016_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_accel_21d_3d_v017_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_accel_63d_3d_v018_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_accel_126d_3d_v019_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_accel_252d_3d_v020_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_accel_21d_3d_v021_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_accel_63d_3d_v022_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_accel_126d_3d_v023_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_accel_252d_3d_v024_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_accel_21d_3d_v025_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_accel_63d_3d_v026_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_accel_126d_3d_v027_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_accel_252d_3d_v028_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_slopez_21d_z126_3d_v029_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_slopez_63d_z252_3d_v030_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_slopez_126d_z252_3d_v031_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_slopez_252d_z504_3d_v032_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_slopez_21d_z126_3d_v033_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_slopez_63d_z252_3d_v034_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_slopez_126d_z252_3d_v035_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_slopez_252d_z504_3d_v036_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_slopez_21d_z126_3d_v037_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_slopez_63d_z252_3d_v038_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_slopez_126d_z252_3d_v039_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_slopez_252d_z504_3d_v040_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_slopez_21d_z126_3d_v041_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_slopez_63d_z252_3d_v042_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_slopez_126d_z252_3d_v043_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_slopez_252d_z504_3d_v044_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_slopez_21d_z126_3d_v045_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_slopez_63d_z252_3d_v046_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_slopez_126d_z252_3d_v047_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_slopez_252d_z504_3d_v048_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_slopez_21d_z126_3d_v049_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_slopez_63d_z252_3d_v050_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_slopez_126d_z252_3d_v051_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_slopez_252d_z504_3d_v052_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_slopez_21d_z126_3d_v053_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_slopez_63d_z252_3d_v054_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_slopez_126d_z252_3d_v055_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_slopez_252d_z504_3d_v056_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_jerk_21d_3d_v057_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_jerk_63d_3d_v058_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_jerk_126d_3d_v059_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_jerk_21d_3d_v060_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_jerk_63d_3d_v061_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_jerk_126d_3d_v062_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_jerk_21d_3d_v063_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_jerk_63d_3d_v064_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_jerk_126d_3d_v065_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_jerk_21d_3d_v066_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_jerk_63d_3d_v067_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_jerk_126d_3d_v068_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_jerk_21d_3d_v069_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_jerk_63d_3d_v070_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_jerk_126d_3d_v071_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_jerk_21d_3d_v072_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_jerk_63d_3d_v073_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_jerk_126d_3d_v074_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_jerk_21d_3d_v075_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_jerk_63d_3d_v076_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_jerk_126d_3d_v077_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dollar_vol smoothed over 252d
def f037fts_f037_float_and_tradeable_scale_dollar_vol_smoothaccel_63d_sm252_3d_v078_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dollar_vol smoothed over 504d
def f037fts_f037_float_and_tradeable_scale_dollar_vol_smoothaccel_252d_sm504_3d_v079_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of turnover smoothed over 252d
def f037fts_f037_float_and_tradeable_scale_turnover_smoothaccel_63d_sm252_3d_v080_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of turnover smoothed over 504d
def f037fts_f037_float_and_tradeable_scale_turnover_smoothaccel_252d_sm504_3d_v081_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dv_to_mcap smoothed over 252d
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_smoothaccel_63d_sm252_3d_v082_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dv_to_mcap smoothed over 504d
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_smoothaccel_252d_sm504_3d_v083_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of turnover_dil smoothed over 252d
def f037fts_f037_float_and_tradeable_scale_turnover_dil_smoothaccel_63d_sm252_3d_v084_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of turnover_dil smoothed over 504d
def f037fts_f037_float_and_tradeable_scale_turnover_dil_smoothaccel_252d_sm504_3d_v085_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of log_dv smoothed over 252d
def f037fts_f037_float_and_tradeable_scale_log_dv_smoothaccel_63d_sm252_3d_v086_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of log_dv smoothed over 504d
def f037fts_f037_float_and_tradeable_scale_log_dv_smoothaccel_252d_sm504_3d_v087_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of dv_to_shareswa smoothed over 252d
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_smoothaccel_63d_sm252_3d_v088_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of dv_to_shareswa smoothed over 504d
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_smoothaccel_252d_sm504_3d_v089_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of float_log smoothed over 252d
def f037fts_f037_float_and_tradeable_scale_float_log_smoothaccel_63d_sm252_3d_v090_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of float_log smoothed over 504d
def f037fts_f037_float_and_tradeable_scale_float_log_smoothaccel_252d_sm504_3d_v091_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_accelz_21d_z252_3d_v092_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_accelz_63d_z504_3d_v093_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_accelz_21d_z252_3d_v094_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_accelz_63d_z504_3d_v095_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_accelz_21d_z252_3d_v096_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_accelz_63d_z504_3d_v097_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_accelz_21d_z252_3d_v098_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_accelz_63d_z504_3d_v099_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_accelz_21d_z252_3d_v100_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_accelz_63d_z504_3d_v101_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_accelz_21d_z252_3d_v102_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_accelz_63d_z504_3d_v103_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_accelz_21d_z252_3d_v104_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_accelz_63d_z504_3d_v105_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dollar_vol (raw count, no price scaling)
def f037fts_f037_float_and_tradeable_scale_dollar_vol_signflip_63d_3d_v106_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dollar_vol (raw count, no price scaling)
def f037fts_f037_float_and_tradeable_scale_dollar_vol_signflip_252d_3d_v107_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in turnover (raw count, no price scaling)
def f037fts_f037_float_and_tradeable_scale_turnover_signflip_63d_3d_v108_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in turnover (raw count, no price scaling)
def f037fts_f037_float_and_tradeable_scale_turnover_signflip_252d_3d_v109_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dv_to_mcap (raw count, no price scaling)
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_signflip_63d_3d_v110_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dv_to_mcap (raw count, no price scaling)
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_signflip_252d_3d_v111_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in turnover_dil (raw count, no price scaling)
def f037fts_f037_float_and_tradeable_scale_turnover_dil_signflip_63d_3d_v112_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in turnover_dil (raw count, no price scaling)
def f037fts_f037_float_and_tradeable_scale_turnover_dil_signflip_252d_3d_v113_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in log_dv (raw count, no price scaling)
def f037fts_f037_float_and_tradeable_scale_log_dv_signflip_63d_3d_v114_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in log_dv (raw count, no price scaling)
def f037fts_f037_float_and_tradeable_scale_log_dv_signflip_252d_3d_v115_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in dv_to_shareswa (raw count, no price scaling)
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_signflip_63d_3d_v116_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in dv_to_shareswa (raw count, no price scaling)
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_signflip_252d_3d_v117_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in float_log (raw count, no price scaling)
def f037fts_f037_float_and_tradeable_scale_float_log_signflip_63d_3d_v118_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in float_log (raw count, no price scaling)
def f037fts_f037_float_and_tradeable_scale_float_log_signflip_252d_3d_v119_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dollar_vol normalized by 252d range
def f037fts_f037_float_and_tradeable_scale_dollar_vol_rngaccel_63d_r252_3d_v120_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dollar_vol normalized by 504d range
def f037fts_f037_float_and_tradeable_scale_dollar_vol_rngaccel_252d_r504_3d_v121_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of turnover normalized by 252d range
def f037fts_f037_float_and_tradeable_scale_turnover_rngaccel_63d_r252_3d_v122_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of turnover normalized by 504d range
def f037fts_f037_float_and_tradeable_scale_turnover_rngaccel_252d_r504_3d_v123_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dv_to_mcap normalized by 252d range
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_rngaccel_63d_r252_3d_v124_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dv_to_mcap normalized by 504d range
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_rngaccel_252d_r504_3d_v125_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of turnover_dil normalized by 252d range
def f037fts_f037_float_and_tradeable_scale_turnover_dil_rngaccel_63d_r252_3d_v126_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of turnover_dil normalized by 504d range
def f037fts_f037_float_and_tradeable_scale_turnover_dil_rngaccel_252d_r504_3d_v127_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of log_dv normalized by 252d range
def f037fts_f037_float_and_tradeable_scale_log_dv_rngaccel_63d_r252_3d_v128_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of log_dv normalized by 504d range
def f037fts_f037_float_and_tradeable_scale_log_dv_rngaccel_252d_r504_3d_v129_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dv_to_shareswa normalized by 252d range
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_rngaccel_63d_r252_3d_v130_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dv_to_shareswa normalized by 504d range
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_rngaccel_252d_r504_3d_v131_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of float_log normalized by 252d range
def f037fts_f037_float_and_tradeable_scale_float_log_rngaccel_63d_r252_3d_v132_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of float_log normalized by 504d range
def f037fts_f037_float_and_tradeable_scale_float_log_rngaccel_252d_r504_3d_v133_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_cumslope_21d_3d_v134_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_cumslope_63d_3d_v135_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_cumslope_252d_3d_v136_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_cumslope_21d_3d_v137_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_cumslope_63d_3d_v138_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_cumslope_252d_3d_v139_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_cumslope_21d_3d_v140_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_cumslope_63d_3d_v141_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_cumslope_252d_3d_v142_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_cumslope_21d_3d_v143_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_cumslope_63d_3d_v144_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_cumslope_252d_3d_v145_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_cumslope_21d_3d_v146_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_cumslope_63d_3d_v147_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_cumslope_252d_3d_v148_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_cumslope_21d_3d_v149_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_cumslope_63d_3d_v150_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

