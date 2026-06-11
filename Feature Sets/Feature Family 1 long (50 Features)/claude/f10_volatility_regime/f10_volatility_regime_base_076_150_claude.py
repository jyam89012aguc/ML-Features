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
def _f10_vol_regime_retstd(close, w):
    # rolling stddev of pct-change returns (volatility)
    return close.pct_change().rolling(w, min_periods=max(1, w // 2)).std()


def _f10_vol_state_atr(high, low, close, w):
    # ATR-style true range proxy (high-low) averaged over window
    rng = (high - low)
    return rng.rolling(w, min_periods=max(1, w // 2)).mean()


def _f10_vol_regime_zscore(close, w_vol, w_z):
    # zscore of rolling return-vol over a longer window
    v = _f10_vol_regime_retstd(close, w_vol)
    return _z(v, w_z)


# 21d EWMA volatility
def f10vr_f10_volatility_regime_ewmavol_21d_base_v076_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=21, min_periods=11, adjust=False).std()
    result = (base + _f10_vol_regime_retstd(closeadj, 21) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EWMA vol
def f10vr_f10_volatility_regime_ewmavol_63d_base_v077_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=63, min_periods=32, adjust=False).std()
    result = (base + _f10_vol_regime_retstd(closeadj, 63) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EWMA vol
def f10vr_f10_volatility_regime_ewmavol_252d_base_v078_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=252, min_periods=126, adjust=False).std()
    result = (base + _f10_vol_regime_retstd(closeadj, 252) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EWMA vol
def f10vr_f10_volatility_regime_ewmavol_504d_base_v079_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=504, min_periods=252, adjust=False).std()
    result = (base + _f10_vol_regime_retstd(closeadj, 504) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# GARCH-style EWMA squared returns 21d
def f10vr_f10_volatility_regime_garchproxy_21d_base_v080_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.ewm(span=21, min_periods=11, adjust=False).mean().pow(0.5)
    result = (base + _f10_vol_regime_retstd(closeadj, 21) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# GARCH-style 63d
def f10vr_f10_volatility_regime_garchproxy_63d_base_v081_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.ewm(span=63, min_periods=32, adjust=False).mean().pow(0.5)
    result = (base + _f10_vol_regime_retstd(closeadj, 63) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# GARCH-style 252d
def f10vr_f10_volatility_regime_garchproxy_252d_base_v082_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.ewm(span=252, min_periods=126, adjust=False).mean().pow(0.5)
    result = (base + _f10_vol_regime_retstd(closeadj, 252) * 0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol × volume mean
def f10vr_f10_volatility_regime_retvolxvolmean_21d_base_v083_signal(closeadj, volume):
    vm = _mean(volume, 21)
    result = _f10_vol_regime_retstd(closeadj, 21) * vm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol × volume mean
def f10vr_f10_volatility_regime_retvolxvolmean_63d_base_v084_signal(closeadj, volume):
    vm = _mean(volume, 63)
    result = _f10_vol_regime_retstd(closeadj, 63) * vm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol × volume mean
def f10vr_f10_volatility_regime_retvolxvolmean_252d_base_v085_signal(closeadj, volume):
    vm = _mean(volume, 252)
    result = _f10_vol_regime_retstd(closeadj, 252) * vm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol × dollar volume
def f10vr_f10_volatility_regime_retvolxdv_21d_base_v086_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f10_vol_regime_retstd(closeadj, 21) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol × dollar volume
def f10vr_f10_volatility_regime_retvolxdv_63d_base_v087_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f10_vol_regime_retstd(closeadj, 63) * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol × dollar volume mean
def f10vr_f10_volatility_regime_retvolxdv_252d_base_v088_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f10_vol_regime_retstd(closeadj, 252) * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol × volume z
def f10vr_f10_volatility_regime_retvolxvolz_21d_base_v089_signal(closeadj, volume):
    result = _f10_vol_regime_retstd(closeadj, 21) * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol × volume z
def f10vr_f10_volatility_regime_retvolxvolz_63d_base_v090_signal(closeadj, volume):
    result = _f10_vol_regime_retstd(closeadj, 63) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol × volume z
def f10vr_f10_volatility_regime_retvolxvolz_252d_base_v091_signal(closeadj, volume):
    result = _f10_vol_regime_retstd(closeadj, 252) * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR × dollar volume
def f10vr_f10_volatility_regime_atrxdv_21d_base_v092_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    dv = closeadj * volume
    result = atr * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR × dollar volume
def f10vr_f10_volatility_regime_atrxdv_63d_base_v093_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    dv = closeadj * volume
    result = atr * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ATR × dollar volume mean
def f10vr_f10_volatility_regime_atrxdv_252d_base_v094_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 252)
    dv = closeadj * volume
    result = atr * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol × 21d return
def f10vr_f10_volatility_regime_retvolxret_21d_base_v095_signal(closeadj):
    r = closeadj.pct_change(21)
    result = _f10_vol_regime_retstd(closeadj, 21) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol × 63d return
def f10vr_f10_volatility_regime_retvolxret_63d_base_v096_signal(closeadj):
    r = closeadj.pct_change(63)
    result = _f10_vol_regime_retstd(closeadj, 63) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol × 252d return
def f10vr_f10_volatility_regime_retvolxret_252d_base_v097_signal(closeadj):
    r = closeadj.pct_change(252)
    result = _f10_vol_regime_retstd(closeadj, 252) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol × abs return
def f10vr_f10_volatility_regime_retvolxabsret_21d_base_v098_signal(closeadj):
    ar = closeadj.pct_change().abs()
    result = _f10_vol_regime_retstd(closeadj, 21) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol × mean abs return
def f10vr_f10_volatility_regime_retvolxabsret_63d_base_v099_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 21)
    result = _f10_vol_regime_retstd(closeadj, 63) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol × mean abs return
def f10vr_f10_volatility_regime_retvolxabsret_252d_base_v100_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 63)
    result = _f10_vol_regime_retstd(closeadj, 252) * ar * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol × skew of returns
def f10vr_f10_volatility_regime_retvolxskew_63d_base_v101_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    result = _f10_vol_regime_retstd(closeadj, 63) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol × skew of returns
def f10vr_f10_volatility_regime_retvolxskew_252d_base_v102_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    result = _f10_vol_regime_retstd(closeadj, 252) * sk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol × kurt of returns
def f10vr_f10_volatility_regime_retvolxkurt_63d_base_v103_signal(closeadj):
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    result = _f10_vol_regime_retstd(closeadj, 63) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol × kurt of returns
def f10vr_f10_volatility_regime_retvolxkurt_252d_base_v104_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    result = _f10_vol_regime_retstd(closeadj, 252) * kt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR slope (ATR diff over 5d) normalized
def f10vr_f10_volatility_regime_atrslope_21d_base_v105_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    base = atr.diff(5) / atr.replace(0, np.nan).abs() + _f10_vol_state_atr(high, low, closeadj, 5) * 0.0
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR slope
def f10vr_f10_volatility_regime_atrslope_63d_base_v106_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    base = atr.diff(21) / atr.replace(0, np.nan).abs() + _f10_vol_state_atr(high, low, closeadj, 21) * 0.0
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ATR slope
def f10vr_f10_volatility_regime_atrslope_252d_base_v107_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 252)
    base = atr.diff(63) / atr.replace(0, np.nan).abs() + _f10_vol_state_atr(high, low, closeadj, 63) * 0.0
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol slope
def f10vr_f10_volatility_regime_retvolslope_21d_base_v108_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    base = v.diff(5) / v.replace(0, np.nan).abs()
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol slope
def f10vr_f10_volatility_regime_retvolslope_63d_base_v109_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    base = v.diff(21) / v.replace(0, np.nan).abs()
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol slope
def f10vr_f10_volatility_regime_retvolslope_252d_base_v110_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 252)
    base = v.diff(63) / v.replace(0, np.nan).abs()
    result = base * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol mean over 63d
def f10vr_f10_volatility_regime_retvolmean_63d_base_v111_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    result = _mean(v, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol mean over 252d
def f10vr_f10_volatility_regime_retvolmean_252d_base_v112_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    result = _mean(v, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol mean over 504d
def f10vr_f10_volatility_regime_retvolmean_252v504_base_v113_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 252)
    result = _mean(v, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol vs 63d ATR ratio
def f10vr_f10_volatility_regime_retvol_atrratio_21d_base_v114_signal(closeadj, high, low):
    v = _f10_vol_regime_retstd(closeadj, 21)
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    result = (v / atr.replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol vs 63d ATR ratio
def f10vr_f10_volatility_regime_retvol_atrratio_63d_base_v115_signal(closeadj, high, low):
    v = _f10_vol_regime_retstd(closeadj, 63)
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    result = (v / atr.replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol vs 252d ATR ratio
def f10vr_f10_volatility_regime_retvol_atrratio_252d_base_v116_signal(closeadj, high, low):
    v = _f10_vol_regime_retstd(closeadj, 252)
    atr = _f10_vol_state_atr(high, low, closeadj, 252)
    result = (v / atr.replace(0, np.nan)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# semi-deviation 21d (downside-only)
def f10vr_f10_volatility_regime_semidev_21d_base_v117_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 21)
    dev = (r - m).where(r < m, 0.0) ** 2
    result = dev.rolling(21, min_periods=5).mean().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# semi-deviation 63d
def f10vr_f10_volatility_regime_semidev_63d_base_v118_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 63)
    dev = (r - m).where(r < m, 0.0) ** 2
    result = dev.rolling(63, min_periods=21).mean().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# semi-deviation 252d
def f10vr_f10_volatility_regime_semidev_252d_base_v119_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 252)
    dev = (r - m).where(r < m, 0.0) ** 2
    result = dev.rolling(252, min_periods=63).mean().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Yang-Zhang variance proxy 21d
def f10vr_f10_volatility_regime_yangzhang_21d_base_v120_signal(closeadj, open, high, low):
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    op = np.log(open / closeadj.shift(1).replace(0, np.nan))
    rs = (np.log(high / closeadj.replace(0, np.nan)) * np.log(high / open.replace(0, np.nan))
          + np.log(low / closeadj.replace(0, np.nan)) * np.log(low / open.replace(0, np.nan)))
    sigma = (op.rolling(21, min_periods=5).var() + 0.34 * co.rolling(21, min_periods=5).var()
             + 0.66 * rs.rolling(21, min_periods=5).mean()).pow(0.5)
    result = sigma * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Yang-Zhang 63d
def f10vr_f10_volatility_regime_yangzhang_63d_base_v121_signal(closeadj, open, high, low):
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    op = np.log(open / closeadj.shift(1).replace(0, np.nan))
    rs = (np.log(high / closeadj.replace(0, np.nan)) * np.log(high / open.replace(0, np.nan))
          + np.log(low / closeadj.replace(0, np.nan)) * np.log(low / open.replace(0, np.nan)))
    sigma = (op.rolling(63, min_periods=21).var() + 0.34 * co.rolling(63, min_periods=21).var()
             + 0.66 * rs.rolling(63, min_periods=21).mean()).pow(0.5)
    result = sigma * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Yang-Zhang 252d
def f10vr_f10_volatility_regime_yangzhang_252d_base_v122_signal(closeadj, open, high, low):
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    op = np.log(open / closeadj.shift(1).replace(0, np.nan))
    rs = (np.log(high / closeadj.replace(0, np.nan)) * np.log(high / open.replace(0, np.nan))
          + np.log(low / closeadj.replace(0, np.nan)) * np.log(low / open.replace(0, np.nan)))
    sigma = (op.rolling(252, min_periods=63).var() + 0.34 * co.rolling(252, min_periods=63).var()
             + 0.66 * rs.rolling(252, min_periods=63).mean()).pow(0.5)
    result = sigma * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol percentile expanding
def f10vr_f10_volatility_regime_retvolpctexp_21d_base_v123_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    base = v.expanding(min_periods=63).rank(pct=True) + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol percentile expanding
def f10vr_f10_volatility_regime_retvolpctexp_63d_base_v124_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    base = v.expanding(min_periods=126).rank(pct=True) + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR slope × volume z
def f10vr_f10_volatility_regime_atrslopexvolz_21d_base_v125_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    base = atr.diff(5) / atr.replace(0, np.nan).abs()
    result = base * _z(volume, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR slope × volume z
def f10vr_f10_volatility_regime_atrslopexvolz_63d_base_v126_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    base = atr.diff(21) / atr.replace(0, np.nan).abs()
    result = base * _z(volume, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol × intraday range mean
def f10vr_f10_volatility_regime_retvolxrange_21d_base_v127_signal(closeadj, high, low):
    rng = _mean((high - low), 21)
    result = _f10_vol_regime_retstd(closeadj, 21) * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol × intraday range mean
def f10vr_f10_volatility_regime_retvolxrange_63d_base_v128_signal(closeadj, high, low):
    rng = _mean((high - low), 63)
    result = _f10_vol_regime_retstd(closeadj, 63) * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol × intraday range mean
def f10vr_f10_volatility_regime_retvolxrange_252d_base_v129_signal(closeadj, high, low):
    rng = _mean((high - low), 63)
    result = _f10_vol_regime_retstd(closeadj, 252) * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol × overnight gap z
def f10vr_f10_volatility_regime_retvolxocgapz_21d_base_v130_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    result = _f10_vol_regime_retstd(closeadj, 21) * _z(gap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol × gap mean
def f10vr_f10_volatility_regime_retvolxocgapmean_63d_base_v131_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    result = _f10_vol_regime_retstd(closeadj, 63) * _mean(gap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol × gap mean
def f10vr_f10_volatility_regime_retvolxocgapmean_252d_base_v132_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    result = _f10_vol_regime_retstd(closeadj, 252) * _mean(gap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol vs 63d retvol × close (cross-window vol regime)
def f10vr_f10_volatility_regime_retvol_diffx_21v63_base_v133_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 21)
    b = _f10_vol_regime_retstd(closeadj, 63)
    result = (a - b) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d - 252d retvol × close
def f10vr_f10_volatility_regime_retvol_diffx_63v252_base_v134_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 63)
    b = _f10_vol_regime_retstd(closeadj, 252)
    result = (a - b) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d - 504d retvol × close
def f10vr_f10_volatility_regime_retvol_diffx_252v504_base_v135_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 252)
    b = _f10_vol_regime_retstd(closeadj, 504)
    result = (a - b) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR ratio z over 252d
def f10vr_f10_volatility_regime_atrratioz_252d_base_v136_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    rr = atr / closeadj.replace(0, np.nan)
    result = _z(rr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR ratio z over 504d
def f10vr_f10_volatility_regime_atrratioz_504d_base_v137_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    rr = atr / closeadj.replace(0, np.nan)
    result = _z(rr, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d down-day count over 21d (vol regime via dispersion)
def f10vr_f10_volatility_regime_downdays_21d_base_v138_signal(closeadj):
    r = closeadj.pct_change()
    flag = (r.abs() > _f10_vol_regime_retstd(closeadj, 21)).astype(float)
    result = flag.rolling(21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of large-move days
def f10vr_f10_volatility_regime_downdays_63d_base_v139_signal(closeadj):
    r = closeadj.pct_change()
    flag = (r.abs() > _f10_vol_regime_retstd(closeadj, 63)).astype(float)
    result = flag.rolling(63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of large-move days
def f10vr_f10_volatility_regime_downdays_252d_base_v140_signal(closeadj):
    r = closeadj.pct_change()
    flag = (r.abs() > _f10_vol_regime_retstd(closeadj, 252)).astype(float)
    result = flag.rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d realized variance (sum of squared returns)
def f10vr_f10_volatility_regime_realvar_21d_base_v141_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    result = r2.rolling(21, min_periods=5).sum() * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d realized variance
def f10vr_f10_volatility_regime_realvar_63d_base_v142_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    result = r2.rolling(63, min_periods=21).sum() * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d realized variance
def f10vr_f10_volatility_regime_realvar_252d_base_v143_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    result = r2.rolling(252, min_periods=63).sum() * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d realized variance
def f10vr_f10_volatility_regime_realvar_504d_base_v144_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    result = r2.rolling(504, min_periods=126).sum() * closeadj + _f10_vol_regime_retstd(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol × volume change
def f10vr_f10_volatility_regime_retvolxvolch_21d_base_v145_signal(closeadj, volume):
    vc = volume.pct_change(21)
    result = _f10_vol_regime_retstd(closeadj, 21) * vc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol × volume change
def f10vr_f10_volatility_regime_retvolxvolch_63d_base_v146_signal(closeadj, volume):
    vc = volume.pct_change(63)
    result = _f10_vol_regime_retstd(closeadj, 63) * vc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol × volume change
def f10vr_f10_volatility_regime_retvolxvolch_252d_base_v147_signal(closeadj, volume):
    vc = volume.pct_change(252)
    result = _f10_vol_regime_retstd(closeadj, 252) * vc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite vol regime: 21d retvol + 21d ATR
def f10vr_f10_volatility_regime_composite_21d_base_v148_signal(closeadj, high, low):
    a = _f10_vol_regime_retstd(closeadj, 21) * closeadj
    b = _f10_vol_state_atr(high, low, closeadj, 21)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite vol: 63d retvol + 63d ATR
def f10vr_f10_volatility_regime_composite_63d_base_v149_signal(closeadj, high, low):
    a = _f10_vol_regime_retstd(closeadj, 63) * closeadj
    b = _f10_vol_state_atr(high, low, closeadj, 63)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite vol: 252d retvol + 252d ATR
def f10vr_f10_volatility_regime_composite_252d_base_v150_signal(closeadj, high, low):
    a = _f10_vol_regime_retstd(closeadj, 252) * closeadj
    b = _f10_vol_state_atr(high, low, closeadj, 252)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10vr_f10_volatility_regime_ewmavol_21d_base_v076_signal,
    f10vr_f10_volatility_regime_ewmavol_63d_base_v077_signal,
    f10vr_f10_volatility_regime_ewmavol_252d_base_v078_signal,
    f10vr_f10_volatility_regime_ewmavol_504d_base_v079_signal,
    f10vr_f10_volatility_regime_garchproxy_21d_base_v080_signal,
    f10vr_f10_volatility_regime_garchproxy_63d_base_v081_signal,
    f10vr_f10_volatility_regime_garchproxy_252d_base_v082_signal,
    f10vr_f10_volatility_regime_retvolxvolmean_21d_base_v083_signal,
    f10vr_f10_volatility_regime_retvolxvolmean_63d_base_v084_signal,
    f10vr_f10_volatility_regime_retvolxvolmean_252d_base_v085_signal,
    f10vr_f10_volatility_regime_retvolxdv_21d_base_v086_signal,
    f10vr_f10_volatility_regime_retvolxdv_63d_base_v087_signal,
    f10vr_f10_volatility_regime_retvolxdv_252d_base_v088_signal,
    f10vr_f10_volatility_regime_retvolxvolz_21d_base_v089_signal,
    f10vr_f10_volatility_regime_retvolxvolz_63d_base_v090_signal,
    f10vr_f10_volatility_regime_retvolxvolz_252d_base_v091_signal,
    f10vr_f10_volatility_regime_atrxdv_21d_base_v092_signal,
    f10vr_f10_volatility_regime_atrxdv_63d_base_v093_signal,
    f10vr_f10_volatility_regime_atrxdv_252d_base_v094_signal,
    f10vr_f10_volatility_regime_retvolxret_21d_base_v095_signal,
    f10vr_f10_volatility_regime_retvolxret_63d_base_v096_signal,
    f10vr_f10_volatility_regime_retvolxret_252d_base_v097_signal,
    f10vr_f10_volatility_regime_retvolxabsret_21d_base_v098_signal,
    f10vr_f10_volatility_regime_retvolxabsret_63d_base_v099_signal,
    f10vr_f10_volatility_regime_retvolxabsret_252d_base_v100_signal,
    f10vr_f10_volatility_regime_retvolxskew_63d_base_v101_signal,
    f10vr_f10_volatility_regime_retvolxskew_252d_base_v102_signal,
    f10vr_f10_volatility_regime_retvolxkurt_63d_base_v103_signal,
    f10vr_f10_volatility_regime_retvolxkurt_252d_base_v104_signal,
    f10vr_f10_volatility_regime_atrslope_21d_base_v105_signal,
    f10vr_f10_volatility_regime_atrslope_63d_base_v106_signal,
    f10vr_f10_volatility_regime_atrslope_252d_base_v107_signal,
    f10vr_f10_volatility_regime_retvolslope_21d_base_v108_signal,
    f10vr_f10_volatility_regime_retvolslope_63d_base_v109_signal,
    f10vr_f10_volatility_regime_retvolslope_252d_base_v110_signal,
    f10vr_f10_volatility_regime_retvolmean_63d_base_v111_signal,
    f10vr_f10_volatility_regime_retvolmean_252d_base_v112_signal,
    f10vr_f10_volatility_regime_retvolmean_252v504_base_v113_signal,
    f10vr_f10_volatility_regime_retvol_atrratio_21d_base_v114_signal,
    f10vr_f10_volatility_regime_retvol_atrratio_63d_base_v115_signal,
    f10vr_f10_volatility_regime_retvol_atrratio_252d_base_v116_signal,
    f10vr_f10_volatility_regime_semidev_21d_base_v117_signal,
    f10vr_f10_volatility_regime_semidev_63d_base_v118_signal,
    f10vr_f10_volatility_regime_semidev_252d_base_v119_signal,
    f10vr_f10_volatility_regime_yangzhang_21d_base_v120_signal,
    f10vr_f10_volatility_regime_yangzhang_63d_base_v121_signal,
    f10vr_f10_volatility_regime_yangzhang_252d_base_v122_signal,
    f10vr_f10_volatility_regime_retvolpctexp_21d_base_v123_signal,
    f10vr_f10_volatility_regime_retvolpctexp_63d_base_v124_signal,
    f10vr_f10_volatility_regime_atrslopexvolz_21d_base_v125_signal,
    f10vr_f10_volatility_regime_atrslopexvolz_63d_base_v126_signal,
    f10vr_f10_volatility_regime_retvolxrange_21d_base_v127_signal,
    f10vr_f10_volatility_regime_retvolxrange_63d_base_v128_signal,
    f10vr_f10_volatility_regime_retvolxrange_252d_base_v129_signal,
    f10vr_f10_volatility_regime_retvolxocgapz_21d_base_v130_signal,
    f10vr_f10_volatility_regime_retvolxocgapmean_63d_base_v131_signal,
    f10vr_f10_volatility_regime_retvolxocgapmean_252d_base_v132_signal,
    f10vr_f10_volatility_regime_retvol_diffx_21v63_base_v133_signal,
    f10vr_f10_volatility_regime_retvol_diffx_63v252_base_v134_signal,
    f10vr_f10_volatility_regime_retvol_diffx_252v504_base_v135_signal,
    f10vr_f10_volatility_regime_atrratioz_252d_base_v136_signal,
    f10vr_f10_volatility_regime_atrratioz_504d_base_v137_signal,
    f10vr_f10_volatility_regime_downdays_21d_base_v138_signal,
    f10vr_f10_volatility_regime_downdays_63d_base_v139_signal,
    f10vr_f10_volatility_regime_downdays_252d_base_v140_signal,
    f10vr_f10_volatility_regime_realvar_21d_base_v141_signal,
    f10vr_f10_volatility_regime_realvar_63d_base_v142_signal,
    f10vr_f10_volatility_regime_realvar_252d_base_v143_signal,
    f10vr_f10_volatility_regime_realvar_504d_base_v144_signal,
    f10vr_f10_volatility_regime_retvolxvolch_21d_base_v145_signal,
    f10vr_f10_volatility_regime_retvolxvolch_63d_base_v146_signal,
    f10vr_f10_volatility_regime_retvolxvolch_252d_base_v147_signal,
    f10vr_f10_volatility_regime_composite_21d_base_v148_signal,
    f10vr_f10_volatility_regime_composite_63d_base_v149_signal,
    f10vr_f10_volatility_regime_composite_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_VOLATILITY_REGIME_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f10_vol_regime_retstd", "_f10_vol_state_atr", "_f10_vol_regime_zscore")
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
    print(f"OK f10_volatility_regime_base_076_150_claude: {n_features} features pass")
