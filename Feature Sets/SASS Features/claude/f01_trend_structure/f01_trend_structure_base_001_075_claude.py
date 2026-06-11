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


# ===== folder domain primitives (trend structure: MA / slope / alignment) =====
def _f01_sma(close, w):
    return close.rolling(w, min_periods=max(1, w // 2)).mean()


def _f01_ema(close, w):
    return close.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _f01_pxma(close, w):
    ma = _f01_sma(close, w)
    return close / ma.replace(0, np.nan) - 1.0


def _f01_pxema(close, w):
    ma = _f01_ema(close, w)
    return close / ma.replace(0, np.nan) - 1.0


def _f01_slope(close, w):
    # OLS slope of log-price vs time, normalized to per-bar return units
    lp = np.log(close.replace(0, np.nan))
    x = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    xm = x.rolling(w, min_periods=max(2, w // 2)).mean()
    ym = lp.rolling(w, min_periods=max(2, w // 2)).mean()
    xy = (x * lp).rolling(w, min_periods=max(2, w // 2)).mean()
    xx = (x * x).rolling(w, min_periods=max(2, w // 2)).mean()
    cov = xy - xm * ym
    var = xx - xm * xm
    return cov / var.replace(0, np.nan)


def _f01_slope_r2(close, w):
    # R^2 of the log-price regression over window w
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


def _f01_slope_tstat(close, w):
    # t-stat of the regression slope = slope / SE(slope)
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
    vy = (yy - ym * ym).replace(0, np.nan)
    beta = cov / vx
    r2 = (cov * cov) / (vx * vy)
    dof = float(max(1, w - 2))
    se = np.sqrt(((1.0 - r2) * vy / vx) / dof)
    return beta / se.replace(0, np.nan)


def _f01_macd(close, fast, slow):
    return _f01_ema(close, fast) - _f01_ema(close, slow)


def _f01_above_frac(close, w):
    ma = _f01_sma(close, w)
    above = (close > ma).astype(float)
    return above.rolling(w, min_periods=max(1, w // 2)).mean()


def _f01_stack3(close, w1, w2, w3):
    # ordering coherence of three MAs, each gap normalized by its own recent scale so the
    # raw price-level factor cancels: emphasizes whether the ribbon is *aligned*, not stretched
    m1 = _f01_sma(close, w1)
    m2 = _f01_sma(close, w2)
    m3 = _f01_sma(close, w3)
    g_12 = m1 / m2.replace(0, np.nan) - 1.0
    g_23 = m2 / m3.replace(0, np.nan) - 1.0
    n_12 = np.tanh(g_12 / g_12.rolling(126, min_periods=42).std().replace(0, np.nan))
    n_23 = np.tanh(g_23 / g_23.rolling(126, min_periods=42).std().replace(0, np.nan))
    return (n_12 + n_23) / 2.0


# ============================================================
# price vs 21d SMA
def f01ts_f01_trend_structure_pxma_21d_base_v001_signal(closeadj):
    b = _f01_pxma(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 63d SMA
def f01ts_f01_trend_structure_pxma_63d_base_v002_signal(closeadj):
    b = _f01_pxma(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 126d SMA
def f01ts_f01_trend_structure_pxma_126d_base_v003_signal(closeadj):
    b = _f01_pxma(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 252d SMA
def f01ts_f01_trend_structure_pxma_252d_base_v004_signal(closeadj):
    b = _f01_pxma(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 21d EMA, demeaned by its own 63d average (short EMA gap mean-reversion)
def f01ts_f01_trend_structure_pxema_21d_base_v005_signal(closeadj):
    d = _f01_pxema(closeadj, 21)
    b = d - d.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum of the 63d-EMA gap: change in price-vs-63d-EMA distance over a month (pulling away)
def f01ts_f01_trend_structure_pxema_63d_base_v006_signal(closeadj):
    d = _f01_pxema(closeadj, 63)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-trend lead: 252d EMA above 252d SMA (exponential weighting leads when accelerating up)
def f01ts_f01_trend_structure_pxema_252d_base_v007_signal(closeadj):
    e = _f01_ema(closeadj, 252)
    s = _f01_sma(closeadj, 252)
    b = e / s.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of price-above-21d-SMA z-scored vs its own 63d history (extension extremity)
def f01ts_f01_trend_structure_pxmaz_21d_base_v008_signal(closeadj):
    d = _f01_pxma(closeadj, 21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of price-above-63d-SMA z-scored vs its own 126d history
def f01ts_f01_trend_structure_pxmaz_63d_base_v009_signal(closeadj):
    d = _f01_pxma(closeadj, 63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of price-above-252d-SMA z-scored vs its own 252d history
def f01ts_f01_trend_structure_pxmaz_252d_base_v010_signal(closeadj):
    d = _f01_pxma(closeadj, 252)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-distance crossing rate: how often (and how decisively) price re-crosses its 63d SMA
def f01ts_f01_trend_structure_pxmavol_63d_base_v011_signal(closeadj):
    d = _f01_pxma(closeadj, 63)
    cross = ((np.sign(d) != np.sign(d.shift(1))) & d.notna()).astype(float)
    rate = cross.rolling(63, min_periods=21).mean()
    # decisive trends cross rarely and sit far from the MA -> low rate, high |d|
    b = d.abs().rolling(21, min_periods=10).mean() * (1.0 - rate) * np.sign(d)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d/63d SMA spread (short-vs-mid MA gap, golden-cross magnitude)
def f01ts_f01_trend_structure_maspr_21v63_base_v012_signal(closeadj):
    m1 = _f01_sma(closeadj, 21)
    m2 = _f01_sma(closeadj, 63)
    b = m1 / m2.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d/126d SMA spread, demeaned by its own 252d average (mid-cross mean-reversion gap)
def f01ts_f01_trend_structure_maspr_63v126_base_v013_signal(closeadj):
    m1 = _f01_sma(closeadj, 63)
    m2 = _f01_sma(closeadj, 126)
    raw = m1 / m2.replace(0, np.nan) - 1.0
    b = raw - raw.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 50/200-style cross ratio (63d vs 252d SMA, golden/death cross)
def f01ts_f01_trend_structure_maspr_63v252_base_v014_signal(closeadj):
    m1 = _f01_sma(closeadj, 63)
    m2 = _f01_sma(closeadj, 252)
    b = m1 / m2.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21/252 SMA cross ratio momentum: change in the fast-vs-slow gap over a quarter
def f01ts_f01_trend_structure_maspr_21v252_base_v015_signal(closeadj):
    m1 = _f01_sma(closeadj, 21)
    m2 = _f01_sma(closeadj, 252)
    gap = m1 / m2.replace(0, np.nan) - 1.0
    b = gap - gap.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EMA cross ratio 21v63, z-scored vs its own 126d history (de-trended cross)
def f01ts_f01_trend_structure_emaspr_21v63_base_v016_signal(closeadj):
    e1 = _f01_ema(closeadj, 21)
    e2 = _f01_ema(closeadj, 63)
    raw = e1 / e2.replace(0, np.nan) - 1.0
    b = _z(raw, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EMA cross ratio 21v126, demeaned by its own 126d average (de-trended fast-vs-slow EMA cross)
def f01ts_f01_trend_structure_emaspr_63v126_base_v017_signal(closeadj):
    e1 = _f01_ema(closeadj, 21)
    e2 = _f01_ema(closeadj, 126)
    raw = e1 / e2.replace(0, np.nan) - 1.0
    b = raw - raw.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA alignment / stacking score across 21/63/252 (bullish stacking)
def f01ts_f01_trend_structure_stack_21_63_252_base_v018_signal(closeadj):
    b = _f01_stack3(closeadj, 21, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA alignment / stacking score across 21/63/126
def f01ts_f01_trend_structure_stack_21_63_126_base_v019_signal(closeadj):
    b = _f01_stack3(closeadj, 21, 63, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA alignment / stacking score across 63/126/252
def f01ts_f01_trend_structure_stack_63_126_252_base_v020_signal(closeadj):
    b = _f01_stack3(closeadj, 63, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stacking persistence: bull-stack fraction over a quarter weighted by current stack depth
def f01ts_f01_trend_structure_stackpersist_63d_base_v021_signal(closeadj):
    st = _f01_stack3(closeadj, 21, 63, 252)
    full = (st > 0).astype(float)
    frac = full.rolling(63, min_periods=21).mean()
    b = frac * st.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 63d that price closed above its 63d SMA (% above MA)
def f01ts_f01_trend_structure_abovefrac_63d_base_v022_signal(closeadj):
    b = _f01_above_frac(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 126d above the 126d SMA
def f01ts_f01_trend_structure_abovefrac_126d_base_v023_signal(closeadj):
    b = _f01_above_frac(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 252d above the 252d SMA
def f01ts_f01_trend_structure_abovefrac_252d_base_v024_signal(closeadj):
    b = _f01_above_frac(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression trend slope of log-price over 63d
def f01ts_f01_trend_structure_slope_63d_base_v025_signal(closeadj):
    b = _f01_slope(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression trend slope of log-price over 126d
def f01ts_f01_trend_structure_slope_126d_base_v026_signal(closeadj):
    b = _f01_slope(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression trend slope of log-price over 252d
def f01ts_f01_trend_structure_slope_252d_base_v027_signal(closeadj):
    b = _f01_slope(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression trend slope over 21d
def f01ts_f01_trend_structure_slope_21d_base_v028_signal(closeadj):
    b = _f01_slope(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend quality: regression R^2 over 63d (how clean the trend is)
def f01ts_f01_trend_structure_sloper2_63d_base_v029_signal(closeadj):
    b = _f01_slope_r2(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend quality: regression R^2 over 126d
def f01ts_f01_trend_structure_sloper2_126d_base_v030_signal(closeadj):
    b = _f01_slope_r2(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend quality: regression R^2 over 252d
def f01ts_f01_trend_structure_sloper2_252d_base_v031_signal(closeadj):
    b = _f01_slope_r2(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope t-stat over 63d, demeaned by its own 126d average (de-trended trend significance)
def f01ts_f01_trend_structure_slopet_63d_base_v032_signal(closeadj):
    t = _f01_slope_tstat(closeadj, 63)
    b = t - t.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope t-stat over 126d
def f01ts_f01_trend_structure_slopet_126d_base_v033_signal(closeadj):
    b = _f01_slope_tstat(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope t-stat over 252d, percentile-ranked vs its own 504d history (trend-significance regime)
def f01ts_f01_trend_structure_slopet_252d_base_v034_signal(closeadj):
    t = _f01_slope_tstat(closeadj, 252)
    b = t.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend cleanliness change: 63d R^2 now minus a month ago, signed by slope (trend forming/decaying)
def f01ts_f01_trend_structure_slopequal_63d_base_v035_signal(closeadj):
    r2 = _f01_slope_r2(closeadj, 63)
    sl = _f01_slope(closeadj, 63)
    b = (r2 - r2.shift(21)) * np.sign(sl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-quality direction over 252d: sign of slope times R^2 (clean-trend conviction, slope-free)
def f01ts_f01_trend_structure_slopequal_252d_base_v036_signal(closeadj):
    sl = _f01_slope(closeadj, 252)
    r2 = _f01_slope_r2(closeadj, 252)
    b = np.sign(sl) * r2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MACD (21/63) level normalized by price (classic trend oscillator)
def f01ts_f01_trend_structure_macd_21v63_base_v037_signal(closeadj):
    macd = _f01_macd(closeadj, 21, 63)
    b = macd / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MACD (63/126) normalized by price
def f01ts_f01_trend_structure_macd_63v126_base_v038_signal(closeadj):
    macd = _f01_macd(closeadj, 63, 126)
    b = macd / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MACD histogram (MACD minus its 21d signal EMA), 21/63
def f01ts_f01_trend_structure_macdhist_21v63_base_v039_signal(closeadj):
    macd = _f01_macd(closeadj, 21, 63)
    sig = macd.ewm(span=21, min_periods=10).mean()
    b = (macd - sig) / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MACD histogram 63/126 with 42d signal
def f01ts_f01_trend_structure_macdhist_63v126_base_v040_signal(closeadj):
    macd = _f01_macd(closeadj, 63, 126)
    sig = macd.ewm(span=42, min_periods=21).mean()
    b = (macd - sig) / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-vs-63d-MA persistence: signed run-length of consecutive days on one side
def f01ts_f01_trend_structure_mapersist_63d_base_v041_signal(closeadj):
    ma = _f01_sma(closeadj, 63)
    sign = np.sign(closeadj - ma)
    grp = (sign != sign.shift(1)).cumsum()
    run = sign.groupby(grp).cumcount() + 1
    b = sign * run / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-vs-252d-MA persistence run-length (signed, normalized)
def f01ts_f01_trend_structure_mapersist_252d_base_v042_signal(closeadj):
    ma = _f01_sma(closeadj, 252)
    sign = np.sign(closeadj - ma)
    grp = (sign != sign.shift(1)).cumsum()
    run = sign.groupby(grp).cumcount() + 1
    b = sign * run / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direction agreement: tanh-magnitude-weighted average of 21/63/126/252 slopes (consensus)
def f01ts_f01_trend_structure_slopeconsensus_base_v043_signal(closeadj):
    s1 = np.tanh(200.0 * _f01_slope(closeadj, 21))
    s2 = np.tanh(200.0 * _f01_slope(closeadj, 63))
    s3 = np.tanh(200.0 * _f01_slope(closeadj, 126))
    s4 = np.tanh(200.0 * _f01_slope(closeadj, 252))
    b = (s1 + s2 + s3 + s4) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope term structure: short slope minus long slope (trend acceleration via windows)
def f01ts_f01_trend_structure_slopeterm_21v252_base_v044_signal(closeadj):
    s_short = _f01_slope(closeadj, 21)
    s_long = _f01_slope(closeadj, 252)
    b = s_short - s_long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope term structure: 63d slope minus 126d slope
def f01ts_f01_trend_structure_slopeterm_63v126_base_v045_signal(closeadj):
    b = _f01_slope(closeadj, 63) - _f01_slope(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA convergence/divergence: dispersion of 21/63/126/252 SMAs around price (fan width)
def f01ts_f01_trend_structure_fanwidth_base_v046_signal(closeadj):
    m1 = _f01_sma(closeadj, 21)
    m2 = _f01_sma(closeadj, 63)
    m3 = _f01_sma(closeadj, 126)
    m4 = _f01_sma(closeadj, 252)
    stacked = pd.concat([m1, m2, m3, m4], axis=1)
    b = (stacked.max(axis=1) - stacked.min(axis=1)) / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA ribbon compression: fan width now relative to its own 126d average (squeeze)
def f01ts_f01_trend_structure_fancompress_base_v047_signal(closeadj):
    m1 = _f01_sma(closeadj, 21)
    m2 = _f01_sma(closeadj, 63)
    m3 = _f01_sma(closeadj, 252)
    stacked = pd.concat([m1, m2, m3], axis=1)
    fw = (stacked.max(axis=1) - stacked.min(axis=1)) / closeadj.replace(0, np.nan)
    b = fw / fw.rolling(126, min_periods=63).mean().replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 63d SMA itself (MA direction, normalized per bar)
def f01ts_f01_trend_structure_maslope_63d_base_v048_signal(closeadj):
    ma = _f01_sma(closeadj, 63)
    b = ma / ma.shift(21).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 252d SMA over a quarter (long MA direction)
def f01ts_f01_trend_structure_maslope_252d_base_v049_signal(closeadj):
    ma = _f01_sma(closeadj, 252)
    b = ma / ma.shift(63).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 126d SMA over a month
def f01ts_f01_trend_structure_maslope_126d_base_v050_signal(closeadj):
    ma = _f01_sma(closeadj, 126)
    b = ma / ma.shift(21).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# golden-cross freshness: days since 63d SMA crossed above 252d SMA (recency)
def f01ts_f01_trend_structure_goldenfresh_base_v051_signal(closeadj):
    m1 = _f01_sma(closeadj, 63)
    m2 = _f01_sma(closeadj, 252)
    bull = (m1 > m2).astype(float)
    cross_up = ((bull == 1) & (bull.shift(1) == 0)).astype(float)
    grp = cross_up.cumsum()
    since = bull.groupby(grp).cumcount().astype(float)
    b = np.where(bull == 1, np.exp(-since / 63.0), -np.exp(-since / 63.0))
    result = pd.Series(b, index=closeadj.index)
    return result.replace([np.inf, -np.inf], np.nan)


# above/below 252d SMA streak entropy: how decisively price sits on one side (63d)
def f01ts_f01_trend_structure_sidebias_252d_base_v052_signal(closeadj):
    ma = _f01_sma(closeadj, 252)
    above = (closeadj > ma).astype(float)
    p = above.rolling(63, min_periods=21).mean()
    b = (p - 0.5) * 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance to 63d SMA, percentile-ranked vs its own 252d history
def f01ts_f01_trend_structure_pxmarank_63d_base_v053_signal(closeadj):
    d = _f01_pxma(closeadj, 63)
    b = d.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance to 252d SMA, percentile-ranked vs 504d history
def f01ts_f01_trend_structure_pxmarank_252d_base_v054_signal(closeadj):
    d = _f01_pxma(closeadj, 252)
    b = d.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend smoothness: realized path length vs net displacement over 63d (efficiency)
def f01ts_f01_trend_structure_patheff_63d_base_v055_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    net = (lp - lp.shift(63)).abs()
    gross = lp.diff().abs().rolling(63, min_periods=21).sum()
    eff = net / gross.replace(0, np.nan)
    b = eff * np.sign(lp - lp.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed trend efficiency over 126d
def f01ts_f01_trend_structure_patheff_126d_base_v056_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    net = (lp - lp.shift(126)).abs()
    gross = lp.diff().abs().rolling(126, min_periods=63).sum()
    eff = net / gross.replace(0, np.nan)
    b = eff * np.sign(lp - lp.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EMA vs SMA divergence at 63d (where exponential weighting leads the simple average)
def f01ts_f01_trend_structure_emasmadiv_63d_base_v057_signal(closeadj):
    e = _f01_ema(closeadj, 63)
    s = _f01_sma(closeadj, 63)
    b = e / s.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed price-vs-126d-MA distance (bounded trend extension)
def f01ts_f01_trend_structure_pxmatanh_126d_base_v058_signal(closeadj):
    d = _f01_pxma(closeadj, 126)
    b = np.tanh(10.0 * d)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x magnitude of price-vs-252d-MA (concave-emphasized trend distance)
def f01ts_f01_trend_structure_pxmasm_252d_base_v059_signal(closeadj):
    d = _f01_pxma(closeadj, 252)
    b = np.sign(d) * np.sqrt(d.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope momentum: change in 63d slope over a month (trend turning)
def f01ts_f01_trend_structure_slopemom_63d_base_v060_signal(closeadj):
    sl = _f01_slope(closeadj, 63)
    b = sl - sl.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope momentum over a quarter, 126d slope
def f01ts_f01_trend_structure_slopemom_126d_base_v061_signal(closeadj):
    sl = _f01_slope(closeadj, 126)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-trend stretch extremity: distance to 21d EMA in vol units, ranked vs 126d history
def f01ts_f01_trend_structure_emastretch_21d_base_v062_signal(closeadj):
    d = _f01_pxema(closeadj, 21)
    vol = closeadj.pct_change().rolling(21, min_periods=10).std()
    stretch = d / vol.replace(0, np.nan)
    b = stretch.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-distance term-structure tilt: short-MA distance minus long-MA distance (trend curvature
# across the ribbon), capturing whether price is pulling away faster from near or far MAs
def f01ts_f01_trend_structure_macount_base_v063_signal(closeadj):
    d1 = _f01_pxma(closeadj, 21)
    d2 = _f01_pxma(closeadj, 63)
    d3 = _f01_pxma(closeadj, 126)
    d4 = _f01_pxma(closeadj, 252)
    b = (d1 - d2) - (d3 - d4)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-count persistence: smoothed breadth of trend support over a quarter
def f01ts_f01_trend_structure_macountsm_base_v064_signal(closeadj):
    c1 = (closeadj > _f01_sma(closeadj, 21)).astype(float)
    c2 = (closeadj > _f01_sma(closeadj, 63)).astype(float)
    c3 = (closeadj > _f01_sma(closeadj, 252)).astype(float)
    cnt = (c1 + c2 + c3) / 3.0
    b = cnt.ewm(span=42, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope dispersion: std of 21/63/126/252 slopes (trend coherence; low=coherent)
def f01ts_f01_trend_structure_slopedisp_base_v065_signal(closeadj):
    s1 = _f01_slope(closeadj, 21)
    s2 = _f01_slope(closeadj, 63)
    s3 = _f01_slope(closeadj, 126)
    s4 = _f01_slope(closeadj, 252)
    b = pd.concat([s1, s2, s3, s4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MACD-hist persistence: fraction of last quarter MACD-hist was positive
def f01ts_f01_trend_structure_macdhistpos_base_v066_signal(closeadj):
    macd = _f01_macd(closeadj, 21, 63)
    sig = macd.ewm(span=21, min_periods=10).mean()
    hist = macd - sig
    pos = (hist > 0).astype(float)
    b = pos.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-vs-noise ratio: 126d slope per unit of 63d vol, percentile-ranked vs 252d history
def f01ts_f01_trend_structure_trendsnr_126d_base_v067_signal(closeadj):
    sl = _f01_slope(closeadj, 126)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    snr = sl / vol.replace(0, np.nan)
    b = snr.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# above-MA breadth asymmetry: time above 63d MA minus time below, year window
def f01ts_f01_trend_structure_aboveasym_252d_base_v068_signal(closeadj):
    ma = _f01_sma(closeadj, 63)
    above = (closeadj > ma).astype(float)
    frac = above.rolling(252, min_periods=126).mean()
    b = 2.0 * frac - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance between price and 252d EMA, z-scored vs own 126d history
def f01ts_f01_trend_structure_pxemaz_252d_base_v069_signal(closeadj):
    d = _f01_pxema(closeadj, 252)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# golden-cross conviction: 63v252 SMA gap z-scored vs its own 504d history (cross extremity)
def f01ts_f01_trend_structure_goldengap_base_v070_signal(closeadj):
    m1 = _f01_sma(closeadj, 63)
    m2 = _f01_sma(closeadj, 252)
    gap = m1 / m2.replace(0, np.nan) - 1.0
    b = _z(gap, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of price relative to its 63d MA (2nd-diff of the gap over a month)
def f01ts_f01_trend_structure_pxmacurve_63d_base_v071_signal(closeadj):
    d = _f01_pxma(closeadj, 63)
    b = d - 2.0 * d.shift(21) + d.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EMA-ribbon ordering coherence: each consecutive EMA gap squashed by its own scale, then
# averaged -- isolates whether the fan is *cleanly ordered* rather than how wide it is
def f01ts_f01_trend_structure_emaorder_base_v072_signal(closeadj):
    e1 = _f01_ema(closeadj, 21)
    e2 = _f01_ema(closeadj, 63)
    e3 = _f01_ema(closeadj, 126)
    e4 = _f01_ema(closeadj, 252)
    g12 = e1 / e2.replace(0, np.nan) - 1.0
    g23 = e2 / e3.replace(0, np.nan) - 1.0
    g34 = e3 / e4.replace(0, np.nan) - 1.0
    n12 = np.tanh(g12 / g12.rolling(126, min_periods=42).std().replace(0, np.nan))
    n23 = np.tanh(g23 / g23.rolling(126, min_periods=42).std().replace(0, np.nan))
    n34 = np.tanh(g34 / g34.rolling(126, min_periods=42).std().replace(0, np.nan))
    b = (n12 + n23 + n34) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend strength index: |price - 252d MA| smoothed, signed (ADX-like directional energy)
def f01ts_f01_trend_structure_tsi_252d_base_v073_signal(closeadj):
    d = _f01_pxma(closeadj, 252)
    b = d.abs().ewm(span=42, min_periods=21).mean() * np.sign(d)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope t-stat consensus: significance-gated average of soft-clipped t-stats across windows
def f01ts_f01_trend_structure_slopetcons_base_v074_signal(closeadj):
    t1 = _f01_slope_tstat(closeadj, 63)
    t2 = _f01_slope_tstat(closeadj, 126)
    t3 = _f01_slope_tstat(closeadj, 252)
    s1 = np.tanh(t1 / 3.0) * (t1.abs() > 2.0).astype(float)
    s2 = np.tanh(t2 / 3.0) * (t2.abs() > 2.0).astype(float)
    s3 = np.tanh(t3 / 3.0) * (t3.abs() > 2.0).astype(float)
    b = (s1 + s2 + s3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-distance interaction with dollar-volume trend (trend confirmed by liquidity)
def f01ts_f01_trend_structure_pxmadvol_63d_base_v075_signal(closeadj, volume):
    d = _f01_pxma(closeadj, 63)
    dvol = (closeadj * volume)
    dvol_z = _z(dvol, 63)
    b = d * dvol_z
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01ts_f01_trend_structure_pxma_21d_base_v001_signal,
    f01ts_f01_trend_structure_pxma_63d_base_v002_signal,
    f01ts_f01_trend_structure_pxma_126d_base_v003_signal,
    f01ts_f01_trend_structure_pxma_252d_base_v004_signal,
    f01ts_f01_trend_structure_pxema_21d_base_v005_signal,
    f01ts_f01_trend_structure_pxema_63d_base_v006_signal,
    f01ts_f01_trend_structure_pxema_252d_base_v007_signal,
    f01ts_f01_trend_structure_pxmaz_21d_base_v008_signal,
    f01ts_f01_trend_structure_pxmaz_63d_base_v009_signal,
    f01ts_f01_trend_structure_pxmaz_252d_base_v010_signal,
    f01ts_f01_trend_structure_pxmavol_63d_base_v011_signal,
    f01ts_f01_trend_structure_maspr_21v63_base_v012_signal,
    f01ts_f01_trend_structure_maspr_63v126_base_v013_signal,
    f01ts_f01_trend_structure_maspr_63v252_base_v014_signal,
    f01ts_f01_trend_structure_maspr_21v252_base_v015_signal,
    f01ts_f01_trend_structure_emaspr_21v63_base_v016_signal,
    f01ts_f01_trend_structure_emaspr_63v126_base_v017_signal,
    f01ts_f01_trend_structure_stack_21_63_252_base_v018_signal,
    f01ts_f01_trend_structure_stack_21_63_126_base_v019_signal,
    f01ts_f01_trend_structure_stack_63_126_252_base_v020_signal,
    f01ts_f01_trend_structure_stackpersist_63d_base_v021_signal,
    f01ts_f01_trend_structure_abovefrac_63d_base_v022_signal,
    f01ts_f01_trend_structure_abovefrac_126d_base_v023_signal,
    f01ts_f01_trend_structure_abovefrac_252d_base_v024_signal,
    f01ts_f01_trend_structure_slope_63d_base_v025_signal,
    f01ts_f01_trend_structure_slope_126d_base_v026_signal,
    f01ts_f01_trend_structure_slope_252d_base_v027_signal,
    f01ts_f01_trend_structure_slope_21d_base_v028_signal,
    f01ts_f01_trend_structure_sloper2_63d_base_v029_signal,
    f01ts_f01_trend_structure_sloper2_126d_base_v030_signal,
    f01ts_f01_trend_structure_sloper2_252d_base_v031_signal,
    f01ts_f01_trend_structure_slopet_63d_base_v032_signal,
    f01ts_f01_trend_structure_slopet_126d_base_v033_signal,
    f01ts_f01_trend_structure_slopet_252d_base_v034_signal,
    f01ts_f01_trend_structure_slopequal_63d_base_v035_signal,
    f01ts_f01_trend_structure_slopequal_252d_base_v036_signal,
    f01ts_f01_trend_structure_macd_21v63_base_v037_signal,
    f01ts_f01_trend_structure_macd_63v126_base_v038_signal,
    f01ts_f01_trend_structure_macdhist_21v63_base_v039_signal,
    f01ts_f01_trend_structure_macdhist_63v126_base_v040_signal,
    f01ts_f01_trend_structure_mapersist_63d_base_v041_signal,
    f01ts_f01_trend_structure_mapersist_252d_base_v042_signal,
    f01ts_f01_trend_structure_slopeconsensus_base_v043_signal,
    f01ts_f01_trend_structure_slopeterm_21v252_base_v044_signal,
    f01ts_f01_trend_structure_slopeterm_63v126_base_v045_signal,
    f01ts_f01_trend_structure_fanwidth_base_v046_signal,
    f01ts_f01_trend_structure_fancompress_base_v047_signal,
    f01ts_f01_trend_structure_maslope_63d_base_v048_signal,
    f01ts_f01_trend_structure_maslope_252d_base_v049_signal,
    f01ts_f01_trend_structure_maslope_126d_base_v050_signal,
    f01ts_f01_trend_structure_goldenfresh_base_v051_signal,
    f01ts_f01_trend_structure_sidebias_252d_base_v052_signal,
    f01ts_f01_trend_structure_pxmarank_63d_base_v053_signal,
    f01ts_f01_trend_structure_pxmarank_252d_base_v054_signal,
    f01ts_f01_trend_structure_patheff_63d_base_v055_signal,
    f01ts_f01_trend_structure_patheff_126d_base_v056_signal,
    f01ts_f01_trend_structure_emasmadiv_63d_base_v057_signal,
    f01ts_f01_trend_structure_pxmatanh_126d_base_v058_signal,
    f01ts_f01_trend_structure_pxmasm_252d_base_v059_signal,
    f01ts_f01_trend_structure_slopemom_63d_base_v060_signal,
    f01ts_f01_trend_structure_slopemom_126d_base_v061_signal,
    f01ts_f01_trend_structure_emastretch_21d_base_v062_signal,
    f01ts_f01_trend_structure_macount_base_v063_signal,
    f01ts_f01_trend_structure_macountsm_base_v064_signal,
    f01ts_f01_trend_structure_slopedisp_base_v065_signal,
    f01ts_f01_trend_structure_macdhistpos_base_v066_signal,
    f01ts_f01_trend_structure_trendsnr_126d_base_v067_signal,
    f01ts_f01_trend_structure_aboveasym_252d_base_v068_signal,
    f01ts_f01_trend_structure_pxemaz_252d_base_v069_signal,
    f01ts_f01_trend_structure_goldengap_base_v070_signal,
    f01ts_f01_trend_structure_pxmacurve_63d_base_v071_signal,
    f01ts_f01_trend_structure_emaorder_base_v072_signal,
    f01ts_f01_trend_structure_tsi_252d_base_v073_signal,
    f01ts_f01_trend_structure_slopetcons_base_v074_signal,
    f01ts_f01_trend_structure_pxmadvol_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_TREND_STRUCTURE_REGISTRY_001_075 = REGISTRY


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

    print("OK f01_trend_structure_base_001_075_claude: %d features pass" % n_features)
