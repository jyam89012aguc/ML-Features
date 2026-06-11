import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives (cyclical trend structure / moving averages) =====
def _f01_ma(close, w):
    return close.rolling(w, min_periods=max(1, w // 2)).mean()


def _f01_ema(close, span):
    return close.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _f01_pdist(close, w):
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.log(close.replace(0, np.nan) / ma.replace(0, np.nan))


def _f01_emadist(close, span):
    ema = close.ewm(span=span, min_periods=max(1, span // 2)).mean()
    return np.log(close.replace(0, np.nan) / ema.replace(0, np.nan))


def _f01_emaslope(close, span, k):
    ema = close.ewm(span=span, min_periods=max(1, span // 2)).mean()
    return np.log(ema.replace(0, np.nan) / ema.shift(k).replace(0, np.nan)) / float(k)


def _f01_maslope(close, w, k):
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.log(ma.replace(0, np.nan) / ma.shift(k).replace(0, np.nan)) / float(k)


def _f01_maband_pos(close, w):
    # position of price within the +/- 1 rolling-std band of the w-day MA (Bollinger-style %b)
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = close.rolling(w, min_periods=max(1, w // 2)).std()
    upper = ma + 2.0 * sd
    lower = ma - 2.0 * sd
    return (close - lower) / (upper - lower).replace(0, np.nan)


def _f01_above_frac(close, w, ow):
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    above = (close > ma).astype(float)
    return above.rolling(ow, min_periods=max(1, ow // 2)).mean()


def _f01_trendpersist(close, w, ow):
    d = _f01_pdist(close, w)
    return np.sign(d).rolling(ow, min_periods=max(1, ow // 2)).mean()


# ============================================================
# price vs 21d EMA (fast exponential trend distance)
def f01ct_f01_cyclical_trend_structure_emadist_21d_base_v076_signal(closeadj):
    b = _f01_emadist(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 63d EMA
def f01ct_f01_cyclical_trend_structure_emadist_63d_base_v077_signal(closeadj):
    b = _f01_emadist(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 126d EMA
def f01ct_f01_cyclical_trend_structure_emadist_126d_base_v078_signal(closeadj):
    b = _f01_emadist(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 252d EMA (long exponential trend distance)
def f01ct_f01_cyclical_trend_structure_emadist_252d_base_v079_signal(closeadj):
    b = _f01_emadist(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA log-slope over a quarter (exponential trend direction)
def f01ct_f01_cyclical_trend_structure_emaslope_63d_base_v080_signal(closeadj):
    b = _f01_emaslope(closeadj, 63, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EMA log-slope over a quarter
def f01ct_f01_cyclical_trend_structure_emaslope_126d_base_v081_signal(closeadj):
    b = _f01_emaslope(closeadj, 126, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA log-slope over a half-year, z-scored vs its own 504d history (trend-strength regime)
def f01ct_f01_cyclical_trend_structure_emaslope_252d_base_v082_signal(closeadj):
    sl = _f01_emaslope(closeadj, 252, 126)
    b = _z(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MACD-style spread: 63d EMA minus 126d EMA, normalized by price (trend impulse)
def f01ct_f01_cyclical_trend_structure_macd_63v126_base_v083_signal(closeadj):
    e1 = _f01_ema(closeadj, 63)
    e2 = _f01_ema(closeadj, 126)
    b = (e1 - e2) / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MACD-style spread: 21d EMA minus 63d EMA, normalized (fast trend impulse)
def f01ct_f01_cyclical_trend_structure_macd_21v63_base_v084_signal(closeadj):
    e1 = _f01_ema(closeadj, 21)
    e2 = _f01_ema(closeadj, 63)
    b = (e1 - e2) / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MACD histogram: MACD(21,63) minus its own 21d EMA signal line (trend acceleration)
def f01ct_f01_cyclical_trend_structure_macdhist_base_v085_signal(closeadj):
    e1 = _f01_ema(closeadj, 21)
    e2 = _f01_ema(closeadj, 63)
    macd = (e1 - e2) / closeadj.replace(0, np.nan)
    sig = macd.ewm(span=21, min_periods=10).mean()
    b = macd - sig
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger %b position vs the 63d MA band (trend-band location)
def f01ct_f01_cyclical_trend_structure_bandpos_63d_base_v086_signal(closeadj):
    b = _f01_maband_pos(closeadj, 63) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger %b position vs the 126d MA band
def f01ct_f01_cyclical_trend_structure_bandpos_126d_base_v087_signal(closeadj):
    b = _f01_maband_pos(closeadj, 126) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger %b position vs the 252d MA band (long trend-band location)
def f01ct_f01_cyclical_trend_structure_bandpos_252d_base_v088_signal(closeadj):
    b = _f01_maband_pos(closeadj, 252) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend slope via OLS on log-price over 126d (per-day drift)
def f01ct_f01_cyclical_trend_structure_olsslope_126d_base_v089_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _f(a):
        x = np.arange(len(a), dtype=float)
        xm = x.mean()
        ym = a.mean()
        denom = ((x - xm) ** 2).sum()
        return ((x - xm) * (a - ym)).sum() / denom
    b = lp.rolling(126, min_periods=63).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend slope via OLS on log-price over 252d (multi-year per-day drift)
def f01ct_f01_cyclical_trend_structure_olsslope_252d_base_v090_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _f(a):
        x = np.arange(len(a), dtype=float)
        xm = x.mean()
        ym = a.mean()
        denom = ((x - xm) ** 2).sum()
        return ((x - xm) * (a - ym)).sum() / denom
    b = lp.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend slope via OLS on log-price over 504d (deep-cycle per-day drift)
def f01ct_f01_cyclical_trend_structure_olsslope_504d_base_v091_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _f(a):
        x = np.arange(len(a), dtype=float)
        xm = x.mean()
        ym = a.mean()
        denom = ((x - xm) ** 2).sum()
        return ((x - xm) * (a - ym)).sum() / denom
    b = lp.rolling(504, min_periods=252).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R-squared of the 252d log-price trend line (trend linearity / cycle smoothness)
def f01ct_f01_cyclical_trend_structure_trendr2_252d_base_v092_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _f(a):
        x = np.arange(len(a), dtype=float)
        xm = x.mean()
        sxx = ((x - xm) ** 2).sum()
        ym = a.mean()
        sxy = ((x - xm) * (a - ym)).sum()
        syy = ((a - ym) ** 2).sum()
        if syy <= 0 or sxx <= 0:
            return np.nan
        return (sxy * sxy) / (sxx * syy)
    b = lp.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R-squared of the 126d log-price trend line
def f01ct_f01_cyclical_trend_structure_trendr2_126d_base_v093_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _f(a):
        x = np.arange(len(a), dtype=float)
        xm = x.mean()
        sxx = ((x - xm) ** 2).sum()
        ym = a.mean()
        sxy = ((x - xm) * (a - ym)).sum()
        syy = ((a - ym) ** 2).sum()
        if syy <= 0 or sxx <= 0:
            return np.nan
        return (sxy * sxy) / (sxx * syy)
    b = lp.rolling(126, min_periods=63).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend conviction over 504d: OLS R-squared of the deep-cycle log-price line (linearity)
def f01ct_f01_cyclical_trend_structure_trendconv_252d_base_v094_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _f(a):
        x = np.arange(len(a), dtype=float)
        xm = x.mean()
        sxx = ((x - xm) ** 2).sum()
        ym = a.mean()
        sxy = ((x - xm) * (a - ym)).sum()
        syy = ((a - ym) ** 2).sum()
        if syy <= 0 or sxx <= 0:
            return np.nan
        return (sxy * sxy) / (sxx * syy)
    b = lp.rolling(504, min_periods=252).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of price from the 252d OLS trend line at its current end (residual gap)
def f01ct_f01_cyclical_trend_structure_trendresid_252d_base_v095_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _f(a):
        x = np.arange(len(a), dtype=float)
        xm = x.mean()
        sxx = ((x - xm) ** 2).sum()
        ym = a.mean()
        sxy = ((x - xm) * (a - ym)).sum()
        if sxx <= 0:
            return np.nan
        slope = sxy / sxx
        intercept = ym - slope * xm
        fit_end = intercept + slope * (len(a) - 1)
        return a[-1] - fit_end
    b = lp.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs the 504d median (robust long trend anchor distance)
def f01ct_f01_cyclical_trend_structure_meddist_504d_base_v096_signal(closeadj):
    med = closeadj.rolling(504, min_periods=252).median()
    b = np.log(closeadj.replace(0, np.nan) / med.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs the 252d median, z-scored vs its own history
def f01ct_f01_cyclical_trend_structure_meddist_252d_base_v097_signal(closeadj):
    med = closeadj.rolling(252, min_periods=126).median()
    d = np.log(closeadj.replace(0, np.nan) / med.replace(0, np.nan))
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between price-vs-EMA and price-vs-SMA at 63d (trend-lag asymmetry)
def f01ct_f01_cyclical_trend_structure_emasmaspr_63d_base_v098_signal(closeadj):
    ed = _f01_emadist(closeadj, 63)
    sd = _f01_pdist(closeadj, 63)
    b = ed - sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between price-vs-EMA and price-vs-SMA at 252d (long trend-lag asymmetry)
def f01ct_f01_cyclical_trend_structure_emasmaspr_252d_base_v099_signal(closeadj):
    ed = _f01_emadist(closeadj, 252)
    sd = _f01_pdist(closeadj, 252)
    b = ed - sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 126d MA, smoothed by a 21d EMA (persistent trend extension)
def f01ct_f01_cyclical_trend_structure_pdistsm_126d_base_v100_signal(closeadj):
    d = _f01_pdist(closeadj, 126)
    b = d.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triple-MA alignment: signed product of (price-ma63), (ma63-ma126), (ma126-ma252)
def f01ct_f01_cyclical_trend_structure_triplealign_base_v101_signal(closeadj):
    m63 = _f01_ma(closeadj, 63)
    m126 = _f01_ma(closeadj, 126)
    m252 = _f01_ma(closeadj, 252)
    s1 = np.sign(closeadj - m63)
    s2 = np.sign(m63 - m126)
    s3 = np.sign(m126 - m252)
    mag = ((closeadj / m252.replace(0, np.nan)) - 1.0).abs()
    b = s1 * s2 * s3 * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last quarter the fast EMA(21) sits above the slow EMA(126) (trend regime %)
def f01ct_f01_cyclical_trend_structure_emaregime_base_v102_signal(closeadj):
    e1 = _f01_ema(closeadj, 21)
    e2 = _f01_ema(closeadj, 126)
    up = (e1 > e2).astype(float)
    b = up.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the price-vs-252d-MA distance smoothed (trend-extension velocity)
def f01ct_f01_cyclical_trend_structure_distvel_252d_base_v103_signal(closeadj):
    d = _f01_pdist(closeadj, 252)
    sm = d.ewm(span=21, min_periods=10).mean()
    b = sm.diff(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Coppock-style long-trend curve: weighted sum of 252d and 126d ROC, smoothed
def f01ct_f01_cyclical_trend_structure_coppock_base_v104_signal(closeadj):
    roc1 = closeadj / closeadj.shift(252).replace(0, np.nan) - 1.0
    roc2 = closeadj / closeadj.shift(126).replace(0, np.nan) - 1.0
    b = (roc1 + roc2).ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MA-minus-median gap (trend skew: mean pulled above/below median = cyclical tail)
def f01ct_f01_cyclical_trend_structure_dualanchor_252d_base_v105_signal(closeadj):
    ma = _f01_ma(closeadj, 252)
    med = closeadj.rolling(252, min_periods=126).median()
    b = np.log(ma.replace(0, np.nan) / med.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how far the 63d MA sits above the 252d MA in 252d-vol units (stacking z)
def f01ct_f01_cyclical_trend_structure_stackz_63v252_base_v106_signal(closeadj):
    m63 = _f01_ma(closeadj, 63)
    m252 = _f01_ma(closeadj, 252)
    spr = np.log(m63.replace(0, np.nan) / m252.replace(0, np.nan))
    b = _z(spr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend persistence breadth: avg of sign-persistence across 63/126/252 MAs
def f01ct_f01_cyclical_trend_structure_persistbreadth_base_v107_signal(closeadj):
    p1 = _f01_trendpersist(closeadj, 63, 63)
    p2 = _f01_trendpersist(closeadj, 126, 63)
    p3 = _f01_trendpersist(closeadj, 252, 63)
    b = pd.concat([p1, p2, p3], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# disagreement between fast and slow trend persistence (regime-transition signal)
def f01ct_f01_cyclical_trend_structure_persistdiverge_base_v108_signal(closeadj):
    p_fast = _f01_trendpersist(closeadj, 63, 63)
    p_slow = _f01_trendpersist(closeadj, 504, 63)
    b = p_fast - p_slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-agreement of 21d vs 252d EMA-slopes over a quarter (fast/long trend concord %)
def f01ct_f01_cyclical_trend_structure_emaslopespr_base_v109_signal(closeadj):
    s_s = np.sign(_f01_emaslope(closeadj, 21, 21))
    s_l = np.sign(_f01_emaslope(closeadj, 252, 21))
    agree = (s_s == s_l).astype(float)
    frac = agree.rolling(63, min_periods=21).mean()
    depth = (_f01_emaslope(closeadj, 63, 21)).abs().rolling(63, min_periods=21).mean()
    b = frac + 50.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized 252d trend stretch, percentile-ranked vs its own 504d history
def f01ct_f01_cyclical_trend_structure_normstretch_252d_base_v110_signal(closeadj):
    ma = _f01_ma(closeadj, 252)
    vol = np.log(closeadj.replace(0, np.nan)).diff().rolling(252, min_periods=126).std()
    stretch = (np.log(closeadj.replace(0, np.nan) / ma.replace(0, np.nan))) / vol.replace(0, np.nan)
    b = stretch.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 126d MA normalized by downside semi-deviation (asymmetric trend stretch)
def f01ct_f01_cyclical_trend_structure_normstretch_126d_base_v111_signal(closeadj):
    ma = _f01_ma(closeadj, 126)
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    downside = lr.clip(upper=0.0)
    semidev = (downside.pow(2).rolling(126, min_periods=63).mean()) ** 0.5
    b = (np.log(closeadj.replace(0, np.nan) / ma.replace(0, np.nan))) / semidev.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of the 252d MA: second difference of the MA over a quarter (trend bend)
def f01ct_f01_cyclical_trend_structure_maaccel_252d_base_v112_signal(closeadj):
    ma = _f01_ma(closeadj, 252)
    lma = np.log(ma.replace(0, np.nan))
    b = lma - 2.0 * lma.shift(63) + lma.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of the 126d MA over a month (intermediate trend bend)
def f01ct_f01_cyclical_trend_structure_maaccel_126d_base_v113_signal(closeadj):
    ma = _f01_ma(closeadj, 126)
    lma = np.log(ma.replace(0, np.nan))
    b = lma - 2.0 * lma.shift(21) + lma.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price position relative to the 504d high-low channel midline (cycle midline distance)
def f01ct_f01_cyclical_trend_structure_chanmid_504d_base_v114_signal(closeadj):
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    mid = (hi + lo) / 2.0
    b = np.log(closeadj.replace(0, np.nan) / mid.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 252d MA relative to the slope of the 504d MA (trend handoff ratio)
def f01ct_f01_cyclical_trend_structure_slopehandoff_base_v115_signal(closeadj):
    s1 = _f01_maslope(closeadj, 252, 63)
    s2 = _f01_maslope(closeadj, 504, 63)
    b = np.tanh(200.0 * (s1 - s2))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 2y with positive 252d MA slope (long uptrend time)
def f01ct_f01_cyclical_trend_structure_uptrendtime_base_v116_signal(closeadj):
    sl = _f01_maslope(closeadj, 252, 21)
    up = (sl > 0).astype(float)
    b = up.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 252d MA, year-over-year acceleration (cycle-phase second difference)
def f01ct_f01_cyclical_trend_structure_distyoyaccel_base_v117_signal(closeadj):
    d = _f01_pdist(closeadj, 252)
    b = d - 2.0 * d.shift(126) + d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger %b at 252d, momentum over a quarter (trend-band climb)
def f01ct_f01_cyclical_trend_structure_bandmom_252d_base_v118_signal(closeadj):
    pb = _f01_maband_pos(closeadj, 252)
    b = pb - pb.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend slope sign-magnitude: signed sqrt of the 252d OLS slope (compressed drift)
def f01ct_f01_cyclical_trend_structure_olsslopesqrt_252d_base_v119_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _f(a):
        x = np.arange(len(a), dtype=float)
        xm = x.mean()
        sxx = ((x - xm) ** 2).sum()
        ym = a.mean()
        return ((x - xm) * (a - ym)).sum() / sxx
    sl = lp.rolling(252, min_periods=126).apply(_f, raw=True)
    b = np.sign(sl) * (sl.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of 63d net change to 252d net change of the MA (trend front-loading)
def f01ct_f01_cyclical_trend_structure_frontload_base_v120_signal(closeadj):
    ma = _f01_ma(closeadj, 126)
    n_short = np.log(ma.replace(0, np.nan) / ma.shift(63).replace(0, np.nan))
    n_long = np.log(ma.replace(0, np.nan) / ma.shift(252).replace(0, np.nan))
    b = n_short / n_long.replace(0, np.nan)
    b = b.clip(-5, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of the price-vs-63d-MA distance vs its own 252d history
def f01ct_f01_cyclical_trend_structure_pdistrank_63d_base_v121_signal(closeadj):
    d = _f01_pdist(closeadj, 63)
    b = d.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger band squeeze: 252d band width relative to its own 252d typical width
def f01ct_f01_cyclical_trend_structure_bandwidth_252d_base_v122_signal(closeadj):
    ma = _f01_ma(closeadj, 252)
    sd = closeadj.rolling(252, min_periods=126).std()
    width = (4.0 * sd) / ma.replace(0, np.nan)
    b = width / width.rolling(252, min_periods=126).mean().replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-extension reversal: price-vs-21d-MA distance minus its 63d mean (overextension)
def f01ct_f01_cyclical_trend_structure_overext_21d_base_v123_signal(closeadj):
    d = _f01_pdist(closeadj, 21)
    b = d - d.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how concentrated the 5 MA levels are around price (trend-confluence, inverse spread)
def f01ct_f01_cyclical_trend_structure_confluence_base_v124_signal(closeadj):
    m21 = _f01_ma(closeadj, 21)
    m63 = _f01_ma(closeadj, 63)
    m126 = _f01_ma(closeadj, 126)
    m252 = _f01_ma(closeadj, 252)
    rel = pd.concat([np.log(closeadj / m21.replace(0, np.nan)),
                     np.log(closeadj / m63.replace(0, np.nan)),
                     np.log(closeadj / m126.replace(0, np.nan)),
                     np.log(closeadj / m252.replace(0, np.nan))], axis=1)
    b = -rel.abs().mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional efficiency of price over 126d (net log-move / total abs log-move)
def f01ct_f01_cyclical_trend_structure_diref_126d_base_v125_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(126, min_periods=63).sum().abs()
    gross = lr.abs().rolling(126, min_periods=63).sum()
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional efficiency of price over 504d (deep-cycle trend cleanliness, unsigned)
def f01ct_f01_cyclical_trend_structure_diref_252d_base_v126_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(504, min_periods=252).sum().abs()
    gross = lr.abs().rolling(504, min_periods=252).sum()
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 252d MA z-scored vs its own 504d slope history (trend-strength regime)
def f01ct_f01_cyclical_trend_structure_slopez_252d_base_v127_signal(closeadj):
    sl = _f01_maslope(closeadj, 252, 63)
    b = _z(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 126d MA z-scored vs its own 252d slope history
def f01ct_f01_cyclical_trend_structure_slopez_126d_base_v128_signal(closeadj):
    sl = _f01_maslope(closeadj, 126, 21)
    b = _z(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance between 21d EMA and 252d SMA, normalized (full fast-vs-long trend gap)
def f01ct_f01_cyclical_trend_structure_fastlonggap_base_v129_signal(closeadj):
    ema = _f01_ema(closeadj, 21)
    sma = _f01_ma(closeadj, 252)
    b = np.log(ema.replace(0, np.nan) / sma.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of months (21d blocks) in the last year with rising 63d MA (trend cadence)
def f01ct_f01_cyclical_trend_structure_risingmonths_base_v130_signal(closeadj):
    ma = _f01_ma(closeadj, 63)
    rising = (ma > ma.shift(21)).astype(float)
    cadence = rising.rolling(252, min_periods=126).mean()
    depth = np.log(ma.replace(0, np.nan) / ma.shift(21).replace(0, np.nan)).abs() \
        .rolling(63, min_periods=21).mean()
    b = cadence + 20.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-gap lead: current 252d MA-gap minus the same gap anchored a quarter ago (gap drift)
def f01ct_f01_cyclical_trend_structure_lagmagap_252d_base_v131_signal(closeadj):
    ma = _f01_ma(closeadj, 252)
    gap_now = np.log(closeadj.replace(0, np.nan) / ma.replace(0, np.nan))
    gap_lag = np.log(closeadj.replace(0, np.nan) / ma.shift(63).replace(0, np.nan))
    b = gap_now - gap_lag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the OLS trend residual (mean-reversion vs trend-following tilt at 126d)
def f01ct_f01_cyclical_trend_structure_residvel_126d_base_v132_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _f(a):
        x = np.arange(len(a), dtype=float)
        xm = x.mean()
        sxx = ((x - xm) ** 2).sum()
        ym = a.mean()
        slope = ((x - xm) * (a - ym)).sum() / sxx
        intercept = ym - slope * xm
        return a[-1] - (intercept + slope * (len(a) - 1))
    resid2 = lp.rolling(126, min_periods=63).apply(_f, raw=True)
    b = resid2.diff(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year price stays inside +/-1 std of the 252d MA (trend calmness)
def f01ct_f01_cyclical_trend_structure_inband_252d_base_v133_signal(closeadj):
    ma = _f01_ma(closeadj, 252)
    sd = closeadj.rolling(252, min_periods=126).std()
    inside = ((closeadj - ma).abs() <= sd).astype(float)
    calm = inside.rolling(252, min_periods=126).mean()
    stretch = ((closeadj - ma).abs() / sd.replace(0, np.nan)) \
        .rolling(63, min_periods=21).mean()
    b = calm - 0.1 * stretch
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Coppock-curve slope (long trend-curve velocity over a quarter)
def f01ct_f01_cyclical_trend_structure_coppockvel_base_v134_signal(closeadj):
    roc1 = closeadj / closeadj.shift(252).replace(0, np.nan) - 1.0
    roc2 = closeadj / closeadj.shift(126).replace(0, np.nan) - 1.0
    cop = (roc1 + roc2).ewm(span=63, min_periods=31).mean()
    b = cop.diff(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ribbon tilt: fast-MA centroid (21,63) minus slow-MA centroid (252,504), log (stack lean)
def f01ct_f01_cyclical_trend_structure_ribboncentroid_base_v135_signal(closeadj):
    m21 = np.log(_f01_ma(closeadj, 21).replace(0, np.nan))
    m63 = np.log(_f01_ma(closeadj, 63).replace(0, np.nan))
    m252 = np.log(_f01_ma(closeadj, 252).replace(0, np.nan))
    m504 = np.log(_f01_ma(closeadj, 504).replace(0, np.nan))
    fast = (m21 + m63) / 2.0
    slow = (m252 + m504) / 2.0
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ribbon slope dispersion: std of the 21/63/126/252/504 MA slopes (trend-speed disagreement)
def f01ct_f01_cyclical_trend_structure_centroidslope_base_v136_signal(closeadj):
    s21 = _f01_maslope(closeadj, 21, 21)
    s63 = _f01_maslope(closeadj, 63, 21)
    s126 = _f01_maslope(closeadj, 126, 21)
    s252 = _f01_maslope(closeadj, 252, 21)
    s504 = _f01_maslope(closeadj, 504, 21)
    b = pd.concat([s21, s63, s126, s252, s504], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend skewness: skew of daily log-returns over 252d (cyclical up/down asymmetry)
def f01ct_f01_cyclical_trend_structure_retskew_252d_base_v137_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    b = lr.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# instability of the 63d-vs-252d MA premium over a quarter (trend-regime churn)
def f01ct_f01_cyclical_trend_structure_fastpremium_base_v138_signal(closeadj):
    m63 = _f01_ma(closeadj, 63)
    m252 = _f01_ma(closeadj, 252)
    spr = np.log(m63.replace(0, np.nan) / m252.replace(0, np.nan))
    b = spr.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in the (tanh-bounded) 504d MA distance over a half-year (deep-cycle phase shift)
def f01ct_f01_cyclical_trend_structure_deepexttanh_base_v139_signal(closeadj):
    d = np.tanh(3.0 * _f01_pdist(closeadj, 504))
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread of Bollinger %b between 63d and 252d bands (short vs long band position)
def f01ct_f01_cyclical_trend_structure_bandposspr_base_v140_signal(closeadj):
    p_s = _f01_maband_pos(closeadj, 63)
    p_l = _f01_maband_pos(closeadj, 252)
    b = p_s - p_l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend half-life proxy: 21d autocorrelation-style persistence of MA-distance sign
def f01ct_f01_cyclical_trend_structure_signpersist_126d_base_v141_signal(closeadj):
    d = _f01_pdist(closeadj, 126)
    s = np.sign(d)
    b = (s * s.shift(21)).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MA-slope minus the OLS-fit slope (smoothing-lag-driven trend bias)
def f01ct_f01_cyclical_trend_structure_slopebias_252d_base_v142_signal(closeadj):
    maslope = _f01_maslope(closeadj, 252, 63)
    lp = np.log(closeadj.replace(0, np.nan))

    def _f(a):
        x = np.arange(len(a), dtype=float)
        xm = x.mean()
        sxx = ((x - xm) ** 2).sum()
        ym = a.mean()
        return ((x - xm) * (a - ym)).sum() / sxx
    ols = lp.rolling(252, min_periods=126).apply(_f, raw=True)
    b = maslope - ols
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 252d MA scaled by the directional efficiency (clean-trend stretch)
def f01ct_f01_cyclical_trend_structure_cleanstretch_base_v143_signal(closeadj):
    d = _f01_pdist(closeadj, 252)
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(252, min_periods=126).sum().abs()
    gross = lr.abs().rolling(252, min_periods=126).sum()
    eff = net / gross.replace(0, np.nan)
    b = d * eff
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count-weighted regime: fraction of last year with EMA(63)>EMA(252) weighted by gap
def f01ct_f01_cyclical_trend_structure_emaregimedeep_base_v144_signal(closeadj):
    e1 = _f01_ema(closeadj, 63)
    e2 = _f01_ema(closeadj, 252)
    up = (e1 > e2).astype(float)
    frac = up.rolling(252, min_periods=126).mean()
    gap = np.log(e1.replace(0, np.nan) / e2.replace(0, np.nan)) \
        .rolling(63, min_periods=21).mean()
    b = frac + 5.0 * gap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# kurtosis of daily log-returns over 252d (trend smoothness vs jump regime)
def f01ct_f01_cyclical_trend_structure_retkurt_252d_base_v145_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    b = lr.rolling(252, min_periods=126).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of the 63d MA from the 504d high-low midline (mid-trend vs cycle midline)
def f01ct_f01_cyclical_trend_structure_mavsmid_504d_base_v146_signal(closeadj):
    m63 = _f01_ma(closeadj, 63)
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    mid = (hi + lo) / 2.0
    b = np.log(m63.replace(0, np.nan) / mid.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend turning detector: sign change of 126d MA slope, recency-weighted
def f01ct_f01_cyclical_trend_structure_turn_126d_base_v147_signal(closeadj):
    sl = _f01_maslope(closeadj, 126, 21)
    turned = (np.sign(sl) != np.sign(sl.shift(1))).astype(float)
    fresh = turned.ewm(span=63, min_periods=21).mean()
    b = fresh * np.sign(sl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# denoising benefit: 5d-smoothed-price trend gap minus the raw-price trend gap (noise lift)
def f01ct_f01_cyclical_trend_structure_denoisegap_252d_base_v148_signal(closeadj):
    sm = closeadj.rolling(5, min_periods=3).mean()
    ma_sm = sm.rolling(252, min_periods=126).mean()
    gap_sm = np.log(sm.replace(0, np.nan) / ma_sm.replace(0, np.nan))
    gap_raw = _f01_pdist(closeadj, 252)
    b = gap_sm - gap_raw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the 5 MA slopes (computed over 63d) that point the same way as price-126 trend
def f01ct_f01_cyclical_trend_structure_slopealign_base_v149_signal(closeadj):
    ref = np.sign(_f01_maslope(closeadj, 126, 63))
    s21 = np.sign(_f01_maslope(closeadj, 21, 63))
    s63 = np.sign(_f01_maslope(closeadj, 63, 63))
    s252 = np.sign(_f01_maslope(closeadj, 252, 63))
    s504 = np.sign(_f01_maslope(closeadj, 504, 63))
    agree = ((s21 == ref).astype(float) + (s63 == ref).astype(float)
             + (s252 == ref).astype(float) + (s504 == ref).astype(float)) / 4.0
    depth = _f01_pdist(closeadj, 126).abs().rolling(21, min_periods=10).mean()
    b = agree + 10.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite trend-structure score: stack-tilt x long-direction x clean-trend
def f01ct_f01_cyclical_trend_structure_composite_base_v150_signal(closeadj):
    m63 = _f01_ma(closeadj, 63)
    m252 = _f01_ma(closeadj, 252)
    tilt = np.tanh(80.0 * np.log(m63.replace(0, np.nan) / m252.replace(0, np.nan)))
    direction = np.tanh(200.0 * _f01_maslope(closeadj, 252, 63))
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(252, min_periods=126).sum().abs()
    gross = lr.abs().rolling(252, min_periods=126).sum()
    eff = net / gross.replace(0, np.nan)
    b = tilt * direction * eff
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01ct_f01_cyclical_trend_structure_emadist_21d_base_v076_signal,
    f01ct_f01_cyclical_trend_structure_emadist_63d_base_v077_signal,
    f01ct_f01_cyclical_trend_structure_emadist_126d_base_v078_signal,
    f01ct_f01_cyclical_trend_structure_emadist_252d_base_v079_signal,
    f01ct_f01_cyclical_trend_structure_emaslope_63d_base_v080_signal,
    f01ct_f01_cyclical_trend_structure_emaslope_126d_base_v081_signal,
    f01ct_f01_cyclical_trend_structure_emaslope_252d_base_v082_signal,
    f01ct_f01_cyclical_trend_structure_macd_63v126_base_v083_signal,
    f01ct_f01_cyclical_trend_structure_macd_21v63_base_v084_signal,
    f01ct_f01_cyclical_trend_structure_macdhist_base_v085_signal,
    f01ct_f01_cyclical_trend_structure_bandpos_63d_base_v086_signal,
    f01ct_f01_cyclical_trend_structure_bandpos_126d_base_v087_signal,
    f01ct_f01_cyclical_trend_structure_bandpos_252d_base_v088_signal,
    f01ct_f01_cyclical_trend_structure_olsslope_126d_base_v089_signal,
    f01ct_f01_cyclical_trend_structure_olsslope_252d_base_v090_signal,
    f01ct_f01_cyclical_trend_structure_olsslope_504d_base_v091_signal,
    f01ct_f01_cyclical_trend_structure_trendr2_252d_base_v092_signal,
    f01ct_f01_cyclical_trend_structure_trendr2_126d_base_v093_signal,
    f01ct_f01_cyclical_trend_structure_trendconv_252d_base_v094_signal,
    f01ct_f01_cyclical_trend_structure_trendresid_252d_base_v095_signal,
    f01ct_f01_cyclical_trend_structure_meddist_504d_base_v096_signal,
    f01ct_f01_cyclical_trend_structure_meddist_252d_base_v097_signal,
    f01ct_f01_cyclical_trend_structure_emasmaspr_63d_base_v098_signal,
    f01ct_f01_cyclical_trend_structure_emasmaspr_252d_base_v099_signal,
    f01ct_f01_cyclical_trend_structure_pdistsm_126d_base_v100_signal,
    f01ct_f01_cyclical_trend_structure_triplealign_base_v101_signal,
    f01ct_f01_cyclical_trend_structure_emaregime_base_v102_signal,
    f01ct_f01_cyclical_trend_structure_distvel_252d_base_v103_signal,
    f01ct_f01_cyclical_trend_structure_coppock_base_v104_signal,
    f01ct_f01_cyclical_trend_structure_dualanchor_252d_base_v105_signal,
    f01ct_f01_cyclical_trend_structure_stackz_63v252_base_v106_signal,
    f01ct_f01_cyclical_trend_structure_persistbreadth_base_v107_signal,
    f01ct_f01_cyclical_trend_structure_persistdiverge_base_v108_signal,
    f01ct_f01_cyclical_trend_structure_emaslopespr_base_v109_signal,
    f01ct_f01_cyclical_trend_structure_normstretch_252d_base_v110_signal,
    f01ct_f01_cyclical_trend_structure_normstretch_126d_base_v111_signal,
    f01ct_f01_cyclical_trend_structure_maaccel_252d_base_v112_signal,
    f01ct_f01_cyclical_trend_structure_maaccel_126d_base_v113_signal,
    f01ct_f01_cyclical_trend_structure_chanmid_504d_base_v114_signal,
    f01ct_f01_cyclical_trend_structure_slopehandoff_base_v115_signal,
    f01ct_f01_cyclical_trend_structure_uptrendtime_base_v116_signal,
    f01ct_f01_cyclical_trend_structure_distyoyaccel_base_v117_signal,
    f01ct_f01_cyclical_trend_structure_bandmom_252d_base_v118_signal,
    f01ct_f01_cyclical_trend_structure_olsslopesqrt_252d_base_v119_signal,
    f01ct_f01_cyclical_trend_structure_frontload_base_v120_signal,
    f01ct_f01_cyclical_trend_structure_pdistrank_63d_base_v121_signal,
    f01ct_f01_cyclical_trend_structure_bandwidth_252d_base_v122_signal,
    f01ct_f01_cyclical_trend_structure_overext_21d_base_v123_signal,
    f01ct_f01_cyclical_trend_structure_confluence_base_v124_signal,
    f01ct_f01_cyclical_trend_structure_diref_126d_base_v125_signal,
    f01ct_f01_cyclical_trend_structure_diref_252d_base_v126_signal,
    f01ct_f01_cyclical_trend_structure_slopez_252d_base_v127_signal,
    f01ct_f01_cyclical_trend_structure_slopez_126d_base_v128_signal,
    f01ct_f01_cyclical_trend_structure_fastlonggap_base_v129_signal,
    f01ct_f01_cyclical_trend_structure_risingmonths_base_v130_signal,
    f01ct_f01_cyclical_trend_structure_lagmagap_252d_base_v131_signal,
    f01ct_f01_cyclical_trend_structure_residvel_126d_base_v132_signal,
    f01ct_f01_cyclical_trend_structure_inband_252d_base_v133_signal,
    f01ct_f01_cyclical_trend_structure_coppockvel_base_v134_signal,
    f01ct_f01_cyclical_trend_structure_ribboncentroid_base_v135_signal,
    f01ct_f01_cyclical_trend_structure_centroidslope_base_v136_signal,
    f01ct_f01_cyclical_trend_structure_retskew_252d_base_v137_signal,
    f01ct_f01_cyclical_trend_structure_fastpremium_base_v138_signal,
    f01ct_f01_cyclical_trend_structure_deepexttanh_base_v139_signal,
    f01ct_f01_cyclical_trend_structure_bandposspr_base_v140_signal,
    f01ct_f01_cyclical_trend_structure_signpersist_126d_base_v141_signal,
    f01ct_f01_cyclical_trend_structure_slopebias_252d_base_v142_signal,
    f01ct_f01_cyclical_trend_structure_cleanstretch_base_v143_signal,
    f01ct_f01_cyclical_trend_structure_emaregimedeep_base_v144_signal,
    f01ct_f01_cyclical_trend_structure_retkurt_252d_base_v145_signal,
    f01ct_f01_cyclical_trend_structure_mavsmid_504d_base_v146_signal,
    f01ct_f01_cyclical_trend_structure_turn_126d_base_v147_signal,
    f01ct_f01_cyclical_trend_structure_denoisegap_252d_base_v148_signal,
    f01ct_f01_cyclical_trend_structure_slopealign_base_v149_signal,
    f01ct_f01_cyclical_trend_structure_composite_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_CYCLICAL_TREND_STRUCTURE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f01_cyclical_trend_structure_base_076_150_claude: %d features pass" % n_features)
