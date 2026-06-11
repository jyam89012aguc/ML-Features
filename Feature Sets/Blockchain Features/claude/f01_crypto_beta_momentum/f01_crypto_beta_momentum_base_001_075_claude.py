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
    # rate of change over w trading days
    return s.pct_change(periods=w)


def _f01_logmom(s, w):
    # log momentum over w (additive, robust to scale)
    return np.log(s / s.shift(w))


def _f01_ampmom(s, w, k):
    # sign-preserving convex amplification of momentum (leveraged-beta signature)
    r = s.pct_change(periods=w)
    return np.sign(r) * (r.abs() ** k)


def _f01_momqual(s, w):
    # momentum quality: return per unit of path volatility (information-ratio style)
    r = s.pct_change(periods=w)
    v = s.pct_change().rolling(w, min_periods=max(2, w // 2)).std() * np.sqrt(w)
    return r / v.replace(0, np.nan)


# ============ FEATURES 001-075 ============

# 21d rate of change (monthly momentum)
def f01cb_f01_crypto_beta_momentum_roc_21d_base_v001_signal(closeadj):
    result = _f01_roc(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rate of change (quarterly momentum)
def f01cb_f01_crypto_beta_momentum_roc_63d_base_v002_signal(closeadj):
    result = _f01_roc(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rate of change (half-year momentum)
def f01cb_f01_crypto_beta_momentum_roc_126d_base_v003_signal(closeadj):
    result = _f01_roc(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rate of change (annual momentum)
def f01cb_f01_crypto_beta_momentum_roc_252d_base_v004_signal(closeadj):
    result = _f01_roc(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d rate of change (weekly thrust)
def f01cb_f01_crypto_beta_momentum_roc_5d_base_v005_signal(closeadj):
    result = _f01_roc(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log momentum
def f01cb_f01_crypto_beta_momentum_logmom_21d_base_v006_signal(closeadj):
    result = _f01_logmom(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log momentum
def f01cb_f01_crypto_beta_momentum_logmom_63d_base_v007_signal(closeadj):
    result = _f01_logmom(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log momentum
def f01cb_f01_crypto_beta_momentum_logmom_126d_base_v008_signal(closeadj):
    result = _f01_logmom(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log momentum
def f01cb_f01_crypto_beta_momentum_logmom_252d_base_v009_signal(closeadj):
    result = _f01_logmom(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log momentum (two-year, halving-scale)
def f01cb_f01_crypto_beta_momentum_logmom_504d_base_v010_signal(closeadj):
    result = _f01_logmom(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d convex-amplified momentum k=1.5
def f01cb_f01_crypto_beta_momentum_amp15_21d_base_v011_signal(closeadj):
    result = _f01_ampmom(closeadj, 21, 1.5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d convex-amplified momentum k=1.5
def f01cb_f01_crypto_beta_momentum_amp15_63d_base_v012_signal(closeadj):
    result = _f01_ampmom(closeadj, 63, 1.5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d convex-amplified momentum k=2.0
def f01cb_f01_crypto_beta_momentum_amp20_21d_base_v013_signal(closeadj):
    result = _f01_ampmom(closeadj, 21, 2.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d convex-amplified momentum k=2.0
def f01cb_f01_crypto_beta_momentum_amp20_63d_base_v014_signal(closeadj):
    result = _f01_ampmom(closeadj, 63, 2.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d convex-amplified momentum k=2.5
def f01cb_f01_crypto_beta_momentum_amp25_126d_base_v015_signal(closeadj):
    result = _f01_ampmom(closeadj, 126, 2.5)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d convex-amplified momentum k=2.0
def f01cb_f01_crypto_beta_momentum_amp20_252d_base_v016_signal(closeadj):
    result = _f01_ampmom(closeadj, 252, 2.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d momentum quality
def f01cb_f01_crypto_beta_momentum_momqual_21d_base_v017_signal(closeadj):
    result = _f01_momqual(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d momentum quality
def f01cb_f01_crypto_beta_momentum_momqual_63d_base_v018_signal(closeadj):
    result = _f01_momqual(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d momentum quality
def f01cb_f01_crypto_beta_momentum_momqual_126d_base_v019_signal(closeadj):
    result = _f01_momqual(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d momentum quality
def f01cb_f01_crypto_beta_momentum_momqual_252d_base_v020_signal(closeadj):
    result = _f01_momqual(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d momentum quality
def f01cb_f01_crypto_beta_momentum_momqual_42d_base_v021_signal(closeadj):
    result = _f01_momqual(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# short-minus-long momentum spread 21d vs 126d
def f01cb_f01_crypto_beta_momentum_spread_21_126_base_v022_signal(closeadj):
    result = _f01_roc(closeadj, 21) - _f01_roc(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# momentum spread 63d vs 252d
def f01cb_f01_crypto_beta_momentum_spread_63_252_base_v023_signal(closeadj):
    result = _f01_roc(closeadj, 63) - _f01_roc(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log-momentum spread 21d vs 63d
def f01cb_f01_crypto_beta_momentum_lspread_21_63_base_v024_signal(closeadj):
    result = _f01_logmom(closeadj, 21) - _f01_logmom(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 21d momentum over 252d
def f01cb_f01_crypto_beta_momentum_zroc_21d_base_v025_signal(closeadj):
    result = _z(_f01_roc(closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d momentum over 252d
def f01cb_f01_crypto_beta_momentum_zroc_63d_base_v026_signal(closeadj):
    result = _z(_f01_roc(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d log-momentum over 504d
def f01cb_f01_crypto_beta_momentum_zlmom_126d_base_v027_signal(closeadj):
    result = _z(_f01_logmom(closeadj, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d momentum minus its 63d average (momentum surprise)
def f01cb_f01_crypto_beta_momentum_surp_21d_base_v028_signal(closeadj):
    r = _f01_roc(closeadj, 21)
    result = r - _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d momentum minus its 126d average
def f01cb_f01_crypto_beta_momentum_surp_63d_base_v029_signal(closeadj):
    r = _f01_roc(closeadj, 63)
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 21d momentum over 126d
def f01cb_f01_crypto_beta_momentum_rank_21d_base_v030_signal(closeadj):
    r = _f01_roc(closeadj, 21)
    result = r.rolling(126, min_periods=21).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of 63d momentum over 252d
def f01cb_f01_crypto_beta_momentum_rank_63d_base_v031_signal(closeadj):
    r = _f01_roc(closeadj, 63)
    result = r.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d amplified momentum standardized over 252d
def f01cb_f01_crypto_beta_momentum_zamp_21d_base_v032_signal(closeadj):
    result = _z(_f01_ampmom(closeadj, 21, 2.0), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d upside-capture ratio of weekly momentum (continuous persistence proxy)
def f01cb_f01_crypto_beta_momentum_upcapture_63d_base_v033_signal(closeadj):
    r = _f01_roc(closeadj, 5)
    pos = r.clip(lower=0).rolling(63, min_periods=21).sum()
    tot = r.abs().rolling(63, min_periods=21).sum()
    result = _safe_div(pos, tot)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d upside-capture ratio of weekly momentum
def f01cb_f01_crypto_beta_momentum_upcapture_126d_base_v034_signal(closeadj):
    r = _f01_roc(closeadj, 5)
    pos = r.clip(lower=0).rolling(126, min_periods=42).sum()
    tot = r.abs().rolling(126, min_periods=42).sum()
    result = _safe_div(pos, tot)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d momentum confirmed by volume z-score
def f01cb_f01_crypto_beta_momentum_volconf_21d_base_v035_signal(closeadj, volume):
    result = _f01_roc(closeadj, 21) * _z(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d momentum confirmed by dollar-volume z-score
def f01cb_f01_crypto_beta_momentum_dvconf_63d_base_v036_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f01_roc(closeadj, 63) * _z(dv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# relative momentum: 21d over 252d ratio
def f01cb_f01_crypto_beta_momentum_ratio_21_252_base_v037_signal(closeadj):
    result = _safe_div(_f01_roc(closeadj, 21), _f01_roc(closeadj, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# relative momentum: 42d over 126d ratio
def f01cb_f01_crypto_beta_momentum_ratio_42_126_base_v038_signal(closeadj):
    result = _safe_div(_f01_roc(closeadj, 42), _f01_roc(closeadj, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gain/loss ratio of weekly momentum (momentum breadth, continuous)
def f01cb_f01_crypto_beta_momentum_glratio_63d_base_v039_signal(closeadj):
    r = _f01_roc(closeadj, 5)
    g = r.clip(lower=0).rolling(63, min_periods=21).sum()
    l = (-r.clip(upper=0)).rolling(63, min_periods=21).sum()
    result = _safe_div(g, l)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gain/loss ratio of weekly momentum
def f01cb_f01_crypto_beta_momentum_glratio_126d_base_v040_signal(closeadj):
    r = _f01_roc(closeadj, 5)
    g = r.clip(lower=0).rolling(126, min_periods=42).sum()
    l = (-r.clip(upper=0)).rolling(126, min_periods=42).sum()
    result = _safe_div(g, l)
    return result.replace([np.inf, -np.inf], np.nan)


# momentum acceleration 21d vs 42d spread
def f01cb_f01_crypto_beta_momentum_accel_21_42_base_v041_signal(closeadj):
    result = _f01_roc(closeadj, 21) - _f01_roc(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# momentum acceleration 42d vs 84d spread
def f01cb_f01_crypto_beta_momentum_accel_42_84_base_v042_signal(closeadj):
    result = _f01_roc(closeadj, 42) - _f01_roc(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# momentum acceleration 63d vs 126d spread
def f01cb_f01_crypto_beta_momentum_accel_63_126_base_v043_signal(closeadj):
    result = _f01_roc(closeadj, 63) - _f01_roc(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d convex-amplified momentum k=3.0 (extreme leverage signature)
def f01cb_f01_crypto_beta_momentum_amp30_21d_base_v044_signal(closeadj):
    result = _f01_ampmom(closeadj, 21, 3.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d convex-amplified momentum k=1.25
def f01cb_f01_crypto_beta_momentum_amp12_252d_base_v045_signal(closeadj):
    result = _f01_ampmom(closeadj, 252, 1.25)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d log momentum
def f01cb_f01_crypto_beta_momentum_logmom_42d_base_v046_signal(closeadj):
    result = _f01_logmom(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d log momentum
def f01cb_f01_crypto_beta_momentum_logmom_189d_base_v047_signal(closeadj):
    result = _f01_logmom(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d log momentum
def f01cb_f01_crypto_beta_momentum_logmom_378d_base_v048_signal(closeadj):
    result = _f01_logmom(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d rate of change
def f01cb_f01_crypto_beta_momentum_roc_42d_base_v049_signal(closeadj):
    result = _f01_roc(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d rate of change
def f01cb_f01_crypto_beta_momentum_roc_189d_base_v050_signal(closeadj):
    result = _f01_roc(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d rate of change
def f01cb_f01_crypto_beta_momentum_roc_378d_base_v051_signal(closeadj):
    result = _f01_roc(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rate of change
def f01cb_f01_crypto_beta_momentum_roc_504d_base_v052_signal(closeadj):
    result = _f01_roc(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d momentum quality
def f01cb_f01_crypto_beta_momentum_momqual_504d_base_v053_signal(closeadj):
    result = _f01_momqual(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d momentum quality
def f01cb_f01_crypto_beta_momentum_momqual_189d_base_v054_signal(closeadj):
    result = _f01_momqual(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 21d momentum over 126d
def f01cb_f01_crypto_beta_momentum_zroc126_21d_base_v055_signal(closeadj):
    result = _z(_f01_roc(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 5d momentum over 63d
def f01cb_f01_crypto_beta_momentum_zroc63_5d_base_v056_signal(closeadj):
    result = _z(_f01_roc(closeadj, 5), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d rate of change
def f01cb_f01_crypto_beta_momentum_roc_10d_base_v057_signal(closeadj):
    result = _f01_roc(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d log momentum
def f01cb_f01_crypto_beta_momentum_logmom_10d_base_v058_signal(closeadj):
    result = _f01_logmom(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d convex-amplified momentum k=2.0
def f01cb_f01_crypto_beta_momentum_amp20_10d_base_v059_signal(closeadj):
    result = _f01_ampmom(closeadj, 10, 2.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d momentum quality
def f01cb_f01_crypto_beta_momentum_momqual_10d_base_v060_signal(closeadj):
    result = _f01_momqual(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed 21d momentum (21d mean of 21d roc)
def f01cb_f01_crypto_beta_momentum_smooth_21d_base_v061_signal(closeadj):
    result = _mean(_f01_roc(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed 63d log momentum (21d mean)
def f01cb_f01_crypto_beta_momentum_smooth_63d_base_v062_signal(closeadj):
    result = _mean(_f01_logmom(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed 21d amplified momentum (21d mean)
def f01cb_f01_crypto_beta_momentum_smoothamp_21d_base_v063_signal(closeadj):
    result = _mean(_f01_ampmom(closeadj, 21, 2.0), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d momentum weighted by its own sign-persistence
def f01cb_f01_crypto_beta_momentum_persistw_63d_base_v064_signal(closeadj):
    r = _f01_roc(closeadj, 63)
    w = np.sign(r).rolling(63, min_periods=21).mean()
    result = r * w
    return result.replace([np.inf, -np.inf], np.nan)


# 126d momentum weighted by up-day fraction
def f01cb_f01_crypto_beta_momentum_breadthw_126d_base_v065_signal(closeadj):
    up = (closeadj.diff() > 0).astype(float).rolling(126, min_periods=42).mean()
    result = _f01_roc(closeadj, 126) * up
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 63d log momentum
def f01cb_f01_crypto_beta_momentum_ann_63d_base_v066_signal(closeadj):
    result = _f01_logmom(closeadj, 63) * (252.0 / 63.0)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 126d log momentum
def f01cb_f01_crypto_beta_momentum_ann_126d_base_v067_signal(closeadj):
    result = _f01_logmom(closeadj, 126) * (252.0 / 126.0)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 21d log momentum
def f01cb_f01_crypto_beta_momentum_ann_21d_base_v068_signal(closeadj):
    result = _f01_logmom(closeadj, 21) * (252.0 / 21.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d momentum convexity (amplified minus linear)
def f01cb_f01_crypto_beta_momentum_convex_63d_base_v069_signal(closeadj):
    result = _f01_ampmom(closeadj, 63, 2.0) - _f01_roc(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d momentum convexity
def f01cb_f01_crypto_beta_momentum_convex_126d_base_v070_signal(closeadj):
    result = _f01_ampmom(closeadj, 126, 2.0) - _f01_roc(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d momentum quality clipped to robust range
def f01cb_f01_crypto_beta_momentum_qualclip_252d_base_v071_signal(closeadj):
    result = _f01_momqual(closeadj, 252).clip(-10, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d momentum information ratio vs 252d momentum dispersion
def f01cb_f01_crypto_beta_momentum_inforatio_21d_base_v072_signal(closeadj):
    r = _f01_roc(closeadj, 21)
    result = _safe_div(r, _std(r, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d momentum information ratio vs 252d dispersion
def f01cb_f01_crypto_beta_momentum_inforatio_63d_base_v073_signal(closeadj):
    r = _f01_roc(closeadj, 63)
    result = _safe_div(r, _std(r, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EWMA of daily log return scaled to horizon
def f01cb_f01_crypto_beta_momentum_ewm_63d_base_v074_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=63, min_periods=21).mean() * 63.0 + _f01_roc(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EWMA of daily log return scaled to horizon
def f01cb_f01_crypto_beta_momentum_ewm_126d_base_v075_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=126, min_periods=42).mean() * 126.0 + _f01_roc(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01cb_f01_crypto_beta_momentum_roc_21d_base_v001_signal,
    f01cb_f01_crypto_beta_momentum_roc_63d_base_v002_signal,
    f01cb_f01_crypto_beta_momentum_roc_126d_base_v003_signal,
    f01cb_f01_crypto_beta_momentum_roc_252d_base_v004_signal,
    f01cb_f01_crypto_beta_momentum_roc_5d_base_v005_signal,
    f01cb_f01_crypto_beta_momentum_logmom_21d_base_v006_signal,
    f01cb_f01_crypto_beta_momentum_logmom_63d_base_v007_signal,
    f01cb_f01_crypto_beta_momentum_logmom_126d_base_v008_signal,
    f01cb_f01_crypto_beta_momentum_logmom_252d_base_v009_signal,
    f01cb_f01_crypto_beta_momentum_logmom_504d_base_v010_signal,
    f01cb_f01_crypto_beta_momentum_amp15_21d_base_v011_signal,
    f01cb_f01_crypto_beta_momentum_amp15_63d_base_v012_signal,
    f01cb_f01_crypto_beta_momentum_amp20_21d_base_v013_signal,
    f01cb_f01_crypto_beta_momentum_amp20_63d_base_v014_signal,
    f01cb_f01_crypto_beta_momentum_amp25_126d_base_v015_signal,
    f01cb_f01_crypto_beta_momentum_amp20_252d_base_v016_signal,
    f01cb_f01_crypto_beta_momentum_momqual_21d_base_v017_signal,
    f01cb_f01_crypto_beta_momentum_momqual_63d_base_v018_signal,
    f01cb_f01_crypto_beta_momentum_momqual_126d_base_v019_signal,
    f01cb_f01_crypto_beta_momentum_momqual_252d_base_v020_signal,
    f01cb_f01_crypto_beta_momentum_momqual_42d_base_v021_signal,
    f01cb_f01_crypto_beta_momentum_spread_21_126_base_v022_signal,
    f01cb_f01_crypto_beta_momentum_spread_63_252_base_v023_signal,
    f01cb_f01_crypto_beta_momentum_lspread_21_63_base_v024_signal,
    f01cb_f01_crypto_beta_momentum_zroc_21d_base_v025_signal,
    f01cb_f01_crypto_beta_momentum_zroc_63d_base_v026_signal,
    f01cb_f01_crypto_beta_momentum_zlmom_126d_base_v027_signal,
    f01cb_f01_crypto_beta_momentum_surp_21d_base_v028_signal,
    f01cb_f01_crypto_beta_momentum_surp_63d_base_v029_signal,
    f01cb_f01_crypto_beta_momentum_rank_21d_base_v030_signal,
    f01cb_f01_crypto_beta_momentum_rank_63d_base_v031_signal,
    f01cb_f01_crypto_beta_momentum_zamp_21d_base_v032_signal,
    f01cb_f01_crypto_beta_momentum_upcapture_63d_base_v033_signal,
    f01cb_f01_crypto_beta_momentum_upcapture_126d_base_v034_signal,
    f01cb_f01_crypto_beta_momentum_volconf_21d_base_v035_signal,
    f01cb_f01_crypto_beta_momentum_dvconf_63d_base_v036_signal,
    f01cb_f01_crypto_beta_momentum_ratio_21_252_base_v037_signal,
    f01cb_f01_crypto_beta_momentum_ratio_42_126_base_v038_signal,
    f01cb_f01_crypto_beta_momentum_glratio_63d_base_v039_signal,
    f01cb_f01_crypto_beta_momentum_glratio_126d_base_v040_signal,
    f01cb_f01_crypto_beta_momentum_accel_21_42_base_v041_signal,
    f01cb_f01_crypto_beta_momentum_accel_42_84_base_v042_signal,
    f01cb_f01_crypto_beta_momentum_accel_63_126_base_v043_signal,
    f01cb_f01_crypto_beta_momentum_amp30_21d_base_v044_signal,
    f01cb_f01_crypto_beta_momentum_amp12_252d_base_v045_signal,
    f01cb_f01_crypto_beta_momentum_logmom_42d_base_v046_signal,
    f01cb_f01_crypto_beta_momentum_logmom_189d_base_v047_signal,
    f01cb_f01_crypto_beta_momentum_logmom_378d_base_v048_signal,
    f01cb_f01_crypto_beta_momentum_roc_42d_base_v049_signal,
    f01cb_f01_crypto_beta_momentum_roc_189d_base_v050_signal,
    f01cb_f01_crypto_beta_momentum_roc_378d_base_v051_signal,
    f01cb_f01_crypto_beta_momentum_roc_504d_base_v052_signal,
    f01cb_f01_crypto_beta_momentum_momqual_504d_base_v053_signal,
    f01cb_f01_crypto_beta_momentum_momqual_189d_base_v054_signal,
    f01cb_f01_crypto_beta_momentum_zroc126_21d_base_v055_signal,
    f01cb_f01_crypto_beta_momentum_zroc63_5d_base_v056_signal,
    f01cb_f01_crypto_beta_momentum_roc_10d_base_v057_signal,
    f01cb_f01_crypto_beta_momentum_logmom_10d_base_v058_signal,
    f01cb_f01_crypto_beta_momentum_amp20_10d_base_v059_signal,
    f01cb_f01_crypto_beta_momentum_momqual_10d_base_v060_signal,
    f01cb_f01_crypto_beta_momentum_smooth_21d_base_v061_signal,
    f01cb_f01_crypto_beta_momentum_smooth_63d_base_v062_signal,
    f01cb_f01_crypto_beta_momentum_smoothamp_21d_base_v063_signal,
    f01cb_f01_crypto_beta_momentum_persistw_63d_base_v064_signal,
    f01cb_f01_crypto_beta_momentum_breadthw_126d_base_v065_signal,
    f01cb_f01_crypto_beta_momentum_ann_63d_base_v066_signal,
    f01cb_f01_crypto_beta_momentum_ann_126d_base_v067_signal,
    f01cb_f01_crypto_beta_momentum_ann_21d_base_v068_signal,
    f01cb_f01_crypto_beta_momentum_convex_63d_base_v069_signal,
    f01cb_f01_crypto_beta_momentum_convex_126d_base_v070_signal,
    f01cb_f01_crypto_beta_momentum_qualclip_252d_base_v071_signal,
    f01cb_f01_crypto_beta_momentum_inforatio_21d_base_v072_signal,
    f01cb_f01_crypto_beta_momentum_inforatio_63d_base_v073_signal,
    f01cb_f01_crypto_beta_momentum_ewm_63d_base_v074_signal,
    f01cb_f01_crypto_beta_momentum_ewm_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_CRYPTO_BETA_MOMENTUM_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f01_crypto_beta_momentum_base_001_075_claude: {n_features} features pass")
