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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f06_accumulation_obv(close, volume, w):
    r = close.pct_change()
    sign = np.sign(r).fillna(0.0)
    obv = (sign * volume).rolling(w, min_periods=max(1, w // 2)).sum()
    return obv / volume.rolling(w, min_periods=max(1, w // 2)).sum().replace(0, np.nan)


def _f06_money_flow(close, high, low, volume, w):
    tp = (high + low + close) / 3.0
    mf = tp * volume
    pos = mf * (close > close.shift(1)).astype(float)
    neg = mf * (close < close.shift(1)).astype(float)
    pos_s = pos.rolling(w, min_periods=max(1, w // 2)).sum()
    neg_s = neg.rolling(w, min_periods=max(1, w // 2)).sum()
    return (pos_s - neg_s) / (pos_s + neg_s).replace(0, np.nan)


def _f06_accumulation_ad(close, high, low, volume, w):
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    ad = (clv * volume).rolling(w, min_periods=max(1, w // 2)).sum()
    return ad / volume.rolling(w, min_periods=max(1, w // 2)).sum().replace(0, np.nan)


# 21d obv × return volatility
def f06va_f06_volume_accumulation_obvxrv_21d_base_v076_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 21)
    result = _f06_accumulation_obv(closeadj, volume, 21) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv × rv
def f06va_f06_volume_accumulation_obvxrv_63d_base_v077_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63)
    result = _f06_accumulation_obv(closeadj, volume, 63) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d obv × rv
def f06va_f06_volume_accumulation_obvxrv_252d_base_v078_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63)
    result = _f06_accumulation_obv(closeadj, volume, 252) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv divided by return volatility
def f06va_f06_volume_accumulation_obvdivrv_21d_base_v079_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    result = (_f06_accumulation_obv(closeadj, volume, 21) / rv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv / rv
def f06va_f06_volume_accumulation_obvdivrv_63d_base_v080_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    result = (_f06_accumulation_obv(closeadj, volume, 63) / rv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d obv / rv
def f06va_f06_volume_accumulation_obvdivrv_252d_base_v081_signal(closeadj, volume):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    result = (_f06_accumulation_obv(closeadj, volume, 252) / rv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MFI × rv
def f06va_f06_volume_accumulation_mfixrv_21d_base_v082_signal(closeadj, volume, high, low):
    rv = _std(closeadj.pct_change(), 21)
    result = _f06_money_flow(closeadj, high, low, volume, 21) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d MFI × rv
def f06va_f06_volume_accumulation_mfixrv_63d_base_v083_signal(closeadj, volume, high, low):
    rv = _std(closeadj.pct_change(), 63)
    result = _f06_money_flow(closeadj, high, low, volume, 63) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MFI × rv
def f06va_f06_volume_accumulation_mfixrv_252d_base_v084_signal(closeadj, volume, high, low):
    rv = _std(closeadj.pct_change(), 63)
    result = _f06_money_flow(closeadj, high, low, volume, 252) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv × log price
def f06va_f06_volume_accumulation_obvxlog_21d_base_v085_signal(closeadj, volume):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    result = _f06_accumulation_obv(closeadj, volume, 21) * lg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv × log
def f06va_f06_volume_accumulation_obvxlog_63d_base_v086_signal(closeadj, volume):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    result = _f06_accumulation_obv(closeadj, volume, 63) * lg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d obv × log
def f06va_f06_volume_accumulation_obvxlog_252d_base_v087_signal(closeadj, volume):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    result = _f06_accumulation_obv(closeadj, volume, 252) * lg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MFI × log price
def f06va_f06_volume_accumulation_mfixlog_21d_base_v088_signal(closeadj, volume, high, low):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    result = _f06_money_flow(closeadj, high, low, volume, 21) * lg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d MFI × log
def f06va_f06_volume_accumulation_mfixlog_63d_base_v089_signal(closeadj, volume, high, low):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    result = _f06_money_flow(closeadj, high, low, volume, 63) * lg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d A/D × log
def f06va_f06_volume_accumulation_adxlog_21d_base_v090_signal(closeadj, volume, high, low):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    result = _f06_accumulation_ad(closeadj, high, low, volume, 21) * lg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d A/D × log
def f06va_f06_volume_accumulation_adxlog_63d_base_v091_signal(closeadj, volume, high, low):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    result = _f06_accumulation_ad(closeadj, high, low, volume, 63) * lg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv × ATR-style range
def f06va_f06_volume_accumulation_obvxatr_21d_base_v092_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f06_accumulation_obv(closeadj, volume, 21) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv × ATR
def f06va_f06_volume_accumulation_obvxatr_63d_base_v093_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f06_accumulation_obv(closeadj, volume, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 252d obv × ATR
def f06va_f06_volume_accumulation_obvxatr_252d_base_v094_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f06_accumulation_obv(closeadj, volume, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MFI × ATR
def f06va_f06_volume_accumulation_mfixatr_21d_base_v095_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f06_money_flow(closeadj, high, low, volume, 21) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 63d MFI × ATR
def f06va_f06_volume_accumulation_mfixatr_63d_base_v096_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f06_money_flow(closeadj, high, low, volume, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MFI × ATR
def f06va_f06_volume_accumulation_mfixatr_252d_base_v097_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f06_money_flow(closeadj, high, low, volume, 252) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 21d A/D × ATR
def f06va_f06_volume_accumulation_adxatr_21d_base_v098_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f06_accumulation_ad(closeadj, high, low, volume, 21) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 63d A/D × ATR
def f06va_f06_volume_accumulation_adxatr_63d_base_v099_signal(closeadj, volume, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f06_accumulation_ad(closeadj, high, low, volume, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv × MFI (compound bullish accumulation)
def f06va_f06_volume_accumulation_obvxmfi_21d_base_v100_signal(closeadj, volume, high, low):
    result = _f06_accumulation_obv(closeadj, volume, 21) * _f06_money_flow(closeadj, high, low, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv × MFI
def f06va_f06_volume_accumulation_obvxmfi_63d_base_v101_signal(closeadj, volume, high, low):
    result = _f06_accumulation_obv(closeadj, volume, 63) * _f06_money_flow(closeadj, high, low, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d obv × MFI
def f06va_f06_volume_accumulation_obvxmfi_252d_base_v102_signal(closeadj, volume, high, low):
    result = _f06_accumulation_obv(closeadj, volume, 252) * _f06_money_flow(closeadj, high, low, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv × A/D
def f06va_f06_volume_accumulation_obvxad_21d_base_v103_signal(closeadj, volume, high, low):
    result = _f06_accumulation_obv(closeadj, volume, 21) * _f06_accumulation_ad(closeadj, high, low, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv × A/D
def f06va_f06_volume_accumulation_obvxad_63d_base_v104_signal(closeadj, volume, high, low):
    result = _f06_accumulation_obv(closeadj, volume, 63) * _f06_accumulation_ad(closeadj, high, low, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d obv × A/D
def f06va_f06_volume_accumulation_obvxad_252d_base_v105_signal(closeadj, volume, high, low):
    result = _f06_accumulation_obv(closeadj, volume, 252) * _f06_accumulation_ad(closeadj, high, low, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MFI × A/D
def f06va_f06_volume_accumulation_mfixad_21d_base_v106_signal(closeadj, volume, high, low):
    result = _f06_money_flow(closeadj, high, low, volume, 21) * _f06_accumulation_ad(closeadj, high, low, volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d MFI × A/D
def f06va_f06_volume_accumulation_mfixad_63d_base_v107_signal(closeadj, volume, high, low):
    result = _f06_money_flow(closeadj, high, low, volume, 63) * _f06_accumulation_ad(closeadj, high, low, volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MFI × A/D
def f06va_f06_volume_accumulation_mfixad_252d_base_v108_signal(closeadj, volume, high, low):
    result = _f06_money_flow(closeadj, high, low, volume, 252) * _f06_accumulation_ad(closeadj, high, low, volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d A/D × dollar volume
def f06va_f06_volume_accumulation_adxdv_21d_base_v109_signal(closeadj, volume, high, low):
    dv = closeadj * volume
    result = _f06_accumulation_ad(closeadj, high, low, volume, 21) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d A/D × dollar volume
def f06va_f06_volume_accumulation_adxdv_63d_base_v110_signal(closeadj, volume, high, low):
    dv = closeadj * volume
    result = _f06_accumulation_ad(closeadj, high, low, volume, 63) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d A/D × dollar volume mean
def f06va_f06_volume_accumulation_adxdv_252d_base_v111_signal(closeadj, volume, high, low):
    dv = closeadj * volume
    result = _f06_accumulation_ad(closeadj, high, low, volume, 252) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MFI × return
def f06va_f06_volume_accumulation_mfixret_21d_base_v112_signal(closeadj, volume, high, low):
    r21 = closeadj.pct_change(21)
    result = _f06_money_flow(closeadj, high, low, volume, 21) * r21 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d MFI × return
def f06va_f06_volume_accumulation_mfixret_63d_base_v113_signal(closeadj, volume, high, low):
    r63 = closeadj.pct_change(63)
    result = _f06_money_flow(closeadj, high, low, volume, 63) * r63 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MFI × return
def f06va_f06_volume_accumulation_mfixret_252d_base_v114_signal(closeadj, volume, high, low):
    r252 = closeadj.pct_change(252)
    result = _f06_money_flow(closeadj, high, low, volume, 252) * r252 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d A/D × return
def f06va_f06_volume_accumulation_adxret_21d_base_v115_signal(closeadj, volume, high, low):
    r21 = closeadj.pct_change(21)
    result = _f06_accumulation_ad(closeadj, high, low, volume, 21) * r21 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d A/D × return
def f06va_f06_volume_accumulation_adxret_63d_base_v116_signal(closeadj, volume, high, low):
    r63 = closeadj.pct_change(63)
    result = _f06_accumulation_ad(closeadj, high, low, volume, 63) * r63 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d A/D × return
def f06va_f06_volume_accumulation_adxret_252d_base_v117_signal(closeadj, volume, high, low):
    r252 = closeadj.pct_change(252)
    result = _f06_accumulation_ad(closeadj, high, low, volume, 252) * r252 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv × skewness
def f06va_f06_volume_accumulation_obvxskew_63d_base_v118_signal(closeadj, volume):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    result = _f06_accumulation_obv(closeadj, volume, 21) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv × kurtosis
def f06va_f06_volume_accumulation_obvxkurt_252d_base_v119_signal(closeadj, volume):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    result = _f06_accumulation_obv(closeadj, volume, 63) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MFI × skewness
def f06va_f06_volume_accumulation_mfixskew_63d_base_v120_signal(closeadj, volume, high, low):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    result = _f06_money_flow(closeadj, high, low, volume, 21) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv minus rolling 252d mean of obv (anomaly)
def f06va_f06_volume_accumulation_obvanom_21d_base_v121_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 21)
    result = (o - _mean(o, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv anomaly
def f06va_f06_volume_accumulation_obvanom_63d_base_v122_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 63)
    result = (o - _mean(o, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d obv anomaly
def f06va_f06_volume_accumulation_obvanom_252d_base_v123_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 252)
    result = (o - _mean(o, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MFI anomaly
def f06va_f06_volume_accumulation_mfianom_21d_base_v124_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 21)
    result = (m - _mean(m, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d MFI anomaly
def f06va_f06_volume_accumulation_mfianom_63d_base_v125_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 63)
    result = (m - _mean(m, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d A/D anomaly
def f06va_f06_volume_accumulation_adanom_21d_base_v126_signal(closeadj, volume, high, low):
    a = _f06_accumulation_ad(closeadj, high, low, volume, 21)
    result = (a - _mean(a, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d A/D anomaly
def f06va_f06_volume_accumulation_adanom_63d_base_v127_signal(closeadj, volume, high, low):
    a = _f06_accumulation_ad(closeadj, high, low, volume, 63)
    result = (a - _mean(a, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv × abs return mean
def f06va_f06_volume_accumulation_obvxabsret_21d_base_v128_signal(closeadj, volume):
    ar = closeadj.pct_change().abs().rolling(21, min_periods=5).mean()
    result = _f06_accumulation_obv(closeadj, volume, 21) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv × abs return mean
def f06va_f06_volume_accumulation_obvxabsret_63d_base_v129_signal(closeadj, volume):
    ar = closeadj.pct_change().abs().rolling(63, min_periods=21).mean()
    result = _f06_accumulation_obv(closeadj, volume, 63) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MFI × abs ret mean
def f06va_f06_volume_accumulation_mfixabsret_21d_base_v130_signal(closeadj, volume, high, low):
    ar = closeadj.pct_change().abs().rolling(21, min_periods=5).mean()
    result = _f06_money_flow(closeadj, high, low, volume, 21) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite acc × dollar volume
def f06va_f06_volume_accumulation_acccompxdv_21d_base_v131_signal(closeadj, volume, high, low):
    dv = closeadj * volume
    comp = _f06_accumulation_obv(closeadj, volume, 21) + _f06_money_flow(closeadj, high, low, volume, 21) + _f06_accumulation_ad(closeadj, high, low, volume, 21)
    result = comp * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite acc × dollar volume
def f06va_f06_volume_accumulation_acccompxdv_252d_base_v132_signal(closeadj, volume, high, low):
    dv = closeadj * volume
    comp = _f06_accumulation_obv(closeadj, volume, 252) + _f06_money_flow(closeadj, high, low, volume, 252) + _f06_accumulation_ad(closeadj, high, low, volume, 252)
    result = comp * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv sum over 63d
def f06va_f06_volume_accumulation_obvsum_63d_base_v133_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 21)
    result = o.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv sum over 252d
def f06va_f06_volume_accumulation_obvsum_252d_base_v134_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 63)
    result = o.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MFI sum over 63d
def f06va_f06_volume_accumulation_mfisum_63d_base_v135_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 21)
    result = m.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d A/D sum over 63d
def f06va_f06_volume_accumulation_adsum_63d_base_v136_signal(closeadj, volume, high, low):
    a = _f06_accumulation_ad(closeadj, high, low, volume, 21)
    result = a.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv max over 63d
def f06va_f06_volume_accumulation_obvmax_63d_base_v137_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 21)
    result = o.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv max over 252d
def f06va_f06_volume_accumulation_obvmax_252d_base_v138_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 63)
    result = o.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv min over 63d
def f06va_f06_volume_accumulation_obvmin_63d_base_v139_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 21)
    result = (o.rolling(63, min_periods=21).min() + o * 0.001) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv min over 252d
def f06va_f06_volume_accumulation_obvmin_252d_base_v140_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 63)
    result = (o.rolling(252, min_periods=63).min() + o * 0.001) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv squared
def f06va_f06_volume_accumulation_obvsq_21d_base_v141_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 21)
    result = o * o.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv squared
def f06va_f06_volume_accumulation_obvsq_63d_base_v142_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 63)
    result = o * o.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d obv squared
def f06va_f06_volume_accumulation_obvsq_252d_base_v143_signal(closeadj, volume):
    o = _f06_accumulation_obv(closeadj, volume, 252)
    result = o * o.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MFI squared
def f06va_f06_volume_accumulation_mfisq_21d_base_v144_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 21)
    result = m * m.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d MFI squared
def f06va_f06_volume_accumulation_mfisq_63d_base_v145_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 63)
    result = m * m.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv × volume / volume mean
def f06va_f06_volume_accumulation_obvxvolratio_21d_base_v146_signal(closeadj, volume):
    vmean = _mean(volume, 21).replace(0, np.nan)
    result = _f06_accumulation_obv(closeadj, volume, 21) * (volume / vmean) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d obv × volume / volume mean
def f06va_f06_volume_accumulation_obvxvolratio_63d_base_v147_signal(closeadj, volume):
    vmean = _mean(volume, 63).replace(0, np.nan)
    result = _f06_accumulation_obv(closeadj, volume, 63) * (volume / vmean) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MFI × volume / volume mean
def f06va_f06_volume_accumulation_mfixvolratio_252d_base_v148_signal(closeadj, volume, high, low):
    vmean = _mean(volume, 252).replace(0, np.nan)
    result = _f06_money_flow(closeadj, high, low, volume, 252) * (volume / vmean) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d obv × hl-spread
def f06va_f06_volume_accumulation_obvxhlspread_21d_base_v149_signal(closeadj, volume, high, low):
    sp = (high - low) / closeadj.replace(0, np.nan)
    result = _f06_accumulation_obv(closeadj, volume, 21) * sp * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MFI EMA × volume zscore (smoothed flow with volume confirmation)
def f06va_f06_volume_accumulation_mfiemaxvolz_21d_base_v150_signal(closeadj, volume, high, low):
    m = _f06_money_flow(closeadj, high, low, volume, 21)
    e = m.ewm(span=21, adjust=False).mean()
    result = e * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06va_f06_volume_accumulation_obvxrv_21d_base_v076_signal,
    f06va_f06_volume_accumulation_obvxrv_63d_base_v077_signal,
    f06va_f06_volume_accumulation_obvxrv_252d_base_v078_signal,
    f06va_f06_volume_accumulation_obvdivrv_21d_base_v079_signal,
    f06va_f06_volume_accumulation_obvdivrv_63d_base_v080_signal,
    f06va_f06_volume_accumulation_obvdivrv_252d_base_v081_signal,
    f06va_f06_volume_accumulation_mfixrv_21d_base_v082_signal,
    f06va_f06_volume_accumulation_mfixrv_63d_base_v083_signal,
    f06va_f06_volume_accumulation_mfixrv_252d_base_v084_signal,
    f06va_f06_volume_accumulation_obvxlog_21d_base_v085_signal,
    f06va_f06_volume_accumulation_obvxlog_63d_base_v086_signal,
    f06va_f06_volume_accumulation_obvxlog_252d_base_v087_signal,
    f06va_f06_volume_accumulation_mfixlog_21d_base_v088_signal,
    f06va_f06_volume_accumulation_mfixlog_63d_base_v089_signal,
    f06va_f06_volume_accumulation_adxlog_21d_base_v090_signal,
    f06va_f06_volume_accumulation_adxlog_63d_base_v091_signal,
    f06va_f06_volume_accumulation_obvxatr_21d_base_v092_signal,
    f06va_f06_volume_accumulation_obvxatr_63d_base_v093_signal,
    f06va_f06_volume_accumulation_obvxatr_252d_base_v094_signal,
    f06va_f06_volume_accumulation_mfixatr_21d_base_v095_signal,
    f06va_f06_volume_accumulation_mfixatr_63d_base_v096_signal,
    f06va_f06_volume_accumulation_mfixatr_252d_base_v097_signal,
    f06va_f06_volume_accumulation_adxatr_21d_base_v098_signal,
    f06va_f06_volume_accumulation_adxatr_63d_base_v099_signal,
    f06va_f06_volume_accumulation_obvxmfi_21d_base_v100_signal,
    f06va_f06_volume_accumulation_obvxmfi_63d_base_v101_signal,
    f06va_f06_volume_accumulation_obvxmfi_252d_base_v102_signal,
    f06va_f06_volume_accumulation_obvxad_21d_base_v103_signal,
    f06va_f06_volume_accumulation_obvxad_63d_base_v104_signal,
    f06va_f06_volume_accumulation_obvxad_252d_base_v105_signal,
    f06va_f06_volume_accumulation_mfixad_21d_base_v106_signal,
    f06va_f06_volume_accumulation_mfixad_63d_base_v107_signal,
    f06va_f06_volume_accumulation_mfixad_252d_base_v108_signal,
    f06va_f06_volume_accumulation_adxdv_21d_base_v109_signal,
    f06va_f06_volume_accumulation_adxdv_63d_base_v110_signal,
    f06va_f06_volume_accumulation_adxdv_252d_base_v111_signal,
    f06va_f06_volume_accumulation_mfixret_21d_base_v112_signal,
    f06va_f06_volume_accumulation_mfixret_63d_base_v113_signal,
    f06va_f06_volume_accumulation_mfixret_252d_base_v114_signal,
    f06va_f06_volume_accumulation_adxret_21d_base_v115_signal,
    f06va_f06_volume_accumulation_adxret_63d_base_v116_signal,
    f06va_f06_volume_accumulation_adxret_252d_base_v117_signal,
    f06va_f06_volume_accumulation_obvxskew_63d_base_v118_signal,
    f06va_f06_volume_accumulation_obvxkurt_252d_base_v119_signal,
    f06va_f06_volume_accumulation_mfixskew_63d_base_v120_signal,
    f06va_f06_volume_accumulation_obvanom_21d_base_v121_signal,
    f06va_f06_volume_accumulation_obvanom_63d_base_v122_signal,
    f06va_f06_volume_accumulation_obvanom_252d_base_v123_signal,
    f06va_f06_volume_accumulation_mfianom_21d_base_v124_signal,
    f06va_f06_volume_accumulation_mfianom_63d_base_v125_signal,
    f06va_f06_volume_accumulation_adanom_21d_base_v126_signal,
    f06va_f06_volume_accumulation_adanom_63d_base_v127_signal,
    f06va_f06_volume_accumulation_obvxabsret_21d_base_v128_signal,
    f06va_f06_volume_accumulation_obvxabsret_63d_base_v129_signal,
    f06va_f06_volume_accumulation_mfixabsret_21d_base_v130_signal,
    f06va_f06_volume_accumulation_acccompxdv_21d_base_v131_signal,
    f06va_f06_volume_accumulation_acccompxdv_252d_base_v132_signal,
    f06va_f06_volume_accumulation_obvsum_63d_base_v133_signal,
    f06va_f06_volume_accumulation_obvsum_252d_base_v134_signal,
    f06va_f06_volume_accumulation_mfisum_63d_base_v135_signal,
    f06va_f06_volume_accumulation_adsum_63d_base_v136_signal,
    f06va_f06_volume_accumulation_obvmax_63d_base_v137_signal,
    f06va_f06_volume_accumulation_obvmax_252d_base_v138_signal,
    f06va_f06_volume_accumulation_obvmin_63d_base_v139_signal,
    f06va_f06_volume_accumulation_obvmin_252d_base_v140_signal,
    f06va_f06_volume_accumulation_obvsq_21d_base_v141_signal,
    f06va_f06_volume_accumulation_obvsq_63d_base_v142_signal,
    f06va_f06_volume_accumulation_obvsq_252d_base_v143_signal,
    f06va_f06_volume_accumulation_mfisq_21d_base_v144_signal,
    f06va_f06_volume_accumulation_mfisq_63d_base_v145_signal,
    f06va_f06_volume_accumulation_obvxvolratio_21d_base_v146_signal,
    f06va_f06_volume_accumulation_obvxvolratio_63d_base_v147_signal,
    f06va_f06_volume_accumulation_mfixvolratio_252d_base_v148_signal,
    f06va_f06_volume_accumulation_obvxhlspread_21d_base_v149_signal,
    f06va_f06_volume_accumulation_mfiemaxvolz_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_VOLUME_ACCUMULATION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f06_accumulation_obv", "_f06_money_flow", "_f06_accumulation_ad")
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
    print(f"OK f06_volume_accumulation_base_076_150_claude: {n_features} features pass")
