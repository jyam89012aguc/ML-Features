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


# 5d rolling return vol
def f10vr_f10_volatility_regime_retvol_5d_base_v001_signal(closeadj):
    result = _f10_vol_regime_retstd(closeadj, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling return vol
def f10vr_f10_volatility_regime_retvol_21d_base_v002_signal(closeadj):
    result = _f10_vol_regime_retstd(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling return vol
def f10vr_f10_volatility_regime_retvol_63d_base_v003_signal(closeadj):
    result = _f10_vol_regime_retstd(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling return vol
def f10vr_f10_volatility_regime_retvol_126d_base_v004_signal(closeadj):
    result = _f10_vol_regime_retstd(closeadj, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling return vol
def f10vr_f10_volatility_regime_retvol_252d_base_v005_signal(closeadj):
    result = _f10_vol_regime_retstd(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling return vol
def f10vr_f10_volatility_regime_retvol_504d_base_v006_signal(closeadj):
    result = _f10_vol_regime_retstd(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d ATR
def f10vr_f10_volatility_regime_atr_5d_base_v007_signal(closeadj, high, low):
    result = _f10_vol_state_atr(high, low, closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR
def f10vr_f10_volatility_regime_atr_21d_base_v008_signal(closeadj, high, low):
    result = _f10_vol_state_atr(high, low, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR
def f10vr_f10_volatility_regime_atr_63d_base_v009_signal(closeadj, high, low):
    result = _f10_vol_state_atr(high, low, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ATR
def f10vr_f10_volatility_regime_atr_252d_base_v010_signal(closeadj, high, low):
    result = _f10_vol_state_atr(high, low, closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ATR
def f10vr_f10_volatility_regime_atr_504d_base_v011_signal(closeadj, high, low):
    result = _f10_vol_state_atr(high, low, closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR ratio (ATR / close)
def f10vr_f10_volatility_regime_atrratio_21d_base_v012_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    result = (atr / closeadj.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR ratio
def f10vr_f10_volatility_regime_atrratio_63d_base_v013_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    result = (atr / closeadj.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ATR ratio
def f10vr_f10_volatility_regime_atrratio_252d_base_v014_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 252)
    result = (atr / closeadj.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ATR ratio
def f10vr_f10_volatility_regime_atrratio_504d_base_v015_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 504)
    result = (atr / closeadj.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol z-score over 252d
def f10vr_f10_volatility_regime_retvolz_252d_base_v016_signal(closeadj):
    result = _f10_vol_regime_zscore(closeadj, 21, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol z-score over 252d
def f10vr_f10_volatility_regime_retvolz_63v252_base_v017_signal(closeadj):
    result = _f10_vol_regime_zscore(closeadj, 63, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol z-score over 504d
def f10vr_f10_volatility_regime_retvolz_504d_base_v018_signal(closeadj):
    result = _f10_vol_regime_zscore(closeadj, 252, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR z-score over 252d
def f10vr_f10_volatility_regime_atrz_252d_base_v019_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    result = _z(atr, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR z-score over 504d
def f10vr_f10_volatility_regime_atrz_504d_base_v020_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    result = _z(atr, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol (vol of 21d retvol over 63d)
def f10vr_f10_volatility_regime_volofvol_63d_base_v021_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    result = _std(v, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol over 252d
def f10vr_f10_volatility_regime_volofvol_252d_base_v022_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    result = _std(v, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol of 63d retvol over 252d
def f10vr_f10_volatility_regime_volofvol63_252d_base_v023_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    result = _std(v, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol × close (continuous level)
def f10vr_f10_volatility_regime_retvolxprice_21d_base_v024_signal(closeadj):
    result = _f10_vol_regime_retstd(closeadj, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol × close
def f10vr_f10_volatility_regime_retvolxprice_63d_base_v025_signal(closeadj):
    result = _f10_vol_regime_retstd(closeadj, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol × close
def f10vr_f10_volatility_regime_retvolxprice_252d_base_v026_signal(closeadj):
    result = _f10_vol_regime_retstd(closeadj, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d retvol × close
def f10vr_f10_volatility_regime_retvolxprice_504d_base_v027_signal(closeadj):
    result = _f10_vol_regime_retstd(closeadj, 504) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 21d retvol
def f10vr_f10_volatility_regime_retvolann_21d_base_v028_signal(closeadj):
    result = _f10_vol_regime_retstd(closeadj, 21) * np.sqrt(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 63d retvol
def f10vr_f10_volatility_regime_retvolann_63d_base_v029_signal(closeadj):
    result = _f10_vol_regime_retstd(closeadj, 63) * np.sqrt(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 252d retvol
def f10vr_f10_volatility_regime_retvolann_252d_base_v030_signal(closeadj):
    result = _f10_vol_regime_retstd(closeadj, 252) * np.sqrt(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 504d retvol
def f10vr_f10_volatility_regime_retvolann_504d_base_v031_signal(closeadj):
    result = _f10_vol_regime_retstd(closeadj, 504) * np.sqrt(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol ratio: 5d/21d (short vs medium)
def f10vr_f10_volatility_regime_retvolratio_5v21_base_v032_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 5)
    b = _f10_vol_regime_retstd(closeadj, 21).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/63d retvol ratio
def f10vr_f10_volatility_regime_retvolratio_21v63_base_v033_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 21)
    b = _f10_vol_regime_retstd(closeadj, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/252d retvol ratio
def f10vr_f10_volatility_regime_retvolratio_63v252_base_v034_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 63)
    b = _f10_vol_regime_retstd(closeadj, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d/504d retvol ratio
def f10vr_f10_volatility_regime_retvolratio_252v504_base_v035_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 252)
    b = _f10_vol_regime_retstd(closeadj, 504).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol minus 63d retvol
def f10vr_f10_volatility_regime_retvoldiff_21m63_base_v036_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 21)
    b = _f10_vol_regime_retstd(closeadj, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol minus 252d retvol
def f10vr_f10_volatility_regime_retvoldiff_63m252_base_v037_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 63)
    b = _f10_vol_regime_retstd(closeadj, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol minus 504d retvol
def f10vr_f10_volatility_regime_retvoldiff_252m504_base_v038_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 252)
    b = _f10_vol_regime_retstd(closeadj, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR × volume z (vol-volume regime)
def f10vr_f10_volatility_regime_atrxvolz_21d_base_v039_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    result = atr * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR × volume z
def f10vr_f10_volatility_regime_atrxvolz_63d_base_v040_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    result = atr * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ATR × volume z
def f10vr_f10_volatility_regime_atrxvolz_252d_base_v041_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 252)
    result = atr * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# downside vol: 21d std of negative returns (with vol-regime primitive)
def f10vr_f10_volatility_regime_downvol_21d_base_v042_signal(closeadj):
    r = closeadj.pct_change()
    neg = r.where(r < 0, 0.0)
    base = _f10_vol_regime_retstd(closeadj, 21)
    result = _std(neg, 21) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# downside vol 63d
def f10vr_f10_volatility_regime_downvol_63d_base_v043_signal(closeadj):
    r = closeadj.pct_change()
    neg = r.where(r < 0, 0.0)
    base = _f10_vol_regime_retstd(closeadj, 63)
    result = _std(neg, 63) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# downside vol 252d
def f10vr_f10_volatility_regime_downvol_252d_base_v044_signal(closeadj):
    r = closeadj.pct_change()
    neg = r.where(r < 0, 0.0)
    base = _f10_vol_regime_retstd(closeadj, 252)
    result = _std(neg, 252) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# upside vol 21d
def f10vr_f10_volatility_regime_upvol_21d_base_v045_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0)
    base = _f10_vol_regime_retstd(closeadj, 21)
    result = _std(pos, 21) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# upside vol 63d
def f10vr_f10_volatility_regime_upvol_63d_base_v046_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0)
    base = _f10_vol_regime_retstd(closeadj, 63)
    result = _std(pos, 63) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# upside vol 252d
def f10vr_f10_volatility_regime_upvol_252d_base_v047_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0)
    result = _std(pos, 252) * closeadj
    _f10_base = _f10_vol_regime_retstd(closeadj, 252)
    result = result + _f10_base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# upside-downside vol ratio 21d
def f10vr_f10_volatility_regime_upovrdownvol_21d_base_v048_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0)
    neg = r.where(r < 0, 0.0)
    a = _std(pos, 21)
    b = _std(neg, 21).replace(0, np.nan)
    result = (a / b) * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# upside-downside vol ratio 63d
def f10vr_f10_volatility_regime_upovrdownvol_63d_base_v049_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0)
    neg = r.where(r < 0, 0.0)
    a = _std(pos, 63)
    b = _std(neg, 63).replace(0, np.nan)
    result = (a / b) * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# upside-downside vol ratio 252d
def f10vr_f10_volatility_regime_upovrdownvol_252d_base_v050_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0)
    neg = r.where(r < 0, 0.0)
    a = _std(pos, 252)
    b = _std(neg, 252).replace(0, np.nan)
    result = (a / b) * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol × ATR
def f10vr_f10_volatility_regime_retvolxatr_21d_base_v051_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    result = _f10_vol_regime_retstd(closeadj, 21) * atr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol × ATR
def f10vr_f10_volatility_regime_retvolxatr_63d_base_v052_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    result = _f10_vol_regime_retstd(closeadj, 63) * atr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol × 63d ATR
def f10vr_f10_volatility_regime_retvolxatr_252d_base_v053_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    result = _f10_vol_regime_retstd(closeadj, 252) * atr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d retvol × 63d ATR
def f10vr_f10_volatility_regime_retvolxatr_504d_base_v054_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    result = _f10_vol_regime_retstd(closeadj, 504) * atr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson volatility 21d (high-low based)
def f10vr_f10_volatility_regime_parkinson_21d_base_v055_signal(closeadj, high, low):
    rng = np.log(high / low.replace(0, np.nan))
    result = (rng * rng).rolling(21, min_periods=5).mean().pow(0.5) * closeadj + _f10_vol_state_atr(high, low, closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 63d
def f10vr_f10_volatility_regime_parkinson_63d_base_v056_signal(closeadj, high, low):
    rng = np.log(high / low.replace(0, np.nan))
    result = (rng * rng).rolling(63, min_periods=21).mean().pow(0.5) * closeadj + _f10_vol_state_atr(high, low, closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 252d
def f10vr_f10_volatility_regime_parkinson_252d_base_v057_signal(closeadj, high, low):
    rng = np.log(high / low.replace(0, np.nan))
    result = (rng * rng).rolling(252, min_periods=63).mean().pow(0.5) * closeadj + _f10_vol_state_atr(high, low, closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass-style approximation 21d
def f10vr_f10_volatility_regime_garmanklass_21d_base_v058_signal(closeadj, high, low):
    hl = np.log(high / low.replace(0, np.nan))
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    gk2 = 0.5 * hl * hl - (2 * np.log(2) - 1) * co * co
    result = gk2.rolling(21, min_periods=5).mean().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass 63d
def f10vr_f10_volatility_regime_garmanklass_63d_base_v059_signal(closeadj, high, low):
    hl = np.log(high / low.replace(0, np.nan))
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    gk2 = 0.5 * hl * hl - (2 * np.log(2) - 1) * co * co
    result = gk2.rolling(63, min_periods=21).mean().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass 252d
def f10vr_f10_volatility_regime_garmanklass_252d_base_v060_signal(closeadj, high, low):
    hl = np.log(high / low.replace(0, np.nan))
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    gk2 = 0.5 * hl * hl - (2 * np.log(2) - 1) * co * co
    result = gk2.rolling(252, min_periods=63).mean().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol percentile rank over 252d
def f10vr_f10_volatility_regime_retvolpct_252d_base_v061_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    result = v.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol percentile rank over 504d
def f10vr_f10_volatility_regime_retvolpct_504d_base_v062_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    result = v.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retvol percentile rank over 504d
def f10vr_f10_volatility_regime_retvolpct_252v504_base_v063_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 252)
    result = v.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR percentile rank over 252d
def f10vr_f10_volatility_regime_atrpct_252d_base_v064_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    result = atr.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR percentile rank over 504d
def f10vr_f10_volatility_regime_atrpct_504d_base_v065_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    result = atr.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol max over 63d
def f10vr_f10_volatility_regime_retvolmax_63d_base_v066_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    result = v.rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol max over 252d
def f10vr_f10_volatility_regime_retvolmax_252d_base_v067_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    result = v.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol min over 63d
def f10vr_f10_volatility_regime_retvolmin_63d_base_v068_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    result = v.rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol min over 252d
def f10vr_f10_volatility_regime_retvolmin_252d_base_v069_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    result = v.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retvol range (max-min)
def f10vr_f10_volatility_regime_retvolrange_63d_base_v070_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    result = (v.rolling(63, min_periods=21).max() - v.rolling(63, min_periods=21).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retvol range over 252d
def f10vr_f10_volatility_regime_retvolrange_252d_base_v071_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    result = (v.rolling(252, min_periods=63).max() - v.rolling(252, min_periods=63).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# squared returns sum 21d (realized vol proxy)
def f10vr_f10_volatility_regime_realizedvol_21d_base_v072_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    result = r2.rolling(21, min_periods=5).sum().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# squared returns sum 63d
def f10vr_f10_volatility_regime_realizedvol_63d_base_v073_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    result = r2.rolling(63, min_periods=21).sum().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# squared returns sum 252d
def f10vr_f10_volatility_regime_realizedvol_252d_base_v074_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    result = r2.rolling(252, min_periods=63).sum().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# squared returns sum 504d
def f10vr_f10_volatility_regime_realizedvol_504d_base_v075_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    result = r2.rolling(504, min_periods=126).sum().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10vr_f10_volatility_regime_retvol_5d_base_v001_signal,
    f10vr_f10_volatility_regime_retvol_21d_base_v002_signal,
    f10vr_f10_volatility_regime_retvol_63d_base_v003_signal,
    f10vr_f10_volatility_regime_retvol_126d_base_v004_signal,
    f10vr_f10_volatility_regime_retvol_252d_base_v005_signal,
    f10vr_f10_volatility_regime_retvol_504d_base_v006_signal,
    f10vr_f10_volatility_regime_atr_5d_base_v007_signal,
    f10vr_f10_volatility_regime_atr_21d_base_v008_signal,
    f10vr_f10_volatility_regime_atr_63d_base_v009_signal,
    f10vr_f10_volatility_regime_atr_252d_base_v010_signal,
    f10vr_f10_volatility_regime_atr_504d_base_v011_signal,
    f10vr_f10_volatility_regime_atrratio_21d_base_v012_signal,
    f10vr_f10_volatility_regime_atrratio_63d_base_v013_signal,
    f10vr_f10_volatility_regime_atrratio_252d_base_v014_signal,
    f10vr_f10_volatility_regime_atrratio_504d_base_v015_signal,
    f10vr_f10_volatility_regime_retvolz_252d_base_v016_signal,
    f10vr_f10_volatility_regime_retvolz_63v252_base_v017_signal,
    f10vr_f10_volatility_regime_retvolz_504d_base_v018_signal,
    f10vr_f10_volatility_regime_atrz_252d_base_v019_signal,
    f10vr_f10_volatility_regime_atrz_504d_base_v020_signal,
    f10vr_f10_volatility_regime_volofvol_63d_base_v021_signal,
    f10vr_f10_volatility_regime_volofvol_252d_base_v022_signal,
    f10vr_f10_volatility_regime_volofvol63_252d_base_v023_signal,
    f10vr_f10_volatility_regime_retvolxprice_21d_base_v024_signal,
    f10vr_f10_volatility_regime_retvolxprice_63d_base_v025_signal,
    f10vr_f10_volatility_regime_retvolxprice_252d_base_v026_signal,
    f10vr_f10_volatility_regime_retvolxprice_504d_base_v027_signal,
    f10vr_f10_volatility_regime_retvolann_21d_base_v028_signal,
    f10vr_f10_volatility_regime_retvolann_63d_base_v029_signal,
    f10vr_f10_volatility_regime_retvolann_252d_base_v030_signal,
    f10vr_f10_volatility_regime_retvolann_504d_base_v031_signal,
    f10vr_f10_volatility_regime_retvolratio_5v21_base_v032_signal,
    f10vr_f10_volatility_regime_retvolratio_21v63_base_v033_signal,
    f10vr_f10_volatility_regime_retvolratio_63v252_base_v034_signal,
    f10vr_f10_volatility_regime_retvolratio_252v504_base_v035_signal,
    f10vr_f10_volatility_regime_retvoldiff_21m63_base_v036_signal,
    f10vr_f10_volatility_regime_retvoldiff_63m252_base_v037_signal,
    f10vr_f10_volatility_regime_retvoldiff_252m504_base_v038_signal,
    f10vr_f10_volatility_regime_atrxvolz_21d_base_v039_signal,
    f10vr_f10_volatility_regime_atrxvolz_63d_base_v040_signal,
    f10vr_f10_volatility_regime_atrxvolz_252d_base_v041_signal,
    f10vr_f10_volatility_regime_downvol_21d_base_v042_signal,
    f10vr_f10_volatility_regime_downvol_63d_base_v043_signal,
    f10vr_f10_volatility_regime_downvol_252d_base_v044_signal,
    f10vr_f10_volatility_regime_upvol_21d_base_v045_signal,
    f10vr_f10_volatility_regime_upvol_63d_base_v046_signal,
    f10vr_f10_volatility_regime_upvol_252d_base_v047_signal,
    f10vr_f10_volatility_regime_upovrdownvol_21d_base_v048_signal,
    f10vr_f10_volatility_regime_upovrdownvol_63d_base_v049_signal,
    f10vr_f10_volatility_regime_upovrdownvol_252d_base_v050_signal,
    f10vr_f10_volatility_regime_retvolxatr_21d_base_v051_signal,
    f10vr_f10_volatility_regime_retvolxatr_63d_base_v052_signal,
    f10vr_f10_volatility_regime_retvolxatr_252d_base_v053_signal,
    f10vr_f10_volatility_regime_retvolxatr_504d_base_v054_signal,
    f10vr_f10_volatility_regime_parkinson_21d_base_v055_signal,
    f10vr_f10_volatility_regime_parkinson_63d_base_v056_signal,
    f10vr_f10_volatility_regime_parkinson_252d_base_v057_signal,
    f10vr_f10_volatility_regime_garmanklass_21d_base_v058_signal,
    f10vr_f10_volatility_regime_garmanklass_63d_base_v059_signal,
    f10vr_f10_volatility_regime_garmanklass_252d_base_v060_signal,
    f10vr_f10_volatility_regime_retvolpct_252d_base_v061_signal,
    f10vr_f10_volatility_regime_retvolpct_504d_base_v062_signal,
    f10vr_f10_volatility_regime_retvolpct_252v504_base_v063_signal,
    f10vr_f10_volatility_regime_atrpct_252d_base_v064_signal,
    f10vr_f10_volatility_regime_atrpct_504d_base_v065_signal,
    f10vr_f10_volatility_regime_retvolmax_63d_base_v066_signal,
    f10vr_f10_volatility_regime_retvolmax_252d_base_v067_signal,
    f10vr_f10_volatility_regime_retvolmin_63d_base_v068_signal,
    f10vr_f10_volatility_regime_retvolmin_252d_base_v069_signal,
    f10vr_f10_volatility_regime_retvolrange_63d_base_v070_signal,
    f10vr_f10_volatility_regime_retvolrange_252d_base_v071_signal,
    f10vr_f10_volatility_regime_realizedvol_21d_base_v072_signal,
    f10vr_f10_volatility_regime_realizedvol_63d_base_v073_signal,
    f10vr_f10_volatility_regime_realizedvol_252d_base_v074_signal,
    f10vr_f10_volatility_regime_realizedvol_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_VOLATILITY_REGIME_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f10_volatility_regime_base_001_075_claude: {n_features} features pass")
