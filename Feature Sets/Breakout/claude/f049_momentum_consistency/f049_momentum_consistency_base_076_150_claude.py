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
def _f049_up_periods(close, w):
    r = close.pct_change()
    up = (r > 0).astype(float)
    return up.rolling(w, min_periods=max(1, w // 2)).mean() * close


def _f049_consistency_ratio(close, w):
    r = close.pct_change()
    up = (r > 0).astype(float)
    up_frac = up.rolling(w, min_periods=max(1, w // 2)).mean()
    mom = close.pct_change(periods=w)
    return up_frac * np.sign(mom) * close


def _f049_smooth_leadership(close, w):
    r = close.pct_change()
    up = (r > 0).astype(float)
    up_frac = up.rolling(w, min_periods=max(1, w // 2)).mean()
    mom = close.pct_change(periods=w)
    return up_frac * mom.abs() * close


# RS line - median over 63d × close
def f049mcs_f049_momentum_consistency_rsdmed_63d_base_v076_signal(closeadj):
    rs = _f049_up_periods(closeadj, 63)
    med = rs.rolling(63, min_periods=21).median()
    result = (rs - med) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line - median over 252d × close
def f049mcs_f049_momentum_consistency_rsdmed_252d_base_v077_signal(closeadj):
    rs = _f049_up_periods(closeadj, 252)
    med = rs.rolling(252, min_periods=63).median()
    result = (rs - med) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line - median 504d × close
def f049mcs_f049_momentum_consistency_rsdmed_504d_base_v078_signal(closeadj):
    rs = _f049_up_periods(closeadj, 504)
    med = rs.rolling(504, min_periods=126).median()
    result = (rs - med) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Max of RS over 21d × close
def f049mcs_f049_momentum_consistency_rsmax_21d_base_v079_signal(closeadj):
    result = _f049_up_periods(closeadj, 21).rolling(21, min_periods=5).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Max of RS over 63d × close
def f049mcs_f049_momentum_consistency_rsmax_63d_base_v080_signal(closeadj):
    result = _f049_up_periods(closeadj, 63).rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Max of RS over 252d × close
def f049mcs_f049_momentum_consistency_rsmax_252d_base_v081_signal(closeadj):
    result = _f049_up_periods(closeadj, 252).rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Min of RS over 63d × close
def f049mcs_f049_momentum_consistency_rsmin_63d_base_v082_signal(closeadj):
    result = _f049_up_periods(closeadj, 63).rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Min of RS over 252d × close
def f049mcs_f049_momentum_consistency_rsmin_252d_base_v083_signal(closeadj):
    result = _f049_up_periods(closeadj, 252).rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS sum over 21d × close
def f049mcs_f049_momentum_consistency_rssum_21d_base_v084_signal(closeadj):
    result = _f049_up_periods(closeadj, 21).rolling(21, min_periods=5).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS sum over 63d × close
def f049mcs_f049_momentum_consistency_rssum_63d_base_v085_signal(closeadj):
    result = _f049_up_periods(closeadj, 63).rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS sum over 252d × close
def f049mcs_f049_momentum_consistency_rssum_252d_base_v086_signal(closeadj):
    result = _f049_up_periods(closeadj, 252).rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS new-high count over 21d × close
def f049mcs_f049_momentum_consistency_rsnh21_base_v087_signal(closeadj):
    rs = _f049_up_periods(closeadj, 10)
    rs_max = rs.rolling(10, min_periods=3).max()
    flg = (rs >= rs_max).astype(float)
    result = flg.rolling(21, min_periods=5).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS new-high count over 126d × close
def f049mcs_f049_momentum_consistency_rsnh126_base_v088_signal(closeadj):
    rs = _f049_up_periods(closeadj, 42)
    rs_max = rs.rolling(42, min_periods=10).max()
    flg = (rs >= rs_max).astype(float)
    result = flg.rolling(126, min_periods=42).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS new-high rate over 252d × close
def f049mcs_f049_momentum_consistency_rsnhrate_252d_base_v089_signal(closeadj):
    rs = _f049_up_periods(closeadj, 63)
    rs_max = rs.rolling(63, min_periods=21).max()
    flg = (rs >= rs_max).astype(float)
    result = (flg.rolling(252, min_periods=63).sum() / 252.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS new-high rate over 504d × close
def f049mcs_f049_momentum_consistency_rsnhrate_504d_base_v090_signal(closeadj):
    rs = _f049_up_periods(closeadj, 126)
    rs_max = rs.rolling(126, min_periods=42).max()
    flg = (rs >= rs_max).astype(float)
    result = (flg.rolling(504, min_periods=126).sum() / 504.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS gap 21d × mean close 21d
def f049mcs_f049_momentum_consistency_rsgxm_21d_base_v091_signal(closeadj):
    result = (_f049_up_periods(closeadj, 21) - 1.0) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# RS gap 63d × mean close 63d
def f049mcs_f049_momentum_consistency_rsgxm_63d_base_v092_signal(closeadj):
    result = (_f049_up_periods(closeadj, 63) - 1.0) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# RS gap 252d × mean close 252d
def f049mcs_f049_momentum_consistency_rsgxm_252d_base_v093_signal(closeadj):
    result = (_f049_up_periods(closeadj, 252) - 1.0) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# RS new high z-score 63d × close
def f049mcs_f049_momentum_consistency_rsnhz_63d_base_v094_signal(closeadj):
    result = _z(_f049_consistency_ratio(closeadj, 63), 252) + _f049_up_periods(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RS new high z-score 252d
def f049mcs_f049_momentum_consistency_rsnhz_252d_base_v095_signal(closeadj):
    result = _z(_f049_consistency_ratio(closeadj, 252), 504) + _f049_up_periods(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RS line sign-weighted score 21d × close
def f049mcs_f049_momentum_consistency_rssign_21d_base_v096_signal(closeadj):
    rs = _f049_up_periods(closeadj, 21) - 1.0
    result = np.sign(rs) * rs.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line sign-weighted score 63d × close
def f049mcs_f049_momentum_consistency_rssign_63d_base_v097_signal(closeadj):
    rs = _f049_up_periods(closeadj, 63) - 1.0
    result = np.sign(rs) * rs.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line sign-weighted score 252d × close
def f049mcs_f049_momentum_consistency_rssign_252d_base_v098_signal(closeadj):
    rs = _safe_div(_f049_up_periods(closeadj, 252), _mean(closeadj, 252)) - 1.0
    result = np.tanh(_z(rs, 63)) * rs.abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# RS line × std(close, 21) — magnitude-modulated
def f049mcs_f049_momentum_consistency_rsxstd_21d_base_v099_signal(closeadj):
    result = _f049_up_periods(closeadj, 21) * _std(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line × std(close, 63)
def f049mcs_f049_momentum_consistency_rsxstd_63d_base_v100_signal(closeadj):
    result = _f049_up_periods(closeadj, 63) * _std(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line × std(close, 252)
def f049mcs_f049_momentum_consistency_rsxstd_252d_base_v101_signal(closeadj):
    result = _f049_up_periods(closeadj, 252) * _std(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line - rs(close,42) momentum
def f049mcs_f049_momentum_consistency_rsmoment_21v42_base_v102_signal(closeadj):
    result = (_f049_up_periods(closeadj, 21) - _f049_up_periods(closeadj, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line 42 - rs 189 mid-term momentum
def f049mcs_f049_momentum_consistency_rsmoment_42v189_base_v103_signal(closeadj):
    result = (_f049_up_periods(closeadj, 42) - _f049_up_periods(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line 189 - rs 378 longer-term momentum
def f049mcs_f049_momentum_consistency_rsmoment_189v378_base_v104_signal(closeadj):
    result = (_f049_up_periods(closeadj, 189) - _f049_up_periods(closeadj, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line ratio 5v21
def f049mcs_f049_momentum_consistency_rsratio_5v21_base_v105_signal(closeadj):
    result = _f049_up_periods(closeadj, 5) / _f049_up_periods(closeadj, 21).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line ratio 10v42
def f049mcs_f049_momentum_consistency_rsratio_10v42_base_v106_signal(closeadj):
    result = _f049_up_periods(closeadj, 10) / _f049_up_periods(closeadj, 42).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line ratio 42v189
def f049mcs_f049_momentum_consistency_rsratio_42v189_base_v107_signal(closeadj):
    result = _f049_up_periods(closeadj, 42) / _f049_up_periods(closeadj, 189).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line z-score over 126d
def f049mcs_f049_momentum_consistency_rsz_42d_base_v108_signal(closeadj):
    result = _z(_f049_up_periods(closeadj, 42), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# RS line z-score 189d over 378d
def f049mcs_f049_momentum_consistency_rsz_189d_base_v109_signal(closeadj):
    result = _z(_f049_up_periods(closeadj, 189), 378)
    return result.replace([np.inf, -np.inf], np.nan)


# RS line z-score 378d over 504d
def f049mcs_f049_momentum_consistency_rsz_378d_base_v110_signal(closeadj):
    result = _z(_f049_up_periods(closeadj, 378), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# RS new-high gap × close * close
def f049mcs_f049_momentum_consistency_rsnhxsq_63d_base_v111_signal(closeadj):
    result = _f049_consistency_ratio(closeadj, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS new-high gap × close * close 252
def f049mcs_f049_momentum_consistency_rsnhxsq_252d_base_v112_signal(closeadj):
    result = _f049_consistency_ratio(closeadj, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line EMA span=5 × close
def f049mcs_f049_momentum_consistency_rsema5_21d_base_v113_signal(closeadj):
    rs = _f049_up_periods(closeadj, 21)
    result = rs.ewm(span=5, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line EMA span=10 × close
def f049mcs_f049_momentum_consistency_rsema10_63d_base_v114_signal(closeadj):
    rs = _f049_up_periods(closeadj, 63)
    result = rs.ewm(span=10, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line EMA span=42 × close
def f049mcs_f049_momentum_consistency_rsema42_252d_base_v115_signal(closeadj):
    rs = _safe_div(_f049_up_periods(closeadj, 252), _mean(closeadj, 252))
    result = rs.ewm(span=42, adjust=False).mean() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# RS new-high gap mean over 63d × close
def f049mcs_f049_momentum_consistency_rsnhmean_63d_base_v116_signal(closeadj):
    result = _mean(_f049_consistency_ratio(closeadj, 21), 63) * closeadj * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# RS new-high gap mean over 252d × close
def f049mcs_f049_momentum_consistency_rsnhmean_252d_base_v117_signal(closeadj):
    result = _mean(_f049_consistency_ratio(closeadj, 63), 252) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# RS new-high gap std over 63d × close
def f049mcs_f049_momentum_consistency_rsnhstd_63d_base_v118_signal(closeadj):
    result = _std(_f049_consistency_ratio(closeadj, 21), 63) * closeadj * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# RS new-high gap std over 252d × close
def f049mcs_f049_momentum_consistency_rsnhstd_252d_base_v119_signal(closeadj):
    result = _std(_f049_consistency_ratio(closeadj, 63), 252) * closeadj * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# RS line - close baseline scaled
def f049mcs_f049_momentum_consistency_rsmclose_21d_base_v120_signal(closeadj):
    result = (_f049_up_periods(closeadj, 21) * closeadj - closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# RS line - close baseline 63d
def f049mcs_f049_momentum_consistency_rsmclose_63d_base_v121_signal(closeadj):
    result = (_f049_up_periods(closeadj, 63) * closeadj - closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# RS line - close baseline 252d
def f049mcs_f049_momentum_consistency_rsmclose_252d_base_v122_signal(closeadj):
    rel = _safe_div(closeadj, _mean(closeadj, 252))
    result = (_safe_div(_f049_up_periods(closeadj, 252), _mean(closeadj, 252)) * rel - rel)
    return result.replace([np.inf, -np.inf], np.nan)


# RS streak smoothed × close
def f049mcs_f049_momentum_consistency_daysatnh_63d_base_v123_signal(closeadj):
    rs = _f049_up_periods(closeadj, 63)
    rs_max = rs.rolling(63, min_periods=21).max()
    at = (rs >= rs_max).astype(float)
    streak = at * (at.groupby((at != at.shift()).cumsum()).cumcount() + 1)
    result = (streak + _safe_div(_mean(closeadj, 21), _mean(closeadj, 252))) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# RS streak smoothed 252d × close
def f049mcs_f049_momentum_consistency_daysatnh_252d_base_v124_signal(closeadj):
    rs = _f049_up_periods(closeadj, 252)
    rs_max = rs.rolling(252, min_periods=63).max()
    at = (rs >= rs_max).astype(float)
    streak = at * (at.groupby((at != at.shift()).cumsum()).cumcount() + 1)
    result = (streak + _mean(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line geometric mean ratio 21d
def f049mcs_f049_momentum_consistency_rsgeo_21d_base_v125_signal(closeadj):
    rs = _f049_up_periods(closeadj, 21).replace(0, np.nan).abs()
    result = np.exp(np.log(rs).rolling(21, min_periods=5).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line geometric mean ratio 63d
def f049mcs_f049_momentum_consistency_rsgeo_63d_base_v126_signal(closeadj):
    rs = _f049_up_periods(closeadj, 63).replace(0, np.nan).abs()
    result = np.exp(np.log(rs).rolling(63, min_periods=21).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line geometric mean ratio 252d
def f049mcs_f049_momentum_consistency_rsgeo_252d_base_v127_signal(closeadj):
    rs = _f049_up_periods(closeadj, 252).replace(0, np.nan).abs()
    result = np.exp(np.log(rs).rolling(252, min_periods=63).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line × close return 5d
def f049mcs_f049_momentum_consistency_rsxret_5d_base_v128_signal(closeadj):
    ret = closeadj.pct_change(5)
    result = _f049_up_periods(closeadj, 21) * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line × close return 21d
def f049mcs_f049_momentum_consistency_rsxret_21d_base_v129_signal(closeadj):
    ret = closeadj.pct_change(21)
    result = _f049_up_periods(closeadj, 63) * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line × close return 63d
def f049mcs_f049_momentum_consistency_rsxret_63d_base_v130_signal(closeadj):
    ret = closeadj.pct_change(63)
    result = _f049_up_periods(closeadj, 252) * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS new-high distance × close return 5d
def f049mcs_f049_momentum_consistency_rsnhxret_5d_base_v131_signal(closeadj):
    ret = closeadj.pct_change(5)
    result = _f049_consistency_ratio(closeadj, 21) * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS new-high distance × close return 21d
def f049mcs_f049_momentum_consistency_rsnhxret_21d_base_v132_signal(closeadj):
    ret = closeadj.pct_change(21)
    result = _f049_consistency_ratio(closeadj, 63) * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line - 1 absolute × close
def f049mcs_f049_momentum_consistency_rsabsgap_21d_base_v133_signal(closeadj):
    result = (_f049_up_periods(closeadj, 21) - 1.0).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line abs gap 63d × close
def f049mcs_f049_momentum_consistency_rsabsgap_63d_base_v134_signal(closeadj):
    result = (_f049_up_periods(closeadj, 63) - 1.0).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line abs gap 252d × close
def f049mcs_f049_momentum_consistency_rsabsgap_252d_base_v135_signal(closeadj):
    result = (_safe_div(_f049_up_periods(closeadj, 252), _mean(closeadj, 252)) - 1.0).abs() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# RS line × log close 21d
def f049mcs_f049_momentum_consistency_rsxlog_21d_base_v136_signal(closeadj):
    result = _f049_up_periods(closeadj, 21) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# RS line × log close 252d
def f049mcs_f049_momentum_consistency_rsxlog_252d_base_v137_signal(closeadj):
    result = _safe_div(_f049_up_periods(closeadj, 252), _mean(closeadj, 252)) * np.log(_safe_div(closeadj, _mean(closeadj, 252)).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# RS new-high oscillator (rs - max) over recent window 21d
def f049mcs_f049_momentum_consistency_rsoscnh_21d_base_v138_signal(closeadj):
    rs = _f049_up_periods(closeadj, 10)
    rs_max = rs.rolling(21, min_periods=5).max()
    result = (rs - rs_max) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS new-high oscillator 63d
def f049mcs_f049_momentum_consistency_rsoscnh_63d_base_v139_signal(closeadj):
    rs = _f049_up_periods(closeadj, 21)
    rs_max = rs.rolling(63, min_periods=21).max()
    result = (rs - rs_max) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS new-high oscillator 252d
def f049mcs_f049_momentum_consistency_rsoscnh_252d_base_v140_signal(closeadj):
    rs = _f049_up_periods(closeadj, 63)
    rs_max = rs.rolling(252, min_periods=63).max()
    result = (rs - rs_max) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line × close × close 21d (dollar^2)
def f049mcs_f049_momentum_consistency_rsxdsq_21d_base_v141_signal(closeadj):
    result = _f049_up_periods(closeadj, 21) * closeadj * _mean(closeadj, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# RS line × dollar^2 63d
def f049mcs_f049_momentum_consistency_rsxdsq_63d_base_v142_signal(closeadj):
    result = _f049_up_periods(closeadj, 63) * closeadj * _mean(closeadj, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# RS line / max(rs over 63d) - new high ratio
def f049mcs_f049_momentum_consistency_rsdmax_63d_base_v143_signal(closeadj):
    rs = _f049_up_periods(closeadj, 21)
    rs_max = rs.rolling(63, min_periods=21).max().replace(0, np.nan)
    result = (rs / rs_max) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line / max over 252d
def f049mcs_f049_momentum_consistency_rsdmax_252d_base_v144_signal(closeadj):
    rs = _f049_up_periods(closeadj, 63)
    rs_max = rs.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (rs / rs_max) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line / max 504d
def f049mcs_f049_momentum_consistency_rsdmax_504d_base_v145_signal(closeadj):
    rs = _f049_up_periods(closeadj, 126)
    rs_max = rs.rolling(504, min_periods=126).max().replace(0, np.nan)
    result = (rs / rs_max) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line difference from 504-day mean × close
def f049mcs_f049_momentum_consistency_rsdmean_504d_base_v146_signal(closeadj):
    rs = _f049_up_periods(closeadj, 63)
    result = (rs - _mean(rs, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line difference from 252-day mean × close
def f049mcs_f049_momentum_consistency_rsdmean_252d_base_v147_signal(closeadj):
    rs = _f049_up_periods(closeadj, 21)
    result = (rs - _mean(rs, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# RS line cumulative product over 21d × close
def f049mcs_f049_momentum_consistency_rscum_21d_base_v148_signal(closeadj):
    rs = _safe_div(_f049_up_periods(closeadj, 21), _mean(closeadj, 252)).replace(0, np.nan).abs()
    result = np.log(rs).rolling(21, min_periods=5).sum() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# RS line cumulative product over 252d × close
def f049mcs_f049_momentum_consistency_rscum_252d_base_v149_signal(closeadj):
    rs = _safe_div(_f049_up_periods(closeadj, 21), _mean(closeadj, 252)).replace(0, np.nan).abs()
    result = np.log(rs).rolling(252, min_periods=63).sum() * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# RS line × leadership smoothed × close 126d
def f049mcs_f049_momentum_consistency_rsxleadsm_126d_base_v150_signal(closeadj):
    lc = _f049_smooth_leadership(closeadj, 126) / closeadj.replace(0, np.nan)
    rate = _mean(lc, 126) + 0.1
    result = _f049_up_periods(closeadj, 126) * rate * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f049mcs_f049_momentum_consistency_rsdmed_63d_base_v076_signal,
    f049mcs_f049_momentum_consistency_rsdmed_252d_base_v077_signal,
    f049mcs_f049_momentum_consistency_rsdmed_504d_base_v078_signal,
    f049mcs_f049_momentum_consistency_rsmax_21d_base_v079_signal,
    f049mcs_f049_momentum_consistency_rsmax_63d_base_v080_signal,
    f049mcs_f049_momentum_consistency_rsmax_252d_base_v081_signal,
    f049mcs_f049_momentum_consistency_rsmin_63d_base_v082_signal,
    f049mcs_f049_momentum_consistency_rsmin_252d_base_v083_signal,
    f049mcs_f049_momentum_consistency_rssum_21d_base_v084_signal,
    f049mcs_f049_momentum_consistency_rssum_63d_base_v085_signal,
    f049mcs_f049_momentum_consistency_rssum_252d_base_v086_signal,
    f049mcs_f049_momentum_consistency_rsnh21_base_v087_signal,
    f049mcs_f049_momentum_consistency_rsnh126_base_v088_signal,
    f049mcs_f049_momentum_consistency_rsnhrate_252d_base_v089_signal,
    f049mcs_f049_momentum_consistency_rsnhrate_504d_base_v090_signal,
    f049mcs_f049_momentum_consistency_rsgxm_21d_base_v091_signal,
    f049mcs_f049_momentum_consistency_rsgxm_63d_base_v092_signal,
    f049mcs_f049_momentum_consistency_rsgxm_252d_base_v093_signal,
    f049mcs_f049_momentum_consistency_rsnhz_63d_base_v094_signal,
    f049mcs_f049_momentum_consistency_rsnhz_252d_base_v095_signal,
    f049mcs_f049_momentum_consistency_rssign_21d_base_v096_signal,
    f049mcs_f049_momentum_consistency_rssign_63d_base_v097_signal,
    f049mcs_f049_momentum_consistency_rssign_252d_base_v098_signal,
    f049mcs_f049_momentum_consistency_rsxstd_21d_base_v099_signal,
    f049mcs_f049_momentum_consistency_rsxstd_63d_base_v100_signal,
    f049mcs_f049_momentum_consistency_rsxstd_252d_base_v101_signal,
    f049mcs_f049_momentum_consistency_rsmoment_21v42_base_v102_signal,
    f049mcs_f049_momentum_consistency_rsmoment_42v189_base_v103_signal,
    f049mcs_f049_momentum_consistency_rsmoment_189v378_base_v104_signal,
    f049mcs_f049_momentum_consistency_rsratio_5v21_base_v105_signal,
    f049mcs_f049_momentum_consistency_rsratio_10v42_base_v106_signal,
    f049mcs_f049_momentum_consistency_rsratio_42v189_base_v107_signal,
    f049mcs_f049_momentum_consistency_rsz_42d_base_v108_signal,
    f049mcs_f049_momentum_consistency_rsz_189d_base_v109_signal,
    f049mcs_f049_momentum_consistency_rsz_378d_base_v110_signal,
    f049mcs_f049_momentum_consistency_rsnhxsq_63d_base_v111_signal,
    f049mcs_f049_momentum_consistency_rsnhxsq_252d_base_v112_signal,
    f049mcs_f049_momentum_consistency_rsema5_21d_base_v113_signal,
    f049mcs_f049_momentum_consistency_rsema10_63d_base_v114_signal,
    f049mcs_f049_momentum_consistency_rsema42_252d_base_v115_signal,
    f049mcs_f049_momentum_consistency_rsnhmean_63d_base_v116_signal,
    f049mcs_f049_momentum_consistency_rsnhmean_252d_base_v117_signal,
    f049mcs_f049_momentum_consistency_rsnhstd_63d_base_v118_signal,
    f049mcs_f049_momentum_consistency_rsnhstd_252d_base_v119_signal,
    f049mcs_f049_momentum_consistency_rsmclose_21d_base_v120_signal,
    f049mcs_f049_momentum_consistency_rsmclose_63d_base_v121_signal,
    f049mcs_f049_momentum_consistency_rsmclose_252d_base_v122_signal,
    f049mcs_f049_momentum_consistency_daysatnh_63d_base_v123_signal,
    f049mcs_f049_momentum_consistency_daysatnh_252d_base_v124_signal,
    f049mcs_f049_momentum_consistency_rsgeo_21d_base_v125_signal,
    f049mcs_f049_momentum_consistency_rsgeo_63d_base_v126_signal,
    f049mcs_f049_momentum_consistency_rsgeo_252d_base_v127_signal,
    f049mcs_f049_momentum_consistency_rsxret_5d_base_v128_signal,
    f049mcs_f049_momentum_consistency_rsxret_21d_base_v129_signal,
    f049mcs_f049_momentum_consistency_rsxret_63d_base_v130_signal,
    f049mcs_f049_momentum_consistency_rsnhxret_5d_base_v131_signal,
    f049mcs_f049_momentum_consistency_rsnhxret_21d_base_v132_signal,
    f049mcs_f049_momentum_consistency_rsabsgap_21d_base_v133_signal,
    f049mcs_f049_momentum_consistency_rsabsgap_63d_base_v134_signal,
    f049mcs_f049_momentum_consistency_rsabsgap_252d_base_v135_signal,
    f049mcs_f049_momentum_consistency_rsxlog_21d_base_v136_signal,
    f049mcs_f049_momentum_consistency_rsxlog_252d_base_v137_signal,
    f049mcs_f049_momentum_consistency_rsoscnh_21d_base_v138_signal,
    f049mcs_f049_momentum_consistency_rsoscnh_63d_base_v139_signal,
    f049mcs_f049_momentum_consistency_rsoscnh_252d_base_v140_signal,
    f049mcs_f049_momentum_consistency_rsxdsq_21d_base_v141_signal,
    f049mcs_f049_momentum_consistency_rsxdsq_63d_base_v142_signal,
    f049mcs_f049_momentum_consistency_rsdmax_63d_base_v143_signal,
    f049mcs_f049_momentum_consistency_rsdmax_252d_base_v144_signal,
    f049mcs_f049_momentum_consistency_rsdmax_504d_base_v145_signal,
    f049mcs_f049_momentum_consistency_rsdmean_504d_base_v146_signal,
    f049mcs_f049_momentum_consistency_rsdmean_252d_base_v147_signal,
    f049mcs_f049_momentum_consistency_rscum_21d_base_v148_signal,
    f049mcs_f049_momentum_consistency_rscum_252d_base_v149_signal,
    f049mcs_f049_momentum_consistency_rsxleadsm_126d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F049_MOMENTUM_CONSISTENCY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f049_up_periods", "_f049_consistency_ratio", "_f049_smooth_leadership")
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
    print(f"OK f049_momentum_consistency_base_076_150_claude: {n_features} features pass")
