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


# 21d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_slope_21d_2d_v001_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_slope_63d_2d_v002_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_slope_126d_2d_v003_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_slope_252d_2d_v004_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_slope_504d_2d_v005_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_slope_21d_2d_v006_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_slope_63d_2d_v007_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_slope_126d_2d_v008_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_slope_252d_2d_v009_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_slope_504d_2d_v010_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_slope_21d_2d_v011_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_slope_63d_2d_v012_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_slope_126d_2d_v013_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_slope_252d_2d_v014_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_slope_504d_2d_v015_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_slope_21d_2d_v016_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_slope_63d_2d_v017_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_slope_126d_2d_v018_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_slope_252d_2d_v019_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_slope_504d_2d_v020_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_slope_21d_2d_v021_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_slope_63d_2d_v022_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_slope_126d_2d_v023_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_slope_252d_2d_v024_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_slope_504d_2d_v025_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_slope_21d_2d_v026_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_slope_63d_2d_v027_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_slope_126d_2d_v028_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_slope_252d_2d_v029_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_slope_504d_2d_v030_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_slope_21d_2d_v031_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_slope_63d_2d_v032_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_slope_126d_2d_v033_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_slope_252d_2d_v034_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_slope_504d_2d_v035_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_sm21_sl21_2d_v036_signal(volume, close, closeadj):
    base = _mean(_f037_dollar_vol(volume, close), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_sm63_sl21_2d_v037_signal(volume, close, closeadj):
    base = _mean(_f037_dollar_vol(volume, close), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_sm63_sl63_2d_v038_signal(volume, close, closeadj):
    base = _mean(_f037_dollar_vol(volume, close), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_sm252_sl63_2d_v039_signal(volume, close, closeadj):
    base = _mean(_f037_dollar_vol(volume, close), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_sm252_sl126_2d_v040_signal(volume, close, closeadj):
    base = _mean(_f037_dollar_vol(volume, close), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_sm21_sl21_2d_v041_signal(volume, sharesbas, closeadj):
    base = _mean(volume / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_sm63_sl21_2d_v042_signal(volume, sharesbas, closeadj):
    base = _mean(volume / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_sm63_sl63_2d_v043_signal(volume, sharesbas, closeadj):
    base = _mean(volume / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_sm252_sl63_2d_v044_signal(volume, sharesbas, closeadj):
    base = _mean(volume / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_sm252_sl126_2d_v045_signal(volume, sharesbas, closeadj):
    base = _mean(volume / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_sm21_sl21_2d_v046_signal(volume, close, marketcap, closeadj):
    base = _mean(_f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_sm63_sl21_2d_v047_signal(volume, close, marketcap, closeadj):
    base = _mean(_f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_sm63_sl63_2d_v048_signal(volume, close, marketcap, closeadj):
    base = _mean(_f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_sm252_sl63_2d_v049_signal(volume, close, marketcap, closeadj):
    base = _mean(_f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_sm252_sl126_2d_v050_signal(volume, close, marketcap, closeadj):
    base = _mean(_f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_sm21_sl21_2d_v051_signal(volume, shareswadil, closeadj):
    base = _mean(volume / shareswadil.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_sm63_sl21_2d_v052_signal(volume, shareswadil, closeadj):
    base = _mean(volume / shareswadil.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_sm63_sl63_2d_v053_signal(volume, shareswadil, closeadj):
    base = _mean(volume / shareswadil.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_sm252_sl63_2d_v054_signal(volume, shareswadil, closeadj):
    base = _mean(volume / shareswadil.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_sm252_sl126_2d_v055_signal(volume, shareswadil, closeadj):
    base = _mean(volume / shareswadil.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_sm21_sl21_2d_v056_signal(volume, close, closeadj):
    base = _mean(np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_sm63_sl21_2d_v057_signal(volume, close, closeadj):
    base = _mean(np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_sm63_sl63_2d_v058_signal(volume, close, closeadj):
    base = _mean(np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_sm252_sl63_2d_v059_signal(volume, close, closeadj):
    base = _mean(np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_sm252_sl126_2d_v060_signal(volume, close, closeadj):
    base = _mean(np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_sm21_sl21_2d_v061_signal(volume, close, shareswa, closeadj):
    base = _mean(_f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_sm63_sl21_2d_v062_signal(volume, close, shareswa, closeadj):
    base = _mean(_f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_sm63_sl63_2d_v063_signal(volume, close, shareswa, closeadj):
    base = _mean(_f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_sm252_sl63_2d_v064_signal(volume, close, shareswa, closeadj):
    base = _mean(_f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_sm252_sl126_2d_v065_signal(volume, close, shareswa, closeadj):
    base = _mean(_f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_sm21_sl21_2d_v066_signal(sharesbas, closeadj):
    base = _mean(np.log(sharesbas.abs().replace(0, np.nan)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_sm63_sl21_2d_v067_signal(sharesbas, closeadj):
    base = _mean(np.log(sharesbas.abs().replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_sm63_sl63_2d_v068_signal(sharesbas, closeadj):
    base = _mean(np.log(sharesbas.abs().replace(0, np.nan)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_sm252_sl63_2d_v069_signal(sharesbas, closeadj):
    base = _mean(np.log(sharesbas.abs().replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_sm252_sl126_2d_v070_signal(sharesbas, closeadj):
    base = _mean(np.log(sharesbas.abs().replace(0, np.nan)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_pctslope_21d_2d_v071_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_pctslope_63d_2d_v072_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_pctslope_252d_2d_v073_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_pctslope_21d_2d_v074_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_pctslope_63d_2d_v075_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_pctslope_252d_2d_v076_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_pctslope_21d_2d_v077_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_pctslope_63d_2d_v078_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_pctslope_252d_2d_v079_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_pctslope_21d_2d_v080_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_pctslope_63d_2d_v081_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_pctslope_252d_2d_v082_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_pctslope_21d_2d_v083_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_pctslope_63d_2d_v084_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_pctslope_252d_2d_v085_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_pctslope_21d_2d_v086_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_pctslope_63d_2d_v087_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_pctslope_252d_2d_v088_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_pctslope_21d_2d_v089_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_pctslope_63d_2d_v090_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_pctslope_252d_2d_v091_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_sgnslope_21d_2d_v092_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_sgnslope_63d_2d_v093_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_sgnslope_252d_2d_v094_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_sgnslope_21d_2d_v095_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_sgnslope_63d_2d_v096_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_sgnslope_252d_2d_v097_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_sgnslope_21d_2d_v098_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_sgnslope_63d_2d_v099_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_sgnslope_252d_2d_v100_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_sgnslope_21d_2d_v101_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_sgnslope_63d_2d_v102_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_sgnslope_252d_2d_v103_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_sgnslope_21d_2d_v104_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_sgnslope_63d_2d_v105_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_sgnslope_252d_2d_v106_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_sgnslope_21d_2d_v107_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_sgnslope_63d_2d_v108_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_sgnslope_252d_2d_v109_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_sgnslope_21d_2d_v110_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_sgnslope_63d_2d_v111_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_sgnslope_252d_2d_v112_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_logmagslope_21d_2d_v113_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_logmagslope_63d_2d_v114_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_logmagslope_252d_2d_v115_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_logmagslope_21d_2d_v116_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_logmagslope_63d_2d_v117_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_logmagslope_252d_2d_v118_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_logmagslope_21d_2d_v119_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_logmagslope_63d_2d_v120_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_logmagslope_252d_2d_v121_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_logmagslope_21d_2d_v122_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_logmagslope_63d_2d_v123_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_logmagslope_252d_2d_v124_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_logmagslope_21d_2d_v125_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_logmagslope_63d_2d_v126_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_logmagslope_252d_2d_v127_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_logmagslope_21d_2d_v128_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_logmagslope_63d_2d_v129_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_logmagslope_252d_2d_v130_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_logmagslope_21d_2d_v131_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_logmagslope_63d_2d_v132_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_logmagslope_252d_2d_v133_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dollar_vol|
def f037fts_f037_float_and_tradeable_scale_dollar_vol_logslope_63d_2d_v134_signal(volume, close, closeadj):
    base = np.log((_f037_dollar_vol(volume, close)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dollar_vol|
def f037fts_f037_float_and_tradeable_scale_dollar_vol_logslope_252d_2d_v135_signal(volume, close, closeadj):
    base = np.log((_f037_dollar_vol(volume, close)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|turnover|
def f037fts_f037_float_and_tradeable_scale_turnover_logslope_63d_2d_v136_signal(volume, sharesbas, closeadj):
    base = np.log((volume / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|turnover|
def f037fts_f037_float_and_tradeable_scale_turnover_logslope_252d_2d_v137_signal(volume, sharesbas, closeadj):
    base = np.log((volume / sharesbas.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dv_to_mcap|
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_logslope_63d_2d_v138_signal(volume, close, marketcap, closeadj):
    base = np.log((_f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dv_to_mcap|
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_logslope_252d_2d_v139_signal(volume, close, marketcap, closeadj):
    base = np.log((_f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|turnover_dil|
def f037fts_f037_float_and_tradeable_scale_turnover_dil_logslope_63d_2d_v140_signal(volume, shareswadil, closeadj):
    base = np.log((volume / shareswadil.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|turnover_dil|
def f037fts_f037_float_and_tradeable_scale_turnover_dil_logslope_252d_2d_v141_signal(volume, shareswadil, closeadj):
    base = np.log((volume / shareswadil.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|log_dv|
def f037fts_f037_float_and_tradeable_scale_log_dv_logslope_63d_2d_v142_signal(volume, close, closeadj):
    base = np.log((np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|log_dv|
def f037fts_f037_float_and_tradeable_scale_log_dv_logslope_252d_2d_v143_signal(volume, close, closeadj):
    base = np.log((np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|dv_to_shareswa|
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_logslope_63d_2d_v144_signal(volume, close, shareswa, closeadj):
    base = np.log((_f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|dv_to_shareswa|
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_logslope_252d_2d_v145_signal(volume, close, shareswa, closeadj):
    base = np.log((_f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|float_log|
def f037fts_f037_float_and_tradeable_scale_float_log_logslope_63d_2d_v146_signal(sharesbas, closeadj):
    base = np.log((np.log(sharesbas.abs().replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|float_log|
def f037fts_f037_float_and_tradeable_scale_float_log_logslope_252d_2d_v147_signal(sharesbas, closeadj):
    base = np.log((np.log(sharesbas.abs().replace(0, np.nan))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

