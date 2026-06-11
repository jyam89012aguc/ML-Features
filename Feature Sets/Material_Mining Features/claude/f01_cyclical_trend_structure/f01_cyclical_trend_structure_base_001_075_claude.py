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


def _f01_pdist(close, w):
    # price distance above/below the w-day MA (log)
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.log(close.replace(0, np.nan) / ma.replace(0, np.nan))


def _f01_pdistz(close, w, zw):
    # distance-from-MA z-scored vs its own history
    d = _f01_pdist(close, w)
    return _z(d, zw)


def _f01_maslope(close, w, k):
    # log slope of the w-day MA over k days (multi-year trend direction)
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.log(ma.replace(0, np.nan) / ma.shift(k).replace(0, np.nan)) / float(k)


def _f01_above_frac(close, w, ow):
    # fraction of last ow days spent above the w-day MA (trend persistence)
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    above = (close > ma).astype(float)
    return above.rolling(ow, min_periods=max(1, ow // 2)).mean()


def _f01_maratio(close, ws, wl):
    # short MA vs long MA (stacking / golden-cross magnitude, log)
    ms = close.rolling(ws, min_periods=max(1, ws // 2)).mean()
    ml = close.rolling(wl, min_periods=max(1, wl // 2)).mean()
    return np.log(ms.replace(0, np.nan) / ml.replace(0, np.nan))


def _f01_stack_score(close):
    # MA-stacking score: how many of the 21<63<126<252<504 orderings hold (Perfect order)
    m21 = close.rolling(21, min_periods=10).mean()
    m63 = close.rolling(63, min_periods=31).mean()
    m126 = close.rolling(126, min_periods=63).mean()
    m252 = close.rolling(252, min_periods=126).mean()
    m504 = close.rolling(504, min_periods=252).mean()
    s = (m21 > m63).astype(float) + (m63 > m126).astype(float) \
        + (m126 > m252).astype(float) + (m252 > m504).astype(float)
    return s


def _f01_stack_mag(close):
    # magnitude-weighted MA-stacking quality: sum of bounded (tanh) adjacent MA log-gaps.
    # tanh removes raw price-level scaling so it measures ordering quality, not trend level.
    m21 = close.rolling(21, min_periods=10).mean()
    m63 = close.rolling(63, min_periods=31).mean()
    m126 = close.rolling(126, min_periods=63).mean()
    m252 = close.rolling(252, min_periods=126).mean()
    m504 = close.rolling(504, min_periods=252).mean()
    g1 = np.tanh(80.0 * np.log(m21.replace(0, np.nan) / m63.replace(0, np.nan)))
    g2 = np.tanh(80.0 * np.log(m63.replace(0, np.nan) / m126.replace(0, np.nan)))
    g3 = np.tanh(80.0 * np.log(m126.replace(0, np.nan) / m252.replace(0, np.nan)))
    g4 = np.tanh(80.0 * np.log(m252.replace(0, np.nan) / m504.replace(0, np.nan)))
    return g1 + g2 + g3 + g4


def _f01_trendpersist(close, w, ow):
    # signed persistence: avg sign of MA-distance over ow days
    d = _f01_pdist(close, w)
    return np.sign(d).rolling(ow, min_periods=max(1, ow // 2)).mean()


def _f01_streak_above(close, w):
    # current consecutive-days streak above the w-day MA, normalized by w
    ma = close.rolling(w, min_periods=max(1, w // 2)).mean()
    above = (close > ma).astype(float)
    grp = (above != above.shift(1)).cumsum()
    streak = above.groupby(grp).cumcount() + 1
    return (streak * above) / float(w)


# ============================================================
# price vs 21d MA (log distance)
def f01ct_f01_cyclical_trend_structure_pdist_21d_base_v001_signal(closeadj):
    b = _f01_pdist(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 63d MA (log distance)
def f01ct_f01_cyclical_trend_structure_pdist_63d_base_v002_signal(closeadj):
    b = _f01_pdist(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 126d MA (log distance)
def f01ct_f01_cyclical_trend_structure_pdist_126d_base_v003_signal(closeadj):
    b = _f01_pdist(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 252d MA (log distance, primary long-trend gauge)
def f01ct_f01_cyclical_trend_structure_pdist_252d_base_v004_signal(closeadj):
    b = _f01_pdist(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs 504d MA (multi-year trend distance)
def f01ct_f01_cyclical_trend_structure_pdist_504d_base_v005_signal(closeadj):
    b = _f01_pdist(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 63d MA z-scored vs its own 252d history
def f01ct_f01_cyclical_trend_structure_pdistz_63d_base_v006_signal(closeadj):
    b = _f01_pdistz(closeadj, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 126d MA z-scored vs its own 252d history
def f01ct_f01_cyclical_trend_structure_pdistz_126d_base_v007_signal(closeadj):
    b = _f01_pdistz(closeadj, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 252d MA z-scored vs its own 504d history (cyclical extension)
def f01ct_f01_cyclical_trend_structure_pdistz_252d_base_v008_signal(closeadj):
    b = _f01_pdistz(closeadj, 252, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 504d MA z-scored vs its own 504d history
def f01ct_f01_cyclical_trend_structure_pdistz_504d_base_v009_signal(closeadj):
    b = _f01_pdistz(closeadj, 504, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MA log-slope over a month (fast trend direction)
def f01ct_f01_cyclical_trend_structure_maslope_21d_base_v010_signal(closeadj):
    b = _f01_maslope(closeadj, 21, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d MA log-slope over a quarter
def f01ct_f01_cyclical_trend_structure_maslope_63d_base_v011_signal(closeadj):
    b = _f01_maslope(closeadj, 63, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d MA log-slope over a quarter (intermediate trend)
def f01ct_f01_cyclical_trend_structure_maslope_126d_base_v012_signal(closeadj):
    b = _f01_maslope(closeadj, 126, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MA log-slope over a quarter (multi-year trend direction)
def f01ct_f01_cyclical_trend_structure_maslope_252d_base_v013_signal(closeadj):
    b = _f01_maslope(closeadj, 252, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d MA log-slope over a half-year (deep-cycle trend direction)
def f01ct_f01_cyclical_trend_structure_maslope_504d_base_v014_signal(closeadj):
    b = _f01_maslope(closeadj, 504, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA stacking magnitude (signed sum of adjacent MA log-gaps, 21>63>126>252>504)
def f01ct_f01_cyclical_trend_structure_stack_base_v015_signal(closeadj):
    b = _f01_stack_mag(closeadj)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year spent above the 200d-ish (252d) MA (% above long MA)
def f01ct_f01_cyclical_trend_structure_abovefrac_252d_base_v016_signal(closeadj):
    b = _f01_above_frac(closeadj, 252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last half-year spent above the 126d MA
def f01ct_f01_cyclical_trend_structure_abovefrac_126d_base_v017_signal(closeadj):
    b = _f01_above_frac(closeadj, 126, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 2y spent above the 504d MA (long persistence)
def f01ct_f01_cyclical_trend_structure_abovefrac_504d_base_v018_signal(closeadj):
    b = _f01_above_frac(closeadj, 504, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MA vs 63d MA ratio (short stacking magnitude)
def f01ct_f01_cyclical_trend_structure_maratio_21v63_base_v019_signal(closeadj):
    b = _f01_maratio(closeadj, 21, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-vs-126d MA cross, z-scored vs its own 252d history (intermediate stacking extremity)
def f01ct_f01_cyclical_trend_structure_maratio_63v126_base_v020_signal(closeadj):
    r = _f01_maratio(closeadj, 63, 126)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d MA vs 252d MA ratio (intermediate vs long stacking)
def f01ct_f01_cyclical_trend_structure_maratio_126v252_base_v021_signal(closeadj):
    b = _f01_maratio(closeadj, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MA vs 504d MA ratio (golden/death cross of the slow MAs)
def f01ct_f01_cyclical_trend_structure_maratio_252v504_base_v022_signal(closeadj):
    b = _f01_maratio(closeadj, 252, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MA vs 252d MA ratio (full short-vs-long spread)
def f01ct_f01_cyclical_trend_structure_maratio_21v252_base_v023_signal(closeadj):
    b = _f01_maratio(closeadj, 21, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed trend persistence vs 63d MA over a quarter (avg sign of distance)
def f01ct_f01_cyclical_trend_structure_persist_63d_base_v024_signal(closeadj):
    b = _f01_trendpersist(closeadj, 63, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# (kept sign-based at 63d; the 252d sibling is depth-weighted to stay distinct)


# depth-weighted trend persistence vs 252d MA over a year (avg signed magnitude of distance)
def f01ct_f01_cyclical_trend_structure_persist_252d_base_v025_signal(closeadj):
    d = _f01_pdist(closeadj, 252)
    b = d.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current consecutive-days streak above the 126d MA (normalized)
def f01ct_f01_cyclical_trend_structure_streak_126d_base_v026_signal(closeadj):
    b = _f01_streak_above(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current consecutive-days streak above the 252d MA (normalized)
def f01ct_f01_cyclical_trend_structure_streak_252d_base_v027_signal(closeadj):
    b = _f01_streak_above(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-distance dispersion across the 5 MAs (trend agreement/disagreement)
def f01ct_f01_cyclical_trend_structure_madisp_base_v028_signal(closeadj):
    d21 = _f01_pdist(closeadj, 21)
    d63 = _f01_pdist(closeadj, 63)
    d126 = _f01_pdist(closeadj, 126)
    d252 = _f01_pdist(closeadj, 252)
    d504 = _f01_pdist(closeadj, 504)
    b = pd.concat([d21, d63, d126, d252, d504], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope breadth: magnitude-weighted agreement of the 5 MA slopes (sum of bounded slopes)
def f01ct_f01_cyclical_trend_structure_slopebreadth_base_v029_signal(closeadj):
    s21 = _f01_maslope(closeadj, 21, 21)
    s63 = _f01_maslope(closeadj, 63, 21)
    s126 = _f01_maslope(closeadj, 126, 21)
    s252 = _f01_maslope(closeadj, 252, 21)
    s504 = _f01_maslope(closeadj, 504, 21)
    b = np.tanh(50.0 * s21) + np.tanh(50.0 * s63) + np.tanh(50.0 * s126) \
        + np.tanh(50.0 * s252) + np.tanh(50.0 * s504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-252d-MA percentile-ranked vs its own 504d history
def f01ct_f01_cyclical_trend_structure_pdistrank_252d_base_v030_signal(closeadj):
    d = _f01_pdist(closeadj, 252)
    b = d.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-126d-MA percentile-ranked vs its own 252d history
def f01ct_f01_cyclical_trend_structure_pdistrank_126d_base_v031_signal(closeadj):
    d = _f01_pdist(closeadj, 126)
    b = d.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-distance momentum: change in price-vs-252d-MA over a quarter
def f01ct_f01_cyclical_trend_structure_pdistmom_252d_base_v032_signal(closeadj):
    d = _f01_pdist(closeadj, 252)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-distance momentum: change in price-vs-126d-MA over a month
def f01ct_f01_cyclical_trend_structure_pdistmom_126d_base_v033_signal(closeadj):
    d = _f01_pdist(closeadj, 126)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d MA-slope risk-adjusted by realized vol, percentile-ranked vs 504d history
def f01ct_f01_cyclical_trend_structure_slopevol_252d_base_v034_signal(closeadj):
    sl = _f01_maslope(closeadj, 252, 63)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    ratio = sl / vol.replace(0, np.nan)
    b = ratio.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d MA-slope risk-adjusted by realized vol, percentile-ranked vs 252d history
def f01ct_f01_cyclical_trend_structure_slopevol_63d_base_v035_signal(closeadj):
    sl = _f01_maslope(closeadj, 63, 21)
    vol = closeadj.pct_change().rolling(21, min_periods=10).std()
    ratio = sl / vol.replace(0, np.nan)
    b = ratio.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stacking-score persistence: avg stack score over the last quarter
def f01ct_f01_cyclical_trend_structure_stackpersist_base_v036_signal(closeadj):
    s = _f01_stack_score(closeadj)
    b = s.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend efficiency: net 252d MA move / sum of |MA daily moves| (smoothness of trend)
def f01ct_f01_cyclical_trend_structure_efficiency_252d_base_v037_signal(closeadj):
    ma = _f01_ma(closeadj, 252)
    net = (ma - ma.shift(126)).abs()
    path = ma.diff().abs().rolling(126, min_periods=63).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend efficiency over 63d MA (intermediate trend smoothness)
def f01ct_f01_cyclical_trend_structure_efficiency_63d_base_v038_signal(closeadj):
    ma = _f01_ma(closeadj, 63)
    net = (ma - ma.shift(63)).abs()
    path = ma.diff().abs().rolling(63, min_periods=31).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# golden-cross distance with sign x magnitude (21v252 spread, sqrt-scaled)
def f01ct_f01_cyclical_trend_structure_crossmag_21v252_base_v039_signal(closeadj):
    r = _f01_maratio(closeadj, 21, 252)
    b = np.sign(r) * (r.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convexity of the MA ladder: spread(21-63) minus spread(252-504) (curvature of stack)
def f01ct_f01_cyclical_trend_structure_ladderconv_base_v040_signal(closeadj):
    near = _f01_maratio(closeadj, 21, 63)
    far = _f01_maratio(closeadj, 252, 504)
    b = near - far
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 252d MA in ATR units, demeaned vs its own quarter (overextension impulse)
def f01ct_f01_cyclical_trend_structure_pdistatr_252d_base_v041_signal(closeadj):
    ma = _f01_ma(closeadj, 252)
    atr = closeadj.diff().abs().rolling(21, min_periods=10).mean()
    kc = (closeadj - ma) / atr.replace(0, np.nan)
    b = kc - kc.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Keltner-style position: distance above 63d MA in ATR units, ranked vs 252d history
def f01ct_f01_cyclical_trend_structure_pdistatr_63d_base_v042_signal(closeadj):
    ma = _f01_ma(closeadj, 63)
    atr = closeadj.diff().abs().rolling(21, min_periods=10).mean()
    kc = (closeadj - ma) / atr.replace(0, np.nan)
    b = kc.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed price-vs-252d-MA distance (bounded trend extension)
def f01ct_f01_cyclical_trend_structure_pdisttanh_252d_base_v043_signal(closeadj):
    d = _f01_pdist(closeadj, 252)
    b = np.tanh(4.0 * d)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend persistence streak above 63d MA (normalized)
def f01ct_f01_cyclical_trend_structure_streak_63d_base_v044_signal(closeadj):
    b = _f01_streak_above(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in stacking magnitude over a quarter (stack building/unwinding)
def f01ct_f01_cyclical_trend_structure_stackmom_base_v045_signal(closeadj):
    s = _f01_stack_mag(closeadj)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# % above 252d MA minus % above 63d MA (long vs short persistence spread)
def f01ct_f01_cyclical_trend_structure_abovespr_base_v046_signal(closeadj):
    a_long = _f01_above_frac(closeadj, 252, 252)
    a_short = _f01_above_frac(closeadj, 63, 63)
    b = a_long - a_short
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-MA z spread: 63d z minus 252d z (short stretch vs long stretch)
def f01ct_f01_cyclical_trend_structure_distzspr_base_v047_signal(closeadj):
    z_s = _f01_pdistz(closeadj, 63, 252)
    z_l = _f01_pdistz(closeadj, 252, 504)
    b = z_s - z_l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deep-cycle trend inflection: 504d MA-slope minus its own slow EMA (slope displacement)
def f01ct_f01_cyclical_trend_structure_slopesm_504d_base_v048_signal(closeadj):
    sl = _f01_maslope(closeadj, 504, 63)
    b = sl - sl.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 21d MA z-scored vs its own 126d history (short overextension)
def f01ct_f01_cyclical_trend_structure_pdistz_21d_base_v049_signal(closeadj):
    b = _f01_pdistz(closeadj, 21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slow-MA bundle convexity: mean pdist(126/252/504) minus the 252d pdist (long-trend bow)
def f01ct_f01_cyclical_trend_structure_slowbundle_base_v050_signal(closeadj):
    d126 = _f01_pdist(closeadj, 126)
    d252 = _f01_pdist(closeadj, 252)
    d504 = _f01_pdist(closeadj, 504)
    bundle = pd.concat([d126, d252, d504], axis=1).mean(axis=1)
    b = bundle - d252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA convexity: 2*MA63 - MA21 - MA126 normalized (curvature of trend in MA space)
def f01ct_f01_cyclical_trend_structure_curv_63d_base_v051_signal(closeadj):
    m21 = _f01_ma(closeadj, 21)
    m63 = _f01_ma(closeadj, 63)
    m126 = _f01_ma(closeadj, 126)
    b = (2.0 * m63 - m21 - m126) / m63.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA convexity at the long end: 2*MA252 - MA126 - MA504 normalized
def f01ct_f01_cyclical_trend_structure_curv_252d_base_v052_signal(closeadj):
    m126 = _f01_ma(closeadj, 126)
    m252 = _f01_ma(closeadj, 252)
    m504 = _f01_ma(closeadj, 504)
    b = (2.0 * m252 - m126 - m504) / m252.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# above-MA persistence weighted by distance depth (strong-trend persistence)
def f01ct_f01_cyclical_trend_structure_persistdepth_252d_base_v053_signal(closeadj):
    d = _f01_pdist(closeadj, 252)
    frac = _f01_above_frac(closeadj, 252, 126)
    b = frac * d.clip(lower=0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope-of-slope sign of 252d MA over a quarter (trend acceleration regime)
def f01ct_f01_cyclical_trend_structure_slopeaccel_252d_base_v054_signal(closeadj):
    sl = _f01_maslope(closeadj, 252, 21)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance between price and 504d MA, percentile-ranked (deep-cycle position)
def f01ct_f01_cyclical_trend_structure_pdistrank_504d_base_v055_signal(closeadj):
    d = _f01_pdist(closeadj, 504)
    b = d.rolling(504, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend direction agreement: sign of pdist21 == sign of pdist252 fraction over quarter
def f01ct_f01_cyclical_trend_structure_dirconsist_base_v056_signal(closeadj):
    d_s = np.sign(_f01_pdist(closeadj, 21))
    d_l = np.sign(_f01_pdist(closeadj, 252))
    agree = (d_s == d_l).astype(float)
    b = agree.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d MA slope minus 504d MA slope (intermediate vs long trend divergence)
def f01ct_f01_cyclical_trend_structure_slopespr_base_v057_signal(closeadj):
    s_i = _f01_maslope(closeadj, 126, 63)
    s_l = _f01_maslope(closeadj, 504, 63)
    b = s_i - s_l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year price held above ALL of 63/126/252 MAs (full-uptrend persistence)
def f01ct_f01_cyclical_trend_structure_fulluptrend_base_v058_signal(closeadj):
    m63 = _f01_ma(closeadj, 63)
    m126 = _f01_ma(closeadj, 126)
    m252 = _f01_ma(closeadj, 252)
    allabove = ((closeadj > m63) & (closeadj > m126) & (closeadj > m252)).astype(float)
    b = allabove.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 252d MA scaled by 252d MA-amplitude (range-normalized trend stretch)
def f01ct_f01_cyclical_trend_structure_pdistamp_252d_base_v059_signal(closeadj):
    ma = _f01_ma(closeadj, 252)
    amp = (closeadj.rolling(252, min_periods=126).max()
           - closeadj.rolling(252, min_periods=126).min())
    b = (closeadj - ma) / amp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stacking magnitude in z-units vs its own 252d history (regime extremity of stack)
def f01ct_f01_cyclical_trend_structure_stackz_base_v060_signal(closeadj):
    s = _f01_stack_mag(closeadj)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d MA-slope minus 126d MA-slope (short vs intermediate momentum of trend)
def f01ct_f01_cyclical_trend_structure_slopespr_21v126_base_v061_signal(closeadj):
    s_s = _f01_maslope(closeadj, 21, 21)
    s_i = _f01_maslope(closeadj, 126, 21)
    b = s_s - s_i
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in price-vs-252d-MA distance (cycle-phase shift)
def f01ct_f01_cyclical_trend_structure_pdistyoy_252d_base_v062_signal(closeadj):
    d = _f01_pdist(closeadj, 252)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-MA cross freshness: exponentially-decayed recency of the last cross, signed by side
def f01ct_f01_cyclical_trend_structure_xover_252d_base_v063_signal(closeadj):
    ma = _f01_ma(closeadj, 252)
    side = np.sign(closeadj - ma)
    crossed = (side != side.shift(1)).astype(float)
    freshness = crossed.ewm(span=63, min_periods=21).mean()
    b = freshness * side
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend choppiness: crossing count of the 252d MA over the year, blended with whipsaw depth
def f01ct_f01_cyclical_trend_structure_xovercount_252d_base_v064_signal(closeadj):
    ma = _f01_ma(closeadj, 252)
    side = np.sign(closeadj - ma)
    crossed = (side != side.shift(1)).astype(float)
    cnt = crossed.rolling(252, min_periods=126).sum()
    depth = (closeadj / ma.replace(0, np.nan) - 1.0).abs().rolling(63, min_periods=21).mean()
    b = cnt + 25.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-from-126d-MA dispersion over a quarter (trend instability)
def f01ct_f01_cyclical_trend_structure_pdiststd_126d_base_v065_signal(closeadj):
    d = _f01_pdist(closeadj, 126)
    b = d.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA ribbon compression: dispersion of the 5 MA levels normalized by price
def f01ct_f01_cyclical_trend_structure_ribboncomp_base_v066_signal(closeadj):
    m21 = _f01_ma(closeadj, 21)
    m63 = _f01_ma(closeadj, 63)
    m126 = _f01_ma(closeadj, 126)
    m252 = _f01_ma(closeadj, 252)
    m504 = _f01_ma(closeadj, 504)
    disp = pd.concat([m21, m63, m126, m252, m504], axis=1).std(axis=1)
    b = disp / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope-weighted stack: stacking magnitude signed by the 252d MA slope direction
def f01ct_f01_cyclical_trend_structure_stacksigned_base_v067_signal(closeadj):
    s = _f01_stack_mag(closeadj)
    sl = _f01_maslope(closeadj, 252, 63)
    b = s * np.sign(sl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 126d MA in ATR units, change over a quarter (approach speed)
def f01ct_f01_cyclical_trend_structure_pdistatrmom_126d_base_v068_signal(closeadj):
    ma = _f01_ma(closeadj, 126)
    atr = closeadj.diff().abs().rolling(21, min_periods=10).mean()
    ratio = (closeadj - ma) / atr.replace(0, np.nan)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest run above 63d MA within the last year, normalized (sustained mid-trend length)
def f01ct_f01_cyclical_trend_structure_maxrun_252d_base_v069_signal(closeadj):
    ma = _f01_ma(closeadj, 63)
    above = (closeadj > ma).astype(float)
    grp = (above != above.shift(1)).cumsum()
    run = above.groupby(grp).cumcount() + 1
    run = run * above
    b = run.rolling(252, min_periods=126).max() / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price vs an EMA(126)-style smoothing minus its SMA(126) (trend asymmetry)
def f01ct_f01_cyclical_trend_structure_emagap_126d_base_v070_signal(closeadj):
    ema = closeadj.ewm(span=126, min_periods=63).mean()
    sma = _f01_ma(closeadj, 126)
    b = np.log(ema.replace(0, np.nan) / sma.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend quality: 252d MA slope times fraction-above-MA (direction x persistence)
def f01ct_f01_cyclical_trend_structure_trendqual_252d_base_v071_signal(closeadj):
    sl = _f01_maslope(closeadj, 252, 63)
    frac = _f01_above_frac(closeadj, 252, 126)
    b = sl * (2.0 * frac - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 504d MA in z-units, momentum over a half-year (deep-cycle shift)
def f01ct_f01_cyclical_trend_structure_distzmom_504d_base_v072_signal(closeadj):
    z = _f01_pdistz(closeadj, 504, 504)
    b = z - z.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of MA-pairs in bullish order over last quarter (stacking persistence pct)
def f01ct_f01_cyclical_trend_structure_stackfrac_base_v073_signal(closeadj):
    s = _f01_stack_score(closeadj)
    bull = (s >= 3).astype(float)
    b = bull.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed sqrt of price-vs-504d-MA distance (compressed deep-trend extension)
def f01ct_f01_cyclical_trend_structure_pdistsqrt_504d_base_v074_signal(closeadj):
    d = _f01_pdist(closeadj, 504)
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-persistence composite: signed persistence(252) x distance-z(252) (conviction)
def f01ct_f01_cyclical_trend_structure_conviction_252d_base_v075_signal(closeadj):
    pers = _f01_trendpersist(closeadj, 252, 126)
    z = _f01_pdistz(closeadj, 252, 504)
    b = pers * z
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01ct_f01_cyclical_trend_structure_pdist_21d_base_v001_signal,
    f01ct_f01_cyclical_trend_structure_pdist_63d_base_v002_signal,
    f01ct_f01_cyclical_trend_structure_pdist_126d_base_v003_signal,
    f01ct_f01_cyclical_trend_structure_pdist_252d_base_v004_signal,
    f01ct_f01_cyclical_trend_structure_pdist_504d_base_v005_signal,
    f01ct_f01_cyclical_trend_structure_pdistz_63d_base_v006_signal,
    f01ct_f01_cyclical_trend_structure_pdistz_126d_base_v007_signal,
    f01ct_f01_cyclical_trend_structure_pdistz_252d_base_v008_signal,
    f01ct_f01_cyclical_trend_structure_pdistz_504d_base_v009_signal,
    f01ct_f01_cyclical_trend_structure_maslope_21d_base_v010_signal,
    f01ct_f01_cyclical_trend_structure_maslope_63d_base_v011_signal,
    f01ct_f01_cyclical_trend_structure_maslope_126d_base_v012_signal,
    f01ct_f01_cyclical_trend_structure_maslope_252d_base_v013_signal,
    f01ct_f01_cyclical_trend_structure_maslope_504d_base_v014_signal,
    f01ct_f01_cyclical_trend_structure_stack_base_v015_signal,
    f01ct_f01_cyclical_trend_structure_abovefrac_252d_base_v016_signal,
    f01ct_f01_cyclical_trend_structure_abovefrac_126d_base_v017_signal,
    f01ct_f01_cyclical_trend_structure_abovefrac_504d_base_v018_signal,
    f01ct_f01_cyclical_trend_structure_maratio_21v63_base_v019_signal,
    f01ct_f01_cyclical_trend_structure_maratio_63v126_base_v020_signal,
    f01ct_f01_cyclical_trend_structure_maratio_126v252_base_v021_signal,
    f01ct_f01_cyclical_trend_structure_maratio_252v504_base_v022_signal,
    f01ct_f01_cyclical_trend_structure_maratio_21v252_base_v023_signal,
    f01ct_f01_cyclical_trend_structure_persist_63d_base_v024_signal,
    f01ct_f01_cyclical_trend_structure_persist_252d_base_v025_signal,
    f01ct_f01_cyclical_trend_structure_streak_126d_base_v026_signal,
    f01ct_f01_cyclical_trend_structure_streak_252d_base_v027_signal,
    f01ct_f01_cyclical_trend_structure_madisp_base_v028_signal,
    f01ct_f01_cyclical_trend_structure_slopebreadth_base_v029_signal,
    f01ct_f01_cyclical_trend_structure_pdistrank_252d_base_v030_signal,
    f01ct_f01_cyclical_trend_structure_pdistrank_126d_base_v031_signal,
    f01ct_f01_cyclical_trend_structure_pdistmom_252d_base_v032_signal,
    f01ct_f01_cyclical_trend_structure_pdistmom_126d_base_v033_signal,
    f01ct_f01_cyclical_trend_structure_slopevol_252d_base_v034_signal,
    f01ct_f01_cyclical_trend_structure_slopevol_63d_base_v035_signal,
    f01ct_f01_cyclical_trend_structure_stackpersist_base_v036_signal,
    f01ct_f01_cyclical_trend_structure_efficiency_252d_base_v037_signal,
    f01ct_f01_cyclical_trend_structure_efficiency_63d_base_v038_signal,
    f01ct_f01_cyclical_trend_structure_crossmag_21v252_base_v039_signal,
    f01ct_f01_cyclical_trend_structure_ladderconv_base_v040_signal,
    f01ct_f01_cyclical_trend_structure_pdistatr_252d_base_v041_signal,
    f01ct_f01_cyclical_trend_structure_pdistatr_63d_base_v042_signal,
    f01ct_f01_cyclical_trend_structure_pdisttanh_252d_base_v043_signal,
    f01ct_f01_cyclical_trend_structure_streak_63d_base_v044_signal,
    f01ct_f01_cyclical_trend_structure_stackmom_base_v045_signal,
    f01ct_f01_cyclical_trend_structure_abovespr_base_v046_signal,
    f01ct_f01_cyclical_trend_structure_distzspr_base_v047_signal,
    f01ct_f01_cyclical_trend_structure_slopesm_504d_base_v048_signal,
    f01ct_f01_cyclical_trend_structure_pdistz_21d_base_v049_signal,
    f01ct_f01_cyclical_trend_structure_slowbundle_base_v050_signal,
    f01ct_f01_cyclical_trend_structure_curv_63d_base_v051_signal,
    f01ct_f01_cyclical_trend_structure_curv_252d_base_v052_signal,
    f01ct_f01_cyclical_trend_structure_persistdepth_252d_base_v053_signal,
    f01ct_f01_cyclical_trend_structure_slopeaccel_252d_base_v054_signal,
    f01ct_f01_cyclical_trend_structure_pdistrank_504d_base_v055_signal,
    f01ct_f01_cyclical_trend_structure_dirconsist_base_v056_signal,
    f01ct_f01_cyclical_trend_structure_slopespr_base_v057_signal,
    f01ct_f01_cyclical_trend_structure_fulluptrend_base_v058_signal,
    f01ct_f01_cyclical_trend_structure_pdistamp_252d_base_v059_signal,
    f01ct_f01_cyclical_trend_structure_stackz_base_v060_signal,
    f01ct_f01_cyclical_trend_structure_slopespr_21v126_base_v061_signal,
    f01ct_f01_cyclical_trend_structure_pdistyoy_252d_base_v062_signal,
    f01ct_f01_cyclical_trend_structure_xover_252d_base_v063_signal,
    f01ct_f01_cyclical_trend_structure_xovercount_252d_base_v064_signal,
    f01ct_f01_cyclical_trend_structure_pdiststd_126d_base_v065_signal,
    f01ct_f01_cyclical_trend_structure_ribboncomp_base_v066_signal,
    f01ct_f01_cyclical_trend_structure_stacksigned_base_v067_signal,
    f01ct_f01_cyclical_trend_structure_pdistatrmom_126d_base_v068_signal,
    f01ct_f01_cyclical_trend_structure_maxrun_252d_base_v069_signal,
    f01ct_f01_cyclical_trend_structure_emagap_126d_base_v070_signal,
    f01ct_f01_cyclical_trend_structure_trendqual_252d_base_v071_signal,
    f01ct_f01_cyclical_trend_structure_distzmom_504d_base_v072_signal,
    f01ct_f01_cyclical_trend_structure_stackfrac_base_v073_signal,
    f01ct_f01_cyclical_trend_structure_pdistsqrt_504d_base_v074_signal,
    f01ct_f01_cyclical_trend_structure_conviction_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_CYCLICAL_TREND_STRUCTURE_REGISTRY_001_075 = REGISTRY


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

    print("OK f01_cyclical_trend_structure_base_001_075_claude: %d features pass" % n_features)
