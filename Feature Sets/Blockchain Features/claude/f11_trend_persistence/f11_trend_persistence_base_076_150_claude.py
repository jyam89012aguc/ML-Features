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


# ===== folder domain primitives (trend persistence) =====
def _f11_slope(s, w):
    # rolling OLS slope of log(price) vs time, per-day, normalized (scale-free via log)
    y = np.log(s.replace(0, np.nan).abs() + 1e-12)
    mp = max(3, w // 2)
    t = pd.Series(np.arange(len(s), dtype="float64"), index=s.index)
    mt = t.rolling(w, min_periods=mp).mean()
    my = y.rolling(w, min_periods=mp).mean()
    cov = (t * y).rolling(w, min_periods=mp).mean() - mt * my
    vart = (t * t).rolling(w, min_periods=mp).mean() - mt * mt
    return cov / vart.replace(0, np.nan)


def _f11_r2(s, w):
    # R^2 (straightness) of the rolling log-price linear fit = corr(t, y)^2
    y = np.log(s.replace(0, np.nan).abs() + 1e-12)
    mp = max(3, w // 2)
    t = pd.Series(np.arange(len(s), dtype="float64"), index=s.index)
    mt = t.rolling(w, min_periods=mp).mean()
    my = y.rolling(w, min_periods=mp).mean()
    cov = (t * y).rolling(w, min_periods=mp).mean() - mt * my
    vart = (t * t).rolling(w, min_periods=mp).mean() - mt * mt
    vary = (y * y).rolling(w, min_periods=mp).mean() - my * my
    denom = (vart * vary).replace(0, np.nan)
    return (cov * cov) / denom


def _f11_di(s, w):
    # ADX-style directional spread (+DI - -DI) built from the series' own moves,
    # normalized by the average absolute move (ATR-like). Continuous in [-1, 1].
    d = s.diff()
    up = d.clip(lower=0.0)
    dn = (-d).clip(lower=0.0)
    mp = max(2, w // 2)
    sup = up.rolling(w, min_periods=mp).mean()
    sdn = dn.rolling(w, min_periods=mp).mean()
    atr = d.abs().rolling(w, min_periods=mp).mean()
    pdi = sup / atr.replace(0, np.nan)
    mdi = sdn / atr.replace(0, np.nan)
    return pdi - mdi


def _f11_autocorr(s, w):
    # rolling lag-1 autocorrelation of daily log returns (persistence statistic)
    r = np.log(s.replace(0, np.nan).abs() + 1e-12).diff()
    mp = max(3, w // 2)
    r1 = r.shift(1)
    mr = r.rolling(w, min_periods=mp).mean()
    mr1 = r1.rolling(w, min_periods=mp).mean()
    cov = (r * r1).rolling(w, min_periods=mp).mean() - mr * mr1
    vr = r.rolling(w, min_periods=mp).var()
    vr1 = r1.rolling(w, min_periods=mp).var()
    denom = np.sqrt((vr * vr1).clip(lower=0.0))
    return cov / denom.replace(0, np.nan)


# ============ FEATURES 076-150 ============

# 10d rolling OLS slope of log price (weekly trend)
def f11tp_f11_trend_persistence_slope_10d_base_v076_signal(closeadj):
    result = _f11_slope(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d rolling OLS slope of log price
def f11tp_f11_trend_persistence_slope_315d_base_v077_signal(closeadj):
    result = _f11_slope(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d rolling OLS slope of log price
def f11tp_f11_trend_persistence_slope_378d_base_v078_signal(closeadj):
    result = _f11_slope(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 21d slope
def f11tp_f11_trend_persistence_slopeann_21d_base_v079_signal(closeadj):
    result = _f11_slope(closeadj, 21) * 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 252d slope
def f11tp_f11_trend_persistence_slopeann_252d_base_v080_signal(closeadj):
    result = _f11_slope(closeadj, 252) * 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# 315d trend straightness R^2
def f11tp_f11_trend_persistence_r2_315d_base_v081_signal(closeadj):
    result = _f11_r2(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d trend straightness R^2
def f11tp_f11_trend_persistence_r2_10d_base_v082_signal(closeadj):
    result = _f11_r2(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# signed straightness over 21d
def f11tp_f11_trend_persistence_sr2_21d_base_v083_signal(closeadj):
    result = _f11_r2(closeadj, 21) * np.sign(_f11_slope(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# signed straightness over 504d
def f11tp_f11_trend_persistence_sr2_504d_base_v084_signal(closeadj):
    result = _f11_r2(closeadj, 504) * np.sign(_f11_slope(closeadj, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# trend quality (slope * R^2) over 42d
def f11tp_f11_trend_persistence_quality_42d_base_v085_signal(closeadj):
    result = _f11_slope(closeadj, 42) * _f11_r2(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# trend quality over 189d
def f11tp_f11_trend_persistence_quality_189d_base_v086_signal(closeadj):
    result = _f11_slope(closeadj, 189) * _f11_r2(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized trend quality over 84d
def f11tp_f11_trend_persistence_qualityann_84d_base_v087_signal(closeadj):
    result = _f11_slope(closeadj, 84) * _f11_r2(closeadj, 84) * 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# 10d directional index spread
def f11tp_f11_trend_persistence_di_10d_base_v088_signal(closeadj):
    result = _f11_di(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d directional index spread
def f11tp_f11_trend_persistence_di_84d_base_v089_signal(closeadj):
    result = _f11_di(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d directional index spread
def f11tp_f11_trend_persistence_di_189d_base_v090_signal(closeadj):
    result = _f11_di(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# ADX-style trend strength over 42d
def f11tp_f11_trend_persistence_adx_42d_base_v091_signal(closeadj):
    result = _f11_di(closeadj, 42).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# ADX-style trend strength over 252d
def f11tp_f11_trend_persistence_adx_252d_base_v092_signal(closeadj):
    result = _f11_di(closeadj, 252).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ADX over 63d (21d mean of 63d DX magnitude)
def f11tp_f11_trend_persistence_adxsm_63d_base_v093_signal(closeadj):
    result = _mean(_f11_di(closeadj, 63).abs(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# +DI/-DI log ratio over 21d
def f11tp_f11_trend_persistence_diratio_21d_base_v094_signal(closeadj):
    d = closeadj.diff()
    up = d.clip(lower=0.0).rolling(21, min_periods=10).mean()
    dn = (-d).clip(lower=0.0).rolling(21, min_periods=10).mean()
    result = np.log(_safe_div(up + 1e-12, dn + 1e-12)) + _f11_di(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# +DI/-DI log ratio over 252d
def f11tp_f11_trend_persistence_diratio_252d_base_v095_signal(closeadj):
    d = closeadj.diff()
    up = d.clip(lower=0.0).rolling(252, min_periods=84).mean()
    dn = (-d).clip(lower=0.0).rolling(252, min_periods=84).mean()
    result = np.log(_safe_div(up + 1e-12, dn + 1e-12)) + _f11_di(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 84d return lag-1 autocorrelation
def f11tp_f11_trend_persistence_acf1_84d_base_v096_signal(closeadj):
    result = _f11_autocorr(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d return lag-1 autocorrelation
def f11tp_f11_trend_persistence_acf1_189d_base_v097_signal(closeadj):
    result = _f11_autocorr(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d return lag-1 autocorrelation
def f11tp_f11_trend_persistence_acf1_504d_base_v098_signal(closeadj):
    result = _f11_autocorr(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# autocorrelation spread: 21d minus 126d (short vs long persistence)
def f11tp_f11_trend_persistence_acfspread_21_126_base_v099_signal(closeadj):
    result = _f11_autocorr(closeadj, 21) - _f11_autocorr(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio VR(5) over 252d
def f11tp_f11_trend_persistence_vr5_252d_base_v100_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    v1 = _std(r, 252) ** 2
    vk = _std(r.rolling(5, min_periods=3).sum(), 252) ** 2 / 5.0
    result = _safe_div(vk, v1) + _f11_autocorr(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio VR(10) over 126d
def f11tp_f11_trend_persistence_vr10_126d_base_v101_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    v1 = _std(r, 126) ** 2
    vk = _std(r.rolling(10, min_periods=5).sum(), 126) ** 2 / 10.0
    result = _safe_div(vk, v1) + _f11_autocorr(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio VR(21) over 504d
def f11tp_f11_trend_persistence_vr21_504d_base_v102_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    v1 = _std(r, 504) ** 2
    vk = _std(r.rolling(21, min_periods=10).sum(), 504) ** 2 / 21.0
    result = _safe_div(vk, v1) + _f11_autocorr(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log variance ratio VR(10) over 252d (centered at 0 for trending vs reverting)
def f11tp_f11_trend_persistence_lvr10_252d_base_v103_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    v1 = _std(r, 252) ** 2
    vk = _std(r.rolling(10, min_periods=5).sum(), 252) ** 2 / 10.0
    result = np.log(_safe_div(vk, v1)) + _f11_autocorr(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Kaufman efficiency ratio over 84d
def f11tp_f11_trend_persistence_eff_84d_base_v104_signal(closeadj):
    net = closeadj - closeadj.shift(84)
    path = closeadj.diff().abs().rolling(84, min_periods=42).sum()
    result = _safe_div(net, path) + _f11_slope(closeadj, 84) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Kaufman efficiency ratio over 189d
def f11tp_f11_trend_persistence_eff_189d_base_v105_signal(closeadj):
    net = closeadj - closeadj.shift(189)
    path = closeadj.diff().abs().rolling(189, min_periods=63).sum()
    result = _safe_div(net, path) + _f11_slope(closeadj, 189) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Kaufman efficiency ratio over 504d
def f11tp_f11_trend_persistence_eff_504d_base_v106_signal(closeadj):
    net = closeadj - closeadj.shift(504)
    path = closeadj.diff().abs().rolling(504, min_periods=168).sum()
    result = _safe_div(net, path) + _f11_slope(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# unsigned efficiency (path-straightness magnitude) over 63d
def f11tp_f11_trend_persistence_effmag_63d_base_v107_signal(closeadj):
    net = closeadj - closeadj.shift(63)
    path = closeadj.diff().abs().rolling(63, min_periods=21).sum()
    result = _safe_div(net.abs(), path) + _f11_slope(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# unsigned efficiency over 126d
def f11tp_f11_trend_persistence_effmag_126d_base_v108_signal(closeadj):
    net = closeadj - closeadj.shift(126)
    path = closeadj.diff().abs().rolling(126, min_periods=42).sum()
    result = _safe_div(net.abs(), path) + _f11_slope(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 42d mean displacement z
def f11tp_f11_trend_persistence_disp_42d_base_v109_signal(closeadj):
    result = _z(closeadj, 42) + _f11_slope(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 504d mean displacement z
def f11tp_f11_trend_persistence_disp_504d_base_v110_signal(closeadj):
    result = _z(closeadj, 504) + _f11_slope(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log price vs its 126d mean, scaled by log-return vol (trend extension)
def f11tp_f11_trend_persistence_ext_126d_base_v111_signal(closeadj):
    y = np.log(closeadj.replace(0, np.nan).abs() + 1e-12)
    result = _safe_div(y - _mean(y, 126), _std(y.diff(), 126)) + _f11_slope(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# magnitude-weighted consecutive-direction intensity over 42d
def f11tp_f11_trend_persistence_streak_42d_base_v112_signal(closeadj):
    r = closeadj.pct_change()
    sg = np.sign(r)
    blk = (sg != sg.shift(1)).cumsum()
    streak = sg.groupby(blk).cumcount() + 1.0
    intens = r * streak
    result = _mean(intens, 42) + _f11_di(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# magnitude-weighted consecutive-direction intensity over 252d
def f11tp_f11_trend_persistence_streak_252d_base_v113_signal(closeadj):
    r = closeadj.pct_change()
    sg = np.sign(r)
    blk = (sg != sg.shift(1)).cumsum()
    streak = sg.groupby(blk).cumcount() + 1.0
    intens = r * streak
    result = _mean(intens, 252) + _f11_di(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# directional run energy: sum of signed squared returns weighted by streak, 63d
def f11tp_f11_trend_persistence_runenergy_63d_base_v114_signal(closeadj):
    r = closeadj.pct_change()
    sg = np.sign(r)
    blk = (sg != sg.shift(1)).cumsum()
    streak = sg.groupby(blk).cumcount() + 1.0
    energy = sg * (r * r) * streak
    result = _mean(energy, 63) + _f11_di(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# slope z-scored 252d / 504w
def f11tp_f11_trend_persistence_zslope_252d_base_v115_signal(closeadj):
    result = _z(_f11_slope(closeadj, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# slope z-scored 42d / 252w
def f11tp_f11_trend_persistence_zslope_42d_base_v116_signal(closeadj):
    result = _z(_f11_slope(closeadj, 42), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# R^2 z-scored 126d / 504w
def f11tp_f11_trend_persistence_zr2_126d_base_v117_signal(closeadj):
    result = _z(_f11_r2(closeadj, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# DI z-scored 63d / 252w
def f11tp_f11_trend_persistence_zdi_63d_base_v118_signal(closeadj):
    result = _z(_f11_di(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope t-stat over 21d
def f11tp_f11_trend_persistence_tstat_21d_base_v119_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    result = _safe_div(_f11_slope(closeadj, 21), _std(lr, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# slope t-stat over 42d
def f11tp_f11_trend_persistence_tstat_42d_base_v120_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    result = _safe_div(_f11_slope(closeadj, 42), _std(lr, 42))
    return result.replace([np.inf, -np.inf], np.nan)


# slope t-stat over 504d
def f11tp_f11_trend_persistence_tstat_504d_base_v121_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    result = _safe_div(_f11_slope(closeadj, 504), _std(lr, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# slope acceleration: 42d minus 126d
def f11tp_f11_trend_persistence_slacc_42_126_base_v122_signal(closeadj):
    result = _f11_slope(closeadj, 42) - _f11_slope(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope acceleration: 21d minus 252d (multi-scale steepening)
def f11tp_f11_trend_persistence_slacc_21_252_base_v123_signal(closeadj):
    result = _f11_slope(closeadj, 21) - _f11_slope(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# R^2 spread: 21d minus 126d
def f11tp_f11_trend_persistence_r2spread_21_126_base_v124_signal(closeadj):
    result = _f11_r2(closeadj, 21) - _f11_r2(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# DI spread: 63d minus 252d
def f11tp_f11_trend_persistence_dispread_63_252_base_v125_signal(closeadj):
    result = _f11_di(closeadj, 63) - _f11_di(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed 126d slope (21d mean)
def f11tp_f11_trend_persistence_slopesm_126d_base_v126_signal(closeadj):
    result = _mean(_f11_slope(closeadj, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed 42d slope (10d mean)
def f11tp_f11_trend_persistence_slopesm_42d_base_v127_signal(closeadj):
    result = _mean(_f11_slope(closeadj, 42), 10)
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-weighted slope over 252d
def f11tp_f11_trend_persistence_effslope_252d_base_v128_signal(closeadj):
    net = closeadj - closeadj.shift(252)
    path = closeadj.diff().abs().rolling(252, min_periods=84).sum()
    eff = _safe_div(net, path)
    result = _f11_slope(closeadj, 252) * eff.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-weighted slope over 21d
def f11tp_f11_trend_persistence_effslope_21d_base_v129_signal(closeadj):
    net = closeadj - closeadj.shift(21)
    path = closeadj.diff().abs().rolling(21, min_periods=10).sum()
    eff = _safe_div(net, path)
    result = _f11_slope(closeadj, 21) * eff.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# autocorrelation-weighted slope over 126d
def f11tp_f11_trend_persistence_acfslope_126d_base_v130_signal(closeadj):
    result = _f11_slope(closeadj, 126) * _f11_autocorr(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# DI-weighted R^2 over 126d
def f11tp_f11_trend_persistence_dir2_126d_base_v131_signal(closeadj):
    result = _f11_di(closeadj, 126) * _f11_r2(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# DI-weighted R^2 over 252d
def f11tp_f11_trend_persistence_dir2_252d_base_v132_signal(closeadj):
    result = _f11_di(closeadj, 252) * _f11_r2(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# R^2-weighted efficiency over 63d (two straightness measures combined)
def f11tp_f11_trend_persistence_r2eff_63d_base_v133_signal(closeadj):
    net = closeadj - closeadj.shift(63)
    path = closeadj.diff().abs().rolling(63, min_periods=21).sum()
    eff = _safe_div(net, path)
    result = eff * _f11_r2(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# R^2-weighted efficiency over 126d
def f11tp_f11_trend_persistence_r2eff_126d_base_v134_signal(closeadj):
    net = closeadj - closeadj.shift(126)
    path = closeadj.diff().abs().rolling(126, min_periods=42).sum()
    eff = _safe_div(net, path)
    result = eff * _f11_r2(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# trend quality smoothed: 21d mean of (63d slope * 63d R^2)
def f11tp_f11_trend_persistence_qualsm_63d_base_v135_signal(closeadj):
    result = _mean(_f11_slope(closeadj, 63) * _f11_r2(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# slope minus its own 63d average (slope surprise) over 21d slope
def f11tp_f11_trend_persistence_slsurp_21d_base_v136_signal(closeadj):
    sl = _f11_slope(closeadj, 21)
    result = sl - _mean(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope surprise over 63d slope vs 126d average
def f11tp_f11_trend_persistence_slsurp_63d_base_v137_signal(closeadj):
    sl = _f11_slope(closeadj, 63)
    result = sl - _mean(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# R^2 surprise: 63d R^2 minus its 126d average
def f11tp_f11_trend_persistence_r2surp_63d_base_v138_signal(closeadj):
    rr = _f11_r2(closeadj, 63)
    result = rr - _mean(rr, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope percentile rank over 252d (63d slope)
def f11tp_f11_trend_persistence_slrank_63d_base_v139_signal(closeadj):
    sl = _f11_slope(closeadj, 63)
    result = sl.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# R^2 percentile rank over 252d (126d R^2)
def f11tp_f11_trend_persistence_r2rank_126d_base_v140_signal(closeadj):
    rr = _f11_r2(closeadj, 126)
    result = rr.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed 63d slope (span 21)
def f11tp_f11_trend_persistence_ewmslope_63d_base_v141_signal(closeadj):
    result = _f11_slope(closeadj, 63).ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed 126d slope (span 42)
def f11tp_f11_trend_persistence_ewmslope_126d_base_v142_signal(closeadj):
    result = _f11_slope(closeadj, 126).ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# straightness-gated directional run: DI(63) * efficiency(63)
def f11tp_f11_trend_persistence_dieff_63d_base_v143_signal(closeadj):
    net = closeadj - closeadj.shift(63)
    path = closeadj.diff().abs().rolling(63, min_periods=21).sum()
    eff = _safe_div(net, path)
    result = _f11_di(closeadj, 63) * eff.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# autocorrelation-weighted R^2 over 126d (persistent AND straight)
def f11tp_f11_trend_persistence_acfr2_126d_base_v144_signal(closeadj):
    result = _f11_autocorr(closeadj, 126) * _f11_r2(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio-tilted slope: 63d slope * (VR10-1) over 252d
def f11tp_f11_trend_persistence_vrslope_63d_base_v145_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    v1 = _std(r, 252) ** 2
    vk = _std(r.rolling(10, min_periods=5).sum(), 252) ** 2 / 10.0
    vr = _safe_div(vk, v1)
    result = _f11_slope(closeadj, 63) * (vr - 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon slope blend (21/63/126/252 average per-day slope)
def f11tp_f11_trend_persistence_slblend_multi_base_v146_signal(closeadj):
    result = (_f11_slope(closeadj, 21) + _f11_slope(closeadj, 63)
              + _f11_slope(closeadj, 126) + _f11_slope(closeadj, 252)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon R^2 blend (straightness consensus 42/84/189)
def f11tp_f11_trend_persistence_r2blend_multi_base_v147_signal(closeadj):
    result = (_f11_r2(closeadj, 42) + _f11_r2(closeadj, 84)
              + _f11_r2(closeadj, 189)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon DI blend (directional consensus 21/63/126)
def f11tp_f11_trend_persistence_diblend_multi_base_v148_signal(closeadj):
    result = (_f11_di(closeadj, 21) + _f11_di(closeadj, 63)
              + _f11_di(closeadj, 126)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# composite trend persistence score: signed-straightness * DI over 126d
def f11tp_f11_trend_persistence_compscore_126d_base_v149_signal(closeadj):
    sr2 = _f11_r2(closeadj, 126) * np.sign(_f11_slope(closeadj, 126))
    result = sr2 * _f11_di(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# composite: t-stat scaled by R^2 over 252d (significance * straightness)
def f11tp_f11_trend_persistence_compsig_252d_base_v150_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    tstat = _safe_div(_f11_slope(closeadj, 252), _std(lr, 252))
    result = tstat * _f11_r2(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f11tp_f11_trend_persistence_slope_10d_base_v076_signal,
    f11tp_f11_trend_persistence_slope_315d_base_v077_signal,
    f11tp_f11_trend_persistence_slope_378d_base_v078_signal,
    f11tp_f11_trend_persistence_slopeann_21d_base_v079_signal,
    f11tp_f11_trend_persistence_slopeann_252d_base_v080_signal,
    f11tp_f11_trend_persistence_r2_315d_base_v081_signal,
    f11tp_f11_trend_persistence_r2_10d_base_v082_signal,
    f11tp_f11_trend_persistence_sr2_21d_base_v083_signal,
    f11tp_f11_trend_persistence_sr2_504d_base_v084_signal,
    f11tp_f11_trend_persistence_quality_42d_base_v085_signal,
    f11tp_f11_trend_persistence_quality_189d_base_v086_signal,
    f11tp_f11_trend_persistence_qualityann_84d_base_v087_signal,
    f11tp_f11_trend_persistence_di_10d_base_v088_signal,
    f11tp_f11_trend_persistence_di_84d_base_v089_signal,
    f11tp_f11_trend_persistence_di_189d_base_v090_signal,
    f11tp_f11_trend_persistence_adx_42d_base_v091_signal,
    f11tp_f11_trend_persistence_adx_252d_base_v092_signal,
    f11tp_f11_trend_persistence_adxsm_63d_base_v093_signal,
    f11tp_f11_trend_persistence_diratio_21d_base_v094_signal,
    f11tp_f11_trend_persistence_diratio_252d_base_v095_signal,
    f11tp_f11_trend_persistence_acf1_84d_base_v096_signal,
    f11tp_f11_trend_persistence_acf1_189d_base_v097_signal,
    f11tp_f11_trend_persistence_acf1_504d_base_v098_signal,
    f11tp_f11_trend_persistence_acfspread_21_126_base_v099_signal,
    f11tp_f11_trend_persistence_vr5_252d_base_v100_signal,
    f11tp_f11_trend_persistence_vr10_126d_base_v101_signal,
    f11tp_f11_trend_persistence_vr21_504d_base_v102_signal,
    f11tp_f11_trend_persistence_lvr10_252d_base_v103_signal,
    f11tp_f11_trend_persistence_eff_84d_base_v104_signal,
    f11tp_f11_trend_persistence_eff_189d_base_v105_signal,
    f11tp_f11_trend_persistence_eff_504d_base_v106_signal,
    f11tp_f11_trend_persistence_effmag_63d_base_v107_signal,
    f11tp_f11_trend_persistence_effmag_126d_base_v108_signal,
    f11tp_f11_trend_persistence_disp_42d_base_v109_signal,
    f11tp_f11_trend_persistence_disp_504d_base_v110_signal,
    f11tp_f11_trend_persistence_ext_126d_base_v111_signal,
    f11tp_f11_trend_persistence_streak_42d_base_v112_signal,
    f11tp_f11_trend_persistence_streak_252d_base_v113_signal,
    f11tp_f11_trend_persistence_runenergy_63d_base_v114_signal,
    f11tp_f11_trend_persistence_zslope_252d_base_v115_signal,
    f11tp_f11_trend_persistence_zslope_42d_base_v116_signal,
    f11tp_f11_trend_persistence_zr2_126d_base_v117_signal,
    f11tp_f11_trend_persistence_zdi_63d_base_v118_signal,
    f11tp_f11_trend_persistence_tstat_21d_base_v119_signal,
    f11tp_f11_trend_persistence_tstat_42d_base_v120_signal,
    f11tp_f11_trend_persistence_tstat_504d_base_v121_signal,
    f11tp_f11_trend_persistence_slacc_42_126_base_v122_signal,
    f11tp_f11_trend_persistence_slacc_21_252_base_v123_signal,
    f11tp_f11_trend_persistence_r2spread_21_126_base_v124_signal,
    f11tp_f11_trend_persistence_dispread_63_252_base_v125_signal,
    f11tp_f11_trend_persistence_slopesm_126d_base_v126_signal,
    f11tp_f11_trend_persistence_slopesm_42d_base_v127_signal,
    f11tp_f11_trend_persistence_effslope_252d_base_v128_signal,
    f11tp_f11_trend_persistence_effslope_21d_base_v129_signal,
    f11tp_f11_trend_persistence_acfslope_126d_base_v130_signal,
    f11tp_f11_trend_persistence_dir2_126d_base_v131_signal,
    f11tp_f11_trend_persistence_dir2_252d_base_v132_signal,
    f11tp_f11_trend_persistence_r2eff_63d_base_v133_signal,
    f11tp_f11_trend_persistence_r2eff_126d_base_v134_signal,
    f11tp_f11_trend_persistence_qualsm_63d_base_v135_signal,
    f11tp_f11_trend_persistence_slsurp_21d_base_v136_signal,
    f11tp_f11_trend_persistence_slsurp_63d_base_v137_signal,
    f11tp_f11_trend_persistence_r2surp_63d_base_v138_signal,
    f11tp_f11_trend_persistence_slrank_63d_base_v139_signal,
    f11tp_f11_trend_persistence_r2rank_126d_base_v140_signal,
    f11tp_f11_trend_persistence_ewmslope_63d_base_v141_signal,
    f11tp_f11_trend_persistence_ewmslope_126d_base_v142_signal,
    f11tp_f11_trend_persistence_dieff_63d_base_v143_signal,
    f11tp_f11_trend_persistence_acfr2_126d_base_v144_signal,
    f11tp_f11_trend_persistence_vrslope_63d_base_v145_signal,
    f11tp_f11_trend_persistence_slblend_multi_base_v146_signal,
    f11tp_f11_trend_persistence_r2blend_multi_base_v147_signal,
    f11tp_f11_trend_persistence_diblend_multi_base_v148_signal,
    f11tp_f11_trend_persistence_compscore_126d_base_v149_signal,
    f11tp_f11_trend_persistence_compsig_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_TREND_PERSISTENCE_REGISTRY_076_150 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f11_slope", "_f11_r2", "_f11_di", "_f11_autocorr")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f11_trend_persistence_base_076_150_claude: {n_features} features pass")
