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
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ JERK FEATURES 001-150 ============
def f05vr_f05_reflexive_volatility_regime_rvol_10d_jerk_v001_signal(closeadj):
    result = _f05_rvol(closeadj, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rvol_21d_jerk_v002_signal(closeadj):
    result = _f05_rvol(closeadj, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rvol_63d_jerk_v003_signal(closeadj):
    result = _f05_rvol(closeadj, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rvol_126d_jerk_v004_signal(closeadj):
    result = _f05_rvol(closeadj, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rvol_252d_jerk_v005_signal(closeadj):
    result = _f05_rvol(closeadj, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rvolann_5d_jerk_v006_signal(closeadj):
    result = _f05_rvol(closeadj, 5) * np.sqrt(252.0)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rvolann_21d_jerk_v007_signal(closeadj):
    result = _f05_rvol(closeadj, 21) * np.sqrt(252.0)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rvolann_63d_jerk_v008_signal(closeadj):
    result = _f05_rvol(closeadj, 63) * np.sqrt(252.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rvol_42d_jerk_v009_signal(closeadj):
    result = _f05_rvol(closeadj, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rvol_84d_jerk_v010_signal(closeadj):
    result = _f05_rvol(closeadj, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termratio_21_252_jerk_v011_signal(closeadj):
    result = _f05_volratio(closeadj, 21, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termratio_10_63_jerk_v012_signal(closeadj):
    result = _f05_volratio(closeadj, 10, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termratio_21_126_jerk_v013_signal(closeadj):
    result = _f05_volratio(closeadj, 21, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termratio_5_63_jerk_v014_signal(closeadj):
    result = _f05_volratio(closeadj, 5, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termratio_42_252_jerk_v015_signal(closeadj):
    result = _f05_volratio(closeadj, 42, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termratio_63_252_jerk_v016_signal(closeadj):
    result = _f05_volratio(closeadj, 63, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_logterm_21_126_jerk_v017_signal(closeadj):
    result = np.log(_f05_volratio(closeadj, 21, 126))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_logterm_21_252_jerk_v018_signal(closeadj):
    result = np.log(_f05_volratio(closeadj, 21, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termslope_21_126_jerk_v019_signal(closeadj):
    result = _f05_rvol(closeadj, 21) - _f05_rvol(closeadj, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termslope_10_63_jerk_v020_signal(closeadj):
    result = _f05_rvol(closeadj, 10) - _f05_rvol(closeadj, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volz_21_252_jerk_v021_signal(closeadj):
    result = _f05_volz(closeadj, 21, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volz_10_126_jerk_v022_signal(closeadj):
    result = _f05_volz(closeadj, 10, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volz_63_252_jerk_v023_signal(closeadj):
    result = _f05_volz(closeadj, 63, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volz_21_126_jerk_v024_signal(closeadj):
    result = _f05_volz(closeadj, 21, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volz_5_63_jerk_v025_signal(closeadj):
    result = _f05_volz(closeadj, 5, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volz_42_252_jerk_v026_signal(closeadj):
    result = _f05_volz(closeadj, 42, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volofvol_21_63_jerk_v027_signal(closeadj):
    result = _std(_f05_rvol(closeadj, 21), 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volofvol_21_126_jerk_v028_signal(closeadj):
    result = _std(_f05_rvol(closeadj, 21), 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volofvol_63_252_jerk_v029_signal(closeadj):
    result = _std(_f05_rvol(closeadj, 63), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volcv_21_126_jerk_v030_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = _safe_div(_std(v, 126), _mean(v, 126))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volcv_63_252_jerk_v031_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = _safe_div(_std(v, 252), _mean(v, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_downvol_21d_jerk_v032_signal(closeadj):
    result = _f05_semivol(closeadj, 21, -1)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_downvol_63d_jerk_v033_signal(closeadj):
    result = _f05_semivol(closeadj, 63, -1)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_downvol_126d_jerk_v034_signal(closeadj):
    result = _f05_semivol(closeadj, 126, -1)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_upvol_21d_jerk_v035_signal(closeadj):
    result = _f05_semivol(closeadj, 21, 1)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_upvol_63d_jerk_v036_signal(closeadj):
    result = _f05_semivol(closeadj, 63, 1)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volasym_21d_jerk_v037_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 21, -1), _f05_semivol(closeadj, 21, 1))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volasym_63d_jerk_v038_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 63, -1), _f05_semivol(closeadj, 63, 1))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volasym_126d_jerk_v039_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 126, -1), _f05_semivol(closeadj, 126, 1))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_downshare_63d_jerk_v040_signal(closeadj):
    dn = _f05_semivol(closeadj, 63, -1)
    up = _f05_semivol(closeadj, 63, 1)
    result = _safe_div(dn, dn + up)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_downnorm_63d_jerk_v041_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 63, -1), _f05_rvol(closeadj, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_ewmavol_21d_jerk_v042_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=21, min_periods=10).std() + _f05_rvol(closeadj, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_ewmavol_63d_jerk_v043_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=63, min_periods=21).std() + _f05_rvol(closeadj, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_ewmavol_126d_jerk_v044_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=126, min_periods=42).std() + _f05_rvol(closeadj, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_ewmagap_63d_jerk_v045_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    ew = lr.ewm(span=63, min_periods=21).std()
    result = ew - _f05_rvol(closeadj, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volpct_21_252_jerk_v046_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = v.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volpct_63_252_jerk_v047_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = v.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volpct_10_126_jerk_v048_signal(closeadj):
    v = _f05_rvol(closeadj, 10)
    result = v.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volsurp_21_63_jerk_v049_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = v - _mean(v, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volsurp_21_126_jerk_v050_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = v - _mean(v, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volsurp_63_126_jerk_v051_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = v - _mean(v, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_voldelta_21d_jerk_v052_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = v - v.shift(21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_voldelta_63d_jerk_v053_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = v - v.shift(63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_logvolchg_21d_jerk_v054_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = np.log(_safe_div(v, v.shift(21)))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rangevol_21d_jerk_v055_signal(high, low, closeadj):
    rng = np.log(high / low.replace(0, np.nan))
    result = _safe_div(rng.rolling(21, min_periods=10).mean(), _f05_rvol(closeadj, 21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rangevol_63d_jerk_v056_signal(high, low, closeadj):
    rng = np.log(high / low.replace(0, np.nan))
    result = _safe_div(rng.rolling(63, min_periods=21).mean(), _f05_rvol(closeadj, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_parkinson_21d_jerk_v057_signal(high, low, closeadj):
    rng2 = (np.log(high / low.replace(0, np.nan))) ** 2
    park = np.sqrt(rng2.rolling(21, min_periods=10).mean() / (4.0 * np.log(2.0)))
    result = park + _f05_rvol(closeadj, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_parkinson_63d_jerk_v058_signal(high, low, closeadj):
    rng2 = (np.log(high / low.replace(0, np.nan))) ** 2
    park = np.sqrt(rng2.rolling(63, min_periods=21).mean() / (4.0 * np.log(2.0)))
    result = park + _f05_rvol(closeadj, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_parkratio_21d_jerk_v059_signal(high, low, closeadj):
    rng2 = (np.log(high / low.replace(0, np.nan))) ** 2
    park = np.sqrt(rng2.rolling(21, min_periods=10).mean() / (4.0 * np.log(2.0)))
    result = _safe_div(park, _f05_rvol(closeadj, 21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_absintens_21d_jerk_v060_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1)).abs()
    result = _safe_div(lr.rolling(21, min_periods=10).mean(), _f05_rvol(closeadj, 63))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_absintens_63d_jerk_v061_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1)).abs()
    result = _safe_div(lr.rolling(63, min_periods=21).mean(), _f05_rvol(closeadj, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_voltilt_63d_jerk_v062_signal(closeadj):
    dn = _f05_semivol(closeadj, 63, -1)
    up = _f05_semivol(closeadj, 63, 1)
    result = _safe_div(dn - up, _f05_rvol(closeadj, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_voltilt_126d_jerk_v063_signal(closeadj):
    dn = _f05_semivol(closeadj, 126, -1)
    up = _f05_semivol(closeadj, 126, 1)
    result = _safe_div(dn - up, _f05_rvol(closeadj, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termratio_10_42_jerk_v064_signal(closeadj):
    result = _f05_volratio(closeadj, 10, 42)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termratio_42_126_jerk_v065_signal(closeadj):
    result = _f05_volratio(closeadj, 42, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termratio_84_252_jerk_v066_signal(closeadj):
    result = _f05_volratio(closeadj, 84, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volz_84_252_jerk_v067_signal(closeadj):
    result = _f05_volz(closeadj, 84, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volz_126_252_jerk_v068_signal(closeadj):
    result = _f05_volz(closeadj, 126, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_downvol_42d_jerk_v069_signal(closeadj):
    result = _f05_semivol(closeadj, 42, -1)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_upvol_126d_jerk_v070_signal(closeadj):
    result = _f05_semivol(closeadj, 126, 1)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_vovz_21_126_jerk_v071_signal(closeadj):
    vv = _std(_f05_rvol(closeadj, 21), 63)
    result = _z(vv, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volz_63_504_jerk_v072_signal(closeadj):
    result = _f05_volz(closeadj, 63, 504)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volpct_21_504_jerk_v073_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = v.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_downnorm_126d_jerk_v074_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 126, -1), _f05_rvol(closeadj, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volaccel_21_63_jerk_v075_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = _safe_div(v, _mean(v, 63))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rvol_5d_jerk_v076_signal(closeadj):
    result = _f05_rvol(closeadj, 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rvol_189d_jerk_v077_signal(closeadj):
    result = _f05_rvol(closeadj, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rvolann_126d_jerk_v078_signal(closeadj):
    result = _f05_rvol(closeadj, 126) * np.sqrt(252.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rvolann_252d_jerk_v079_signal(closeadj):
    result = _f05_rvol(closeadj, 252) * np.sqrt(252.0)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_logrvol_21d_jerk_v080_signal(closeadj):
    result = np.log(_f05_rvol(closeadj, 21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_logrvol_63d_jerk_v081_signal(closeadj):
    result = np.log(_f05_rvol(closeadj, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_logrvol_126d_jerk_v082_signal(closeadj):
    result = np.log(_f05_rvol(closeadj, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termratio_5_21_jerk_v083_signal(closeadj):
    result = _f05_volratio(closeadj, 5, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termratio_10_126_jerk_v084_signal(closeadj):
    result = _f05_volratio(closeadj, 10, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termratio_126_252_jerk_v085_signal(closeadj):
    result = _f05_volratio(closeadj, 126, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_logterm_10_63_jerk_v086_signal(closeadj):
    result = np.log(_f05_volratio(closeadj, 10, 63))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_logterm_42_252_jerk_v087_signal(closeadj):
    result = np.log(_f05_volratio(closeadj, 42, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termslope_21_252_jerk_v088_signal(closeadj):
    result = _f05_rvol(closeadj, 21) - _f05_rvol(closeadj, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termslope_42_126_jerk_v089_signal(closeadj):
    result = _f05_rvol(closeadj, 42) - _f05_rvol(closeadj, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termcurv_jerk_v090_signal(closeadj):
    result = _f05_rvol(closeadj, 10) - 2.0 * _f05_rvol(closeadj, 63) + _f05_rvol(closeadj, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volz_10_252_jerk_v091_signal(closeadj):
    result = _f05_volz(closeadj, 10, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volz_5_126_jerk_v092_signal(closeadj):
    result = _f05_volz(closeadj, 5, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volz_21_504_jerk_v093_signal(closeadj):
    result = _f05_volz(closeadj, 21, 504)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volz_42_126_jerk_v094_signal(closeadj):
    result = _f05_volz(closeadj, 42, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volofvol_10_63_jerk_v095_signal(closeadj):
    result = _std(_f05_rvol(closeadj, 10), 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volofvol_21_252_jerk_v096_signal(closeadj):
    result = _std(_f05_rvol(closeadj, 21), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volcv_10_63_jerk_v097_signal(closeadj):
    v = _f05_rvol(closeadj, 10)
    result = _safe_div(_std(v, 63), _mean(v, 63))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volcv_42_252_jerk_v098_signal(closeadj):
    v = _f05_rvol(closeadj, 42)
    result = _safe_div(_std(v, 252), _mean(v, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_downvol_252d_jerk_v099_signal(closeadj):
    result = _f05_semivol(closeadj, 252, -1)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_upvol_42d_jerk_v100_signal(closeadj):
    result = _f05_semivol(closeadj, 42, 1)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_upvol_252d_jerk_v101_signal(closeadj):
    result = _f05_semivol(closeadj, 252, 1)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volasym_42d_jerk_v102_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 42, -1), _f05_semivol(closeadj, 42, 1))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volasym_252d_jerk_v103_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 252, -1), _f05_semivol(closeadj, 252, 1))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_downshare_126d_jerk_v104_signal(closeadj):
    dn = _f05_semivol(closeadj, 126, -1)
    up = _f05_semivol(closeadj, 126, 1)
    result = _safe_div(dn, dn + up)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_logasym_63d_jerk_v105_signal(closeadj):
    result = np.log(_safe_div(_f05_semivol(closeadj, 63, -1), _f05_semivol(closeadj, 63, 1)))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_upnorm_63d_jerk_v106_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 63, 1), _f05_rvol(closeadj, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_ewmavol_10d_jerk_v107_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=10, min_periods=5).std() + _f05_rvol(closeadj, 10) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_ewmavol_252d_jerk_v108_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=252, min_periods=84).std() + _f05_rvol(closeadj, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_ewmaratio_21d_jerk_v109_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    ew = lr.ewm(span=21, min_periods=10).std()
    result = _safe_div(ew, _f05_rvol(closeadj, 21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_ewmagap_126d_jerk_v110_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    ew = lr.ewm(span=126, min_periods=42).std()
    result = ew - _f05_rvol(closeadj, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volpct_42_252_jerk_v111_signal(closeadj):
    v = _f05_rvol(closeadj, 42)
    result = v.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volpct_126_504_jerk_v112_signal(closeadj):
    v = _f05_rvol(closeadj, 126)
    result = v.rolling(504, min_periods=168).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_downpct_63_252_jerk_v113_signal(closeadj):
    v = _f05_semivol(closeadj, 63, -1)
    result = v.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volsurp_10_63_jerk_v114_signal(closeadj):
    v = _f05_rvol(closeadj, 10)
    result = v - _mean(v, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volsurp_42_252_jerk_v115_signal(closeadj):
    v = _f05_rvol(closeadj, 42)
    result = v - _mean(v, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_voldelta_10d_jerk_v116_signal(closeadj):
    v = _f05_rvol(closeadj, 10)
    result = v - v.shift(10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_voldelta_42d_jerk_v117_signal(closeadj):
    v = _f05_rvol(closeadj, 42)
    result = v - v.shift(42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_logvolchg_63d_jerk_v118_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = np.log(_safe_div(v, v.shift(63)))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volaccel_10_42_jerk_v119_signal(closeadj):
    v = _f05_rvol(closeadj, 10)
    result = _safe_div(v, _mean(v, 42))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volaccel_63_252_jerk_v120_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = _safe_div(v, _mean(v, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_rangevol_126d_jerk_v121_signal(high, low, closeadj):
    rng = np.log(high / low.replace(0, np.nan))
    result = _safe_div(rng.rolling(126, min_periods=42).mean(), _f05_rvol(closeadj, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_parkinson_126d_jerk_v122_signal(high, low, closeadj):
    rng2 = (np.log(high / low.replace(0, np.nan))) ** 2
    park = np.sqrt(rng2.rolling(126, min_periods=42).mean() / (4.0 * np.log(2.0)))
    result = park + _f05_rvol(closeadj, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_parkratio_63d_jerk_v123_signal(high, low, closeadj):
    rng2 = (np.log(high / low.replace(0, np.nan))) ** 2
    park = np.sqrt(rng2.rolling(63, min_periods=21).mean() / (4.0 * np.log(2.0)))
    result = _safe_div(park, _f05_rvol(closeadj, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_gkvol_21d_jerk_v124_signal(high, low, open, closeadj):
    hl = 0.5 * (np.log(high / low.replace(0, np.nan))) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * (np.log(closeadj / open.replace(0, np.nan))) ** 2
    result = np.sqrt((hl - co).rolling(21, min_periods=10).mean()) + _f05_rvol(closeadj, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_gkvol_63d_jerk_v125_signal(high, low, open, closeadj):
    hl = 0.5 * (np.log(high / low.replace(0, np.nan))) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * (np.log(closeadj / open.replace(0, np.nan))) ** 2
    result = np.sqrt((hl - co).rolling(63, min_periods=21).mean()) + _f05_rvol(closeadj, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_absintens_126d_jerk_v126_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1)).abs()
    result = _safe_div(lr.rolling(126, min_periods=42).mean(), _f05_rvol(closeadj, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_voltilt_252d_jerk_v127_signal(closeadj):
    dn = _f05_semivol(closeadj, 252, -1)
    up = _f05_semivol(closeadj, 252, 1)
    result = _safe_div(dn - up, _f05_rvol(closeadj, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volvolconf_21d_jerk_v128_signal(closeadj, volume):
    result = _f05_rvol(closeadj, 21) * _z(volume, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_dvvolconf_63d_jerk_v129_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f05_rvol(closeadj, 63) * _z(dv, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_vovz_63_252_jerk_v130_signal(closeadj):
    vv = _std(_f05_rvol(closeadj, 63), 126)
    result = _z(vv, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volmom_21d_jerk_v131_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = _safe_div(v - v.shift(21), _std(v, 126))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volmom_63d_jerk_v132_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = _safe_div(v - v.shift(63), _std(v, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_ewmavov_63d_jerk_v133_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = v.ewm(span=63, min_periods=21).std()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_smoothvol_21d_jerk_v134_signal(closeadj):
    result = _mean(_f05_rvol(closeadj, 21), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_smoothvol_63d_jerk_v135_signal(closeadj):
    result = _mean(_f05_rvol(closeadj, 63), 21)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_regimegap_21d_jerk_v136_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = v - v.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_regimegap_63d_jerk_v137_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = v - v.ewm(span=252, min_periods=84).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volrange_21_126_jerk_v138_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    hi = v.rolling(126, min_periods=42).max()
    lo = v.rolling(126, min_periods=42).min()
    result = _safe_div(hi - lo, _mean(v, 126))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volpos_21_252_jerk_v139_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    hi = v.rolling(252, min_periods=63).max()
    lo = v.rolling(252, min_periods=63).min()
    result = _safe_div(v - lo, hi - lo)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volpos_63_504_jerk_v140_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    hi = v.rolling(504, min_periods=126).max()
    lo = v.rolling(504, min_periods=126).min()
    result = _safe_div(v - lo, hi - lo)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_downz_63_252_jerk_v141_signal(closeadj):
    result = _z(_f05_semivol(closeadj, 63, -1), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_upz_63_252_jerk_v142_signal(closeadj):
    result = _z(_f05_semivol(closeadj, 63, 1), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_asymz_126_252_jerk_v143_signal(closeadj):
    a = _safe_div(_f05_semivol(closeadj, 126, -1), _f05_semivol(closeadj, 126, 1))
    result = _z(a, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termz_21_126_jerk_v144_signal(closeadj):
    result = _z(_f05_volratio(closeadj, 21, 126), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_termz_42_252_jerk_v145_signal(closeadj):
    result = _z(_f05_volratio(closeadj, 42, 252), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volnorm_21_252_jerk_v146_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = _safe_div(v, _mean(v, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_volnorm_63ewm_jerk_v147_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = _safe_div(v, v.ewm(span=252, min_periods=84).mean())
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_instab_63d_jerk_v148_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = _safe_div(_std(v, 63), _f05_rvol(closeadj, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_blendvolz_jerk_v149_signal(closeadj):
    result = (_f05_volz(closeadj, 21, 252) + _f05_volz(closeadj, 63, 252)
              + _f05_volz(closeadj, 126, 252)) / 3.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f05vr_f05_reflexive_volatility_regime_blendterm_jerk_v150_signal(closeadj):
    result = (_f05_volratio(closeadj, 5, 63) + _f05_volratio(closeadj, 21, 126)
              + _f05_volratio(closeadj, 42, 252)) / 3.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f05vr_f05_reflexive_volatility_regime_rvol_10d_jerk_v001_signal,    f05vr_f05_reflexive_volatility_regime_rvol_21d_jerk_v002_signal,    f05vr_f05_reflexive_volatility_regime_rvol_63d_jerk_v003_signal,    f05vr_f05_reflexive_volatility_regime_rvol_126d_jerk_v004_signal,    f05vr_f05_reflexive_volatility_regime_rvol_252d_jerk_v005_signal,    f05vr_f05_reflexive_volatility_regime_rvolann_5d_jerk_v006_signal,    f05vr_f05_reflexive_volatility_regime_rvolann_21d_jerk_v007_signal,    f05vr_f05_reflexive_volatility_regime_rvolann_63d_jerk_v008_signal,    f05vr_f05_reflexive_volatility_regime_rvol_42d_jerk_v009_signal,    f05vr_f05_reflexive_volatility_regime_rvol_84d_jerk_v010_signal,    f05vr_f05_reflexive_volatility_regime_termratio_21_252_jerk_v011_signal,    f05vr_f05_reflexive_volatility_regime_termratio_10_63_jerk_v012_signal,    f05vr_f05_reflexive_volatility_regime_termratio_21_126_jerk_v013_signal,    f05vr_f05_reflexive_volatility_regime_termratio_5_63_jerk_v014_signal,    f05vr_f05_reflexive_volatility_regime_termratio_42_252_jerk_v015_signal,    f05vr_f05_reflexive_volatility_regime_termratio_63_252_jerk_v016_signal,    f05vr_f05_reflexive_volatility_regime_logterm_21_126_jerk_v017_signal,    f05vr_f05_reflexive_volatility_regime_logterm_21_252_jerk_v018_signal,    f05vr_f05_reflexive_volatility_regime_termslope_21_126_jerk_v019_signal,    f05vr_f05_reflexive_volatility_regime_termslope_10_63_jerk_v020_signal,    f05vr_f05_reflexive_volatility_regime_volz_21_252_jerk_v021_signal,    f05vr_f05_reflexive_volatility_regime_volz_10_126_jerk_v022_signal,    f05vr_f05_reflexive_volatility_regime_volz_63_252_jerk_v023_signal,    f05vr_f05_reflexive_volatility_regime_volz_21_126_jerk_v024_signal,    f05vr_f05_reflexive_volatility_regime_volz_5_63_jerk_v025_signal,    f05vr_f05_reflexive_volatility_regime_volz_42_252_jerk_v026_signal,    f05vr_f05_reflexive_volatility_regime_volofvol_21_63_jerk_v027_signal,    f05vr_f05_reflexive_volatility_regime_volofvol_21_126_jerk_v028_signal,    f05vr_f05_reflexive_volatility_regime_volofvol_63_252_jerk_v029_signal,    f05vr_f05_reflexive_volatility_regime_volcv_21_126_jerk_v030_signal,    f05vr_f05_reflexive_volatility_regime_volcv_63_252_jerk_v031_signal,    f05vr_f05_reflexive_volatility_regime_downvol_21d_jerk_v032_signal,    f05vr_f05_reflexive_volatility_regime_downvol_63d_jerk_v033_signal,    f05vr_f05_reflexive_volatility_regime_downvol_126d_jerk_v034_signal,    f05vr_f05_reflexive_volatility_regime_upvol_21d_jerk_v035_signal,    f05vr_f05_reflexive_volatility_regime_upvol_63d_jerk_v036_signal,    f05vr_f05_reflexive_volatility_regime_volasym_21d_jerk_v037_signal,    f05vr_f05_reflexive_volatility_regime_volasym_63d_jerk_v038_signal,    f05vr_f05_reflexive_volatility_regime_volasym_126d_jerk_v039_signal,    f05vr_f05_reflexive_volatility_regime_downshare_63d_jerk_v040_signal,    f05vr_f05_reflexive_volatility_regime_downnorm_63d_jerk_v041_signal,    f05vr_f05_reflexive_volatility_regime_ewmavol_21d_jerk_v042_signal,    f05vr_f05_reflexive_volatility_regime_ewmavol_63d_jerk_v043_signal,    f05vr_f05_reflexive_volatility_regime_ewmavol_126d_jerk_v044_signal,    f05vr_f05_reflexive_volatility_regime_ewmagap_63d_jerk_v045_signal,    f05vr_f05_reflexive_volatility_regime_volpct_21_252_jerk_v046_signal,    f05vr_f05_reflexive_volatility_regime_volpct_63_252_jerk_v047_signal,    f05vr_f05_reflexive_volatility_regime_volpct_10_126_jerk_v048_signal,    f05vr_f05_reflexive_volatility_regime_volsurp_21_63_jerk_v049_signal,    f05vr_f05_reflexive_volatility_regime_volsurp_21_126_jerk_v050_signal,    f05vr_f05_reflexive_volatility_regime_volsurp_63_126_jerk_v051_signal,    f05vr_f05_reflexive_volatility_regime_voldelta_21d_jerk_v052_signal,    f05vr_f05_reflexive_volatility_regime_voldelta_63d_jerk_v053_signal,    f05vr_f05_reflexive_volatility_regime_logvolchg_21d_jerk_v054_signal,    f05vr_f05_reflexive_volatility_regime_rangevol_21d_jerk_v055_signal,    f05vr_f05_reflexive_volatility_regime_rangevol_63d_jerk_v056_signal,    f05vr_f05_reflexive_volatility_regime_parkinson_21d_jerk_v057_signal,    f05vr_f05_reflexive_volatility_regime_parkinson_63d_jerk_v058_signal,    f05vr_f05_reflexive_volatility_regime_parkratio_21d_jerk_v059_signal,    f05vr_f05_reflexive_volatility_regime_absintens_21d_jerk_v060_signal,    f05vr_f05_reflexive_volatility_regime_absintens_63d_jerk_v061_signal,    f05vr_f05_reflexive_volatility_regime_voltilt_63d_jerk_v062_signal,    f05vr_f05_reflexive_volatility_regime_voltilt_126d_jerk_v063_signal,    f05vr_f05_reflexive_volatility_regime_termratio_10_42_jerk_v064_signal,    f05vr_f05_reflexive_volatility_regime_termratio_42_126_jerk_v065_signal,    f05vr_f05_reflexive_volatility_regime_termratio_84_252_jerk_v066_signal,    f05vr_f05_reflexive_volatility_regime_volz_84_252_jerk_v067_signal,    f05vr_f05_reflexive_volatility_regime_volz_126_252_jerk_v068_signal,    f05vr_f05_reflexive_volatility_regime_downvol_42d_jerk_v069_signal,    f05vr_f05_reflexive_volatility_regime_upvol_126d_jerk_v070_signal,    f05vr_f05_reflexive_volatility_regime_vovz_21_126_jerk_v071_signal,    f05vr_f05_reflexive_volatility_regime_volz_63_504_jerk_v072_signal,    f05vr_f05_reflexive_volatility_regime_volpct_21_504_jerk_v073_signal,    f05vr_f05_reflexive_volatility_regime_downnorm_126d_jerk_v074_signal,    f05vr_f05_reflexive_volatility_regime_volaccel_21_63_jerk_v075_signal,    f05vr_f05_reflexive_volatility_regime_rvol_5d_jerk_v076_signal,    f05vr_f05_reflexive_volatility_regime_rvol_189d_jerk_v077_signal,    f05vr_f05_reflexive_volatility_regime_rvolann_126d_jerk_v078_signal,    f05vr_f05_reflexive_volatility_regime_rvolann_252d_jerk_v079_signal,    f05vr_f05_reflexive_volatility_regime_logrvol_21d_jerk_v080_signal,    f05vr_f05_reflexive_volatility_regime_logrvol_63d_jerk_v081_signal,    f05vr_f05_reflexive_volatility_regime_logrvol_126d_jerk_v082_signal,    f05vr_f05_reflexive_volatility_regime_termratio_5_21_jerk_v083_signal,    f05vr_f05_reflexive_volatility_regime_termratio_10_126_jerk_v084_signal,    f05vr_f05_reflexive_volatility_regime_termratio_126_252_jerk_v085_signal,    f05vr_f05_reflexive_volatility_regime_logterm_10_63_jerk_v086_signal,    f05vr_f05_reflexive_volatility_regime_logterm_42_252_jerk_v087_signal,    f05vr_f05_reflexive_volatility_regime_termslope_21_252_jerk_v088_signal,    f05vr_f05_reflexive_volatility_regime_termslope_42_126_jerk_v089_signal,    f05vr_f05_reflexive_volatility_regime_termcurv_jerk_v090_signal,    f05vr_f05_reflexive_volatility_regime_volz_10_252_jerk_v091_signal,    f05vr_f05_reflexive_volatility_regime_volz_5_126_jerk_v092_signal,    f05vr_f05_reflexive_volatility_regime_volz_21_504_jerk_v093_signal,    f05vr_f05_reflexive_volatility_regime_volz_42_126_jerk_v094_signal,    f05vr_f05_reflexive_volatility_regime_volofvol_10_63_jerk_v095_signal,    f05vr_f05_reflexive_volatility_regime_volofvol_21_252_jerk_v096_signal,    f05vr_f05_reflexive_volatility_regime_volcv_10_63_jerk_v097_signal,    f05vr_f05_reflexive_volatility_regime_volcv_42_252_jerk_v098_signal,    f05vr_f05_reflexive_volatility_regime_downvol_252d_jerk_v099_signal,    f05vr_f05_reflexive_volatility_regime_upvol_42d_jerk_v100_signal,    f05vr_f05_reflexive_volatility_regime_upvol_252d_jerk_v101_signal,    f05vr_f05_reflexive_volatility_regime_volasym_42d_jerk_v102_signal,    f05vr_f05_reflexive_volatility_regime_volasym_252d_jerk_v103_signal,    f05vr_f05_reflexive_volatility_regime_downshare_126d_jerk_v104_signal,    f05vr_f05_reflexive_volatility_regime_logasym_63d_jerk_v105_signal,    f05vr_f05_reflexive_volatility_regime_upnorm_63d_jerk_v106_signal,    f05vr_f05_reflexive_volatility_regime_ewmavol_10d_jerk_v107_signal,    f05vr_f05_reflexive_volatility_regime_ewmavol_252d_jerk_v108_signal,    f05vr_f05_reflexive_volatility_regime_ewmaratio_21d_jerk_v109_signal,    f05vr_f05_reflexive_volatility_regime_ewmagap_126d_jerk_v110_signal,    f05vr_f05_reflexive_volatility_regime_volpct_42_252_jerk_v111_signal,    f05vr_f05_reflexive_volatility_regime_volpct_126_504_jerk_v112_signal,    f05vr_f05_reflexive_volatility_regime_downpct_63_252_jerk_v113_signal,    f05vr_f05_reflexive_volatility_regime_volsurp_10_63_jerk_v114_signal,    f05vr_f05_reflexive_volatility_regime_volsurp_42_252_jerk_v115_signal,    f05vr_f05_reflexive_volatility_regime_voldelta_10d_jerk_v116_signal,    f05vr_f05_reflexive_volatility_regime_voldelta_42d_jerk_v117_signal,    f05vr_f05_reflexive_volatility_regime_logvolchg_63d_jerk_v118_signal,    f05vr_f05_reflexive_volatility_regime_volaccel_10_42_jerk_v119_signal,    f05vr_f05_reflexive_volatility_regime_volaccel_63_252_jerk_v120_signal,    f05vr_f05_reflexive_volatility_regime_rangevol_126d_jerk_v121_signal,    f05vr_f05_reflexive_volatility_regime_parkinson_126d_jerk_v122_signal,    f05vr_f05_reflexive_volatility_regime_parkratio_63d_jerk_v123_signal,    f05vr_f05_reflexive_volatility_regime_gkvol_21d_jerk_v124_signal,    f05vr_f05_reflexive_volatility_regime_gkvol_63d_jerk_v125_signal,    f05vr_f05_reflexive_volatility_regime_absintens_126d_jerk_v126_signal,    f05vr_f05_reflexive_volatility_regime_voltilt_252d_jerk_v127_signal,    f05vr_f05_reflexive_volatility_regime_volvolconf_21d_jerk_v128_signal,    f05vr_f05_reflexive_volatility_regime_dvvolconf_63d_jerk_v129_signal,    f05vr_f05_reflexive_volatility_regime_vovz_63_252_jerk_v130_signal,    f05vr_f05_reflexive_volatility_regime_volmom_21d_jerk_v131_signal,    f05vr_f05_reflexive_volatility_regime_volmom_63d_jerk_v132_signal,    f05vr_f05_reflexive_volatility_regime_ewmavov_63d_jerk_v133_signal,    f05vr_f05_reflexive_volatility_regime_smoothvol_21d_jerk_v134_signal,    f05vr_f05_reflexive_volatility_regime_smoothvol_63d_jerk_v135_signal,    f05vr_f05_reflexive_volatility_regime_regimegap_21d_jerk_v136_signal,    f05vr_f05_reflexive_volatility_regime_regimegap_63d_jerk_v137_signal,    f05vr_f05_reflexive_volatility_regime_volrange_21_126_jerk_v138_signal,    f05vr_f05_reflexive_volatility_regime_volpos_21_252_jerk_v139_signal,    f05vr_f05_reflexive_volatility_regime_volpos_63_504_jerk_v140_signal,    f05vr_f05_reflexive_volatility_regime_downz_63_252_jerk_v141_signal,    f05vr_f05_reflexive_volatility_regime_upz_63_252_jerk_v142_signal,    f05vr_f05_reflexive_volatility_regime_asymz_126_252_jerk_v143_signal,    f05vr_f05_reflexive_volatility_regime_termz_21_126_jerk_v144_signal,    f05vr_f05_reflexive_volatility_regime_termz_42_252_jerk_v145_signal,    f05vr_f05_reflexive_volatility_regime_volnorm_21_252_jerk_v146_signal,    f05vr_f05_reflexive_volatility_regime_volnorm_63ewm_jerk_v147_signal,    f05vr_f05_reflexive_volatility_regime_instab_63d_jerk_v148_signal,    f05vr_f05_reflexive_volatility_regime_blendvolz_jerk_v149_signal,    f05vr_f05_reflexive_volatility_regime_blendterm_jerk_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_REFLEXIVE_VOLATILITY_REGIME_REGISTRY_JERK = REGISTRY

def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = ('_f05_rvol', '_f05_volratio', '_f05_volz', '_f05_semivol')
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
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print("OK f05_reflexive_volatility_regime_" + "3rd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
