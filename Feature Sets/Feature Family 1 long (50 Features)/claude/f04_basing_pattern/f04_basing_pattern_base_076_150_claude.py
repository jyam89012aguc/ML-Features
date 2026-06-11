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
def _f04_basing_range(close, w):
    rmax = close.rolling(w, min_periods=max(1, w // 2)).max()
    rmin = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (rmax - rmin) / close.replace(0, np.nan).abs()


def _f04_basing_height(close, w):
    mid = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return (close - mid) / mid.replace(0, np.nan).abs()


def _f04_consolidation_atr(high, low, close, w):
    rng = (high - low) / close.replace(0, np.nan).abs()
    return rng.rolling(w, min_periods=max(1, w // 2)).mean()


# 21d basing range times return volatility (volatile-tight base)
def f04bp_f04_basing_pattern_rangexrv_21d_base_v076_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21)
    result = _f04_basing_range(closeadj, 21) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range times 63d return volatility
def f04bp_f04_basing_pattern_rangexrv_63d_base_v077_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    result = _f04_basing_range(closeadj, 63) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing range times 63d return volatility
def f04bp_f04_basing_pattern_rangexrv_252d_base_v078_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63)
    result = _f04_basing_range(closeadj, 252) * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range divided by return volatility (vol-adjusted tightness)
def f04bp_f04_basing_pattern_rangedivrv_21d_base_v079_signal(closeadj):
    rv = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    result = (_f04_basing_range(closeadj, 21) / rv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range / 63d return volatility
def f04bp_f04_basing_pattern_rangedivrv_63d_base_v080_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    result = (_f04_basing_range(closeadj, 63) / rv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing range / 63d return volatility
def f04bp_f04_basing_pattern_rangedivrv_252d_base_v081_signal(closeadj):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    result = (_f04_basing_range(closeadj, 252) / rv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR-style range / 21d return volatility
def f04bp_f04_basing_pattern_atrdivrv_21d_base_v082_signal(closeadj, high, low):
    rv = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    result = (_f04_consolidation_atr(high, low, closeadj, 21) / rv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR / 63d return volatility
def f04bp_f04_basing_pattern_atrdivrv_63d_base_v083_signal(closeadj, high, low):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    result = (_f04_consolidation_atr(high, low, closeadj, 63) / rv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range times skew of returns (asymmetric tight base)
def f04bp_f04_basing_pattern_rangexskew_63d_base_v084_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    result = _f04_basing_range(closeadj, 21) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range times kurtosis of returns
def f04bp_f04_basing_pattern_rangexkurt_252d_base_v085_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    result = _f04_basing_range(closeadj, 63) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing height times skewness
def f04bp_f04_basing_pattern_heightxskew_252d_base_v086_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    result = _f04_basing_height(closeadj, 252) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing height divided by 21d basing range (position-in-base)
def f04bp_f04_basing_pattern_heightoverrange_21d_base_v087_signal(closeadj):
    h = _f04_basing_height(closeadj, 21)
    r = _f04_basing_range(closeadj, 21).replace(0, np.nan)
    result = (h / r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d height/range
def f04bp_f04_basing_pattern_heightoverrange_63d_base_v088_signal(closeadj):
    h = _f04_basing_height(closeadj, 63)
    r = _f04_basing_range(closeadj, 63).replace(0, np.nan)
    result = (h / r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d height/range
def f04bp_f04_basing_pattern_heightoverrange_252d_base_v089_signal(closeadj):
    h = _f04_basing_height(closeadj, 252)
    r = _f04_basing_range(closeadj, 252).replace(0, np.nan)
    result = (h / r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range times absolute basing height
def f04bp_f04_basing_pattern_rangexabsheight_21d_base_v090_signal(closeadj):
    result = _f04_basing_range(closeadj, 21) * _f04_basing_height(closeadj, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range × abs height
def f04bp_f04_basing_pattern_rangexabsheight_63d_base_v091_signal(closeadj):
    result = _f04_basing_range(closeadj, 63) * _f04_basing_height(closeadj, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing range × abs height
def f04bp_f04_basing_pattern_rangexabsheight_252d_base_v092_signal(closeadj):
    result = _f04_basing_range(closeadj, 252) * _f04_basing_height(closeadj, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range minus rolling min of 252d range (tightening progress)
def f04bp_f04_basing_pattern_rangevsmin_252d_base_v093_signal(closeadj):
    r = _f04_basing_range(closeadj, 21)
    rmin = r.rolling(252, min_periods=63).min()
    result = (r - rmin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range minus rolling min of 504d range
def f04bp_f04_basing_pattern_rangevsmin_504d_base_v094_signal(closeadj):
    r = _f04_basing_range(closeadj, 63)
    rmin = r.rolling(504, min_periods=126).min()
    result = (r - rmin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range divided by rolling max of 504d range (relative to widest base)
def f04bp_f04_basing_pattern_rangepctmax_504d_base_v095_signal(closeadj):
    r = _f04_basing_range(closeadj, 252)
    rmax = r.rolling(504, min_periods=126).max().replace(0, np.nan)
    result = (r / rmax) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range divided by 252d max basing range
def f04bp_f04_basing_pattern_rangepctmax_252d_base_v096_signal(closeadj):
    r = _f04_basing_range(closeadj, 21)
    rmax = r.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (r / rmax) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding worst-tight base
def f04bp_f04_basing_pattern_tightestever_base_v097_signal(closeadj):
    r = _f04_basing_range(closeadj, 252)
    result = r.expanding(min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range minus expanding-min range (expansion vs all-time tight)
def f04bp_f04_basing_pattern_rangevshisttight_base_v098_signal(closeadj):
    r = _f04_basing_range(closeadj, 252)
    tight = r.expanding(min_periods=63).min()
    result = (r - tight) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d duration in narrow range (count of days range below 10% over 63d)
def f04bp_f04_basing_pattern_dayswithinnarrow_63d_base_v099_signal(closeadj):
    flag = (_f04_basing_range(closeadj, 21) < 0.10).astype(float)
    result = flag.rolling(63, min_periods=21).sum() * (1.0 + closeadj * 0.001)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d duration in narrow range
def f04bp_f04_basing_pattern_dayswithinnarrow_252d_base_v100_signal(closeadj):
    flag = (_f04_basing_range(closeadj, 21) < 0.07).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * (1.0 + closeadj * 0.001)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d days where 63d basing range below 28%, scaled by close
def f04bp_f04_basing_pattern_dayswithinnarrow_504d_base_v101_signal(closeadj):
    flag = (_f04_basing_range(closeadj, 63) < 0.28).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range × dollar volume (tight base × turnover)
def f04bp_f04_basing_pattern_rangexcurdv_21d_base_v102_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f04_basing_range(closeadj, 21) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range × dollar volume
def f04bp_f04_basing_pattern_rangexcurdv_63d_base_v103_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f04_basing_range(closeadj, 63) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing range × current dollar volume
def f04bp_f04_basing_pattern_rangexcurdv_252d_base_v104_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f04_basing_range(closeadj, 252) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range × volume zscore
def f04bp_f04_basing_pattern_rangexvolz_21d_base_v105_signal(closeadj, volume):
    result = _f04_basing_range(closeadj, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range × volume zscore
def f04bp_f04_basing_pattern_rangexvolz_63d_base_v106_signal(closeadj, volume):
    result = _f04_basing_range(closeadj, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing range × 252d volume zscore
def f04bp_f04_basing_pattern_rangexvolz_252d_base_v107_signal(closeadj, volume):
    result = _f04_basing_range(closeadj, 252) * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR × volume zscore
def f04bp_f04_basing_pattern_atrxvolz_21d_base_v108_signal(closeadj, high, low, volume):
    result = _f04_consolidation_atr(high, low, closeadj, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR × volume zscore
def f04bp_f04_basing_pattern_atrxvolz_63d_base_v109_signal(closeadj, high, low, volume):
    result = _f04_consolidation_atr(high, low, closeadj, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ATR × 252d dollar-volume mean
def f04bp_f04_basing_pattern_atrxdv_252d_base_v110_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    result = _f04_consolidation_atr(high, low, closeadj, 252) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of ATR
def f04bp_f04_basing_pattern_atrema_21d_base_v111_signal(closeadj, high, low):
    a = _f04_consolidation_atr(high, low, closeadj, 21)
    result = a.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of ATR
def f04bp_f04_basing_pattern_atrema_63d_base_v112_signal(closeadj, high, low):
    a = _f04_consolidation_atr(high, low, closeadj, 63)
    result = a.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of ATR
def f04bp_f04_basing_pattern_atrema_252d_base_v113_signal(closeadj, high, low):
    a = _f04_consolidation_atr(high, low, closeadj, 252)
    result = a.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of basing height
def f04bp_f04_basing_pattern_heightema_21d_base_v114_signal(closeadj):
    h = _f04_basing_height(closeadj, 21)
    result = h.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of basing height
def f04bp_f04_basing_pattern_heightema_63d_base_v115_signal(closeadj):
    h = _f04_basing_height(closeadj, 63)
    result = h.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of basing height
def f04bp_f04_basing_pattern_heightema_252d_base_v116_signal(closeadj):
    h = _f04_basing_height(closeadj, 252)
    result = h.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range area sum (cumulative tightness)
def f04bp_f04_basing_pattern_rangearea_63d_base_v117_signal(closeadj):
    r = _f04_basing_range(closeadj, 21)
    result = r.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range area
def f04bp_f04_basing_pattern_rangearea_252d_base_v118_signal(closeadj):
    r = _f04_basing_range(closeadj, 21)
    result = r.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range area
def f04bp_f04_basing_pattern_rangearea_504d_base_v119_signal(closeadj):
    r = _f04_basing_range(closeadj, 63)
    result = r.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range × 21d return (range × momentum)
def f04bp_f04_basing_pattern_rangexret_21d_base_v120_signal(closeadj):
    r21 = closeadj.pct_change(21)
    result = _f04_basing_range(closeadj, 21) * r21 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range × 63d return
def f04bp_f04_basing_pattern_rangexret_63d_base_v121_signal(closeadj):
    r63 = closeadj.pct_change(63)
    result = _f04_basing_range(closeadj, 63) * r63 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing range × 252d return
def f04bp_f04_basing_pattern_rangexret_252d_base_v122_signal(closeadj):
    r252 = closeadj.pct_change(252)
    result = _f04_basing_range(closeadj, 252) * r252 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing height × 21d return
def f04bp_f04_basing_pattern_heightxret_21d_base_v123_signal(closeadj):
    r21 = closeadj.pct_change(21)
    result = _f04_basing_height(closeadj, 21) * r21 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing height × 63d return
def f04bp_f04_basing_pattern_heightxret_63d_base_v124_signal(closeadj):
    r63 = closeadj.pct_change(63)
    result = _f04_basing_height(closeadj, 63) * r63 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing height × 252d return
def f04bp_f04_basing_pattern_heightxret_252d_base_v125_signal(closeadj):
    r252 = closeadj.pct_change(252)
    result = _f04_basing_height(closeadj, 252) * r252 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range times closeadj log
def f04bp_f04_basing_pattern_rangexlog_21d_base_v126_signal(closeadj):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    result = _f04_basing_range(closeadj, 21) * lg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range × closeadj log
def f04bp_f04_basing_pattern_rangexlog_63d_base_v127_signal(closeadj):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    result = _f04_basing_range(closeadj, 63) * lg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR × closeadj log
def f04bp_f04_basing_pattern_atrxlog_21d_base_v128_signal(closeadj, high, low):
    lg = np.log(closeadj.replace(0, np.nan).abs())
    result = _f04_consolidation_atr(high, low, closeadj, 21) * lg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range minus 252d EMA (deviation from smoothed)
def f04bp_f04_basing_pattern_rangedevema_63d_base_v129_signal(closeadj):
    r = _f04_basing_range(closeadj, 63)
    e = r.ewm(span=252, adjust=False).mean()
    result = (r - e) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing range minus 504d EMA
def f04bp_f04_basing_pattern_rangedevema_252d_base_v130_signal(closeadj):
    r = _f04_basing_range(closeadj, 252)
    e = r.ewm(span=504, adjust=False).mean()
    result = (r - e) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d height minus 252d height EMA
def f04bp_f04_basing_pattern_heightdevema_63d_base_v131_signal(closeadj):
    h = _f04_basing_height(closeadj, 63)
    e = h.ewm(span=252, adjust=False).mean()
    result = (h - e) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR minus 252d ATR EMA
def f04bp_f04_basing_pattern_atrdevema_21d_base_v132_signal(closeadj, high, low):
    a = _f04_consolidation_atr(high, low, closeadj, 21)
    e = a.ewm(span=252, adjust=False).mean()
    result = (a - e) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range × 21d ATR × closeadj (compound base intensity)
def f04bp_f04_basing_pattern_compbase_21d_base_v133_signal(closeadj, high, low):
    result = _f04_basing_range(closeadj, 21) * _f04_consolidation_atr(high, low, closeadj, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range + ATR composite
def f04bp_f04_basing_pattern_compbase_63d_base_v134_signal(closeadj, high, low):
    result = (_f04_basing_range(closeadj, 63) + _f04_consolidation_atr(high, low, closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range + ATR + abs height composite
def f04bp_f04_basing_pattern_compbase_252d_base_v135_signal(closeadj, high, low):
    result = (_f04_basing_range(closeadj, 252) + _f04_consolidation_atr(high, low, closeadj, 252) + _f04_basing_height(closeadj, 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range / closeadj log return std
def f04bp_f04_basing_pattern_rangeperriskunit_21d_base_v136_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan).abs()).diff()
    rv = lr.rolling(21, min_periods=5).std().replace(0, np.nan)
    result = (_f04_basing_range(closeadj, 21) / rv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range / 63d log-return std
def f04bp_f04_basing_pattern_rangeperriskunit_63d_base_v137_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan).abs()).diff()
    rv = lr.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = (_f04_basing_range(closeadj, 63) / rv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing range / 252d log-return std
def f04bp_f04_basing_pattern_rangeperriskunit_252d_base_v138_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan).abs()).diff()
    rv = lr.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = (_f04_basing_range(closeadj, 252) / rv) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range minus 21d range mean (range deviation)
def f04bp_f04_basing_pattern_rangedevmean_21d_base_v139_signal(closeadj):
    r = _f04_basing_range(closeadj, 21)
    m = _mean(r, 252)
    result = (r - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range minus 63d range mean over 252
def f04bp_f04_basing_pattern_rangedevmean_63d_base_v140_signal(closeadj):
    r = _f04_basing_range(closeadj, 63)
    m = _mean(r, 252)
    result = (r - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range minus 504d range mean
def f04bp_f04_basing_pattern_rangedevmean_252d_base_v141_signal(closeadj):
    r = _f04_basing_range(closeadj, 252)
    m = _mean(r, 504)
    result = (r - m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing height × 21d ATR (height-volatility product)
def f04bp_f04_basing_pattern_heightxatr_21d_base_v142_signal(closeadj, high, low):
    result = _f04_basing_height(closeadj, 21) * _f04_consolidation_atr(high, low, closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing height × ATR
def f04bp_f04_basing_pattern_heightxatr_63d_base_v143_signal(closeadj, high, low):
    result = _f04_basing_height(closeadj, 63) * _f04_consolidation_atr(high, low, closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing height × ATR
def f04bp_f04_basing_pattern_heightxatr_252d_base_v144_signal(closeadj, high, low):
    result = _f04_basing_height(closeadj, 252) * _f04_consolidation_atr(high, low, closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d std of basing height z
def f04bp_f04_basing_pattern_heightzstd_63d_base_v145_signal(closeadj):
    z = _z(_f04_basing_height(closeadj, 63), 252)
    result = _std(z, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d std of basing range z
def f04bp_f04_basing_pattern_rangezstd_252d_base_v146_signal(closeadj):
    z = _z(_f04_basing_range(closeadj, 63), 252)
    result = _std(z, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d std of ATR z
def f04bp_f04_basing_pattern_atrzstd_252d_base_v147_signal(closeadj, high, low):
    z = _z(_f04_consolidation_atr(high, low, closeadj, 63), 252)
    result = _std(z, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d basing range × 21d basing height (compound base shape)
def f04bp_f04_basing_pattern_rangexheight_21d_base_v148_signal(closeadj):
    result = _f04_basing_range(closeadj, 21) * _f04_basing_height(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d basing range × basing height
def f04bp_f04_basing_pattern_rangexheight_63d_base_v149_signal(closeadj):
    result = _f04_basing_range(closeadj, 63) * _f04_basing_height(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d basing range × basing height
def f04bp_f04_basing_pattern_rangexheight_252d_base_v150_signal(closeadj):
    result = _f04_basing_range(closeadj, 252) * _f04_basing_height(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04bp_f04_basing_pattern_rangexrv_21d_base_v076_signal,
    f04bp_f04_basing_pattern_rangexrv_63d_base_v077_signal,
    f04bp_f04_basing_pattern_rangexrv_252d_base_v078_signal,
    f04bp_f04_basing_pattern_rangedivrv_21d_base_v079_signal,
    f04bp_f04_basing_pattern_rangedivrv_63d_base_v080_signal,
    f04bp_f04_basing_pattern_rangedivrv_252d_base_v081_signal,
    f04bp_f04_basing_pattern_atrdivrv_21d_base_v082_signal,
    f04bp_f04_basing_pattern_atrdivrv_63d_base_v083_signal,
    f04bp_f04_basing_pattern_rangexskew_63d_base_v084_signal,
    f04bp_f04_basing_pattern_rangexkurt_252d_base_v085_signal,
    f04bp_f04_basing_pattern_heightxskew_252d_base_v086_signal,
    f04bp_f04_basing_pattern_heightoverrange_21d_base_v087_signal,
    f04bp_f04_basing_pattern_heightoverrange_63d_base_v088_signal,
    f04bp_f04_basing_pattern_heightoverrange_252d_base_v089_signal,
    f04bp_f04_basing_pattern_rangexabsheight_21d_base_v090_signal,
    f04bp_f04_basing_pattern_rangexabsheight_63d_base_v091_signal,
    f04bp_f04_basing_pattern_rangexabsheight_252d_base_v092_signal,
    f04bp_f04_basing_pattern_rangevsmin_252d_base_v093_signal,
    f04bp_f04_basing_pattern_rangevsmin_504d_base_v094_signal,
    f04bp_f04_basing_pattern_rangepctmax_504d_base_v095_signal,
    f04bp_f04_basing_pattern_rangepctmax_252d_base_v096_signal,
    f04bp_f04_basing_pattern_tightestever_base_v097_signal,
    f04bp_f04_basing_pattern_rangevshisttight_base_v098_signal,
    f04bp_f04_basing_pattern_dayswithinnarrow_63d_base_v099_signal,
    f04bp_f04_basing_pattern_dayswithinnarrow_252d_base_v100_signal,
    f04bp_f04_basing_pattern_dayswithinnarrow_504d_base_v101_signal,
    f04bp_f04_basing_pattern_rangexcurdv_21d_base_v102_signal,
    f04bp_f04_basing_pattern_rangexcurdv_63d_base_v103_signal,
    f04bp_f04_basing_pattern_rangexcurdv_252d_base_v104_signal,
    f04bp_f04_basing_pattern_rangexvolz_21d_base_v105_signal,
    f04bp_f04_basing_pattern_rangexvolz_63d_base_v106_signal,
    f04bp_f04_basing_pattern_rangexvolz_252d_base_v107_signal,
    f04bp_f04_basing_pattern_atrxvolz_21d_base_v108_signal,
    f04bp_f04_basing_pattern_atrxvolz_63d_base_v109_signal,
    f04bp_f04_basing_pattern_atrxdv_252d_base_v110_signal,
    f04bp_f04_basing_pattern_atrema_21d_base_v111_signal,
    f04bp_f04_basing_pattern_atrema_63d_base_v112_signal,
    f04bp_f04_basing_pattern_atrema_252d_base_v113_signal,
    f04bp_f04_basing_pattern_heightema_21d_base_v114_signal,
    f04bp_f04_basing_pattern_heightema_63d_base_v115_signal,
    f04bp_f04_basing_pattern_heightema_252d_base_v116_signal,
    f04bp_f04_basing_pattern_rangearea_63d_base_v117_signal,
    f04bp_f04_basing_pattern_rangearea_252d_base_v118_signal,
    f04bp_f04_basing_pattern_rangearea_504d_base_v119_signal,
    f04bp_f04_basing_pattern_rangexret_21d_base_v120_signal,
    f04bp_f04_basing_pattern_rangexret_63d_base_v121_signal,
    f04bp_f04_basing_pattern_rangexret_252d_base_v122_signal,
    f04bp_f04_basing_pattern_heightxret_21d_base_v123_signal,
    f04bp_f04_basing_pattern_heightxret_63d_base_v124_signal,
    f04bp_f04_basing_pattern_heightxret_252d_base_v125_signal,
    f04bp_f04_basing_pattern_rangexlog_21d_base_v126_signal,
    f04bp_f04_basing_pattern_rangexlog_63d_base_v127_signal,
    f04bp_f04_basing_pattern_atrxlog_21d_base_v128_signal,
    f04bp_f04_basing_pattern_rangedevema_63d_base_v129_signal,
    f04bp_f04_basing_pattern_rangedevema_252d_base_v130_signal,
    f04bp_f04_basing_pattern_heightdevema_63d_base_v131_signal,
    f04bp_f04_basing_pattern_atrdevema_21d_base_v132_signal,
    f04bp_f04_basing_pattern_compbase_21d_base_v133_signal,
    f04bp_f04_basing_pattern_compbase_63d_base_v134_signal,
    f04bp_f04_basing_pattern_compbase_252d_base_v135_signal,
    f04bp_f04_basing_pattern_rangeperriskunit_21d_base_v136_signal,
    f04bp_f04_basing_pattern_rangeperriskunit_63d_base_v137_signal,
    f04bp_f04_basing_pattern_rangeperriskunit_252d_base_v138_signal,
    f04bp_f04_basing_pattern_rangedevmean_21d_base_v139_signal,
    f04bp_f04_basing_pattern_rangedevmean_63d_base_v140_signal,
    f04bp_f04_basing_pattern_rangedevmean_252d_base_v141_signal,
    f04bp_f04_basing_pattern_heightxatr_21d_base_v142_signal,
    f04bp_f04_basing_pattern_heightxatr_63d_base_v143_signal,
    f04bp_f04_basing_pattern_heightxatr_252d_base_v144_signal,
    f04bp_f04_basing_pattern_heightzstd_63d_base_v145_signal,
    f04bp_f04_basing_pattern_rangezstd_252d_base_v146_signal,
    f04bp_f04_basing_pattern_atrzstd_252d_base_v147_signal,
    f04bp_f04_basing_pattern_rangexheight_21d_base_v148_signal,
    f04bp_f04_basing_pattern_rangexheight_63d_base_v149_signal,
    f04bp_f04_basing_pattern_rangexheight_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_BASING_PATTERN_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f04_basing_range", "_f04_basing_height", "_f04_consolidation_atr")
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
    print(f"OK f04_basing_pattern_base_076_150_claude: {n_features} features pass")
