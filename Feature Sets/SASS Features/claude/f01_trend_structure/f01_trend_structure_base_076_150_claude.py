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


# ===== folder domain primitives (trend structure: MA / slope / channel) =====
def _f01_sma(close, w):
    return close.rolling(w, min_periods=max(1, w // 2)).mean()


def _f01_ema(close, w):
    return close.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _f01_pxma(close, w):
    ma = _f01_sma(close, w)
    return close / ma.replace(0, np.nan) - 1.0


def _f01_slope(close, w):
    lp = np.log(close.replace(0, np.nan))
    x = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    mp = max(2, w // 2)
    xm = x.rolling(w, min_periods=mp).mean()
    ym = lp.rolling(w, min_periods=mp).mean()
    xy = (x * lp).rolling(w, min_periods=mp).mean()
    xx = (x * x).rolling(w, min_periods=mp).mean()
    cov = xy - xm * ym
    var = xx - xm * xm
    return cov / var.replace(0, np.nan)


def _f01_slope_r2(close, w):
    lp = np.log(close.replace(0, np.nan))
    x = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    mp = max(2, w // 2)
    xm = x.rolling(w, min_periods=mp).mean()
    ym = lp.rolling(w, min_periods=mp).mean()
    xy = (x * lp).rolling(w, min_periods=mp).mean()
    xx = (x * x).rolling(w, min_periods=mp).mean()
    yy = (lp * lp).rolling(w, min_periods=mp).mean()
    cov = xy - xm * ym
    vx = xx - xm * xm
    vy = yy - ym * ym
    return (cov * cov) / (vx * vy).replace(0, np.nan)


def _f01_kama_er(close, w):
    # Kaufman efficiency ratio over window w: |net change| / sum|daily change|
    net = (close - close.shift(w)).abs()
    gross = close.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return net / gross.replace(0, np.nan)


def _f01_chan_pos(close, w):
    # position of price within the regression-implied channel, scaled by residual std
    lp = np.log(close.replace(0, np.nan))
    x = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    mp = max(3, w // 2)
    xm = x.rolling(w, min_periods=mp).mean()
    ym = lp.rolling(w, min_periods=mp).mean()
    xy = (x * lp).rolling(w, min_periods=mp).mean()
    xx = (x * x).rolling(w, min_periods=mp).mean()
    yy = (lp * lp).rolling(w, min_periods=mp).mean()
    cov = xy - xm * ym
    vx = (xx - xm * xm).replace(0, np.nan)
    vy = (yy - ym * ym)
    beta = cov / vx
    alpha = ym - beta * xm
    fitted = alpha + beta * x
    resid_var = (vy - beta * cov).clip(lower=0)
    resid_sd = np.sqrt(resid_var)
    return (lp - fitted) / resid_sd.replace(0, np.nan)


# ============================================================
# Kaufman efficiency ratio over 21d, signed by direction (short trend cleanliness)
def f01ts_f01_trend_structure_er_21d_base_v076_signal(closeadj):
    er = _f01_kama_er(closeadj, 21)
    b = er * np.sign(closeadj - closeadj.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Kaufman efficiency ratio over 63d, signed
def f01ts_f01_trend_structure_er_63d_base_v077_signal(closeadj):
    er = _f01_kama_er(closeadj, 63)
    b = er * np.sign(closeadj - closeadj.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Kaufman efficiency ratio over 126d, signed
def f01ts_f01_trend_structure_er_126d_base_v078_signal(closeadj):
    er = _f01_kama_er(closeadj, 126)
    b = er * np.sign(closeadj - closeadj.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Kaufman efficiency ratio over 252d, signed
def f01ts_f01_trend_structure_er_252d_base_v079_signal(closeadj):
    er = _f01_kama_er(closeadj, 252)
    b = er * np.sign(closeadj - closeadj.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression channel position over 63d (how far price is from its trendline, in resid-std)
def f01ts_f01_trend_structure_chanpos_63d_base_v080_signal(closeadj):
    b = _f01_chan_pos(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression channel position over 126d
def f01ts_f01_trend_structure_chanpos_126d_base_v081_signal(closeadj):
    b = _f01_chan_pos(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression channel position over 252d
def f01ts_f01_trend_structure_chanpos_252d_base_v082_signal(closeadj):
    b = _f01_chan_pos(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day fraction: share of last 63d closing in the period's direction, smoothed (continuous)
def f01ts_f01_trend_structure_trenddays_63d_base_v083_signal(closeadj):
    ret = closeadj.pct_change()
    netret = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    dirn = np.tanh(50.0 * netret)
    agree = (np.sign(ret) == np.sign(netret)).astype(float)
    frac = agree.ewm(span=42, min_periods=21).mean()
    b = (frac - 0.5) * dirn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day fraction over 126d, smoothed and direction-weighted (continuous)
def f01ts_f01_trend_structure_trenddays_126d_base_v084_signal(closeadj):
    ret = closeadj.pct_change()
    netret = np.log(closeadj.replace(0, np.nan) / closeadj.shift(126).replace(0, np.nan))
    dirn = np.tanh(40.0 * netret)
    agree = (np.sign(ret) == np.sign(netret)).astype(float)
    frac = agree.ewm(span=84, min_periods=42).mean()
    b = (frac - 0.5) * dirn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-day minus down-day count over 63d relative to the 252d SMA (directional pressure vs trend)
def f01ts_f01_trend_structure_updownbal_63d_base_v085_signal(closeadj):
    ma = _f01_sma(closeadj, 252)
    above = np.sign(closeadj - ma)
    b = above.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of price relative to the 252d MA (does price gain on its long anchor), 63d window
def f01ts_f01_trend_structure_relslope_252d_base_v086_signal(closeadj):
    rel = np.log(closeadj.replace(0, np.nan) / _f01_sma(closeadj, 252).replace(0, np.nan))
    b = _f01_slope(np.exp(rel), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d/21d EMA crossover (very short trend), normalized by price
def f01ts_f01_trend_structure_emaspr_5v21_base_v087_signal(closeadj):
    e1 = _f01_ema(closeadj, 5)
    e2 = _f01_ema(closeadj, 21)
    b = e1 / e2.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA distance from 126d EMA over 252d EMA (curvature of the EMA ribbon)
def f01ts_f01_trend_structure_emacurve_base_v088_signal(closeadj):
    e1 = _f01_ema(closeadj, 21)
    e2 = _f01_ema(closeadj, 126)
    e3 = _f01_ema(closeadj, 252)
    g_up = e1 / e2.replace(0, np.nan) - 1.0
    g_dn = e2 / e3.replace(0, np.nan) - 1.0
    b = g_up - g_dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MACD (12/26-style scaled to 21/42) histogram acceleration over a week
def f01ts_f01_trend_structure_macdaccel_base_v089_signal(closeadj):
    macd = _f01_ema(closeadj, 21) - _f01_ema(closeadj, 42)
    sig = macd.ewm(span=14, min_periods=7).mean()
    hist = (macd - sig) / closeadj.replace(0, np.nan)
    b = hist - hist.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance to 126d SMA in 126d-SMA-std units (channel-band breach depth)
def f01ts_f01_trend_structure_maband_126d_base_v090_signal(closeadj):
    ma = _f01_sma(closeadj, 126)
    sd = closeadj.rolling(126, min_periods=63).std()
    b = (closeadj - ma) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance to 252d SMA in 252d-SMA-std units
def f01ts_f01_trend_structure_maband_252d_base_v091_signal(closeadj):
    ma = _f01_sma(closeadj, 252)
    sd = closeadj.rolling(252, min_periods=126).std()
    b = (closeadj - ma) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# number of 21d-SMA crossings over 63d (trendiness; few crossings = strong trend) signed
def f01ts_f01_trend_structure_crossrate_21d_base_v092_signal(closeadj):
    d = _f01_pxma(closeadj, 21)
    cross = ((np.sign(d) != np.sign(d.shift(1))) & d.notna()).astype(float)
    rate = cross.rolling(63, min_periods=21).mean()
    b = -np.log1p(rate) * d.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 252d the 63d SMA stayed above the 252d SMA (golden-cross regime time)
def f01ts_f01_trend_structure_goldentime_base_v093_signal(closeadj):
    m1 = _f01_sma(closeadj, 63)
    m2 = _f01_sma(closeadj, 252)
    bull = (m1 > m2).astype(float)
    frac = bull.rolling(252, min_periods=126).mean()
    b = 2.0 * frac - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how stretched the 21d SMA is above the 252d SMA, in 63d-vol units of the gap
def f01ts_f01_trend_structure_stretchgap_base_v094_signal(closeadj):
    gap = _f01_sma(closeadj, 21) / _f01_sma(closeadj, 252).replace(0, np.nan) - 1.0
    sd = gap.rolling(63, min_periods=21).std()
    b = gap / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 21d SMA over a week (very short MA direction)
def f01ts_f01_trend_structure_maslope_21d_base_v095_signal(closeadj):
    ma = _f01_sma(closeadj, 21)
    b = ma / ma.shift(5).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of the 63d SMA (its slope now minus a quarter ago) -- MA curvature
def f01ts_f01_trend_structure_macurv_63d_base_v096_signal(closeadj):
    ma = _f01_sma(closeadj, 63)
    sl = ma / ma.shift(21).replace(0, np.nan) - 1.0
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression slope over 63d divided by regression slope over 252d (trend term-structure ratio)
def f01ts_f01_trend_structure_slopeshape_base_v097_signal(closeadj):
    s_s = _f01_slope(closeadj, 63)
    s_l = _f01_slope(closeadj, 252)
    b = np.tanh((s_s - s_l) / (s_l.abs() + 1e-4))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest above-21d-SMA run within 126d relative to window length (max persistence streak)
def f01ts_f01_trend_structure_maxrun_21d_base_v098_signal(closeadj):
    above = (closeadj > _f01_sma(closeadj, 21)).astype(float)

    def _maxrun(a):
        best = cur = 0
        for v in a:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return best / float(len(a))
    b = above.rolling(126, min_periods=63).apply(_maxrun, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# above/below 63d SMA run asymmetry: avg up-side run length minus avg down-side run length
def f01ts_f01_trend_structure_runasym_63d_base_v099_signal(closeadj):
    d = _f01_pxma(closeadj, 63)
    sign = np.sign(d)
    grp = (sign != sign.shift(1)).cumsum()
    run = sign.groupby(grp).cumcount() + 1
    signed_run = sign * run
    b = signed_run.rolling(126, min_periods=63).mean() / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend conviction: efficiency ratio (63d) times distance above 63d SMA (clean AND extended)
def f01ts_f01_trend_structure_conviction_63d_base_v100_signal(closeadj):
    er = _f01_kama_er(closeadj, 63)
    d = _f01_pxma(closeadj, 63)
    b = er * d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression R^2 spread: short-window trend clarity minus long-window (where the trend lives)
def f01ts_f01_trend_structure_r2spread_base_v101_signal(closeadj):
    r_s = _f01_slope_r2(closeadj, 63)
    r_l = _f01_slope_r2(closeadj, 252)
    b = r_s - r_l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price position within the 63d high-low channel relative to the 63d SMA (range-anchored trend)
def f01ts_f01_trend_structure_chanma_63d_base_v102_signal(closeadj):
    ma = _f01_sma(closeadj, 63)
    hi = _rmax(closeadj, 63)
    lo = _rmin(closeadj, 63)
    b = (closeadj - ma) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above the 252d SMA squashed by tanh and weighted by 252d R^2 (clean long uptrend)
def f01ts_f01_trend_structure_cleanuptrend_base_v103_signal(closeadj):
    d = _f01_pxma(closeadj, 252)
    r2 = _f01_slope_r2(closeadj, 252)
    b = np.tanh(8.0 * d) * r2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# the 63d EMA's own log-return slope over 21d (smoothed-price trend velocity)
def f01ts_f01_trend_structure_emavel_63d_base_v104_signal(closeadj):
    e = _f01_ema(closeadj, 63)
    b = np.log(e.replace(0, np.nan) / e.shift(21).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# the 252d EMA's velocity over a quarter (long smoothed trend velocity)
def f01ts_f01_trend_structure_emavel_252d_base_v105_signal(closeadj):
    e = _f01_ema(closeadj, 252)
    b = np.log(e.replace(0, np.nan) / e.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional MACD-line slope: is the 21/63 MACD line itself trending up (over 21d)
def f01ts_f01_trend_structure_macdslope_base_v106_signal(closeadj):
    macd = (_f01_ema(closeadj, 21) - _f01_ema(closeadj, 63)) / closeadj.replace(0, np.nan)
    b = macd - macd.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of 21/63/126/252 SMAs that are themselves rising (breadth of MA upturn)
def f01ts_f01_trend_structure_marising_base_v107_signal(closeadj):
    def _rising(w, lag):
        ma = _f01_sma(closeadj, w)
        return np.tanh(100.0 * (ma / ma.shift(lag).replace(0, np.nan) - 1.0))
    b = (_rising(21, 5) + _rising(63, 21) + _rising(126, 21) + _rising(252, 63)) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 504d SMA (very long anchor trend)
def f01ts_f01_trend_structure_pxma_504d_base_v108_signal(closeadj):
    b = _f01_pxma(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d/252d SMA spread (mid-vs-long golden cross), demeaned by its own 252d average
def f01ts_f01_trend_structure_maspr_126v252_base_v109_signal(closeadj):
    raw = _f01_sma(closeadj, 126) / _f01_sma(closeadj, 252).replace(0, np.nan) - 1.0
    b = raw - raw.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 21d SMA times distance above 252d SMA (joint short&long trend agreement)
def f01ts_f01_trend_structure_dualtrend_base_v110_signal(closeadj):
    d_s = _f01_pxma(closeadj, 21)
    d_l = _f01_pxma(closeadj, 252)
    b = np.sign(d_s * d_l) * np.sqrt((d_s * d_l).abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how far price has trended from where it crossed its 252d SMA (post-cross extension)
def f01ts_f01_trend_structure_postcross_252d_base_v111_signal(closeadj):
    ma = _f01_sma(closeadj, 252)
    above = (closeadj > ma).astype(float)
    cross = ((above != above.shift(1)) & above.notna()).astype(float)
    grp = cross.cumsum()
    base_px = closeadj.groupby(grp).transform("first")
    b = np.log(closeadj.replace(0, np.nan) / base_px.replace(0, np.nan)) * (2.0 * above - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression slope sign agreement across price, 63d-EMA, and 252d-SMA velocities (consensus)
def f01ts_f01_trend_structure_velconsensus_base_v112_signal(closeadj):
    v1 = np.tanh(60.0 * _f01_slope(closeadj, 21))
    v2 = np.tanh(60.0 * (np.log(_f01_ema(closeadj, 63).replace(0, np.nan)
                                / _f01_ema(closeadj, 63).shift(21).replace(0, np.nan))))
    ma = _f01_sma(closeadj, 252)
    v3 = np.tanh(60.0 * (ma / ma.shift(63).replace(0, np.nan) - 1.0))
    b = (v1 + v2 + v3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of the regression channel position over 63d (price diverging from trendline)
def f01ts_f01_trend_structure_chanaccel_63d_base_v113_signal(closeadj):
    cp = _f01_chan_pos(closeadj, 63)
    b = cp - cp.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest below-63d-SMA run within 252d (downtrend persistence depth)
def f01ts_f01_trend_structure_maxdownrun_63d_base_v114_signal(closeadj):
    below = (closeadj < _f01_sma(closeadj, 63)).astype(float)

    def _maxrun(a):
        best = cur = 0
        for v in a:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return best / float(len(a))
    b = below.rolling(252, min_periods=126).apply(_maxrun, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio momentum: change in 63d efficiency ratio over a month (trend forming)
def f01ts_f01_trend_structure_ermom_63d_base_v115_signal(closeadj):
    er = _f01_kama_er(closeadj, 63)
    b = er - er.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price distance above 63d SMA, normalized cross-sectionally over time by its 252d MAD
def f01ts_f01_trend_structure_pxmamad_63d_base_v116_signal(closeadj):
    d = _f01_pxma(closeadj, 63)
    med = d.rolling(252, min_periods=63).median()
    mad = (d - med).abs().rolling(252, min_periods=63).median()
    b = (d - med) / mad.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope-of-EMA-distance: regression slope of (price/63d-EMA - 1) over 63d (trend re-acceleration)
def f01ts_f01_trend_structure_emadistslope_base_v117_signal(closeadj):
    d = (closeadj / _f01_ema(closeadj, 63).replace(0, np.nan)) - 1.0
    b = _f01_slope(np.exp(d), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mid-trend lead: 63d SMA distance minus 126d SMA distance (mid trend leading the longer one)
def f01ts_f01_trend_structure_distlead_base_v118_signal(closeadj):
    d1 = _f01_pxma(closeadj, 63)
    d2 = _f01_pxma(closeadj, 126)
    b = d1 - d2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend persistence quality: 126d R^2 weighted by slope sign, ranked vs 252d history
def f01ts_f01_trend_structure_qualrank_126d_base_v119_signal(closeadj):
    q = _f01_slope_r2(closeadj, 126) * np.sign(_f01_slope(closeadj, 126))
    b = q.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how concentrated trend gains are: ratio of best 21d move to total 126d move (jumpiness)
def f01ts_f01_trend_structure_gainconc_base_v120_signal(closeadj):
    r21 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan))
    best = r21.rolling(126, min_periods=63).max()
    total = np.log(closeadj.replace(0, np.nan) / closeadj.shift(126).replace(0, np.nan))
    b = best / total.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger-on-MA: where price sits in the 63d SMA +/- band, change over a month
def f01ts_f01_trend_structure_bandmom_63d_base_v121_signal(closeadj):
    ma = _f01_sma(closeadj, 63)
    sd = closeadj.rolling(63, min_periods=21).std()
    pos = (closeadj - ma) / (2.0 * sd).replace(0, np.nan)
    b = pos - pos.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triple-EMA (TRIX-like) rate of change over 21d (smoothed trend momentum)
def f01ts_f01_trend_structure_trix_base_v122_signal(closeadj):
    e1 = _f01_ema(closeadj, 21)
    e2 = e1.ewm(span=21, min_periods=10).mean()
    e3 = e2.ewm(span=21, min_periods=10).mean()
    b = np.log(e3.replace(0, np.nan) / e3.shift(21).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# very-long trend acceleration: 252d slope minus 504d slope, ranked vs its own 504d history
def f01ts_f01_trend_structure_slopeterm_252v504_base_v123_signal(closeadj):
    term = _f01_slope(closeadj, 252) - _f01_slope(closeadj, 504)
    b = term.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 252d SMA persistence-weighted by time spent above it (durable leadership)
def f01ts_f01_trend_structure_durlead_252d_base_v124_signal(closeadj):
    d = _f01_pxma(closeadj, 252)
    above_frac = (d > 0).astype(float).rolling(126, min_periods=63).mean()
    b = d * above_frac
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression channel position dispersion: std of 63d channel position over the last 63d
def f01ts_f01_trend_structure_chanvol_63d_base_v125_signal(closeadj):
    cp = _f01_chan_pos(closeadj, 63)
    b = cp.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# does the short trend agree with the long trend in slope magnitude (alignment ratio, bounded)
def f01ts_f01_trend_structure_slopealign_base_v126_signal(closeadj):
    s_s = _f01_slope(closeadj, 21)
    s_l = _f01_slope(closeadj, 252)
    b = np.tanh(150.0 * s_s) * np.tanh(150.0 * s_l)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d/63d SMA cross ratio (fast pulse vs quarter trend)
def f01ts_f01_trend_structure_maspr_5v63_base_v127_signal(closeadj):
    b = _f01_sma(closeadj, 5) / _f01_sma(closeadj, 63).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how long since the 21d SMA last crossed the 63d SMA (trend regime age), signed by side
def f01ts_f01_trend_structure_crossage_base_v128_signal(closeadj):
    m1 = _f01_sma(closeadj, 21)
    m2 = _f01_sma(closeadj, 63)
    bull = (m1 > m2).astype(float)
    cross = ((bull != bull.shift(1)) & bull.notna()).astype(float)
    grp = cross.cumsum()
    age = bull.groupby(grp).cumcount().astype(float)
    b = np.log1p(age) * (2.0 * bull - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 126d EMA z-scored vs its own 252d history (mid trend extension extremity)
def f01ts_f01_trend_structure_pxemaz_126d_base_v129_signal(closeadj):
    d = (closeadj / _f01_ema(closeadj, 126).replace(0, np.nan)) - 1.0
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend smoothness penalty: signed 252d efficiency ratio minus signed 63d efficiency ratio
def f01ts_f01_trend_structure_erterm_base_v130_signal(closeadj):
    er_l = _f01_kama_er(closeadj, 252) * np.sign(closeadj - closeadj.shift(252))
    er_s = _f01_kama_er(closeadj, 63) * np.sign(closeadj - closeadj.shift(63))
    b = er_l - er_s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of 63d where price > 21d SMA > 63d SMA (perfect short-stack time)
def f01ts_f01_trend_structure_shortstacktime_base_v131_signal(closeadj):
    m1 = _f01_sma(closeadj, 21)
    m2 = _f01_sma(closeadj, 63)
    perfect = ((closeadj > m1) & (m1 > m2)).astype(float)
    frac = perfect.rolling(63, min_periods=21).mean()
    deep = _f01_pxma(closeadj, 63).clip(lower=0).rolling(21, min_periods=10).mean()
    b = frac + 5.0 * deep
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression slope measured on the 21d-EMA-smoothed price over 126d (de-noised mid trend)
def f01ts_f01_trend_structure_smoothslope_126d_base_v132_signal(closeadj):
    sm = _f01_ema(closeadj, 21)
    b = _f01_slope(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price acceleration vs its 63d SMA: 2nd difference of the gap over 21d steps
def f01ts_f01_trend_structure_gapcurve_63d_base_v133_signal(closeadj):
    d = _f01_pxma(closeadj, 63)
    b = d - 2.0 * d.shift(21) + d.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of last 252d in a confirmed uptrend (price>63d SMA AND 63d SMA rising)
def f01ts_f01_trend_structure_uptrendtime_base_v134_signal(closeadj):
    ma = _f01_sma(closeadj, 63)
    rising = (ma > ma.shift(21)).astype(float)
    above = (closeadj > ma).astype(float)
    conf = (rising * above)
    b = conf.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# the 63d slope expressed in annualized-return terms, tanh-bounded
def f01ts_f01_trend_structure_slopeann_63d_base_v135_signal(closeadj):
    sl = _f01_slope(closeadj, 63)
    b = np.tanh(0.5 * (sl * 252.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance between price and the midpoint of its 126d regression channel (above/below trendline)
def f01ts_f01_trend_structure_trendlinegap_126d_base_v136_signal(closeadj):
    cp = _f01_chan_pos(closeadj, 126)
    b = np.tanh(cp) * _f01_slope_r2(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-ribbon width trend: is the 21..252 SMA fan widening or contracting (over a quarter)
def f01ts_f01_trend_structure_fantrend_base_v137_signal(closeadj):
    m1 = _f01_sma(closeadj, 21)
    m4 = _f01_sma(closeadj, 252)
    width = (m1 - m4).abs() / closeadj.replace(0, np.nan)
    b = width - width.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed efficiency ratio (126d) times R^2 (126d) -- doubly-confirmed clean trend
def f01ts_f01_trend_structure_doubleclean_126d_base_v138_signal(closeadj):
    er = _f01_kama_er(closeadj, 126) * np.sign(closeadj - closeadj.shift(126))
    r2 = _f01_slope_r2(closeadj, 126)
    b = er * r2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA slope minus 252d EMA slope (short vs long smoothed-trend velocity spread)
def f01ts_f01_trend_structure_emavelterm_base_v139_signal(closeadj):
    e_s = _f01_ema(closeadj, 21)
    e_l = _f01_ema(closeadj, 252)
    v_s = np.log(e_s.replace(0, np.nan) / e_s.shift(21).replace(0, np.nan))
    v_l = np.log(e_l.replace(0, np.nan) / e_l.shift(63).replace(0, np.nan))
    b = v_s - v_l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# above-trendline time weighted by channel-position magnitude (durable above-trend pressure)
def f01ts_f01_trend_structure_abovetrendtime_base_v140_signal(closeadj):
    cp = _f01_chan_pos(closeadj, 63)
    pos = (cp > 0).astype(float)
    frac = pos.rolling(126, min_periods=63).mean() - 0.5
    b = frac + 0.3 * cp.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume-confirmed trend: 63d slope sign times z-scored dollar-volume trend
def f01ts_f01_trend_structure_trenddvol_base_v141_signal(closeadj, volume):
    sl = np.tanh(150.0 * _f01_slope(closeadj, 63))
    dvol = closeadj * volume
    dvol_slope = _z(dvol.rolling(21, min_periods=10).mean(), 126)
    b = sl * dvol_slope
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend exhaustion: distance above 252d SMA minus its 63d-ago value, when far above (fade)
def f01ts_f01_trend_structure_exhaust_252d_base_v142_signal(closeadj):
    d = _f01_pxma(closeadj, 252)
    stretched = d.clip(lower=0)
    b = (d - d.shift(63)) * stretched
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how many distinct MAs (21/63/126/252) the price has crossed in the last 21d (regime churn)
def f01ts_f01_trend_structure_machurn_base_v143_signal(closeadj):
    def _flips(w):
        d = _f01_pxma(closeadj, w)
        return ((np.sign(d) != np.sign(d.shift(1))) & d.notna()).astype(float).rolling(21, min_periods=10).sum()
    churn = _flips(21) + _flips(63) + _flips(126) + _flips(252)
    b = -churn + 10.0 * _f01_pxma(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log distance from price to the 252d EMA, smoothed over a month (persistent long extension)
def f01ts_f01_trend_structure_emadistsm_252d_base_v144_signal(closeadj):
    d = np.log(closeadj.replace(0, np.nan) / _f01_ema(closeadj, 252).replace(0, np.nan))
    b = d.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression slope t-like ratio on 21d-smoothed price over 252d (clean long-trend significance)
def f01ts_f01_trend_structure_smoothtrend_252d_base_v145_signal(closeadj):
    sm = _f01_ema(closeadj, 21)
    sl = _f01_slope(sm, 252)
    r2 = _f01_slope_r2(sm, 252)
    b = sl * np.sqrt(r2.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how decisively price re-anchored above the 126d SMA after dipping (recovery-above-MA depth)
def f01ts_f01_trend_structure_reclaimma_126d_base_v146_signal(closeadj):
    ma = _f01_sma(closeadj, 126)
    below = (closeadj < ma).astype(float)
    recent_below = below.rolling(63, min_periods=21).mean()
    d = _f01_pxma(closeadj, 126)
    b = d.clip(lower=0) * recent_below
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend coherence: 1 minus normalized dispersion of price/SMA distances across 4 windows
def f01ts_f01_trend_structure_coherence_base_v147_signal(closeadj):
    d1 = _f01_pxma(closeadj, 21)
    d2 = _f01_pxma(closeadj, 63)
    d3 = _f01_pxma(closeadj, 126)
    d4 = _f01_pxma(closeadj, 252)
    stacked = pd.concat([d1, d2, d3, d4], axis=1)
    disp = stacked.std(axis=1)
    mag = stacked.mean(axis=1).abs()
    b = np.sign(stacked.mean(axis=1)) * mag / (mag + disp).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d regression slope of the dollar-volume-weighted price proxy vs raw slope (trend confirmation)
def f01ts_f01_trend_structure_vwtrend_base_v148_signal(closeadj, volume):
    dvol = closeadj * volume
    vw = (dvol).rolling(21, min_periods=10).sum() / volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = _f01_slope(vw, 63) - _f01_slope(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of the 63v252 golden-cross gap (is the long cross widening faster), 2nd diff
def f01ts_f01_trend_structure_goldenaccel_base_v149_signal(closeadj):
    gap = _f01_sma(closeadj, 63) / _f01_sma(closeadj, 252).replace(0, np.nan) - 1.0
    b = gap - 2.0 * gap.shift(21) + gap.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite trend score: tanh of (price-vs-252d-SMA) + sign-of-slope*R^2 over 126d (blend)
def f01ts_f01_trend_structure_composite_base_v150_signal(closeadj):
    lvl = np.tanh(6.0 * _f01_pxma(closeadj, 252))
    qual = np.sign(_f01_slope(closeadj, 126)) * _f01_slope_r2(closeadj, 126)
    b = 0.5 * lvl + 0.5 * qual
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01ts_f01_trend_structure_er_21d_base_v076_signal,
    f01ts_f01_trend_structure_er_63d_base_v077_signal,
    f01ts_f01_trend_structure_er_126d_base_v078_signal,
    f01ts_f01_trend_structure_er_252d_base_v079_signal,
    f01ts_f01_trend_structure_chanpos_63d_base_v080_signal,
    f01ts_f01_trend_structure_chanpos_126d_base_v081_signal,
    f01ts_f01_trend_structure_chanpos_252d_base_v082_signal,
    f01ts_f01_trend_structure_trenddays_63d_base_v083_signal,
    f01ts_f01_trend_structure_trenddays_126d_base_v084_signal,
    f01ts_f01_trend_structure_updownbal_63d_base_v085_signal,
    f01ts_f01_trend_structure_relslope_252d_base_v086_signal,
    f01ts_f01_trend_structure_emaspr_5v21_base_v087_signal,
    f01ts_f01_trend_structure_emacurve_base_v088_signal,
    f01ts_f01_trend_structure_macdaccel_base_v089_signal,
    f01ts_f01_trend_structure_maband_126d_base_v090_signal,
    f01ts_f01_trend_structure_maband_252d_base_v091_signal,
    f01ts_f01_trend_structure_crossrate_21d_base_v092_signal,
    f01ts_f01_trend_structure_goldentime_base_v093_signal,
    f01ts_f01_trend_structure_stretchgap_base_v094_signal,
    f01ts_f01_trend_structure_maslope_21d_base_v095_signal,
    f01ts_f01_trend_structure_macurv_63d_base_v096_signal,
    f01ts_f01_trend_structure_slopeshape_base_v097_signal,
    f01ts_f01_trend_structure_maxrun_21d_base_v098_signal,
    f01ts_f01_trend_structure_runasym_63d_base_v099_signal,
    f01ts_f01_trend_structure_conviction_63d_base_v100_signal,
    f01ts_f01_trend_structure_r2spread_base_v101_signal,
    f01ts_f01_trend_structure_chanma_63d_base_v102_signal,
    f01ts_f01_trend_structure_cleanuptrend_base_v103_signal,
    f01ts_f01_trend_structure_emavel_63d_base_v104_signal,
    f01ts_f01_trend_structure_emavel_252d_base_v105_signal,
    f01ts_f01_trend_structure_macdslope_base_v106_signal,
    f01ts_f01_trend_structure_marising_base_v107_signal,
    f01ts_f01_trend_structure_pxma_504d_base_v108_signal,
    f01ts_f01_trend_structure_maspr_126v252_base_v109_signal,
    f01ts_f01_trend_structure_dualtrend_base_v110_signal,
    f01ts_f01_trend_structure_postcross_252d_base_v111_signal,
    f01ts_f01_trend_structure_velconsensus_base_v112_signal,
    f01ts_f01_trend_structure_chanaccel_63d_base_v113_signal,
    f01ts_f01_trend_structure_maxdownrun_63d_base_v114_signal,
    f01ts_f01_trend_structure_ermom_63d_base_v115_signal,
    f01ts_f01_trend_structure_pxmamad_63d_base_v116_signal,
    f01ts_f01_trend_structure_emadistslope_base_v117_signal,
    f01ts_f01_trend_structure_distlead_base_v118_signal,
    f01ts_f01_trend_structure_qualrank_126d_base_v119_signal,
    f01ts_f01_trend_structure_gainconc_base_v120_signal,
    f01ts_f01_trend_structure_bandmom_63d_base_v121_signal,
    f01ts_f01_trend_structure_trix_base_v122_signal,
    f01ts_f01_trend_structure_slopeterm_252v504_base_v123_signal,
    f01ts_f01_trend_structure_durlead_252d_base_v124_signal,
    f01ts_f01_trend_structure_chanvol_63d_base_v125_signal,
    f01ts_f01_trend_structure_slopealign_base_v126_signal,
    f01ts_f01_trend_structure_maspr_5v63_base_v127_signal,
    f01ts_f01_trend_structure_crossage_base_v128_signal,
    f01ts_f01_trend_structure_pxemaz_126d_base_v129_signal,
    f01ts_f01_trend_structure_erterm_base_v130_signal,
    f01ts_f01_trend_structure_shortstacktime_base_v131_signal,
    f01ts_f01_trend_structure_smoothslope_126d_base_v132_signal,
    f01ts_f01_trend_structure_gapcurve_63d_base_v133_signal,
    f01ts_f01_trend_structure_uptrendtime_base_v134_signal,
    f01ts_f01_trend_structure_slopeann_63d_base_v135_signal,
    f01ts_f01_trend_structure_trendlinegap_126d_base_v136_signal,
    f01ts_f01_trend_structure_fantrend_base_v137_signal,
    f01ts_f01_trend_structure_doubleclean_126d_base_v138_signal,
    f01ts_f01_trend_structure_emavelterm_base_v139_signal,
    f01ts_f01_trend_structure_abovetrendtime_base_v140_signal,
    f01ts_f01_trend_structure_trenddvol_base_v141_signal,
    f01ts_f01_trend_structure_exhaust_252d_base_v142_signal,
    f01ts_f01_trend_structure_machurn_base_v143_signal,
    f01ts_f01_trend_structure_emadistsm_252d_base_v144_signal,
    f01ts_f01_trend_structure_smoothtrend_252d_base_v145_signal,
    f01ts_f01_trend_structure_reclaimma_126d_base_v146_signal,
    f01ts_f01_trend_structure_coherence_base_v147_signal,
    f01ts_f01_trend_structure_vwtrend_base_v148_signal,
    f01ts_f01_trend_structure_goldenaccel_base_v149_signal,
    f01ts_f01_trend_structure_composite_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_TREND_STRUCTURE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

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
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f01_trend_structure_base_076_150_claude: %d features pass" % n_features)
