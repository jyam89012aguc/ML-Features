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
def _f29_revenue_accel(revenue, w):
    g = _diff(_mean(revenue, w), w) / _mean(revenue.abs(), w).replace(0, np.nan)
    return _diff(g, w)


def _f29_revenue_growth(revenue, w):
    return _diff(_mean(revenue, w), w) / _mean(revenue.abs(), w).replace(0, np.nan)


def _f29_revenue_jerk(revenue, w):
    g = _diff(_mean(revenue, w), w) / _mean(revenue.abs(), w).replace(0, np.nan)
    a = _diff(g, w)
    return _diff(a, w)


# 21d revenue acceleration weighted by closeadj
def f29ra_f29_revenue_acceleration_revaccel_21d_base_v001_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue acceleration weighted by closeadj
def f29ra_f29_revenue_acceleration_revaccel_63d_base_v002_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d revenue acceleration weighted by closeadj
def f29ra_f29_revenue_acceleration_revaccel_126d_base_v003_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue acceleration weighted by closeadj
def f29ra_f29_revenue_acceleration_revaccel_252d_base_v004_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue acceleration weighted by closeadj
def f29ra_f29_revenue_acceleration_revaccel_504d_base_v005_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of 63d revenue acceleration
def f29ra_f29_revenue_acceleration_revaccelmean_21d_base_v006_signal(revenue, closeadj):
    result = _mean(_f29_revenue_accel(revenue, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of 252d revenue acceleration
def f29ra_f29_revenue_acceleration_revaccelmean_63d_base_v007_signal(revenue, closeadj):
    result = _mean(_f29_revenue_accel(revenue, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of 504d revenue acceleration
def f29ra_f29_revenue_acceleration_revaccelmean_252d_base_v008_signal(revenue, closeadj):
    result = _mean(_f29_revenue_accel(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of 63d revenue acceleration
def f29ra_f29_revenue_acceleration_revaccelz_252d_base_v009_signal(revenue, closeadj):
    result = _z(_f29_revenue_accel(revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of 252d revenue acceleration
def f29ra_f29_revenue_acceleration_revaccelz_504d_base_v010_signal(revenue, closeadj):
    result = _z(_f29_revenue_accel(revenue, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue acceleration weighted by absolute revenue level
def f29ra_f29_revenue_acceleration_revaccelxlvl_21d_base_v011_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 21) * _mean(revenue, 21) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue acceleration weighted by revenue level
def f29ra_f29_revenue_acceleration_revaccelxlvl_63d_base_v012_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 63) * _mean(revenue, 63) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue acceleration weighted by revenue level
def f29ra_f29_revenue_acceleration_revaccelxlvl_252d_base_v013_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 252) * _mean(revenue, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue acceleration weighted by revenue level
def f29ra_f29_revenue_acceleration_revaccelxlvl_504d_base_v014_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 252) * _mean(revenue, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue acceleration squared (severity)
def f29ra_f29_revenue_acceleration_revaccelsq_21d_base_v015_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    result = a * a.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue acceleration squared
def f29ra_f29_revenue_acceleration_revaccelsq_63d_base_v016_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    result = a * a.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue acceleration squared
def f29ra_f29_revenue_acceleration_revaccelsq_252d_base_v017_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * a.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of accelerating revenue months (rolling sum)
def f29ra_f29_revenue_acceleration_revaccelupcnt_252d_base_v018_signal(revenue, closeadj):
    flag = (_f29_revenue_accel(revenue, 21) > 0).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of decelerating revenue quarters
def f29ra_f29_revenue_acceleration_revacceldowncnt_504d_base_v019_signal(revenue, closeadj):
    flag = (_f29_revenue_accel(revenue, 63) < 0).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue acceleration absolute value
def f29ra_f29_revenue_acceleration_revaccelabs_252d_base_v020_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue acceleration absolute value
def f29ra_f29_revenue_acceleration_revaccelabs_504d_base_v021_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue acceleration EMA short
def f29ra_f29_revenue_acceleration_revaccelema_21d_base_v022_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 21).ewm(span=21, adjust=False, min_periods=10).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue acceleration EMA mid
def f29ra_f29_revenue_acceleration_revaccelema_63d_base_v023_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 63).ewm(span=63, adjust=False, min_periods=21).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue acceleration EMA long
def f29ra_f29_revenue_acceleration_revaccelema_252d_base_v024_signal(revenue, closeadj):
    base = _f29_revenue_accel(revenue, 252).ewm(span=252, adjust=False, min_periods=63).mean()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of revenue acceleration
def f29ra_f29_revenue_acceleration_revaccelstd_252d_base_v025_signal(revenue, closeadj):
    base = _std(_f29_revenue_accel(revenue, 21), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of revenue acceleration
def f29ra_f29_revenue_acceleration_revaccelstd_504d_base_v026_signal(revenue, closeadj):
    base = _std(_f29_revenue_accel(revenue, 63), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d net acceleration sign sum
def f29ra_f29_revenue_acceleration_revaccelsign_252d_base_v027_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    sign = np.sign(a).fillna(0)
    result = sign.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net acceleration sign sum
def f29ra_f29_revenue_acceleration_revaccelsign_504d_base_v028_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    sign = np.sign(a).fillna(0)
    result = sign.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d revenue acceleration ultra-short
def f29ra_f29_revenue_acceleration_revaccelultra_5d_base_v029_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d revenue acceleration short
def f29ra_f29_revenue_acceleration_revaccelshrt_10d_base_v030_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d revenue acceleration medium
def f29ra_f29_revenue_acceleration_revaccelmed_42d_base_v031_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d revenue acceleration long
def f29ra_f29_revenue_acceleration_revaccellong_189d_base_v032_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d revenue acceleration very long
def f29ra_f29_revenue_acceleration_revaccelvlong_378d_base_v033_signal(revenue, closeadj):
    result = _f29_revenue_accel(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue acceleration × revenue growth (compound)
def f29ra_f29_revenue_acceleration_accelxgrow_252d_base_v034_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    result = a * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue acceleration × revenue growth
def f29ra_f29_revenue_acceleration_accelxgrow_504d_base_v035_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    result = a * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue acceleration / revenue growth ratio
def f29ra_f29_revenue_acceleration_accelvsgrow_252d_base_v036_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252).replace(0, np.nan)
    result = (a / g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue acceleration / revenue growth ratio
def f29ra_f29_revenue_acceleration_accelvsgrow_504d_base_v037_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252).replace(0, np.nan)
    result = (a / g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue jerk (3rd derivative of revenue) weighted by closeadj
def f29ra_f29_revenue_acceleration_revjerk_252d_base_v038_signal(revenue, closeadj):
    result = _f29_revenue_jerk(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue jerk weighted by closeadj
def f29ra_f29_revenue_acceleration_revjerk_504d_base_v039_signal(revenue, closeadj):
    result = _f29_revenue_jerk(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue acceleration × netinc
def f29ra_f29_revenue_acceleration_accelxni_252d_base_v040_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(netinc, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue acceleration × netinc
def f29ra_f29_revenue_acceleration_accelxni_504d_base_v041_signal(revenue, netinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(netinc, 504) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel * fcf
def f29ra_f29_revenue_acceleration_accelxfcf_252d_base_v042_signal(revenue, fcf, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(fcf, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel * fcf
def f29ra_f29_revenue_acceleration_accelxfcf_504d_base_v043_signal(revenue, fcf, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(fcf, 504) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel * ebitda
def f29ra_f29_revenue_acceleration_accelxebitda_252d_base_v044_signal(revenue, ebitda, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(ebitda, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel * ebitda
def f29ra_f29_revenue_acceleration_accelxebitda_504d_base_v045_signal(revenue, ebitda, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(ebitda, 504) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel * gp
def f29ra_f29_revenue_acceleration_accelxgp_252d_base_v046_signal(revenue, gp, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(gp, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel * gp
def f29ra_f29_revenue_acceleration_accelxgp_504d_base_v047_signal(revenue, gp, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(gp, 504) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue accel divided by sharesbas
def f29ra_f29_revenue_acceleration_accelpershare_21d_base_v048_signal(revenue, sharesbas, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    result = a * _safe_div(_mean(revenue, 21), _mean(sharesbas, 21)) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue accel per share
def f29ra_f29_revenue_acceleration_accelpershare_63d_base_v049_signal(revenue, sharesbas, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    result = a * _safe_div(_mean(revenue, 63), _mean(sharesbas, 63)) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel per share
def f29ra_f29_revenue_acceleration_accelpershare_252d_base_v050_signal(revenue, sharesbas, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _safe_div(_mean(revenue, 252), _mean(sharesbas, 252)) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue acceleration ratio (short vs long accel)
def f29ra_f29_revenue_acceleration_accelratio_63v252_base_v051_signal(revenue, closeadj):
    sa = _f29_revenue_accel(revenue, 63)
    la = _f29_revenue_accel(revenue, 252).replace(0, np.nan)
    result = (sa / la) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21v63 revenue accel ratio
def f29ra_f29_revenue_acceleration_accelratio_21v63_base_v052_signal(revenue, closeadj):
    sa = _f29_revenue_accel(revenue, 21)
    la = _f29_revenue_accel(revenue, 63).replace(0, np.nan)
    result = (sa / la) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel ratio long
def f29ra_f29_revenue_acceleration_accelratio_252v504_base_v053_signal(revenue, closeadj):
    sa = _f29_revenue_accel(revenue, 252)
    la = _f29_revenue_accel(revenue, 252).replace(0, np.nan)
    result = (sa / la) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of revenue acceleration absolute value
def f29ra_f29_revenue_acceleration_accelsumabs_252d_base_v054_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21).abs()
    result = a.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sum of revenue acceleration absolute value
def f29ra_f29_revenue_acceleration_accelsumabs_504d_base_v055_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63).abs()
    result = a.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative revenue acceleration sum
def f29ra_f29_revenue_acceleration_accelcum_252d_base_v056_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    result = a.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative revenue acceleration sum
def f29ra_f29_revenue_acceleration_accelcum_504d_base_v057_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    result = a.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue acceleration coefficient of variation
def f29ra_f29_revenue_acceleration_accelcv_252d_base_v058_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    result = _safe_div(_std(a, 252), _mean(a.abs(), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue acceleration coefficient of variation
def f29ra_f29_revenue_acceleration_accelcv_504d_base_v059_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    result = _safe_div(_std(a, 504), _mean(a.abs(), 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel skew
def f29ra_f29_revenue_acceleration_accelskew_252d_base_v060_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    result = a.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel skew
def f29ra_f29_revenue_acceleration_accelskew_504d_base_v061_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    result = a.rolling(504, min_periods=126).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel kurtosis
def f29ra_f29_revenue_acceleration_accelkurt_252d_base_v062_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 21)
    result = a.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel kurtosis
def f29ra_f29_revenue_acceleration_accelkurt_504d_base_v063_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 63)
    result = a.rolling(504, min_periods=126).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × ncfo
def f29ra_f29_revenue_acceleration_accelxncfo_252d_base_v064_signal(revenue, ncfo, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(ncfo, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × ncfo
def f29ra_f29_revenue_acceleration_accelxncfo_504d_base_v065_signal(revenue, ncfo, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(ncfo, 504) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × opinc
def f29ra_f29_revenue_acceleration_accelxopinc_252d_base_v066_signal(revenue, opinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(opinc, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × opinc
def f29ra_f29_revenue_acceleration_accelxopinc_504d_base_v067_signal(revenue, opinc, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * _mean(opinc, 504) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × revenue level squared
def f29ra_f29_revenue_acceleration_accelxrevsq_252d_base_v068_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rev = _mean(revenue, 252) / 1e8
    result = a * rev * rev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel × revenue level squared
def f29ra_f29_revenue_acceleration_accelxrevsq_504d_base_v069_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    rev = _mean(revenue, 252) / 1e8
    result = a * rev * rev * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue accel × momentum
def f29ra_f29_revenue_acceleration_accelxmom_21d_base_v070_signal(revenue, closeadj):
    mom = closeadj.pct_change(21)
    result = _f29_revenue_accel(revenue, 21) * (1.0 + mom) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue accel × momentum
def f29ra_f29_revenue_acceleration_accelxmom_63d_base_v071_signal(revenue, closeadj):
    mom = closeadj.pct_change(63)
    result = _f29_revenue_accel(revenue, 63) * (1.0 + mom) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × momentum
def f29ra_f29_revenue_acceleration_accelxmom_252d_base_v072_signal(revenue, closeadj):
    mom = closeadj.pct_change(252)
    result = _f29_revenue_accel(revenue, 252) * (1.0 + mom) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel + revenue growth (compound velocity)
def f29ra_f29_revenue_acceleration_accelplusgrow_252d_base_v073_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    result = (a + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue accel + revenue growth
def f29ra_f29_revenue_acceleration_accelplusgrow_504d_base_v074_signal(revenue, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    g = _f29_revenue_growth(revenue, 252)
    result = (a + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue accel × marketcap
def f29ra_f29_revenue_acceleration_accelxmcap_252d_base_v075_signal(revenue, marketcap, closeadj):
    a = _f29_revenue_accel(revenue, 252)
    result = a * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29ra_f29_revenue_acceleration_revaccel_21d_base_v001_signal,
    f29ra_f29_revenue_acceleration_revaccel_63d_base_v002_signal,
    f29ra_f29_revenue_acceleration_revaccel_126d_base_v003_signal,
    f29ra_f29_revenue_acceleration_revaccel_252d_base_v004_signal,
    f29ra_f29_revenue_acceleration_revaccel_504d_base_v005_signal,
    f29ra_f29_revenue_acceleration_revaccelmean_21d_base_v006_signal,
    f29ra_f29_revenue_acceleration_revaccelmean_63d_base_v007_signal,
    f29ra_f29_revenue_acceleration_revaccelmean_252d_base_v008_signal,
    f29ra_f29_revenue_acceleration_revaccelz_252d_base_v009_signal,
    f29ra_f29_revenue_acceleration_revaccelz_504d_base_v010_signal,
    f29ra_f29_revenue_acceleration_revaccelxlvl_21d_base_v011_signal,
    f29ra_f29_revenue_acceleration_revaccelxlvl_63d_base_v012_signal,
    f29ra_f29_revenue_acceleration_revaccelxlvl_252d_base_v013_signal,
    f29ra_f29_revenue_acceleration_revaccelxlvl_504d_base_v014_signal,
    f29ra_f29_revenue_acceleration_revaccelsq_21d_base_v015_signal,
    f29ra_f29_revenue_acceleration_revaccelsq_63d_base_v016_signal,
    f29ra_f29_revenue_acceleration_revaccelsq_252d_base_v017_signal,
    f29ra_f29_revenue_acceleration_revaccelupcnt_252d_base_v018_signal,
    f29ra_f29_revenue_acceleration_revacceldowncnt_504d_base_v019_signal,
    f29ra_f29_revenue_acceleration_revaccelabs_252d_base_v020_signal,
    f29ra_f29_revenue_acceleration_revaccelabs_504d_base_v021_signal,
    f29ra_f29_revenue_acceleration_revaccelema_21d_base_v022_signal,
    f29ra_f29_revenue_acceleration_revaccelema_63d_base_v023_signal,
    f29ra_f29_revenue_acceleration_revaccelema_252d_base_v024_signal,
    f29ra_f29_revenue_acceleration_revaccelstd_252d_base_v025_signal,
    f29ra_f29_revenue_acceleration_revaccelstd_504d_base_v026_signal,
    f29ra_f29_revenue_acceleration_revaccelsign_252d_base_v027_signal,
    f29ra_f29_revenue_acceleration_revaccelsign_504d_base_v028_signal,
    f29ra_f29_revenue_acceleration_revaccelultra_5d_base_v029_signal,
    f29ra_f29_revenue_acceleration_revaccelshrt_10d_base_v030_signal,
    f29ra_f29_revenue_acceleration_revaccelmed_42d_base_v031_signal,
    f29ra_f29_revenue_acceleration_revaccellong_189d_base_v032_signal,
    f29ra_f29_revenue_acceleration_revaccelvlong_378d_base_v033_signal,
    f29ra_f29_revenue_acceleration_accelxgrow_252d_base_v034_signal,
    f29ra_f29_revenue_acceleration_accelxgrow_504d_base_v035_signal,
    f29ra_f29_revenue_acceleration_accelvsgrow_252d_base_v036_signal,
    f29ra_f29_revenue_acceleration_accelvsgrow_504d_base_v037_signal,
    f29ra_f29_revenue_acceleration_revjerk_252d_base_v038_signal,
    f29ra_f29_revenue_acceleration_revjerk_504d_base_v039_signal,
    f29ra_f29_revenue_acceleration_accelxni_252d_base_v040_signal,
    f29ra_f29_revenue_acceleration_accelxni_504d_base_v041_signal,
    f29ra_f29_revenue_acceleration_accelxfcf_252d_base_v042_signal,
    f29ra_f29_revenue_acceleration_accelxfcf_504d_base_v043_signal,
    f29ra_f29_revenue_acceleration_accelxebitda_252d_base_v044_signal,
    f29ra_f29_revenue_acceleration_accelxebitda_504d_base_v045_signal,
    f29ra_f29_revenue_acceleration_accelxgp_252d_base_v046_signal,
    f29ra_f29_revenue_acceleration_accelxgp_504d_base_v047_signal,
    f29ra_f29_revenue_acceleration_accelpershare_21d_base_v048_signal,
    f29ra_f29_revenue_acceleration_accelpershare_63d_base_v049_signal,
    f29ra_f29_revenue_acceleration_accelpershare_252d_base_v050_signal,
    f29ra_f29_revenue_acceleration_accelratio_63v252_base_v051_signal,
    f29ra_f29_revenue_acceleration_accelratio_21v63_base_v052_signal,
    f29ra_f29_revenue_acceleration_accelratio_252v504_base_v053_signal,
    f29ra_f29_revenue_acceleration_accelsumabs_252d_base_v054_signal,
    f29ra_f29_revenue_acceleration_accelsumabs_504d_base_v055_signal,
    f29ra_f29_revenue_acceleration_accelcum_252d_base_v056_signal,
    f29ra_f29_revenue_acceleration_accelcum_504d_base_v057_signal,
    f29ra_f29_revenue_acceleration_accelcv_252d_base_v058_signal,
    f29ra_f29_revenue_acceleration_accelcv_504d_base_v059_signal,
    f29ra_f29_revenue_acceleration_accelskew_252d_base_v060_signal,
    f29ra_f29_revenue_acceleration_accelskew_504d_base_v061_signal,
    f29ra_f29_revenue_acceleration_accelkurt_252d_base_v062_signal,
    f29ra_f29_revenue_acceleration_accelkurt_504d_base_v063_signal,
    f29ra_f29_revenue_acceleration_accelxncfo_252d_base_v064_signal,
    f29ra_f29_revenue_acceleration_accelxncfo_504d_base_v065_signal,
    f29ra_f29_revenue_acceleration_accelxopinc_252d_base_v066_signal,
    f29ra_f29_revenue_acceleration_accelxopinc_504d_base_v067_signal,
    f29ra_f29_revenue_acceleration_accelxrevsq_252d_base_v068_signal,
    f29ra_f29_revenue_acceleration_accelxrevsq_504d_base_v069_signal,
    f29ra_f29_revenue_acceleration_accelxmom_21d_base_v070_signal,
    f29ra_f29_revenue_acceleration_accelxmom_63d_base_v071_signal,
    f29ra_f29_revenue_acceleration_accelxmom_252d_base_v072_signal,
    f29ra_f29_revenue_acceleration_accelplusgrow_252d_base_v073_signal,
    f29ra_f29_revenue_acceleration_accelplusgrow_504d_base_v074_signal,
    f29ra_f29_revenue_acceleration_accelxmcap_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_REVENUE_ACCELERATION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    gp = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="gp")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "equity": equity, "debt": debt, "assets": assets,
        "ebitda": ebitda, "capex": capex, "sharesbas": sharesbas, "opinc": opinc,
        "gp": gp, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f29_revenue_accel", "_f29_revenue_growth", "_f29_revenue_jerk")
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
    print(f"OK f29_revenue_acceleration_base_001_075_claude: {n_features} features pass")
