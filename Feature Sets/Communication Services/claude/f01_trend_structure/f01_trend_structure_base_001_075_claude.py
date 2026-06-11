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


# ===== folder domain primitives (trend structure: price vs MA, stacking, slope, persistence) =====
def _f01_ma(close, w):
    return close.rolling(w, min_periods=max(1, w // 2)).mean()


def _f01_ema(close, span):
    return close.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _f01_pxvma(close, w):
    # price relative to its w-day moving average (level above/below the MA)
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return close / ma.replace(0, np.nan) - 1.0


def _f01_logpxvma(close, w):
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.log(close.replace(0, np.nan) / ma.replace(0, np.nan))


def _f01_maslope(close, w, k):
    # log-slope of the w-day MA over k days (trend direction/strength of the MA itself)
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.log(ma.replace(0, np.nan) / ma.shift(k).replace(0, np.nan)) / float(k)


def _f01_maspread(close, ws, wl):
    # short MA vs long MA spread (golden/death-cross magnitude)
    s = close.rolling(ws, min_periods=max(1, ws // 2)).mean()
    l = close.rolling(wl, min_periods=max(1, wl // 2)).mean()
    return s / l.replace(0, np.nan) - 1.0


def _f01_distz(close, w, zw):
    # distance-from-MA z-score (how stretched price is vs its MA, in own units)
    d = close / close.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan) - 1.0
    return _z(d, zw)


def _f01_abovefrac(close, w, lw):
    # persistence: fraction of the last lw days price closed above its w-day MA
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    above = (close > ma).astype(float)
    return above.rolling(lw, min_periods=max(1, lw // 2)).mean()


def _f01_stack3(close):
    # MA stacking score across 21/63/126/252: count of correctly ordered adjacent pairs
    m21 = close.rolling(21, min_periods=10).mean()
    m63 = close.rolling(63, min_periods=31).mean()
    m126 = close.rolling(126, min_periods=63).mean()
    m252 = close.rolling(252, min_periods=126).mean()
    s = (m21 > m63).astype(float) + (m63 > m126).astype(float) + (m126 > m252).astype(float)
    return s - 1.5


def _f01_dirpersist(close, w, lw):
    # trend direction persistence: net fraction of days the w-day MA rose over lw days
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    up = np.sign(ma.diff())
    return up.rolling(lw, min_periods=max(1, lw // 2)).mean()


def _f01_runlen(close, w):
    # current signed run length of price-above/below the w-day MA, normalized
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    sign = np.sign(close - ma)

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

    r = sign.rolling(w, min_periods=max(1, w // 2)).apply(_run, raw=True)
    return r / float(w)


def _f01_tstat(close, w):
    # trend t-stat: log-price regressed on time over w days -> slope / stderr
    lp = np.log(close.replace(0, np.nan))

    def _t(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        if np.any(np.isnan(a)):
            return np.nan
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


# ============================================================
# price vs 21d MA (level above/below the fast MA)
def f01ts_f01_trend_structure_pxvma_21d_base_v001_signal(closeadj):
    b = _f01_pxvma(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 63d MA
def f01ts_f01_trend_structure_pxvma_63d_base_v002_signal(closeadj):
    b = _f01_pxvma(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 126d MA
def f01ts_f01_trend_structure_pxvma_126d_base_v003_signal(closeadj):
    b = _f01_pxvma(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 252d MA (long-trend extension)
def f01ts_f01_trend_structure_pxvma_252d_base_v004_signal(closeadj):
    b = _f01_pxvma(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log price vs 21d MA EMA-smoothed (persistent fast displacement)
def f01ts_f01_trend_structure_logpxvma_21d_base_v005_signal(closeadj):
    b = _f01_logpxvma(closeadj, 21).ewm(span=10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 252d EMA displacement, percentile-ranked vs own 504d history (long-trend extremity)
def f01ts_f01_trend_structure_logpxvema_252d_base_v006_signal(closeadj):
    ema = _f01_ema(closeadj, 252)
    d = np.log(closeadj.replace(0, np.nan) / ema.replace(0, np.nan))
    b = d.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-MA z: 21d MA distance z-scored vs own 126d history
def f01ts_f01_trend_structure_distz_21d_base_v007_signal(closeadj):
    b = _f01_distz(closeadj, 21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-MA z: 63d MA distance z-scored vs own 252d history
def f01ts_f01_trend_structure_distz_63d_base_v008_signal(closeadj):
    b = _f01_distz(closeadj, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-MA z: 126d MA distance z-scored vs own 252d history
def f01ts_f01_trend_structure_distz_126d_base_v009_signal(closeadj):
    b = _f01_distz(closeadj, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-MA z: 252d MA distance z-scored vs own 504d history
def f01ts_f01_trend_structure_distz_252d_base_v010_signal(closeadj):
    b = _f01_distz(closeadj, 252, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21/63 MA spread (fast vs medium cross magnitude)
def f01ts_f01_trend_structure_maspread_21v63_base_v011_signal(closeadj):
    b = _f01_maspread(closeadj, 21, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21/126 MA spread
def f01ts_f01_trend_structure_maspread_21v126_base_v012_signal(closeadj):
    b = _f01_maspread(closeadj, 21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 50/200-style 63/252 MA spread (golden/death cross)
def f01ts_f01_trend_structure_maspread_63v252_base_v013_signal(closeadj):
    b = _f01_maspread(closeadj, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126/252 MA spread (slow trend regime)
def f01ts_f01_trend_structure_maspread_126v252_base_v014_signal(closeadj):
    b = _f01_maspread(closeadj, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MA log-slope over 21d (fast MA trend direction)
def f01ts_f01_trend_structure_maslope_21d_base_v015_signal(closeadj):
    b = _f01_maslope(closeadj, 21, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d MA log-slope over 21d
def f01ts_f01_trend_structure_maslope_63d_base_v016_signal(closeadj):
    b = _f01_maslope(closeadj, 63, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d MA log-slope over 63d, de-meaned vs its own year (trend acceleration vs normal)
def f01ts_f01_trend_structure_maslope_126d_base_v017_signal(closeadj):
    sl = _f01_maslope(closeadj, 126, 63)
    b = sl - sl.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MA log-slope over 63d (long-trend direction)
def f01ts_f01_trend_structure_maslope_252d_base_v018_signal(closeadj):
    b = _f01_maslope(closeadj, 252, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA stacking score across 21/63/126/252, magnitude-weighted by gap sizes
def f01ts_f01_trend_structure_stack_base_v019_signal(closeadj):
    m21 = _f01_ma(closeadj, 21)
    m63 = _f01_ma(closeadj, 63)
    m126 = _f01_ma(closeadj, 126)
    m252 = _f01_ma(closeadj, 252)
    g1 = (m21 - m63) / m63.replace(0, np.nan)
    g2 = (m63 - m126) / m126.replace(0, np.nan)
    g3 = (m126 - m252) / m252.replace(0, np.nan)
    sc = _f01_stack3(closeadj)
    b = sc + 5.0 * (g1 + g2 + g3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA stacking persistence: fraction of last quarter fully stacked up
def f01ts_f01_trend_structure_stackpersist_base_v020_signal(closeadj):
    st = _f01_stack3(closeadj)
    full = (st >= 1.49).astype(float)
    b = full.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 63d price closed above 21d MA (fast persistence)
def f01ts_f01_trend_structure_abovefrac_21d_base_v021_signal(closeadj):
    b = _f01_abovefrac(closeadj, 21, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 126d price closed above 63d MA
def f01ts_f01_trend_structure_abovefrac_63d_base_v022_signal(closeadj):
    b = _f01_abovefrac(closeadj, 63, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 252d price closed above 126d MA
def f01ts_f01_trend_structure_abovefrac_126d_base_v023_signal(closeadj):
    b = _f01_abovefrac(closeadj, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 252d price closed above 252d MA (long persistence)
def f01ts_f01_trend_structure_abovefrac_252d_base_v024_signal(closeadj):
    b = _f01_abovefrac(closeadj, 252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend t-stat over 63d (regression strength of log-price trend)
def f01ts_f01_trend_structure_tstat_63d_base_v025_signal(closeadj):
    b = _f01_tstat(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend t-stat over 126d
def f01ts_f01_trend_structure_tstat_126d_base_v026_signal(closeadj):
    b = _f01_tstat(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend t-stat over 252d, de-meaned vs its own 504d history (long-trend regime extremity)
def f01ts_f01_trend_structure_tstat_252d_base_v027_signal(closeadj):
    t = _f01_tstat(closeadj, 252)
    b = t - t.rolling(504, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed run length of price-above-MA(21d), normalized (trend streak)
def f01ts_f01_trend_structure_runlen_21d_base_v028_signal(closeadj):
    b = _f01_runlen(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed run length of price-above-MA(63d), normalized
def f01ts_f01_trend_structure_runlen_63d_base_v029_signal(closeadj):
    b = _f01_runlen(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-direction persistence: net up-fraction of 63d MA over a quarter
def f01ts_f01_trend_structure_dirpersist_63d_base_v030_signal(closeadj):
    b = _f01_dirpersist(closeadj, 63, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-direction persistence: net up-fraction of 126d MA over a half-year
def f01ts_f01_trend_structure_dirpersist_126d_base_v031_signal(closeadj):
    b = _f01_dirpersist(closeadj, 126, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convexity of trend: 21/63 spread minus 63/252 spread (accel of stacking)
def f01ts_f01_trend_structure_stackconvex_base_v032_signal(closeadj):
    fast = _f01_maspread(closeadj, 21, 63)
    slow = _f01_maspread(closeadj, 63, 252)
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fast-MA displacement convexity: signed square of price-vs-MA(21d) (extreme stretch emphasis)
def f01ts_f01_trend_structure_pxvmavol_21d_base_v033_signal(closeadj):
    d = _f01_pxvma(closeadj, 21)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    norm = d / vol.replace(0, np.nan)
    b = np.sign(norm) * (norm.abs() ** 1.5) - norm.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-MA displacement momentum: change in price-vs-MA(63d) over a month minus its drift
def f01ts_f01_trend_structure_pxvmavol_63d_base_v034_signal(closeadj):
    d = _f01_pxvma(closeadj, 63)
    chg = d - d.shift(21)
    b = chg - chg.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-vs-MA(21d) percentile-ranked vs own 252d history
def f01ts_f01_trend_structure_pxvmarank_21d_base_v035_signal(closeadj):
    d = _f01_pxvma(closeadj, 21)
    b = d.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-vs-MA(126d) percentile-ranked vs own 504d history
def f01ts_f01_trend_structure_pxvmarank_126d_base_v036_signal(closeadj):
    d = _f01_pxvma(closeadj, 126)
    b = d.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day fraction: return-weighted share of last 63d moving with the 63d MA trend
def f01ts_f01_trend_structure_trenddayfrac_63d_base_v037_signal(closeadj):
    ma = _f01_ma(closeadj, 63)
    trend = np.sign(ma - ma.shift(21))
    ret = closeadj.pct_change()
    aligned = trend * ret
    b = aligned.rolling(63, min_periods=21).mean() / ret.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA spread 21v63 z-scored vs own 252d history (regime-relative cross)
def f01ts_f01_trend_structure_maspreadz_21v63_base_v038_signal(closeadj):
    sp = _f01_maspread(closeadj, 21, 63)
    b = _z(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA spread 63v252 z-scored vs own 252d history
def f01ts_f01_trend_structure_maspreadz_63v252_base_v039_signal(closeadj):
    sp = _f01_maspread(closeadj, 63, 252)
    b = _z(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# golden-cross state persistence: fraction of last 126d with 63d MA > 252d MA
def f01ts_f01_trend_structure_goldenpersist_base_v040_signal(closeadj):
    m63 = _f01_ma(closeadj, 63)
    m252 = _f01_ma(closeadj, 252)
    state = (m63 > m252).astype(float)
    b = state.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since last 21d/63d MA cross, normalized (cross freshness)
def f01ts_f01_trend_structure_crossage_21v63_base_v041_signal(closeadj):
    m21 = _f01_ma(closeadj, 21)
    m63 = _f01_ma(closeadj, 63)
    state = np.sign(m21 - m63)

    def _age(a):
        last = a[-1]
        if np.isnan(last):
            return np.nan
        c = 0
        for v in a[::-1]:
            if v == last:
                c += 1
            else:
                break
        return c / float(len(a))

    b = state.rolling(126, min_periods=31).apply(_age, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-slope agreement: sign-vote of 21/63/126 MA slopes, magnitude-weighted by mean slope
def f01ts_f01_trend_structure_slopeagree_base_v042_signal(closeadj):
    sl1 = _f01_maslope(closeadj, 21, 21)
    sl2 = _f01_maslope(closeadj, 63, 21)
    sl3 = _f01_maslope(closeadj, 126, 21)
    vote = (np.sign(sl1) + np.sign(sl2) + np.sign(sl3)) / 3.0
    mag = (sl1 + sl2 + sl3) / 3.0
    b = vote * (1.0 + 30.0 * mag.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend efficiency: net move over 63d divided by total path traveled
def f01ts_f01_trend_structure_efficiency_63d_base_v043_signal(closeadj):
    net = (closeadj - closeadj.shift(63)).abs()
    path = closeadj.diff().abs().rolling(63, min_periods=21).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend efficiency 126d, signed by direction
def f01ts_f01_trend_structure_signeff_126d_base_v044_signal(closeadj):
    net = closeadj - closeadj.shift(126)
    path = closeadj.diff().abs().rolling(126, min_periods=63).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stacking score smoothed (persistent alignment level)
def f01ts_f01_trend_structure_stacksm_base_v045_signal(closeadj):
    st = _f01_stack3(closeadj)
    b = st.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-crossing rate of price through its 21d MA over 63d (trend instability around fast MA)
def f01ts_f01_trend_structure_distatr_21d_base_v046_signal(closeadj):
    ma = _f01_ma(closeadj, 21)
    side = np.sign(closeadj - ma)
    cross = (side != side.shift(1)).astype(float)
    rate = cross.rolling(63, min_periods=21).mean()
    dur = side.rolling(63, min_periods=21).mean()
    b = rate - 0.3 * dur.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-MA distance asymmetry: upside-vs-downside excursion balance over a quarter
def f01ts_f01_trend_structure_distatr_63d_base_v047_signal(closeadj):
    d = _f01_pxvma(closeadj, 63)
    up = d.clip(lower=0).rolling(63, min_periods=21).mean()
    dn = (-d).clip(lower=0).rolling(63, min_periods=21).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend curvature: change in 63d MA log-slope over a month (is trend bending?)
def f01ts_f01_trend_structure_curve_63d_base_v048_signal(closeadj):
    sl = _f01_maslope(closeadj, 63, 21)
    b = sl - sl.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend curvature of 126d MA over a quarter
def f01ts_f01_trend_structure_curve_126d_base_v049_signal(closeadj):
    sl = _f01_maslope(closeadj, 126, 21)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed 21v63 MA spread (bounded fast-cross state)
def f01ts_f01_trend_structure_spreadtanh_21v63_base_v050_signal(closeadj):
    sp = _f01_maspread(closeadj, 21, 63)
    b = np.tanh(30.0 * sp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest unbroken streak (last year) of price holding above the 126d MA, normalized
def f01ts_f01_trend_structure_abovenet_126d_base_v051_signal(closeadj):
    ma = _f01_ma(closeadj, 126)
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

    b = above.rolling(252, min_periods=126).apply(_maxrun, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-MA dispersion: std of price/MA across 21/63/126/252 (trend fan-out)
def f01ts_f01_trend_structure_madisp_base_v052_signal(closeadj):
    r1 = closeadj / _f01_ma(closeadj, 21).replace(0, np.nan)
    r2 = closeadj / _f01_ma(closeadj, 63).replace(0, np.nan)
    r3 = closeadj / _f01_ma(closeadj, 126).replace(0, np.nan)
    r4 = closeadj / _f01_ma(closeadj, 252).replace(0, np.nan)
    b = pd.concat([r1, r2, r3, r4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA ribbon compression: range of the four MAs scaled by price (squeeze vs spread)
def f01ts_f01_trend_structure_ribboncomp_base_v053_signal(closeadj):
    m1 = _f01_ma(closeadj, 21)
    m2 = _f01_ma(closeadj, 63)
    m3 = _f01_ma(closeadj, 126)
    m4 = _f01_ma(closeadj, 252)
    stacked = pd.concat([m1, m2, m3, m4], axis=1)
    b = (stacked.max(axis=1) - stacked.min(axis=1)) / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 21d MA, year-over-year change (trend regime shift)
def f01ts_f01_trend_structure_pxvmayoy_63d_base_v054_signal(closeadj):
    d = _f01_pxvma(closeadj, 63)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend monotonicity: net fraction of last 126d daily closes that advanced (drift breadth)
def f01ts_f01_trend_structure_strengthdir_126d_base_v055_signal(closeadj):
    up = (closeadj.diff() > 0).astype(float)
    breadth = up.rolling(126, min_periods=63).mean() - 0.5
    mag = (closeadj / closeadj.shift(126).replace(0, np.nan) - 1.0)
    b = breadth * np.sign(mag) * (1.0 + mag.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last quarter price spent >10% stretched above its 252d MA (overextension regime)
def f01ts_f01_trend_structure_overext_up_252d_base_v056_signal(closeadj):
    d = _f01_pxvma(closeadj, 252)
    hot = (d > 0.10).astype(float)
    entries = ((hot == 1) & (hot.shift(1) == 0)).astype(float)
    rate = entries.rolling(126, min_periods=63).sum()
    frac = hot.rolling(63, min_periods=21).mean()
    b = rate + frac
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how stretched price is below 252d MA, clipped to downside (overextension down)
def f01ts_f01_trend_structure_overext_dn_252d_base_v057_signal(closeadj):
    d = _f01_pxvma(closeadj, 252)
    b = (-d).clip(lower=0).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fast-vs-slow trend slope ratio (acceleration regime of the MAs)
def f01ts_f01_trend_structure_sloperatio_base_v058_signal(closeadj):
    fast = _f01_maslope(closeadj, 21, 21)
    slow = _f01_maslope(closeadj, 126, 21)
    b = np.tanh(50.0 * (fast - slow))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# above-all-MAs flag persistence: fraction of last 63d price above all four MAs
def f01ts_f01_trend_structure_aboveall_base_v059_signal(closeadj):
    m1 = _f01_ma(closeadj, 21)
    m2 = _f01_ma(closeadj, 63)
    m3 = _f01_ma(closeadj, 126)
    m4 = _f01_ma(closeadj, 252)
    flag = ((closeadj > m1) & (closeadj > m2) & (closeadj > m3) & (closeadj > m4)).astype(float)
    b = flag.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend acceleration: 63d return minus prior 63d return (momentum-of-trend as level)
def f01ts_f01_trend_structure_accel_63d_base_v060_signal(closeadj):
    r_now = closeadj / closeadj.shift(63).replace(0, np.nan) - 1.0
    r_prev = closeadj.shift(63) / closeadj.shift(126).replace(0, np.nan) - 1.0
    b = r_now - r_prev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stack alignment change over a quarter, magnitude-weighted by ribbon width
def f01ts_f01_trend_structure_stackchg_base_v061_signal(closeadj):
    m21 = _f01_ma(closeadj, 21)
    m252 = _f01_ma(closeadj, 252)
    width = (m21 - m252) / m252.replace(0, np.nan)
    st = _f01_stack3(closeadj) + 10.0 * width
    b = st - st.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-MA(21d) mean-reversion: current minus its own 63d average
def f01ts_f01_trend_structure_distrev_21d_base_v062_signal(closeadj):
    d = _f01_pxvma(closeadj, 21)
    b = d - d.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-MA(63d) mean-reversion vs its 126d average
def f01ts_f01_trend_structure_distrev_63d_base_v063_signal(closeadj):
    d = _f01_pxvma(closeadj, 63)
    b = d - d.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# whipsaw intensity: 21d/63d cross count over 126d divided by trend efficiency (choppiness)
def f01ts_f01_trend_structure_whipsaw_base_v064_signal(closeadj):
    m21 = _f01_ma(closeadj, 21)
    m63 = _f01_ma(closeadj, 63)
    state = np.sign(m21 - m63)
    flip = (state != state.shift(1)).astype(float)
    cnt = flip.rolling(126, min_periods=63).sum()
    net = (closeadj - closeadj.shift(126)).abs()
    path = closeadj.diff().abs().rolling(126, min_periods=63).sum()
    eff = net / path.replace(0, np.nan)
    b = cnt * (1.0 - eff)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EMA vs SMA divergence at 252d: where the exponential trend leads the simple trend
def f01ts_f01_trend_structure_emaslope_252d_base_v065_signal(closeadj):
    ema = _f01_ema(closeadj, 252)
    sma = _f01_ma(closeadj, 252)
    b = (ema - sma) / sma.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend smoothness: R^2 of the 126d log-price trend regression (how linear the trend is)
def f01ts_f01_trend_structure_quality_252d_base_v066_signal(closeadj):
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

    r2 = lp.rolling(126, min_periods=63).apply(_r2, raw=True)
    dirn = np.sign(_f01_maslope(closeadj, 126, 21))
    b = r2 * dirn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net days above 21d MA minus days above 252d MA (fast vs slow trend split)
def f01ts_f01_trend_structure_abovespl_base_v067_signal(closeadj):
    a_fast = _f01_abovefrac(closeadj, 21, 126)
    a_slow = _f01_abovefrac(closeadj, 252, 126)
    b = a_fast - a_slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA spread 21v252 (widest fast-slow displacement)
def f01ts_f01_trend_structure_maspread_21v252_base_v068_signal(closeadj):
    b = _f01_maspread(closeadj, 21, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direction-of-trend sign-magnitude: sqrt-compressed 126d MA slope
def f01ts_f01_trend_structure_slopesignmag_126d_base_v069_signal(closeadj):
    sl = _f01_maslope(closeadj, 126, 63)
    b = np.sign(sl) * (sl.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# persistence-weighted stack: stack score times its own 63d persistence
def f01ts_f01_trend_structure_stackpw_base_v070_signal(closeadj):
    st = _f01_stack3(closeadj)
    persist = (st >= 0.49).astype(float).rolling(63, min_periods=21).mean()
    b = st * persist
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-MA z(126) interacted with stacking (stretched AND aligned)
def f01ts_f01_trend_structure_distzstack_base_v071_signal(closeadj):
    dz = _f01_distz(closeadj, 126, 252)
    st = _f01_stack3(closeadj)
    b = dz * st
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend slope dispersion: std of 21/63/126/252 MA slopes (fan divergence)
def f01ts_f01_trend_structure_slopedisp_base_v072_signal(closeadj):
    s1 = _f01_maslope(closeadj, 21, 21)
    s2 = _f01_maslope(closeadj, 63, 21)
    s3 = _f01_maslope(closeadj, 126, 21)
    s4 = _f01_maslope(closeadj, 252, 21)
    b = pd.concat([s1, s2, s3, s4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pullback-in-uptrend: depth below 21d MA while 63d MA rising (healthy dip)
def f01ts_f01_trend_structure_pullback_base_v073_signal(closeadj):
    d21 = _f01_pxvma(closeadj, 21)
    up = (_f01_maslope(closeadj, 63, 21) > 0).astype(float)
    b = (-d21).clip(lower=0) * up
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend age: signed run length of golden-cross state, normalized (mature trend)
def f01ts_f01_trend_structure_trendage_base_v074_signal(closeadj):
    m63 = _f01_ma(closeadj, 63)
    m252 = _f01_ma(closeadj, 252)
    state = np.sign(m63 - m252)

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

    r = state.rolling(252, min_periods=63).apply(_run, raw=True)
    b = r / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite trend score: stack vote blended with continuous cross & displacement magnitude
def f01ts_f01_trend_structure_composite_base_v075_signal(closeadj):
    st = _f01_stack3(closeadj) / 1.5
    cross = np.tanh(40.0 * _f01_maspread(closeadj, 63, 252))
    fast = np.tanh(25.0 * _f01_pxvma(closeadj, 21))
    b = (st + cross + fast) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01ts_f01_trend_structure_pxvma_21d_base_v001_signal,
    f01ts_f01_trend_structure_pxvma_63d_base_v002_signal,
    f01ts_f01_trend_structure_pxvma_126d_base_v003_signal,
    f01ts_f01_trend_structure_pxvma_252d_base_v004_signal,
    f01ts_f01_trend_structure_logpxvma_21d_base_v005_signal,
    f01ts_f01_trend_structure_logpxvema_252d_base_v006_signal,
    f01ts_f01_trend_structure_distz_21d_base_v007_signal,
    f01ts_f01_trend_structure_distz_63d_base_v008_signal,
    f01ts_f01_trend_structure_distz_126d_base_v009_signal,
    f01ts_f01_trend_structure_distz_252d_base_v010_signal,
    f01ts_f01_trend_structure_maspread_21v63_base_v011_signal,
    f01ts_f01_trend_structure_maspread_21v126_base_v012_signal,
    f01ts_f01_trend_structure_maspread_63v252_base_v013_signal,
    f01ts_f01_trend_structure_maspread_126v252_base_v014_signal,
    f01ts_f01_trend_structure_maslope_21d_base_v015_signal,
    f01ts_f01_trend_structure_maslope_63d_base_v016_signal,
    f01ts_f01_trend_structure_maslope_126d_base_v017_signal,
    f01ts_f01_trend_structure_maslope_252d_base_v018_signal,
    f01ts_f01_trend_structure_stack_base_v019_signal,
    f01ts_f01_trend_structure_stackpersist_base_v020_signal,
    f01ts_f01_trend_structure_abovefrac_21d_base_v021_signal,
    f01ts_f01_trend_structure_abovefrac_63d_base_v022_signal,
    f01ts_f01_trend_structure_abovefrac_126d_base_v023_signal,
    f01ts_f01_trend_structure_abovefrac_252d_base_v024_signal,
    f01ts_f01_trend_structure_tstat_63d_base_v025_signal,
    f01ts_f01_trend_structure_tstat_126d_base_v026_signal,
    f01ts_f01_trend_structure_tstat_252d_base_v027_signal,
    f01ts_f01_trend_structure_runlen_21d_base_v028_signal,
    f01ts_f01_trend_structure_runlen_63d_base_v029_signal,
    f01ts_f01_trend_structure_dirpersist_63d_base_v030_signal,
    f01ts_f01_trend_structure_dirpersist_126d_base_v031_signal,
    f01ts_f01_trend_structure_stackconvex_base_v032_signal,
    f01ts_f01_trend_structure_pxvmavol_21d_base_v033_signal,
    f01ts_f01_trend_structure_pxvmavol_63d_base_v034_signal,
    f01ts_f01_trend_structure_pxvmarank_21d_base_v035_signal,
    f01ts_f01_trend_structure_pxvmarank_126d_base_v036_signal,
    f01ts_f01_trend_structure_trenddayfrac_63d_base_v037_signal,
    f01ts_f01_trend_structure_maspreadz_21v63_base_v038_signal,
    f01ts_f01_trend_structure_maspreadz_63v252_base_v039_signal,
    f01ts_f01_trend_structure_goldenpersist_base_v040_signal,
    f01ts_f01_trend_structure_crossage_21v63_base_v041_signal,
    f01ts_f01_trend_structure_slopeagree_base_v042_signal,
    f01ts_f01_trend_structure_efficiency_63d_base_v043_signal,
    f01ts_f01_trend_structure_signeff_126d_base_v044_signal,
    f01ts_f01_trend_structure_stacksm_base_v045_signal,
    f01ts_f01_trend_structure_distatr_21d_base_v046_signal,
    f01ts_f01_trend_structure_distatr_63d_base_v047_signal,
    f01ts_f01_trend_structure_curve_63d_base_v048_signal,
    f01ts_f01_trend_structure_curve_126d_base_v049_signal,
    f01ts_f01_trend_structure_spreadtanh_21v63_base_v050_signal,
    f01ts_f01_trend_structure_abovenet_126d_base_v051_signal,
    f01ts_f01_trend_structure_madisp_base_v052_signal,
    f01ts_f01_trend_structure_ribboncomp_base_v053_signal,
    f01ts_f01_trend_structure_pxvmayoy_63d_base_v054_signal,
    f01ts_f01_trend_structure_strengthdir_126d_base_v055_signal,
    f01ts_f01_trend_structure_overext_up_252d_base_v056_signal,
    f01ts_f01_trend_structure_overext_dn_252d_base_v057_signal,
    f01ts_f01_trend_structure_sloperatio_base_v058_signal,
    f01ts_f01_trend_structure_aboveall_base_v059_signal,
    f01ts_f01_trend_structure_accel_63d_base_v060_signal,
    f01ts_f01_trend_structure_stackchg_base_v061_signal,
    f01ts_f01_trend_structure_distrev_21d_base_v062_signal,
    f01ts_f01_trend_structure_distrev_63d_base_v063_signal,
    f01ts_f01_trend_structure_whipsaw_base_v064_signal,
    f01ts_f01_trend_structure_emaslope_252d_base_v065_signal,
    f01ts_f01_trend_structure_quality_252d_base_v066_signal,
    f01ts_f01_trend_structure_abovespl_base_v067_signal,
    f01ts_f01_trend_structure_maspread_21v252_base_v068_signal,
    f01ts_f01_trend_structure_slopesignmag_126d_base_v069_signal,
    f01ts_f01_trend_structure_stackpw_base_v070_signal,
    f01ts_f01_trend_structure_distzstack_base_v071_signal,
    f01ts_f01_trend_structure_slopedisp_base_v072_signal,
    f01ts_f01_trend_structure_pullback_base_v073_signal,
    f01ts_f01_trend_structure_trendage_base_v074_signal,
    f01ts_f01_trend_structure_composite_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_TREND_STRUCTURE_REGISTRY_001_075 = REGISTRY


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

    print("OK f01_trend_structure_base_001_075_claude: %d features pass" % n_features)
