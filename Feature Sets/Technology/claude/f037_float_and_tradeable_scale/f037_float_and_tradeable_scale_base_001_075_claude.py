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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f037_dollar_vol(volume, close):
    return volume * close


# 21d mean of dollar_vol scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_dollar_vol_mean_21d_base_v001_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dollar_vol scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_dollar_vol_mean_63d_base_v002_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dollar_vol scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_dollar_vol_mean_126d_base_v003_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dollar_vol scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_dollar_vol_mean_252d_base_v004_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dollar_vol scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_dollar_vol_mean_504d_base_v005_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of turnover scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_turnover_mean_21d_base_v006_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of turnover scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_turnover_mean_63d_base_v007_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of turnover scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_turnover_mean_126d_base_v008_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of turnover scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_turnover_mean_252d_base_v009_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of turnover scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_turnover_mean_504d_base_v010_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dv_to_mcap scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_mean_21d_base_v011_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dv_to_mcap scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_mean_63d_base_v012_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dv_to_mcap scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_mean_126d_base_v013_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dv_to_mcap scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_mean_252d_base_v014_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dv_to_mcap scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_mean_504d_base_v015_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of turnover_dil scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_turnover_dil_mean_21d_base_v016_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of turnover_dil scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_turnover_dil_mean_63d_base_v017_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of turnover_dil scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_turnover_dil_mean_126d_base_v018_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of turnover_dil scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_turnover_dil_mean_252d_base_v019_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of turnover_dil scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_turnover_dil_mean_504d_base_v020_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of log_dv scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_log_dv_mean_21d_base_v021_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of log_dv scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_log_dv_mean_63d_base_v022_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of log_dv scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_log_dv_mean_126d_base_v023_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of log_dv scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_log_dv_mean_252d_base_v024_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of log_dv scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_log_dv_mean_504d_base_v025_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dv_to_shareswa scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_mean_21d_base_v026_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dv_to_shareswa scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_mean_63d_base_v027_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dv_to_shareswa scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_mean_126d_base_v028_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dv_to_shareswa scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_mean_252d_base_v029_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dv_to_shareswa scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_mean_504d_base_v030_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of float_log scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_float_log_mean_21d_base_v031_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of float_log scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_float_log_mean_63d_base_v032_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of float_log scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_float_log_mean_126d_base_v033_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of float_log scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_float_log_mean_252d_base_v034_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of float_log scaled by closeadj
def f037fts_f037_float_and_tradeable_scale_float_log_mean_504d_base_v035_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_median_63d_base_v036_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_median_252d_base_v037_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_median_504d_base_v038_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_median_63d_base_v039_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_median_252d_base_v040_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_median_504d_base_v041_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_median_63d_base_v042_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_median_252d_base_v043_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_median_504d_base_v044_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_median_63d_base_v045_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_median_252d_base_v046_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_median_504d_base_v047_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_median_63d_base_v048_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_median_252d_base_v049_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_median_504d_base_v050_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_median_63d_base_v051_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_median_252d_base_v052_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_median_504d_base_v053_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_median_63d_base_v054_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_median_252d_base_v055_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_median_504d_base_v056_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_rmax_252d_base_v057_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_rmax_504d_base_v058_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_rmax_252d_base_v059_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_rmax_504d_base_v060_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_rmax_252d_base_v061_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_rmax_504d_base_v062_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_rmax_252d_base_v063_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_rmax_504d_base_v064_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_rmax_252d_base_v065_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_rmax_504d_base_v066_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_rmax_252d_base_v067_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_rmax_504d_base_v068_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_rmax_252d_base_v069_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_rmax_504d_base_v070_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_rmin_252d_base_v071_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_rmin_504d_base_v072_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_rmin_252d_base_v073_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_rmin_504d_base_v074_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_rmin_252d_base_v075_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

