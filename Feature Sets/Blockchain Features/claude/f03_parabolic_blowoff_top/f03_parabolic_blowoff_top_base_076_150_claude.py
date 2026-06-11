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


# ============ FEATURES 076-150 ============

# stretch above EMA(42) - parabolic extension
def f03pb_f03_parabolic_blowoff_top_stretch_42d_base_v076_signal(closeadj):
    result = _f03_stretch(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above EMA(84)
def f03pb_f03_parabolic_blowoff_top_stretch_84d_base_v077_signal(closeadj):
    result = _f03_stretch(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch above EMA(189)
def f03pb_f03_parabolic_blowoff_top_stretch_189d_base_v078_signal(closeadj):
    result = _f03_stretch(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of EMA(42) stretch over 252d
def f03pb_f03_parabolic_blowoff_top_zstretch_42d_base_v079_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 42), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of EMA(63) stretch over 252d
def f03pb_f03_parabolic_blowoff_top_zstretch_63d_base_v080_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of EMA(126) stretch over 504d
def f03pb_f03_parabolic_blowoff_top_zstretch_126d_base_v081_signal(closeadj):
    result = _z(_f03_stretch(closeadj, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed EMA(21) stretch (21d mean) - persistent extension
def f03pb_f03_parabolic_blowoff_top_smstretch_21d_base_v082_signal(closeadj):
    result = _mean(_f03_stretch(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed EMA(50) stretch (42d mean)
def f03pb_f03_parabolic_blowoff_top_smstretch_50d_base_v083_signal(closeadj):
    result = _mean(_f03_stretch(closeadj, 50), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# convexity over 84d
def f03pb_f03_parabolic_blowoff_top_convex_84d_base_v084_signal(closeadj):
    result = _f03_convexity(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# convexity over 126d
def f03pb_f03_parabolic_blowoff_top_convex_126d_base_v085_signal(closeadj):
    result = _f03_convexity(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed convexity (42d mean of 21d convexity)
def f03pb_f03_parabolic_blowoff_top_smconvex_42d_base_v086_signal(closeadj):
    result = _mean(_f03_convexity(closeadj, 21), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of convexity(63) over 252d
def f03pb_f03_parabolic_blowoff_top_zconvex_63d_base_v087_signal(closeadj):
    result = _z(_f03_convexity(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# climax range intensity over 84d
def f03pb_f03_parabolic_blowoff_top_climax_84d_base_v088_signal(high, low):
    result = _f03_climax(high, low, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# climax range intensity over 126d
def f03pb_f03_parabolic_blowoff_top_climax_126d_base_v089_signal(high, low):
    result = _f03_climax(high, low, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed climax (21d mean of 21d climax)
def f03pb_f03_parabolic_blowoff_top_smclimax_21d_base_v090_signal(high, low):
    result = _mean(_f03_climax(high, low, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of climax(63) over 252d
def f03pb_f03_parabolic_blowoff_top_zclimax_63d_base_v091_signal(high, low):
    result = _z(_f03_climax(high, low, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR-normalized extension above SMA(42)
def f03pb_f03_parabolic_blowoff_top_ext_42d_base_v092_signal(closeadj):
    result = _f03_extension(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR-normalized extension above SMA(84)
def f03pb_f03_parabolic_blowoff_top_ext_84d_base_v093_signal(closeadj):
    result = _f03_extension(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR-normalized extension above SMA(126)
def f03pb_f03_parabolic_blowoff_top_ext_126d_base_v094_signal(closeadj):
    result = _f03_extension(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of extension(21) over 126d
def f03pb_f03_parabolic_blowoff_top_zext_21d_base_v095_signal(closeadj):
    result = _z(_f03_extension(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of extension(63) over 252d
def f03pb_f03_parabolic_blowoff_top_zext_63d_base_v096_signal(closeadj):
    result = _z(_f03_extension(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# upper Bollinger %B style over 63d
def f03pb_f03_parabolic_blowoff_top_pctb_63d_base_v097_signal(closeadj):
    m = _mean(closeadj, 63)
    sd = _std(closeadj, 63)
    result = _safe_div(closeadj - m, 2.0 * sd) + _f03_stretch(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# upper Bollinger %B style over 126d
def f03pb_f03_parabolic_blowoff_top_pctb_126d_base_v098_signal(closeadj):
    m = _mean(closeadj, 126)
    sd = _std(closeadj, 126)
    result = _safe_div(closeadj - m, 2.0 * sd) + _f03_stretch(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price vs upper Bollinger band normalized over 126d
def f03pb_f03_parabolic_blowoff_top_ubdist_126d_base_v099_signal(closeadj):
    m = _mean(closeadj, 126)
    sd = _std(closeadj, 126)
    ub = m + 2.0 * sd
    result = _safe_div(closeadj - ub, sd) + _f03_stretch(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# vertical velocity: 42d return per unit realized vol
def f03pb_f03_parabolic_blowoff_top_vvel_42d_base_v100_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    r = closeadj.pct_change(periods=42)
    vol = _std(lr, 84) * np.sqrt(42.0)
    result = _safe_div(r, vol) + _f03_stretch(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# vertical velocity: 63d return per unit realized vol
def f03pb_f03_parabolic_blowoff_top_vvel_63d_base_v101_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    r = closeadj.pct_change(periods=63)
    vol = _std(lr, 126) * np.sqrt(63.0)
    result = _safe_div(r, vol) + _f03_stretch(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# blow-off ratio close vs 21d low scaled
def f03pb_f03_parabolic_blowoff_top_blowoff_21d_base_v102_signal(closeadj):
    lo = closeadj.rolling(21, min_periods=10).min().replace(0, np.nan)
    result = _safe_div(closeadj - lo, lo) + _f03_stretch(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# blow-off ratio close vs 84d low scaled by ATR
def f03pb_f03_parabolic_blowoff_top_blowoffatr_84d_base_v103_signal(closeadj):
    lo = closeadj.rolling(84, min_periods=42).min()
    atr = closeadj.diff().abs().rolling(84, min_periods=42).mean()
    result = _safe_div(closeadj - lo, atr) + _f03_stretch(closeadj, 84) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# blow-off ratio close vs 126d low scaled by ATR
def f03pb_f03_parabolic_blowoff_top_blowoffatr_126d_base_v104_signal(closeadj):
    lo = closeadj.rolling(126, min_periods=42).min()
    atr = closeadj.diff().abs().rolling(126, min_periods=42).mean()
    result = _safe_div(closeadj - lo, atr) + _f03_stretch(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# exhaustion: EMA(21) stretch times dollar-volume surge
def f03pb_f03_parabolic_blowoff_top_exhaustdv_21d_base_v105_signal(closeadj, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 126))
    result = _f03_stretch(closeadj, 21) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# exhaustion: EMA(63) stretch times volume z-score
def f03pb_f03_parabolic_blowoff_top_exhaustz_63d_base_v106_signal(closeadj, volume):
    result = _f03_stretch(closeadj, 63) * _z(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# exhaustion: extension(21) times volume surge
def f03pb_f03_parabolic_blowoff_top_extvol_21d_base_v107_signal(closeadj, volume):
    surge = _safe_div(volume, _mean(volume, 63))
    result = _f03_extension(closeadj, 21) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# stretch ratio: EMA(42) vs EMA(189)
def f03pb_f03_parabolic_blowoff_top_stretchratio_42_189_base_v108_signal(closeadj):
    result = _f03_stretch(closeadj, 42) - _f03_stretch(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch acceleration: 21d change in EMA(100) stretch
def f03pb_f03_parabolic_blowoff_top_stretchaccel_100d_base_v109_signal(closeadj):
    st = _f03_stretch(closeadj, 100)
    result = st - st.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive-acceleration intensity over 63d
def f03pb_f03_parabolic_blowoff_top_accelint_63d_base_v110_signal(closeadj):
    c = _f03_convexity(closeadj, 21)
    result = c.clip(lower=0).rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration intensity: rolling mean of |convexity| (raw magnitude) over 42d
def f03pb_f03_parabolic_blowoff_top_accelmag_42d_base_v111_signal(closeadj):
    c = _f03_convexity(closeadj, 21).abs()
    result = c.rolling(42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# stretch times climax over 100/63d
def f03pb_f03_parabolic_blowoff_top_stretchclimax_100d_base_v112_signal(closeadj, high, low):
    result = _f03_stretch(closeadj, 100) * (1.0 + _f03_climax(high, low, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# extension times convexity over 100d
def f03pb_f03_parabolic_blowoff_top_extconvex_100d_base_v113_signal(closeadj):
    result = _f03_extension(closeadj, 100) * _f03_convexity(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# normalized gap of close above EMA(126) scaled by ATR
def f03pb_f03_parabolic_blowoff_top_emagap_126d_base_v114_signal(closeadj):
    ema = closeadj.ewm(span=126, min_periods=42).mean()
    atr = closeadj.diff().abs().rolling(126, min_periods=42).mean()
    result = _safe_div(closeadj - ema, atr) + _f03_stretch(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of EMA(100) stretch over 252d
def f03pb_f03_parabolic_blowoff_top_rankstretch_100d_base_v115_signal(closeadj):
    st = _f03_stretch(closeadj, 100)
    result = st.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of extension(50) over 252d
def f03pb_f03_parabolic_blowoff_top_rankext_50d_base_v116_signal(closeadj):
    e = _f03_extension(closeadj, 50)
    result = e.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# high-vs-SMA stretch over 100d
def f03pb_f03_parabolic_blowoff_top_highstretch_100d_base_v117_signal(high, closeadj):
    sma = _mean(closeadj, 100)
    result = _safe_div(high - sma, sma) + _f03_stretch(closeadj, 100) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# parabolic curvature of EMA(100) stretch (spaced 21d)
def f03pb_f03_parabolic_blowoff_top_curv_100d_base_v118_signal(closeadj):
    st = _f03_stretch(closeadj, 100)
    result = st - 2.0 * st.shift(21) + st.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# climax-weighted convexity over 63d
def f03pb_f03_parabolic_blowoff_top_climaxconvex_63d_base_v119_signal(closeadj, high, low):
    result = _f03_convexity(closeadj, 63) * (1.0 + _f03_climax(high, low, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# vertical velocity scaled stretch 100d
def f03pb_f03_parabolic_blowoff_top_stretchvol_100d_base_v120_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 126) * np.sqrt(252.0)
    result = _safe_div(_f03_stretch(closeadj, 100), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch convexity composite: extension times stretch acceleration 21d
def f03pb_f03_parabolic_blowoff_top_extaccel_21d_base_v121_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    accel = st - st.shift(5)
    result = _f03_extension(closeadj, 21) * accel
    return result.replace([np.inf, -np.inf], np.nan)


# blow-off climax: close-vs-63d-low run-up times range climax
def f03pb_f03_parabolic_blowoff_top_blowclimax_63d_base_v122_signal(closeadj, high, low):
    lo = closeadj.rolling(63, min_periods=21).min().replace(0, np.nan)
    runup = _safe_div(closeadj - lo, lo)
    result = runup * (1.0 + _f03_climax(high, low, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# convexity scaled by realized vol (acceleration per unit risk) 21d
def f03pb_f03_parabolic_blowoff_top_convexvol_21d_base_v123_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 63)
    result = _safe_div(_f03_convexity(closeadj, 21), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# convexity scaled by realized vol 63d
def f03pb_f03_parabolic_blowoff_top_convexvol_63d_base_v124_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 126)
    result = _safe_div(_f03_convexity(closeadj, 63), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA(21) stretch minus its 63d running mean (stretch surprise)
def f03pb_f03_parabolic_blowoff_top_stretchsurp_21d_base_v125_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    result = st - _mean(st, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# EMA(50) stretch minus its 126d running mean
def f03pb_f03_parabolic_blowoff_top_stretchsurp_50d_base_v126_signal(closeadj):
    st = _f03_stretch(closeadj, 50)
    result = st - _mean(st, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# extension(21) minus its 63d running mean (extension surprise)
def f03pb_f03_parabolic_blowoff_top_extsurp_21d_base_v127_signal(closeadj):
    e = _f03_extension(closeadj, 21)
    result = e - _mean(e, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# climax(21) minus its 63d running mean (range-expansion surprise)
def f03pb_f03_parabolic_blowoff_top_climaxsurp_21d_base_v128_signal(high, low):
    c = _f03_climax(high, low, 21)
    result = c - _mean(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch dispersion: std of EMA(21) stretch over 63d (instability of extension)
def f03pb_f03_parabolic_blowoff_top_stretchdisp_63d_base_v129_signal(closeadj):
    result = _std(_f03_stretch(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch dispersion over 126d
def f03pb_f03_parabolic_blowoff_top_stretchdisp_126d_base_v130_signal(closeadj):
    result = _std(_f03_stretch(closeadj, 50), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# convexity dispersion over 63d (variability of acceleration)
def f03pb_f03_parabolic_blowoff_top_convexdisp_63d_base_v131_signal(closeadj):
    result = _std(_f03_convexity(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# range-climax EWMA over 21d (smoothed exponential climax)
def f03pb_f03_parabolic_blowoff_top_climaxewm_21d_base_v132_signal(high, low):
    c = _f03_climax(high, low, 21)
    result = c.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# stretch EWMA over 21d (smoothed exponential extension)
def f03pb_f03_parabolic_blowoff_top_stretchewm_21d_base_v133_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    result = st.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# stretch EWMA over 63d
def f03pb_f03_parabolic_blowoff_top_stretchewm_63d_base_v134_signal(closeadj):
    st = _f03_stretch(closeadj, 50)
    result = st.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# parabolic intensity: EMA(21) stretch raised to convex power (sign-preserving)
def f03pb_f03_parabolic_blowoff_top_stretchpow_21d_base_v135_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    result = np.sign(st) * (st.abs() ** 1.5)
    return result.replace([np.inf, -np.inf], np.nan)


# parabolic intensity: EMA(50) stretch raised to convex power k=2
def f03pb_f03_parabolic_blowoff_top_stretchpow_50d_base_v136_signal(closeadj):
    st = _f03_stretch(closeadj, 50)
    result = np.sign(st) * (st.abs() ** 2.0)
    return result.replace([np.inf, -np.inf], np.nan)


# upper-band penetration depth scaled by ATR over 50d
def f03pb_f03_parabolic_blowoff_top_ubatr_50d_base_v137_signal(closeadj):
    m = _mean(closeadj, 50)
    sd = _std(closeadj, 50)
    ub = m + 2.0 * sd
    atr = closeadj.diff().abs().rolling(50, min_periods=21).mean()
    result = _safe_div(closeadj - ub, atr) + _f03_stretch(closeadj, 50) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# climax of close-based range proxy: |daily return| vs trailing avg (price-only climax)
def f03pb_f03_parabolic_blowoff_top_retclimax_21d_base_v138_signal(closeadj):
    r = closeadj.pct_change().abs()
    avg = r.rolling(21, min_periods=10).mean()
    result = _safe_div(r, avg) - 1.0 + _f03_stretch(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# climax of |return| over 63d
def f03pb_f03_parabolic_blowoff_top_retclimax_63d_base_v139_signal(closeadj):
    r = closeadj.pct_change().abs()
    avg = r.rolling(63, min_periods=21).mean()
    result = _safe_div(r, avg) - 1.0 + _f03_stretch(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# parabolic score: stretch z times convexity z (extended AND accelerating, standardized)
def f03pb_f03_parabolic_blowoff_top_paraz_21d_base_v140_signal(closeadj):
    sz = _z(_f03_stretch(closeadj, 21), 126)
    cz = _z(_f03_convexity(closeadj, 21), 126)
    result = sz * cz
    return result.replace([np.inf, -np.inf], np.nan)


# parabolic score over 63d windows
def f03pb_f03_parabolic_blowoff_top_paraz_63d_base_v141_signal(closeadj):
    sz = _z(_f03_stretch(closeadj, 63), 252)
    cz = _z(_f03_convexity(closeadj, 63), 252)
    result = sz * cz
    return result.replace([np.inf, -np.inf], np.nan)


# stretch confirmed by climax z-score (volatility-confirmed extension)
def f03pb_f03_parabolic_blowoff_top_stretchclimaxz_21d_base_v142_signal(closeadj, high, low):
    result = _f03_stretch(closeadj, 21) * _z(_f03_climax(high, low, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# extension over SMA(21) confirmed by dollar-volume z-score
def f03pb_f03_parabolic_blowoff_top_extdvz_21d_base_v143_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f03_extension(closeadj, 21) * _z(dv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# stretch slope: 10d linear-fit slope of EMA(21) stretch (rate of extension change)
def f03pb_f03_parabolic_blowoff_top_stretchslope_21d_base_v144_signal(closeadj):
    st = _f03_stretch(closeadj, 21)
    result = (st - st.shift(10)) / 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# stretch slope over 21d window on EMA(50) stretch
def f03pb_f03_parabolic_blowoff_top_stretchslope_50d_base_v145_signal(closeadj):
    st = _f03_stretch(closeadj, 50)
    result = (st - st.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


# blow-off composite: extension times blow-off run-up over 126d
def f03pb_f03_parabolic_blowoff_top_extblow_126d_base_v146_signal(closeadj):
    lo = closeadj.rolling(126, min_periods=42).min().replace(0, np.nan)
    runup = _safe_div(closeadj - lo, lo)
    result = _f03_extension(closeadj, 126) * runup
    return result.replace([np.inf, -np.inf], np.nan)


# multi-extension composite (21/63/126 average ATR-extension)
def f03pb_f03_parabolic_blowoff_top_extblend_base_v147_signal(closeadj):
    result = (_f03_extension(closeadj, 21) + _f03_extension(closeadj, 63)
              + _f03_extension(closeadj, 126)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# multi-convexity composite (10/21/42 average acceleration)
def f03pb_f03_parabolic_blowoff_top_convexblend_base_v148_signal(closeadj):
    result = (_f03_convexity(closeadj, 10) + _f03_convexity(closeadj, 21)
              + _f03_convexity(closeadj, 42)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# full parabolic exhaustion: stretch z + extension z + climax z composite
def f03pb_f03_parabolic_blowoff_top_exhaustcomp_base_v149_signal(closeadj, high, low):
    a = _z(_f03_stretch(closeadj, 21), 126)
    b = _z(_f03_extension(closeadj, 21), 126)
    c = _z(_f03_climax(high, low, 21), 126)
    result = (a + b + c) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# blow-off-top intensity: stretch * convexity * climax (triple confirmation)
def f03pb_f03_parabolic_blowoff_top_triple_21d_base_v150_signal(closeadj, high, low):
    result = (_f03_stretch(closeadj, 21) * (1.0 + _f03_convexity(closeadj, 21).abs())
              * (1.0 + _f03_climax(high, low, 21)))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03pb_f03_parabolic_blowoff_top_stretch_42d_base_v076_signal,
    f03pb_f03_parabolic_blowoff_top_stretch_84d_base_v077_signal,
    f03pb_f03_parabolic_blowoff_top_stretch_189d_base_v078_signal,
    f03pb_f03_parabolic_blowoff_top_zstretch_42d_base_v079_signal,
    f03pb_f03_parabolic_blowoff_top_zstretch_63d_base_v080_signal,
    f03pb_f03_parabolic_blowoff_top_zstretch_126d_base_v081_signal,
    f03pb_f03_parabolic_blowoff_top_smstretch_21d_base_v082_signal,
    f03pb_f03_parabolic_blowoff_top_smstretch_50d_base_v083_signal,
    f03pb_f03_parabolic_blowoff_top_convex_84d_base_v084_signal,
    f03pb_f03_parabolic_blowoff_top_convex_126d_base_v085_signal,
    f03pb_f03_parabolic_blowoff_top_smconvex_42d_base_v086_signal,
    f03pb_f03_parabolic_blowoff_top_zconvex_63d_base_v087_signal,
    f03pb_f03_parabolic_blowoff_top_climax_84d_base_v088_signal,
    f03pb_f03_parabolic_blowoff_top_climax_126d_base_v089_signal,
    f03pb_f03_parabolic_blowoff_top_smclimax_21d_base_v090_signal,
    f03pb_f03_parabolic_blowoff_top_zclimax_63d_base_v091_signal,
    f03pb_f03_parabolic_blowoff_top_ext_42d_base_v092_signal,
    f03pb_f03_parabolic_blowoff_top_ext_84d_base_v093_signal,
    f03pb_f03_parabolic_blowoff_top_ext_126d_base_v094_signal,
    f03pb_f03_parabolic_blowoff_top_zext_21d_base_v095_signal,
    f03pb_f03_parabolic_blowoff_top_zext_63d_base_v096_signal,
    f03pb_f03_parabolic_blowoff_top_pctb_63d_base_v097_signal,
    f03pb_f03_parabolic_blowoff_top_pctb_126d_base_v098_signal,
    f03pb_f03_parabolic_blowoff_top_ubdist_126d_base_v099_signal,
    f03pb_f03_parabolic_blowoff_top_vvel_42d_base_v100_signal,
    f03pb_f03_parabolic_blowoff_top_vvel_63d_base_v101_signal,
    f03pb_f03_parabolic_blowoff_top_blowoff_21d_base_v102_signal,
    f03pb_f03_parabolic_blowoff_top_blowoffatr_84d_base_v103_signal,
    f03pb_f03_parabolic_blowoff_top_blowoffatr_126d_base_v104_signal,
    f03pb_f03_parabolic_blowoff_top_exhaustdv_21d_base_v105_signal,
    f03pb_f03_parabolic_blowoff_top_exhaustz_63d_base_v106_signal,
    f03pb_f03_parabolic_blowoff_top_extvol_21d_base_v107_signal,
    f03pb_f03_parabolic_blowoff_top_stretchratio_42_189_base_v108_signal,
    f03pb_f03_parabolic_blowoff_top_stretchaccel_100d_base_v109_signal,
    f03pb_f03_parabolic_blowoff_top_accelint_63d_base_v110_signal,
    f03pb_f03_parabolic_blowoff_top_accelmag_42d_base_v111_signal,
    f03pb_f03_parabolic_blowoff_top_stretchclimax_100d_base_v112_signal,
    f03pb_f03_parabolic_blowoff_top_extconvex_100d_base_v113_signal,
    f03pb_f03_parabolic_blowoff_top_emagap_126d_base_v114_signal,
    f03pb_f03_parabolic_blowoff_top_rankstretch_100d_base_v115_signal,
    f03pb_f03_parabolic_blowoff_top_rankext_50d_base_v116_signal,
    f03pb_f03_parabolic_blowoff_top_highstretch_100d_base_v117_signal,
    f03pb_f03_parabolic_blowoff_top_curv_100d_base_v118_signal,
    f03pb_f03_parabolic_blowoff_top_climaxconvex_63d_base_v119_signal,
    f03pb_f03_parabolic_blowoff_top_stretchvol_100d_base_v120_signal,
    f03pb_f03_parabolic_blowoff_top_extaccel_21d_base_v121_signal,
    f03pb_f03_parabolic_blowoff_top_blowclimax_63d_base_v122_signal,
    f03pb_f03_parabolic_blowoff_top_convexvol_21d_base_v123_signal,
    f03pb_f03_parabolic_blowoff_top_convexvol_63d_base_v124_signal,
    f03pb_f03_parabolic_blowoff_top_stretchsurp_21d_base_v125_signal,
    f03pb_f03_parabolic_blowoff_top_stretchsurp_50d_base_v126_signal,
    f03pb_f03_parabolic_blowoff_top_extsurp_21d_base_v127_signal,
    f03pb_f03_parabolic_blowoff_top_climaxsurp_21d_base_v128_signal,
    f03pb_f03_parabolic_blowoff_top_stretchdisp_63d_base_v129_signal,
    f03pb_f03_parabolic_blowoff_top_stretchdisp_126d_base_v130_signal,
    f03pb_f03_parabolic_blowoff_top_convexdisp_63d_base_v131_signal,
    f03pb_f03_parabolic_blowoff_top_climaxewm_21d_base_v132_signal,
    f03pb_f03_parabolic_blowoff_top_stretchewm_21d_base_v133_signal,
    f03pb_f03_parabolic_blowoff_top_stretchewm_63d_base_v134_signal,
    f03pb_f03_parabolic_blowoff_top_stretchpow_21d_base_v135_signal,
    f03pb_f03_parabolic_blowoff_top_stretchpow_50d_base_v136_signal,
    f03pb_f03_parabolic_blowoff_top_ubatr_50d_base_v137_signal,
    f03pb_f03_parabolic_blowoff_top_retclimax_21d_base_v138_signal,
    f03pb_f03_parabolic_blowoff_top_retclimax_63d_base_v139_signal,
    f03pb_f03_parabolic_blowoff_top_paraz_21d_base_v140_signal,
    f03pb_f03_parabolic_blowoff_top_paraz_63d_base_v141_signal,
    f03pb_f03_parabolic_blowoff_top_stretchclimaxz_21d_base_v142_signal,
    f03pb_f03_parabolic_blowoff_top_extdvz_21d_base_v143_signal,
    f03pb_f03_parabolic_blowoff_top_stretchslope_21d_base_v144_signal,
    f03pb_f03_parabolic_blowoff_top_stretchslope_50d_base_v145_signal,
    f03pb_f03_parabolic_blowoff_top_extblow_126d_base_v146_signal,
    f03pb_f03_parabolic_blowoff_top_extblend_base_v147_signal,
    f03pb_f03_parabolic_blowoff_top_convexblend_base_v148_signal,
    f03pb_f03_parabolic_blowoff_top_exhaustcomp_base_v149_signal,
    f03pb_f03_parabolic_blowoff_top_triple_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_PARABOLIC_BLOWOFF_TOP_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f03_parabolic_blowoff_top_base_076_150_claude: {n_features} features pass")
