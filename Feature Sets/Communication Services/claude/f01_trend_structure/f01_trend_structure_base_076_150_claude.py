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


# ===== folder domain primitives =====
def _f01_ma(close, w):
    return close.rolling(w, min_periods=max(1, w // 2)).mean()


def _f01_ema(close, span):
    return close.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _f01_pxvma(close, w):
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return close / ma.replace(0, np.nan) - 1.0


def _f01_maslope(close, w, k):
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.log(ma.replace(0, np.nan) / ma.shift(k).replace(0, np.nan)) / float(k)


def _f01_maspread(close, ws, wl):
    s = close.rolling(ws, min_periods=max(1, ws // 2)).mean()
    l = close.rolling(wl, min_periods=max(1, wl // 2)).mean()
    return s / l.replace(0, np.nan) - 1.0


def _f01_stack3(close):
    m21 = close.rolling(21, min_periods=10).mean()
    m63 = close.rolling(63, min_periods=31).mean()
    m126 = close.rolling(126, min_periods=63).mean()
    m252 = close.rolling(252, min_periods=126).mean()
    s = (m21 > m63).astype(float) + (m63 > m126).astype(float) + (m126 > m252).astype(float)
    return s - 1.5


def _f01_efficiency(close, w):
    net = (close - close.shift(w)).abs()
    path = close.diff().abs().rolling(w, min_periods=max(1, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _f01_tstat(close, w):
    lp = np.log(close.replace(0, np.nan))

    def _t(a):
        m = len(a)
        if np.any(np.isnan(a)):
            return np.nan
        x = np.arange(m, dtype=float)
        xm = x.mean()
        ym = a.mean()
        sxx = ((x - xm) ** 2).sum()
        if sxx == 0:
            return np.nan
        b = ((x - xm) * (a - ym)).sum() / sxx
        resid = a - (ym + b * (x - xm))
        s2 = (resid ** 2).sum() / max(1, (m - 2))
        se = np.sqrt(s2 / sxx)
        if se == 0:
            return np.nan
        return b / se

    return lp.rolling(w, min_periods=max(1, w // 2)).apply(_t, raw=True)


def _f01_abovefrac(close, w, lw):
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    above = (close > ma).astype(float)
    return above.rolling(lw, min_periods=max(1, lw // 2)).mean()


# ============================================================
# weekly fast MA: price vs 5d MA (short-term trend bias)
def f01ts_f01_trend_structure_pxvma_5d_base_v076_signal(closeadj):
    b = _f01_pxvma(closeadj, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 42d MA (two-month trend)
def f01ts_f01_trend_structure_pxvma_42d_base_v077_signal(closeadj):
    b = _f01_pxvma(closeadj, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 189d MA (three-quarter trend)
def f01ts_f01_trend_structure_pxvma_189d_base_v078_signal(closeadj):
    b = _f01_pxvma(closeadj, 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 504d MA (two-year trend extension)
def f01ts_f01_trend_structure_pxvma_504d_base_v079_signal(closeadj):
    b = _f01_pxvma(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-MA(42d) z-scored vs own 126d history
def f01ts_f01_trend_structure_distz_42d_base_v080_signal(closeadj):
    d = _f01_pxvma(closeadj, 42)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-MA(189d) z-scored vs own 252d history
def f01ts_f01_trend_structure_distz_189d_base_v081_signal(closeadj):
    d = _f01_pxvma(closeadj, 189)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-MA(504d) z-scored vs own 504d history (deep long stretch)
def f01ts_f01_trend_structure_distz_504d_base_v082_signal(closeadj):
    d = _f01_pxvma(closeadj, 504)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5/21 MA spread (very-fast cross)
def f01ts_f01_trend_structure_maspread_5v21_base_v083_signal(closeadj):
    b = _f01_maspread(closeadj, 5, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 42/126 MA spread (medium cross)
def f01ts_f01_trend_structure_maspread_42v126_base_v084_signal(closeadj):
    b = _f01_maspread(closeadj, 42, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63/189 MA spread
def f01ts_f01_trend_structure_maspread_63v189_base_v085_signal(closeadj):
    b = _f01_maspread(closeadj, 63, 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126/504 MA spread (long-trend regime)
def f01ts_f01_trend_structure_maspread_126v504_base_v086_signal(closeadj):
    b = _f01_maspread(closeadj, 126, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d MA log-slope over 5d (very-short trend direction)
def f01ts_f01_trend_structure_maslope_5d_base_v087_signal(closeadj):
    b = _f01_maslope(closeadj, 5, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 42d MA log-slope over 21d
def f01ts_f01_trend_structure_maslope_42d_base_v088_signal(closeadj):
    b = _f01_maslope(closeadj, 42, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 189d MA log-slope over 63d
def f01ts_f01_trend_structure_maslope_189d_base_v089_signal(closeadj):
    b = _f01_maslope(closeadj, 189, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d MA log-slope over 126d (very-long trend direction)
def f01ts_f01_trend_structure_maslope_504d_base_v090_signal(closeadj):
    b = _f01_maslope(closeadj, 504, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5-MA ribbon stacking with 5/21/63/126/252 (extended alignment, magnitude-weighted)
def f01ts_f01_trend_structure_stack5_base_v091_signal(closeadj):
    m5 = _f01_ma(closeadj, 5)
    m21 = _f01_ma(closeadj, 21)
    m63 = _f01_ma(closeadj, 63)
    m126 = _f01_ma(closeadj, 126)
    m252 = _f01_ma(closeadj, 252)
    sc = ((m5 > m21).astype(float) + (m21 > m63).astype(float)
          + (m63 > m126).astype(float) + (m126 > m252).astype(float)) - 2.0
    width = (m5 - m252) / m252.replace(0, np.nan)
    b = sc + 8.0 * width
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope-weighted stack: stack3 score times mean 21/63/126 slope magnitude (powered alignment)
def f01ts_f01_trend_structure_stackslope_base_v092_signal(closeadj):
    st = _f01_stack3(closeadj)
    sl = (_f01_maslope(closeadj, 21, 21) + _f01_maslope(closeadj, 63, 21)
          + _f01_maslope(closeadj, 126, 21)) / 3.0
    b = st * (1.0 + 40.0 * sl.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 252d price above 504d MA (very-long persistence)
def f01ts_f01_trend_structure_abovefrac_504d_base_v093_signal(closeadj):
    b = _f01_abovefrac(closeadj, 504, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 42d price above 42d MA (fast persistence)
def f01ts_f01_trend_structure_abovefrac_42d_base_v094_signal(closeadj):
    b = _f01_abovefrac(closeadj, 42, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend efficiency over 21d (Kaufman ratio, short)
def f01ts_f01_trend_structure_efficiency_21d_base_v095_signal(closeadj):
    b = _f01_efficiency(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed trend efficiency over 252d (long directional cleanliness)
def f01ts_f01_trend_structure_signeff_252d_base_v096_signal(closeadj):
    net = closeadj - closeadj.shift(252)
    path = closeadj.diff().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend t-stat over 42d (short regression strength)
def f01ts_f01_trend_structure_tstat_42d_base_v097_signal(closeadj):
    b = _f01_tstat(closeadj, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend t-stat over 189d
def f01ts_f01_trend_structure_tstat_189d_base_v098_signal(closeadj):
    b = _f01_tstat(closeadj, 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-direction persistence: net up-fraction of 21d MA over a month
def f01ts_f01_trend_structure_dirpersist_21d_base_v099_signal(closeadj):
    ma = _f01_ma(closeadj, 21)
    up = np.sign(ma.diff())
    b = up.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MA direction-flip count over a year (long-trend reversal frequency)
def f01ts_f01_trend_structure_dirpersist_252d_base_v100_signal(closeadj):
    ma = _f01_ma(closeadj, 252)
    sign = np.sign(ma.diff())
    flip = (sign != sign.shift(1)).astype(float)
    cnt = flip.rolling(252, min_periods=126).sum()
    mag = _f01_maslope(closeadj, 252, 21).abs().rolling(252, min_periods=126).mean()
    b = cnt - 500.0 * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 42/126 spread z-scored vs own 252d history (regime-relative medium cross)
def f01ts_f01_trend_structure_maspreadz_42v126_base_v101_signal(closeadj):
    sp = _f01_maspread(closeadj, 42, 126)
    b = _z(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126/504 spread z-scored vs own 504d history (regime-relative long cross)
def f01ts_f01_trend_structure_maspreadz_126v504_base_v102_signal(closeadj):
    sp = _f01_maspread(closeadj, 126, 504)
    b = _z(sp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how stretched price is above 126d MA, percentile-ranked vs own 252d history
def f01ts_f01_trend_structure_pxvmarank_63d_base_v103_signal(closeadj):
    d = _f01_pxvma(closeadj, 63)
    b = d.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-vs-MA(252d) percentile-ranked vs own 1260d history (long-trend extremity)
def f01ts_f01_trend_structure_pxvmarank_252d_base_v104_signal(closeadj):
    d = _f01_pxvma(closeadj, 252)
    b = d.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA convexity: 42d MA second difference (is the medium MA accelerating?)
def f01ts_f01_trend_structure_maconvex_42d_base_v105_signal(closeadj):
    ma = _f01_ma(closeadj, 42)
    sl = np.log(ma.replace(0, np.nan) / ma.shift(21).replace(0, np.nan))
    b = sl - sl.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA convexity of 252d MA over a quarter (long-trend bending)
def f01ts_f01_trend_structure_maconvex_252d_base_v106_signal(closeadj):
    ma = _f01_ma(closeadj, 252)
    sl = np.log(ma.replace(0, np.nan) / ma.shift(63).replace(0, np.nan))
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# golden-cross state persistence for 42/189 (medium-trend conviction)
def f01ts_f01_trend_structure_goldenpersist_42v189_base_v107_signal(closeadj):
    s = _f01_ma(closeadj, 42)
    l = _f01_ma(closeadj, 189)
    state = (s > l).astype(float)
    b = state.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed 63v252 MA spread (bounded long-cross state)
def f01ts_f01_trend_structure_spreadtanh_63v252_base_v108_signal(closeadj):
    sp = _f01_maspread(closeadj, 63, 252)
    b = np.tanh(25.0 * sp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-slope dispersion across 5/21/63/126/252 (slope fan divergence)
def f01ts_f01_trend_structure_slopedisp5_base_v109_signal(closeadj):
    s1 = _f01_maslope(closeadj, 5, 5)
    s2 = _f01_maslope(closeadj, 21, 21)
    s3 = _f01_maslope(closeadj, 63, 21)
    s4 = _f01_maslope(closeadj, 126, 21)
    s5 = _f01_maslope(closeadj, 252, 21)
    b = pd.concat([s1, s2, s3, s4, s5], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inter-MA fan dispersion of the MAs themselves (excludes price level): 5/42/189/504 ordering spread
def f01ts_f01_trend_structure_madisp2_base_v110_signal(closeadj):
    m1 = _f01_ma(closeadj, 5)
    m2 = _f01_ma(closeadj, 42)
    m3 = _f01_ma(closeadj, 189)
    base = m2.replace(0, np.nan)
    r1 = m1 / base
    r3 = m3 / base
    r4 = _f01_ma(closeadj, 504) / base
    disp = pd.concat([r1, r3, r4], axis=1).std(axis=1)
    b = disp - disp.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ribbon compression for 5/42/189/504 scaled by price (alternate squeeze)
def f01ts_f01_trend_structure_ribboncomp2_base_v111_signal(closeadj):
    m1 = _f01_ma(closeadj, 5)
    m2 = _f01_ma(closeadj, 42)
    m3 = _f01_ma(closeadj, 189)
    m4 = _f01_ma(closeadj, 504)
    stacked = pd.concat([m1, m2, m3, m4], axis=1)
    b = (stacked.max(axis=1) - stacked.min(axis=1)) / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend acceleration: 21d return minus prior 21d return (short accel-as-level)
def f01ts_f01_trend_structure_accel_21d_base_v112_signal(closeadj):
    r_now = closeadj / closeadj.shift(21).replace(0, np.nan) - 1.0
    r_prev = closeadj.shift(21) / closeadj.shift(42).replace(0, np.nan) - 1.0
    b = r_now - r_prev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend acceleration: 126d return minus prior 126d return (long accel-as-level)
def f01ts_f01_trend_structure_accel_126d_base_v113_signal(closeadj):
    r_now = closeadj / closeadj.shift(126).replace(0, np.nan) - 1.0
    r_prev = closeadj.shift(126) / closeadj.shift(252).replace(0, np.nan) - 1.0
    b = r_now - r_prev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-MA(42d) mean-reversion vs its 126d average
def f01ts_f01_trend_structure_distrev_42d_base_v114_signal(closeadj):
    d = _f01_pxvma(closeadj, 42)
    b = d - d.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-MA(126d) mean-reversion vs its 252d average
def f01ts_f01_trend_structure_distrev_126d_base_v115_signal(closeadj):
    d = _f01_pxvma(closeadj, 126)
    b = d - d.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# whipsaw count for 42/126 MA crosses over the last 252d (medium choppiness)
def f01ts_f01_trend_structure_whipsaw_42v126_base_v116_signal(closeadj):
    m1 = _f01_ma(closeadj, 42)
    m2 = _f01_ma(closeadj, 126)
    state = np.sign(m1 - m2)
    flip = (state != state.shift(1)).astype(float)
    cnt = flip.rolling(252, min_periods=126).sum()
    eff = _f01_efficiency(closeadj, 252)
    b = cnt * (1.0 - eff)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# above-all-MAs flag persistence using 5/42/189/504 over 126d
def f01ts_f01_trend_structure_aboveall2_base_v117_signal(closeadj):
    m1 = _f01_ma(closeadj, 5)
    m2 = _f01_ma(closeadj, 42)
    m3 = _f01_ma(closeadj, 189)
    m4 = _f01_ma(closeadj, 504)
    flag = ((closeadj > m1) & (closeadj > m2) & (closeadj > m3) & (closeadj > m4)).astype(float)
    b = flag.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest streak (last 126d) price held above 42d MA, normalized
def f01ts_f01_trend_structure_maxabove_42d_base_v118_signal(closeadj):
    ma = _f01_ma(closeadj, 42)
    above = (closeadj > ma).astype(float)

    def _maxrun(a):
        best = 0
        cur = 0
        for v in a:
            if v == 1.0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return best / float(len(a))

    b = above.rolling(126, min_periods=63).apply(_maxrun, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-quality via R^2 of 252d log-price regression, signed by direction
def f01ts_f01_trend_structure_r2dir_252d_base_v119_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _r2(a):
        m = len(a)
        if np.any(np.isnan(a)):
            return np.nan
        x = np.arange(m, dtype=float)
        xm = x.mean()
        ym = a.mean()
        sxx = ((x - xm) ** 2).sum()
        syy = ((a - ym) ** 2).sum()
        if sxx == 0 or syy == 0:
            return np.nan
        sxy = ((x - xm) * (a - ym)).sum()
        return (sxy * sxy) / (sxx * syy)

    r2 = lp.rolling(252, min_periods=126).apply(_r2, raw=True)
    dirn = np.sign(_f01_maslope(closeadj, 252, 21))
    b = r2 * dirn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope sign-magnitude of 252d MA (compressed long direction)
def f01ts_f01_trend_structure_slopesignmag_252d_base_v120_signal(closeadj):
    sl = _f01_maslope(closeadj, 252, 63)
    b = np.sign(sl) * (sl.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pullback-in-uptrend at 63d MA while 126d MA rising (deeper healthy dip)
def f01ts_f01_trend_structure_pullback_63d_base_v121_signal(closeadj):
    d = _f01_pxvma(closeadj, 63)
    up = (_f01_maslope(closeadj, 126, 21) > 0).astype(float)
    b = (-d).clip(lower=0) * up
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# thrust-in-downtrend: upside stretch above 63d MA while 126d MA falling (bear rally)
def f01ts_f01_trend_structure_thrust_63d_base_v122_signal(closeadj):
    d = _f01_pxvma(closeadj, 63)
    dn = (_f01_maslope(closeadj, 126, 21) < 0).astype(float)
    b = d.clip(lower=0) * dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend age: signed run length of 42/189 cross state, normalized (medium maturity)
def f01ts_f01_trend_structure_trendage_42v189_base_v123_signal(closeadj):
    s = _f01_ma(closeadj, 42)
    l = _f01_ma(closeadj, 189)
    state = np.sign(s - l)

    def _run(a):
        last = a[-1]
        if last == 0 or np.isnan(last):
            return 0.0
        c = 0
        for v in a[::-1]:
            if v == last:
                c += 1
            else:
                break
        return last * c

    r = state.rolling(189, min_periods=63).apply(_run, raw=True)
    b = r / 189.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope agreement across 5/42/189 MAs, magnitude-weighted (multi-horizon coherence)
def f01ts_f01_trend_structure_slopeagree2_base_v124_signal(closeadj):
    sl1 = _f01_maslope(closeadj, 5, 5)
    sl2 = _f01_maslope(closeadj, 42, 21)
    sl3 = _f01_maslope(closeadj, 189, 21)
    vote = (np.sign(sl1) + np.sign(sl2) + np.sign(sl3)) / 3.0
    mag = (sl1.abs() + sl2.abs() + sl3.abs()) / 3.0
    b = vote * (1.0 + 30.0 * mag)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-MA(63d) interacted with stack5 (stretched and broadly aligned)
def f01ts_f01_trend_structure_distzstack5_base_v125_signal(closeadj):
    dz = _z(_f01_pxvma(closeadj, 63), 252)
    m5 = _f01_ma(closeadj, 5)
    m252 = _f01_ma(closeadj, 252)
    align = np.tanh(20.0 * (m5 / m252.replace(0, np.nan) - 1.0))
    b = dz * align
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite long-trend score: blend pxvma252, maslope252-sign, abovefrac252
def f01ts_f01_trend_structure_composite_long_base_v126_signal(closeadj):
    a = np.tanh(8.0 * _f01_pxvma(closeadj, 252))
    b2 = np.tanh(200.0 * _f01_maslope(closeadj, 252, 63))
    c = 2.0 * (_f01_abovefrac(closeadj, 252, 252) - 0.5)
    b = (a + b2 + c) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change of price-vs-MA(126d) (long trend regime shift)
def f01ts_f01_trend_structure_pxvmayoy_126d_base_v127_signal(closeadj):
    d = _f01_pxvma(closeadj, 126)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ribbon order entropy: how scrambled the 5/21/63/126/252 ordering is (trend chaos)
def f01ts_f01_trend_structure_ribbonentropy_base_v128_signal(closeadj):
    m5 = _f01_ma(closeadj, 5)
    m21 = _f01_ma(closeadj, 21)
    m63 = _f01_ma(closeadj, 63)
    m126 = _f01_ma(closeadj, 126)
    m252 = _f01_ma(closeadj, 252)
    inv = ((m5 < m21).astype(float) + (m21 < m63).astype(float)
           + (m63 < m126).astype(float) + (m126 < m252).astype(float))
    disp = pd.concat([m5 / closeadj, m21 / closeadj, m63 / closeadj,
                      m126 / closeadj, m252 / closeadj], axis=1).std(axis=1)
    b = inv + 5.0 * disp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MACD-style: 12-26 EMA spread normalized by price (classic trend oscillator)
def f01ts_f01_trend_structure_macd_base_v129_signal(closeadj):
    e1 = _f01_ema(closeadj, 12)
    e2 = _f01_ema(closeadj, 26)
    b = (e1 - e2) / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MACD histogram: MACD minus its 9-EMA signal line (trend momentum shift)
def f01ts_f01_trend_structure_macdhist_base_v130_signal(closeadj):
    e1 = _f01_ema(closeadj, 12)
    e2 = _f01_ema(closeadj, 26)
    macd = (e1 - e2) / closeadj.replace(0, np.nan)
    sig = macd.ewm(span=9, min_periods=5).mean()
    b = macd - sig
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 126d the MACD line was positive (trend-up regime breadth)
def f01ts_f01_trend_structure_macdpos_base_v131_signal(closeadj):
    e1 = _f01_ema(closeadj, 12)
    e2 = _f01_ema(closeadj, 26)
    pos = (e1 > e2).astype(float)
    b = pos.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long EMA(126) vs SMA(126) divergence (exponential leads simple, medium horizon)
def f01ts_f01_trend_structure_emavssma_126d_base_v132_signal(closeadj):
    ema = _f01_ema(closeadj, 126)
    sma = _f01_ma(closeadj, 126)
    b = (ema - sma) / sma.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of price-vs-MA(126d) over a quarter (displacement trend, momentum-of-stretch)
def f01ts_f01_trend_structure_distslope_126d_base_v133_signal(closeadj):
    d = _f01_pxvma(closeadj, 126)
    b = (d - d.shift(63)) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MA slope per unit of long realized vol (risk-adjusted long trend)
def f01ts_f01_trend_structure_riskadjslope_252d_base_v134_signal(closeadj):
    sl = _f01_maslope(closeadj, 252, 63)
    vol = closeadj.pct_change().rolling(126, min_periods=63).std()
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth of rising MAs: count of 5/21/63/126/252 MAs rising over 21d (trend breadth)
def f01ts_f01_trend_structure_risingbreadth_base_v135_signal(closeadj):
    cnt = 0.0
    for w in (5, 21, 63, 126, 252):
        ma = _f01_ma(closeadj, w)
        cnt = cnt + (ma > ma.shift(21)).astype(float)
    disp = pd.concat([_f01_maslope(closeadj, w, 21) for w in (5, 21, 63, 126, 252)], axis=1).mean(axis=1)
    b = (cnt - 2.5) + 50.0 * disp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convex price-vs-MA(21d): signed-square emphasis of fast stretch, mean-removed
def f01ts_f01_trend_structure_convex_21d_base_v136_signal(closeadj):
    d = _f01_pxvma(closeadj, 21)
    conv = np.sign(d) * (d ** 2) * 50.0
    b = conv - conv.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d MA vs 252d MA spread, tanh-bounded (fastest vs slowest trend gap)
def f01ts_f01_trend_structure_fastslowgap_base_v137_signal(closeadj):
    sp = _f01_maspread(closeadj, 5, 252)
    b = np.tanh(15.0 * sp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend persistence asymmetry: time above 63d MA in uptrend vs downtrend regimes
def f01ts_f01_trend_structure_persistasym_63d_base_v138_signal(closeadj):
    d = _f01_pxvma(closeadj, 63)
    above = (d > 0).astype(float)
    long_up = (_f01_maslope(closeadj, 252, 63) > 0).astype(float)
    pa = (above * long_up).rolling(126, min_periods=63).mean()
    pb = (above * (1 - long_up)).rolling(126, min_periods=63).mean()
    b = pa - pb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-MA(189d) z, percentile ranked vs own 504d (long stretch extremity)
def f01ts_f01_trend_structure_distzrank_189d_base_v139_signal(closeadj):
    dz = _z(_f01_pxvma(closeadj, 189), 252)
    b = dz.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of the 63d MA slope vs the 126d MA slope (short leading long)
def f01ts_f01_trend_structure_slopelead_base_v140_signal(closeadj):
    sf = _f01_maslope(closeadj, 63, 21)
    sl = _f01_maslope(closeadj, 126, 21)
    b = np.tanh(60.0 * (sf - sl))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 252d in a fully-stacked-down ribbon (bear-trend regime breadth)
def f01ts_f01_trend_structure_stackdownfrac_base_v141_signal(closeadj):
    st = _f01_stack3(closeadj)
    down = (st <= -1.49).astype(float)
    frac = down.rolling(252, min_periods=126).mean()
    width = (_f01_ma(closeadj, 252) - _f01_ma(closeadj, 21)) / _f01_ma(closeadj, 252).replace(0, np.nan)
    b = frac + 5.0 * width.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net trend score: mean of tanh price-vs-MA across 21/63/126/252 (smooth multi-MA bias)
def f01ts_f01_trend_structure_netbias_base_v142_signal(closeadj):
    parts = [np.tanh(c * _f01_pxvma(closeadj, w))
             for w, c in ((21, 20.0), (63, 12.0), (126, 9.0), (252, 7.0))]
    b = sum(parts) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 42d MA slope de-meaned vs its 252d normal (medium accel vs typical)
def f01ts_f01_trend_structure_slopeanom_42d_base_v143_signal(closeadj):
    sl = _f01_maslope(closeadj, 42, 21)
    b = sl - sl.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how long the 21d MA slope has stayed one sign, normalized (fast-trend run)
def f01ts_f01_trend_structure_sloperun_21d_base_v144_signal(closeadj):
    sl = np.sign(_f01_maslope(closeadj, 21, 5))

    def _run(a):
        last = a[-1]
        if last == 0 or np.isnan(last):
            return 0.0
        c = 0
        for v in a[::-1]:
            if v == last:
                c += 1
            else:
                break
        return last * c

    r = sl.rolling(63, min_periods=21).apply(_run, raw=True)
    b = r / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-vs-chop: 126d efficiency minus 21d efficiency (regime maturation)
def f01ts_f01_trend_structure_effspread_base_v145_signal(closeadj):
    e_long = _f01_efficiency(closeadj, 126)
    e_short = _f01_efficiency(closeadj, 21)
    b = e_long - e_short
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price distance above the 252d MA expressed in 252d-vol units, smoothed (long z-stretch)
def f01ts_f01_trend_structure_volstretch_252d_base_v146_signal(closeadj):
    ma = _f01_ma(closeadj, 252)
    d = closeadj - ma
    sd = closeadj.rolling(252, min_periods=126).std()
    b = (d / sd.replace(0, np.nan)).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# golden-cross magnitude weighted by its own persistence (durable cross strength)
def f01ts_f01_trend_structure_crosspw_base_v147_signal(closeadj):
    sp = _f01_maspread(closeadj, 63, 252)
    persist = (sp > 0).astype(float).rolling(126, min_periods=63).mean()
    b = sp * persist
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net new-trend-high frequency: price making 252d highs while above 63d MA (leadership)
def f01ts_f01_trend_structure_trendlead_base_v148_signal(closeadj):
    hi = _rmax(closeadj, 252)
    new_hi = (closeadj >= hi * 0.99999).astype(float)
    above = (closeadj > _f01_ma(closeadj, 63)).astype(float)
    freq = (new_hi * above).rolling(63, min_periods=21).mean()
    d = _f01_pxvma(closeadj, 63).clip(lower=0)
    b = freq + 0.5 * d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend reversal pressure: 21d slope sign opposite to 252d slope sign, magnitude-weighted
def f01ts_f01_trend_structure_revpress_base_v149_signal(closeadj):
    sf = _f01_maslope(closeadj, 21, 21)
    sl = _f01_maslope(closeadj, 252, 63)
    opp = (np.sign(sf) != np.sign(sl)).astype(float)
    b = opp * np.tanh(80.0 * sf.abs()) * np.sign(sf)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon trend composite: weighted vote of 5/42/189/504 price-vs-MA signs + magnitude
def f01ts_f01_trend_structure_multicomposite_base_v150_signal(closeadj):
    parts = []
    for w, c in ((5, 25.0), (42, 14.0), (189, 8.0), (504, 6.0)):
        parts.append(np.tanh(c * _f01_pxvma(closeadj, w)))
    vote = sum(parts) / 4.0
    disp = pd.concat(parts, axis=1).std(axis=1)
    b = vote * (1.0 + disp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01ts_f01_trend_structure_pxvma_5d_base_v076_signal,
    f01ts_f01_trend_structure_pxvma_42d_base_v077_signal,
    f01ts_f01_trend_structure_pxvma_189d_base_v078_signal,
    f01ts_f01_trend_structure_pxvma_504d_base_v079_signal,
    f01ts_f01_trend_structure_distz_42d_base_v080_signal,
    f01ts_f01_trend_structure_distz_189d_base_v081_signal,
    f01ts_f01_trend_structure_distz_504d_base_v082_signal,
    f01ts_f01_trend_structure_maspread_5v21_base_v083_signal,
    f01ts_f01_trend_structure_maspread_42v126_base_v084_signal,
    f01ts_f01_trend_structure_maspread_63v189_base_v085_signal,
    f01ts_f01_trend_structure_maspread_126v504_base_v086_signal,
    f01ts_f01_trend_structure_maslope_5d_base_v087_signal,
    f01ts_f01_trend_structure_maslope_42d_base_v088_signal,
    f01ts_f01_trend_structure_maslope_189d_base_v089_signal,
    f01ts_f01_trend_structure_maslope_504d_base_v090_signal,
    f01ts_f01_trend_structure_stack5_base_v091_signal,
    f01ts_f01_trend_structure_stackslope_base_v092_signal,
    f01ts_f01_trend_structure_abovefrac_504d_base_v093_signal,
    f01ts_f01_trend_structure_abovefrac_42d_base_v094_signal,
    f01ts_f01_trend_structure_efficiency_21d_base_v095_signal,
    f01ts_f01_trend_structure_signeff_252d_base_v096_signal,
    f01ts_f01_trend_structure_tstat_42d_base_v097_signal,
    f01ts_f01_trend_structure_tstat_189d_base_v098_signal,
    f01ts_f01_trend_structure_dirpersist_21d_base_v099_signal,
    f01ts_f01_trend_structure_dirpersist_252d_base_v100_signal,
    f01ts_f01_trend_structure_maspreadz_42v126_base_v101_signal,
    f01ts_f01_trend_structure_maspreadz_126v504_base_v102_signal,
    f01ts_f01_trend_structure_pxvmarank_63d_base_v103_signal,
    f01ts_f01_trend_structure_pxvmarank_252d_base_v104_signal,
    f01ts_f01_trend_structure_maconvex_42d_base_v105_signal,
    f01ts_f01_trend_structure_maconvex_252d_base_v106_signal,
    f01ts_f01_trend_structure_goldenpersist_42v189_base_v107_signal,
    f01ts_f01_trend_structure_spreadtanh_63v252_base_v108_signal,
    f01ts_f01_trend_structure_slopedisp5_base_v109_signal,
    f01ts_f01_trend_structure_madisp2_base_v110_signal,
    f01ts_f01_trend_structure_ribboncomp2_base_v111_signal,
    f01ts_f01_trend_structure_accel_21d_base_v112_signal,
    f01ts_f01_trend_structure_accel_126d_base_v113_signal,
    f01ts_f01_trend_structure_distrev_42d_base_v114_signal,
    f01ts_f01_trend_structure_distrev_126d_base_v115_signal,
    f01ts_f01_trend_structure_whipsaw_42v126_base_v116_signal,
    f01ts_f01_trend_structure_aboveall2_base_v117_signal,
    f01ts_f01_trend_structure_maxabove_42d_base_v118_signal,
    f01ts_f01_trend_structure_r2dir_252d_base_v119_signal,
    f01ts_f01_trend_structure_slopesignmag_252d_base_v120_signal,
    f01ts_f01_trend_structure_pullback_63d_base_v121_signal,
    f01ts_f01_trend_structure_thrust_63d_base_v122_signal,
    f01ts_f01_trend_structure_trendage_42v189_base_v123_signal,
    f01ts_f01_trend_structure_slopeagree2_base_v124_signal,
    f01ts_f01_trend_structure_distzstack5_base_v125_signal,
    f01ts_f01_trend_structure_composite_long_base_v126_signal,
    f01ts_f01_trend_structure_pxvmayoy_126d_base_v127_signal,
    f01ts_f01_trend_structure_ribbonentropy_base_v128_signal,
    f01ts_f01_trend_structure_macd_base_v129_signal,
    f01ts_f01_trend_structure_macdhist_base_v130_signal,
    f01ts_f01_trend_structure_macdpos_base_v131_signal,
    f01ts_f01_trend_structure_emavssma_126d_base_v132_signal,
    f01ts_f01_trend_structure_distslope_126d_base_v133_signal,
    f01ts_f01_trend_structure_riskadjslope_252d_base_v134_signal,
    f01ts_f01_trend_structure_risingbreadth_base_v135_signal,
    f01ts_f01_trend_structure_convex_21d_base_v136_signal,
    f01ts_f01_trend_structure_fastslowgap_base_v137_signal,
    f01ts_f01_trend_structure_persistasym_63d_base_v138_signal,
    f01ts_f01_trend_structure_distzrank_189d_base_v139_signal,
    f01ts_f01_trend_structure_slopelead_base_v140_signal,
    f01ts_f01_trend_structure_stackdownfrac_base_v141_signal,
    f01ts_f01_trend_structure_netbias_base_v142_signal,
    f01ts_f01_trend_structure_slopeanom_42d_base_v143_signal,
    f01ts_f01_trend_structure_sloperun_21d_base_v144_signal,
    f01ts_f01_trend_structure_effspread_base_v145_signal,
    f01ts_f01_trend_structure_volstretch_252d_base_v146_signal,
    f01ts_f01_trend_structure_crosspw_base_v147_signal,
    f01ts_f01_trend_structure_trendlead_base_v148_signal,
    f01ts_f01_trend_structure_revpress_base_v149_signal,
    f01ts_f01_trend_structure_multicomposite_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_TREND_STRUCTURE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f01_trend_structure_base_076_150_claude: %d features pass" % n_features)
