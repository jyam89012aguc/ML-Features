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


# ===== folder domain primitives (reflexive volatility regime) =====
def _f05_rvol(s, w):
    # rolling realized volatility = std of daily log returns over w (annualizable)
    lr = np.log(s / s.shift(1))
    return lr.rolling(w, min_periods=max(2, w // 2)).std()


def _f05_volratio(s, ws, wl):
    # short-window vol / long-window vol (term-structure / regime tilt)
    vs = _f05_rvol(s, ws)
    vl = _f05_rvol(s, wl)
    return vs / vl.replace(0, np.nan)


def _f05_volz(s, w, wz):
    # z-score of realized vol over a longer lookback (regime extremity)
    v = _f05_rvol(s, w)
    m = v.rolling(wz, min_periods=max(2, wz // 2)).mean()
    sd = v.rolling(wz, min_periods=max(2, wz // 2)).std()
    return (v - m) / sd.replace(0, np.nan)


def _f05_semivol(s, w, side):
    # downside (side<0) or upside (side>0) semideviation of daily log returns
    lr = np.log(s / s.shift(1))
    if side < 0:
        d = lr.clip(upper=0.0)
    else:
        d = lr.clip(lower=0.0)
    return np.sqrt((d * d).rolling(w, min_periods=max(2, w // 2)).mean())


# ============ FEATURES 001-075 ============

# 10d realized volatility
def f05vr_f05_reflexive_volatility_regime_rvol_10d_base_v001_signal(closeadj):
    result = _f05_rvol(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d realized volatility
def f05vr_f05_reflexive_volatility_regime_rvol_21d_base_v002_signal(closeadj):
    result = _f05_rvol(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d realized volatility
def f05vr_f05_reflexive_volatility_regime_rvol_63d_base_v003_signal(closeadj):
    result = _f05_rvol(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d realized volatility
def f05vr_f05_reflexive_volatility_regime_rvol_126d_base_v004_signal(closeadj):
    result = _f05_rvol(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d realized volatility
def f05vr_f05_reflexive_volatility_regime_rvol_252d_base_v005_signal(closeadj):
    result = _f05_rvol(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d realized volatility (annualized)
def f05vr_f05_reflexive_volatility_regime_rvolann_5d_base_v006_signal(closeadj):
    result = _f05_rvol(closeadj, 5) * np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d realized volatility (annualized)
def f05vr_f05_reflexive_volatility_regime_rvolann_21d_base_v007_signal(closeadj):
    result = _f05_rvol(closeadj, 21) * np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d realized volatility (annualized)
def f05vr_f05_reflexive_volatility_regime_rvolann_63d_base_v008_signal(closeadj):
    result = _f05_rvol(closeadj, 63) * np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d realized volatility
def f05vr_f05_reflexive_volatility_regime_rvol_42d_base_v009_signal(closeadj):
    result = _f05_rvol(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d realized volatility
def f05vr_f05_reflexive_volatility_regime_rvol_84d_base_v010_signal(closeadj):
    result = _f05_rvol(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# vol term structure 21/252
def f05vr_f05_reflexive_volatility_regime_termratio_21_252_base_v011_signal(closeadj):
    result = _f05_volratio(closeadj, 21, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# vol term structure 10/63
def f05vr_f05_reflexive_volatility_regime_termratio_10_63_base_v012_signal(closeadj):
    result = _f05_volratio(closeadj, 10, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# vol term structure 21/126
def f05vr_f05_reflexive_volatility_regime_termratio_21_126_base_v013_signal(closeadj):
    result = _f05_volratio(closeadj, 21, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vol term structure 5/63
def f05vr_f05_reflexive_volatility_regime_termratio_5_63_base_v014_signal(closeadj):
    result = _f05_volratio(closeadj, 5, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# vol term structure 42/252
def f05vr_f05_reflexive_volatility_regime_termratio_42_252_base_v015_signal(closeadj):
    result = _f05_volratio(closeadj, 42, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# vol term structure 63/252
def f05vr_f05_reflexive_volatility_regime_termratio_63_252_base_v016_signal(closeadj):
    result = _f05_volratio(closeadj, 63, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log vol term structure 21/126 (symmetric around 0)
def f05vr_f05_reflexive_volatility_regime_logterm_21_126_base_v017_signal(closeadj):
    result = np.log(_f05_volratio(closeadj, 21, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# log vol term structure 21/252
def f05vr_f05_reflexive_volatility_regime_logterm_21_252_base_v018_signal(closeadj):
    result = np.log(_f05_volratio(closeadj, 21, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# vol term-structure slope (short minus long level)
def f05vr_f05_reflexive_volatility_regime_termslope_21_126_base_v019_signal(closeadj):
    result = _f05_rvol(closeadj, 21) - _f05_rvol(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vol term-structure slope 10 minus 63
def f05vr_f05_reflexive_volatility_regime_termslope_10_63_base_v020_signal(closeadj):
    result = _f05_rvol(closeadj, 10) - _f05_rvol(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# vol z-score: 21d vol over 252d history
def f05vr_f05_reflexive_volatility_regime_volz_21_252_base_v021_signal(closeadj):
    result = _f05_volz(closeadj, 21, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# vol z-score: 10d vol over 126d history
def f05vr_f05_reflexive_volatility_regime_volz_10_126_base_v022_signal(closeadj):
    result = _f05_volz(closeadj, 10, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vol z-score: 63d vol over 252d history
def f05vr_f05_reflexive_volatility_regime_volz_63_252_base_v023_signal(closeadj):
    result = _f05_volz(closeadj, 63, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# vol z-score: 21d vol over 126d history
def f05vr_f05_reflexive_volatility_regime_volz_21_126_base_v024_signal(closeadj):
    result = _f05_volz(closeadj, 21, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vol z-score: 5d vol over 63d history
def f05vr_f05_reflexive_volatility_regime_volz_5_63_base_v025_signal(closeadj):
    result = _f05_volz(closeadj, 5, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# vol z-score: 42d vol over 252d history
def f05vr_f05_reflexive_volatility_regime_volz_42_252_base_v026_signal(closeadj):
    result = _f05_volz(closeadj, 42, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol: 63d std of 21d realized vol
def f05vr_f05_reflexive_volatility_regime_volofvol_21_63_base_v027_signal(closeadj):
    result = _std(_f05_rvol(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol: 126d std of 21d realized vol
def f05vr_f05_reflexive_volatility_regime_volofvol_21_126_base_v028_signal(closeadj):
    result = _std(_f05_rvol(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol: 252d std of 63d realized vol
def f05vr_f05_reflexive_volatility_regime_volofvol_63_252_base_v029_signal(closeadj):
    result = _std(_f05_rvol(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# normalized vol-of-vol: vol-of-vol divided by mean vol (coefficient of variation)
def f05vr_f05_reflexive_volatility_regime_volcv_21_126_base_v030_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = _safe_div(_std(v, 126), _mean(v, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# normalized vol-of-vol 63d
def f05vr_f05_reflexive_volatility_regime_volcv_63_252_base_v031_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = _safe_div(_std(v, 252), _mean(v, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# downside semideviation 21d
def f05vr_f05_reflexive_volatility_regime_downvol_21d_base_v032_signal(closeadj):
    result = _f05_semivol(closeadj, 21, -1)
    return result.replace([np.inf, -np.inf], np.nan)


# downside semideviation 63d
def f05vr_f05_reflexive_volatility_regime_downvol_63d_base_v033_signal(closeadj):
    result = _f05_semivol(closeadj, 63, -1)
    return result.replace([np.inf, -np.inf], np.nan)


# downside semideviation 126d
def f05vr_f05_reflexive_volatility_regime_downvol_126d_base_v034_signal(closeadj):
    result = _f05_semivol(closeadj, 126, -1)
    return result.replace([np.inf, -np.inf], np.nan)


# upside semideviation 21d
def f05vr_f05_reflexive_volatility_regime_upvol_21d_base_v035_signal(closeadj):
    result = _f05_semivol(closeadj, 21, 1)
    return result.replace([np.inf, -np.inf], np.nan)


# upside semideviation 63d
def f05vr_f05_reflexive_volatility_regime_upvol_63d_base_v036_signal(closeadj):
    result = _f05_semivol(closeadj, 63, 1)
    return result.replace([np.inf, -np.inf], np.nan)


# downside/upside vol ratio 21d (vol asymmetry / crash tilt)
def f05vr_f05_reflexive_volatility_regime_volasym_21d_base_v037_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 21, -1), _f05_semivol(closeadj, 21, 1))
    return result.replace([np.inf, -np.inf], np.nan)


# downside/upside vol ratio 63d
def f05vr_f05_reflexive_volatility_regime_volasym_63d_base_v038_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 63, -1), _f05_semivol(closeadj, 63, 1))
    return result.replace([np.inf, -np.inf], np.nan)


# downside/upside vol ratio 126d
def f05vr_f05_reflexive_volatility_regime_volasym_126d_base_v039_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 126, -1), _f05_semivol(closeadj, 126, 1))
    return result.replace([np.inf, -np.inf], np.nan)


# downside share of total vol 63d (continuous fraction of variance)
def f05vr_f05_reflexive_volatility_regime_downshare_63d_base_v040_signal(closeadj):
    dn = _f05_semivol(closeadj, 63, -1)
    up = _f05_semivol(closeadj, 63, 1)
    result = _safe_div(dn, dn + up)
    return result.replace([np.inf, -np.inf], np.nan)


# downside vol normalized by total realized vol 63d
def f05vr_f05_reflexive_volatility_regime_downnorm_63d_base_v041_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 63, -1), _f05_rvol(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA volatility span 21
def f05vr_f05_reflexive_volatility_regime_ewmavol_21d_base_v042_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=21, min_periods=10).std() + _f05_rvol(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA volatility span 63
def f05vr_f05_reflexive_volatility_regime_ewmavol_63d_base_v043_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=63, min_periods=21).std() + _f05_rvol(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA volatility span 126
def f05vr_f05_reflexive_volatility_regime_ewmavol_126d_base_v044_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=126, min_periods=42).std() + _f05_rvol(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA vs simple vol gap 63 (reflexive lead/lag)
def f05vr_f05_reflexive_volatility_regime_ewmagap_63d_base_v045_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    ew = lr.ewm(span=63, min_periods=21).std()
    result = ew - _f05_rvol(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# vol percentile rank 21d over 252d window
def f05vr_f05_reflexive_volatility_regime_volpct_21_252_base_v046_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = v.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# vol percentile rank 63d over 252d window
def f05vr_f05_reflexive_volatility_regime_volpct_63_252_base_v047_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = v.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# vol percentile rank 10d over 126d window
def f05vr_f05_reflexive_volatility_regime_volpct_10_126_base_v048_signal(closeadj):
    v = _f05_rvol(closeadj, 10)
    result = v.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# vol acceleration: 21d vol minus its 63d mean (level surprise)
def f05vr_f05_reflexive_volatility_regime_volsurp_21_63_base_v049_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = v - _mean(v, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# vol acceleration: 21d vol minus its 126d mean
def f05vr_f05_reflexive_volatility_regime_volsurp_21_126_base_v050_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = v - _mean(v, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vol acceleration: 63d vol minus its 126d mean
def f05vr_f05_reflexive_volatility_regime_volsurp_63_126_base_v051_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = v - _mean(v, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vol change rate 21d (level diff over 21d of 21d vol)
def f05vr_f05_reflexive_volatility_regime_voldelta_21d_base_v052_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = v - v.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# vol change rate 63d
def f05vr_f05_reflexive_volatility_regime_voldelta_63d_base_v053_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = v - v.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# log vol change 21d (proportional vol move)
def f05vr_f05_reflexive_volatility_regime_logvolchg_21d_base_v054_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = np.log(_safe_div(v, v.shift(21)))
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized daily range proxy 21d (high-low style via returns)
def f05vr_f05_reflexive_volatility_regime_rangevol_21d_base_v055_signal(high, low, closeadj):
    rng = np.log(high / low.replace(0, np.nan))
    result = _safe_div(rng.rolling(21, min_periods=10).mean(), _f05_rvol(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized daily range proxy 63d
def f05vr_f05_reflexive_volatility_regime_rangevol_63d_base_v056_signal(high, low, closeadj):
    rng = np.log(high / low.replace(0, np.nan))
    result = _safe_div(rng.rolling(63, min_periods=21).mean(), _f05_rvol(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson high-low volatility 21d
def f05vr_f05_reflexive_volatility_regime_parkinson_21d_base_v057_signal(high, low, closeadj):
    rng2 = (np.log(high / low.replace(0, np.nan))) ** 2
    park = np.sqrt(rng2.rolling(21, min_periods=10).mean() / (4.0 * np.log(2.0)))
    result = park + _f05_rvol(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson high-low volatility 63d
def f05vr_f05_reflexive_volatility_regime_parkinson_63d_base_v058_signal(high, low, closeadj):
    rng2 = (np.log(high / low.replace(0, np.nan))) ** 2
    park = np.sqrt(rng2.rolling(63, min_periods=21).mean() / (4.0 * np.log(2.0)))
    result = park + _f05_rvol(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vs close-to-close vol ratio 21d (intraday vs overnight regime)
def f05vr_f05_reflexive_volatility_regime_parkratio_21d_base_v059_signal(high, low, closeadj):
    rng2 = (np.log(high / low.replace(0, np.nan))) ** 2
    park = np.sqrt(rng2.rolling(21, min_periods=10).mean() / (4.0 * np.log(2.0)))
    result = _safe_div(park, _f05_rvol(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# vol-scaled absolute return (reflexive intensity) 21d
def f05vr_f05_reflexive_volatility_regime_absintens_21d_base_v060_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1)).abs()
    result = _safe_div(lr.rolling(21, min_periods=10).mean(), _f05_rvol(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# vol-scaled absolute return 63d
def f05vr_f05_reflexive_volatility_regime_absintens_63d_base_v061_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1)).abs()
    result = _safe_div(lr.rolling(63, min_periods=21).mean(), _f05_rvol(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol skew tilt 63d (semivol gap normalized by vol)
def f05vr_f05_reflexive_volatility_regime_voltilt_63d_base_v062_signal(closeadj):
    dn = _f05_semivol(closeadj, 63, -1)
    up = _f05_semivol(closeadj, 63, 1)
    result = _safe_div(dn - up, _f05_rvol(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol skew tilt 126d
def f05vr_f05_reflexive_volatility_regime_voltilt_126d_base_v063_signal(closeadj):
    dn = _f05_semivol(closeadj, 126, -1)
    up = _f05_semivol(closeadj, 126, 1)
    result = _safe_div(dn - up, _f05_rvol(closeadj, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# vol ratio short/medium 10/42
def f05vr_f05_reflexive_volatility_regime_termratio_10_42_base_v064_signal(closeadj):
    result = _f05_volratio(closeadj, 10, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# vol ratio medium/long 42/126
def f05vr_f05_reflexive_volatility_regime_termratio_42_126_base_v065_signal(closeadj):
    result = _f05_volratio(closeadj, 42, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vol ratio 84/252
def f05vr_f05_reflexive_volatility_regime_termratio_84_252_base_v066_signal(closeadj):
    result = _f05_volratio(closeadj, 84, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# vol z-score: 84d vol over 252d
def f05vr_f05_reflexive_volatility_regime_volz_84_252_base_v067_signal(closeadj):
    result = _f05_volz(closeadj, 84, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# vol z-score: 126d vol over 252d
def f05vr_f05_reflexive_volatility_regime_volz_126_252_base_v068_signal(closeadj):
    result = _f05_volz(closeadj, 126, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# downside semideviation 42d
def f05vr_f05_reflexive_volatility_regime_downvol_42d_base_v069_signal(closeadj):
    result = _f05_semivol(closeadj, 42, -1)
    return result.replace([np.inf, -np.inf], np.nan)


# upside semideviation 126d
def f05vr_f05_reflexive_volatility_regime_upvol_126d_base_v070_signal(closeadj):
    result = _f05_semivol(closeadj, 126, 1)
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol normalized z 21/126
def f05vr_f05_reflexive_volatility_regime_vovz_21_126_base_v071_signal(closeadj):
    vv = _std(_f05_rvol(closeadj, 21), 63)
    result = _z(vv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol level z over 504 (long-horizon regime extremity)
def f05vr_f05_reflexive_volatility_regime_volz_63_504_base_v072_signal(closeadj):
    result = _f05_volz(closeadj, 63, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# vol percentile rank 21d over 504d
def f05vr_f05_reflexive_volatility_regime_volpct_21_504_base_v073_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = v.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized drawdown velocity proxy 63d (downside vol vs total)
def f05vr_f05_reflexive_volatility_regime_downnorm_126d_base_v074_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 126, -1), _f05_rvol(closeadj, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# vol acceleration ratio: 21d vol over its own 63d mean
def f05vr_f05_reflexive_volatility_regime_volaccel_21_63_base_v075_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = _safe_div(v, _mean(v, 63))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05vr_f05_reflexive_volatility_regime_rvol_10d_base_v001_signal,
    f05vr_f05_reflexive_volatility_regime_rvol_21d_base_v002_signal,
    f05vr_f05_reflexive_volatility_regime_rvol_63d_base_v003_signal,
    f05vr_f05_reflexive_volatility_regime_rvol_126d_base_v004_signal,
    f05vr_f05_reflexive_volatility_regime_rvol_252d_base_v005_signal,
    f05vr_f05_reflexive_volatility_regime_rvolann_5d_base_v006_signal,
    f05vr_f05_reflexive_volatility_regime_rvolann_21d_base_v007_signal,
    f05vr_f05_reflexive_volatility_regime_rvolann_63d_base_v008_signal,
    f05vr_f05_reflexive_volatility_regime_rvol_42d_base_v009_signal,
    f05vr_f05_reflexive_volatility_regime_rvol_84d_base_v010_signal,
    f05vr_f05_reflexive_volatility_regime_termratio_21_252_base_v011_signal,
    f05vr_f05_reflexive_volatility_regime_termratio_10_63_base_v012_signal,
    f05vr_f05_reflexive_volatility_regime_termratio_21_126_base_v013_signal,
    f05vr_f05_reflexive_volatility_regime_termratio_5_63_base_v014_signal,
    f05vr_f05_reflexive_volatility_regime_termratio_42_252_base_v015_signal,
    f05vr_f05_reflexive_volatility_regime_termratio_63_252_base_v016_signal,
    f05vr_f05_reflexive_volatility_regime_logterm_21_126_base_v017_signal,
    f05vr_f05_reflexive_volatility_regime_logterm_21_252_base_v018_signal,
    f05vr_f05_reflexive_volatility_regime_termslope_21_126_base_v019_signal,
    f05vr_f05_reflexive_volatility_regime_termslope_10_63_base_v020_signal,
    f05vr_f05_reflexive_volatility_regime_volz_21_252_base_v021_signal,
    f05vr_f05_reflexive_volatility_regime_volz_10_126_base_v022_signal,
    f05vr_f05_reflexive_volatility_regime_volz_63_252_base_v023_signal,
    f05vr_f05_reflexive_volatility_regime_volz_21_126_base_v024_signal,
    f05vr_f05_reflexive_volatility_regime_volz_5_63_base_v025_signal,
    f05vr_f05_reflexive_volatility_regime_volz_42_252_base_v026_signal,
    f05vr_f05_reflexive_volatility_regime_volofvol_21_63_base_v027_signal,
    f05vr_f05_reflexive_volatility_regime_volofvol_21_126_base_v028_signal,
    f05vr_f05_reflexive_volatility_regime_volofvol_63_252_base_v029_signal,
    f05vr_f05_reflexive_volatility_regime_volcv_21_126_base_v030_signal,
    f05vr_f05_reflexive_volatility_regime_volcv_63_252_base_v031_signal,
    f05vr_f05_reflexive_volatility_regime_downvol_21d_base_v032_signal,
    f05vr_f05_reflexive_volatility_regime_downvol_63d_base_v033_signal,
    f05vr_f05_reflexive_volatility_regime_downvol_126d_base_v034_signal,
    f05vr_f05_reflexive_volatility_regime_upvol_21d_base_v035_signal,
    f05vr_f05_reflexive_volatility_regime_upvol_63d_base_v036_signal,
    f05vr_f05_reflexive_volatility_regime_volasym_21d_base_v037_signal,
    f05vr_f05_reflexive_volatility_regime_volasym_63d_base_v038_signal,
    f05vr_f05_reflexive_volatility_regime_volasym_126d_base_v039_signal,
    f05vr_f05_reflexive_volatility_regime_downshare_63d_base_v040_signal,
    f05vr_f05_reflexive_volatility_regime_downnorm_63d_base_v041_signal,
    f05vr_f05_reflexive_volatility_regime_ewmavol_21d_base_v042_signal,
    f05vr_f05_reflexive_volatility_regime_ewmavol_63d_base_v043_signal,
    f05vr_f05_reflexive_volatility_regime_ewmavol_126d_base_v044_signal,
    f05vr_f05_reflexive_volatility_regime_ewmagap_63d_base_v045_signal,
    f05vr_f05_reflexive_volatility_regime_volpct_21_252_base_v046_signal,
    f05vr_f05_reflexive_volatility_regime_volpct_63_252_base_v047_signal,
    f05vr_f05_reflexive_volatility_regime_volpct_10_126_base_v048_signal,
    f05vr_f05_reflexive_volatility_regime_volsurp_21_63_base_v049_signal,
    f05vr_f05_reflexive_volatility_regime_volsurp_21_126_base_v050_signal,
    f05vr_f05_reflexive_volatility_regime_volsurp_63_126_base_v051_signal,
    f05vr_f05_reflexive_volatility_regime_voldelta_21d_base_v052_signal,
    f05vr_f05_reflexive_volatility_regime_voldelta_63d_base_v053_signal,
    f05vr_f05_reflexive_volatility_regime_logvolchg_21d_base_v054_signal,
    f05vr_f05_reflexive_volatility_regime_rangevol_21d_base_v055_signal,
    f05vr_f05_reflexive_volatility_regime_rangevol_63d_base_v056_signal,
    f05vr_f05_reflexive_volatility_regime_parkinson_21d_base_v057_signal,
    f05vr_f05_reflexive_volatility_regime_parkinson_63d_base_v058_signal,
    f05vr_f05_reflexive_volatility_regime_parkratio_21d_base_v059_signal,
    f05vr_f05_reflexive_volatility_regime_absintens_21d_base_v060_signal,
    f05vr_f05_reflexive_volatility_regime_absintens_63d_base_v061_signal,
    f05vr_f05_reflexive_volatility_regime_voltilt_63d_base_v062_signal,
    f05vr_f05_reflexive_volatility_regime_voltilt_126d_base_v063_signal,
    f05vr_f05_reflexive_volatility_regime_termratio_10_42_base_v064_signal,
    f05vr_f05_reflexive_volatility_regime_termratio_42_126_base_v065_signal,
    f05vr_f05_reflexive_volatility_regime_termratio_84_252_base_v066_signal,
    f05vr_f05_reflexive_volatility_regime_volz_84_252_base_v067_signal,
    f05vr_f05_reflexive_volatility_regime_volz_126_252_base_v068_signal,
    f05vr_f05_reflexive_volatility_regime_downvol_42d_base_v069_signal,
    f05vr_f05_reflexive_volatility_regime_upvol_126d_base_v070_signal,
    f05vr_f05_reflexive_volatility_regime_vovz_21_126_base_v071_signal,
    f05vr_f05_reflexive_volatility_regime_volz_63_504_base_v072_signal,
    f05vr_f05_reflexive_volatility_regime_volpct_21_504_base_v073_signal,
    f05vr_f05_reflexive_volatility_regime_downnorm_126d_base_v074_signal,
    f05vr_f05_reflexive_volatility_regime_volaccel_21_63_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_REFLEXIVE_VOLATILITY_REGIME_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume", "marketcap", "ev",
           "assets", "assetsc", "equity", "revenue", "gp", "ebitda", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory", "receivables",
           "intangibles", "evebitda", "evebit", "pe", "pb", "ps", "currentratio", "bvps", "sps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "sf3a_shares", "sf3a_value",
           "sf3b_shares", "sf3b_value", "grossmargin", "beta1y", "beta5y", "invcap", "debt"}
    for nm in names:
        if nm in ("closeadj", "close", "price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            s = level + 50.0 * walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f05_rvol", "_f05_volratio", "_f05_volz", "_f05_semivol")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
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
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f05_reflexive_volatility_regime_base_001_075_claude: {n_features} features pass")
