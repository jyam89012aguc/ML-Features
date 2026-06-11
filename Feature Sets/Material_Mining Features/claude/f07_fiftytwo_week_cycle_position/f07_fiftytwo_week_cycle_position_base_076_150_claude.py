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
# Same anti-overlap policy as base_001_075: anchoring GAP in z/rank/frequency forms,
# nested-anchor RELATIONSHIPS, new-high/new-low FREQUENCY counts. No raw
# proximity/drawdown/range-position level, no base-tightness/breakout.

def _f07_anchor_gap(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(close.replace(0, np.nan) / hi.replace(0, np.nan))


def _f07_floor_gap(close, w):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return np.log(close.replace(0, np.nan) / lo.replace(0, np.nan))


def _f07_newhi_events(close, w):
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
# --- Block A: shorter-horizon anchoring gap rank/z (126/63d anchors) ---

# v076 anchoring gap to the 126d high, percentile-ranked vs its 252d history
def f07cy_f07_fiftytwo_week_cycle_position_gaprank_126d_base_v076_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 126)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v077 floor gap to the 126d low, percentile-ranked vs its 252d history
def f07cy_f07_fiftytwo_week_cycle_position_floorrank_126d_base_v077_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 126)
    b = _rank(fg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v078 anchoring gap to the 126d high, z-scored vs its 126d typical depth
def f07cy_f07_fiftytwo_week_cycle_position_gapz_126d_base_v078_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 126)
    b = _z(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v079 nested-floor disagreement: 504d floor gap minus 1260d floor gap, ranked
#       (how far the two-year low sits above the five-year low -- nested floor relation)
def f07cy_f07_fiftytwo_week_cycle_position_floorz_1260d_base_v079_signal(closeadj):
    f2 = _f07_floor_gap(closeadj, 504)
    f3 = _f07_floor_gap(closeadj, 1260)
    b = _rank(f2 - f3, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v080 anchoring gap to the 504d high ranked over a short 126d window (fast deep-position percentile)
def f07cy_f07_fiftytwo_week_cycle_position_gaprank_504short_base_v080_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 504)
    b = _rank(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block B: nested-anchor relationships mixing high & low (avoid pure-high collinearity) ---

# v081 anchored band position: above-1260d-low minus below-504d-high (deep-vs-mid net position)
def f07cy_f07_fiftytwo_week_cycle_position_bandpos_504v1260_base_v081_signal(closeadj):
    g2 = _f07_anchor_gap(closeadj, 504)        # <= 0
    f3 = _f07_floor_gap(closeadj, 1260)        # >= 0
    b = f3 + g2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v082 anchored band position over the 126d-high / 504d-low pair, z-scored
def f07cy_f07_fiftytwo_week_cycle_position_bandpos_126v504_base_v082_signal(closeadj):
    g1 = _f07_anchor_gap(closeadj, 126)
    f2 = _f07_floor_gap(closeadj, 504)
    b = _z(f2 + g1, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v083 deep overhead vs near floor: log(1260d high / 504d low) (multi-year overhead span, mid floor)
def f07cy_f07_fiftytwo_week_cycle_position_overhead_1260v504_base_v083_signal(closeadj):
    hi3 = _rmax(closeadj, 1260)
    lo2 = _rmin(closeadj, 504)
    b = np.log(hi3.replace(0, np.nan) / lo2.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v084 nested-band fraction: where price sits in the 1260d band but measured vs the 252d band width
def f07cy_f07_fiftytwo_week_cycle_position_nestfrac_base_v084_signal(closeadj):
    f3 = _f07_floor_gap(closeadj, 1260)        # above 5y low
    width1 = np.log(_rmax(closeadj, 252).replace(0, np.nan) / _rmin(closeadj, 252).replace(0, np.nan))
    b = f3 / width1.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v085 span ratio: 504d log-span as a fraction of 1260d log-span (mid vs deep amplitude)
def f07cy_f07_fiftytwo_week_cycle_position_spanratio_504v1260_base_v085_signal(closeadj):
    s2 = np.log(_rmax(closeadj, 504).replace(0, np.nan) / _rmin(closeadj, 504).replace(0, np.nan))
    s3 = np.log(_rmax(closeadj, 1260).replace(0, np.nan) / _rmin(closeadj, 1260).replace(0, np.nan))
    b = s2 / s3.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block C: new-high / new-low FREQUENCY counts at additional horizons ---

# v086 count of fresh 126d highs in the trailing quarter
def f07cy_f07_fiftytwo_week_cycle_position_newhicnt_126d_base_v086_signal(closeadj):
    ev = _f07_newhi_events(closeadj, 126)
    b = ev.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v087 fresh-504d-high spacing: average bars between consecutive new two-year highs over the year
def f07cy_f07_fiftytwo_week_cycle_position_newhicnt_504y_base_v087_signal(closeadj):
    ev = _f07_newhi_events(closeadj, 504)
    cnt = ev.rolling(252, min_periods=63).sum()
    b = 252.0 / (cnt + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v088 fresh-126d-low tally over the quarter blended with continuous nearness to the low
def f07cy_f07_fiftytwo_week_cycle_position_newlocnt_126d_base_v088_signal(closeadj):
    ev = _f07_newlo_events(closeadj, 126)
    cnt = ev.rolling(63, min_periods=21).sum()
    nearness = _f07_nearness_lo(closeadj, 126).rolling(21, min_periods=7).mean()
    b = cnt + 5.0 * nearness
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v089 fresh-504d-low tally over the year, blended with nearness to the two-year low
def f07cy_f07_fiftytwo_week_cycle_position_newlocnt_504d_base_v089_signal(closeadj):
    ev = _f07_newlo_events(closeadj, 504)
    cnt = ev.rolling(252, min_periods=63).sum()
    nearness = _f07_nearness_lo(closeadj, 504).rolling(63, min_periods=21).mean()
    b = cnt + 5.0 * nearness
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v090 new-high frequency MOMENTUM: change in the trailing-quarter new-252d-high count over a quarter
def f07cy_f07_fiftytwo_week_cycle_position_hifreqmom_252d_base_v090_signal(closeadj):
    cnt = _f07_newhi_events(closeadj, 252).rolling(63, min_periods=21).sum()
    b = cnt - cnt.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v091 multi-year new-high spacing: average bars between consecutive 1260d highs over the year
def f07cy_f07_fiftytwo_week_cycle_position_hirate_1260d_base_v091_signal(closeadj):
    ev = _f07_newhi_events(closeadj, 1260)
    cnt = ev.rolling(252, min_periods=63).sum()
    b = 252.0 / (cnt + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v092 fresh-high gaps: average spacing between consecutive new-252d-high events (sparser => weaker)
def f07cy_f07_fiftytwo_week_cycle_position_hispacing_252d_base_v092_signal(closeadj):
    ev = _f07_newhi_events(closeadj, 252)
    cnt = ev.rolling(252, min_periods=63).sum()
    b = 252.0 / (cnt + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v093 new-low fraction of all extreme events over the trailing year (down-pressure share)
def f07cy_f07_fiftytwo_week_cycle_position_loshare_252d_base_v093_signal(closeadj):
    hi = _f07_newhi_events(closeadj, 252).rolling(252, min_periods=63).sum()
    lo = _f07_newlo_events(closeadj, 252).rolling(252, min_periods=63).sum()
    base_lo = _f07_nearness_lo(closeadj, 252).rolling(21, min_periods=7).mean()
    b = (lo + base_lo) / (hi + lo + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block D: staleness / recency in transformed forms (not bare days-since) ---

# v094 high-anchor staleness over the 504d window, z-scored vs its 252d history
def f07cy_f07_fiftytwo_week_cycle_position_dshz_504d_base_v094_signal(closeadj):
    dh = _f07_days_since_hi(closeadj, 504)
    b = _z(dh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v095 low-anchor staleness over the 1260d window, z-scored vs its 252d history
def f07cy_f07_fiftytwo_week_cycle_position_dslz_1260d_base_v095_signal(closeadj):
    dl = _f07_days_since_lo(closeadj, 1260)
    b = _z(dl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v096 staleness-asymmetry ratio: days-since-high vs days-since-low at the 252d horizon (turnover)
def f07cy_f07_fiftytwo_week_cycle_position_stalexdepth_252d_base_v096_signal(closeadj):
    dh = _f07_days_since_hi(closeadj, 252)
    dl = _f07_days_since_lo(closeadj, 252)
    b = (dh + 0.02) / (dl + 0.02)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v097 leadership-decay interaction: new-high recency times below-high depth (stale & far from anchor)
def f07cy_f07_fiftytwo_week_cycle_position_lorecxheight_252d_base_v097_signal(closeadj):
    ev = _f07_newhi_events(closeadj, 252)
    age = _f07_last_event_age(ev, 252)
    depth = (-_f07_anchor_gap(closeadj, 252)).clip(lower=0)
    b = np.log1p(age) * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v098 staleness asymmetry over the 504d window (which anchor is fresher at the two-year scale)
def f07cy_f07_fiftytwo_week_cycle_position_staleasym_504d_base_v098_signal(closeadj):
    dh = _f07_days_since_hi(closeadj, 504)
    dl = _f07_days_since_lo(closeadj, 504)
    b = dh - dl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block E: anchor-gap momentum / YoY at additional horizons ---

# v099 504d anchoring gap now vs one year ago (multi-year YoY anchor shift)
def f07cy_f07_fiftytwo_week_cycle_position_gapyoy_504d_base_v099_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 504)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v100 126d anchoring gap displacement from its own 63d EMA (fast anchor displacement)
def f07cy_f07_fiftytwo_week_cycle_position_gapdisp_126d_base_v100_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 126)
    b = g - g.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v101 504d floor gap displacement from its own 126d EMA (recovery-position displacement)
def f07cy_f07_fiftytwo_week_cycle_position_floordisp_504d_base_v101_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 504)
    b = fg - fg.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v102 252d floor gap year-over-year change (recovery position vs one year ago)
def f07cy_f07_fiftytwo_week_cycle_position_flooryoy_252d_base_v102_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 252)
    b = fg - fg.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block F: occupancy / time-in-zone of the anchored band at new bands ---

# v103 fraction of the trailing half-year within 10% of the 504d high (mid-anchor leadership occupancy)
def f07cy_f07_fiftytwo_week_cycle_position_nearhioccup_504d_base_v103_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 504)
    near = (g >= np.log(0.90)).astype(float)
    b = near.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v104 fraction of the trailing half-year within 10% of the 504d low (mid-anchor basing occupancy)
def f07cy_f07_fiftytwo_week_cycle_position_nearlooccup_504d_base_v104_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 504)
    near = (fg <= np.log(1.10)).astype(float)
    b = near.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v105 entries into the near-low zone over the trailing year (distinct tests of the floor)
def f07cy_f07_fiftytwo_week_cycle_position_loapproaches_252d_base_v105_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 252)
    near = (fg <= np.log(1.05)).astype(float)
    entries = ((near == 1) & (near.shift(1) == 0)).astype(float)
    cnt = entries.rolling(252, min_periods=63).sum()
    nearness = _f07_nearness_lo(closeadj, 252).rolling(42, min_periods=14).mean()
    b = cnt + 5.0 * nearness
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v106 mid-band occupancy: fraction of trailing year spent neither near high nor near low (1260d)
def f07cy_f07_fiftytwo_week_cycle_position_midoccup_1260d_base_v106_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 1260)
    fg = _f07_floor_gap(closeadj, 1260)
    mid = ((g < np.log(0.90)) & (fg > np.log(1.10))).astype(float)
    b = mid.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block G: anchor-band balance & tilt at new horizons ---

# v107 anchor-band balance at the 504d horizon, z-scored (where in the two-year band)
def f07cy_f07_fiftytwo_week_cycle_position_anchbal_504d_base_v107_signal(closeadj):
    g = (-_f07_anchor_gap(closeadj, 504)).clip(lower=1e-6)
    fg = (_f07_floor_gap(closeadj, 504)).clip(lower=1e-6)
    bal = (fg - g) / (fg + g)
    b = _z(bal, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v108 anchor-band tilt momentum at the 1260d horizon, change over a half-year
def f07cy_f07_fiftytwo_week_cycle_position_anchtilt_1260d_base_v108_signal(closeadj):
    g = (-_f07_anchor_gap(closeadj, 1260)).clip(lower=1e-6)
    fg = (_f07_floor_gap(closeadj, 1260)).clip(lower=1e-6)
    bal = (fg - g) / (fg + g)
    b = bal - bal.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v109 band-balance YoY: 252d band-balance now minus one year ago (cycle-position turnover)
def f07cy_f07_fiftytwo_week_cycle_position_anchbalrank_252d_base_v109_signal(closeadj):
    g = (-_f07_anchor_gap(closeadj, 252)).clip(lower=1e-6)
    fg = (_f07_floor_gap(closeadj, 252)).clip(lower=1e-6)
    bal = (fg - g) / (fg + g)
    b = bal - bal.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block H: cross-window term structure / convexity (mixed sides) ---

# v110 floor-gap term structure: 126d floor relative to 504d floor (near vs mid recovery)
def f07cy_f07_fiftytwo_week_cycle_position_floorterm_126v504_base_v110_signal(closeadj):
    f1 = _f07_floor_gap(closeadj, 126)
    f2 = _f07_floor_gap(closeadj, 504)
    b = f1 / f2.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v111 anchor-gap term structure: 126d gap relative to 504d gap (near vs mid below-high depth)
def f07cy_f07_fiftytwo_week_cycle_position_gapterm_126v504_base_v111_signal(closeadj):
    g1 = _f07_anchor_gap(closeadj, 126)
    g2 = _f07_anchor_gap(closeadj, 504)
    b = g1 / g2.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v112 band-balance convexity: 504d balance minus average of 252d & 1260d balances (curvature)
def f07cy_f07_fiftytwo_week_cycle_position_balconvex_base_v112_signal(closeadj):
    def _bal(w):
        g = (-_f07_anchor_gap(closeadj, w)).clip(lower=1e-6)
        fg = (_f07_floor_gap(closeadj, w)).clip(lower=1e-6)
        return (fg - g) / (fg + g)
    b = _bal(504) - 0.5 * (_bal(252) + _bal(1260))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block I: risk-adjusted & nonlinear position forms ---

# v113 126d anchoring gap per unit of realized risk, change over a month (fast risk-position momentum)
def f07cy_f07_fiftytwo_week_cycle_position_gapvolz_126d_base_v113_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 126)
    vol = closeadj.pct_change().rolling(42, min_periods=14).std()
    ratio = g / vol.replace(0, np.nan)
    b = ratio - ratio.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v114 504d floor gap tanh-bounded level (squashed multi-year recovery position)
def f07cy_f07_fiftytwo_week_cycle_position_floortanh_504d_base_v114_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 504)
    b = np.tanh(2.0 * fg) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v115 252d anchoring gap signed-root displacement from its typical level (compressed extremity)
def f07cy_f07_fiftytwo_week_cycle_position_gaproot_252d_base_v115_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 252)
    root = np.sign(g) * (g.abs() ** 0.5)
    b = root - root.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v116 1260d floor gap per unit of long risk, ranked (deep risk-scaled recovery percentile)
def f07cy_f07_fiftytwo_week_cycle_position_floorvolrank_1260d_base_v116_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 1260)
    vol = closeadj.pct_change().rolling(252, min_periods=63).std()
    ratio = fg / vol.replace(0, np.nan)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block J: intraday true-high/true-low anchoring at additional forms ---

# v117 true-high anchoring gap to the 504d intraday high, ranked vs 504d history
def f07cy_f07_fiftytwo_week_cycle_position_truehigap_504d_base_v117_signal(closeadj, high):
    hi = high.rolling(504, min_periods=252).max()
    g = np.log(closeadj.replace(0, np.nan) / hi.replace(0, np.nan))
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v118 true-high anchor gap to the 504d intraday high, displaced from its own 126d EMA (leadership pulse)
def f07cy_f07_fiftytwo_week_cycle_position_truelofloor_504d_base_v118_signal(closeadj, high):
    hi = high.rolling(504, min_periods=252).max()
    g = np.log(closeadj.replace(0, np.nan) / hi.replace(0, np.nan))
    b = g - g.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v119 intraday anchored-band balance (true 252d high vs true 252d low), z-scored
def f07cy_f07_fiftytwo_week_cycle_position_truebal_252d_base_v119_signal(closeadj, high, low):
    hi = high.rolling(252, min_periods=126).max()
    lo = low.rolling(252, min_periods=126).min()
    g = (-np.log(closeadj.replace(0, np.nan) / hi.replace(0, np.nan))).clip(lower=1e-6)
    fg = (np.log(closeadj.replace(0, np.nan) / lo.replace(0, np.nan))).clip(lower=1e-6)
    bal = (fg - g) / (fg + g)
    b = _z(bal, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v120 intraday cycle-span at the 504d horizon (true high/low), displaced from its 126d EMA
def f07cy_f07_fiftytwo_week_cycle_position_truespan_1260d_base_v120_signal(closeadj, high, low):
    hi = high.rolling(504, min_periods=252).max()
    lo = low.rolling(504, min_periods=252).min()
    span = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    b = span - span.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block K: anchor-gap excursion / regime occupancy counts at new thresholds ---

# v121 below-anchor regime fraction: fraction of trailing year deeper than -30% from the 252d high
def f07cy_f07_fiftytwo_week_cycle_position_deepregime_252d_base_v121_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 252)
    deep = (g <= np.log(0.70)).astype(float)
    frac = deep.rolling(252, min_periods=63).mean()
    cushion = (-(g - np.log(0.70))).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + 3.0 * cushion
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v122 recovery regime fraction: fraction of trailing year more than +50% above the 1260d low
def f07cy_f07_fiftytwo_week_cycle_position_recovregime_1260d_base_v122_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 1260)
    up = (fg >= np.log(1.50)).astype(float)
    b = up.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v123 new-low cluster count at the 504d horizon, blended with nearness (multi-year capitulation tally)
def f07cy_f07_fiftytwo_week_cycle_position_loclusters_504d_base_v123_signal(closeadj):
    ev = _f07_newlo_events(closeadj, 504)
    starts = ((ev == 1) & (ev.shift(1) == 0)).astype(float)
    cnt = starts.rolling(252, min_periods=63).sum()
    nearness = _f07_nearness_lo(closeadj, 504).rolling(63, min_periods=21).mean()
    b = cnt + 5.0 * nearness
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v124 deep new-low cluster tally at the 756d horizon, blended with de-trended floor displacement
def f07cy_f07_fiftytwo_week_cycle_position_hiclusters_1260d_base_v124_signal(closeadj):
    ev = _f07_newlo_events(closeadj, 756)
    starts = ((ev == 1) & (ev.shift(1) == 0)).astype(float)
    cnt = starts.rolling(252, min_periods=63).sum()
    fg = _f07_floor_gap(closeadj, 756)
    disp = (fg - fg.ewm(span=189, min_periods=63).mean())
    b = cnt + 3.0 * disp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block L: anchor-gap smoothing / persistence at new horizons ---

# v125 504d anchor-gap EMA term spread (fast minus slow two-year anchor mean reversion)
def f07cy_f07_fiftytwo_week_cycle_position_gapema_252d_base_v125_signal(closeadj):
    g = _f07_anchor_gap(closeadj, 252)
    b = g.ewm(span=21, min_periods=7).mean() - g.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v126 persistence-weighted floor proximity: how long & deep price has hugged the 252d low
def f07cy_f07_fiftytwo_week_cycle_position_lopersist_252d_base_v126_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 252)
    persist = (fg <= np.log(1.08)).astype(float).rolling(63, min_periods=21).mean()
    nearness = (np.log(1.08) - fg).clip(lower=0).rolling(21, min_periods=7).mean()
    b = persist * nearness
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v127 anchor-band balance EMA (slow, persistent cycle-position level)
def f07cy_f07_fiftytwo_week_cycle_position_balema_504d_base_v127_signal(closeadj):
    g = (-_f07_anchor_gap(closeadj, 504)).clip(lower=1e-6)
    fg = (_f07_floor_gap(closeadj, 504)).clip(lower=1e-6)
    bal = (fg - g) / (fg + g)
    b = bal.ewm(span=63, min_periods=21).mean() - bal.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block M: nested-span dynamics & cycle amplitude (mixed, ranked/momentum) ---

# v128 multi-year span momentum: change in log(1260d high/low) over a half-year (amplitude expansion)
def f07cy_f07_fiftytwo_week_cycle_position_spanmom_1260d_base_v128_signal(closeadj):
    span = np.log(_rmax(closeadj, 1260).replace(0, np.nan) / _rmin(closeadj, 1260).replace(0, np.nan))
    b = span - span.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v129 252d span ranked vs its own 504d history (where current amplitude sits historically)
def f07cy_f07_fiftytwo_week_cycle_position_spanrank_252d_base_v129_signal(closeadj):
    span = np.log(_rmax(closeadj, 252).replace(0, np.nan) / _rmin(closeadj, 252).replace(0, np.nan))
    b = _rank(span, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v130 overhead-span momentum: change in log(1260d high / 252d low) over a quarter
def f07cy_f07_fiftytwo_week_cycle_position_overheadmom_base_v130_signal(closeadj):
    ov = np.log(_rmax(closeadj, 1260).replace(0, np.nan) / _rmin(closeadj, 252).replace(0, np.nan))
    b = ov - ov.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block N: composite cycle-position net-pull & blends ---

# v131 net pull at the 504d horizon: anchor-gap rank minus floor-gap rank
def f07cy_f07_fiftytwo_week_cycle_position_netpull_504d_base_v131_signal(closeadj):
    gr = _rank(_f07_anchor_gap(closeadj, 504), 504)
    fr = _rank(_f07_floor_gap(closeadj, 504), 504)
    b = gr - fr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v132 blended floor gap: average of 252/504/1260 floor gaps, z-scored (composite recovery height)
def f07cy_f07_fiftytwo_week_cycle_position_blendfloorz_base_v132_signal(closeadj):
    f1 = _f07_floor_gap(closeadj, 252)
    f2 = _f07_floor_gap(closeadj, 504)
    f3 = _f07_floor_gap(closeadj, 1260)
    blend = (f1 + f2 + f3) / 3.0
    b = _z(blend, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v133 anchor-gap range across horizons (max-min of 126/504/1260 gaps), ranked (anchor disagreement)
def f07cy_f07_fiftytwo_week_cycle_position_gaprangerank_base_v133_signal(closeadj):
    g1 = _f07_anchor_gap(closeadj, 126)
    g2 = _f07_anchor_gap(closeadj, 504)
    g3 = _f07_anchor_gap(closeadj, 1260)
    stk = pd.concat([g1, g2, g3], axis=1)
    spread = stk.max(axis=1) - stk.min(axis=1)
    b = _rank(spread, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block O: continuous nearness-to-anchor (smooth proximity, distinct from raw level) ---

# v134 smoothed nearness to the 252d high, ranked vs its 504d history (leadership-proximity percentile)
def f07cy_f07_fiftytwo_week_cycle_position_hinearpulse_252d_base_v134_signal(closeadj):
    nh = _f07_nearness_hi(closeadj, 252).rolling(21, min_periods=7).mean()
    b = _rank(nh, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v135 smoothed nearness to the 1260d low, change over a half-year (deep-basing momentum)
def f07cy_f07_fiftytwo_week_cycle_position_lonearz_1260d_base_v135_signal(closeadj):
    nl = _f07_nearness_lo(closeadj, 1260).rolling(21, min_periods=7).mean()
    b = nl - nl.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v136 nearness balance: smoothed nearness-to-high minus nearness-to-low (252d), de-trended
def f07cy_f07_fiftytwo_week_cycle_position_nearbal_252d_base_v136_signal(closeadj):
    nh = _f07_nearness_hi(closeadj, 252)
    nl = _f07_nearness_lo(closeadj, 252)
    bal = (nh - nl).rolling(21, min_periods=7).mean()
    b = bal - bal.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block P: anchor-gap percentile interactions & recency balance ---

# v137 504d anchor gap ranked, minus 1260d anchor gap ranked (cross-horizon position divergence)
def f07cy_f07_fiftytwo_week_cycle_position_rankdiv_504v1260_base_v137_signal(closeadj):
    r2 = _rank(_f07_anchor_gap(closeadj, 504), 504)
    r3 = _rank(_f07_anchor_gap(closeadj, 1260), 756)
    b = r2 - r3
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v138 recency balance at the 504d horizon: new-low age vs new-high age, normalized
def f07cy_f07_fiftytwo_week_cycle_position_recencybal_504d_base_v138_signal(closeadj):
    hev = _f07_newhi_events(closeadj, 504)
    lev = _f07_newlo_events(closeadj, 504)
    ha = _f07_last_event_age(hev, 504)
    la = _f07_last_event_age(lev, 504)
    b = (la - ha) / (la + ha + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v139 fresh-high recency at the 1260d horizon, log-bars since the last multi-year high
def f07cy_f07_fiftytwo_week_cycle_position_hirecency_1260d_base_v139_signal(closeadj):
    ev = _f07_newhi_events(closeadj, 1260)
    age = _f07_last_event_age(ev, 1260)
    b = np.log1p(age)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block Q: deep-value / survival-position composites (ranked, mixed) ---

# v140 deep-value position: 1260d anchor gap ranked, gated by being above the 1260d low (solvent-cheap)
def f07cy_f07_fiftytwo_week_cycle_position_deepvalue_1260d_base_v140_signal(closeadj):
    gr = _rank(_f07_anchor_gap(closeadj, 1260), 756)
    surv = np.log(closeadj.replace(0, np.nan) / _rmin(closeadj, 1260).replace(0, np.nan))
    gate = (surv > 0.05).astype(float)
    b = gr * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v141 cycle-position net pull at the 1260d horizon (deep top-vs-bottom net)
def f07cy_f07_fiftytwo_week_cycle_position_netpull_1260d_base_v141_signal(closeadj):
    gr = _rank(_f07_anchor_gap(closeadj, 1260), 756)
    fr = _rank(_f07_floor_gap(closeadj, 1260), 756)
    b = gr - fr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v142 survival-multiple displacement: log(price/1260d-low) minus its 252d EMA, z-scored
def f07cy_f07_fiftytwo_week_cycle_position_survdisp_1260d_base_v142_signal(closeadj):
    surv = np.log(closeadj.replace(0, np.nan) / _rmin(closeadj, 1260).replace(0, np.nan))
    disp = surv - surv.ewm(span=252, min_periods=63).mean()
    b = _z(disp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block R: anchored-range fraction (ranked/momentum) avoiding raw range-position level ---

# v143 distance-above-low band fraction at the 504d horizon, displaced from its 126d EMA
def f07cy_f07_fiftytwo_week_cycle_position_bandfracrank_504d_base_v143_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 504)
    span = np.log(_rmax(closeadj, 504).replace(0, np.nan) / _rmin(closeadj, 504).replace(0, np.nan))
    frac = fg / span.replace(0, np.nan)
    b = frac - frac.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v144 multi-year new-low spacing: average bars between consecutive 1260d lows over the year
#       (sparser deep capitulations => stronger; a count-friendly multi-year floor signal)
def f07cy_f07_fiftytwo_week_cycle_position_bandfracmom_1260d_base_v144_signal(closeadj):
    ev = _f07_newlo_events(closeadj, 1260)
    cnt = ev.rolling(252, min_periods=63).sum()
    spacing = 252.0 / (cnt + 1.0)
    nearness = _f07_nearness_lo(closeadj, 1260).rolling(63, min_periods=21).mean()
    b = spacing - 200.0 * nearness
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v145 band-fraction displacement at the 252d horizon from its own EMA (anchored-position pulse)
def f07cy_f07_fiftytwo_week_cycle_position_bandfracdisp_252d_base_v145_signal(closeadj):
    fg = _f07_floor_gap(closeadj, 252)
    span = np.log(_rmax(closeadj, 252).replace(0, np.nan) / _rmin(closeadj, 252).replace(0, np.nan))
    frac = fg / span.replace(0, np.nan)
    b = frac - frac.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Block S: multi-horizon dispersion & blended counts ---

# v146 anchor-gap dispersion across the SHORT horizons 63/126/252 (near-term anchor disagreement)
def f07cy_f07_fiftytwo_week_cycle_position_gapdisp_short_base_v146_signal(closeadj):
    g1 = _f07_anchor_gap(closeadj, 63)
    g2 = _f07_anchor_gap(closeadj, 126)
    g3 = _f07_anchor_gap(closeadj, 252)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v147 new-high breadth dispersion across 126/252/1260 horizons (disagreement in leadership)
def f07cy_f07_fiftytwo_week_cycle_position_hicntblend_base_v147_signal(closeadj):
    c1 = _f07_newhi_events(closeadj, 126).rolling(252, min_periods=63).mean()
    c2 = _f07_newhi_events(closeadj, 252).rolling(252, min_periods=63).mean()
    c3 = _f07_newhi_events(closeadj, 1260).rolling(252, min_periods=63).mean()
    b = pd.concat([c1, c2, c3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v148 anchor-gap convexity over short horizons 63/126/252 (near-term curvature)
def f07cy_f07_fiftytwo_week_cycle_position_gapconvex_short_base_v148_signal(closeadj):
    g1 = _f07_anchor_gap(closeadj, 63)
    g2 = _f07_anchor_gap(closeadj, 126)
    g3 = _f07_anchor_gap(closeadj, 252)
    b = g2 - 0.5 * (g1 + g3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v149 staleness asymmetry ranked: (days-since-high - days-since-low) over 252d, percentile-ranked
def f07cy_f07_fiftytwo_week_cycle_position_staleasymrank_252d_base_v149_signal(closeadj):
    dh = _f07_days_since_hi(closeadj, 252)
    dl = _f07_days_since_lo(closeadj, 252)
    b = _rank(dh - dl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v150 composite cycle position: blend of band-balance(252/504/1260) z-scored (multi-horizon position)
def f07cy_f07_fiftytwo_week_cycle_position_blendbalz_base_v150_signal(closeadj):
    def _bal(w):
        g = (-_f07_anchor_gap(closeadj, w)).clip(lower=1e-6)
        fg = (_f07_floor_gap(closeadj, w)).clip(lower=1e-6)
        return (fg - g) / (fg + g)
    blend = (_bal(252) + _bal(504) + _bal(1260)) / 3.0
    b = _z(blend, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07cy_f07_fiftytwo_week_cycle_position_gaprank_126d_base_v076_signal,
    f07cy_f07_fiftytwo_week_cycle_position_floorrank_126d_base_v077_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapz_126d_base_v078_signal,
    f07cy_f07_fiftytwo_week_cycle_position_floorz_1260d_base_v079_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gaprank_504short_base_v080_signal,
    f07cy_f07_fiftytwo_week_cycle_position_bandpos_504v1260_base_v081_signal,
    f07cy_f07_fiftytwo_week_cycle_position_bandpos_126v504_base_v082_signal,
    f07cy_f07_fiftytwo_week_cycle_position_overhead_1260v504_base_v083_signal,
    f07cy_f07_fiftytwo_week_cycle_position_nestfrac_base_v084_signal,
    f07cy_f07_fiftytwo_week_cycle_position_spanratio_504v1260_base_v085_signal,
    f07cy_f07_fiftytwo_week_cycle_position_newhicnt_126d_base_v086_signal,
    f07cy_f07_fiftytwo_week_cycle_position_newhicnt_504y_base_v087_signal,
    f07cy_f07_fiftytwo_week_cycle_position_newlocnt_126d_base_v088_signal,
    f07cy_f07_fiftytwo_week_cycle_position_newlocnt_504d_base_v089_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hifreqmom_252d_base_v090_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hirate_1260d_base_v091_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hispacing_252d_base_v092_signal,
    f07cy_f07_fiftytwo_week_cycle_position_loshare_252d_base_v093_signal,
    f07cy_f07_fiftytwo_week_cycle_position_dshz_504d_base_v094_signal,
    f07cy_f07_fiftytwo_week_cycle_position_dslz_1260d_base_v095_signal,
    f07cy_f07_fiftytwo_week_cycle_position_stalexdepth_252d_base_v096_signal,
    f07cy_f07_fiftytwo_week_cycle_position_lorecxheight_252d_base_v097_signal,
    f07cy_f07_fiftytwo_week_cycle_position_staleasym_504d_base_v098_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapyoy_504d_base_v099_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapdisp_126d_base_v100_signal,
    f07cy_f07_fiftytwo_week_cycle_position_floordisp_504d_base_v101_signal,
    f07cy_f07_fiftytwo_week_cycle_position_flooryoy_252d_base_v102_signal,
    f07cy_f07_fiftytwo_week_cycle_position_nearhioccup_504d_base_v103_signal,
    f07cy_f07_fiftytwo_week_cycle_position_nearlooccup_504d_base_v104_signal,
    f07cy_f07_fiftytwo_week_cycle_position_loapproaches_252d_base_v105_signal,
    f07cy_f07_fiftytwo_week_cycle_position_midoccup_1260d_base_v106_signal,
    f07cy_f07_fiftytwo_week_cycle_position_anchbal_504d_base_v107_signal,
    f07cy_f07_fiftytwo_week_cycle_position_anchtilt_1260d_base_v108_signal,
    f07cy_f07_fiftytwo_week_cycle_position_anchbalrank_252d_base_v109_signal,
    f07cy_f07_fiftytwo_week_cycle_position_floorterm_126v504_base_v110_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapterm_126v504_base_v111_signal,
    f07cy_f07_fiftytwo_week_cycle_position_balconvex_base_v112_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapvolz_126d_base_v113_signal,
    f07cy_f07_fiftytwo_week_cycle_position_floortanh_504d_base_v114_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gaproot_252d_base_v115_signal,
    f07cy_f07_fiftytwo_week_cycle_position_floorvolrank_1260d_base_v116_signal,
    f07cy_f07_fiftytwo_week_cycle_position_truehigap_504d_base_v117_signal,
    f07cy_f07_fiftytwo_week_cycle_position_truelofloor_504d_base_v118_signal,
    f07cy_f07_fiftytwo_week_cycle_position_truebal_252d_base_v119_signal,
    f07cy_f07_fiftytwo_week_cycle_position_truespan_1260d_base_v120_signal,
    f07cy_f07_fiftytwo_week_cycle_position_deepregime_252d_base_v121_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovregime_1260d_base_v122_signal,
    f07cy_f07_fiftytwo_week_cycle_position_loclusters_504d_base_v123_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hiclusters_1260d_base_v124_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapema_252d_base_v125_signal,
    f07cy_f07_fiftytwo_week_cycle_position_lopersist_252d_base_v126_signal,
    f07cy_f07_fiftytwo_week_cycle_position_balema_504d_base_v127_signal,
    f07cy_f07_fiftytwo_week_cycle_position_spanmom_1260d_base_v128_signal,
    f07cy_f07_fiftytwo_week_cycle_position_spanrank_252d_base_v129_signal,
    f07cy_f07_fiftytwo_week_cycle_position_overheadmom_base_v130_signal,
    f07cy_f07_fiftytwo_week_cycle_position_netpull_504d_base_v131_signal,
    f07cy_f07_fiftytwo_week_cycle_position_blendfloorz_base_v132_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gaprangerank_base_v133_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hinearpulse_252d_base_v134_signal,
    f07cy_f07_fiftytwo_week_cycle_position_lonearz_1260d_base_v135_signal,
    f07cy_f07_fiftytwo_week_cycle_position_nearbal_252d_base_v136_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rankdiv_504v1260_base_v137_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recencybal_504d_base_v138_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hirecency_1260d_base_v139_signal,
    f07cy_f07_fiftytwo_week_cycle_position_deepvalue_1260d_base_v140_signal,
    f07cy_f07_fiftytwo_week_cycle_position_netpull_1260d_base_v141_signal,
    f07cy_f07_fiftytwo_week_cycle_position_survdisp_1260d_base_v142_signal,
    f07cy_f07_fiftytwo_week_cycle_position_bandfracrank_504d_base_v143_signal,
    f07cy_f07_fiftytwo_week_cycle_position_bandfracmom_1260d_base_v144_signal,
    f07cy_f07_fiftytwo_week_cycle_position_bandfracdisp_252d_base_v145_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapdisp_short_base_v146_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hicntblend_base_v147_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapconvex_short_base_v148_signal,
    f07cy_f07_fiftytwo_week_cycle_position_staleasymrank_252d_base_v149_signal,
    f07cy_f07_fiftytwo_week_cycle_position_blendbalz_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_FIFTYTWO_WEEK_CYCLE_POSITION_REGISTRY_076_150 = REGISTRY


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

    print("OK f07_fiftytwo_week_cycle_position_base_076_150_claude: %d features pass" % n_features)
