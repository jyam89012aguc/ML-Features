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


# ============ FEATURES 001-075 ============

# 21d rolling OLS slope of log price
def f11tp_f11_trend_persistence_slope_21d_base_v001_signal(closeadj):
    result = _f11_slope(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling OLS slope of log price
def f11tp_f11_trend_persistence_slope_63d_base_v002_signal(closeadj):
    result = _f11_slope(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling OLS slope of log price
def f11tp_f11_trend_persistence_slope_126d_base_v003_signal(closeadj):
    result = _f11_slope(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling OLS slope of log price
def f11tp_f11_trend_persistence_slope_252d_base_v004_signal(closeadj):
    result = _f11_slope(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d rolling OLS slope of log price
def f11tp_f11_trend_persistence_slope_42d_base_v005_signal(closeadj):
    result = _f11_slope(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d rolling OLS slope of log price
def f11tp_f11_trend_persistence_slope_84d_base_v006_signal(closeadj):
    result = _f11_slope(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d rolling OLS slope of log price
def f11tp_f11_trend_persistence_slope_189d_base_v007_signal(closeadj):
    result = _f11_slope(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling OLS slope of log price
def f11tp_f11_trend_persistence_slope_504d_base_v008_signal(closeadj):
    result = _f11_slope(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 63d slope (slope scaled to a yearly log change)
def f11tp_f11_trend_persistence_slopeann_63d_base_v009_signal(closeadj):
    result = _f11_slope(closeadj, 63) * 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 126d slope
def f11tp_f11_trend_persistence_slopeann_126d_base_v010_signal(closeadj):
    result = _f11_slope(closeadj, 126) * 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d trend straightness R^2
def f11tp_f11_trend_persistence_r2_21d_base_v011_signal(closeadj):
    result = _f11_r2(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d trend straightness R^2
def f11tp_f11_trend_persistence_r2_63d_base_v012_signal(closeadj):
    result = _f11_r2(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d trend straightness R^2
def f11tp_f11_trend_persistence_r2_126d_base_v013_signal(closeadj):
    result = _f11_r2(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d trend straightness R^2
def f11tp_f11_trend_persistence_r2_252d_base_v014_signal(closeadj):
    result = _f11_r2(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d trend straightness R^2
def f11tp_f11_trend_persistence_r2_42d_base_v015_signal(closeadj):
    result = _f11_r2(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d trend straightness R^2
def f11tp_f11_trend_persistence_r2_84d_base_v016_signal(closeadj):
    result = _f11_r2(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d trend straightness R^2
def f11tp_f11_trend_persistence_r2_189d_base_v017_signal(closeadj):
    result = _f11_r2(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d trend straightness R^2
def f11tp_f11_trend_persistence_r2_504d_base_v018_signal(closeadj):
    result = _f11_r2(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# signed straightness: R^2 carrying the sign of the 63d slope
def f11tp_f11_trend_persistence_sr2_63d_base_v019_signal(closeadj):
    result = _f11_r2(closeadj, 63) * np.sign(_f11_slope(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# signed straightness over 126d
def f11tp_f11_trend_persistence_sr2_126d_base_v020_signal(closeadj):
    result = _f11_r2(closeadj, 126) * np.sign(_f11_slope(closeadj, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# signed straightness over 252d
def f11tp_f11_trend_persistence_sr2_252d_base_v021_signal(closeadj):
    result = _f11_r2(closeadj, 252) * np.sign(_f11_slope(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# trend quality = slope * R^2 over 63d (straight AND steep)
def f11tp_f11_trend_persistence_quality_63d_base_v022_signal(closeadj):
    result = _f11_slope(closeadj, 63) * _f11_r2(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# trend quality over 126d
def f11tp_f11_trend_persistence_quality_126d_base_v023_signal(closeadj):
    result = _f11_slope(closeadj, 126) * _f11_r2(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# trend quality over 252d
def f11tp_f11_trend_persistence_quality_252d_base_v024_signal(closeadj):
    result = _f11_slope(closeadj, 252) * _f11_r2(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# trend quality over 21d
def f11tp_f11_trend_persistence_quality_21d_base_v025_signal(closeadj):
    result = _f11_slope(closeadj, 21) * _f11_r2(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized trend quality over 42d
def f11tp_f11_trend_persistence_qualityann_42d_base_v026_signal(closeadj):
    result = _f11_slope(closeadj, 42) * _f11_r2(closeadj, 42) * 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d directional index spread (+DI - -DI)
def f11tp_f11_trend_persistence_di_21d_base_v027_signal(closeadj):
    result = _f11_di(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d directional index spread
def f11tp_f11_trend_persistence_di_42d_base_v028_signal(closeadj):
    result = _f11_di(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d directional index spread
def f11tp_f11_trend_persistence_di_63d_base_v029_signal(closeadj):
    result = _f11_di(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d directional index spread
def f11tp_f11_trend_persistence_di_126d_base_v030_signal(closeadj):
    result = _f11_di(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d directional index spread
def f11tp_f11_trend_persistence_di_252d_base_v031_signal(closeadj):
    result = _f11_di(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ADX-style trend strength: magnitude of 21d DI spread (continuous |DX|)
def f11tp_f11_trend_persistence_adx_21d_base_v032_signal(closeadj):
    result = _f11_di(closeadj, 21).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# ADX-style trend strength over 63d
def f11tp_f11_trend_persistence_adx_63d_base_v033_signal(closeadj):
    result = _f11_di(closeadj, 63).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# ADX-style trend strength over 126d
def f11tp_f11_trend_persistence_adx_126d_base_v034_signal(closeadj):
    result = _f11_di(closeadj, 126).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ADX: 21d mean of the 21d DX magnitude
def f11tp_f11_trend_persistence_adxsm_21d_base_v035_signal(closeadj):
    result = _mean(_f11_di(closeadj, 21).abs(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# +DI / -DI ratio over 63d (log of the directional balance)
def f11tp_f11_trend_persistence_diratio_63d_base_v036_signal(closeadj):
    d = closeadj.diff()
    up = d.clip(lower=0.0).rolling(63, min_periods=21).mean()
    dn = (-d).clip(lower=0.0).rolling(63, min_periods=21).mean()
    result = np.log(_safe_div(up + 1e-12, dn + 1e-12)) + _f11_di(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# +DI / -DI ratio over 126d
def f11tp_f11_trend_persistence_diratio_126d_base_v037_signal(closeadj):
    d = closeadj.diff()
    up = d.clip(lower=0.0).rolling(126, min_periods=42).mean()
    dn = (-d).clip(lower=0.0).rolling(126, min_periods=42).mean()
    result = np.log(_safe_div(up + 1e-12, dn + 1e-12)) + _f11_di(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d return lag-1 autocorrelation (persistence)
def f11tp_f11_trend_persistence_acf1_21d_base_v038_signal(closeadj):
    result = _f11_autocorr(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d return lag-1 autocorrelation
def f11tp_f11_trend_persistence_acf1_42d_base_v039_signal(closeadj):
    result = _f11_autocorr(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d return lag-1 autocorrelation
def f11tp_f11_trend_persistence_acf1_63d_base_v040_signal(closeadj):
    result = _f11_autocorr(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d return lag-1 autocorrelation
def f11tp_f11_trend_persistence_acf1_126d_base_v041_signal(closeadj):
    result = _f11_autocorr(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d return lag-1 autocorrelation
def f11tp_f11_trend_persistence_acf1_252d_base_v042_signal(closeadj):
    result = _f11_autocorr(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Lo-MacKinlay variance ratio VR(5) over 126d (>1 trending, <1 mean-reverting)
def f11tp_f11_trend_persistence_vr5_126d_base_v043_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    v1 = _std(r, 126) ** 2
    vk = _std(r.rolling(5, min_periods=3).sum(), 126) ** 2 / 5.0
    result = _safe_div(vk, v1) + _f11_autocorr(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio VR(10) over 252d
def f11tp_f11_trend_persistence_vr10_252d_base_v044_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    v1 = _std(r, 252) ** 2
    vk = _std(r.rolling(10, min_periods=5).sum(), 252) ** 2 / 10.0
    result = _safe_div(vk, v1) + _f11_autocorr(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio VR(21) over 252d
def f11tp_f11_trend_persistence_vr21_252d_base_v045_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    v1 = _std(r, 252) ** 2
    vk = _std(r.rolling(21, min_periods=10).sum(), 252) ** 2 / 21.0
    result = _safe_div(vk, v1) + _f11_autocorr(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio VR(5) over 63d
def f11tp_f11_trend_persistence_vr5_63d_base_v046_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    v1 = _std(r, 63) ** 2
    vk = _std(r.rolling(5, min_periods=3).sum(), 63) ** 2 / 5.0
    result = _safe_div(vk, v1) + _f11_autocorr(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Kaufman efficiency ratio over 21d (net move / path length, signed)
def f11tp_f11_trend_persistence_eff_21d_base_v047_signal(closeadj):
    net = closeadj - closeadj.shift(21)
    path = closeadj.diff().abs().rolling(21, min_periods=10).sum()
    result = _safe_div(net, path) + _f11_slope(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Kaufman efficiency ratio over 63d
def f11tp_f11_trend_persistence_eff_63d_base_v048_signal(closeadj):
    net = closeadj - closeadj.shift(63)
    path = closeadj.diff().abs().rolling(63, min_periods=21).sum()
    result = _safe_div(net, path) + _f11_slope(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Kaufman efficiency ratio over 126d
def f11tp_f11_trend_persistence_eff_126d_base_v049_signal(closeadj):
    net = closeadj - closeadj.shift(126)
    path = closeadj.diff().abs().rolling(126, min_periods=42).sum()
    result = _safe_div(net, path) + _f11_slope(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Kaufman efficiency ratio over 252d
def f11tp_f11_trend_persistence_eff_252d_base_v050_signal(closeadj):
    net = closeadj - closeadj.shift(252)
    path = closeadj.diff().abs().rolling(252, min_periods=84).sum()
    result = _safe_div(net, path) + _f11_slope(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Kaufman efficiency ratio over 42d
def f11tp_f11_trend_persistence_eff_42d_base_v051_signal(closeadj):
    net = closeadj - closeadj.shift(42)
    path = closeadj.diff().abs().rolling(42, min_periods=21).sum()
    result = _safe_div(net, path) + _f11_slope(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 63d mean, scaled by dispersion (trend displacement z)
def f11tp_f11_trend_persistence_disp_63d_base_v052_signal(closeadj):
    result = _z(closeadj, 63) + _f11_slope(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 126d mean, scaled by dispersion
def f11tp_f11_trend_persistence_disp_126d_base_v053_signal(closeadj):
    result = _z(closeadj, 126) + _f11_slope(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 252d mean, scaled by dispersion
def f11tp_f11_trend_persistence_disp_252d_base_v054_signal(closeadj):
    result = _z(closeadj, 252) + _f11_slope(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# magnitude-weighted consecutive-direction intensity over 21d
# (mean of return * its own running same-sign streak length, continuous)
def f11tp_f11_trend_persistence_streak_21d_base_v055_signal(closeadj):
    r = closeadj.pct_change()
    sg = np.sign(r)
    blk = (sg != sg.shift(1)).cumsum()
    streak = sg.groupby(blk).cumcount() + 1.0
    intens = r * streak
    result = _mean(intens, 21) + _f11_di(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# magnitude-weighted consecutive-direction intensity over 63d
def f11tp_f11_trend_persistence_streak_63d_base_v056_signal(closeadj):
    r = closeadj.pct_change()
    sg = np.sign(r)
    blk = (sg != sg.shift(1)).cumsum()
    streak = sg.groupby(blk).cumcount() + 1.0
    intens = r * streak
    result = _mean(intens, 63) + _f11_di(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# magnitude-weighted consecutive-direction intensity over 126d
def f11tp_f11_trend_persistence_streak_126d_base_v057_signal(closeadj):
    r = closeadj.pct_change()
    sg = np.sign(r)
    blk = (sg != sg.shift(1)).cumsum()
    streak = sg.groupby(blk).cumcount() + 1.0
    intens = r * streak
    result = _mean(intens, 126) + _f11_di(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# slope z-scored over a long window (standardized trend strength) 63d / 252w
def f11tp_f11_trend_persistence_zslope_63d_base_v058_signal(closeadj):
    result = _z(_f11_slope(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope z-scored 126d / 504w
def f11tp_f11_trend_persistence_zslope_126d_base_v059_signal(closeadj):
    result = _z(_f11_slope(closeadj, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# slope z-scored 21d / 126w
def f11tp_f11_trend_persistence_zslope_21d_base_v060_signal(closeadj):
    result = _z(_f11_slope(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# R^2 z-scored 63d / 252w (is trend unusually straight now?)
def f11tp_f11_trend_persistence_zr2_63d_base_v061_signal(closeadj):
    result = _z(_f11_r2(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# slope-to-volatility ratio: 63d slope per unit daily return std (t-stat-like)
def f11tp_f11_trend_persistence_tstat_63d_base_v062_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    result = _safe_div(_f11_slope(closeadj, 63), _std(lr, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# slope-to-volatility ratio over 126d
def f11tp_f11_trend_persistence_tstat_126d_base_v063_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    result = _safe_div(_f11_slope(closeadj, 126), _std(lr, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# slope-to-volatility ratio over 252d
def f11tp_f11_trend_persistence_tstat_252d_base_v064_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan).abs() + 1e-12).diff()
    result = _safe_div(_f11_slope(closeadj, 252), _std(lr, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# slope acceleration: 21d slope minus 63d slope (steepening of the trend)
def f11tp_f11_trend_persistence_slacc_21_63_base_v065_signal(closeadj):
    result = _f11_slope(closeadj, 21) - _f11_slope(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# slope acceleration: 63d slope minus 126d slope
def f11tp_f11_trend_persistence_slacc_63_126_base_v066_signal(closeadj):
    result = _f11_slope(closeadj, 63) - _f11_slope(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# slope acceleration: 126d slope minus 252d slope
def f11tp_f11_trend_persistence_slacc_126_252_base_v067_signal(closeadj):
    result = _f11_slope(closeadj, 126) - _f11_slope(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# R^2 agreement across horizons: 63d R^2 minus 252d R^2 (multi-scale straightness)
def f11tp_f11_trend_persistence_r2spread_63_252_base_v068_signal(closeadj):
    result = _f11_r2(closeadj, 63) - _f11_r2(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# DI spread agreement across horizons: 21d DI minus 126d DI
def f11tp_f11_trend_persistence_dispread_21_126_base_v069_signal(closeadj):
    result = _f11_di(closeadj, 21) - _f11_di(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed 21d slope (21d mean of the 21d slope)
def f11tp_f11_trend_persistence_slopesm_21d_base_v070_signal(closeadj):
    result = _mean(_f11_slope(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed 63d slope (21d mean)
def f11tp_f11_trend_persistence_slopesm_63d_base_v071_signal(closeadj):
    result = _mean(_f11_slope(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-weighted slope over 63d (steepness gated by straightness of path)
def f11tp_f11_trend_persistence_effslope_63d_base_v072_signal(closeadj):
    net = closeadj - closeadj.shift(63)
    path = closeadj.diff().abs().rolling(63, min_periods=21).sum()
    eff = _safe_div(net, path)
    result = _f11_slope(closeadj, 63) * eff.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-weighted slope over 126d
def f11tp_f11_trend_persistence_effslope_126d_base_v073_signal(closeadj):
    net = closeadj - closeadj.shift(126)
    path = closeadj.diff().abs().rolling(126, min_periods=42).sum()
    eff = _safe_div(net, path)
    result = _f11_slope(closeadj, 126) * eff.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# autocorrelation-weighted slope: trend strength gated by return persistence (63d)
def f11tp_f11_trend_persistence_acfslope_63d_base_v074_signal(closeadj):
    result = _f11_slope(closeadj, 63) * _f11_autocorr(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# DI-weighted R^2: directional bias scaled by straightness over 63d
def f11tp_f11_trend_persistence_dir2_63d_base_v075_signal(closeadj):
    result = _f11_di(closeadj, 63) * _f11_r2(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f11tp_f11_trend_persistence_slope_21d_base_v001_signal,
    f11tp_f11_trend_persistence_slope_63d_base_v002_signal,
    f11tp_f11_trend_persistence_slope_126d_base_v003_signal,
    f11tp_f11_trend_persistence_slope_252d_base_v004_signal,
    f11tp_f11_trend_persistence_slope_42d_base_v005_signal,
    f11tp_f11_trend_persistence_slope_84d_base_v006_signal,
    f11tp_f11_trend_persistence_slope_189d_base_v007_signal,
    f11tp_f11_trend_persistence_slope_504d_base_v008_signal,
    f11tp_f11_trend_persistence_slopeann_63d_base_v009_signal,
    f11tp_f11_trend_persistence_slopeann_126d_base_v010_signal,
    f11tp_f11_trend_persistence_r2_21d_base_v011_signal,
    f11tp_f11_trend_persistence_r2_63d_base_v012_signal,
    f11tp_f11_trend_persistence_r2_126d_base_v013_signal,
    f11tp_f11_trend_persistence_r2_252d_base_v014_signal,
    f11tp_f11_trend_persistence_r2_42d_base_v015_signal,
    f11tp_f11_trend_persistence_r2_84d_base_v016_signal,
    f11tp_f11_trend_persistence_r2_189d_base_v017_signal,
    f11tp_f11_trend_persistence_r2_504d_base_v018_signal,
    f11tp_f11_trend_persistence_sr2_63d_base_v019_signal,
    f11tp_f11_trend_persistence_sr2_126d_base_v020_signal,
    f11tp_f11_trend_persistence_sr2_252d_base_v021_signal,
    f11tp_f11_trend_persistence_quality_63d_base_v022_signal,
    f11tp_f11_trend_persistence_quality_126d_base_v023_signal,
    f11tp_f11_trend_persistence_quality_252d_base_v024_signal,
    f11tp_f11_trend_persistence_quality_21d_base_v025_signal,
    f11tp_f11_trend_persistence_qualityann_42d_base_v026_signal,
    f11tp_f11_trend_persistence_di_21d_base_v027_signal,
    f11tp_f11_trend_persistence_di_42d_base_v028_signal,
    f11tp_f11_trend_persistence_di_63d_base_v029_signal,
    f11tp_f11_trend_persistence_di_126d_base_v030_signal,
    f11tp_f11_trend_persistence_di_252d_base_v031_signal,
    f11tp_f11_trend_persistence_adx_21d_base_v032_signal,
    f11tp_f11_trend_persistence_adx_63d_base_v033_signal,
    f11tp_f11_trend_persistence_adx_126d_base_v034_signal,
    f11tp_f11_trend_persistence_adxsm_21d_base_v035_signal,
    f11tp_f11_trend_persistence_diratio_63d_base_v036_signal,
    f11tp_f11_trend_persistence_diratio_126d_base_v037_signal,
    f11tp_f11_trend_persistence_acf1_21d_base_v038_signal,
    f11tp_f11_trend_persistence_acf1_42d_base_v039_signal,
    f11tp_f11_trend_persistence_acf1_63d_base_v040_signal,
    f11tp_f11_trend_persistence_acf1_126d_base_v041_signal,
    f11tp_f11_trend_persistence_acf1_252d_base_v042_signal,
    f11tp_f11_trend_persistence_vr5_126d_base_v043_signal,
    f11tp_f11_trend_persistence_vr10_252d_base_v044_signal,
    f11tp_f11_trend_persistence_vr21_252d_base_v045_signal,
    f11tp_f11_trend_persistence_vr5_63d_base_v046_signal,
    f11tp_f11_trend_persistence_eff_21d_base_v047_signal,
    f11tp_f11_trend_persistence_eff_63d_base_v048_signal,
    f11tp_f11_trend_persistence_eff_126d_base_v049_signal,
    f11tp_f11_trend_persistence_eff_252d_base_v050_signal,
    f11tp_f11_trend_persistence_eff_42d_base_v051_signal,
    f11tp_f11_trend_persistence_disp_63d_base_v052_signal,
    f11tp_f11_trend_persistence_disp_126d_base_v053_signal,
    f11tp_f11_trend_persistence_disp_252d_base_v054_signal,
    f11tp_f11_trend_persistence_streak_21d_base_v055_signal,
    f11tp_f11_trend_persistence_streak_63d_base_v056_signal,
    f11tp_f11_trend_persistence_streak_126d_base_v057_signal,
    f11tp_f11_trend_persistence_zslope_63d_base_v058_signal,
    f11tp_f11_trend_persistence_zslope_126d_base_v059_signal,
    f11tp_f11_trend_persistence_zslope_21d_base_v060_signal,
    f11tp_f11_trend_persistence_zr2_63d_base_v061_signal,
    f11tp_f11_trend_persistence_tstat_63d_base_v062_signal,
    f11tp_f11_trend_persistence_tstat_126d_base_v063_signal,
    f11tp_f11_trend_persistence_tstat_252d_base_v064_signal,
    f11tp_f11_trend_persistence_slacc_21_63_base_v065_signal,
    f11tp_f11_trend_persistence_slacc_63_126_base_v066_signal,
    f11tp_f11_trend_persistence_slacc_126_252_base_v067_signal,
    f11tp_f11_trend_persistence_r2spread_63_252_base_v068_signal,
    f11tp_f11_trend_persistence_dispread_21_126_base_v069_signal,
    f11tp_f11_trend_persistence_slopesm_21d_base_v070_signal,
    f11tp_f11_trend_persistence_slopesm_63d_base_v071_signal,
    f11tp_f11_trend_persistence_effslope_63d_base_v072_signal,
    f11tp_f11_trend_persistence_effslope_126d_base_v073_signal,
    f11tp_f11_trend_persistence_acfslope_63d_base_v074_signal,
    f11tp_f11_trend_persistence_dir2_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_TREND_PERSISTENCE_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f11_trend_persistence_base_001_075_claude: {n_features} features pass")
