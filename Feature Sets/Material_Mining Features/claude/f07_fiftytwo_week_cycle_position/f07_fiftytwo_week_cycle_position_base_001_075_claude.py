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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives: 52-week / multi-year ANCHORING & POSITION =====
# NOTE (anti-overlap): f07 deliberately AVOIDS raw proximity-to-high level
# (== 1 - drawdown, that is f04), raw range-position/phase level (f03),
# raw drawdown depth/duration/velocity (f04), base-tightness/breakout (f06),
# and bare days-since fractions (f03 tsh/tsl). The behavioral-anchor signal is
# expressed as anchoring GAP in z / rank / frequency forms, nested-anchor
# RELATIONSHIPS (52w vs 5y), and count-friendly new-high/new-low FREQUENCY.

def _f07_anchor_gap(close, w):
    # log gap of price below the rolling 52w-style high (the behavioral anchor).
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(close.replace(0, np.nan) / hi.replace(0, np.nan))


def _f07_floor_gap(close, w):
    # log gap of price above the rolling multi-year low.
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return np.log(close.replace(0, np.nan) / lo.replace(0, np.nan))


def _f07_newhi_events(close, w):
    # 1.0 on a bar that prints a fresh rolling-w high (new-high EVENT, count-friendly).
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close >= hi * 0.999999).astype(float)


def _f07_newlo_events(close, w):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (close <= lo * 1.000001).astype(float)


def _f07_days_since_hi(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f07_days_since_lo(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f07_last_event_age(ev, w):
    # bars since the most recent event flag within the trailing window.
    def _f(a):
        idx = np.where(a > 0.5)[0]
        if idx.size == 0:
            return float(len(a))
        return float(len(a) - 1 - idx[-1])
    return ev.rolling(w, min_periods=max(1, w // 4)).apply(_f, raw=True)


def _f07_nearness_lo(close, w):
    # continuous nearness to the rolling low: 1/(1+floor_gap), 1 at the low, ->0 far above.
    return 1.0 / (1.0 + _f07_floor_gap(close, w))


def _f07_nearness_hi(close, w):
    # continuous nearness to the rolling high: 1/(1-anchor_gap), 1 at the high.
    return 1.0 / (1.0 - _f07_anchor_gap(close, w))


# ============================================================
# --- Block A: anchoring gap in RANK / Z forms (not raw level) ---

# v001 nested-anchor disagreement: 252d-high gap minus 1260d-high gap, percentile-ranked
#       (how much closer the price hugs the recent 52w anchor vs the multi-year anchor)
def f07cy_f07_fiftytwo_week_cycle_position_gaprank_252d_base_v001_signal(closeadj):
    g1 = _f07_anchor_gap(closeadj, 252)
    g3 = _f07_anchor_gap(closeadj, 1260)
    b = _rank(g1 - g3, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v002 anchoring gap to 504d high, percentile-ranked within its own 504d history
def f07cy_f07_fiftytwo_week_cycle_position_gaprank_504d_base_v002_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 504)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v003 anchoring gap to 1260d high, detrended (gap minus its 252d EMA) then ranked short-window
def f07cy_f07_fiftytwo_week_cycle_position_gaprank_1260d_base_v003_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 1260)
    detr = g - g.ewm(span=252, min_periods=63).mean()
    b = _rank(detr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v004 anchor-approach momentum percentile: change in the 252d-high gap over a quarter, ranked
def f07cy_f07_fiftytwo_week_cycle_position_gapz_252d_base_v004_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 252)
    mom = g - g.shift(63)
    b = _rank(mom, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v005 anchoring gap to 504d high, z vs its 252d typical depth
def f07cy_f07_fiftytwo_week_cycle_position_gapz_504d_base_v005_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 504)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v006 deep-vs-mid anchor disagreement: 1260d-high gap minus 504d-high gap, ranked
#       (extra overhead the multi-year anchor adds beyond the two-year anchor)
def f07cy_f07_fiftytwo_week_cycle_position_gapz_1260d_base_v006_signal(closeadj):
    g2 = _f07_anchor_gap(closeadj, 504)
    g3 = _f07_anchor_gap(closeadj, 1260)
    b = _rank(g3 - g2, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v007 floor gap above 252d low, percentile-ranked within its 504d history
def f07cy_f07_fiftytwo_week_cycle_position_floorrank_252d_base_v007_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 252)
    b = _rank(fg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v008 floor gap above 1260d low, percentile-ranked within its 756d history
def f07cy_f07_fiftytwo_week_cycle_position_floorrank_1260d_base_v008_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 1260)
    b = _rank(fg, 756)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v009 high-anchor staleness at the 504d window, ranked vs its 504d history
#       (how stale the two-year high is relative to its own history -- leadership decay percentile)
def f07cy_f07_fiftytwo_week_cycle_position_floorz_504d_base_v009_signal(closeadj):
    dh = _f07_days_since_hi(closeadj, 504)
    b = _rank(dh, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block B: NESTED-ANCHOR relationships (52w vs 2y vs 5y) ---

# v010 cross-anchor band position: distance above the 1260d low vs distance below the 252d high
def f07cy_f07_fiftytwo_week_cycle_position_gapspread_252v1260_base_v010_signal(closeadj):
    g1 = _f07_anchor_gap(closeadj, 252)        # <= 0, below the 52w high
    f3 = _f07_floor_gap(closeadj, 1260)        # >= 0, above the 5y low
    b = f3 + g1                                 # net position across the nested band
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v011 cross-anchor band position over the mid horizon: above-504d-low minus below-252d-high, z
def f07cy_f07_fiftytwo_week_cycle_position_gapspread_252v504_base_v011_signal(closeadj):
    g1 = _f07_anchor_gap(closeadj, 252)        # <= 0
    f2 = _f07_floor_gap(closeadj, 504)         # >= 0
    net = f2 + g1
    b = _z(net, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v012 anchor-freshness ratio: is the 252d high also the 1260d high? log(hi252/hi1260)
def f07cy_f07_fiftytwo_week_cycle_position_hifresh_252v1260_base_v012_signal(closeadj):
    hi1 = _rmax(closeadj, 252)
    hi3 = _rmax(closeadj, 1260)
    b = np.log(hi1.replace(0, np.nan) / hi3.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v013 anchor-freshness ratio: 252d high vs 504d high, z-scored (de-trended freshness)
def f07cy_f07_fiftytwo_week_cycle_position_hifresh_252v504_base_v013_signal(closeadj):
    hi1 = _rmax(closeadj, 252)
    hi2 = _rmax(closeadj, 504)
    fresh = np.log(hi1.replace(0, np.nan) / hi2.replace(0, np.nan))
    b = _z(fresh, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v014 new-high frequency ratio: trailing-year 252d new-high rate vs 504d new-high rate
#       (>1 => recent leadership is fresher than the two-year leadership -- nested freshness)
def f07cy_f07_fiftytwo_week_cycle_position_lofresh_252v1260_base_v014_signal(closeadj):
    r1 = _f07_newhi_events(closeadj, 252).rolling(252, min_periods=63).mean()
    r2 = _f07_newhi_events(closeadj, 504).rolling(252, min_periods=63).mean()
    b = (r1 + 0.01) / (r2 + 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v015 nested amplitude gain: 1260d log-span minus 252d log-span (extra amplitude of the long cycle)
def f07cy_f07_fiftytwo_week_cycle_position_span_1260d_base_v015_signal(closeadj):
    s3 = np.log(_rmax(closeadj, 1260).replace(0, np.nan) / _rmin(closeadj, 1260).replace(0, np.nan))
    s1 = np.log(_rmax(closeadj, 252).replace(0, np.nan) / _rmin(closeadj, 252).replace(0, np.nan))
    b = s3 - s1
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v016 nested span ratio: 252d log-span as a fraction of 1260d log-span
def f07cy_f07_fiftytwo_week_cycle_position_spanratio_252v1260_base_v016_signal(closeadj):
    s1 = np.log(_rmax(closeadj, 252).replace(0, np.nan) / _rmin(closeadj, 252).replace(0, np.nan))
    s3 = np.log(_rmax(closeadj, 1260).replace(0, np.nan) / _rmin(closeadj, 1260).replace(0, np.nan))
    b = s1 / s3.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v017 anchoring tension: mean absolute gap across high & low anchors at the 252d horizon, z
def f07cy_f07_fiftytwo_week_cycle_position_gapdisp_multi_base_v017_signal(closeadj):
    g1 = _f07_anchor_gap(closeadj, 252).abs()
    f1 = _f07_floor_gap(closeadj, 252).abs()
    g2 = _f07_anchor_gap(closeadj, 504).abs()
    tension = (g1 + f1 + g2) / 3.0
    b = _z(tension, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v018 where the 1260d high sits above the 252d low (multi-year overhead span)
def f07cy_f07_fiftytwo_week_cycle_position_overheadspan_base_v018_signal(closeadj):
    hi3 = _rmax(closeadj, 1260)
    lo1 = _rmin(closeadj, 252)
    b = np.log(hi3.replace(0, np.nan) / lo1.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block C: new-multi-year-high / new-low FREQUENCY (count-friendly) ---

# v019 quarter new-high count net of new-low count (252d anchors) -- breadth of extreme prints
def f07cy_f07_fiftytwo_week_cycle_position_newhicnt_252d_base_v019_signal(closeadj):
    hi = _f07_newhi_events(closeadj, 252).rolling(63, min_periods=21).sum()
    lo = _f07_newlo_events(closeadj, 252).rolling(63, min_periods=21).sum()
    nearness = _f07_nearness_lo(closeadj, 252).rolling(21, min_periods=7).mean()
    b = hi - lo - 3.0 * nearness
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v020 count of fresh 504d highs printed in the trailing half-year
def f07cy_f07_fiftytwo_week_cycle_position_newhicnt_504d_base_v020_signal(closeadj):
    ev = _f07_newhi_events(closeadj, 504)
    b = ev.rolling(126, min_periods=42).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v021 count of fresh 1260d (multi-year) highs in the trailing year
def f07cy_f07_fiftytwo_week_cycle_position_newhicnt_1260d_base_v021_signal(closeadj):
    ev = _f07_newhi_events(closeadj, 1260)
    b = ev.rolling(252, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v022 fresh-252d-low tally over the quarter, blended with continuous nearness to the low
def f07cy_f07_fiftytwo_week_cycle_position_newlocnt_252d_base_v022_signal(closeadj):
    ev = _f07_newlo_events(closeadj, 252)
    cnt = ev.rolling(63, min_periods=21).sum()
    # nearness-to-low: small floor gap => near the low; smoothed so it varies continuously
    nearness = (1.0 / (1.0 + _f07_floor_gap(closeadj, 252))).rolling(21, min_periods=7).mean()
    b = cnt + 5.0 * nearness
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v023 fresh-1260d-low tally over the year, blended with nearness to the multi-year low
def f07cy_f07_fiftytwo_week_cycle_position_newlocnt_1260d_base_v023_signal(closeadj):
    ev = _f07_newlo_events(closeadj, 1260)
    cnt = ev.rolling(252, min_periods=63).sum()
    nearness = (1.0 / (1.0 + _f07_floor_gap(closeadj, 1260))).rolling(63, min_periods=21).mean()
    b = cnt + 5.0 * nearness
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v024 new-high minus new-low event balance over the trailing year (net anchor pressure)
def f07cy_f07_fiftytwo_week_cycle_position_newbal_252d_base_v024_signal(closeadj):
    hi = _f07_newhi_events(closeadj, 252).rolling(252, min_periods=63).sum()
    lo = _f07_newlo_events(closeadj, 252).rolling(252, min_periods=63).sum()
    b = (hi - lo) / (hi + lo + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v025 fresh-high event rate to 504d high over the trailing year (leadership intensity)
def f07cy_f07_fiftytwo_week_cycle_position_hirate_504d_base_v025_signal(closeadj):
    ev = _f07_newhi_events(closeadj, 504)
    b = ev.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v026 distinct new-high CLUSTERS: count of fresh-high streak starts in trailing year
def f07cy_f07_fiftytwo_week_cycle_position_hiclusters_252d_base_v026_signal(closeadj):
    ev = _f07_newhi_events(closeadj, 252)
    starts = ((ev == 1) & (ev.shift(1) == 0)).astype(float)
    b = starts.rolling(252, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v027 distinct new-low CLUSTERS (streak starts) blended with continuous nearness-to-low
def f07cy_f07_fiftytwo_week_cycle_position_loclusters_252d_base_v027_signal(closeadj):
    ev = _f07_newlo_events(closeadj, 252)
    starts = ((ev == 1) & (ev.shift(1) == 0)).astype(float)
    cnt = starts.rolling(252, min_periods=63).sum()
    nearness = (1.0 / (1.0 + _f07_floor_gap(closeadj, 252))).rolling(42, min_periods=14).mean()
    b = cnt + 5.0 * nearness
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v028 cluster balance ratio: (hi clusters - lo clusters)/(total) for 504d anchors over a half-year
def f07cy_f07_fiftytwo_week_cycle_position_clusterbal_504d_base_v028_signal(closeadj):
    hev = _f07_newhi_events(closeadj, 504)
    lev = _f07_newlo_events(closeadj, 504)
    hs = ((hev == 1) & (hev.shift(1) == 0)).astype(float).rolling(126, min_periods=42).sum()
    ls = ((lev == 1) & (lev.shift(1) == 0)).astype(float).rolling(126, min_periods=42).sum()
    ratio = (hs - ls) / (hs + ls + 1.0)
    tilt = (_f07_anchor_gap(closeadj, 504) - _f07_floor_gap(closeadj, 504)).rolling(21, min_periods=7).mean()
    b = ratio + 0.5 * tilt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block D: recovery-off-multi-year-low in distinctive (ranked/normalized) forms ---

# v029 recovery off 1260d low (floor gap), displaced from its own 252d EMA (de-trended recovery)
def f07cy_f07_fiftytwo_week_cycle_position_recovrank_1260d_base_v029_signal(closeadj):
    rec = _f07_floor_gap(closeadj, 1260)
    b = rec - rec.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v030 floor-test frequency: distinct entries into the bottom 5% of the 504d band over the year
#       (how many times price re-tested the two-year floor -- a count-friendly basing signal)
def f07cy_f07_fiftytwo_week_cycle_position_recovshare_504d_base_v030_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 504)
    near = (fg <= np.log(1.05)).astype(float)
    entries = ((near == 1) & (near.shift(1) == 0)).astype(float)
    cnt = entries.rolling(252, min_periods=63).sum()
    nearness = _f07_nearness_lo(closeadj, 504).rolling(42, min_periods=14).mean()
    b = cnt + 5.0 * nearness
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v031 change in the 1260d recovery-share over a quarter (multi-year recovery-position momentum)
def f07cy_f07_fiftytwo_week_cycle_position_recovshare_1260d_base_v031_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 1260)
    span = np.log(_rmax(closeadj, 1260).replace(0, np.nan) / _rmin(closeadj, 1260).replace(0, np.nan))
    share = fg / span.replace(0, np.nan)
    b = share - share.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v032 multi-year survival multiple momentum: change in log(price/1260d-low) over a half-year
def f07cy_f07_fiftytwo_week_cycle_position_survrank_1260d_base_v032_signal(closeadj):
    surv = np.log(closeadj.replace(0, np.nan) / _rmin(closeadj, 1260).replace(0, np.nan))
    b = surv - surv.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block E: anchor STALENESS expressed in transformed (count/ratio) forms ---

# v033 staleness-asymmetry momentum: change in (days-since-high - days-since-low) over a quarter
#       (is leadership freshening or staling relative to the floor -- a turnover signal)
def f07cy_f07_fiftytwo_week_cycle_position_staleasym_252d_base_v033_signal(closeadj):
    dh = _f07_days_since_hi(closeadj, 252)
    dl = _f07_days_since_lo(closeadj, 252)
    asym = dh - dl
    b = asym - asym.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v034 staleness asymmetry over the 1260d (multi-year) window
def f07cy_f07_fiftytwo_week_cycle_position_staleasym_1260d_base_v034_signal(closeadj):
    dh = _f07_days_since_hi(closeadj, 1260)
    dl = _f07_days_since_lo(closeadj, 1260)
    b = dh - dl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v035 high-anchor staleness ranked vs its own 504d history (relatively stale leadership)
def f07cy_f07_fiftytwo_week_cycle_position_dshrank_252d_base_v035_signal(closeadj):
    dh = _f07_days_since_hi(closeadj, 252)
    b = _rank(dh, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v036 low-anchor staleness ranked vs its own 504d history
def f07cy_f07_fiftytwo_week_cycle_position_dslrank_252d_base_v036_signal(closeadj):
    dl = _f07_days_since_lo(closeadj, 252)
    b = _rank(dl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v037 staleness ratio: fraction of window since high relative to since low (504d)
def f07cy_f07_fiftytwo_week_cycle_position_staleratio_504d_base_v037_signal(closeadj):
    dh = _f07_days_since_hi(closeadj, 504)
    dl = _f07_days_since_lo(closeadj, 504)
    b = (dh + 0.02) / (dl + 0.02) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block F: position expressed through anchor-gap nonlinearity / interaction ---

# v038 anchoring-gap signed-root compression to 504d high (squashed deep-anchor displacement)
def f07cy_f07_fiftytwo_week_cycle_position_gaproot_504d_base_v038_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 504)
    root = np.sign(g) * (g.abs() ** 0.5)
    typ = root.rolling(252, min_periods=63).mean()
    b = root - typ
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v039 anchoring-gap to 252d high per unit of realized risk, ranked (risk-scaled position)
def f07cy_f07_fiftytwo_week_cycle_position_gapvolrank_252d_base_v039_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    ratio = g / vol.replace(0, np.nan)
    b = _rank(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v040 nested-floor disagreement: 252d floor gap minus 504d floor gap, ranked
#       (whether the recent low sits well above the two-year low -- nested anchor relation)
def f07cy_f07_fiftytwo_week_cycle_position_floorvolrank_252d_base_v040_signal(closeadj):
    f1 = _f07_floor_gap(closeadj, 252)
    f2 = _f07_floor_gap(closeadj, 504)
    b = _rank(f1 - f2, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v041 anchoring-gap tanh-bounded level to 1260d high (squashed deep-value position)
def f07cy_f07_fiftytwo_week_cycle_position_gaptanh_1260d_base_v041_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 1260)
    b = np.tanh(3.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block G: anchor-gap YoY and de-trended displacement (not velocity of drawdown) ---

# v042 anchoring gap now vs the anchoring gap one year ago (252d) -- YoY anchor shift
def f07cy_f07_fiftytwo_week_cycle_position_gapyoy_252d_base_v042_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 252)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v043 anchoring gap displacement from its own slow EMA (anchor-position displacement)
def f07cy_f07_fiftytwo_week_cycle_position_gapdisp_252d_base_v043_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 252)
    b = g - g.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v044 floor gap YoY: recovery position vs one year ago (1260d window)
def f07cy_f07_fiftytwo_week_cycle_position_flooryoy_1260d_base_v044_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 1260)
    b = fg - fg.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block H: time-in-zone occupancy of the anchored range (count-friendly fractions) ---

# v045 leadership occupancy net of basing: near-high time minus mid-zone time (252d, half-year)
def f07cy_f07_fiftytwo_week_cycle_position_nearhioccup_252d_base_v045_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 252)
    near = (g >= np.log(0.97)).astype(float)
    mid = ((g < np.log(0.85)) & (g >= np.log(0.70))).astype(float)
    b = (near - mid).rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v046 fraction of trailing year spent within 5% of the 252d low (basing occupancy)
def f07cy_f07_fiftytwo_week_cycle_position_nearlooccup_252d_base_v046_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 252)
    near = (fg <= np.log(1.05)).astype(float)
    b = near.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v047 multi-year floor-test entries: distinct approaches into the bottom 10% of the 1260d band
def f07cy_f07_fiftytwo_week_cycle_position_occupbal_1260d_base_v047_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 1260)
    near = (fg <= np.log(1.10)).astype(float)
    entries = ((near == 1) & (near.shift(1) == 0)).astype(float)
    cnt = entries.rolling(252, min_periods=63).sum()
    nearness = _f07_nearness_lo(closeadj, 1260).rolling(42, min_periods=14).mean()
    b = cnt + 4.0 * nearness
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v048 entries into the near-high zone over the trailing year (distinct approaches to the anchor)
def f07cy_f07_fiftytwo_week_cycle_position_hiapproaches_252d_base_v048_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 252)
    near = (g >= np.log(0.97)).astype(float)
    entries = ((near == 1) & (near.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block I: anchor-gap smoothing / persistence (distinct from raw level) ---

# v049 persistence-weighted anchor proximity: how long & deep price has stayed near the 252d high
def f07cy_f07_fiftytwo_week_cycle_position_hipersist_252d_base_v049_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 252)
    persist = (g >= np.log(0.92)).astype(float).rolling(63, min_periods=21).mean()
    depth = (g - np.log(0.92)).clip(lower=0)
    b = persist * depth.rolling(21, min_periods=7).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v050 anchor-gap EMA term spread to 504d high (fast minus slow anchor mean reversion)
def f07cy_f07_fiftytwo_week_cycle_position_gapema_504d_base_v050_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 504)
    b = g.ewm(span=63, min_periods=21).mean() - g.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block J: intraday true-high/true-low anchoring (uses high/low columns) ---

# v051 true-high anchoring gap to 252d intraday high, z-scored vs its 126d history (de-trended)
def f07cy_f07_fiftytwo_week_cycle_position_truehigaprank_252d_base_v051_signal(closeadj, high):
    hi = high.rolling(252, min_periods=126).max()
    g = np.log(closeadj.replace(0, np.nan) / hi.replace(0, np.nan))
    b = g - g.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v052 true-low floor gap to 252d intraday low, de-trended vs its own 63d EMA
def f07cy_f07_fiftytwo_week_cycle_position_truelofloorrank_252d_base_v052_signal(closeadj, low):
    lo = low.rolling(252, min_periods=126).min()
    fg = np.log(closeadj.replace(0, np.nan) / lo.replace(0, np.nan))
    b = fg - fg.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v053 true-high premium: how far the 252d intraday high sits above the close-based high (z)
def f07cy_f07_fiftytwo_week_cycle_position_hipremium_252d_base_v053_signal(closeadj, high):
    hi_t = high.rolling(252, min_periods=126).max()
    hi_c = closeadj.rolling(252, min_periods=126).max()
    raw = np.log(hi_t.replace(0, np.nan) / hi_c.replace(0, np.nan))
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v054 true-low discount: how far the 252d intraday low sits below the close-based low (z)
def f07cy_f07_fiftytwo_week_cycle_position_lodiscount_252d_base_v054_signal(closeadj, low):
    lo_t = low.rolling(252, min_periods=126).min()
    lo_c = closeadj.rolling(252, min_periods=126).min()
    raw = np.log(lo_c.replace(0, np.nan) / lo_t.replace(0, np.nan))
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v055 intraday cycle span: log(252d true-high / 252d true-low), ranked
def f07cy_f07_fiftytwo_week_cycle_position_truespanrank_252d_base_v055_signal(closeadj, high, low):
    hi = high.rolling(252, min_periods=126).max()
    lo = low.rolling(252, min_periods=126).min()
    span = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    b = _rank(span, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block K: anchor-band balance (where in the anchored band via gap ratio) ---

# v056 anchor balance: log distance to low vs log distance to high (252d), z-scored
def f07cy_f07_fiftytwo_week_cycle_position_anchbal_252d_base_v056_signal(closeadj):
    g = (-_f07_anchor_gap(closeadj, 252)).clip(lower=1e-6)   # magnitude below high
    fg = (_f07_floor_gap(closeadj, 252)).clip(lower=1e-6)    # magnitude above low
    bal = (fg - g) / (fg + g)
    b = _z(bal, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v057 multi-year new-high occupancy: fraction of the trailing year within 10% of the 1260d high
#       (deep-cycle time-at-leadership -- a count-friendly multi-year position signal)
def f07cy_f07_fiftytwo_week_cycle_position_anchbal_1260d_base_v057_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 1260)
    near = (g >= np.log(0.90)).astype(float)
    frac = near.rolling(252, min_periods=63).mean()
    pulse = _f07_nearness_hi(closeadj, 1260).rolling(42, min_periods=14).mean()
    b = frac + 0.5 * pulse
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v058 anchor-band tilt momentum: change in the 504d gap-balance over a quarter
def f07cy_f07_fiftytwo_week_cycle_position_anchtilt_504d_base_v058_signal(closeadj):
    g = (-_f07_anchor_gap(closeadj, 504)).clip(lower=1e-6)
    fg = (_f07_floor_gap(closeadj, 504)).clip(lower=1e-6)
    bal = (fg - g) / (fg + g)
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block L: cross-window anchor-gap term structure ---

# v059 anchor-gap term structure: 252d gap relative to 1260d gap (ratio, near/far depth)
def f07cy_f07_fiftytwo_week_cycle_position_gapterm_252v1260_base_v059_signal(closeadj):
    g1 = _f07_anchor_gap(closeadj, 252)
    g3 = _f07_anchor_gap(closeadj, 1260)
    b = g1 / g3.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v060 floor-gap term structure: 252d floor relative to 1260d floor (near/far recovery)
def f07cy_f07_fiftytwo_week_cycle_position_floorterm_252v1260_base_v060_signal(closeadj):
    f1 = _f07_floor_gap(closeadj, 252)
    f3 = _f07_floor_gap(closeadj, 1260)
    b = f1 / f3.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v061 floor-gap convexity: 504d floor minus the average of 252d and 1260d floors (low-anchor curvature)
def f07cy_f07_fiftytwo_week_cycle_position_gapconvex_base_v061_signal(closeadj):
    f1 = _f07_floor_gap(closeadj, 252)
    f2 = _f07_floor_gap(closeadj, 504)
    f3 = _f07_floor_gap(closeadj, 1260)
    b = f2 - 0.5 * (f1 + f3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block M: anchor-gap frequency-of-extremes & regime occupancy ---

# v062 fraction of trailing window where the gap is deeper than its rolling median (below-anchor regime)
def f07cy_f07_fiftytwo_week_cycle_position_belowanchfrac_252d_base_v062_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 252)
    med = g.rolling(252, min_periods=63).median()
    below = (g < med).astype(float)
    b = below.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v063 anchor-gap excursion count (crosses below -20%) blended with avg below-anchor depth
def f07cy_f07_fiftytwo_week_cycle_position_gapexcursion_252d_base_v063_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 252)
    deep = (g <= np.log(0.80)).astype(float)
    entries = ((deep == 1) & (deep.shift(1) == 0)).astype(float)
    cnt = entries.rolling(252, min_periods=63).sum()
    depth = (-g).clip(lower=0).rolling(63, min_periods=21).mean()
    b = cnt + 8.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v064 recovery excursion count (floor gap crosses above +30%) blended with avg recovery height
def f07cy_f07_fiftytwo_week_cycle_position_recovexcursion_252d_base_v064_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 252)
    up = (fg >= np.log(1.30)).astype(float)
    entries = ((up == 1) & (up.shift(1) == 0)).astype(float)
    cnt = entries.rolling(252, min_periods=63).sum()
    height = (fg - np.log(1.30)).clip(lower=0).rolling(63, min_periods=21).mean()
    b = cnt + 8.0 * height
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block N: anchor-gap risk-adjusted long-horizon position ---

# v065 1260d anchor gap per unit of long-horizon risk, change over a quarter (risk-position momentum)
def f07cy_f07_fiftytwo_week_cycle_position_deepgapvol_1260d_base_v065_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 1260)
    vol = closeadj.pct_change().rolling(126, min_periods=63).std()
    ratio = g / vol.replace(0, np.nan)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v066 504d floor gap per unit of risk, ranked (risk-scaled multi-year recovery)
def f07cy_f07_fiftytwo_week_cycle_position_floorvolrank_504d_base_v066_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 504)
    vol = closeadj.pct_change().rolling(126, min_periods=63).std()
    ratio = fg / vol.replace(0, np.nan)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block O: anchor-gap percentile within long self-history ---

# v067 anchor gap to 504d high ranked within a long 756d window (deep position percentile)
def f07cy_f07_fiftytwo_week_cycle_position_gaprank_504long_base_v067_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 504)
    b = _rank(g, 756)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v068 floor gap to 252d low ranked within a long 756d window
def f07cy_f07_fiftytwo_week_cycle_position_floorrank_252long_base_v068_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 252)
    b = _rank(fg, 756)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block P: new-high / new-low recency interactions (event age, not bare days-since) ---

# v069 fresh-anchor recency: log-bars since the last new 252d high (anchor age)
def f07cy_f07_fiftytwo_week_cycle_position_hirecency_252d_base_v069_signal(closeadj):
    ev = _f07_newhi_events(closeadj, 252)
    age = _f07_last_event_age(ev, 252)
    b = np.log1p(age)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v070 new-low recency: log-bars since the last new 252d low (capitulation freshness)
def f07cy_f07_fiftytwo_week_cycle_position_lorecency_252d_base_v070_signal(closeadj):
    ev = _f07_newlo_events(closeadj, 252)
    age = _f07_last_event_age(ev, 252)
    b = np.log1p(age)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v071 recency balance: new-low recency vs new-high recency (which extreme is more recent)
def f07cy_f07_fiftytwo_week_cycle_position_recencybal_252d_base_v071_signal(closeadj):
    hev = _f07_newhi_events(closeadj, 252)
    lev = _f07_newlo_events(closeadj, 252)
    ha = _f07_last_event_age(hev, 252)
    la = _f07_last_event_age(lev, 252)
    b = (la - ha) / (la + ha + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block Q: anchor-gap multi-horizon blend & dispersion ---

# v072 anchor-gap range across horizons: max-minus-min gap (252/504/1260), z-scored (anchor spread)
def f07cy_f07_fiftytwo_week_cycle_position_blendgapz_base_v072_signal(closeadj):
    g1 = _f07_anchor_gap(closeadj, 252)
    g2 = _f07_anchor_gap(closeadj, 504)
    g3 = _f07_anchor_gap(closeadj, 1260)
    stk = pd.concat([g1, g2, g3], axis=1)
    spread = stk.max(axis=1) - stk.min(axis=1)
    b = _z(spread, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v073 short-horizon floor-gap dispersion across 63/126/252 (near-term recovery disagreement)
def f07cy_f07_fiftytwo_week_cycle_position_floordisp_multi_base_v073_signal(closeadj):
    f1 = _f07_floor_gap(closeadj, 63)
    f2 = _f07_floor_gap(closeadj, 126)
    f3 = _f07_floor_gap(closeadj, 252)
    b = pd.concat([f1, f2, f3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v074 anchored-band-fraction YoY: distance-above-low/span (252d) now minus one year ago
#       (where in the 52w band vs a year ago -- a cycle-position turnover signal)
def f07cy_f07_fiftytwo_week_cycle_position_bandfracrank_252d_base_v074_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 252)
    span = np.log(_rmax(closeadj, 252).replace(0, np.nan) / _rmin(closeadj, 252).replace(0, np.nan))
    frac = fg / span.replace(0, np.nan)
    b = frac - frac.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v075 cycle-position net pull: anchor-gap rank minus floor-gap rank (top-vs-bottom net pull)
def f07cy_f07_fiftytwo_week_cycle_position_netpull_252d_base_v075_signal(closeadj):
    gr = _rank(_f07_anchor_gap(closeadj, 252), 504)
    fr = _rank(_f07_floor_gap(closeadj, 252), 504)
    b = gr - fr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07cy_f07_fiftytwo_week_cycle_position_gaprank_252d_base_v001_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gaprank_504d_base_v002_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gaprank_1260d_base_v003_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapz_252d_base_v004_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapz_504d_base_v005_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapz_1260d_base_v006_signal,
    f07cy_f07_fiftytwo_week_cycle_position_floorrank_252d_base_v007_signal,
    f07cy_f07_fiftytwo_week_cycle_position_floorrank_1260d_base_v008_signal,
    f07cy_f07_fiftytwo_week_cycle_position_floorz_504d_base_v009_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapspread_252v1260_base_v010_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapspread_252v504_base_v011_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hifresh_252v1260_base_v012_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hifresh_252v504_base_v013_signal,
    f07cy_f07_fiftytwo_week_cycle_position_lofresh_252v1260_base_v014_signal,
    f07cy_f07_fiftytwo_week_cycle_position_span_1260d_base_v015_signal,
    f07cy_f07_fiftytwo_week_cycle_position_spanratio_252v1260_base_v016_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapdisp_multi_base_v017_signal,
    f07cy_f07_fiftytwo_week_cycle_position_overheadspan_base_v018_signal,
    f07cy_f07_fiftytwo_week_cycle_position_newhicnt_252d_base_v019_signal,
    f07cy_f07_fiftytwo_week_cycle_position_newhicnt_504d_base_v020_signal,
    f07cy_f07_fiftytwo_week_cycle_position_newhicnt_1260d_base_v021_signal,
    f07cy_f07_fiftytwo_week_cycle_position_newlocnt_252d_base_v022_signal,
    f07cy_f07_fiftytwo_week_cycle_position_newlocnt_1260d_base_v023_signal,
    f07cy_f07_fiftytwo_week_cycle_position_newbal_252d_base_v024_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hirate_504d_base_v025_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hiclusters_252d_base_v026_signal,
    f07cy_f07_fiftytwo_week_cycle_position_loclusters_252d_base_v027_signal,
    f07cy_f07_fiftytwo_week_cycle_position_clusterbal_504d_base_v028_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovrank_1260d_base_v029_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovshare_504d_base_v030_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovshare_1260d_base_v031_signal,
    f07cy_f07_fiftytwo_week_cycle_position_survrank_1260d_base_v032_signal,
    f07cy_f07_fiftytwo_week_cycle_position_staleasym_252d_base_v033_signal,
    f07cy_f07_fiftytwo_week_cycle_position_staleasym_1260d_base_v034_signal,
    f07cy_f07_fiftytwo_week_cycle_position_dshrank_252d_base_v035_signal,
    f07cy_f07_fiftytwo_week_cycle_position_dslrank_252d_base_v036_signal,
    f07cy_f07_fiftytwo_week_cycle_position_staleratio_504d_base_v037_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gaproot_504d_base_v038_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapvolrank_252d_base_v039_signal,
    f07cy_f07_fiftytwo_week_cycle_position_floorvolrank_252d_base_v040_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gaptanh_1260d_base_v041_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapyoy_252d_base_v042_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapdisp_252d_base_v043_signal,
    f07cy_f07_fiftytwo_week_cycle_position_flooryoy_1260d_base_v044_signal,
    f07cy_f07_fiftytwo_week_cycle_position_nearhioccup_252d_base_v045_signal,
    f07cy_f07_fiftytwo_week_cycle_position_nearlooccup_252d_base_v046_signal,
    f07cy_f07_fiftytwo_week_cycle_position_occupbal_1260d_base_v047_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hiapproaches_252d_base_v048_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hipersist_252d_base_v049_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapema_504d_base_v050_signal,
    f07cy_f07_fiftytwo_week_cycle_position_truehigaprank_252d_base_v051_signal,
    f07cy_f07_fiftytwo_week_cycle_position_truelofloorrank_252d_base_v052_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hipremium_252d_base_v053_signal,
    f07cy_f07_fiftytwo_week_cycle_position_lodiscount_252d_base_v054_signal,
    f07cy_f07_fiftytwo_week_cycle_position_truespanrank_252d_base_v055_signal,
    f07cy_f07_fiftytwo_week_cycle_position_anchbal_252d_base_v056_signal,
    f07cy_f07_fiftytwo_week_cycle_position_anchbal_1260d_base_v057_signal,
    f07cy_f07_fiftytwo_week_cycle_position_anchtilt_504d_base_v058_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapterm_252v1260_base_v059_signal,
    f07cy_f07_fiftytwo_week_cycle_position_floorterm_252v1260_base_v060_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapconvex_base_v061_signal,
    f07cy_f07_fiftytwo_week_cycle_position_belowanchfrac_252d_base_v062_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapexcursion_252d_base_v063_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovexcursion_252d_base_v064_signal,
    f07cy_f07_fiftytwo_week_cycle_position_deepgapvol_1260d_base_v065_signal,
    f07cy_f07_fiftytwo_week_cycle_position_floorvolrank_504d_base_v066_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gaprank_504long_base_v067_signal,
    f07cy_f07_fiftytwo_week_cycle_position_floorrank_252long_base_v068_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hirecency_252d_base_v069_signal,
    f07cy_f07_fiftytwo_week_cycle_position_lorecency_252d_base_v070_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recencybal_252d_base_v071_signal,
    f07cy_f07_fiftytwo_week_cycle_position_blendgapz_base_v072_signal,
    f07cy_f07_fiftytwo_week_cycle_position_floordisp_multi_base_v073_signal,
    f07cy_f07_fiftytwo_week_cycle_position_bandfracrank_252d_base_v074_signal,
    f07cy_f07_fiftytwo_week_cycle_position_netpull_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_FIFTYTWO_WEEK_CYCLE_POSITION_REGISTRY_001_075 = REGISTRY


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

    print("OK f07_fiftytwo_week_cycle_position_base_001_075_claude: %d features pass" % n_features)
