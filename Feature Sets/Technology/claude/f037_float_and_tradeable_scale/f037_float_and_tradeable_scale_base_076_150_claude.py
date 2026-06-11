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


# 63d z-score of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_z_63d_base_v076_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_z_126d_base_v077_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_z_252d_base_v078_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_z_504d_base_v079_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_z_63d_base_v080_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_z_126d_base_v081_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_z_252d_base_v082_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_z_504d_base_v083_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_z_63d_base_v084_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_z_126d_base_v085_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_z_252d_base_v086_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_z_504d_base_v087_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_z_63d_base_v088_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_z_126d_base_v089_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_z_252d_base_v090_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_z_504d_base_v091_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_z_63d_base_v092_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_z_126d_base_v093_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_z_252d_base_v094_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_z_504d_base_v095_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_z_63d_base_v096_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_z_126d_base_v097_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_z_252d_base_v098_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_z_504d_base_v099_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_z_63d_base_v100_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_z_126d_base_v101_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_z_252d_base_v102_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_z_504d_base_v103_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_distmax_252d_base_v104_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_distmax_504d_base_v105_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_distmax_252d_base_v106_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_distmax_504d_base_v107_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_distmax_252d_base_v108_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_distmax_504d_base_v109_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_distmax_252d_base_v110_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_distmax_504d_base_v111_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_distmax_252d_base_v112_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_distmax_504d_base_v113_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_distmax_252d_base_v114_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_distmax_504d_base_v115_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_distmax_252d_base_v116_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_distmax_504d_base_v117_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_distmed_126d_base_v118_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_distmed_252d_base_v119_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_distmed_504d_base_v120_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_distmed_126d_base_v121_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_distmed_252d_base_v122_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of turnover
def f037fts_f037_float_and_tradeable_scale_turnover_distmed_504d_base_v123_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_distmed_126d_base_v124_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_distmed_252d_base_v125_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_distmed_504d_base_v126_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_distmed_126d_base_v127_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_distmed_252d_base_v128_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_distmed_504d_base_v129_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_distmed_126d_base_v130_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_distmed_252d_base_v131_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_distmed_504d_base_v132_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_distmed_126d_base_v133_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_distmed_252d_base_v134_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_distmed_504d_base_v135_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_distmed_126d_base_v136_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_distmed_252d_base_v137_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of float_log
def f037fts_f037_float_and_tradeable_scale_float_log_distmed_504d_base_v138_signal(sharesbas, closeadj):
    base = np.log(sharesbas.abs().replace(0, np.nan))
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_chg_63d_base_v139_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in dollar_vol
def f037fts_f037_float_and_tradeable_scale_dollar_vol_chg_252d_base_v140_signal(volume, close, closeadj):
    base = _f037_dollar_vol(volume, close)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in turnover
def f037fts_f037_float_and_tradeable_scale_turnover_chg_63d_base_v141_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in turnover
def f037fts_f037_float_and_tradeable_scale_turnover_chg_252d_base_v142_signal(volume, sharesbas, closeadj):
    base = volume / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_chg_63d_base_v143_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in dv_to_mcap
def f037fts_f037_float_and_tradeable_scale_dv_to_mcap_chg_252d_base_v144_signal(volume, close, marketcap, closeadj):
    base = _f037_dollar_vol(volume, close) / marketcap.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_chg_63d_base_v145_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in turnover_dil
def f037fts_f037_float_and_tradeable_scale_turnover_dil_chg_252d_base_v146_signal(volume, shareswadil, closeadj):
    base = volume / shareswadil.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_chg_63d_base_v147_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in log_dv
def f037fts_f037_float_and_tradeable_scale_log_dv_chg_252d_base_v148_signal(volume, close, closeadj):
    base = np.log(_f037_dollar_vol(volume, close).abs().replace(0, np.nan))
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_chg_63d_base_v149_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in dv_to_shareswa
def f037fts_f037_float_and_tradeable_scale_dv_to_shareswa_chg_252d_base_v150_signal(volume, close, shareswa, closeadj):
    base = _f037_dollar_vol(volume, close) / shareswa.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

