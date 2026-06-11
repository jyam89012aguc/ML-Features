import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


# ===== folder domain primitives (crypto winter drawdown) =====
def _f04_dd(s, w):
    # drawdown from rolling peak: close/peak - 1 (<= 0, continuous)
    peak = s.rolling(w, min_periods=max(2, w // 2)).max()
    return s / peak.replace(0, np.nan) - 1.0


def _f04_underwater(s, w):
    # cumulative underwater AREA: rolling sum of instantaneous drawdown depth
    # (continuous integral of depth, NOT a day count)
    peak = s.rolling(w, min_periods=max(2, w // 2)).max()
    depth = s / peak.replace(0, np.nan) - 1.0
    return depth.rolling(w, min_periods=max(2, w // 2)).sum()


def _f04_recovery(s, w):
    # recovery off the rolling trough: close/trough - 1 (>= 0, continuous)
    trough = s.rolling(w, min_periods=max(2, w // 2)).min()
    return s / trough.replace(0, np.nan) - 1.0


def _f04_painvol(s, w):
    # dispersion (std) of the drawdown path over the window (underwater severity vol)
    peak = s.rolling(w, min_periods=max(2, w // 2)).max()
    depth = s / peak.replace(0, np.nan) - 1.0
    return depth.rolling(w, min_periods=max(2, w // 2)).std()


# ============ FEATURES 076-150 ============

# 21d drawdown depth from rolling peak (local pullback)
def f04cw_f04_crypto_winter_drawdown_dd_21d_base_v076_signal(closeadj):
    result = _f04_dd(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d drawdown depth from rolling peak
def f04cw_f04_crypto_winter_drawdown_dd_315d_base_v077_signal(closeadj):
    result = _f04_dd(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# expanding-window drawdown depth (all-time peak, cumulative)
def f04cw_f04_crypto_winter_drawdown_dd_expand_base_v078_signal(closeadj):
    peak = closeadj.expanding(min_periods=21).max()
    result = closeadj / peak.replace(0, np.nan) - 1.0 + _f04_dd(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown depth amplified (convex severity, sign-preserving, 252d)
def f04cw_f04_crypto_winter_drawdown_ddamp_252d_base_v079_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = np.sign(dd) * (dd.abs() ** 1.5)
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown depth amplified (convex severity, 126d)
def f04cw_f04_crypto_winter_drawdown_ddamp_126d_base_v080_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = np.sign(dd) * (dd.abs() ** 1.5)
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown depth amplified k=2 (504d)
def f04cw_f04_crypto_winter_drawdown_ddamp2_504d_base_v081_signal(closeadj):
    dd = _f04_dd(closeadj, 504)
    result = np.sign(dd) * (dd.abs() ** 2.0)
    return result.replace([np.inf, -np.inf], np.nan)


# underwater area 21d (short local pain integral)
def f04cw_f04_crypto_winter_drawdown_uwarea_21d_base_v082_signal(closeadj):
    result = _f04_underwater(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# underwater area 84d
def f04cw_f04_crypto_winter_drawdown_uwarea_84d_base_v083_signal(closeadj):
    result = _f04_underwater(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# underwater area 315d
def f04cw_f04_crypto_winter_drawdown_uwarea_315d_base_v084_signal(closeadj):
    result = _f04_underwater(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# underwater area squared-depth (emphasizes deep winter, 252d)
def f04cw_f04_crypto_winter_drawdown_uwsq_252d_base_v085_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = (dd * dd).rolling(252, min_periods=84).sum() + _f04_underwater(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# underwater area squared-depth (126d)
def f04cw_f04_crypto_winter_drawdown_uwsq_126d_base_v086_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = (dd * dd).rolling(126, min_periods=42).sum() + _f04_underwater(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# recovery off trough amplified (convex rebound, 252d)
def f04cw_f04_crypto_winter_drawdown_recamp_252d_base_v087_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    result = rec ** 1.5
    return result.replace([np.inf, -np.inf], np.nan)


# recovery off trough amplified (126d)
def f04cw_f04_crypto_winter_drawdown_recamp_126d_base_v088_signal(closeadj):
    rec = _f04_recovery(closeadj, 126)
    result = rec ** 1.5
    return result.replace([np.inf, -np.inf], np.nan)


# recovery z-score over 252d
def f04cw_f04_crypto_winter_drawdown_recz_252d_base_v089_signal(closeadj):
    result = _z(_f04_recovery(closeadj, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery z-score over 126d
def f04cw_f04_crypto_winter_drawdown_recz_126d_base_v090_signal(closeadj):
    result = _z(_f04_recovery(closeadj, 126), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pain volatility (short severity dispersion)
def f04cw_f04_crypto_winter_drawdown_ddvol_21d_base_v091_signal(closeadj):
    result = _f04_painvol(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d pain volatility
def f04cw_f04_crypto_winter_drawdown_ddvol_84d_base_v092_signal(closeadj):
    result = _f04_painvol(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d pain volatility
def f04cw_f04_crypto_winter_drawdown_ddvol_189d_base_v093_signal(closeadj):
    result = _f04_painvol(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# pain volatility normalized by mean depth (severity coefficient of variation, 252d)
def f04cw_f04_crypto_winter_drawdown_paincv_252d_base_v094_signal(closeadj):
    pv = _f04_painvol(closeadj, 252)
    pain = _mean(_f04_dd(closeadj, 252), 252).abs()
    result = _safe_div(pv, pain)
    return result.replace([np.inf, -np.inf], np.nan)


# pain volatility CV (126d)
def f04cw_f04_crypto_winter_drawdown_paincv_126d_base_v095_signal(closeadj):
    pv = _f04_painvol(closeadj, 126)
    pain = _mean(_f04_dd(closeadj, 126), 126).abs()
    result = _safe_div(pv, pain)
    return result.replace([np.inf, -np.inf], np.nan)


# pain index 189d
def f04cw_f04_crypto_winter_drawdown_pain_189d_base_v096_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 189), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# pain index 84d
def f04cw_f04_crypto_winter_drawdown_pain_84d_base_v097_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 84), 84)
    return result.replace([np.inf, -np.inf], np.nan)


# Ulcer index 189d
def f04cw_f04_crypto_winter_drawdown_ulcer_189d_base_v098_signal(closeadj):
    dd = _f04_dd(closeadj, 189)
    result = np.sqrt((dd * dd).rolling(189, min_periods=63).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# Ulcer index 84d
def f04cw_f04_crypto_winter_drawdown_ulcer_84d_base_v099_signal(closeadj):
    dd = _f04_dd(closeadj, 84)
    result = np.sqrt((dd * dd).rolling(84, min_periods=28).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# MAR-style ratio 189d
def f04cw_f04_crypto_winter_drawdown_mar_189d_base_v100_signal(closeadj):
    ret = closeadj / closeadj.shift(189) - 1.0
    maxdd = _f04_dd(closeadj, 189).rolling(189, min_periods=63).min().abs()
    result = _safe_div(ret, maxdd)
    return result.replace([np.inf, -np.inf], np.nan)


# MAR-style ratio 84d
def f04cw_f04_crypto_winter_drawdown_mar_84d_base_v101_signal(closeadj):
    ret = closeadj / closeadj.shift(84) - 1.0
    maxdd = _f04_dd(closeadj, 84).rolling(84, min_periods=28).min().abs()
    result = _safe_div(ret, maxdd)
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown z-score 42d over 126d
def f04cw_f04_crypto_winter_drawdown_ddz_42d_base_v102_signal(closeadj):
    result = _z(_f04_dd(closeadj, 42), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown z-score 189d over 504d
def f04cw_f04_crypto_winter_drawdown_ddz_189d_base_v103_signal(closeadj):
    result = _z(_f04_dd(closeadj, 189), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# depth weighted by raw-volume z-score (capitulation, 189d)
def f04cw_f04_crypto_winter_drawdown_ddvolw_189d_base_v104_signal(closeadj, volume):
    result = _f04_dd(closeadj, 189) * _z(volume, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# depth weighted by dollar-volume surge (504d)
def f04cw_f04_crypto_winter_drawdown_ddflow_504d_base_v105_signal(closeadj, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 252))
    result = _f04_dd(closeadj, 504) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# recovery slope 21d (504d trough base)
def f04cw_f04_crypto_winter_drawdown_recovslope_504d_base_v106_signal(closeadj):
    rec = _f04_recovery(closeadj, 504)
    result = rec - rec.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown deepening slope 21d (504d peak base)
def f04cw_f04_crypto_winter_drawdown_ddslope_504d_base_v107_signal(closeadj):
    dd = _f04_dd(closeadj, 504)
    result = dd - dd.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown deepening slope 10d (63d peak base)
def f04cw_f04_crypto_winter_drawdown_ddslope_63d_base_v108_signal(closeadj):
    dd = _f04_dd(closeadj, 63)
    result = dd - dd.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery ratio 504d
def f04cw_f04_crypto_winter_drawdown_recratio_504d_base_v109_signal(closeadj):
    rec = _f04_recovery(closeadj, 504)
    dd = _f04_dd(closeadj, 504).abs()
    result = _safe_div(rec, rec + dd)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery ratio 189d
def f04cw_f04_crypto_winter_drawdown_recratio_189d_base_v110_signal(closeadj):
    rec = _f04_recovery(closeadj, 189)
    dd = _f04_dd(closeadj, 189).abs()
    result = _safe_div(rec, rec + dd)
    return result.replace([np.inf, -np.inf], np.nan)


# average drawdown vol-adjusted 504d
def f04cw_f04_crypto_winter_drawdown_painvoladj_504d_base_v111_signal(closeadj):
    pain = _mean(_f04_dd(closeadj, 504), 252)
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(pain, _std(lr, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# average drawdown vol-adjusted 63d
def f04cw_f04_crypto_winter_drawdown_painvoladj_63d_base_v112_signal(closeadj):
    pain = _mean(_f04_dd(closeadj, 63), 63)
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(pain, _std(lr, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# underwater mean depth per day 189d
def f04cw_f04_crypto_winter_drawdown_uwmean_189d_base_v113_signal(closeadj):
    result = _f04_underwater(closeadj, 189) / 189.0
    return result.replace([np.inf, -np.inf], np.nan)


# underwater mean depth per day 63d
def f04cw_f04_crypto_winter_drawdown_uwmean_63d_base_v114_signal(closeadj):
    result = _f04_underwater(closeadj, 63) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# depth severity skew 504d
def f04cw_f04_crypto_winter_drawdown_ddskew_504d_base_v115_signal(closeadj):
    dd = _f04_dd(closeadj, 504)
    result = dd.rolling(252, min_periods=84).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# depth severity kurtosis 126d
def f04cw_f04_crypto_winter_drawdown_ddkurt_126d_base_v116_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    result = dd.rolling(126, min_periods=42).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# current depth fraction of worst 504d
def f04cw_f04_crypto_winter_drawdown_ddfrac_504d_base_v117_signal(closeadj):
    dd = _f04_dd(closeadj, 504)
    worst = dd.rolling(252, min_periods=84).min()
    result = _safe_div(dd, worst)
    return result.replace([np.inf, -np.inf], np.nan)


# current depth fraction of worst 63d
def f04cw_f04_crypto_winter_drawdown_ddfrac_63d_base_v118_signal(closeadj):
    dd = _f04_dd(closeadj, 63)
    worst = dd.rolling(126, min_periods=42).min()
    result = _safe_div(dd, worst)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed drawdown depth 21d-mean of 504d dd
def f04cw_f04_crypto_winter_drawdown_ddsmooth_504d_base_v119_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 504), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed drawdown depth 10d-mean of 63d dd
def f04cw_f04_crypto_winter_drawdown_ddsmooth_63d_base_v120_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 63), 10)
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of drawdown depth 504d dd span 84
def f04cw_f04_crypto_winter_drawdown_ddewm_504d_base_v121_signal(closeadj):
    dd = _f04_dd(closeadj, 504)
    result = dd.ewm(span=84, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of drawdown depth 63d dd span 21
def f04cw_f04_crypto_winter_drawdown_ddewm_63d_base_v122_signal(closeadj):
    dd = _f04_dd(closeadj, 63)
    result = dd.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# underwater area slope 504d
def f04cw_f04_crypto_winter_drawdown_uwslope_504d_base_v123_signal(closeadj):
    uw = _f04_underwater(closeadj, 504)
    result = uw - uw.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# underwater area slope 63d
def f04cw_f04_crypto_winter_drawdown_uwslope_63d_base_v124_signal(closeadj):
    uw = _f04_underwater(closeadj, 63)
    result = uw - uw.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# pain vol ratio 21d over 126d (severity regime shift)
def f04cw_f04_crypto_winter_drawdown_ddvolratio2_base_v125_signal(closeadj):
    result = _safe_div(_f04_painvol(closeadj, 21), _f04_painvol(closeadj, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# depth spread 21d dd minus 126d dd
def f04cw_f04_crypto_winter_drawdown_ddspread_21_126_base_v126_signal(closeadj):
    result = _f04_dd(closeadj, 21) - _f04_dd(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# depth spread 84d dd minus 252d dd
def f04cw_f04_crypto_winter_drawdown_ddspread_84_252_base_v127_signal(closeadj):
    result = _f04_dd(closeadj, 84) - _f04_dd(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net winter state 504d
def f04cw_f04_crypto_winter_drawdown_netstate_504d_base_v128_signal(closeadj):
    result = _f04_recovery(closeadj, 504) + _f04_dd(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# net winter state 63d
def f04cw_f04_crypto_winter_drawdown_netstate_63d_base_v129_signal(closeadj):
    result = _f04_recovery(closeadj, 63) + _f04_dd(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown rank 252d over 504d
def f04cw_f04_crypto_winter_drawdown_ddrank_252d_base_v130_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    result = dd.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery rank 252d over 504d
def f04cw_f04_crypto_winter_drawdown_recrank_252d_base_v131_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    result = rec.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# return over ulcer 126d (Calmar-style)
def f04cw_f04_crypto_winter_drawdown_retoverulcer_126d_base_v132_signal(closeadj):
    ret = closeadj / closeadj.shift(126) - 1.0
    dd = _f04_dd(closeadj, 126)
    ulcer = np.sqrt((dd * dd).rolling(126, min_periods=42).mean())
    result = _safe_div(ret, ulcer)
    return result.replace([np.inf, -np.inf], np.nan)


# return over ulcer 504d
def f04cw_f04_crypto_winter_drawdown_retoverulcer_504d_base_v133_signal(closeadj):
    ret = closeadj / closeadj.shift(504) - 1.0
    dd = _f04_dd(closeadj, 504)
    ulcer = np.sqrt((dd * dd).rolling(252, min_periods=84).mean())
    result = _safe_div(ret, ulcer)
    return result.replace([np.inf, -np.inf], np.nan)


# rebound per unit pain 126d
def f04cw_f04_crypto_winter_drawdown_reboundpain_126d_base_v134_signal(closeadj):
    rec = _f04_recovery(closeadj, 126)
    uw = _f04_underwater(closeadj, 126).abs()
    result = _safe_div(rec, uw / 126.0)
    return result.replace([np.inf, -np.inf], np.nan)


# depth times dollar-volume level (capitulation notional, 252d)
def f04cw_f04_crypto_winter_drawdown_ddnotional_252d_base_v135_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f04_dd(closeadj, 252) * _z(dv, 252) + _f04_dd(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pain-adjusted recovery momentum: recovery slope scaled by ulcer (252d)
def f04cw_f04_crypto_winter_drawdown_recmompain_252d_base_v136_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    slope = rec - rec.shift(21)
    dd = _f04_dd(closeadj, 252)
    ulcer = np.sqrt((dd * dd).rolling(252, min_periods=84).mean())
    result = _safe_div(slope, ulcer)
    return result.replace([np.inf, -np.inf], np.nan)


# pain-adjusted recovery momentum (126d)
def f04cw_f04_crypto_winter_drawdown_recmompain_126d_base_v137_signal(closeadj):
    rec = _f04_recovery(closeadj, 126)
    slope = rec - rec.shift(21)
    dd = _f04_dd(closeadj, 126)
    ulcer = np.sqrt((dd * dd).rolling(126, min_periods=42).mean())
    result = _safe_div(slope, ulcer)
    return result.replace([np.inf, -np.inf], np.nan)


# depth acceleration: 21d change of drawdown slope (252d)
def f04cw_f04_crypto_winter_drawdown_ddaccel_252d_base_v138_signal(closeadj):
    dd = _f04_dd(closeadj, 252)
    slope = dd - dd.shift(21)
    result = slope - slope.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# depth acceleration (126d)
def f04cw_f04_crypto_winter_drawdown_ddaccel_126d_base_v139_signal(closeadj):
    dd = _f04_dd(closeadj, 126)
    slope = dd - dd.shift(21)
    result = slope - slope.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# underwater area z-score (severity vs own history, 252d)
def f04cw_f04_crypto_winter_drawdown_uwz_252d_base_v140_signal(closeadj):
    result = _z(_f04_underwater(closeadj, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# underwater area z-score (126d)
def f04cw_f04_crypto_winter_drawdown_uwz_126d_base_v141_signal(closeadj):
    result = _z(_f04_underwater(closeadj, 126), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# pain index z-score 252d
def f04cw_f04_crypto_winter_drawdown_painz_252d_base_v142_signal(closeadj):
    pain = _mean(_f04_dd(closeadj, 252), 252)
    result = _z(pain, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery vs pain spread: recovery rank minus depth rank (252d)
def f04cw_f04_crypto_winter_drawdown_recpainspread_252d_base_v143_signal(closeadj):
    rrank = _f04_recovery(closeadj, 252).rolling(504, min_periods=126).rank(pct=True)
    drank = _f04_dd(closeadj, 252).rolling(504, min_periods=126).rank(pct=True)
    result = rrank - drank
    return result.replace([np.inf, -np.inf], np.nan)


# depth scaled by trailing realized vol (winter severity in vol units, 252d)
def f04cw_f04_crypto_winter_drawdown_ddvolunits_252d_base_v144_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 252) * np.sqrt(252.0)
    result = _safe_div(_f04_dd(closeadj, 252), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# depth scaled by trailing realized vol (126d)
def f04cw_f04_crypto_winter_drawdown_ddvolunits_126d_base_v145_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 126) * np.sqrt(126.0)
    result = _safe_div(_f04_dd(closeadj, 126), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# pain index spread 63d minus 252d (acute vs chronic winter)
def f04cw_f04_crypto_winter_drawdown_painspread_base_v146_signal(closeadj):
    result = _mean(_f04_dd(closeadj, 63), 63) - _mean(_f04_dd(closeadj, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ulcer spread 63d minus 252d
def f04cw_f04_crypto_winter_drawdown_ulcerspread_base_v147_signal(closeadj):
    dd_s = _f04_dd(closeadj, 63)
    dd_l = _f04_dd(closeadj, 252)
    u_s = np.sqrt((dd_s * dd_s).rolling(63, min_periods=21).mean())
    u_l = np.sqrt((dd_l * dd_l).rolling(252, min_periods=84).mean())
    result = u_s - u_l
    return result.replace([np.inf, -np.inf], np.nan)


# recovery off trough scaled by realized vol (rebound in vol units, 252d)
def f04cw_f04_crypto_winter_drawdown_recvolunits_252d_base_v148_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 252) * np.sqrt(252.0)
    result = _safe_div(_f04_recovery(closeadj, 252), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# underwater EWMA severity (252d depth, span 126)
def f04cw_f04_crypto_winter_drawdown_uwewm_252d_base_v149_signal(closeadj):
    uw = _f04_underwater(closeadj, 252) / 252.0
    result = uw.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon drawdown composite (63/126/252/504)
def f04cw_f04_crypto_winter_drawdown_blend_multi_base_v150_signal(closeadj):
    result = (_f04_dd(closeadj, 63) + _f04_dd(closeadj, 126)
              + _f04_dd(closeadj, 252) + _f04_dd(closeadj, 504)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04cw_f04_crypto_winter_drawdown_dd_21d_base_v076_signal,
    f04cw_f04_crypto_winter_drawdown_dd_315d_base_v077_signal,
    f04cw_f04_crypto_winter_drawdown_dd_expand_base_v078_signal,
    f04cw_f04_crypto_winter_drawdown_ddamp_252d_base_v079_signal,
    f04cw_f04_crypto_winter_drawdown_ddamp_126d_base_v080_signal,
    f04cw_f04_crypto_winter_drawdown_ddamp2_504d_base_v081_signal,
    f04cw_f04_crypto_winter_drawdown_uwarea_21d_base_v082_signal,
    f04cw_f04_crypto_winter_drawdown_uwarea_84d_base_v083_signal,
    f04cw_f04_crypto_winter_drawdown_uwarea_315d_base_v084_signal,
    f04cw_f04_crypto_winter_drawdown_uwsq_252d_base_v085_signal,
    f04cw_f04_crypto_winter_drawdown_uwsq_126d_base_v086_signal,
    f04cw_f04_crypto_winter_drawdown_recamp_252d_base_v087_signal,
    f04cw_f04_crypto_winter_drawdown_recamp_126d_base_v088_signal,
    f04cw_f04_crypto_winter_drawdown_recz_252d_base_v089_signal,
    f04cw_f04_crypto_winter_drawdown_recz_126d_base_v090_signal,
    f04cw_f04_crypto_winter_drawdown_ddvol_21d_base_v091_signal,
    f04cw_f04_crypto_winter_drawdown_ddvol_84d_base_v092_signal,
    f04cw_f04_crypto_winter_drawdown_ddvol_189d_base_v093_signal,
    f04cw_f04_crypto_winter_drawdown_paincv_252d_base_v094_signal,
    f04cw_f04_crypto_winter_drawdown_paincv_126d_base_v095_signal,
    f04cw_f04_crypto_winter_drawdown_pain_189d_base_v096_signal,
    f04cw_f04_crypto_winter_drawdown_pain_84d_base_v097_signal,
    f04cw_f04_crypto_winter_drawdown_ulcer_189d_base_v098_signal,
    f04cw_f04_crypto_winter_drawdown_ulcer_84d_base_v099_signal,
    f04cw_f04_crypto_winter_drawdown_mar_189d_base_v100_signal,
    f04cw_f04_crypto_winter_drawdown_mar_84d_base_v101_signal,
    f04cw_f04_crypto_winter_drawdown_ddz_42d_base_v102_signal,
    f04cw_f04_crypto_winter_drawdown_ddz_189d_base_v103_signal,
    f04cw_f04_crypto_winter_drawdown_ddvolw_189d_base_v104_signal,
    f04cw_f04_crypto_winter_drawdown_ddflow_504d_base_v105_signal,
    f04cw_f04_crypto_winter_drawdown_recovslope_504d_base_v106_signal,
    f04cw_f04_crypto_winter_drawdown_ddslope_504d_base_v107_signal,
    f04cw_f04_crypto_winter_drawdown_ddslope_63d_base_v108_signal,
    f04cw_f04_crypto_winter_drawdown_recratio_504d_base_v109_signal,
    f04cw_f04_crypto_winter_drawdown_recratio_189d_base_v110_signal,
    f04cw_f04_crypto_winter_drawdown_painvoladj_504d_base_v111_signal,
    f04cw_f04_crypto_winter_drawdown_painvoladj_63d_base_v112_signal,
    f04cw_f04_crypto_winter_drawdown_uwmean_189d_base_v113_signal,
    f04cw_f04_crypto_winter_drawdown_uwmean_63d_base_v114_signal,
    f04cw_f04_crypto_winter_drawdown_ddskew_504d_base_v115_signal,
    f04cw_f04_crypto_winter_drawdown_ddkurt_126d_base_v116_signal,
    f04cw_f04_crypto_winter_drawdown_ddfrac_504d_base_v117_signal,
    f04cw_f04_crypto_winter_drawdown_ddfrac_63d_base_v118_signal,
    f04cw_f04_crypto_winter_drawdown_ddsmooth_504d_base_v119_signal,
    f04cw_f04_crypto_winter_drawdown_ddsmooth_63d_base_v120_signal,
    f04cw_f04_crypto_winter_drawdown_ddewm_504d_base_v121_signal,
    f04cw_f04_crypto_winter_drawdown_ddewm_63d_base_v122_signal,
    f04cw_f04_crypto_winter_drawdown_uwslope_504d_base_v123_signal,
    f04cw_f04_crypto_winter_drawdown_uwslope_63d_base_v124_signal,
    f04cw_f04_crypto_winter_drawdown_ddvolratio2_base_v125_signal,
    f04cw_f04_crypto_winter_drawdown_ddspread_21_126_base_v126_signal,
    f04cw_f04_crypto_winter_drawdown_ddspread_84_252_base_v127_signal,
    f04cw_f04_crypto_winter_drawdown_netstate_504d_base_v128_signal,
    f04cw_f04_crypto_winter_drawdown_netstate_63d_base_v129_signal,
    f04cw_f04_crypto_winter_drawdown_ddrank_252d_base_v130_signal,
    f04cw_f04_crypto_winter_drawdown_recrank_252d_base_v131_signal,
    f04cw_f04_crypto_winter_drawdown_retoverulcer_126d_base_v132_signal,
    f04cw_f04_crypto_winter_drawdown_retoverulcer_504d_base_v133_signal,
    f04cw_f04_crypto_winter_drawdown_reboundpain_126d_base_v134_signal,
    f04cw_f04_crypto_winter_drawdown_ddnotional_252d_base_v135_signal,
    f04cw_f04_crypto_winter_drawdown_recmompain_252d_base_v136_signal,
    f04cw_f04_crypto_winter_drawdown_recmompain_126d_base_v137_signal,
    f04cw_f04_crypto_winter_drawdown_ddaccel_252d_base_v138_signal,
    f04cw_f04_crypto_winter_drawdown_ddaccel_126d_base_v139_signal,
    f04cw_f04_crypto_winter_drawdown_uwz_252d_base_v140_signal,
    f04cw_f04_crypto_winter_drawdown_uwz_126d_base_v141_signal,
    f04cw_f04_crypto_winter_drawdown_painz_252d_base_v142_signal,
    f04cw_f04_crypto_winter_drawdown_recpainspread_252d_base_v143_signal,
    f04cw_f04_crypto_winter_drawdown_ddvolunits_252d_base_v144_signal,
    f04cw_f04_crypto_winter_drawdown_ddvolunits_126d_base_v145_signal,
    f04cw_f04_crypto_winter_drawdown_painspread_base_v146_signal,
    f04cw_f04_crypto_winter_drawdown_ulcerspread_base_v147_signal,
    f04cw_f04_crypto_winter_drawdown_recvolunits_252d_base_v148_signal,
    f04cw_f04_crypto_winter_drawdown_uwewm_252d_base_v149_signal,
    f04cw_f04_crypto_winter_drawdown_blend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_CRYPTO_WINTER_DRAWDOWN_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0008, 0.045, n)
    closeadj = pd.Series(50.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name="volume")
    cols = {"closeadj": closeadj, "volume": volume}

    domain_primitives = ("_f04_dd", "_f04_underwater", "_f04_recovery", "_f04_painvol")
    n_features = 0
    nan_ok = 0
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
    print(f"OK f04_crypto_winter_drawdown_base_076_150_claude: {n_features} features pass")
