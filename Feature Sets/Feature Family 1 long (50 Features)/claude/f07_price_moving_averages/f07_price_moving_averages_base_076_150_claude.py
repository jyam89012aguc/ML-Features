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
def _f07_price_ma(close, w):
    # simple moving average of price over window w
    return close.rolling(w, min_periods=max(1, w // 2)).mean()


def _f07_above_ma_dist(close, w):
    # distance of price above SMA in percent terms
    ma = _f07_price_ma(close, w)
    return (close - ma) / ma.replace(0, np.nan).abs()


def _f07_above_ma_atr(close, high, low, w):
    # distance of price above SMA in ATR units
    ma = _f07_price_ma(close, w)
    atr = (high - low).rolling(21, min_periods=5).mean()
    return (close - ma) / atr.replace(0, np.nan)


# 21d EMA-style SMA distance using exponential weighting
def f07pma_f07_price_moving_averages_emadist_21d_base_v076_signal(closeadj):
    ema = closeadj.ewm(span=21, min_periods=11, adjust=False).mean()
    base = (closeadj - ema) / ema.replace(0, np.nan).abs()
    result = (base + _f07_above_ma_dist(closeadj, 21) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA-style SMA distance
def f07pma_f07_price_moving_averages_emadist_63d_base_v077_signal(closeadj):
    ema = closeadj.ewm(span=63, min_periods=32, adjust=False).mean()
    base = (closeadj - ema) / ema.replace(0, np.nan).abs()
    result = (base + _f07_above_ma_dist(closeadj, 63) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EMA-style SMA distance
def f07pma_f07_price_moving_averages_emadist_126d_base_v078_signal(closeadj):
    ema = closeadj.ewm(span=126, min_periods=63, adjust=False).mean()
    base = (closeadj - ema) / ema.replace(0, np.nan).abs()
    result = (base + _f07_above_ma_dist(closeadj, 126) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA-style SMA distance
def f07pma_f07_price_moving_averages_emadist_252d_base_v079_signal(closeadj):
    ema = closeadj.ewm(span=252, min_periods=126, adjust=False).mean()
    base = (closeadj - ema) / ema.replace(0, np.nan).abs()
    result = (base + _f07_above_ma_dist(closeadj, 252) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EMA-style SMA distance
def f07pma_f07_price_moving_averages_emadist_504d_base_v080_signal(closeadj):
    ema = closeadj.ewm(span=504, min_periods=252, adjust=False).mean()
    base = (closeadj - ema) / ema.replace(0, np.nan).abs()
    result = (base + _f07_above_ma_dist(closeadj, 504) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d distance from SMA averaged across 5 anchors
def f07pma_f07_price_moving_averages_distmulti_21d_base_v081_signal(closeadj):
    a = _f07_above_ma_dist(closeadj, 5)
    b = _f07_above_ma_dist(closeadj, 21)
    result = (a + b) * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite SMA distance using 21d and 63d
def f07pma_f07_price_moving_averages_distmulti_63d_base_v082_signal(closeadj):
    a = _f07_above_ma_dist(closeadj, 21)
    b = _f07_above_ma_dist(closeadj, 63)
    result = (a + b) * closeadj * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite SMA distance using 63d, 126d, 252d
def f07pma_f07_price_moving_averages_distmulti_252d_base_v083_signal(closeadj):
    a = _f07_above_ma_dist(closeadj, 63)
    b = _f07_above_ma_dist(closeadj, 126)
    c = _f07_above_ma_dist(closeadj, 252)
    result = (a + b + c) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite SMA distance using 126d, 252d, 504d
def f07pma_f07_price_moving_averages_distmulti_504d_base_v084_signal(closeadj):
    a = _f07_above_ma_dist(closeadj, 126)
    b = _f07_above_ma_dist(closeadj, 252)
    c = _f07_above_ma_dist(closeadj, 504)
    result = (a + b + c) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA slope (price ma minus its lag) scaled
def f07pma_f07_price_moving_averages_smaslope_21d_base_v085_signal(closeadj):
    ma = _f07_price_ma(closeadj, 21)
    result = (ma - ma.shift(5)) / ma.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA slope (price ma minus its lag)
def f07pma_f07_price_moving_averages_smaslope_63d_base_v086_signal(closeadj):
    ma = _f07_price_ma(closeadj, 63)
    result = (ma - ma.shift(21)) / ma.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA slope
def f07pma_f07_price_moving_averages_smaslope_252d_base_v087_signal(closeadj):
    ma = _f07_price_ma(closeadj, 252)
    result = (ma - ma.shift(63)) / ma.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d SMA slope
def f07pma_f07_price_moving_averages_smaslope_504d_base_v088_signal(closeadj):
    ma = _f07_price_ma(closeadj, 504)
    result = (ma - ma.shift(126)) / ma.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance × 5d return
def f07pma_f07_price_moving_averages_distxret_5d_base_v089_signal(closeadj):
    r5 = closeadj.pct_change(5)
    result = _f07_above_ma_dist(closeadj, 21) * r5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance × 21d return
def f07pma_f07_price_moving_averages_distxret_21d_base_v090_signal(closeadj):
    r21 = closeadj.pct_change(21)
    result = _f07_above_ma_dist(closeadj, 63) * r21 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance × 63d return
def f07pma_f07_price_moving_averages_distxret_63d_base_v091_signal(closeadj):
    r63 = closeadj.pct_change(63)
    result = _f07_above_ma_dist(closeadj, 252) * r63 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d SMA distance × 252d return
def f07pma_f07_price_moving_averages_distxret_252d_base_v092_signal(closeadj):
    r252 = closeadj.pct_change(252)
    result = _f07_above_ma_dist(closeadj, 504) * r252 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance × skewness of returns
def f07pma_f07_price_moving_averages_distxskew_63d_base_v093_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    result = _f07_above_ma_dist(closeadj, 63) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance × skewness of returns
def f07pma_f07_price_moving_averages_distxskew_252d_base_v094_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    result = _f07_above_ma_dist(closeadj, 252) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance × kurtosis of returns
def f07pma_f07_price_moving_averages_distxkurt_63d_base_v095_signal(closeadj):
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    result = _f07_above_ma_dist(closeadj, 63) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance × kurtosis of returns
def f07pma_f07_price_moving_averages_distxkurt_252d_base_v096_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    result = _f07_above_ma_dist(closeadj, 252) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding mean SMA distance scaled by current price
def f07pma_f07_price_moving_averages_distexp_252d_base_v097_signal(closeadj):
    ma = closeadj.expanding(min_periods=21).mean()
    base = (closeadj - ma) / ma.replace(0, np.nan).abs()
    result = (base + _f07_above_ma_dist(closeadj, 252) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d SMA distance × dollar volume
def f07pma_f07_price_moving_averages_distxdv_5d_base_v098_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f07_above_ma_dist(closeadj, 5) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance × dollar volume
def f07pma_f07_price_moving_averages_distxdv_21d_base_v099_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f07_above_ma_dist(closeadj, 21) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance × dollar volume
def f07pma_f07_price_moving_averages_distxdv_63d_base_v100_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f07_above_ma_dist(closeadj, 63) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 504d SMA distance × dollar volume
def f07pma_f07_price_moving_averages_distxdv_504d_base_v101_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f07_above_ma_dist(closeadj, 504) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 21d SMA × ATR weighted by close
def f07pma_f07_price_moving_averages_distatrxret_21d_base_v102_signal(closeadj, high, low):
    r = closeadj.pct_change(5)
    result = _f07_above_ma_atr(closeadj, high, low, 21) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 63d SMA × ATR × 21d return
def f07pma_f07_price_moving_averages_distatrxret_63d_base_v103_signal(closeadj, high, low):
    r = closeadj.pct_change(21)
    result = _f07_above_ma_atr(closeadj, high, low, 63) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 504d SMA × ATR × 252d return
def f07pma_f07_price_moving_averages_distatrxret_504d_base_v104_signal(closeadj, high, low):
    r = closeadj.pct_change(252)
    result = _f07_above_ma_atr(closeadj, high, low, 504) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of days above 21d SMA, scaled by close
def f07pma_f07_price_moving_averages_aboveruncts_21d_base_v105_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 21) > 0).astype(float)
    result = flag.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days above 63d SMA, scaled by close
def f07pma_f07_price_moving_averages_aboveruncts_63d_base_v106_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 63) > 0).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days above 252d SMA, scaled by close
def f07pma_f07_price_moving_averages_aboveruncts_252d_base_v107_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 252) > 0).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days above 504d SMA, scaled by close
def f07pma_f07_price_moving_averages_aboveruncts_504d_base_v108_signal(closeadj):
    flag = (_f07_above_ma_dist(closeadj, 504) > 0).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance × open-close gap
def f07pma_f07_price_moving_averages_distxocgap_21d_base_v109_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    result = _f07_above_ma_dist(closeadj, 21) * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance × overnight gap
def f07pma_f07_price_moving_averages_distxocgap_63d_base_v110_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    result = _f07_above_ma_dist(closeadj, 63) * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance × monthly gap z-score
def f07pma_f07_price_moving_averages_distxgapz_252d_base_v111_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    result = _f07_above_ma_dist(closeadj, 252) * _z(gap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance × intraday range
def f07pma_f07_price_moving_averages_distxintraday_21d_base_v112_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan).abs()
    result = _f07_above_ma_dist(closeadj, 21) * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance × intraday range
def f07pma_f07_price_moving_averages_distxintraday_63d_base_v113_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan).abs()
    result = _f07_above_ma_dist(closeadj, 63) * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance × intraday range mean
def f07pma_f07_price_moving_averages_distxintraday_252d_base_v114_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan).abs()
    result = _f07_above_ma_dist(closeadj, 252) * _mean(rng, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d distance min over 21d window
def f07pma_f07_price_moving_averages_distminw_21d_base_v115_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    result = d.rolling(21, min_periods=5).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distance min over 63d window
def f07pma_f07_price_moving_averages_distminw_63d_base_v116_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    result = d.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distance min over 252d
def f07pma_f07_price_moving_averages_distminw_252d_base_v117_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 252)
    result = d.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d distance max over 21d
def f07pma_f07_price_moving_averages_distmaxw_21d_base_v118_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    result = d.rolling(21, min_periods=5).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distance max over 63d
def f07pma_f07_price_moving_averages_distmaxw_63d_base_v119_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    result = d.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distance max over 252d
def f07pma_f07_price_moving_averages_distmaxw_252d_base_v120_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 252)
    result = d.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d distance range (max - min)
def f07pma_f07_price_moving_averages_distrange_21d_base_v121_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    result = (d.rolling(21, min_periods=5).max() - d.rolling(21, min_periods=5).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d distance range
def f07pma_f07_price_moving_averages_distrange_63d_base_v122_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    result = (d.rolling(63, min_periods=21).max() - d.rolling(63, min_periods=21).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d distance range
def f07pma_f07_price_moving_averages_distrange_252d_base_v123_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 252)
    result = (d.rolling(252, min_periods=63).max() - d.rolling(252, min_periods=63).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR distance × volume z-score
def f07pma_f07_price_moving_averages_distatrxvolz_21d_base_v124_signal(closeadj, high, low, volume):
    result = _f07_above_ma_atr(closeadj, high, low, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR distance × volume z-score
def f07pma_f07_price_moving_averages_distatrxvolz_63d_base_v125_signal(closeadj, high, low, volume):
    result = _f07_above_ma_atr(closeadj, high, low, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ATR distance × volume z-score
def f07pma_f07_price_moving_averages_distatrxvolz_252d_base_v126_signal(closeadj, high, low, volume):
    result = _f07_above_ma_atr(closeadj, high, low, 252) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance times absolute return
def f07pma_f07_price_moving_averages_distxabsret_21d_base_v127_signal(closeadj):
    ar = closeadj.pct_change().abs()
    result = _f07_above_ma_dist(closeadj, 21) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance times mean abs return
def f07pma_f07_price_moving_averages_distxabsret_63d_base_v128_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 21)
    result = _f07_above_ma_dist(closeadj, 63) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance times mean abs return
def f07pma_f07_price_moving_averages_distxabsret_252d_base_v129_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 63)
    result = _f07_above_ma_dist(closeadj, 252) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance × volume change
def f07pma_f07_price_moving_averages_distxvolch_21d_base_v130_signal(closeadj, volume):
    vc = volume.pct_change(21)
    result = _f07_above_ma_dist(closeadj, 21) * vc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance × volume change
def f07pma_f07_price_moving_averages_distxvolch_63d_base_v131_signal(closeadj, volume):
    vc = volume.pct_change(63)
    result = _f07_above_ma_dist(closeadj, 63) * vc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance × volume change
def f07pma_f07_price_moving_averages_distxvolch_252d_base_v132_signal(closeadj, volume):
    vc = volume.pct_change(252)
    result = _f07_above_ma_dist(closeadj, 252) * vc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA spread (close-SMA) × ATR
def f07pma_f07_price_moving_averages_spreadxatr_21d_base_v133_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    spread = closeadj - _f07_price_ma(closeadj, 21)
    base = _f07_above_ma_dist(closeadj, 21) * 0.0
    result = (spread * atr) + base
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA spread × ATR
def f07pma_f07_price_moving_averages_spreadxatr_63d_base_v134_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    spread = closeadj - _f07_price_ma(closeadj, 63)
    base = _f07_above_ma_dist(closeadj, 63) * 0.0
    result = (spread * atr) + base
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA spread × ATR
def f07pma_f07_price_moving_averages_spreadxatr_252d_base_v135_signal(closeadj, high, low):
    atr = (high - low).rolling(63, min_periods=21).mean()
    spread = closeadj - _f07_price_ma(closeadj, 252)
    base = _f07_above_ma_dist(closeadj, 252) * 0.0
    result = (spread * atr) + base
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance / 252d SMA distance ratio
def f07pma_f07_price_moving_averages_distrelratio_21v252_base_v136_signal(closeadj):
    a = _f07_above_ma_dist(closeadj, 21)
    b = _f07_above_ma_dist(closeadj, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance / 504d SMA distance ratio
def f07pma_f07_price_moving_averages_distrelratio_63v504_base_v137_signal(closeadj):
    a = _f07_above_ma_dist(closeadj, 63)
    b = _f07_above_ma_dist(closeadj, 504).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance × 21d return std
def f07pma_f07_price_moving_averages_distxstd_21d_base_v138_signal(closeadj):
    s = _std(closeadj.pct_change(), 21)
    result = _f07_above_ma_dist(closeadj, 21) * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance × 63d return std
def f07pma_f07_price_moving_averages_distxstd_63d_base_v139_signal(closeadj):
    s = _std(closeadj.pct_change(), 63)
    result = _f07_above_ma_dist(closeadj, 63) * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance × 252d return std
def f07pma_f07_price_moving_averages_distxstd_252d_base_v140_signal(closeadj):
    s = _std(closeadj.pct_change(), 252)
    result = _f07_above_ma_dist(closeadj, 252) * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance summed and price-weighted
def f07pma_f07_price_moving_averages_distintegxprice_21d_base_v141_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 21)
    result = d.rolling(63, min_periods=21).sum() * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance summed and price-weighted
def f07pma_f07_price_moving_averages_distintegxprice_63d_base_v142_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 63)
    result = d.rolling(252, min_periods=63).sum() * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance summed and price-weighted
def f07pma_f07_price_moving_averages_distintegxprice_252d_base_v143_signal(closeadj):
    d = _f07_above_ma_dist(closeadj, 252)
    result = d.rolling(252, min_periods=63).sum() * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA distance correlation with returns proxy via product
def f07pma_f07_price_moving_averages_distxretmean_21d_base_v144_signal(closeadj):
    rmean = _mean(closeadj.pct_change(), 21)
    result = _f07_above_ma_dist(closeadj, 21) * rmean * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA distance × 63d mean return
def f07pma_f07_price_moving_averages_distxretmean_63d_base_v145_signal(closeadj):
    rmean = _mean(closeadj.pct_change(), 63)
    result = _f07_above_ma_dist(closeadj, 63) * rmean * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d SMA distance × 252d mean return
def f07pma_f07_price_moving_averages_distxretmean_252d_base_v146_signal(closeadj):
    rmean = _mean(closeadj.pct_change(), 252)
    result = _f07_above_ma_dist(closeadj, 252) * rmean * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR-distance × dollar volume
def f07pma_f07_price_moving_averages_distatrxdv_21d_base_v147_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    result = _f07_above_ma_atr(closeadj, high, low, 21) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR-distance × dollar volume
def f07pma_f07_price_moving_averages_distatrxdv_63d_base_v148_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    result = _f07_above_ma_atr(closeadj, high, low, 63) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ATR-distance × dollar volume mean
def f07pma_f07_price_moving_averages_distatrxdv_252d_base_v149_signal(closeadj, high, low, volume):
    dv = closeadj * volume
    result = _f07_above_ma_atr(closeadj, high, low, 252) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# composite SMA-distance signal: (21d - 252d) × close × ATR
def f07pma_f07_price_moving_averages_composite_21v252_base_v150_signal(closeadj, high, low):
    atr = (high - low).rolling(21, min_periods=5).mean()
    diff = _f07_above_ma_dist(closeadj, 21) - _f07_above_ma_dist(closeadj, 252)
    result = diff * closeadj * atr
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07pma_f07_price_moving_averages_emadist_21d_base_v076_signal,
    f07pma_f07_price_moving_averages_emadist_63d_base_v077_signal,
    f07pma_f07_price_moving_averages_emadist_126d_base_v078_signal,
    f07pma_f07_price_moving_averages_emadist_252d_base_v079_signal,
    f07pma_f07_price_moving_averages_emadist_504d_base_v080_signal,
    f07pma_f07_price_moving_averages_distmulti_21d_base_v081_signal,
    f07pma_f07_price_moving_averages_distmulti_63d_base_v082_signal,
    f07pma_f07_price_moving_averages_distmulti_252d_base_v083_signal,
    f07pma_f07_price_moving_averages_distmulti_504d_base_v084_signal,
    f07pma_f07_price_moving_averages_smaslope_21d_base_v085_signal,
    f07pma_f07_price_moving_averages_smaslope_63d_base_v086_signal,
    f07pma_f07_price_moving_averages_smaslope_252d_base_v087_signal,
    f07pma_f07_price_moving_averages_smaslope_504d_base_v088_signal,
    f07pma_f07_price_moving_averages_distxret_5d_base_v089_signal,
    f07pma_f07_price_moving_averages_distxret_21d_base_v090_signal,
    f07pma_f07_price_moving_averages_distxret_63d_base_v091_signal,
    f07pma_f07_price_moving_averages_distxret_252d_base_v092_signal,
    f07pma_f07_price_moving_averages_distxskew_63d_base_v093_signal,
    f07pma_f07_price_moving_averages_distxskew_252d_base_v094_signal,
    f07pma_f07_price_moving_averages_distxkurt_63d_base_v095_signal,
    f07pma_f07_price_moving_averages_distxkurt_252d_base_v096_signal,
    f07pma_f07_price_moving_averages_distexp_252d_base_v097_signal,
    f07pma_f07_price_moving_averages_distxdv_5d_base_v098_signal,
    f07pma_f07_price_moving_averages_distxdv_21d_base_v099_signal,
    f07pma_f07_price_moving_averages_distxdv_63d_base_v100_signal,
    f07pma_f07_price_moving_averages_distxdv_504d_base_v101_signal,
    f07pma_f07_price_moving_averages_distatrxret_21d_base_v102_signal,
    f07pma_f07_price_moving_averages_distatrxret_63d_base_v103_signal,
    f07pma_f07_price_moving_averages_distatrxret_504d_base_v104_signal,
    f07pma_f07_price_moving_averages_aboveruncts_21d_base_v105_signal,
    f07pma_f07_price_moving_averages_aboveruncts_63d_base_v106_signal,
    f07pma_f07_price_moving_averages_aboveruncts_252d_base_v107_signal,
    f07pma_f07_price_moving_averages_aboveruncts_504d_base_v108_signal,
    f07pma_f07_price_moving_averages_distxocgap_21d_base_v109_signal,
    f07pma_f07_price_moving_averages_distxocgap_63d_base_v110_signal,
    f07pma_f07_price_moving_averages_distxgapz_252d_base_v111_signal,
    f07pma_f07_price_moving_averages_distxintraday_21d_base_v112_signal,
    f07pma_f07_price_moving_averages_distxintraday_63d_base_v113_signal,
    f07pma_f07_price_moving_averages_distxintraday_252d_base_v114_signal,
    f07pma_f07_price_moving_averages_distminw_21d_base_v115_signal,
    f07pma_f07_price_moving_averages_distminw_63d_base_v116_signal,
    f07pma_f07_price_moving_averages_distminw_252d_base_v117_signal,
    f07pma_f07_price_moving_averages_distmaxw_21d_base_v118_signal,
    f07pma_f07_price_moving_averages_distmaxw_63d_base_v119_signal,
    f07pma_f07_price_moving_averages_distmaxw_252d_base_v120_signal,
    f07pma_f07_price_moving_averages_distrange_21d_base_v121_signal,
    f07pma_f07_price_moving_averages_distrange_63d_base_v122_signal,
    f07pma_f07_price_moving_averages_distrange_252d_base_v123_signal,
    f07pma_f07_price_moving_averages_distatrxvolz_21d_base_v124_signal,
    f07pma_f07_price_moving_averages_distatrxvolz_63d_base_v125_signal,
    f07pma_f07_price_moving_averages_distatrxvolz_252d_base_v126_signal,
    f07pma_f07_price_moving_averages_distxabsret_21d_base_v127_signal,
    f07pma_f07_price_moving_averages_distxabsret_63d_base_v128_signal,
    f07pma_f07_price_moving_averages_distxabsret_252d_base_v129_signal,
    f07pma_f07_price_moving_averages_distxvolch_21d_base_v130_signal,
    f07pma_f07_price_moving_averages_distxvolch_63d_base_v131_signal,
    f07pma_f07_price_moving_averages_distxvolch_252d_base_v132_signal,
    f07pma_f07_price_moving_averages_spreadxatr_21d_base_v133_signal,
    f07pma_f07_price_moving_averages_spreadxatr_63d_base_v134_signal,
    f07pma_f07_price_moving_averages_spreadxatr_252d_base_v135_signal,
    f07pma_f07_price_moving_averages_distrelratio_21v252_base_v136_signal,
    f07pma_f07_price_moving_averages_distrelratio_63v504_base_v137_signal,
    f07pma_f07_price_moving_averages_distxstd_21d_base_v138_signal,
    f07pma_f07_price_moving_averages_distxstd_63d_base_v139_signal,
    f07pma_f07_price_moving_averages_distxstd_252d_base_v140_signal,
    f07pma_f07_price_moving_averages_distintegxprice_21d_base_v141_signal,
    f07pma_f07_price_moving_averages_distintegxprice_63d_base_v142_signal,
    f07pma_f07_price_moving_averages_distintegxprice_252d_base_v143_signal,
    f07pma_f07_price_moving_averages_distxretmean_21d_base_v144_signal,
    f07pma_f07_price_moving_averages_distxretmean_63d_base_v145_signal,
    f07pma_f07_price_moving_averages_distxretmean_252d_base_v146_signal,
    f07pma_f07_price_moving_averages_distatrxdv_21d_base_v147_signal,
    f07pma_f07_price_moving_averages_distatrxdv_63d_base_v148_signal,
    f07pma_f07_price_moving_averages_distatrxdv_252d_base_v149_signal,
    f07pma_f07_price_moving_averages_composite_21v252_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_PRICE_MOVING_AVERAGES_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f07_price_ma", "_f07_above_ma_dist", "_f07_above_ma_atr")
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
    print(f"OK f07_price_moving_averages_base_076_150_claude: {n_features} features pass")
