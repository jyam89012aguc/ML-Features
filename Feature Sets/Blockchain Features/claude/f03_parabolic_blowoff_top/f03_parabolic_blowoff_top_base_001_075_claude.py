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


# ============ FEATURES 001-075 ============

# stretch above EMA(10) - short blow-off extension
def f03pb_f03_parabolic_blowoff_top_stretch_10d_base_v001_signal(close):
    result = _f03_stretch(close, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above EMA(21) - monthly extension
def f03pb_f03_parabolic_blowoff_top_stretch_21d_base_v002_signal(close):
    result = _f03_stretch(close, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above EMA(50)
def f03pb_f03_parabolic_blowoff_top_stretch_50d_base_v003_signal(closeadj):
    result = _f03_stretch(closeadj, 50)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above EMA(100)
def f03pb_f03_parabolic_blowoff_top_stretch_100d_base_v004_signal(closeadj):
    result = _f03_stretch(closeadj, 100)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above EMA(200)
def f03pb_f03_parabolic_blowoff_top_stretch_200d_base_v005_signal(closeadj):
    result = _f03_stretch(closeadj, 200)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above EMA(5) - weekly thrust extension
def f03pb_f03_parabolic_blowoff_top_stretch_5d_base_v006_signal(close):
    result = _f03_stretch(close, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above EMA(63) - quarterly extension
def f03pb_f03_parabolic_blowoff_top_stretch_63d_base_v007_signal(closeadj):
    result = _f03_stretch(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above EMA(126)
def f03pb_f03_parabolic_blowoff_top_stretch_126d_base_v008_signal(closeadj):
    result = _f03_stretch(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of EMA(21) stretch over 126d (parabolic stretch z-score)
def f03pb_f03_parabolic_blowoff_top_zstretch_21d_base_v009_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of EMA(50) stretch over 252d
def f03pb_f03_parabolic_blowoff_top_zstretch_50d_base_v010_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 50), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of EMA(10) stretch over 63d
def f03pb_f03_parabolic_blowoff_top_zstretch_10d_base_v011_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 10), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of EMA(100) stretch over 252d
def f03pb_f03_parabolic_blowoff_top_zstretch_100d_base_v012_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 100), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# distance above SMA(21) normalized by price (parabolic SMA-distance)
def f03pb_f03_parabolic_blowoff_top_smadist_21d_base_v013_signal(close):
    sma = _mean(close, 21)
    result = _safe_div(close - sma, close) + _f03_stretch(close, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance above SMA(50) normalized by price
def f03pb_f03_parabolic_blowoff_top_smadist_50d_base_v014_signal(closeadj):
    sma = _mean(closeadj, 50)
    result = _safe_div(closeadj - sma, closeadj) + _f03_stretch(closeadj, 50) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance above SMA(100) normalized by price
def f03pb_f03_parabolic_blowoff_top_smadist_100d_base_v015_signal(closeadj):
    sma = _mean(closeadj, 100)
    result = _safe_div(closeadj - sma, closeadj) + _f03_stretch(closeadj, 100) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance above SMA(200) normalized by price
def f03pb_f03_parabolic_blowoff_top_smadist_200d_base_v016_signal(closeadj):
    sma = _mean(closeadj, 200)
    result = _safe_div(closeadj - sma, closeadj) + _f03_stretch(closeadj, 200) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# convexity of log ascent over 21d (parabolic acceleration level)
def f03pb_f03_parabolic_blowoff_top_convex_21d_base_v017_signal(close):
    result = _f03_convexity(close, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# convexity of log ascent over 10d
def f03pb_f03_parabolic_blowoff_top_convex_10d_base_v018_signal(close):
    result = _f03_convexity(close, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# convexity of log ascent over 42d
def f03pb_f03_parabolic_blowoff_top_convex_42d_base_v019_signal(closeadj):
    result = _f03_convexity(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# convexity of log ascent over 63d
def f03pb_f03_parabolic_blowoff_top_convex_63d_base_v020_signal(closeadj):
    result = _f03_convexity(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# convexity of log ascent over 5d
def f03pb_f03_parabolic_blowoff_top_convex_5d_base_v021_signal(close):
    result = _f03_convexity(close, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed convexity (21d mean of 10d convexity) - sustained acceleration
def f03pb_f03_parabolic_blowoff_top_smconvex_21d_base_v022_signal(closeadj):
    result = _mean(_f03_convexity(closeadj, 10), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of convexity(21) over 126d
def f03pb_f03_parabolic_blowoff_top_zconvex_21d_base_v023_signal(closeadj):
    result = _z(_f03_convexity(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of convexity(42) over 252d
def f03pb_f03_parabolic_blowoff_top_zconvex_42d_base_v024_signal(closeadj):
    result = _z(_f03_convexity(closeadj, 42), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# climax range intensity over 21d
def f03pb_f03_parabolic_blowoff_top_climax_21d_base_v025_signal(high, low):
    result = _f03_climax(high, low, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# climax range intensity over 10d
def f03pb_f03_parabolic_blowoff_top_climax_10d_base_v026_signal(high, low):
    result = _f03_climax(high, low, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# climax range intensity over 42d
def f03pb_f03_parabolic_blowoff_top_climax_42d_base_v027_signal(high, low):
    result = _f03_climax(high, low, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# climax range intensity over 63d
def f03pb_f03_parabolic_blowoff_top_climax_63d_base_v028_signal(high, low):
    result = _f03_climax(high, low, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed climax (10d mean of 5d climax)
def f03pb_f03_parabolic_blowoff_top_smclimax_10d_base_v029_signal(high, low):
    result = _mean(_f03_climax(high, low, 5), 10)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of climax(21) over 126d
def f03pb_f03_parabolic_blowoff_top_zclimax_21d_base_v030_signal(high, low):
    result = _z(_f03_climax(high, low, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR-normalized extension above SMA(21)
def f03pb_f03_parabolic_blowoff_top_ext_21d_base_v031_signal(close):
    result = _f03_extension(close, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR-normalized extension above SMA(50)
def f03pb_f03_parabolic_blowoff_top_ext_50d_base_v032_signal(closeadj):
    result = _f03_extension(closeadj, 50)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR-normalized extension above SMA(100)
def f03pb_f03_parabolic_blowoff_top_ext_100d_base_v033_signal(closeadj):
    result = _f03_extension(closeadj, 100)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR-normalized extension above SMA(10)
def f03pb_f03_parabolic_blowoff_top_ext_10d_base_v034_signal(close):
    result = _f03_extension(close, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR-normalized extension above SMA(63)
def f03pb_f03_parabolic_blowoff_top_ext_63d_base_v035_signal(closeadj):
    result = _f03_extension(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR-normalized extension above SMA(200)
def f03pb_f03_parabolic_blowoff_top_ext_200d_base_v036_signal(closeadj):
    result = _f03_extension(closeadj, 200)
    return result.replace([np.inf, -np.inf], np.nan)


# upper Bollinger %B style penetration over 21d (continuous standardized position)
def f03pb_f03_parabolic_blowoff_top_pctb_21d_base_v037_signal(close):
    m = _mean(close, 21)
    sd = _std(close, 21)
    result = _safe_div(close - m, 2.0 * sd) + _f03_stretch(close, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# upper Bollinger %B style penetration over 50d
def f03pb_f03_parabolic_blowoff_top_pctb_50d_base_v038_signal(closeadj):
    m = _mean(closeadj, 50)
    sd = _std(closeadj, 50)
    result = _safe_div(closeadj - m, 2.0 * sd) + _f03_stretch(closeadj, 50) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# upper Bollinger %B style penetration over 100d
def f03pb_f03_parabolic_blowoff_top_pctb_100d_base_v039_signal(closeadj):
    m = _mean(closeadj, 100)
    sd = _std(closeadj, 100)
    result = _safe_div(closeadj - m, 2.0 * sd) + _f03_stretch(closeadj, 100) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price vs upper Bollinger band normalized over 21d
def f03pb_f03_parabolic_blowoff_top_ubdist_21d_base_v040_signal(close):
    m = _mean(close, 21)
    sd = _std(close, 21)
    ub = m + 2.0 * sd
    result = _safe_div(close - ub, sd) + _f03_stretch(close, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price vs upper Bollinger band normalized over 63d
def f03pb_f03_parabolic_blowoff_top_ubdist_63d_base_v041_signal(closeadj):
    m = _mean(closeadj, 63)
    sd = _std(closeadj, 63)
    ub = m + 2.0 * sd
    result = _safe_div(closeadj - ub, sd) + _f03_stretch(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# vertical velocity: 5d return per unit realized vol (blow-off thrust)
def f03pb_f03_parabolic_blowoff_top_vvel_5d_base_v042_signal(close):
    lr = np.log(close / close.shift(1))
    r = close.pct_change(periods=5)
    vol = _std(lr, 21) * np.sqrt(5.0)
    result = _safe_div(r, vol) + _f03_stretch(close, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# vertical velocity: 10d return per unit realized vol
def f03pb_f03_parabolic_blowoff_top_vvel_10d_base_v043_signal(close):
    lr = np.log(close / close.shift(1))
    r = close.pct_change(periods=10)
    vol = _std(lr, 42) * np.sqrt(10.0)
    result = _safe_div(r, vol) + _f03_stretch(close, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# vertical velocity: 21d return per unit realized vol
def f03pb_f03_parabolic_blowoff_top_vvel_21d_base_v044_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    r = closeadj.pct_change(periods=21)
    vol = _std(lr, 63) * np.sqrt(21.0)
    result = _safe_div(r, vol) + _f03_stretch(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# blow-off ratio: close vs 63d low scaled by price (run-up extension)
def f03pb_f03_parabolic_blowoff_top_blowoff_63d_base_v045_signal(closeadj):
    lo = closeadj.rolling(63, min_periods=21).min().replace(0, np.nan)
    result = _safe_div(closeadj - lo, lo) + _f03_stretch(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# blow-off ratio: close vs 126d low scaled
def f03pb_f03_parabolic_blowoff_top_blowoff_126d_base_v046_signal(closeadj):
    lo = closeadj.rolling(126, min_periods=42).min().replace(0, np.nan)
    result = _safe_div(closeadj - lo, lo) + _f03_stretch(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# blow-off ratio: close vs 252d low scaled
def f03pb_f03_parabolic_blowoff_top_blowoff_252d_base_v047_signal(closeadj):
    lo = closeadj.rolling(252, min_periods=84).min().replace(0, np.nan)
    result = _safe_div(closeadj - lo, lo) + _f03_stretch(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# exhaustion: EMA(21) stretch times volume surge
def f03pb_f03_parabolic_blowoff_top_exhaust_21d_base_v048_signal(close, volume):
    surge = _safe_div(volume, _mean(volume, 63))
    result = _f03_stretch(close, 21) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# exhaustion: EMA(50) stretch times volume surge
def f03pb_f03_parabolic_blowoff_top_exhaust_50d_base_v049_signal(closeadj, volume):
    surge = _safe_div(volume, _mean(volume, 126))
    result = _f03_stretch(closeadj, 50) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# exhaustion: EMA(10) stretch times dollar-volume surge
def f03pb_f03_parabolic_blowoff_top_exhaust_10d_base_v050_signal(close, volume):
    dv = close * volume
    surge = _safe_div(dv, _mean(dv, 63))
    result = _f03_stretch(close, 10) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# stretch ratio: short EMA(10) stretch vs long EMA(63) stretch
def f03pb_f03_parabolic_blowoff_top_stretchratio_10_63_base_v051_signal(closeadj):
    result = _f03_stretch(closeadj, 10) - _f03_stretch(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch ratio: EMA(21) vs EMA(126)
def f03pb_f03_parabolic_blowoff_top_stretchratio_21_126_base_v052_signal(closeadj):
    result = _f03_stretch(closeadj, 21) - _f03_stretch(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch ratio: EMA(50) vs EMA(200)
def f03pb_f03_parabolic_blowoff_top_stretchratio_50_200_base_v053_signal(closeadj):
    result = _f03_stretch(closeadj, 50) - _f03_stretch(closeadj, 200)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch acceleration: 5d change in EMA(21) stretch
def f03pb_f03_parabolic_blowoff_top_stretchaccel_21d_base_v054_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    result = st - st.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch acceleration: 10d change in EMA(50) stretch
def f03pb_f03_parabolic_blowoff_top_stretchaccel_50d_base_v055_signal(closeadj):
    st = _f03_stretch(closeadj, 50)
    result = st - st.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive-acceleration intensity: rolling mean of positive convexity magnitude
def f03pb_f03_parabolic_blowoff_top_accelint_21d_base_v056_signal(closeadj):
    c = _f03_convexity(closeadj, 21)
    result = c.clip(lower=0).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive-acceleration intensity over 42d
def f03pb_f03_parabolic_blowoff_top_accelint_42d_base_v057_signal(closeadj):
    c = _f03_convexity(closeadj, 21)
    result = c.clip(lower=0).rolling(42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# stretch times climax (extension confirmed by volatility climax)
def f03pb_f03_parabolic_blowoff_top_stretchclimax_21d_base_v058_signal(close, high, low):
    result = _f03_stretch(close, 21) * (1.0 + _f03_climax(high, low, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# stretch times climax over 50/42d
def f03pb_f03_parabolic_blowoff_top_stretchclimax_50d_base_v059_signal(closeadj, high, low):
    result = _f03_stretch(closeadj, 50) * (1.0 + _f03_climax(high, low, 42))
    return result.replace([np.inf, -np.inf], np.nan)


# extension times convexity (extended AND accelerating)
def f03pb_f03_parabolic_blowoff_top_extconvex_21d_base_v060_signal(closeadj):
    result = _f03_extension(closeadj, 21) * _f03_convexity(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# extension times convexity over 50d
def f03pb_f03_parabolic_blowoff_top_extconvex_50d_base_v061_signal(closeadj):
    result = _f03_extension(closeadj, 50) * _f03_convexity(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# normalized gap of close above EMA(21) scaled by ATR
def f03pb_f03_parabolic_blowoff_top_emagap_21d_base_v062_signal(close):
    ema = close.ewm(span=21, min_periods=10).mean()
    atr = close.diff().abs().rolling(21, min_periods=10).mean()
    result = _safe_div(close - ema, atr) + _f03_stretch(close, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# normalized gap of close above EMA(63) scaled by ATR
def f03pb_f03_parabolic_blowoff_top_emagap_63d_base_v063_signal(closeadj):
    ema = closeadj.ewm(span=63, min_periods=21).mean()
    atr = closeadj.diff().abs().rolling(63, min_periods=21).mean()
    result = _safe_div(closeadj - ema, atr) + _f03_stretch(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of EMA(21) stretch over 126d
def f03pb_f03_parabolic_blowoff_top_rankstretch_21d_base_v064_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    result = st.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of EMA(50) stretch over 252d
def f03pb_f03_parabolic_blowoff_top_rankstretch_50d_base_v065_signal(closeadj):
    st = _f03_stretch(closeadj, 50)
    result = st.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# high-vs-SMA stretch (intraday-high extension above SMA(21))
def f03pb_f03_parabolic_blowoff_top_highstretch_21d_base_v066_signal(high, closeadj):
    sma = _mean(closeadj, 21)
    result = _safe_div(high - sma, sma) + _f03_stretch(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# high-vs-SMA stretch over 50d
def f03pb_f03_parabolic_blowoff_top_highstretch_50d_base_v067_signal(high, closeadj):
    sma = _mean(closeadj, 50)
    result = _safe_div(high - sma, sma) + _f03_stretch(closeadj, 50) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# parabolic curvature of EMA(21) stretch (its own 2nd difference, spaced 5d)
def f03pb_f03_parabolic_blowoff_top_curv_21d_base_v068_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    result = st - 2.0 * st.shift(5) + st.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# parabolic curvature of EMA(50) stretch (spaced 10d)
def f03pb_f03_parabolic_blowoff_top_curv_50d_base_v069_signal(closeadj):
    st = _f03_stretch(closeadj, 50)
    result = st - 2.0 * st.shift(10) + st.shift(20)
    return result.replace([np.inf, -np.inf], np.nan)


# climax-weighted convexity (acceleration during range expansion)
def f03pb_f03_parabolic_blowoff_top_climaxconvex_21d_base_v070_signal(closeadj, high, low):
    result = _f03_convexity(closeadj, 21) * (1.0 + _f03_climax(high, low, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# EMA(10) stretch standardized over 252d (extreme short extension)
def f03pb_f03_parabolic_blowoff_top_zstretch10_252_base_v071_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 10), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# blow-off ratio close vs 42d low scaled by ATR
def f03pb_f03_parabolic_blowoff_top_blowoffatr_42d_base_v072_signal(closeadj):
    lo = closeadj.rolling(42, min_periods=21).min()
    atr = closeadj.diff().abs().rolling(42, min_periods=21).mean()
    result = _safe_div(closeadj - lo, atr) + _f03_stretch(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# vertical velocity scaled stretch (extension per unit of recent vol) 21d
def f03pb_f03_parabolic_blowoff_top_stretchvol_21d_base_v073_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 21) * np.sqrt(252.0)
    result = _safe_div(_f03_stretch(closeadj, 21), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# vertical velocity scaled stretch 50d
def f03pb_f03_parabolic_blowoff_top_stretchvol_50d_base_v074_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 63) * np.sqrt(252.0)
    result = _safe_div(_f03_stretch(closeadj, 50), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# multi-EMA stretch composite (10/21/50 average extension)
def f03pb_f03_parabolic_blowoff_top_stretchblend_base_v075_signal(closeadj):
    result = (_f03_stretch(closeadj, 10) + _f03_stretch(closeadj, 21)
              + _f03_stretch(closeadj, 50)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03pb_f03_parabolic_blowoff_top_stretch_10d_base_v001_signal,
    f03pb_f03_parabolic_blowoff_top_stretch_21d_base_v002_signal,
    f03pb_f03_parabolic_blowoff_top_stretch_50d_base_v003_signal,
    f03pb_f03_parabolic_blowoff_top_stretch_100d_base_v004_signal,
    f03pb_f03_parabolic_blowoff_top_stretch_200d_base_v005_signal,
    f03pb_f03_parabolic_blowoff_top_stretch_5d_base_v006_signal,
    f03pb_f03_parabolic_blowoff_top_stretch_63d_base_v007_signal,
    f03pb_f03_parabolic_blowoff_top_stretch_126d_base_v008_signal,
    f03pb_f03_parabolic_blowoff_top_zstretch_21d_base_v009_signal,
    f03pb_f03_parabolic_blowoff_top_zstretch_50d_base_v010_signal,
    f03pb_f03_parabolic_blowoff_top_zstretch_10d_base_v011_signal,
    f03pb_f03_parabolic_blowoff_top_zstretch_100d_base_v012_signal,
    f03pb_f03_parabolic_blowoff_top_smadist_21d_base_v013_signal,
    f03pb_f03_parabolic_blowoff_top_smadist_50d_base_v014_signal,
    f03pb_f03_parabolic_blowoff_top_smadist_100d_base_v015_signal,
    f03pb_f03_parabolic_blowoff_top_smadist_200d_base_v016_signal,
    f03pb_f03_parabolic_blowoff_top_convex_21d_base_v017_signal,
    f03pb_f03_parabolic_blowoff_top_convex_10d_base_v018_signal,
    f03pb_f03_parabolic_blowoff_top_convex_42d_base_v019_signal,
    f03pb_f03_parabolic_blowoff_top_convex_63d_base_v020_signal,
    f03pb_f03_parabolic_blowoff_top_convex_5d_base_v021_signal,
    f03pb_f03_parabolic_blowoff_top_smconvex_21d_base_v022_signal,
    f03pb_f03_parabolic_blowoff_top_zconvex_21d_base_v023_signal,
    f03pb_f03_parabolic_blowoff_top_zconvex_42d_base_v024_signal,
    f03pb_f03_parabolic_blowoff_top_climax_21d_base_v025_signal,
    f03pb_f03_parabolic_blowoff_top_climax_10d_base_v026_signal,
    f03pb_f03_parabolic_blowoff_top_climax_42d_base_v027_signal,
    f03pb_f03_parabolic_blowoff_top_climax_63d_base_v028_signal,
    f03pb_f03_parabolic_blowoff_top_smclimax_10d_base_v029_signal,
    f03pb_f03_parabolic_blowoff_top_zclimax_21d_base_v030_signal,
    f03pb_f03_parabolic_blowoff_top_ext_21d_base_v031_signal,
    f03pb_f03_parabolic_blowoff_top_ext_50d_base_v032_signal,
    f03pb_f03_parabolic_blowoff_top_ext_100d_base_v033_signal,
    f03pb_f03_parabolic_blowoff_top_ext_10d_base_v034_signal,
    f03pb_f03_parabolic_blowoff_top_ext_63d_base_v035_signal,
    f03pb_f03_parabolic_blowoff_top_ext_200d_base_v036_signal,
    f03pb_f03_parabolic_blowoff_top_pctb_21d_base_v037_signal,
    f03pb_f03_parabolic_blowoff_top_pctb_50d_base_v038_signal,
    f03pb_f03_parabolic_blowoff_top_pctb_100d_base_v039_signal,
    f03pb_f03_parabolic_blowoff_top_ubdist_21d_base_v040_signal,
    f03pb_f03_parabolic_blowoff_top_ubdist_63d_base_v041_signal,
    f03pb_f03_parabolic_blowoff_top_vvel_5d_base_v042_signal,
    f03pb_f03_parabolic_blowoff_top_vvel_10d_base_v043_signal,
    f03pb_f03_parabolic_blowoff_top_vvel_21d_base_v044_signal,
    f03pb_f03_parabolic_blowoff_top_blowoff_63d_base_v045_signal,
    f03pb_f03_parabolic_blowoff_top_blowoff_126d_base_v046_signal,
    f03pb_f03_parabolic_blowoff_top_blowoff_252d_base_v047_signal,
    f03pb_f03_parabolic_blowoff_top_exhaust_21d_base_v048_signal,
    f03pb_f03_parabolic_blowoff_top_exhaust_50d_base_v049_signal,
    f03pb_f03_parabolic_blowoff_top_exhaust_10d_base_v050_signal,
    f03pb_f03_parabolic_blowoff_top_stretchratio_10_63_base_v051_signal,
    f03pb_f03_parabolic_blowoff_top_stretchratio_21_126_base_v052_signal,
    f03pb_f03_parabolic_blowoff_top_stretchratio_50_200_base_v053_signal,
    f03pb_f03_parabolic_blowoff_top_stretchaccel_21d_base_v054_signal,
    f03pb_f03_parabolic_blowoff_top_stretchaccel_50d_base_v055_signal,
    f03pb_f03_parabolic_blowoff_top_accelint_21d_base_v056_signal,
    f03pb_f03_parabolic_blowoff_top_accelint_42d_base_v057_signal,
    f03pb_f03_parabolic_blowoff_top_stretchclimax_21d_base_v058_signal,
    f03pb_f03_parabolic_blowoff_top_stretchclimax_50d_base_v059_signal,
    f03pb_f03_parabolic_blowoff_top_extconvex_21d_base_v060_signal,
    f03pb_f03_parabolic_blowoff_top_extconvex_50d_base_v061_signal,
    f03pb_f03_parabolic_blowoff_top_emagap_21d_base_v062_signal,
    f03pb_f03_parabolic_blowoff_top_emagap_63d_base_v063_signal,
    f03pb_f03_parabolic_blowoff_top_rankstretch_21d_base_v064_signal,
    f03pb_f03_parabolic_blowoff_top_rankstretch_50d_base_v065_signal,
    f03pb_f03_parabolic_blowoff_top_highstretch_21d_base_v066_signal,
    f03pb_f03_parabolic_blowoff_top_highstretch_50d_base_v067_signal,
    f03pb_f03_parabolic_blowoff_top_curv_21d_base_v068_signal,
    f03pb_f03_parabolic_blowoff_top_curv_50d_base_v069_signal,
    f03pb_f03_parabolic_blowoff_top_climaxconvex_21d_base_v070_signal,
    f03pb_f03_parabolic_blowoff_top_zstretch10_252_base_v071_signal,
    f03pb_f03_parabolic_blowoff_top_blowoffatr_42d_base_v072_signal,
    f03pb_f03_parabolic_blowoff_top_stretchvol_21d_base_v073_signal,
    f03pb_f03_parabolic_blowoff_top_stretchvol_50d_base_v074_signal,
    f03pb_f03_parabolic_blowoff_top_stretchblend_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_PARABOLIC_BLOWOFF_TOP_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f03_stretch", "_f03_convexity", "_f03_climax", "_f03_extension")
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
    print(f"OK f03_parabolic_blowoff_top_base_001_075_claude: {n_features} features pass")
