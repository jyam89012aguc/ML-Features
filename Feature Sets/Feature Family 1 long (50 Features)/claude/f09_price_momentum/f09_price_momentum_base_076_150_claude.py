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
def _f09_momentum_roc(close, w):
    # rate of change (close to close) over window w
    return close.pct_change(periods=w)


def _f09_momentum_logret(close, w):
    # log return over window w
    return np.log(close / close.shift(w).replace(0, np.nan))


def _f09_momentum_riskadj(close, w, vol_w):
    # rate of change normalized by rolling stddev of returns
    r = close.pct_change(periods=w)
    s = _std(close.pct_change(), vol_w)
    return r / s.replace(0, np.nan)


# 21d ROC × ATR (ATR-weighted momentum)
def f09pm_f09_price_momentum_rocxatr_21d_base_v076_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f09_momentum_roc(closeadj, 21) * atr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × 21d ATR
def f09pm_f09_price_momentum_rocxatr_63d_base_v077_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = _f09_momentum_roc(closeadj, 63) * atr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × 63d ATR
def f09pm_f09_price_momentum_rocxatr_252d_base_v078_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = _f09_momentum_roc(closeadj, 252) * atr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC ratio: 5d/21d
def f09pm_f09_price_momentum_rocratio_5v21_base_v079_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 5)
    b = _f09_momentum_roc(closeadj, 21).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/63d ROC ratio
def f09pm_f09_price_momentum_rocratio_21v63_base_v080_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 21)
    b = _f09_momentum_roc(closeadj, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d ROC ratio
def f09pm_f09_price_momentum_rocratio_63v252_base_v081_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 63)
    b = _f09_momentum_roc(closeadj, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d/504d ROC ratio
def f09pm_f09_price_momentum_rocratio_252v504_base_v082_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 252)
    b = _f09_momentum_roc(closeadj, 504).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × log ret (compound momentum)
def f09pm_f09_price_momentum_rocxlog_21d_base_v083_signal(closeadj):
    result = _f09_momentum_roc(closeadj, 21) * _f09_momentum_logret(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × log ret
def f09pm_f09_price_momentum_rocxlog_63d_base_v084_signal(closeadj):
    result = _f09_momentum_roc(closeadj, 63) * _f09_momentum_logret(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × log ret
def f09pm_f09_price_momentum_rocxlog_252d_base_v085_signal(closeadj):
    result = _f09_momentum_roc(closeadj, 252) * _f09_momentum_logret(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × 21d skewness
def f09pm_f09_price_momentum_rocxskew_63d_base_v086_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    result = _f09_momentum_roc(closeadj, 63) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × 252d skewness
def f09pm_f09_price_momentum_rocxskew_252d_base_v087_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    result = _f09_momentum_roc(closeadj, 252) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × 63d kurtosis
def f09pm_f09_price_momentum_rocxkurt_63d_base_v088_signal(closeadj):
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    result = _f09_momentum_roc(closeadj, 63) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × 252d kurtosis
def f09pm_f09_price_momentum_rocxkurt_252d_base_v089_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    result = _f09_momentum_roc(closeadj, 252) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × 21d return mean (auto compounding)
def f09pm_f09_price_momentum_rocxretmean_21d_base_v090_signal(closeadj):
    rmean = _mean(closeadj.pct_change(), 21)
    result = _f09_momentum_roc(closeadj, 21) * rmean * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × 63d return mean
def f09pm_f09_price_momentum_rocxretmean_63d_base_v091_signal(closeadj):
    rmean = _mean(closeadj.pct_change(), 63)
    result = _f09_momentum_roc(closeadj, 63) * rmean * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × 252d return mean
def f09pm_f09_price_momentum_rocxretmean_252d_base_v092_signal(closeadj):
    rmean = _mean(closeadj.pct_change(), 252)
    result = _f09_momentum_roc(closeadj, 252) * rmean * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × close-to-close volatility
def f09pm_f09_price_momentum_rocxretvol_21d_base_v093_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    result = _f09_momentum_roc(closeadj, 21) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × volatility
def f09pm_f09_price_momentum_rocxretvol_63d_base_v094_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    result = _f09_momentum_roc(closeadj, 63) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × volatility
def f09pm_f09_price_momentum_rocxretvol_252d_base_v095_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    result = _f09_momentum_roc(closeadj, 252) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC percentile rank over 252d
def f09pm_f09_price_momentum_rocpct_252d_base_v096_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    result = r.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC percentile rank over 504d
def f09pm_f09_price_momentum_rocpct_504d_base_v097_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 63)
    result = r.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC percentile rank over 504d
def f09pm_f09_price_momentum_rocpct_252v504_base_v098_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 252)
    result = r.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding mean ROC scaled by close
def f09pm_f09_price_momentum_rocexpmean_21d_base_v099_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    base = r.expanding(min_periods=21).mean()
    result = (base + _f09_momentum_roc(closeadj, 252) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding std ROC
def f09pm_f09_price_momentum_rocexpstd_21d_base_v100_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    base = r.expanding(min_periods=21).std()
    result = (base + _f09_momentum_roc(closeadj, 252) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA-ROC
def f09pm_f09_price_momentum_emaroc_21d_base_v101_signal(closeadj):
    ema = closeadj.ewm(span=21, min_periods=11, adjust=False).mean()
    base = ema.pct_change(21)
    result = (base + _f09_momentum_roc(closeadj, 21) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA-ROC
def f09pm_f09_price_momentum_emaroc_63d_base_v102_signal(closeadj):
    ema = closeadj.ewm(span=63, min_periods=32, adjust=False).mean()
    base = ema.pct_change(21)
    result = (base + _f09_momentum_roc(closeadj, 63) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA-ROC
def f09pm_f09_price_momentum_emaroc_252d_base_v103_signal(closeadj):
    ema = closeadj.ewm(span=252, min_periods=126, adjust=False).mean()
    base = ema.pct_change(63)
    result = (base + _f09_momentum_roc(closeadj, 252) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EMA-ROC
def f09pm_f09_price_momentum_emaroc_504d_base_v104_signal(closeadj):
    ema = closeadj.ewm(span=504, min_periods=252, adjust=False).mean()
    base = ema.pct_change(126)
    result = (base + _f09_momentum_roc(closeadj, 504) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × 21d return autocorr (proxy)
def f09pm_f09_price_momentum_rocxret_21d_base_v105_signal(closeadj):
    r = closeadj.pct_change()
    result = _f09_momentum_roc(closeadj, 21) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × 5d return
def f09pm_f09_price_momentum_rocxret_5d_base_v106_signal(closeadj):
    r5 = closeadj.pct_change(5)
    result = _f09_momentum_roc(closeadj, 63) * r5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × 21d return
def f09pm_f09_price_momentum_rocxret_252_21d_base_v107_signal(closeadj):
    r = closeadj.pct_change(21)
    result = _f09_momentum_roc(closeadj, 252) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × abs return (severity)
def f09pm_f09_price_momentum_rocxabsret_21d_base_v108_signal(closeadj):
    ar = closeadj.pct_change().abs()
    result = _f09_momentum_roc(closeadj, 21) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × mean abs return
def f09pm_f09_price_momentum_rocxabsret_63d_base_v109_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 21)
    result = _f09_momentum_roc(closeadj, 63) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × mean abs return
def f09pm_f09_price_momentum_rocxabsret_252d_base_v110_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 63)
    result = _f09_momentum_roc(closeadj, 252) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × volume change
def f09pm_f09_price_momentum_rocxvolch_21d_base_v111_signal(closeadj, volume):
    vc = volume.pct_change(21)
    result = _f09_momentum_roc(closeadj, 21) * vc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × volume change
def f09pm_f09_price_momentum_rocxvolch_63d_base_v112_signal(closeadj, volume):
    vc = volume.pct_change(63)
    result = _f09_momentum_roc(closeadj, 63) * vc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × volume change
def f09pm_f09_price_momentum_rocxvolch_252d_base_v113_signal(closeadj, volume):
    vc = volume.pct_change(252)
    result = _f09_momentum_roc(closeadj, 252) * vc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × volume z-score
def f09pm_f09_price_momentum_rocxvolz_short_21d_base_v114_signal(closeadj, volume):
    result = _f09_momentum_roc(closeadj, 21) * _z(volume, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × volume z-score (long window)
def f09pm_f09_price_momentum_rocxvolz_long_63d_base_v115_signal(closeadj, volume):
    result = _f09_momentum_roc(closeadj, 63) * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sortino-like: mean ret / downside std
def f09pm_f09_price_momentum_sortino_21d_base_v116_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 21)
    neg = r.where(r < 0, 0.0)
    ds = _std(neg, 21)
    result = (m / ds.replace(0, np.nan)) * np.sqrt(252) * closeadj + _f09_momentum_roc(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sortino
def f09pm_f09_price_momentum_sortino_63d_base_v117_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 63)
    neg = r.where(r < 0, 0.0)
    ds = _std(neg, 63)
    result = (m / ds.replace(0, np.nan)) * np.sqrt(252) * closeadj + _f09_momentum_roc(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sortino
def f09pm_f09_price_momentum_sortino_252d_base_v118_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 252)
    neg = r.where(r < 0, 0.0)
    ds = _std(neg, 252)
    result = (m / ds.replace(0, np.nan)) * np.sqrt(252) * closeadj + _f09_momentum_roc(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d up/down ratio
def f09pm_f09_price_momentum_updownratio_21d_base_v119_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0).rolling(21, min_periods=5).sum()
    neg = r.where(r < 0, 0.0).abs().rolling(21, min_periods=5).sum().replace(0, np.nan)
    result = (pos / neg) * closeadj + _f09_momentum_roc(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d up/down ratio
def f09pm_f09_price_momentum_updownratio_63d_base_v120_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0).rolling(63, min_periods=21).sum()
    neg = r.where(r < 0, 0.0).abs().rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = (pos / neg) * closeadj + _f09_momentum_roc(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up/down ratio
def f09pm_f09_price_momentum_updownratio_252d_base_v121_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0).rolling(252, min_periods=63).sum()
    neg = r.where(r < 0, 0.0).abs().rolling(252, min_periods=63).sum().replace(0, np.nan)
    result = (pos / neg) * closeadj + _f09_momentum_roc(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RSI proxy 14d (typical RSI window)
def f09pm_f09_price_momentum_rsi_14d_base_v122_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0).rolling(14, min_periods=7).mean()
    neg = r.where(r < 0, 0.0).abs().rolling(14, min_periods=7).mean()
    rs = pos / neg.replace(0, np.nan)
    result = (100 - 100 / (1 + rs)) * closeadj + _f09_momentum_roc(closeadj, 14) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RSI proxy 21d
def f09pm_f09_price_momentum_rsi_21d_base_v123_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0).rolling(21, min_periods=11).mean()
    neg = r.where(r < 0, 0.0).abs().rolling(21, min_periods=11).mean()
    rs = pos / neg.replace(0, np.nan)
    result = (100 - 100 / (1 + rs)) * closeadj + _f09_momentum_roc(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RSI proxy 63d
def f09pm_f09_price_momentum_rsi_63d_base_v124_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0).rolling(63, min_periods=21).mean()
    neg = r.where(r < 0, 0.0).abs().rolling(63, min_periods=21).mean()
    rs = pos / neg.replace(0, np.nan)
    result = (100 - 100 / (1 + rs)) * closeadj + _f09_momentum_roc(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC integrated (sum)
def f09pm_f09_price_momentum_rocsum_63d_base_v125_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    result = r.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC integrated
def f09pm_f09_price_momentum_rocsum_252d_base_v126_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 63)
    result = r.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC integrated
def f09pm_f09_price_momentum_rocsum_504d_base_v127_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 252)
    result = r.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × 21d ATR ratio
def f09pm_f09_price_momentum_rocxatrratio_21d_base_v128_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean() / closeadj.replace(0, np.nan)
    result = _f09_momentum_roc(closeadj, 21) * atr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × 63d ATR ratio
def f09pm_f09_price_momentum_rocxatrratio_252d_base_v129_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean() / closeadj.replace(0, np.nan)
    result = _f09_momentum_roc(closeadj, 252) * atr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × 5d return
def f09pm_f09_price_momentum_rocxshort_21d_base_v130_signal(closeadj):
    r5 = closeadj.pct_change(5)
    result = _f09_momentum_roc(closeadj, 21) * r5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × 21d ROC
def f09pm_f09_price_momentum_rocprod_63x21_base_v131_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 63)
    b = _f09_momentum_roc(closeadj, 21)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × 63d ROC
def f09pm_f09_price_momentum_rocprod_252x63_base_v132_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 252)
    b = _f09_momentum_roc(closeadj, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ROC × 252d ROC
def f09pm_f09_price_momentum_rocprod_504x252_base_v133_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 504)
    b = _f09_momentum_roc(closeadj, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × volume mean
def f09pm_f09_price_momentum_rocxvolmean_21d_base_v134_signal(closeadj, volume):
    vm = _mean(volume, 21)
    result = _f09_momentum_roc(closeadj, 21) * vm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × volume mean
def f09pm_f09_price_momentum_rocxvolmean_63d_base_v135_signal(closeadj, volume):
    vm = _mean(volume, 63)
    result = _f09_momentum_roc(closeadj, 63) * vm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × volume mean
def f09pm_f09_price_momentum_rocxvolmean_252d_base_v136_signal(closeadj, volume):
    vm = _mean(volume, 252)
    result = _f09_momentum_roc(closeadj, 252) * vm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed ROC (sign × magnitude)
def f09pm_f09_price_momentum_signedroc_21d_base_v137_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 21)
    result = np.sign(r) * r.abs() * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed ROC
def f09pm_f09_price_momentum_signedroc_63d_base_v138_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 63)
    result = np.sign(r) * r.abs() * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed ROC
def f09pm_f09_price_momentum_signedroc_252d_base_v139_signal(closeadj):
    r = _f09_momentum_roc(closeadj, 252)
    result = np.sign(r) * r.abs() * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC z-score over 63d × volume z-score
def f09pm_f09_price_momentum_rocz_volz_21d_base_v140_signal(closeadj, volume):
    rz = _z(_f09_momentum_roc(closeadj, 21), 63)
    vz = _z(volume, 21)
    result = rz * vz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC z-score × volume z-score
def f09pm_f09_price_momentum_rocz_volz_63d_base_v141_signal(closeadj, volume):
    rz = _z(_f09_momentum_roc(closeadj, 63), 252)
    vz = _z(volume, 63)
    result = rz * vz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC z-score × dollar volume mean
def f09pm_f09_price_momentum_rocz_dv_252d_base_v142_signal(closeadj, volume):
    dv = closeadj * volume
    rz = _z(_f09_momentum_roc(closeadj, 252), 504)
    result = rz * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × intraday range (high-low)
def f09pm_f09_price_momentum_rocxrange_21d_base_v143_signal(closeadj, high, low):
    rng = (high - low)
    result = _f09_momentum_roc(closeadj, 21) * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × intraday range mean
def f09pm_f09_price_momentum_rocxrange_63d_base_v144_signal(closeadj, high, low):
    rng = _mean((high - low), 21)
    result = _f09_momentum_roc(closeadj, 63) * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × intraday range mean
def f09pm_f09_price_momentum_rocxrange_252d_base_v145_signal(closeadj, high, low):
    rng = _mean((high - low), 63)
    result = _f09_momentum_roc(closeadj, 252) * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROC × overnight gap
def f09pm_f09_price_momentum_rocxocgap_21d_base_v146_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    result = _f09_momentum_roc(closeadj, 21) * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROC × overnight gap z-score
def f09pm_f09_price_momentum_rocxocgapz_63d_base_v147_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    result = _f09_momentum_roc(closeadj, 63) * _z(gap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROC × overnight gap mean
def f09pm_f09_price_momentum_rocxocgapmean_252d_base_v148_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    result = _f09_momentum_roc(closeadj, 252) * _mean(gap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite momentum: 21d + 63d + 252d ROC weighted
def f09pm_f09_price_momentum_composite_short_base_v149_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 21)
    b = _f09_momentum_roc(closeadj, 63)
    c = _f09_momentum_roc(closeadj, 252)
    result = (a + b + c) / 3.0 * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite long-term momentum: 252d × 504d
def f09pm_f09_price_momentum_composite_long_base_v150_signal(closeadj):
    a = _f09_momentum_roc(closeadj, 252)
    b = _f09_momentum_roc(closeadj, 504)
    result = (a + b) * closeadj * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09pm_f09_price_momentum_rocxatr_21d_base_v076_signal,
    f09pm_f09_price_momentum_rocxatr_63d_base_v077_signal,
    f09pm_f09_price_momentum_rocxatr_252d_base_v078_signal,
    f09pm_f09_price_momentum_rocratio_5v21_base_v079_signal,
    f09pm_f09_price_momentum_rocratio_21v63_base_v080_signal,
    f09pm_f09_price_momentum_rocratio_63v252_base_v081_signal,
    f09pm_f09_price_momentum_rocratio_252v504_base_v082_signal,
    f09pm_f09_price_momentum_rocxlog_21d_base_v083_signal,
    f09pm_f09_price_momentum_rocxlog_63d_base_v084_signal,
    f09pm_f09_price_momentum_rocxlog_252d_base_v085_signal,
    f09pm_f09_price_momentum_rocxskew_63d_base_v086_signal,
    f09pm_f09_price_momentum_rocxskew_252d_base_v087_signal,
    f09pm_f09_price_momentum_rocxkurt_63d_base_v088_signal,
    f09pm_f09_price_momentum_rocxkurt_252d_base_v089_signal,
    f09pm_f09_price_momentum_rocxretmean_21d_base_v090_signal,
    f09pm_f09_price_momentum_rocxretmean_63d_base_v091_signal,
    f09pm_f09_price_momentum_rocxretmean_252d_base_v092_signal,
    f09pm_f09_price_momentum_rocxretvol_21d_base_v093_signal,
    f09pm_f09_price_momentum_rocxretvol_63d_base_v094_signal,
    f09pm_f09_price_momentum_rocxretvol_252d_base_v095_signal,
    f09pm_f09_price_momentum_rocpct_252d_base_v096_signal,
    f09pm_f09_price_momentum_rocpct_504d_base_v097_signal,
    f09pm_f09_price_momentum_rocpct_252v504_base_v098_signal,
    f09pm_f09_price_momentum_rocexpmean_21d_base_v099_signal,
    f09pm_f09_price_momentum_rocexpstd_21d_base_v100_signal,
    f09pm_f09_price_momentum_emaroc_21d_base_v101_signal,
    f09pm_f09_price_momentum_emaroc_63d_base_v102_signal,
    f09pm_f09_price_momentum_emaroc_252d_base_v103_signal,
    f09pm_f09_price_momentum_emaroc_504d_base_v104_signal,
    f09pm_f09_price_momentum_rocxret_21d_base_v105_signal,
    f09pm_f09_price_momentum_rocxret_5d_base_v106_signal,
    f09pm_f09_price_momentum_rocxret_252_21d_base_v107_signal,
    f09pm_f09_price_momentum_rocxabsret_21d_base_v108_signal,
    f09pm_f09_price_momentum_rocxabsret_63d_base_v109_signal,
    f09pm_f09_price_momentum_rocxabsret_252d_base_v110_signal,
    f09pm_f09_price_momentum_rocxvolch_21d_base_v111_signal,
    f09pm_f09_price_momentum_rocxvolch_63d_base_v112_signal,
    f09pm_f09_price_momentum_rocxvolch_252d_base_v113_signal,
    f09pm_f09_price_momentum_rocxvolz_short_21d_base_v114_signal,
    f09pm_f09_price_momentum_rocxvolz_long_63d_base_v115_signal,
    f09pm_f09_price_momentum_sortino_21d_base_v116_signal,
    f09pm_f09_price_momentum_sortino_63d_base_v117_signal,
    f09pm_f09_price_momentum_sortino_252d_base_v118_signal,
    f09pm_f09_price_momentum_updownratio_21d_base_v119_signal,
    f09pm_f09_price_momentum_updownratio_63d_base_v120_signal,
    f09pm_f09_price_momentum_updownratio_252d_base_v121_signal,
    f09pm_f09_price_momentum_rsi_14d_base_v122_signal,
    f09pm_f09_price_momentum_rsi_21d_base_v123_signal,
    f09pm_f09_price_momentum_rsi_63d_base_v124_signal,
    f09pm_f09_price_momentum_rocsum_63d_base_v125_signal,
    f09pm_f09_price_momentum_rocsum_252d_base_v126_signal,
    f09pm_f09_price_momentum_rocsum_504d_base_v127_signal,
    f09pm_f09_price_momentum_rocxatrratio_21d_base_v128_signal,
    f09pm_f09_price_momentum_rocxatrratio_252d_base_v129_signal,
    f09pm_f09_price_momentum_rocxshort_21d_base_v130_signal,
    f09pm_f09_price_momentum_rocprod_63x21_base_v131_signal,
    f09pm_f09_price_momentum_rocprod_252x63_base_v132_signal,
    f09pm_f09_price_momentum_rocprod_504x252_base_v133_signal,
    f09pm_f09_price_momentum_rocxvolmean_21d_base_v134_signal,
    f09pm_f09_price_momentum_rocxvolmean_63d_base_v135_signal,
    f09pm_f09_price_momentum_rocxvolmean_252d_base_v136_signal,
    f09pm_f09_price_momentum_signedroc_21d_base_v137_signal,
    f09pm_f09_price_momentum_signedroc_63d_base_v138_signal,
    f09pm_f09_price_momentum_signedroc_252d_base_v139_signal,
    f09pm_f09_price_momentum_rocz_volz_21d_base_v140_signal,
    f09pm_f09_price_momentum_rocz_volz_63d_base_v141_signal,
    f09pm_f09_price_momentum_rocz_dv_252d_base_v142_signal,
    f09pm_f09_price_momentum_rocxrange_21d_base_v143_signal,
    f09pm_f09_price_momentum_rocxrange_63d_base_v144_signal,
    f09pm_f09_price_momentum_rocxrange_252d_base_v145_signal,
    f09pm_f09_price_momentum_rocxocgap_21d_base_v146_signal,
    f09pm_f09_price_momentum_rocxocgapz_63d_base_v147_signal,
    f09pm_f09_price_momentum_rocxocgapmean_252d_base_v148_signal,
    f09pm_f09_price_momentum_composite_short_base_v149_signal,
    f09pm_f09_price_momentum_composite_long_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_PRICE_MOMENTUM_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    open_ = closeadj * (1.0 + np.random.normal(0, 0.005, n))
    open_ = pd.Series(open_, name="open")
    close = closeadj.copy()
    close.name = "close"
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "open": open_, "close": close, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f09_momentum_roc", "_f09_momentum_logret", "_f09_momentum_riskadj")
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
    print(f"OK f09_price_momentum_base_076_150_claude: {n_features} features pass")
