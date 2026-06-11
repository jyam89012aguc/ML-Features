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


# ===== folder domain primitives (parabolic blow-off top) =====
def _f03_stretch(s, w):
    # distance of price above its EMA(w): close/EMA(w) - 1 (parabolic extension)
    ema = s.ewm(span=w, min_periods=max(2, w // 2)).mean()
    return s / ema.replace(0, np.nan) - 1.0


def _f03_convexity(s, w):
    # acceleration of log-price ascent: 2nd difference of log price as a LEVEL,
    # smoothed over w to capture parabolic curvature
    lp = np.log(s.replace(0, np.nan))
    return (lp.diff() - lp.diff().shift(w)) / float(w)


def _f03_climax(h, l, w):
    # daily true range vs trailing average range (volatility-climax intensity)
    rng = (h - l)
    avg = rng.rolling(w, min_periods=max(2, w // 2)).mean()
    return _safe_div(rng, avg) - 1.0


def _f03_extension(s, w):
    # ATR-normalized extension above SMA(w): how many average-daily-moves price sits
    # above its own moving average (vertical-extension exhaustion)
    sma = s.rolling(w, min_periods=max(2, w // 2)).mean()
    atr = s.diff().abs().rolling(w, min_periods=max(2, w // 2)).mean()
    return _safe_div(s - sma, atr)
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ JERK FEATURES 001-150 ============
def f03pb_f03_parabolic_blowoff_top_stretch_10d_jerk_v001_signal(close):
    result = _f03_stretch(close, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretch_21d_jerk_v002_signal(close):
    result = _f03_stretch(close, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretch_50d_jerk_v003_signal(closeadj):
    result = _f03_stretch(closeadj, 50)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretch_100d_jerk_v004_signal(closeadj):
    result = _f03_stretch(closeadj, 100)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretch_200d_jerk_v005_signal(closeadj):
    result = _f03_stretch(closeadj, 200)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretch_5d_jerk_v006_signal(close):
    result = _f03_stretch(close, 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretch_63d_jerk_v007_signal(closeadj):
    result = _f03_stretch(closeadj, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretch_126d_jerk_v008_signal(closeadj):
    result = _f03_stretch(closeadj, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_zstretch_21d_jerk_v009_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 21), 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_zstretch_50d_jerk_v010_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 50), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_zstretch_10d_jerk_v011_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 10), 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_zstretch_100d_jerk_v012_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 100), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_smadist_21d_jerk_v013_signal(close):
    sma = _mean(close, 21)
    result = _safe_div(close - sma, close) + _f03_stretch(close, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_smadist_50d_jerk_v014_signal(closeadj):
    sma = _mean(closeadj, 50)
    result = _safe_div(closeadj - sma, closeadj) + _f03_stretch(closeadj, 50) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_smadist_100d_jerk_v015_signal(closeadj):
    sma = _mean(closeadj, 100)
    result = _safe_div(closeadj - sma, closeadj) + _f03_stretch(closeadj, 100) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_smadist_200d_jerk_v016_signal(closeadj):
    sma = _mean(closeadj, 200)
    result = _safe_div(closeadj - sma, closeadj) + _f03_stretch(closeadj, 200) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_convex_21d_jerk_v017_signal(close):
    result = _f03_convexity(close, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_convex_10d_jerk_v018_signal(close):
    result = _f03_convexity(close, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_convex_42d_jerk_v019_signal(closeadj):
    result = _f03_convexity(closeadj, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_convex_63d_jerk_v020_signal(closeadj):
    result = _f03_convexity(closeadj, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_convex_5d_jerk_v021_signal(close):
    result = _f03_convexity(close, 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_smconvex_21d_jerk_v022_signal(closeadj):
    result = _mean(_f03_convexity(closeadj, 10), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_zconvex_21d_jerk_v023_signal(closeadj):
    result = _z(_f03_convexity(closeadj, 21), 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_zconvex_42d_jerk_v024_signal(closeadj):
    result = _z(_f03_convexity(closeadj, 42), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_climax_21d_jerk_v025_signal(high, low):
    result = _f03_climax(high, low, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_climax_10d_jerk_v026_signal(high, low):
    result = _f03_climax(high, low, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_climax_42d_jerk_v027_signal(high, low):
    result = _f03_climax(high, low, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_climax_63d_jerk_v028_signal(high, low):
    result = _f03_climax(high, low, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_smclimax_10d_jerk_v029_signal(high, low):
    result = _mean(_f03_climax(high, low, 5), 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_zclimax_21d_jerk_v030_signal(high, low):
    result = _z(_f03_climax(high, low, 21), 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_ext_21d_jerk_v031_signal(close):
    result = _f03_extension(close, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_ext_50d_jerk_v032_signal(closeadj):
    result = _f03_extension(closeadj, 50)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_ext_100d_jerk_v033_signal(closeadj):
    result = _f03_extension(closeadj, 100)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_ext_10d_jerk_v034_signal(close):
    result = _f03_extension(close, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_ext_63d_jerk_v035_signal(closeadj):
    result = _f03_extension(closeadj, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_ext_200d_jerk_v036_signal(closeadj):
    result = _f03_extension(closeadj, 200)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_pctb_21d_jerk_v037_signal(close):
    m = _mean(close, 21)
    sd = _std(close, 21)
    result = _safe_div(close - m, 2.0 * sd) + _f03_stretch(close, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_pctb_50d_jerk_v038_signal(closeadj):
    m = _mean(closeadj, 50)
    sd = _std(closeadj, 50)
    result = _safe_div(closeadj - m, 2.0 * sd) + _f03_stretch(closeadj, 50) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_pctb_100d_jerk_v039_signal(closeadj):
    m = _mean(closeadj, 100)
    sd = _std(closeadj, 100)
    result = _safe_div(closeadj - m, 2.0 * sd) + _f03_stretch(closeadj, 100) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_ubdist_21d_jerk_v040_signal(close):
    m = _mean(close, 21)
    sd = _std(close, 21)
    ub = m + 2.0 * sd
    result = _safe_div(close - ub, sd) + _f03_stretch(close, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_ubdist_63d_jerk_v041_signal(closeadj):
    m = _mean(closeadj, 63)
    sd = _std(closeadj, 63)
    ub = m + 2.0 * sd
    result = _safe_div(closeadj - ub, sd) + _f03_stretch(closeadj, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_vvel_5d_jerk_v042_signal(close):
    lr = np.log(close / close.shift(1))
    r = close.pct_change(periods=5)
    vol = _std(lr, 21) * np.sqrt(5.0)
    result = _safe_div(r, vol) + _f03_stretch(close, 5) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_vvel_10d_jerk_v043_signal(close):
    lr = np.log(close / close.shift(1))
    r = close.pct_change(periods=10)
    vol = _std(lr, 42) * np.sqrt(10.0)
    result = _safe_div(r, vol) + _f03_stretch(close, 10) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_vvel_21d_jerk_v044_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    r = closeadj.pct_change(periods=21)
    vol = _std(lr, 63) * np.sqrt(21.0)
    result = _safe_div(r, vol) + _f03_stretch(closeadj, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_blowoff_63d_jerk_v045_signal(closeadj):
    lo = closeadj.rolling(63, min_periods=21).min().replace(0, np.nan)
    result = _safe_div(closeadj - lo, lo) + _f03_stretch(closeadj, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_blowoff_126d_jerk_v046_signal(closeadj):
    lo = closeadj.rolling(126, min_periods=42).min().replace(0, np.nan)
    result = _safe_div(closeadj - lo, lo) + _f03_stretch(closeadj, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_blowoff_252d_jerk_v047_signal(closeadj):
    lo = closeadj.rolling(252, min_periods=84).min().replace(0, np.nan)
    result = _safe_div(closeadj - lo, lo) + _f03_stretch(closeadj, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_exhaust_21d_jerk_v048_signal(close, volume):
    surge = _safe_div(volume, _mean(volume, 63))
    result = _f03_stretch(close, 21) * surge
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_exhaust_50d_jerk_v049_signal(closeadj, volume):
    surge = _safe_div(volume, _mean(volume, 126))
    result = _f03_stretch(closeadj, 50) * surge
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_exhaust_10d_jerk_v050_signal(close, volume):
    dv = close * volume
    surge = _safe_div(dv, _mean(dv, 63))
    result = _f03_stretch(close, 10) * surge
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchratio_10_63_jerk_v051_signal(closeadj):
    result = _f03_stretch(closeadj, 10) - _f03_stretch(closeadj, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchratio_21_126_jerk_v052_signal(closeadj):
    result = _f03_stretch(closeadj, 21) - _f03_stretch(closeadj, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchratio_50_200_jerk_v053_signal(closeadj):
    result = _f03_stretch(closeadj, 50) - _f03_stretch(closeadj, 200)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchaccel_21d_jerk_v054_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    result = st - st.shift(5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchaccel_50d_jerk_v055_signal(closeadj):
    st = _f03_stretch(closeadj, 50)
    result = st - st.shift(10)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_accelint_21d_jerk_v056_signal(closeadj):
    c = _f03_convexity(closeadj, 21)
    result = c.clip(lower=0).rolling(21, min_periods=10).mean()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_accelint_42d_jerk_v057_signal(closeadj):
    c = _f03_convexity(closeadj, 21)
    result = c.clip(lower=0).rolling(42, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchclimax_21d_jerk_v058_signal(close, high, low):
    result = _f03_stretch(close, 21) * (1.0 + _f03_climax(high, low, 21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchclimax_50d_jerk_v059_signal(closeadj, high, low):
    result = _f03_stretch(closeadj, 50) * (1.0 + _f03_climax(high, low, 42))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_extconvex_21d_jerk_v060_signal(closeadj):
    result = _f03_extension(closeadj, 21) * _f03_convexity(closeadj, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_extconvex_50d_jerk_v061_signal(closeadj):
    result = _f03_extension(closeadj, 50) * _f03_convexity(closeadj, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_emagap_21d_jerk_v062_signal(close):
    ema = close.ewm(span=21, min_periods=10).mean()
    atr = close.diff().abs().rolling(21, min_periods=10).mean()
    result = _safe_div(close - ema, atr) + _f03_stretch(close, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_emagap_63d_jerk_v063_signal(closeadj):
    ema = closeadj.ewm(span=63, min_periods=21).mean()
    atr = closeadj.diff().abs().rolling(63, min_periods=21).mean()
    result = _safe_div(closeadj - ema, atr) + _f03_stretch(closeadj, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_rankstretch_21d_jerk_v064_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    result = st.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_rankstretch_50d_jerk_v065_signal(closeadj):
    st = _f03_stretch(closeadj, 50)
    result = st.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_highstretch_21d_jerk_v066_signal(high, closeadj):
    sma = _mean(closeadj, 21)
    result = _safe_div(high - sma, sma) + _f03_stretch(closeadj, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_highstretch_50d_jerk_v067_signal(high, closeadj):
    sma = _mean(closeadj, 50)
    result = _safe_div(high - sma, sma) + _f03_stretch(closeadj, 50) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_curv_21d_jerk_v068_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    result = st - 2.0 * st.shift(5) + st.shift(10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_curv_50d_jerk_v069_signal(closeadj):
    st = _f03_stretch(closeadj, 50)
    result = st - 2.0 * st.shift(10) + st.shift(20)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_climaxconvex_21d_jerk_v070_signal(closeadj, high, low):
    result = _f03_convexity(closeadj, 21) * (1.0 + _f03_climax(high, low, 21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_zstretch10_252_jerk_v071_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 10), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_blowoffatr_42d_jerk_v072_signal(closeadj):
    lo = closeadj.rolling(42, min_periods=21).min()
    atr = closeadj.diff().abs().rolling(42, min_periods=21).mean()
    result = _safe_div(closeadj - lo, atr) + _f03_stretch(closeadj, 42) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchvol_21d_jerk_v073_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 21) * np.sqrt(252.0)
    result = _safe_div(_f03_stretch(closeadj, 21), vol)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchvol_50d_jerk_v074_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 63) * np.sqrt(252.0)
    result = _safe_div(_f03_stretch(closeadj, 50), vol)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchblend_jerk_v075_signal(closeadj):
    result = (_f03_stretch(closeadj, 10) + _f03_stretch(closeadj, 21)
              + _f03_stretch(closeadj, 50)) / 3.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretch_42d_jerk_v076_signal(closeadj):
    result = _f03_stretch(closeadj, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretch_84d_jerk_v077_signal(closeadj):
    result = _f03_stretch(closeadj, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretch_189d_jerk_v078_signal(closeadj):
    result = _f03_stretch(closeadj, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_zstretch_42d_jerk_v079_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 42), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_zstretch_63d_jerk_v080_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_zstretch_126d_jerk_v081_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 126), 504)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_smstretch_21d_jerk_v082_signal(closeadj):
    result = _mean(_f03_stretch(closeadj, 21), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_smstretch_50d_jerk_v083_signal(closeadj):
    result = _mean(_f03_stretch(closeadj, 50), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_convex_84d_jerk_v084_signal(closeadj):
    result = _f03_convexity(closeadj, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_convex_126d_jerk_v085_signal(closeadj):
    result = _f03_convexity(closeadj, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_smconvex_42d_jerk_v086_signal(closeadj):
    result = _mean(_f03_convexity(closeadj, 21), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_zconvex_63d_jerk_v087_signal(closeadj):
    result = _z(_f03_convexity(closeadj, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_climax_84d_jerk_v088_signal(high, low):
    result = _f03_climax(high, low, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_climax_126d_jerk_v089_signal(high, low):
    result = _f03_climax(high, low, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_smclimax_21d_jerk_v090_signal(high, low):
    result = _mean(_f03_climax(high, low, 21), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_zclimax_63d_jerk_v091_signal(high, low):
    result = _z(_f03_climax(high, low, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_ext_42d_jerk_v092_signal(closeadj):
    result = _f03_extension(closeadj, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_ext_84d_jerk_v093_signal(closeadj):
    result = _f03_extension(closeadj, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_ext_126d_jerk_v094_signal(closeadj):
    result = _f03_extension(closeadj, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_zext_21d_jerk_v095_signal(closeadj):
    result = _z(_f03_extension(closeadj, 21), 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_zext_63d_jerk_v096_signal(closeadj):
    result = _z(_f03_extension(closeadj, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_pctb_63d_jerk_v097_signal(closeadj):
    m = _mean(closeadj, 63)
    sd = _std(closeadj, 63)
    result = _safe_div(closeadj - m, 2.0 * sd) + _f03_stretch(closeadj, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_pctb_126d_jerk_v098_signal(closeadj):
    m = _mean(closeadj, 126)
    sd = _std(closeadj, 126)
    result = _safe_div(closeadj - m, 2.0 * sd) + _f03_stretch(closeadj, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_ubdist_126d_jerk_v099_signal(closeadj):
    m = _mean(closeadj, 126)
    sd = _std(closeadj, 126)
    ub = m + 2.0 * sd
    result = _safe_div(closeadj - ub, sd) + _f03_stretch(closeadj, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_vvel_42d_jerk_v100_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    r = closeadj.pct_change(periods=42)
    vol = _std(lr, 84) * np.sqrt(42.0)
    result = _safe_div(r, vol) + _f03_stretch(closeadj, 42) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_vvel_63d_jerk_v101_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    r = closeadj.pct_change(periods=63)
    vol = _std(lr, 126) * np.sqrt(63.0)
    result = _safe_div(r, vol) + _f03_stretch(closeadj, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_blowoff_21d_jerk_v102_signal(closeadj):
    lo = closeadj.rolling(21, min_periods=10).min().replace(0, np.nan)
    result = _safe_div(closeadj - lo, lo) + _f03_stretch(closeadj, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_blowoffatr_84d_jerk_v103_signal(closeadj):
    lo = closeadj.rolling(84, min_periods=42).min()
    atr = closeadj.diff().abs().rolling(84, min_periods=42).mean()
    result = _safe_div(closeadj - lo, atr) + _f03_stretch(closeadj, 84) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_blowoffatr_126d_jerk_v104_signal(closeadj):
    lo = closeadj.rolling(126, min_periods=42).min()
    atr = closeadj.diff().abs().rolling(126, min_periods=42).mean()
    result = _safe_div(closeadj - lo, atr) + _f03_stretch(closeadj, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_exhaustdv_21d_jerk_v105_signal(closeadj, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 126))
    result = _f03_stretch(closeadj, 21) * surge
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_exhaustz_63d_jerk_v106_signal(closeadj, volume):
    result = _f03_stretch(closeadj, 63) * _z(volume, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_extvol_21d_jerk_v107_signal(closeadj, volume):
    surge = _safe_div(volume, _mean(volume, 63))
    result = _f03_extension(closeadj, 21) * surge
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchratio_42_189_jerk_v108_signal(closeadj):
    result = _f03_stretch(closeadj, 42) - _f03_stretch(closeadj, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchaccel_100d_jerk_v109_signal(closeadj):
    st = _f03_stretch(closeadj, 100)
    result = st - st.shift(21)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_accelint_63d_jerk_v110_signal(closeadj):
    c = _f03_convexity(closeadj, 21)
    result = c.clip(lower=0).rolling(63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_accelmag_42d_jerk_v111_signal(closeadj):
    c = _f03_convexity(closeadj, 21).abs()
    result = c.rolling(42, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchclimax_100d_jerk_v112_signal(closeadj, high, low):
    result = _f03_stretch(closeadj, 100) * (1.0 + _f03_climax(high, low, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_extconvex_100d_jerk_v113_signal(closeadj):
    result = _f03_extension(closeadj, 100) * _f03_convexity(closeadj, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_emagap_126d_jerk_v114_signal(closeadj):
    ema = closeadj.ewm(span=126, min_periods=42).mean()
    atr = closeadj.diff().abs().rolling(126, min_periods=42).mean()
    result = _safe_div(closeadj - ema, atr) + _f03_stretch(closeadj, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_rankstretch_100d_jerk_v115_signal(closeadj):
    st = _f03_stretch(closeadj, 100)
    result = st.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_rankext_50d_jerk_v116_signal(closeadj):
    e = _f03_extension(closeadj, 50)
    result = e.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_highstretch_100d_jerk_v117_signal(high, closeadj):
    sma = _mean(closeadj, 100)
    result = _safe_div(high - sma, sma) + _f03_stretch(closeadj, 100) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_curv_100d_jerk_v118_signal(closeadj):
    st = _f03_stretch(closeadj, 100)
    result = st - 2.0 * st.shift(21) + st.shift(42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_climaxconvex_63d_jerk_v119_signal(closeadj, high, low):
    result = _f03_convexity(closeadj, 63) * (1.0 + _f03_climax(high, low, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchvol_100d_jerk_v120_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 126) * np.sqrt(252.0)
    result = _safe_div(_f03_stretch(closeadj, 100), vol)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_extaccel_21d_jerk_v121_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    accel = st - st.shift(5)
    result = _f03_extension(closeadj, 21) * accel
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_blowclimax_63d_jerk_v122_signal(closeadj, high, low):
    lo = closeadj.rolling(63, min_periods=21).min().replace(0, np.nan)
    runup = _safe_div(closeadj - lo, lo)
    result = runup * (1.0 + _f03_climax(high, low, 21))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_convexvol_21d_jerk_v123_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 63)
    result = _safe_div(_f03_convexity(closeadj, 21), vol)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_convexvol_63d_jerk_v124_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 126)
    result = _safe_div(_f03_convexity(closeadj, 63), vol)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchsurp_21d_jerk_v125_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    result = st - _mean(st, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchsurp_50d_jerk_v126_signal(closeadj):
    st = _f03_stretch(closeadj, 50)
    result = st - _mean(st, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_extsurp_21d_jerk_v127_signal(closeadj):
    e = _f03_extension(closeadj, 21)
    result = e - _mean(e, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_climaxsurp_21d_jerk_v128_signal(high, low):
    c = _f03_climax(high, low, 21)
    result = c - _mean(c, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchdisp_63d_jerk_v129_signal(closeadj):
    result = _std(_f03_stretch(closeadj, 21), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchdisp_126d_jerk_v130_signal(closeadj):
    result = _std(_f03_stretch(closeadj, 50), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_convexdisp_63d_jerk_v131_signal(closeadj):
    result = _std(_f03_convexity(closeadj, 21), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_climaxewm_21d_jerk_v132_signal(high, low):
    c = _f03_climax(high, low, 21)
    result = c.ewm(span=21, min_periods=10).mean()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchewm_21d_jerk_v133_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    result = st.ewm(span=21, min_periods=10).mean()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchewm_63d_jerk_v134_signal(closeadj):
    st = _f03_stretch(closeadj, 50)
    result = st.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchpow_21d_jerk_v135_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    result = np.sign(st) * (st.abs() ** 1.5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchpow_50d_jerk_v136_signal(closeadj):
    st = _f03_stretch(closeadj, 50)
    result = np.sign(st) * (st.abs() ** 2.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_ubatr_50d_jerk_v137_signal(closeadj):
    m = _mean(closeadj, 50)
    sd = _std(closeadj, 50)
    ub = m + 2.0 * sd
    atr = closeadj.diff().abs().rolling(50, min_periods=21).mean()
    result = _safe_div(closeadj - ub, atr) + _f03_stretch(closeadj, 50) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_retclimax_21d_jerk_v138_signal(closeadj):
    r = closeadj.pct_change().abs()
    avg = r.rolling(21, min_periods=10).mean()
    result = _safe_div(r, avg) - 1.0 + _f03_stretch(closeadj, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_retclimax_63d_jerk_v139_signal(closeadj):
    r = closeadj.pct_change().abs()
    avg = r.rolling(63, min_periods=21).mean()
    result = _safe_div(r, avg) - 1.0 + _f03_stretch(closeadj, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_paraz_21d_jerk_v140_signal(closeadj):
    sz = _z(_f03_stretch(closeadj, 21), 126)
    cz = _z(_f03_convexity(closeadj, 21), 126)
    result = sz * cz
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_paraz_63d_jerk_v141_signal(closeadj):
    sz = _z(_f03_stretch(closeadj, 63), 252)
    cz = _z(_f03_convexity(closeadj, 63), 252)
    result = sz * cz
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchclimaxz_21d_jerk_v142_signal(closeadj, high, low):
    result = _f03_stretch(closeadj, 21) * _z(_f03_climax(high, low, 21), 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_extdvz_21d_jerk_v143_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f03_extension(closeadj, 21) * _z(dv, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchslope_21d_jerk_v144_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    result = (st - st.shift(10)) / 10.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_stretchslope_50d_jerk_v145_signal(closeadj):
    st = _f03_stretch(closeadj, 50)
    result = (st - st.shift(21)) / 21.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_extblow_126d_jerk_v146_signal(closeadj):
    lo = closeadj.rolling(126, min_periods=42).min().replace(0, np.nan)
    runup = _safe_div(closeadj - lo, lo)
    result = _f03_extension(closeadj, 126) * runup
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_extblend_jerk_v147_signal(closeadj):
    result = (_f03_extension(closeadj, 21) + _f03_extension(closeadj, 63)
              + _f03_extension(closeadj, 126)) / 3.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_convexblend_jerk_v148_signal(closeadj):
    result = (_f03_convexity(closeadj, 10) + _f03_convexity(closeadj, 21)
              + _f03_convexity(closeadj, 42)) / 3.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_exhaustcomp_jerk_v149_signal(closeadj, high, low):
    a = _z(_f03_stretch(closeadj, 21), 126)
    b = _z(_f03_extension(closeadj, 21), 126)
    c = _z(_f03_climax(high, low, 21), 126)
    result = (a + b + c) / 3.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f03pb_f03_parabolic_blowoff_top_triple_21d_jerk_v150_signal(closeadj, high, low):
    result = (_f03_stretch(closeadj, 21) * (1.0 + _f03_convexity(closeadj, 21).abs())
              * (1.0 + _f03_climax(high, low, 21)))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f03pb_f03_parabolic_blowoff_top_stretch_10d_jerk_v001_signal,    f03pb_f03_parabolic_blowoff_top_stretch_21d_jerk_v002_signal,    f03pb_f03_parabolic_blowoff_top_stretch_50d_jerk_v003_signal,    f03pb_f03_parabolic_blowoff_top_stretch_100d_jerk_v004_signal,    f03pb_f03_parabolic_blowoff_top_stretch_200d_jerk_v005_signal,    f03pb_f03_parabolic_blowoff_top_stretch_5d_jerk_v006_signal,    f03pb_f03_parabolic_blowoff_top_stretch_63d_jerk_v007_signal,    f03pb_f03_parabolic_blowoff_top_stretch_126d_jerk_v008_signal,    f03pb_f03_parabolic_blowoff_top_zstretch_21d_jerk_v009_signal,    f03pb_f03_parabolic_blowoff_top_zstretch_50d_jerk_v010_signal,    f03pb_f03_parabolic_blowoff_top_zstretch_10d_jerk_v011_signal,    f03pb_f03_parabolic_blowoff_top_zstretch_100d_jerk_v012_signal,    f03pb_f03_parabolic_blowoff_top_smadist_21d_jerk_v013_signal,    f03pb_f03_parabolic_blowoff_top_smadist_50d_jerk_v014_signal,    f03pb_f03_parabolic_blowoff_top_smadist_100d_jerk_v015_signal,    f03pb_f03_parabolic_blowoff_top_smadist_200d_jerk_v016_signal,    f03pb_f03_parabolic_blowoff_top_convex_21d_jerk_v017_signal,    f03pb_f03_parabolic_blowoff_top_convex_10d_jerk_v018_signal,    f03pb_f03_parabolic_blowoff_top_convex_42d_jerk_v019_signal,    f03pb_f03_parabolic_blowoff_top_convex_63d_jerk_v020_signal,    f03pb_f03_parabolic_blowoff_top_convex_5d_jerk_v021_signal,    f03pb_f03_parabolic_blowoff_top_smconvex_21d_jerk_v022_signal,    f03pb_f03_parabolic_blowoff_top_zconvex_21d_jerk_v023_signal,    f03pb_f03_parabolic_blowoff_top_zconvex_42d_jerk_v024_signal,    f03pb_f03_parabolic_blowoff_top_climax_21d_jerk_v025_signal,    f03pb_f03_parabolic_blowoff_top_climax_10d_jerk_v026_signal,    f03pb_f03_parabolic_blowoff_top_climax_42d_jerk_v027_signal,    f03pb_f03_parabolic_blowoff_top_climax_63d_jerk_v028_signal,    f03pb_f03_parabolic_blowoff_top_smclimax_10d_jerk_v029_signal,    f03pb_f03_parabolic_blowoff_top_zclimax_21d_jerk_v030_signal,    f03pb_f03_parabolic_blowoff_top_ext_21d_jerk_v031_signal,    f03pb_f03_parabolic_blowoff_top_ext_50d_jerk_v032_signal,    f03pb_f03_parabolic_blowoff_top_ext_100d_jerk_v033_signal,    f03pb_f03_parabolic_blowoff_top_ext_10d_jerk_v034_signal,    f03pb_f03_parabolic_blowoff_top_ext_63d_jerk_v035_signal,    f03pb_f03_parabolic_blowoff_top_ext_200d_jerk_v036_signal,    f03pb_f03_parabolic_blowoff_top_pctb_21d_jerk_v037_signal,    f03pb_f03_parabolic_blowoff_top_pctb_50d_jerk_v038_signal,    f03pb_f03_parabolic_blowoff_top_pctb_100d_jerk_v039_signal,    f03pb_f03_parabolic_blowoff_top_ubdist_21d_jerk_v040_signal,    f03pb_f03_parabolic_blowoff_top_ubdist_63d_jerk_v041_signal,    f03pb_f03_parabolic_blowoff_top_vvel_5d_jerk_v042_signal,    f03pb_f03_parabolic_blowoff_top_vvel_10d_jerk_v043_signal,    f03pb_f03_parabolic_blowoff_top_vvel_21d_jerk_v044_signal,    f03pb_f03_parabolic_blowoff_top_blowoff_63d_jerk_v045_signal,    f03pb_f03_parabolic_blowoff_top_blowoff_126d_jerk_v046_signal,    f03pb_f03_parabolic_blowoff_top_blowoff_252d_jerk_v047_signal,    f03pb_f03_parabolic_blowoff_top_exhaust_21d_jerk_v048_signal,    f03pb_f03_parabolic_blowoff_top_exhaust_50d_jerk_v049_signal,    f03pb_f03_parabolic_blowoff_top_exhaust_10d_jerk_v050_signal,    f03pb_f03_parabolic_blowoff_top_stretchratio_10_63_jerk_v051_signal,    f03pb_f03_parabolic_blowoff_top_stretchratio_21_126_jerk_v052_signal,    f03pb_f03_parabolic_blowoff_top_stretchratio_50_200_jerk_v053_signal,    f03pb_f03_parabolic_blowoff_top_stretchaccel_21d_jerk_v054_signal,    f03pb_f03_parabolic_blowoff_top_stretchaccel_50d_jerk_v055_signal,    f03pb_f03_parabolic_blowoff_top_accelint_21d_jerk_v056_signal,    f03pb_f03_parabolic_blowoff_top_accelint_42d_jerk_v057_signal,    f03pb_f03_parabolic_blowoff_top_stretchclimax_21d_jerk_v058_signal,    f03pb_f03_parabolic_blowoff_top_stretchclimax_50d_jerk_v059_signal,    f03pb_f03_parabolic_blowoff_top_extconvex_21d_jerk_v060_signal,    f03pb_f03_parabolic_blowoff_top_extconvex_50d_jerk_v061_signal,    f03pb_f03_parabolic_blowoff_top_emagap_21d_jerk_v062_signal,    f03pb_f03_parabolic_blowoff_top_emagap_63d_jerk_v063_signal,    f03pb_f03_parabolic_blowoff_top_rankstretch_21d_jerk_v064_signal,    f03pb_f03_parabolic_blowoff_top_rankstretch_50d_jerk_v065_signal,    f03pb_f03_parabolic_blowoff_top_highstretch_21d_jerk_v066_signal,    f03pb_f03_parabolic_blowoff_top_highstretch_50d_jerk_v067_signal,    f03pb_f03_parabolic_blowoff_top_curv_21d_jerk_v068_signal,    f03pb_f03_parabolic_blowoff_top_curv_50d_jerk_v069_signal,    f03pb_f03_parabolic_blowoff_top_climaxconvex_21d_jerk_v070_signal,    f03pb_f03_parabolic_blowoff_top_zstretch10_252_jerk_v071_signal,    f03pb_f03_parabolic_blowoff_top_blowoffatr_42d_jerk_v072_signal,    f03pb_f03_parabolic_blowoff_top_stretchvol_21d_jerk_v073_signal,    f03pb_f03_parabolic_blowoff_top_stretchvol_50d_jerk_v074_signal,    f03pb_f03_parabolic_blowoff_top_stretchblend_jerk_v075_signal,    f03pb_f03_parabolic_blowoff_top_stretch_42d_jerk_v076_signal,    f03pb_f03_parabolic_blowoff_top_stretch_84d_jerk_v077_signal,    f03pb_f03_parabolic_blowoff_top_stretch_189d_jerk_v078_signal,    f03pb_f03_parabolic_blowoff_top_zstretch_42d_jerk_v079_signal,    f03pb_f03_parabolic_blowoff_top_zstretch_63d_jerk_v080_signal,    f03pb_f03_parabolic_blowoff_top_zstretch_126d_jerk_v081_signal,    f03pb_f03_parabolic_blowoff_top_smstretch_21d_jerk_v082_signal,    f03pb_f03_parabolic_blowoff_top_smstretch_50d_jerk_v083_signal,    f03pb_f03_parabolic_blowoff_top_convex_84d_jerk_v084_signal,    f03pb_f03_parabolic_blowoff_top_convex_126d_jerk_v085_signal,    f03pb_f03_parabolic_blowoff_top_smconvex_42d_jerk_v086_signal,    f03pb_f03_parabolic_blowoff_top_zconvex_63d_jerk_v087_signal,    f03pb_f03_parabolic_blowoff_top_climax_84d_jerk_v088_signal,    f03pb_f03_parabolic_blowoff_top_climax_126d_jerk_v089_signal,    f03pb_f03_parabolic_blowoff_top_smclimax_21d_jerk_v090_signal,    f03pb_f03_parabolic_blowoff_top_zclimax_63d_jerk_v091_signal,    f03pb_f03_parabolic_blowoff_top_ext_42d_jerk_v092_signal,    f03pb_f03_parabolic_blowoff_top_ext_84d_jerk_v093_signal,    f03pb_f03_parabolic_blowoff_top_ext_126d_jerk_v094_signal,    f03pb_f03_parabolic_blowoff_top_zext_21d_jerk_v095_signal,    f03pb_f03_parabolic_blowoff_top_zext_63d_jerk_v096_signal,    f03pb_f03_parabolic_blowoff_top_pctb_63d_jerk_v097_signal,    f03pb_f03_parabolic_blowoff_top_pctb_126d_jerk_v098_signal,    f03pb_f03_parabolic_blowoff_top_ubdist_126d_jerk_v099_signal,    f03pb_f03_parabolic_blowoff_top_vvel_42d_jerk_v100_signal,    f03pb_f03_parabolic_blowoff_top_vvel_63d_jerk_v101_signal,    f03pb_f03_parabolic_blowoff_top_blowoff_21d_jerk_v102_signal,    f03pb_f03_parabolic_blowoff_top_blowoffatr_84d_jerk_v103_signal,    f03pb_f03_parabolic_blowoff_top_blowoffatr_126d_jerk_v104_signal,    f03pb_f03_parabolic_blowoff_top_exhaustdv_21d_jerk_v105_signal,    f03pb_f03_parabolic_blowoff_top_exhaustz_63d_jerk_v106_signal,    f03pb_f03_parabolic_blowoff_top_extvol_21d_jerk_v107_signal,    f03pb_f03_parabolic_blowoff_top_stretchratio_42_189_jerk_v108_signal,    f03pb_f03_parabolic_blowoff_top_stretchaccel_100d_jerk_v109_signal,    f03pb_f03_parabolic_blowoff_top_accelint_63d_jerk_v110_signal,    f03pb_f03_parabolic_blowoff_top_accelmag_42d_jerk_v111_signal,    f03pb_f03_parabolic_blowoff_top_stretchclimax_100d_jerk_v112_signal,    f03pb_f03_parabolic_blowoff_top_extconvex_100d_jerk_v113_signal,    f03pb_f03_parabolic_blowoff_top_emagap_126d_jerk_v114_signal,    f03pb_f03_parabolic_blowoff_top_rankstretch_100d_jerk_v115_signal,    f03pb_f03_parabolic_blowoff_top_rankext_50d_jerk_v116_signal,    f03pb_f03_parabolic_blowoff_top_highstretch_100d_jerk_v117_signal,    f03pb_f03_parabolic_blowoff_top_curv_100d_jerk_v118_signal,    f03pb_f03_parabolic_blowoff_top_climaxconvex_63d_jerk_v119_signal,    f03pb_f03_parabolic_blowoff_top_stretchvol_100d_jerk_v120_signal,    f03pb_f03_parabolic_blowoff_top_extaccel_21d_jerk_v121_signal,    f03pb_f03_parabolic_blowoff_top_blowclimax_63d_jerk_v122_signal,    f03pb_f03_parabolic_blowoff_top_convexvol_21d_jerk_v123_signal,    f03pb_f03_parabolic_blowoff_top_convexvol_63d_jerk_v124_signal,    f03pb_f03_parabolic_blowoff_top_stretchsurp_21d_jerk_v125_signal,    f03pb_f03_parabolic_blowoff_top_stretchsurp_50d_jerk_v126_signal,    f03pb_f03_parabolic_blowoff_top_extsurp_21d_jerk_v127_signal,    f03pb_f03_parabolic_blowoff_top_climaxsurp_21d_jerk_v128_signal,    f03pb_f03_parabolic_blowoff_top_stretchdisp_63d_jerk_v129_signal,    f03pb_f03_parabolic_blowoff_top_stretchdisp_126d_jerk_v130_signal,    f03pb_f03_parabolic_blowoff_top_convexdisp_63d_jerk_v131_signal,    f03pb_f03_parabolic_blowoff_top_climaxewm_21d_jerk_v132_signal,    f03pb_f03_parabolic_blowoff_top_stretchewm_21d_jerk_v133_signal,    f03pb_f03_parabolic_blowoff_top_stretchewm_63d_jerk_v134_signal,    f03pb_f03_parabolic_blowoff_top_stretchpow_21d_jerk_v135_signal,    f03pb_f03_parabolic_blowoff_top_stretchpow_50d_jerk_v136_signal,    f03pb_f03_parabolic_blowoff_top_ubatr_50d_jerk_v137_signal,    f03pb_f03_parabolic_blowoff_top_retclimax_21d_jerk_v138_signal,    f03pb_f03_parabolic_blowoff_top_retclimax_63d_jerk_v139_signal,    f03pb_f03_parabolic_blowoff_top_paraz_21d_jerk_v140_signal,    f03pb_f03_parabolic_blowoff_top_paraz_63d_jerk_v141_signal,    f03pb_f03_parabolic_blowoff_top_stretchclimaxz_21d_jerk_v142_signal,    f03pb_f03_parabolic_blowoff_top_extdvz_21d_jerk_v143_signal,    f03pb_f03_parabolic_blowoff_top_stretchslope_21d_jerk_v144_signal,    f03pb_f03_parabolic_blowoff_top_stretchslope_50d_jerk_v145_signal,    f03pb_f03_parabolic_blowoff_top_extblow_126d_jerk_v146_signal,    f03pb_f03_parabolic_blowoff_top_extblend_jerk_v147_signal,    f03pb_f03_parabolic_blowoff_top_convexblend_jerk_v148_signal,    f03pb_f03_parabolic_blowoff_top_exhaustcomp_jerk_v149_signal,    f03pb_f03_parabolic_blowoff_top_triple_21d_jerk_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_PARABOLIC_BLOWOFF_TOP_REGISTRY_JERK = REGISTRY

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
    domain_primitives = ('_f03_stretch', '_f03_convexity', '_f03_climax', '_f03_extension')
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
    print("OK f03_parabolic_blowoff_top_" + "3rd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
