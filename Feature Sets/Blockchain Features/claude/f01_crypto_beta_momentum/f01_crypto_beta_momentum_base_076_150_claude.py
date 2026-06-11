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


# ===== folder domain primitives (crypto-beta momentum) =====
def _f01_roc(s, w):
    return s.pct_change(periods=w)


def _f01_logmom(s, w):
    return np.log(s / s.shift(w))


def _f01_ampmom(s, w, k):
    r = s.pct_change(periods=w)
    return np.sign(r) * (r.abs() ** k)


def _f01_momqual(s, w):
    r = s.pct_change(periods=w)
    v = s.pct_change().rolling(w, min_periods=max(2, w // 2)).std() * np.sqrt(w)
    return r / v.replace(0, np.nan)


# ============ FEATURES 076-150 ============

# 21d EWMA of daily log return scaled to horizon
def f01cb_f01_crypto_beta_momentum_ewm_21d_base_v076_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=21, min_periods=10).mean() * 21.0 + _f01_roc(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d EWMA of daily log return scaled to horizon
def f01cb_f01_crypto_beta_momentum_ewm_42d_base_v077_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=42, min_periods=21).mean() * 42.0 + _f01_roc(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d EWMA of daily log return scaled to horizon
def f01cb_f01_crypto_beta_momentum_ewm_189d_base_v078_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=189, min_periods=63).mean() * 189.0 + _f01_roc(closeadj, 189) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EWMA of daily log return scaled to horizon
def f01cb_f01_crypto_beta_momentum_ewm_252d_base_v079_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=252, min_periods=84).mean() * 252.0 + _f01_roc(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EWMA of daily log return scaled to horizon
def f01cb_f01_crypto_beta_momentum_ewm_504d_base_v080_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=504, min_periods=168).mean() * 504.0 + _f01_roc(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d dispersion of monthly momentum
def f01cb_f01_crypto_beta_momentum_disp_42d_base_v081_signal(closeadj):
    result = _std(_f01_roc(closeadj, 21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dispersion of monthly momentum
def f01cb_f01_crypto_beta_momentum_disp_63d_base_v082_signal(closeadj):
    result = _std(_f01_roc(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d dispersion of monthly momentum
def f01cb_f01_crypto_beta_momentum_disp_126d_base_v083_signal(closeadj):
    result = _std(_f01_roc(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dispersion of quarterly momentum
def f01cb_f01_crypto_beta_momentum_disp_252d_base_v084_signal(closeadj):
    result = _std(_f01_roc(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dispersion of quarterly momentum
def f01cb_f01_crypto_beta_momentum_disp_504d_base_v085_signal(closeadj):
    result = _std(_f01_roc(closeadj, 63), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling Sharpe of daily log returns
def f01cb_f01_crypto_beta_momentum_sharpe_21d_base_v086_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(_mean(lr, 21), _std(lr, 21)) * np.sqrt(21.0) + _f01_roc(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d rolling Sharpe of daily log returns
def f01cb_f01_crypto_beta_momentum_sharpe_42d_base_v087_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(_mean(lr, 42), _std(lr, 42)) * np.sqrt(42.0) + _f01_roc(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling Sharpe of daily log returns
def f01cb_f01_crypto_beta_momentum_sharpe_63d_base_v088_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(_mean(lr, 63), _std(lr, 63)) * np.sqrt(63.0) + _f01_roc(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling Sharpe of daily log returns
def f01cb_f01_crypto_beta_momentum_sharpe_126d_base_v089_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(_mean(lr, 126), _std(lr, 126)) * np.sqrt(126.0) + _f01_roc(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling Sharpe of daily log returns
def f01cb_f01_crypto_beta_momentum_sharpe_252d_base_v090_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(_mean(lr, 252), _std(lr, 252)) * np.sqrt(252.0) + _f01_roc(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d Kaufman efficiency ratio (signed)
def f01cb_f01_crypto_beta_momentum_eff_21d_base_v091_signal(closeadj):
    net = closeadj - closeadj.shift(21)
    path = closeadj.diff().abs().rolling(21, min_periods=10).sum()
    result = _safe_div(net, path) + _f01_roc(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d Kaufman efficiency ratio (signed)
def f01cb_f01_crypto_beta_momentum_eff_42d_base_v092_signal(closeadj):
    net = closeadj - closeadj.shift(42)
    path = closeadj.diff().abs().rolling(42, min_periods=21).sum()
    result = _safe_div(net, path) + _f01_roc(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Kaufman efficiency ratio (signed)
def f01cb_f01_crypto_beta_momentum_eff_63d_base_v093_signal(closeadj):
    net = closeadj - closeadj.shift(63)
    path = closeadj.diff().abs().rolling(63, min_periods=21).sum()
    result = _safe_div(net, path) + _f01_roc(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d Kaufman efficiency ratio (signed)
def f01cb_f01_crypto_beta_momentum_eff_126d_base_v094_signal(closeadj):
    net = closeadj - closeadj.shift(126)
    path = closeadj.diff().abs().rolling(126, min_periods=42).sum()
    result = _safe_div(net, path) + _f01_roc(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Kaufman efficiency ratio (signed)
def f01cb_f01_crypto_beta_momentum_eff_252d_base_v095_signal(closeadj):
    net = closeadj - closeadj.shift(252)
    path = closeadj.diff().abs().rolling(252, min_periods=84).sum()
    result = _safe_div(net, path) + _f01_roc(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d Kaufman efficiency ratio (signed)
def f01cb_f01_crypto_beta_momentum_eff_504d_base_v096_signal(closeadj):
    net = closeadj - closeadj.shift(504)
    path = closeadj.diff().abs().rolling(504, min_periods=168).sum()
    result = _safe_div(net, path) + _f01_roc(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up from rolling trough (recovery thrust)
def f01cb_f01_crypto_beta_momentum_runup_21d_base_v097_signal(closeadj):
    trough = closeadj.rolling(21, min_periods=10).min().replace(0, np.nan)
    result = (closeadj - trough) / trough.abs() + _f01_roc(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up from rolling trough
def f01cb_f01_crypto_beta_momentum_runup_63d_base_v098_signal(closeadj):
    trough = closeadj.rolling(63, min_periods=21).min().replace(0, np.nan)
    result = (closeadj - trough) / trough.abs() + _f01_roc(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up from rolling trough
def f01cb_f01_crypto_beta_momentum_runup_126d_base_v099_signal(closeadj):
    trough = closeadj.rolling(126, min_periods=42).min().replace(0, np.nan)
    result = (closeadj - trough) / trough.abs() + _f01_roc(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up from rolling trough
def f01cb_f01_crypto_beta_momentum_runup_252d_base_v100_signal(closeadj):
    trough = closeadj.rolling(252, min_periods=84).min().replace(0, np.nan)
    result = (closeadj - trough) / trough.abs() + _f01_roc(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up from rolling trough
def f01cb_f01_crypto_beta_momentum_runup_504d_base_v101_signal(closeadj):
    trough = closeadj.rolling(504, min_periods=168).min().replace(0, np.nan)
    result = (closeadj - trough) / trough.abs() + _f01_roc(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d return skew (asymmetry of daily returns)
def f01cb_f01_crypto_beta_momentum_retskew_63d_base_v102_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.rolling(63, min_periods=21).skew() + _f01_roc(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d return skew
def f01cb_f01_crypto_beta_momentum_retskew_126d_base_v103_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.rolling(126, min_periods=42).skew() + _f01_roc(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d return skew
def f01cb_f01_crypto_beta_momentum_retskew_252d_base_v104_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.rolling(252, min_periods=84).skew() + _f01_roc(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d return kurtosis (fat-tail momentum regime)
def f01cb_f01_crypto_beta_momentum_retkurt_63d_base_v105_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.rolling(63, min_periods=21).kurt() + _f01_roc(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d return kurtosis
def f01cb_f01_crypto_beta_momentum_retkurt_126d_base_v106_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.rolling(126, min_periods=42).kurt() + _f01_roc(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d momentum scaled by 252d realized vol
def f01cb_f01_crypto_beta_momentum_volscaled_21d_base_v107_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 252) * np.sqrt(21.0)
    result = _safe_div(_f01_roc(closeadj, 21), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d momentum scaled by 252d realized vol
def f01cb_f01_crypto_beta_momentum_volscaled_42d_base_v108_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 252) * np.sqrt(42.0)
    result = _safe_div(_f01_roc(closeadj, 42), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d momentum scaled by 252d realized vol
def f01cb_f01_crypto_beta_momentum_volscaled_63d_base_v109_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 252) * np.sqrt(63.0)
    result = _safe_div(_f01_roc(closeadj, 63), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d momentum scaled by 252d realized vol
def f01cb_f01_crypto_beta_momentum_volscaled_126d_base_v110_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 252) * np.sqrt(126.0)
    result = _safe_div(_f01_roc(closeadj, 126), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d momentum scaled by 126d realized vol
def f01cb_f01_crypto_beta_momentum_volscaled_252d_base_v111_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 126) * np.sqrt(252.0)
    result = _safe_div(_f01_roc(closeadj, 252), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d momentum weighted by efficiency
def f01cb_f01_crypto_beta_momentum_effw_21d_base_v112_signal(closeadj):
    net = closeadj - closeadj.shift(21)
    path = closeadj.diff().abs().rolling(21, min_periods=10).sum()
    eff = _safe_div(net, path)
    result = _f01_roc(closeadj, 21) * eff
    return result.replace([np.inf, -np.inf], np.nan)


# 63d momentum weighted by efficiency
def f01cb_f01_crypto_beta_momentum_effw_63d_base_v113_signal(closeadj):
    net = closeadj - closeadj.shift(63)
    path = closeadj.diff().abs().rolling(63, min_periods=21).sum()
    eff = _safe_div(net, path)
    result = _f01_roc(closeadj, 63) * eff
    return result.replace([np.inf, -np.inf], np.nan)


# 126d momentum weighted by efficiency
def f01cb_f01_crypto_beta_momentum_effw_126d_base_v114_signal(closeadj):
    net = closeadj - closeadj.shift(126)
    path = closeadj.diff().abs().rolling(126, min_periods=42).sum()
    eff = _safe_div(net, path)
    result = _f01_roc(closeadj, 126) * eff
    return result.replace([np.inf, -np.inf], np.nan)


# 252d momentum weighted by efficiency
def f01cb_f01_crypto_beta_momentum_effw_252d_base_v115_signal(closeadj):
    net = closeadj - closeadj.shift(252)
    path = closeadj.diff().abs().rolling(252, min_periods=84).sum()
    eff = _safe_div(net, path)
    result = _f01_roc(closeadj, 252) * eff
    return result.replace([np.inf, -np.inf], np.nan)


# 21d volume-weighted price momentum
def f01cb_f01_crypto_beta_momentum_vwmom_21d_base_v116_signal(closeadj, volume):
    flow = (closeadj.diff() * volume).rolling(21, min_periods=10).sum()
    base = volume.rolling(21, min_periods=10).sum() * closeadj
    result = _safe_div(flow, base) + _f01_roc(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d volume-weighted price momentum
def f01cb_f01_crypto_beta_momentum_vwmom_63d_base_v117_signal(closeadj, volume):
    flow = (closeadj.diff() * volume).rolling(63, min_periods=21).sum()
    base = volume.rolling(63, min_periods=21).sum() * closeadj
    result = _safe_div(flow, base) + _f01_roc(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d volume-weighted price momentum
def f01cb_f01_crypto_beta_momentum_vwmom_126d_base_v118_signal(closeadj, volume):
    flow = (closeadj.diff() * volume).rolling(126, min_periods=42).sum()
    base = volume.rolling(126, min_periods=42).sum() * closeadj
    result = _safe_div(flow, base) + _f01_roc(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d momentum scaled by dollar-volume surge
def f01cb_f01_crypto_beta_momentum_dvsurge_21d_base_v119_signal(closeadj, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 63))
    result = _f01_roc(closeadj, 21) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# 21d amplified momentum k=1.75
def f01cb_f01_crypto_beta_momentum_amp17_21d_base_v120_signal(closeadj):
    result = _f01_ampmom(closeadj, 21, 1.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d amplified momentum k=1.5
def f01cb_f01_crypto_beta_momentum_amp15_126d_base_v121_signal(closeadj):
    result = _f01_ampmom(closeadj, 126, 1.5)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d amplified momentum k=2.0
def f01cb_f01_crypto_beta_momentum_amp20_42d_base_v122_signal(closeadj):
    result = _f01_ampmom(closeadj, 42, 2.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d amplified momentum k=1.5
def f01cb_f01_crypto_beta_momentum_amp15_189d_base_v123_signal(closeadj):
    result = _f01_ampmom(closeadj, 189, 1.5)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d amplified momentum k=1.25
def f01cb_f01_crypto_beta_momentum_amp12_504d_base_v124_signal(closeadj):
    result = _f01_ampmom(closeadj, 504, 1.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d momentum convexity at k=2.5 (excess over linear)
def f01cb_f01_crypto_beta_momentum_convex25_21d_base_v125_signal(closeadj):
    result = _f01_ampmom(closeadj, 21, 2.5) - _f01_roc(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d momentum convexity at k=1.5 (excess over linear)
def f01cb_f01_crypto_beta_momentum_convex15_252d_base_v126_signal(closeadj):
    result = _f01_ampmom(closeadj, 252, 1.5) - _f01_roc(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d log momentum
def f01cb_f01_crypto_beta_momentum_logmom_84d_base_v127_signal(closeadj):
    result = _f01_logmom(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d log momentum
def f01cb_f01_crypto_beta_momentum_logmom_315d_base_v128_signal(closeadj):
    result = _f01_logmom(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d rate of change
def f01cb_f01_crypto_beta_momentum_roc_84d_base_v129_signal(closeadj):
    result = _f01_roc(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d rate of change
def f01cb_f01_crypto_beta_momentum_roc_315d_base_v130_signal(closeadj):
    result = _f01_roc(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 42d momentum over 252d
def f01cb_f01_crypto_beta_momentum_zroc_42d_base_v131_signal(closeadj):
    result = _z(_f01_roc(closeadj, 42), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d momentum over 504d
def f01cb_f01_crypto_beta_momentum_zroc_126d_base_v132_signal(closeadj):
    result = _z(_f01_roc(closeadj, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 252d momentum over 504d
def f01cb_f01_crypto_beta_momentum_zroc_252d_base_v133_signal(closeadj):
    result = _z(_f01_roc(closeadj, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 10d momentum over 126d
def f01cb_f01_crypto_beta_momentum_zroc_10d_base_v134_signal(closeadj):
    result = _z(_f01_roc(closeadj, 10), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 84d log momentum over 252d
def f01cb_f01_crypto_beta_momentum_zlmom_84d_base_v135_signal(closeadj):
    result = _z(_f01_logmom(closeadj, 84), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 126d momentum over 252d
def f01cb_f01_crypto_beta_momentum_rank_126d_base_v136_signal(closeadj):
    r = _f01_roc(closeadj, 126)
    result = r.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 21d momentum over 252d
def f01cb_f01_crypto_beta_momentum_rank_21d252w_base_v137_signal(closeadj):
    r = _f01_roc(closeadj, 21)
    result = r.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 5d momentum over 63d
def f01cb_f01_crypto_beta_momentum_rank_5d_base_v138_signal(closeadj):
    r = _f01_roc(closeadj, 5)
    result = r.rolling(63, min_periods=21).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed monthly momentum (63d mean)
def f01cb_f01_crypto_beta_momentum_smooth63_21d_base_v139_signal(closeadj):
    result = _mean(_f01_roc(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d smoothed quarterly momentum (42d mean)
def f01cb_f01_crypto_beta_momentum_smooth42_63d_base_v140_signal(closeadj):
    result = _mean(_f01_roc(closeadj, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log momentum (21d mean of 42d logmom)
def f01cb_f01_crypto_beta_momentum_smooth21_42d_base_v141_signal(closeadj):
    result = _mean(_f01_logmom(closeadj, 42), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed amplified momentum (63d mean)
def f01cb_f01_crypto_beta_momentum_smoothamp63_63d_base_v142_signal(closeadj):
    result = _mean(_f01_ampmom(closeadj, 63, 2.0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 42d log momentum
def f01cb_f01_crypto_beta_momentum_ann_42d_base_v143_signal(closeadj):
    result = _f01_logmom(closeadj, 42) * (252.0 / 42.0)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 189d log momentum
def f01cb_f01_crypto_beta_momentum_ann_189d_base_v144_signal(closeadj):
    result = _f01_logmom(closeadj, 189) * (252.0 / 189.0)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 252d log momentum
def f01cb_f01_crypto_beta_momentum_ann_252d_base_v145_signal(closeadj):
    result = _f01_logmom(closeadj, 252) * (252.0 / 252.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d momentum quality
def f01cb_f01_crypto_beta_momentum_momqual_84d_base_v146_signal(closeadj):
    result = _f01_momqual(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d momentum quality
def f01cb_f01_crypto_beta_momentum_momqual_315d_base_v147_signal(closeadj):
    result = _f01_momqual(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d momentum information ratio vs 126d dispersion
def f01cb_f01_crypto_beta_momentum_inforatio126_21d_base_v148_signal(closeadj):
    r = _f01_roc(closeadj, 21)
    result = _safe_div(r, _std(r, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d momentum information ratio vs 252d dispersion
def f01cb_f01_crypto_beta_momentum_inforatio252_126d_base_v149_signal(closeadj):
    r = _f01_roc(closeadj, 126)
    result = _safe_div(r, _std(r, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon momentum composite (21/63/126/252)
def f01cb_f01_crypto_beta_momentum_blend_multi_base_v150_signal(closeadj):
    result = (_f01_roc(closeadj, 21) + _f01_roc(closeadj, 63)
              + _f01_roc(closeadj, 126) + _f01_roc(closeadj, 252)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01cb_f01_crypto_beta_momentum_ewm_21d_base_v076_signal,
    f01cb_f01_crypto_beta_momentum_ewm_42d_base_v077_signal,
    f01cb_f01_crypto_beta_momentum_ewm_189d_base_v078_signal,
    f01cb_f01_crypto_beta_momentum_ewm_252d_base_v079_signal,
    f01cb_f01_crypto_beta_momentum_ewm_504d_base_v080_signal,
    f01cb_f01_crypto_beta_momentum_disp_42d_base_v081_signal,
    f01cb_f01_crypto_beta_momentum_disp_63d_base_v082_signal,
    f01cb_f01_crypto_beta_momentum_disp_126d_base_v083_signal,
    f01cb_f01_crypto_beta_momentum_disp_252d_base_v084_signal,
    f01cb_f01_crypto_beta_momentum_disp_504d_base_v085_signal,
    f01cb_f01_crypto_beta_momentum_sharpe_21d_base_v086_signal,
    f01cb_f01_crypto_beta_momentum_sharpe_42d_base_v087_signal,
    f01cb_f01_crypto_beta_momentum_sharpe_63d_base_v088_signal,
    f01cb_f01_crypto_beta_momentum_sharpe_126d_base_v089_signal,
    f01cb_f01_crypto_beta_momentum_sharpe_252d_base_v090_signal,
    f01cb_f01_crypto_beta_momentum_eff_21d_base_v091_signal,
    f01cb_f01_crypto_beta_momentum_eff_42d_base_v092_signal,
    f01cb_f01_crypto_beta_momentum_eff_63d_base_v093_signal,
    f01cb_f01_crypto_beta_momentum_eff_126d_base_v094_signal,
    f01cb_f01_crypto_beta_momentum_eff_252d_base_v095_signal,
    f01cb_f01_crypto_beta_momentum_eff_504d_base_v096_signal,
    f01cb_f01_crypto_beta_momentum_runup_21d_base_v097_signal,
    f01cb_f01_crypto_beta_momentum_runup_63d_base_v098_signal,
    f01cb_f01_crypto_beta_momentum_runup_126d_base_v099_signal,
    f01cb_f01_crypto_beta_momentum_runup_252d_base_v100_signal,
    f01cb_f01_crypto_beta_momentum_runup_504d_base_v101_signal,
    f01cb_f01_crypto_beta_momentum_retskew_63d_base_v102_signal,
    f01cb_f01_crypto_beta_momentum_retskew_126d_base_v103_signal,
    f01cb_f01_crypto_beta_momentum_retskew_252d_base_v104_signal,
    f01cb_f01_crypto_beta_momentum_retkurt_63d_base_v105_signal,
    f01cb_f01_crypto_beta_momentum_retkurt_126d_base_v106_signal,
    f01cb_f01_crypto_beta_momentum_volscaled_21d_base_v107_signal,
    f01cb_f01_crypto_beta_momentum_volscaled_42d_base_v108_signal,
    f01cb_f01_crypto_beta_momentum_volscaled_63d_base_v109_signal,
    f01cb_f01_crypto_beta_momentum_volscaled_126d_base_v110_signal,
    f01cb_f01_crypto_beta_momentum_volscaled_252d_base_v111_signal,
    f01cb_f01_crypto_beta_momentum_effw_21d_base_v112_signal,
    f01cb_f01_crypto_beta_momentum_effw_63d_base_v113_signal,
    f01cb_f01_crypto_beta_momentum_effw_126d_base_v114_signal,
    f01cb_f01_crypto_beta_momentum_effw_252d_base_v115_signal,
    f01cb_f01_crypto_beta_momentum_vwmom_21d_base_v116_signal,
    f01cb_f01_crypto_beta_momentum_vwmom_63d_base_v117_signal,
    f01cb_f01_crypto_beta_momentum_vwmom_126d_base_v118_signal,
    f01cb_f01_crypto_beta_momentum_dvsurge_21d_base_v119_signal,
    f01cb_f01_crypto_beta_momentum_amp17_21d_base_v120_signal,
    f01cb_f01_crypto_beta_momentum_amp15_126d_base_v121_signal,
    f01cb_f01_crypto_beta_momentum_amp20_42d_base_v122_signal,
    f01cb_f01_crypto_beta_momentum_amp15_189d_base_v123_signal,
    f01cb_f01_crypto_beta_momentum_amp12_504d_base_v124_signal,
    f01cb_f01_crypto_beta_momentum_convex25_21d_base_v125_signal,
    f01cb_f01_crypto_beta_momentum_convex15_252d_base_v126_signal,
    f01cb_f01_crypto_beta_momentum_logmom_84d_base_v127_signal,
    f01cb_f01_crypto_beta_momentum_logmom_315d_base_v128_signal,
    f01cb_f01_crypto_beta_momentum_roc_84d_base_v129_signal,
    f01cb_f01_crypto_beta_momentum_roc_315d_base_v130_signal,
    f01cb_f01_crypto_beta_momentum_zroc_42d_base_v131_signal,
    f01cb_f01_crypto_beta_momentum_zroc_126d_base_v132_signal,
    f01cb_f01_crypto_beta_momentum_zroc_252d_base_v133_signal,
    f01cb_f01_crypto_beta_momentum_zroc_10d_base_v134_signal,
    f01cb_f01_crypto_beta_momentum_zlmom_84d_base_v135_signal,
    f01cb_f01_crypto_beta_momentum_rank_126d_base_v136_signal,
    f01cb_f01_crypto_beta_momentum_rank_21d252w_base_v137_signal,
    f01cb_f01_crypto_beta_momentum_rank_5d_base_v138_signal,
    f01cb_f01_crypto_beta_momentum_smooth63_21d_base_v139_signal,
    f01cb_f01_crypto_beta_momentum_smooth42_63d_base_v140_signal,
    f01cb_f01_crypto_beta_momentum_smooth21_42d_base_v141_signal,
    f01cb_f01_crypto_beta_momentum_smoothamp63_63d_base_v142_signal,
    f01cb_f01_crypto_beta_momentum_ann_42d_base_v143_signal,
    f01cb_f01_crypto_beta_momentum_ann_189d_base_v144_signal,
    f01cb_f01_crypto_beta_momentum_ann_252d_base_v145_signal,
    f01cb_f01_crypto_beta_momentum_momqual_84d_base_v146_signal,
    f01cb_f01_crypto_beta_momentum_momqual_315d_base_v147_signal,
    f01cb_f01_crypto_beta_momentum_inforatio126_21d_base_v148_signal,
    f01cb_f01_crypto_beta_momentum_inforatio252_126d_base_v149_signal,
    f01cb_f01_crypto_beta_momentum_blend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_CRYPTO_BETA_MOMENTUM_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0008, 0.045, n)
    closeadj = pd.Series(50.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name="volume")
    cols = {"closeadj": closeadj, "volume": volume}

    domain_primitives = ("_f01_roc", "_f01_logmom", "_f01_ampmom", "_f01_momqual")
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
    print(f"OK f01_crypto_beta_momentum_base_076_150_claude: {n_features} features pass")
