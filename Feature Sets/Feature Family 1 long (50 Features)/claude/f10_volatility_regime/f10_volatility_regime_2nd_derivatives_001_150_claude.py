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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


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


# 5d slope of 5d retvol
def f10vr_f10_volatility_regime_retvol_5d_slope_v001_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d retvol
def f10vr_f10_volatility_regime_retvol_21d_slope_v002_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d retvol (variant)
def f10vr_f10_volatility_regime_retvol_21d_slope_v003_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d retvol
def f10vr_f10_volatility_regime_retvol_63d_slope_v004_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d retvol
def f10vr_f10_volatility_regime_retvol_63d_slope_v005_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d retvol
def f10vr_f10_volatility_regime_retvol_126d_slope_v006_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d retvol
def f10vr_f10_volatility_regime_retvol_126d_slope_v007_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d retvol
def f10vr_f10_volatility_regime_retvol_252d_slope_v008_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d retvol
def f10vr_f10_volatility_regime_retvol_252d_slope_v009_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d retvol
def f10vr_f10_volatility_regime_retvol_252d_slope_v010_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d retvol
def f10vr_f10_volatility_regime_retvol_504d_slope_v011_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d retvol
def f10vr_f10_volatility_regime_retvol_504d_slope_v012_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 504) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d ATR
def f10vr_f10_volatility_regime_atr_5d_slope_v013_signal(closeadj, high, low):
    base = _f10_vol_state_atr(high, low, closeadj, 5)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ATR
def f10vr_f10_volatility_regime_atr_21d_slope_v014_signal(closeadj, high, low):
    base = _f10_vol_state_atr(high, low, closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ATR
def f10vr_f10_volatility_regime_atr_63d_slope_v015_signal(closeadj, high, low):
    base = _f10_vol_state_atr(high, low, closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ATR
def f10vr_f10_volatility_regime_atr_252d_slope_v016_signal(closeadj, high, low):
    base = _f10_vol_state_atr(high, low, closeadj, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d ATR
def f10vr_f10_volatility_regime_atr_504d_slope_v017_signal(closeadj, high, low):
    base = _f10_vol_state_atr(high, low, closeadj, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ATR ratio
def f10vr_f10_volatility_regime_atrratio_21d_slope_v018_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    base = (atr / closeadj.replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ATR ratio
def f10vr_f10_volatility_regime_atrratio_63d_slope_v019_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    base = (atr / closeadj.replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ATR ratio
def f10vr_f10_volatility_regime_atrratio_252d_slope_v020_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 252)
    base = (atr / closeadj.replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d ATR ratio
def f10vr_f10_volatility_regime_atrratio_504d_slope_v021_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 504)
    base = (atr / closeadj.replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol z-score
def f10vr_f10_volatility_regime_retvolz_252d_slope_v022_signal(closeadj):
    base = _f10_vol_regime_zscore(closeadj, 21, 252) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63v252 retvol z
def f10vr_f10_volatility_regime_retvolz_63v252_slope_v023_signal(closeadj):
    base = _f10_vol_regime_zscore(closeadj, 63, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d retvol z over 504d
def f10vr_f10_volatility_regime_retvolz_504d_slope_v024_signal(closeadj):
    base = _f10_vol_regime_zscore(closeadj, 252, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ATR z
def f10vr_f10_volatility_regime_atrz_252d_slope_v025_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    base = _z(atr, 252) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ATR z
def f10vr_f10_volatility_regime_atrz_504d_slope_v026_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    base = _z(atr, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of vol-of-vol 63d
def f10vr_f10_volatility_regime_volofvol_63d_slope_v027_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    base = _std(v, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vol-of-vol 252d
def f10vr_f10_volatility_regime_volofvol_252d_slope_v028_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    base = _std(v, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of vol-of-vol of 63d retvol
def f10vr_f10_volatility_regime_volofvol63_252d_slope_v029_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    base = _std(v, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol×price (21d)
def f10vr_f10_volatility_regime_retvolxprice_21d_slope_v030_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 21) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol×price (63d)
def f10vr_f10_volatility_regime_retvolxprice_63d_slope_v031_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 63) * closeadj * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol×price (252d)
def f10vr_f10_volatility_regime_retvolxprice_252d_slope_v032_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 252) * closeadj * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of retvol×price (504d)
def f10vr_f10_volatility_regime_retvolxprice_504d_slope_v033_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 504) * closeadj * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of annualized 21d retvol
def f10vr_f10_volatility_regime_retvolann_21d_slope_v034_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 21) * np.sqrt(252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of annualized 63d retvol
def f10vr_f10_volatility_regime_retvolann_63d_slope_v035_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 63) * np.sqrt(252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of annualized 252d retvol
def f10vr_f10_volatility_regime_retvolann_252d_slope_v036_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 252) * np.sqrt(252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of annualized 504d retvol
def f10vr_f10_volatility_regime_retvolann_504d_slope_v037_signal(closeadj):
    base = _f10_vol_regime_retstd(closeadj, 504) * np.sqrt(252) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5v21 retvol ratio
def f10vr_f10_volatility_regime_retvolratio_5v21_slope_v038_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 5)
    b = _f10_vol_regime_retstd(closeadj, 21).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21v63 retvol ratio
def f10vr_f10_volatility_regime_retvolratio_21v63_slope_v039_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 21)
    b = _f10_vol_regime_retstd(closeadj, 63).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63v252 retvol ratio
def f10vr_f10_volatility_regime_retvolratio_63v252_slope_v040_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 63)
    b = _f10_vol_regime_retstd(closeadj, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252v504 retvol ratio
def f10vr_f10_volatility_regime_retvolratio_252v504_slope_v041_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 252)
    b = _f10_vol_regime_retstd(closeadj, 504).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of (21d - 63d) retvol diff
def f10vr_f10_volatility_regime_retvoldiff_21m63_slope_v042_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 21)
    b = _f10_vol_regime_retstd(closeadj, 63)
    base = (a - b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (63d - 252d) retvol diff
def f10vr_f10_volatility_regime_retvoldiff_63m252_slope_v043_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 63)
    b = _f10_vol_regime_retstd(closeadj, 252)
    base = (a - b) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of (252d - 504d) retvol diff
def f10vr_f10_volatility_regime_retvoldiff_252m504_slope_v044_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 252)
    b = _f10_vol_regime_retstd(closeadj, 504)
    base = (a - b) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ATR × volume z
def f10vr_f10_volatility_regime_atrxvolz_21d_slope_v045_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    base = atr * _z(volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ATR × volume z
def f10vr_f10_volatility_regime_atrxvolz_63d_slope_v046_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    base = atr * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ATR × volume z
def f10vr_f10_volatility_regime_atrxvolz_252d_slope_v047_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 252)
    base = atr * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d downside vol
def f10vr_f10_volatility_regime_downvol_21d_slope_v048_signal(closeadj):
    r = closeadj.pct_change()
    neg = r.where(r < 0, 0.0)
    base = _std(neg, 21) * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d downside vol
def f10vr_f10_volatility_regime_downvol_63d_slope_v049_signal(closeadj):
    r = closeadj.pct_change()
    neg = r.where(r < 0, 0.0)
    base = _std(neg, 63) * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d downside vol
def f10vr_f10_volatility_regime_downvol_252d_slope_v050_signal(closeadj):
    r = closeadj.pct_change()
    neg = r.where(r < 0, 0.0)
    base = _std(neg, 252) * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d upside vol
def f10vr_f10_volatility_regime_upvol_21d_slope_v051_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0)
    base = _std(pos, 21) * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d upside vol
def f10vr_f10_volatility_regime_upvol_63d_slope_v052_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0)
    base = _std(pos, 63) * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d upside vol
def f10vr_f10_volatility_regime_upvol_252d_slope_v053_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0)
    base = _std(pos, 252) * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of up/down vol ratio (21d)
def f10vr_f10_volatility_regime_upovrdownvol_21d_slope_v054_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0)
    neg = r.where(r < 0, 0.0)
    a = _std(pos, 21)
    b = _std(neg, 21).replace(0, np.nan)
    base = (a / b) * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of up/down vol ratio (63d)
def f10vr_f10_volatility_regime_upovrdownvol_63d_slope_v055_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0)
    neg = r.where(r < 0, 0.0)
    a = _std(pos, 63)
    b = _std(neg, 63).replace(0, np.nan)
    base = (a / b) * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of up/down vol ratio (252d)
def f10vr_f10_volatility_regime_upovrdownvol_252d_slope_v056_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0, 0.0)
    neg = r.where(r < 0, 0.0)
    a = _std(pos, 252)
    b = _std(neg, 252).replace(0, np.nan)
    base = (a / b) * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d retvol × ATR
def f10vr_f10_volatility_regime_retvolxatr_21d_slope_v057_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    base = _f10_vol_regime_retstd(closeadj, 21) * atr * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d retvol × ATR
def f10vr_f10_volatility_regime_retvolxatr_63d_slope_v058_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    base = _f10_vol_regime_retstd(closeadj, 63) * atr * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d retvol × 63d ATR
def f10vr_f10_volatility_regime_retvolxatr_252d_slope_v059_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    base = _f10_vol_regime_retstd(closeadj, 252) * atr * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d retvol × 63d ATR
def f10vr_f10_volatility_regime_retvolxatr_504d_slope_v060_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    base = _f10_vol_regime_retstd(closeadj, 504) * atr * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d Parkinson
def f10vr_f10_volatility_regime_parkinson_21d_slope_v061_signal(closeadj, high, low):
    rng = np.log(high / low.replace(0, np.nan))
    base = (rng * rng).rolling(21, min_periods=5).mean().pow(0.5) * closeadj + _f10_vol_state_atr(high, low, closeadj, 21) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d Parkinson
def f10vr_f10_volatility_regime_parkinson_63d_slope_v062_signal(closeadj, high, low):
    rng = np.log(high / low.replace(0, np.nan))
    base = (rng * rng).rolling(63, min_periods=21).mean().pow(0.5) * closeadj + _f10_vol_state_atr(high, low, closeadj, 63) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d Parkinson
def f10vr_f10_volatility_regime_parkinson_252d_slope_v063_signal(closeadj, high, low):
    rng = np.log(high / low.replace(0, np.nan))
    base = (rng * rng).rolling(252, min_periods=63).mean().pow(0.5) * closeadj + _f10_vol_state_atr(high, low, closeadj, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of Garman-Klass 21d
def f10vr_f10_volatility_regime_garmanklass_21d_slope_v064_signal(closeadj, high, low):
    hl = np.log(high / low.replace(0, np.nan))
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    gk2 = 0.5 * hl * hl - (2 * np.log(2) - 1) * co * co
    base = gk2.rolling(21, min_periods=5).mean().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of Garman-Klass 63d
def f10vr_f10_volatility_regime_garmanklass_63d_slope_v065_signal(closeadj, high, low):
    hl = np.log(high / low.replace(0, np.nan))
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    gk2 = 0.5 * hl * hl - (2 * np.log(2) - 1) * co * co
    base = gk2.rolling(63, min_periods=21).mean().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of Garman-Klass 252d
def f10vr_f10_volatility_regime_garmanklass_252d_slope_v066_signal(closeadj, high, low):
    hl = np.log(high / low.replace(0, np.nan))
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    gk2 = 0.5 * hl * hl - (2 * np.log(2) - 1) * co * co
    base = gk2.rolling(252, min_periods=63).mean().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol pct rank (21 over 252)
def f10vr_f10_volatility_regime_retvolpct_252d_slope_v067_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    base = v.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol pct rank (63 over 504)
def f10vr_f10_volatility_regime_retvolpct_504d_slope_v068_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    base = v.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol pct rank (252 over 504)
def f10vr_f10_volatility_regime_retvolpct_252v504_slope_v069_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 252)
    base = v.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ATR pct rank (21 over 252)
def f10vr_f10_volatility_regime_atrpct_252d_slope_v070_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    base = atr.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ATR pct rank (63 over 504)
def f10vr_f10_volatility_regime_atrpct_504d_slope_v071_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    base = atr.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d retvol max
def f10vr_f10_volatility_regime_retvolmax_63d_slope_v072_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    base = v.rolling(63, min_periods=21).max() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d retvol max
def f10vr_f10_volatility_regime_retvolmax_252d_slope_v073_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    base = v.rolling(252, min_periods=63).max() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d retvol min
def f10vr_f10_volatility_regime_retvolmin_63d_slope_v074_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    base = v.rolling(63, min_periods=21).min() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d retvol min
def f10vr_f10_volatility_regime_retvolmin_252d_slope_v075_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    base = v.rolling(252, min_periods=63).min() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d retvol range
def f10vr_f10_volatility_regime_retvolrange_63d_slope_v076_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    base = (v.rolling(63, min_periods=21).max() - v.rolling(63, min_periods=21).min()) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d retvol range
def f10vr_f10_volatility_regime_retvolrange_252d_slope_v077_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    base = (v.rolling(252, min_periods=63).max() - v.rolling(252, min_periods=63).min()) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d realized vol
def f10vr_f10_volatility_regime_realizedvol_21d_slope_v078_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(21, min_periods=5).sum().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d realized vol
def f10vr_f10_volatility_regime_realizedvol_63d_slope_v079_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(63, min_periods=21).sum().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d realized vol
def f10vr_f10_volatility_regime_realizedvol_252d_slope_v080_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(252, min_periods=63).sum().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d realized vol
def f10vr_f10_volatility_regime_realizedvol_504d_slope_v081_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(504, min_periods=126).sum().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 504) * 0.0
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of EWMA vol 21d
def f10vr_f10_volatility_regime_ewmavol_21d_slope_v082_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=21, min_periods=11, adjust=False).std() * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EWMA vol 63d
def f10vr_f10_volatility_regime_ewmavol_63d_slope_v083_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=63, min_periods=32, adjust=False).std() * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EWMA vol 252d
def f10vr_f10_volatility_regime_ewmavol_252d_slope_v084_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=252, min_periods=126, adjust=False).std() * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of EWMA vol 504d
def f10vr_f10_volatility_regime_ewmavol_504d_slope_v085_signal(closeadj):
    r = closeadj.pct_change()
    base = r.ewm(span=504, min_periods=252, adjust=False).std() * closeadj + _f10_vol_regime_retstd(closeadj, 504) * 0.0
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of GARCH proxy 21d
def f10vr_f10_volatility_regime_garchproxy_21d_slope_v086_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.ewm(span=21, min_periods=11, adjust=False).mean().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of GARCH proxy 63d
def f10vr_f10_volatility_regime_garchproxy_63d_slope_v087_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.ewm(span=63, min_periods=32, adjust=False).mean().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of GARCH proxy 252d
def f10vr_f10_volatility_regime_garchproxy_252d_slope_v088_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.ewm(span=252, min_periods=126, adjust=False).mean().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol × volume mean (21d)
def f10vr_f10_volatility_regime_retvolxvolmean_21d_slope_v089_signal(closeadj, volume):
    vm = _mean(volume, 21)
    base = _f10_vol_regime_retstd(closeadj, 21) * vm * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol × volume mean (63d)
def f10vr_f10_volatility_regime_retvolxvolmean_63d_slope_v090_signal(closeadj, volume):
    vm = _mean(volume, 63)
    base = _f10_vol_regime_retstd(closeadj, 63) * vm * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol × volume mean (252d)
def f10vr_f10_volatility_regime_retvolxvolmean_252d_slope_v091_signal(closeadj, volume):
    vm = _mean(volume, 252)
    base = _f10_vol_regime_retstd(closeadj, 252) * vm * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol × dollar volume (21d)
def f10vr_f10_volatility_regime_retvolxdv_21d_slope_v092_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f10_vol_regime_retstd(closeadj, 21) * dv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol × dollar volume (63d)
def f10vr_f10_volatility_regime_retvolxdv_63d_slope_v093_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f10_vol_regime_retstd(closeadj, 63) * dv
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol × dollar volume mean (252d)
def f10vr_f10_volatility_regime_retvolxdv_252d_slope_v094_signal(closeadj, volume):
    dv = closeadj * volume
    base = _f10_vol_regime_retstd(closeadj, 252) * _mean(dv, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol × volume z (21d)
def f10vr_f10_volatility_regime_retvolxvolz_21d_slope_v095_signal(closeadj, volume):
    base = _f10_vol_regime_retstd(closeadj, 21) * _z(volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol × volume z (63d)
def f10vr_f10_volatility_regime_retvolxvolz_63d_slope_v096_signal(closeadj, volume):
    base = _f10_vol_regime_retstd(closeadj, 63) * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol × volume z (252d)
def f10vr_f10_volatility_regime_retvolxvolz_252d_slope_v097_signal(closeadj, volume):
    base = _f10_vol_regime_retstd(closeadj, 252) * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ATR × dollar volume (21d)
def f10vr_f10_volatility_regime_atrxdv_21d_slope_v098_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    dv = closeadj * volume
    base = atr * dv
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ATR × dollar volume (63d)
def f10vr_f10_volatility_regime_atrxdv_63d_slope_v099_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    dv = closeadj * volume
    base = atr * dv
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ATR × dv mean (252d)
def f10vr_f10_volatility_regime_atrxdv_252d_slope_v100_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 252)
    dv = closeadj * volume
    base = atr * _mean(dv, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol × ret (21d)
def f10vr_f10_volatility_regime_retvolxret_21d_slope_v101_signal(closeadj):
    r = closeadj.pct_change(21)
    base = _f10_vol_regime_retstd(closeadj, 21) * r * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol × ret (63d)
def f10vr_f10_volatility_regime_retvolxret_63d_slope_v102_signal(closeadj):
    r = closeadj.pct_change(63)
    base = _f10_vol_regime_retstd(closeadj, 63) * r * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol × ret (252d)
def f10vr_f10_volatility_regime_retvolxret_252d_slope_v103_signal(closeadj):
    r = closeadj.pct_change(252)
    base = _f10_vol_regime_retstd(closeadj, 252) * r * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol × abs ret (21d)
def f10vr_f10_volatility_regime_retvolxabsret_21d_slope_v104_signal(closeadj):
    ar = closeadj.pct_change().abs()
    base = _f10_vol_regime_retstd(closeadj, 21) * ar * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol × mean abs ret (63d)
def f10vr_f10_volatility_regime_retvolxabsret_63d_slope_v105_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 21)
    base = _f10_vol_regime_retstd(closeadj, 63) * ar * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol × mean abs ret (252d)
def f10vr_f10_volatility_regime_retvolxabsret_252d_slope_v106_signal(closeadj):
    ar = _mean(closeadj.pct_change().abs(), 63)
    base = _f10_vol_regime_retstd(closeadj, 252) * ar * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol × skew (63d)
def f10vr_f10_volatility_regime_retvolxskew_63d_slope_v107_signal(closeadj):
    sk = closeadj.pct_change().rolling(63, min_periods=21).skew()
    base = _f10_vol_regime_retstd(closeadj, 63) * sk * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol × skew (252d)
def f10vr_f10_volatility_regime_retvolxskew_252d_slope_v108_signal(closeadj):
    sk = closeadj.pct_change().rolling(252, min_periods=63).skew()
    base = _f10_vol_regime_retstd(closeadj, 252) * sk * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol × kurt (63d)
def f10vr_f10_volatility_regime_retvolxkurt_63d_slope_v109_signal(closeadj):
    kt = closeadj.pct_change().rolling(63, min_periods=21).kurt()
    base = _f10_vol_regime_retstd(closeadj, 63) * kt * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol × kurt (252d)
def f10vr_f10_volatility_regime_retvolxkurt_252d_slope_v110_signal(closeadj):
    kt = closeadj.pct_change().rolling(252, min_periods=63).kurt()
    base = _f10_vol_regime_retstd(closeadj, 252) * kt * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ATR slope (21d)
def f10vr_f10_volatility_regime_atrslope_21d_slope_v111_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    inner = atr.diff(5) / atr.replace(0, np.nan).abs() + _f10_vol_state_atr(high, low, closeadj, 5) * 0.0
    base = inner * closeadj * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ATR slope (63d)
def f10vr_f10_volatility_regime_atrslope_63d_slope_v112_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    inner = atr.diff(21) / atr.replace(0, np.nan).abs() + _f10_vol_state_atr(high, low, closeadj, 21) * 0.0
    base = inner * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ATR slope (252d)
def f10vr_f10_volatility_regime_atrslope_252d_slope_v113_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 252)
    inner = atr.diff(63) / atr.replace(0, np.nan).abs() + _f10_vol_state_atr(high, low, closeadj, 63) * 0.0
    base = inner * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol slope (21d)
def f10vr_f10_volatility_regime_retvolslope_21d_slope_v114_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    inner = v.diff(5) / v.replace(0, np.nan).abs()
    base = inner * closeadj * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol slope (63d)
def f10vr_f10_volatility_regime_retvolslope_63d_slope_v115_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    inner = v.diff(21) / v.replace(0, np.nan).abs()
    base = inner * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol slope (252d)
def f10vr_f10_volatility_regime_retvolslope_252d_slope_v116_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 252)
    inner = v.diff(63) / v.replace(0, np.nan).abs()
    base = inner * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol mean (63d)
def f10vr_f10_volatility_regime_retvolmean_63d_slope_v117_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    base = _mean(v, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol mean (252d)
def f10vr_f10_volatility_regime_retvolmean_252d_slope_v118_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    base = _mean(v, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol mean (252v504)
def f10vr_f10_volatility_regime_retvolmean_252v504_slope_v119_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 252)
    base = _mean(v, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol/atr ratio (21d)
def f10vr_f10_volatility_regime_retvol_atrratio_21d_slope_v120_signal(closeadj, high, low):
    v = _f10_vol_regime_retstd(closeadj, 21)
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    base = (v / atr.replace(0, np.nan)) * closeadj * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol/atr ratio (63d)
def f10vr_f10_volatility_regime_retvol_atrratio_63d_slope_v121_signal(closeadj, high, low):
    v = _f10_vol_regime_retstd(closeadj, 63)
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    base = (v / atr.replace(0, np.nan)) * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol/atr ratio (252d)
def f10vr_f10_volatility_regime_retvol_atrratio_252d_slope_v122_signal(closeadj, high, low):
    v = _f10_vol_regime_retstd(closeadj, 252)
    atr = _f10_vol_state_atr(high, low, closeadj, 252)
    base = (v / atr.replace(0, np.nan)) * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of semi-deviation (21d)
def f10vr_f10_volatility_regime_semidev_21d_slope_v123_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 21)
    dev = (r - m).where(r < m, 0.0) ** 2
    base = dev.rolling(21, min_periods=5).mean().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of semi-deviation (63d)
def f10vr_f10_volatility_regime_semidev_63d_slope_v124_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 63)
    dev = (r - m).where(r < m, 0.0) ** 2
    base = dev.rolling(63, min_periods=21).mean().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of semi-deviation (252d)
def f10vr_f10_volatility_regime_semidev_252d_slope_v125_signal(closeadj):
    r = closeadj.pct_change()
    m = _mean(r, 252)
    dev = (r - m).where(r < m, 0.0) ** 2
    base = dev.rolling(252, min_periods=63).mean().pow(0.5) * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of Yang-Zhang 21d
def f10vr_f10_volatility_regime_yangzhang_21d_slope_v126_signal(closeadj, open, high, low):
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    op = np.log(open / closeadj.shift(1).replace(0, np.nan))
    rs = (np.log(high / closeadj.replace(0, np.nan)) * np.log(high / open.replace(0, np.nan))
          + np.log(low / closeadj.replace(0, np.nan)) * np.log(low / open.replace(0, np.nan)))
    sigma = (op.rolling(21, min_periods=5).var() + 0.34 * co.rolling(21, min_periods=5).var()
             + 0.66 * rs.rolling(21, min_periods=5).mean()).pow(0.5)
    base = sigma * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of Yang-Zhang 63d
def f10vr_f10_volatility_regime_yangzhang_63d_slope_v127_signal(closeadj, open, high, low):
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    op = np.log(open / closeadj.shift(1).replace(0, np.nan))
    rs = (np.log(high / closeadj.replace(0, np.nan)) * np.log(high / open.replace(0, np.nan))
          + np.log(low / closeadj.replace(0, np.nan)) * np.log(low / open.replace(0, np.nan)))
    sigma = (op.rolling(63, min_periods=21).var() + 0.34 * co.rolling(63, min_periods=21).var()
             + 0.66 * rs.rolling(63, min_periods=21).mean()).pow(0.5)
    base = sigma * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of Yang-Zhang 252d
def f10vr_f10_volatility_regime_yangzhang_252d_slope_v128_signal(closeadj, open, high, low):
    co = np.log(closeadj / closeadj.shift(1).replace(0, np.nan))
    op = np.log(open / closeadj.shift(1).replace(0, np.nan))
    rs = (np.log(high / closeadj.replace(0, np.nan)) * np.log(high / open.replace(0, np.nan))
          + np.log(low / closeadj.replace(0, np.nan)) * np.log(low / open.replace(0, np.nan)))
    sigma = (op.rolling(252, min_periods=63).var() + 0.34 * co.rolling(252, min_periods=63).var()
             + 0.66 * rs.rolling(252, min_periods=63).mean()).pow(0.5)
    base = sigma * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol pct expanding (21d)
def f10vr_f10_volatility_regime_retvolpctexp_21d_slope_v129_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 21)
    base = v.expanding(min_periods=63).rank(pct=True) * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol pct expanding (63d)
def f10vr_f10_volatility_regime_retvolpctexp_63d_slope_v130_signal(closeadj):
    v = _f10_vol_regime_retstd(closeadj, 63)
    base = v.expanding(min_periods=126).rank(pct=True) * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ATR slope × volume z (21d)
def f10vr_f10_volatility_regime_atrslopexvolz_21d_slope_v131_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    inner = atr.diff(5) / atr.replace(0, np.nan).abs()
    base = inner * _z(volume, 21) * closeadj * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ATR slope × volume z (63d)
def f10vr_f10_volatility_regime_atrslopexvolz_63d_slope_v132_signal(closeadj, high, low, volume):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    inner = atr.diff(21) / atr.replace(0, np.nan).abs()
    base = inner * _z(volume, 63) * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol × range (21d)
def f10vr_f10_volatility_regime_retvolxrange_21d_slope_v133_signal(closeadj, high, low):
    rng = _mean((high - low), 21)
    base = _f10_vol_regime_retstd(closeadj, 21) * rng * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol × range (63d)
def f10vr_f10_volatility_regime_retvolxrange_63d_slope_v134_signal(closeadj, high, low):
    rng = _mean((high - low), 63)
    base = _f10_vol_regime_retstd(closeadj, 63) * rng * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol × range (252d)
def f10vr_f10_volatility_regime_retvolxrange_252d_slope_v135_signal(closeadj, high, low):
    rng = _mean((high - low), 63)
    base = _f10_vol_regime_retstd(closeadj, 252) * rng * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of retvol × overnight gap z (21d)
def f10vr_f10_volatility_regime_retvolxocgapz_21d_slope_v136_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    base = _f10_vol_regime_retstd(closeadj, 21) * _z(gap, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol × gap mean (63d)
def f10vr_f10_volatility_regime_retvolxocgapmean_63d_slope_v137_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    base = _f10_vol_regime_retstd(closeadj, 63) * _mean(gap, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol × gap mean (252d)
def f10vr_f10_volatility_regime_retvolxocgapmean_252d_slope_v138_signal(closeadj, open, close):
    gap = (open - close.shift(1)) / close.shift(1).abs().replace(0, np.nan)
    base = _f10_vol_regime_retstd(closeadj, 252) * _mean(gap, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retvol diffx (21v63)
def f10vr_f10_volatility_regime_retvol_diffx_21v63_slope_v139_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 21)
    b = _f10_vol_regime_retstd(closeadj, 63)
    base = (a - b) * closeadj * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retvol diffx (63v252)
def f10vr_f10_volatility_regime_retvol_diffx_63v252_slope_v140_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 63)
    b = _f10_vol_regime_retstd(closeadj, 252)
    base = (a - b) * closeadj * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of retvol diffx (252v504)
def f10vr_f10_volatility_regime_retvol_diffx_252v504_slope_v141_signal(closeadj):
    a = _f10_vol_regime_retstd(closeadj, 252)
    b = _f10_vol_regime_retstd(closeadj, 504)
    base = (a - b) * closeadj * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ATR ratio z (252)
def f10vr_f10_volatility_regime_atrratioz_252d_slope_v142_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 21)
    rr = atr / closeadj.replace(0, np.nan)
    base = _z(rr, 252) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ATR ratio z (504)
def f10vr_f10_volatility_regime_atrratioz_504d_slope_v143_signal(closeadj, high, low):
    atr = _f10_vol_state_atr(high, low, closeadj, 63)
    rr = atr / closeadj.replace(0, np.nan)
    base = _z(rr, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of large-move days (21d)
def f10vr_f10_volatility_regime_downdays_21d_slope_v144_signal(closeadj):
    r = closeadj.pct_change()
    flag = (r.abs() > _f10_vol_regime_retstd(closeadj, 21)).astype(float)
    base = flag.rolling(21, min_periods=5).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of large-move days (63d)
def f10vr_f10_volatility_regime_downdays_63d_slope_v145_signal(closeadj):
    r = closeadj.pct_change()
    flag = (r.abs() > _f10_vol_regime_retstd(closeadj, 63)).astype(float)
    base = flag.rolling(63, min_periods=21).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of large-move days (252d)
def f10vr_f10_volatility_regime_downdays_252d_slope_v146_signal(closeadj):
    r = closeadj.pct_change()
    flag = (r.abs() > _f10_vol_regime_retstd(closeadj, 252)).astype(float)
    base = flag.rolling(252, min_periods=63).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of realized variance (21d)
def f10vr_f10_volatility_regime_realvar_21d_slope_v147_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(21, min_periods=5).sum() * closeadj + _f10_vol_regime_retstd(closeadj, 21) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of realized variance (63d)
def f10vr_f10_volatility_regime_realvar_63d_slope_v148_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(63, min_periods=21).sum() * closeadj + _f10_vol_regime_retstd(closeadj, 63) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of realized variance (252d)
def f10vr_f10_volatility_regime_realvar_252d_slope_v149_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(252, min_periods=63).sum() * closeadj + _f10_vol_regime_retstd(closeadj, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of composite vol (63d)
def f10vr_f10_volatility_regime_composite_63d_slope_v150_signal(closeadj, high, low):
    a = _f10_vol_regime_retstd(closeadj, 63) * closeadj
    b = _f10_vol_state_atr(high, low, closeadj, 63)
    base = (a + b) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10vr_f10_volatility_regime_retvol_5d_slope_v001_signal,
    f10vr_f10_volatility_regime_retvol_21d_slope_v002_signal,
    f10vr_f10_volatility_regime_retvol_21d_slope_v003_signal,
    f10vr_f10_volatility_regime_retvol_63d_slope_v004_signal,
    f10vr_f10_volatility_regime_retvol_63d_slope_v005_signal,
    f10vr_f10_volatility_regime_retvol_126d_slope_v006_signal,
    f10vr_f10_volatility_regime_retvol_126d_slope_v007_signal,
    f10vr_f10_volatility_regime_retvol_252d_slope_v008_signal,
    f10vr_f10_volatility_regime_retvol_252d_slope_v009_signal,
    f10vr_f10_volatility_regime_retvol_252d_slope_v010_signal,
    f10vr_f10_volatility_regime_retvol_504d_slope_v011_signal,
    f10vr_f10_volatility_regime_retvol_504d_slope_v012_signal,
    f10vr_f10_volatility_regime_atr_5d_slope_v013_signal,
    f10vr_f10_volatility_regime_atr_21d_slope_v014_signal,
    f10vr_f10_volatility_regime_atr_63d_slope_v015_signal,
    f10vr_f10_volatility_regime_atr_252d_slope_v016_signal,
    f10vr_f10_volatility_regime_atr_504d_slope_v017_signal,
    f10vr_f10_volatility_regime_atrratio_21d_slope_v018_signal,
    f10vr_f10_volatility_regime_atrratio_63d_slope_v019_signal,
    f10vr_f10_volatility_regime_atrratio_252d_slope_v020_signal,
    f10vr_f10_volatility_regime_atrratio_504d_slope_v021_signal,
    f10vr_f10_volatility_regime_retvolz_252d_slope_v022_signal,
    f10vr_f10_volatility_regime_retvolz_63v252_slope_v023_signal,
    f10vr_f10_volatility_regime_retvolz_504d_slope_v024_signal,
    f10vr_f10_volatility_regime_atrz_252d_slope_v025_signal,
    f10vr_f10_volatility_regime_atrz_504d_slope_v026_signal,
    f10vr_f10_volatility_regime_volofvol_63d_slope_v027_signal,
    f10vr_f10_volatility_regime_volofvol_252d_slope_v028_signal,
    f10vr_f10_volatility_regime_volofvol63_252d_slope_v029_signal,
    f10vr_f10_volatility_regime_retvolxprice_21d_slope_v030_signal,
    f10vr_f10_volatility_regime_retvolxprice_63d_slope_v031_signal,
    f10vr_f10_volatility_regime_retvolxprice_252d_slope_v032_signal,
    f10vr_f10_volatility_regime_retvolxprice_504d_slope_v033_signal,
    f10vr_f10_volatility_regime_retvolann_21d_slope_v034_signal,
    f10vr_f10_volatility_regime_retvolann_63d_slope_v035_signal,
    f10vr_f10_volatility_regime_retvolann_252d_slope_v036_signal,
    f10vr_f10_volatility_regime_retvolann_504d_slope_v037_signal,
    f10vr_f10_volatility_regime_retvolratio_5v21_slope_v038_signal,
    f10vr_f10_volatility_regime_retvolratio_21v63_slope_v039_signal,
    f10vr_f10_volatility_regime_retvolratio_63v252_slope_v040_signal,
    f10vr_f10_volatility_regime_retvolratio_252v504_slope_v041_signal,
    f10vr_f10_volatility_regime_retvoldiff_21m63_slope_v042_signal,
    f10vr_f10_volatility_regime_retvoldiff_63m252_slope_v043_signal,
    f10vr_f10_volatility_regime_retvoldiff_252m504_slope_v044_signal,
    f10vr_f10_volatility_regime_atrxvolz_21d_slope_v045_signal,
    f10vr_f10_volatility_regime_atrxvolz_63d_slope_v046_signal,
    f10vr_f10_volatility_regime_atrxvolz_252d_slope_v047_signal,
    f10vr_f10_volatility_regime_downvol_21d_slope_v048_signal,
    f10vr_f10_volatility_regime_downvol_63d_slope_v049_signal,
    f10vr_f10_volatility_regime_downvol_252d_slope_v050_signal,
    f10vr_f10_volatility_regime_upvol_21d_slope_v051_signal,
    f10vr_f10_volatility_regime_upvol_63d_slope_v052_signal,
    f10vr_f10_volatility_regime_upvol_252d_slope_v053_signal,
    f10vr_f10_volatility_regime_upovrdownvol_21d_slope_v054_signal,
    f10vr_f10_volatility_regime_upovrdownvol_63d_slope_v055_signal,
    f10vr_f10_volatility_regime_upovrdownvol_252d_slope_v056_signal,
    f10vr_f10_volatility_regime_retvolxatr_21d_slope_v057_signal,
    f10vr_f10_volatility_regime_retvolxatr_63d_slope_v058_signal,
    f10vr_f10_volatility_regime_retvolxatr_252d_slope_v059_signal,
    f10vr_f10_volatility_regime_retvolxatr_504d_slope_v060_signal,
    f10vr_f10_volatility_regime_parkinson_21d_slope_v061_signal,
    f10vr_f10_volatility_regime_parkinson_63d_slope_v062_signal,
    f10vr_f10_volatility_regime_parkinson_252d_slope_v063_signal,
    f10vr_f10_volatility_regime_garmanklass_21d_slope_v064_signal,
    f10vr_f10_volatility_regime_garmanklass_63d_slope_v065_signal,
    f10vr_f10_volatility_regime_garmanklass_252d_slope_v066_signal,
    f10vr_f10_volatility_regime_retvolpct_252d_slope_v067_signal,
    f10vr_f10_volatility_regime_retvolpct_504d_slope_v068_signal,
    f10vr_f10_volatility_regime_retvolpct_252v504_slope_v069_signal,
    f10vr_f10_volatility_regime_atrpct_252d_slope_v070_signal,
    f10vr_f10_volatility_regime_atrpct_504d_slope_v071_signal,
    f10vr_f10_volatility_regime_retvolmax_63d_slope_v072_signal,
    f10vr_f10_volatility_regime_retvolmax_252d_slope_v073_signal,
    f10vr_f10_volatility_regime_retvolmin_63d_slope_v074_signal,
    f10vr_f10_volatility_regime_retvolmin_252d_slope_v075_signal,
    f10vr_f10_volatility_regime_retvolrange_63d_slope_v076_signal,
    f10vr_f10_volatility_regime_retvolrange_252d_slope_v077_signal,
    f10vr_f10_volatility_regime_realizedvol_21d_slope_v078_signal,
    f10vr_f10_volatility_regime_realizedvol_63d_slope_v079_signal,
    f10vr_f10_volatility_regime_realizedvol_252d_slope_v080_signal,
    f10vr_f10_volatility_regime_realizedvol_504d_slope_v081_signal,
    f10vr_f10_volatility_regime_ewmavol_21d_slope_v082_signal,
    f10vr_f10_volatility_regime_ewmavol_63d_slope_v083_signal,
    f10vr_f10_volatility_regime_ewmavol_252d_slope_v084_signal,
    f10vr_f10_volatility_regime_ewmavol_504d_slope_v085_signal,
    f10vr_f10_volatility_regime_garchproxy_21d_slope_v086_signal,
    f10vr_f10_volatility_regime_garchproxy_63d_slope_v087_signal,
    f10vr_f10_volatility_regime_garchproxy_252d_slope_v088_signal,
    f10vr_f10_volatility_regime_retvolxvolmean_21d_slope_v089_signal,
    f10vr_f10_volatility_regime_retvolxvolmean_63d_slope_v090_signal,
    f10vr_f10_volatility_regime_retvolxvolmean_252d_slope_v091_signal,
    f10vr_f10_volatility_regime_retvolxdv_21d_slope_v092_signal,
    f10vr_f10_volatility_regime_retvolxdv_63d_slope_v093_signal,
    f10vr_f10_volatility_regime_retvolxdv_252d_slope_v094_signal,
    f10vr_f10_volatility_regime_retvolxvolz_21d_slope_v095_signal,
    f10vr_f10_volatility_regime_retvolxvolz_63d_slope_v096_signal,
    f10vr_f10_volatility_regime_retvolxvolz_252d_slope_v097_signal,
    f10vr_f10_volatility_regime_atrxdv_21d_slope_v098_signal,
    f10vr_f10_volatility_regime_atrxdv_63d_slope_v099_signal,
    f10vr_f10_volatility_regime_atrxdv_252d_slope_v100_signal,
    f10vr_f10_volatility_regime_retvolxret_21d_slope_v101_signal,
    f10vr_f10_volatility_regime_retvolxret_63d_slope_v102_signal,
    f10vr_f10_volatility_regime_retvolxret_252d_slope_v103_signal,
    f10vr_f10_volatility_regime_retvolxabsret_21d_slope_v104_signal,
    f10vr_f10_volatility_regime_retvolxabsret_63d_slope_v105_signal,
    f10vr_f10_volatility_regime_retvolxabsret_252d_slope_v106_signal,
    f10vr_f10_volatility_regime_retvolxskew_63d_slope_v107_signal,
    f10vr_f10_volatility_regime_retvolxskew_252d_slope_v108_signal,
    f10vr_f10_volatility_regime_retvolxkurt_63d_slope_v109_signal,
    f10vr_f10_volatility_regime_retvolxkurt_252d_slope_v110_signal,
    f10vr_f10_volatility_regime_atrslope_21d_slope_v111_signal,
    f10vr_f10_volatility_regime_atrslope_63d_slope_v112_signal,
    f10vr_f10_volatility_regime_atrslope_252d_slope_v113_signal,
    f10vr_f10_volatility_regime_retvolslope_21d_slope_v114_signal,
    f10vr_f10_volatility_regime_retvolslope_63d_slope_v115_signal,
    f10vr_f10_volatility_regime_retvolslope_252d_slope_v116_signal,
    f10vr_f10_volatility_regime_retvolmean_63d_slope_v117_signal,
    f10vr_f10_volatility_regime_retvolmean_252d_slope_v118_signal,
    f10vr_f10_volatility_regime_retvolmean_252v504_slope_v119_signal,
    f10vr_f10_volatility_regime_retvol_atrratio_21d_slope_v120_signal,
    f10vr_f10_volatility_regime_retvol_atrratio_63d_slope_v121_signal,
    f10vr_f10_volatility_regime_retvol_atrratio_252d_slope_v122_signal,
    f10vr_f10_volatility_regime_semidev_21d_slope_v123_signal,
    f10vr_f10_volatility_regime_semidev_63d_slope_v124_signal,
    f10vr_f10_volatility_regime_semidev_252d_slope_v125_signal,
    f10vr_f10_volatility_regime_yangzhang_21d_slope_v126_signal,
    f10vr_f10_volatility_regime_yangzhang_63d_slope_v127_signal,
    f10vr_f10_volatility_regime_yangzhang_252d_slope_v128_signal,
    f10vr_f10_volatility_regime_retvolpctexp_21d_slope_v129_signal,
    f10vr_f10_volatility_regime_retvolpctexp_63d_slope_v130_signal,
    f10vr_f10_volatility_regime_atrslopexvolz_21d_slope_v131_signal,
    f10vr_f10_volatility_regime_atrslopexvolz_63d_slope_v132_signal,
    f10vr_f10_volatility_regime_retvolxrange_21d_slope_v133_signal,
    f10vr_f10_volatility_regime_retvolxrange_63d_slope_v134_signal,
    f10vr_f10_volatility_regime_retvolxrange_252d_slope_v135_signal,
    f10vr_f10_volatility_regime_retvolxocgapz_21d_slope_v136_signal,
    f10vr_f10_volatility_regime_retvolxocgapmean_63d_slope_v137_signal,
    f10vr_f10_volatility_regime_retvolxocgapmean_252d_slope_v138_signal,
    f10vr_f10_volatility_regime_retvol_diffx_21v63_slope_v139_signal,
    f10vr_f10_volatility_regime_retvol_diffx_63v252_slope_v140_signal,
    f10vr_f10_volatility_regime_retvol_diffx_252v504_slope_v141_signal,
    f10vr_f10_volatility_regime_atrratioz_252d_slope_v142_signal,
    f10vr_f10_volatility_regime_atrratioz_504d_slope_v143_signal,
    f10vr_f10_volatility_regime_downdays_21d_slope_v144_signal,
    f10vr_f10_volatility_regime_downdays_63d_slope_v145_signal,
    f10vr_f10_volatility_regime_downdays_252d_slope_v146_signal,
    f10vr_f10_volatility_regime_realvar_21d_slope_v147_signal,
    f10vr_f10_volatility_regime_realvar_63d_slope_v148_signal,
    f10vr_f10_volatility_regime_realvar_252d_slope_v149_signal,
    f10vr_f10_volatility_regime_composite_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_VOLATILITY_REGIME_REGISTRY_SLOPE = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f10_volatility_regime_2nd_derivatives_001_150_claude: {n_features} features pass")
