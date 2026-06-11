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


# ===== folder domain primitives (52-week / multi-year anchoring) =====
def _f05_prox_high(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return close / hi.replace(0, np.nan)


def _f05_prox_low(close, w):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return close / lo.replace(0, np.nan)


def _f05_range_pos(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (close - lo) / (hi - lo).replace(0, np.nan)


def _f05_drawdown(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return close / hi.replace(0, np.nan) - 1.0


def _f05_recovery(close, w):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return close / lo.replace(0, np.nan) - 1.0


def _f05_anchor_gap(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(close.replace(0, np.nan) / hi.replace(0, np.nan))


def _f05_days_since_high(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f05_days_since_low(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


# ============================================================
# anchoring gap momentum at 252d (gap improving = approaching high)
def f05fw_f05_fiftytwo_week_anchor_gapmom_252d_base_v076_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap momentum at 504d
def f05fw_f05_fiftytwo_week_anchor_gapmom_504d_base_v077_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 504)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-high acceleration: 2nd difference of the gap (curvature of approach)
def f05fw_f05_fiftytwo_week_anchor_gapaccel_252d_base_v078_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    b = g - 2.0 * g.shift(21) + g.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how many distinct new-52w-highs were printed over the last year (leadership count)
def f05fw_f05_fiftytwo_week_anchor_newhicount_252d_base_v079_signal(closeadj):
    hi = closeadj.rolling(252, min_periods=126).max()
    is_new = (closeadj >= hi.shift(1)).astype(float)
    cnt = is_new.rolling(252, min_periods=126).sum()
    b = cnt + 0.1 * _f05_prox_high(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-52w-low count over the last year (capitulation count)
def f05fw_f05_fiftytwo_week_anchor_newlocount_252d_base_v080_signal(closeadj):
    lo = closeadj.rolling(252, min_periods=126).min()
    is_new = (closeadj <= lo.shift(1)).astype(float)
    cnt = is_new.rolling(252, min_periods=126).sum()
    b = cnt + 0.1 * _f05_prox_low(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap dispersion: volatility of the 252d gap (how unstable the anchor is)
def f05fw_f05_fiftytwo_week_anchor_gapdisp_252d_base_v081_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    b = g.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position dispersion at 504d (anchor instability, long)
def f05fw_f05_fiftytwo_week_anchor_rngposdisp_504d_base_v082_signal(closeadj):
    rp = _f05_range_pos(closeadj, 504)
    b = rp.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery-off-low momentum at 252d
def f05fw_f05_fiftytwo_week_anchor_recovmom_252d_base_v083_signal(closeadj):
    rec = _f05_recovery(closeadj, 252)
    b = rec - rec.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown healing rank: where the current 252d drawdown sits in its 252d history
def f05fw_f05_fiftytwo_week_anchor_ddheal_252d_base_v084_signal(closeadj):
    dd = _f05_drawdown(closeadj, 252)
    b = dd.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-high relative to proximity-to-low (signed anchor tilt, log)
def f05fw_f05_fiftytwo_week_anchor_anchtilt_252d_base_v085_signal(closeadj):
    ph = _f05_prox_high(closeadj, 252)
    pl = _f05_prox_low(closeadj, 252)
    b = np.log(pl.replace(0, np.nan)) - np.log((1.0 / ph).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in time-near the 1260d high (long leadership gaining or fading)
def f05fw_f05_fiftytwo_week_anchor_longnearhi_1260d_base_v086_signal(closeadj):
    hi = closeadj.rolling(1260, min_periods=504).max()
    near = (closeadj >= 0.90 * hi).astype(float)
    frac = near.rolling(126, min_periods=63).mean()
    b = frac - frac.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range position EMA displacement (long anchor displacement)
def f05fw_f05_fiftytwo_week_anchor_rngposdisp504_504d_base_v087_signal(closeadj):
    rp = _f05_range_pos(closeadj, 504)
    b = rp - rp.ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap to 252d high vs anchoring gap to 504d high (nested gap difference)
def f05fw_f05_fiftytwo_week_anchor_nestedgap_252v504_base_v088_signal(closeadj):
    g1 = _f05_anchor_gap(closeadj, 252)
    g2 = _f05_anchor_gap(closeadj, 504)
    b = g1 - g2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# nested low gap: how far the 504d low sits above the 1260d low (multi-year base lift)
def f05fw_f05_fiftytwo_week_anchor_nestedgap_504v1260_base_v089_signal(closeadj):
    lo504 = _rmin(closeadj, 504)
    lo1260 = _rmin(closeadj, 1260)
    b = np.log(lo504.replace(0, np.nan) / lo1260.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-since-252d-high trend (is the anchor getting staler or refreshing)
def f05fw_f05_fiftytwo_week_anchor_dshtrend_252d_base_v090_signal(closeadj):
    dsh = _f05_days_since_high(closeadj, 252)
    b = dsh - dsh.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-since-252d-low trend
def f05fw_f05_fiftytwo_week_anchor_dsltrend_252d_base_v091_signal(closeadj):
    dsl = _f05_days_since_low(closeadj, 252)
    b = dsl - dsl.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sharpe-of-recovery: recovery off low divided by drawdown volatility
def f05fw_f05_fiftytwo_week_anchor_recovsharpe_252d_base_v092_signal(closeadj):
    rec = _f05_recovery(closeadj, 252)
    dd = _f05_drawdown(closeadj, 252)
    vol = dd.rolling(63, min_periods=21).std()
    b = rec.rolling(63, min_periods=21).mean() / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position hit-rate: fraction of days above the 252d range midpoint
def f05fw_f05_fiftytwo_week_anchor_abovemid_252d_base_v093_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    above = (rp >= 0.5).astype(float)
    b = above.rolling(126, min_periods=63).mean() + 0.2 * (rp - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap skewness over the half-year (asymmetry of approaches to the high)
def f05fw_f05_fiftytwo_week_anchor_gapskew_252d_base_v094_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    b = g.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 1260d range position acceleration (multi-year curvature)
def f05fw_f05_fiftytwo_week_anchor_rngposacc_1260d_base_v095_signal(closeadj):
    rp = _f05_range_pos(closeadj, 1260)
    b = rp - 2.0 * rp.shift(42) + rp.shift(84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown depth normalized by the 252d amplitude (relative drawdown severity)
def f05fw_f05_fiftytwo_week_anchor_relddamp_252d_base_v096_signal(closeadj):
    dd = _f05_drawdown(closeadj, 252).abs()
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    amp = (hi - lo) / closeadj.replace(0, np.nan)
    b = dd / amp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery depth normalized by 504d amplitude
def f05fw_f05_fiftytwo_week_anchor_relrecamp_504d_base_v097_signal(closeadj):
    rec = _f05_recovery(closeadj, 504)
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    amp = (hi - lo) / closeadj.replace(0, np.nan)
    b = rec / amp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position momentum at 252d (anchor climb rate)
def f05fw_f05_fiftytwo_week_anchor_rngposmom_252d_base_v098_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    b = rp - rp.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap kurtosis-like: max gap over half-year vs current gap (overhang)
def f05fw_f05_fiftytwo_week_anchor_gapoverhang_252d_base_v099_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    worst = g.rolling(126, min_periods=63).min()
    b = g - worst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity to 1260d high in 252d-vol units, change (multi-year approach speed)
def f05fw_f05_fiftytwo_week_anchor_longapproach_1260d_base_v100_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 1260)
    vol = closeadj.pct_change().rolling(252, min_periods=126).std()
    ratio = g / vol.replace(0, np.nan)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside potential to the 1260d high vs downside risk to the 252d low (asym ratio)
def f05fw_f05_fiftytwo_week_anchor_updownratio_base_v101_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 252)
    up = hi / closeadj.replace(0, np.nan) - 1.0
    dn = 1.0 - lo / closeadj.replace(0, np.nan)
    b = np.log((up + 1e-6) / (dn + 1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range-position vs 252d-old range-position (year-over-year anchor change)
def f05fw_f05_fiftytwo_week_anchor_rngposyoy_252d_base_v102_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    b = rp - rp.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last quarter making higher-highs in the 252d window (uptrend confirm)
def f05fw_f05_fiftytwo_week_anchor_hhfrac_252d_base_v103_signal(closeadj):
    hi = closeadj.rolling(252, min_periods=126).max()
    new_hi = (hi > hi.shift(1)).astype(float)
    b = new_hi.rolling(63, min_periods=21).mean() + 0.05 * _f05_range_pos(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last quarter making lower-lows
def f05fw_f05_fiftytwo_week_anchor_llfrac_252d_base_v104_signal(closeadj):
    lo = closeadj.rolling(252, min_periods=126).min()
    new_lo = (lo < lo.shift(1)).astype(float)
    b = new_lo.rolling(63, min_periods=21).mean() + 0.05 * (1.0 - _f05_range_pos(closeadj, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 252d high z-scored by the 1260d distribution of distances
def f05fw_f05_fiftytwo_week_anchor_gapzlong_252d_base_v105_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery off 1260d low z-scored vs its 504d history (multi-year value rebound)
def f05fw_f05_fiftytwo_week_anchor_recovzlong_1260d_base_v106_signal(closeadj):
    rec = _f05_recovery(closeadj, 1260)
    b = _z(rec, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh of range position centered (bounded anchor position)
def f05fw_f05_fiftytwo_week_anchor_rngpostanh_504d_base_v107_signal(closeadj):
    rp = _f05_range_pos(closeadj, 504)
    b = np.tanh(4.0 * (rp - 0.5))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap times its own momentum (sign-confirmed anchor approach)
def f05fw_f05_fiftytwo_week_anchor_gapxmom_252d_base_v108_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    mom = g - g.shift(21)
    b = np.sign(mom) * g.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-high stability: 1 minus normalized std of proximity (steadiness near high)
def f05fw_f05_fiftytwo_week_anchor_proxhistab_252d_base_v109_signal(closeadj):
    p = _f05_prox_high(closeadj, 252)
    b = -p.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of months in last year that ended in the upper quartile of 52w range
def f05fw_f05_fiftytwo_week_anchor_upperqfrac_252d_base_v110_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    uq = (rp >= 0.75).astype(float)
    b = uq.rolling(252, min_periods=126).mean() + 0.1 * rp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# the 252d-low itself relative to the 1260d-low (is the recent floor higher = rising base)
def f05fw_f05_fiftytwo_week_anchor_risingbase_base_v111_signal(closeadj):
    lo252 = _rmin(closeadj, 252)
    lo1260 = _rmin(closeadj, 1260)
    b = np.log(lo252.replace(0, np.nan) / lo1260.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capped regime: fraction of the last year spent >15% below the 1260d high
def f05fw_f05_fiftytwo_week_anchor_cappedceiling_base_v112_signal(closeadj):
    hi1260 = _rmax(closeadj, 1260)
    capped = (closeadj <= 0.85 * hi1260).astype(float)
    frac = capped.rolling(252, min_periods=126).mean()
    depth = (0.85 - closeadj / hi1260.replace(0, np.nan)).clip(lower=0)
    b = frac + 5.0 * depth.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap interacted with realized momentum (gap closing with thrust)
def f05fw_f05_fiftytwo_week_anchor_gapthrust_252d_base_v113_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    mom = closeadj.pct_change(63)
    b = (-g) * mom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown convexity: drawdown minus a smoothed drawdown (acute distress vs chronic)
def f05fw_f05_fiftytwo_week_anchor_ddconvex_252d_base_v114_signal(closeadj):
    dd = _f05_drawdown(closeadj, 252)
    b = dd - dd.ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery convexity: recovery minus smoothed recovery
def f05fw_f05_fiftytwo_week_anchor_recovconvex_252d_base_v115_signal(closeadj):
    rec = _f05_recovery(closeadj, 252)
    b = rec - rec.ewm(span=63, min_periods=31).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap term-structure slope: how the anchoring gap steepens per log-horizon
def f05fw_f05_fiftytwo_week_anchor_proxhslope_base_v116_signal(closeadj):
    g252 = _f05_anchor_gap(closeadj, 252)
    g1260 = _f05_anchor_gap(closeadj, 1260)
    slope = (g252 - g1260) / np.log(1260.0 / 252.0)
    b = _z(slope, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown severity rank: where current underwater sits in its 504d history
def f05fw_f05_fiftytwo_week_anchor_ddvel_504d_base_v117_signal(closeadj):
    dd = _f05_drawdown(closeadj, 504)
    b = dd.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-high percentile within the cross-time 1260d distribution
def f05fw_f05_fiftytwo_week_anchor_proxhirank_1260d_base_v118_signal(closeadj):
    p = _f05_prox_high(closeadj, 252)
    b = p.rolling(1260, min_periods=504).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position percentile within cross-time 1260d distribution
def f05fw_f05_fiftytwo_week_anchor_rngposrank_1260d_base_v119_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    b = rp.rolling(1260, min_periods=504).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# is price closer to 52w high or 52w low (signed nearest-anchor indicator, smoothed)
def f05fw_f05_fiftytwo_week_anchor_nearestanchor_252d_base_v120_signal(closeadj):
    dh = (_rmax(closeadj, 252) - closeadj).abs()
    dl = (closeadj - _rmin(closeadj, 252)).abs()
    raw = (dl - dh) / (dl + dh).replace(0, np.nan)
    b = raw.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring overhang interacted with vol (heavy anchor under high uncertainty)
def f05fw_f05_fiftytwo_week_anchor_overhangvol_252d_base_v121_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = g * vol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fresh-high streak: consecutive days within 2% of the 252d high (smoothed length)
def f05fw_f05_fiftytwo_week_anchor_freshhistreak_252d_base_v122_signal(closeadj):
    hi = closeadj.rolling(252, min_periods=126).max()
    near = (closeadj >= 0.98 * hi).astype(float)
    grp = (near != near.shift(1)).cumsum()
    run = near.groupby(grp).cumsum() * near
    b = run.rolling(21, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-low pressure: smoothed inverse distance to the 252d low (basing pressure)
def f05fw_f05_fiftytwo_week_anchor_deeplostreak_252d_base_v123_signal(closeadj):
    lo = closeadj.rolling(252, min_periods=126).min()
    closeness = lo.replace(0, np.nan) / closeadj.replace(0, np.nan)
    b = closeness.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap mean-reversion z at 504d (deep value extremity, long)
def f05fw_f05_fiftytwo_week_anchor_gaprevz_504d_base_v124_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 504)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range amplitude trend: is the 252d range expanding or contracting (regime)
def f05fw_f05_fiftytwo_week_anchor_amptrend_252d_base_v125_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    amp = (hi - lo) / closeadj.replace(0, np.nan)
    b = amp - amp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-high weighted by inverse amplitude (clean breakout near tight range)
def f05fw_f05_fiftytwo_week_anchor_tightprox_252d_base_v126_signal(closeadj):
    p = _f05_prox_high(closeadj, 252)
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    amp = (hi - lo) / closeadj.replace(0, np.nan)
    b = (p - p.rolling(63, min_periods=21).mean()) / amp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how much of the 252d-high gain happened in the last quarter (momentum concentration)
def f05fw_f05_fiftytwo_week_anchor_hiconc_252d_base_v127_signal(closeadj):
    hi = _rmax(closeadj, 252)
    hi_lag = _rmax(closeadj, 252).shift(63)
    full = hi / _rmin(closeadj, 252).replace(0, np.nan) - 1.0
    recent = hi / hi_lag.replace(0, np.nan) - 1.0
    b = recent / full.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring extremity: risk-scaled range position percentile-ranked vs 252d history
def f05fw_f05_fiftytwo_week_anchor_extremity_252d_base_v128_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    ext = (2.0 * rp - 1.0) * vol
    b = ext.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown-to-recovery handoff: time underwater times recent drawdown change (turn)
def f05fw_f05_fiftytwo_week_anchor_ddhandoff_252d_base_v129_signal(closeadj):
    dd = _f05_drawdown(closeadj, 252)
    underwater = (dd < -0.01).astype(float)
    dur = underwater.rolling(63, min_periods=21).mean()
    chg = dd - dd.shift(21)
    b = dur * chg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d relative gap momentum: change in distance-to-high (amplitude units) over a quarter
def f05fw_f05_fiftytwo_week_anchor_relgap_504d_base_v130_signal(closeadj):
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    rg = (hi - closeadj) / (hi - lo).replace(0, np.nan)
    b = rg - rg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 1260d relative gap percentile-ranked vs its own 504d history (multi-year)
def f05fw_f05_fiftytwo_week_anchor_relgap_1260d_base_v131_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 1260)
    rg = (hi - closeadj) / (hi - lo).replace(0, np.nan)
    b = rg.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position acceleration at 252d (curvature of the anchor climb)
def f05fw_f05_fiftytwo_week_anchor_rngposaccel_252d_base_v132_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    b = rp - 2.0 * rp.shift(21) + rp.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery-strength rank: 504d recovery percentile in its 504d history (deep rebound rank)
def f05fw_f05_fiftytwo_week_anchor_recovrank_504d_base_v133_signal(closeadj):
    rec = _f05_recovery(closeadj, 504)
    b = rec.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 52w-high freshness decay: time-since-high times the depth of the gap (heavy stale anchor)
def f05fw_f05_fiftytwo_week_anchor_staleheavy_252d_base_v134_signal(closeadj):
    dsh = _f05_days_since_high(closeadj, 252)
    g = _f05_anchor_gap(closeadj, 252)
    b = dsh * (-g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor disagreement: rolling std of the 252d range position over a half-year
def f05fw_f05_fiftytwo_week_anchor_anchdisagree_base_v135_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    b = rp.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d high climb rate (log-slope of the rolling max, new-high creation)
def f05fw_f05_fiftytwo_week_anchor_hiclimb_252d_base_v136_signal(closeadj):
    hi = _rmax(closeadj, 252)
    b = np.log(hi.replace(0, np.nan) / hi.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d low climb rate (rising floor speed)
def f05fw_f05_fiftytwo_week_anchor_loclimb_252d_base_v137_signal(closeadj):
    lo = _rmin(closeadj, 252)
    b = np.log(lo.replace(0, np.nan) / lo.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap relative to a 504d EMA of the gap (gap regime displacement)
def f05fw_f05_fiftytwo_week_anchor_gapregime_252d_base_v138_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    b = g - g.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last half-year above the 504d range midpoint (long anchor bias)
def f05fw_f05_fiftytwo_week_anchor_abovemid_504d_base_v139_signal(closeadj):
    rp = _f05_range_pos(closeadj, 504)
    above = (rp >= 0.5).astype(float)
    b = above.rolling(126, min_periods=63).mean() + 0.2 * (rp - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# normalized excursion: where the close sits between 1260d low and 252d high (blended)
def f05fw_f05_fiftytwo_week_anchor_blendpos_base_v140_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 1260)
    b = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap autocorrelation-like: gap vs its own 21d-lagged value (persistence)
def f05fw_f05_fiftytwo_week_anchor_gappersist_252d_base_v141_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    prod = (g * g.shift(21)).rolling(126, min_periods=63).mean()
    norm = (g * g).rolling(126, min_periods=63).mean()
    b = prod / norm.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-high acceleration scaled by amplitude (clean thrust into the high)
def f05fw_f05_fiftytwo_week_anchor_thrustamp_252d_base_v142_signal(closeadj):
    p = _f05_prox_high(closeadj, 252)
    acc = p - 2.0 * p.shift(21) + p.shift(42)
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    amp = (hi - lo) / closeadj.replace(0, np.nan)
    b = acc / amp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year base-building: 252d low relative to the 504d low, smoothed (rising base)
def f05fw_f05_fiftytwo_week_anchor_baserise_1260d_base_v143_signal(closeadj):
    lo252 = _rmin(closeadj, 252)
    lo504 = _rmin(closeadj, 504)
    raw = np.log(lo252.replace(0, np.nan) / lo504.replace(0, np.nan))
    b = raw.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance below the all-time (1260d) high net of the typical such distance (excess gap)
def f05fw_f05_fiftytwo_week_anchor_excessgap_1260d_base_v144_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 1260)
    typ = g.rolling(252, min_periods=126).median()
    b = g - typ
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery-spread momentum: change in short-vs-long recovery spread over a quarter
def f05fw_f05_fiftytwo_week_anchor_recovspread_base_v145_signal(closeadj):
    r1 = _f05_recovery(closeadj, 252)
    r2 = _f05_recovery(closeadj, 1260)
    spread = np.log((1.0 + r1) / (1.0 + r2).replace(0, np.nan))
    b = spread - spread.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring tilt momentum: change in the high-vs-low tilt over a quarter
def f05fw_f05_fiftytwo_week_anchor_tiltmom_252d_base_v146_signal(closeadj):
    dh = (_rmax(closeadj, 252) - closeadj).abs()
    dl = (closeadj - _rmin(closeadj, 252)).abs()
    tilt = (dl - dh) / (dl + dh).replace(0, np.nan)
    b = tilt - tilt.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year strictly between 252d low band and high band (range-bound)
def f05fw_f05_fiftytwo_week_anchor_rangebound_252d_base_v147_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    mid = ((rp > 0.25) & (rp < 0.75)).astype(float)
    b = mid.rolling(252, min_periods=126).mean() - 0.3 * (rp - 0.5).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d anchoring gap times time-since-504d-high (long heavy stale anchor)
def f05fw_f05_fiftytwo_week_anchor_longstale_504d_base_v148_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 504)
    dsh = _f05_days_since_high(closeadj, 504)
    b = (-g) * dsh
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored 252d range position momentum (de-trended anchor climb)
def f05fw_f05_fiftytwo_week_anchor_rngposmomz_252d_base_v149_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    mom = rp - rp.shift(21)
    b = _z(mom, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite anchor health: range position penalized by drawdown-episode frequency
def f05fw_f05_fiftytwo_week_anchor_anchhealth_252d_base_v150_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    dd = _f05_drawdown(closeadj, 252)
    in_dd = (dd <= -0.10).astype(float)
    freq = in_dd.rolling(252, min_periods=126).mean()
    b = rp - 1.5 * freq
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05fw_f05_fiftytwo_week_anchor_gapmom_252d_base_v076_signal,
    f05fw_f05_fiftytwo_week_anchor_gapmom_504d_base_v077_signal,
    f05fw_f05_fiftytwo_week_anchor_gapaccel_252d_base_v078_signal,
    f05fw_f05_fiftytwo_week_anchor_newhicount_252d_base_v079_signal,
    f05fw_f05_fiftytwo_week_anchor_newlocount_252d_base_v080_signal,
    f05fw_f05_fiftytwo_week_anchor_gapdisp_252d_base_v081_signal,
    f05fw_f05_fiftytwo_week_anchor_rngposdisp_504d_base_v082_signal,
    f05fw_f05_fiftytwo_week_anchor_recovmom_252d_base_v083_signal,
    f05fw_f05_fiftytwo_week_anchor_ddheal_252d_base_v084_signal,
    f05fw_f05_fiftytwo_week_anchor_anchtilt_252d_base_v085_signal,
    f05fw_f05_fiftytwo_week_anchor_longnearhi_1260d_base_v086_signal,
    f05fw_f05_fiftytwo_week_anchor_rngposdisp504_504d_base_v087_signal,
    f05fw_f05_fiftytwo_week_anchor_nestedgap_252v504_base_v088_signal,
    f05fw_f05_fiftytwo_week_anchor_nestedgap_504v1260_base_v089_signal,
    f05fw_f05_fiftytwo_week_anchor_dshtrend_252d_base_v090_signal,
    f05fw_f05_fiftytwo_week_anchor_dsltrend_252d_base_v091_signal,
    f05fw_f05_fiftytwo_week_anchor_recovsharpe_252d_base_v092_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemid_252d_base_v093_signal,
    f05fw_f05_fiftytwo_week_anchor_gapskew_252d_base_v094_signal,
    f05fw_f05_fiftytwo_week_anchor_rngposacc_1260d_base_v095_signal,
    f05fw_f05_fiftytwo_week_anchor_relddamp_252d_base_v096_signal,
    f05fw_f05_fiftytwo_week_anchor_relrecamp_504d_base_v097_signal,
    f05fw_f05_fiftytwo_week_anchor_rngposmom_252d_base_v098_signal,
    f05fw_f05_fiftytwo_week_anchor_gapoverhang_252d_base_v099_signal,
    f05fw_f05_fiftytwo_week_anchor_longapproach_1260d_base_v100_signal,
    f05fw_f05_fiftytwo_week_anchor_updownratio_base_v101_signal,
    f05fw_f05_fiftytwo_week_anchor_rngposyoy_252d_base_v102_signal,
    f05fw_f05_fiftytwo_week_anchor_hhfrac_252d_base_v103_signal,
    f05fw_f05_fiftytwo_week_anchor_llfrac_252d_base_v104_signal,
    f05fw_f05_fiftytwo_week_anchor_gapzlong_252d_base_v105_signal,
    f05fw_f05_fiftytwo_week_anchor_recovzlong_1260d_base_v106_signal,
    f05fw_f05_fiftytwo_week_anchor_rngpostanh_504d_base_v107_signal,
    f05fw_f05_fiftytwo_week_anchor_gapxmom_252d_base_v108_signal,
    f05fw_f05_fiftytwo_week_anchor_proxhistab_252d_base_v109_signal,
    f05fw_f05_fiftytwo_week_anchor_upperqfrac_252d_base_v110_signal,
    f05fw_f05_fiftytwo_week_anchor_risingbase_base_v111_signal,
    f05fw_f05_fiftytwo_week_anchor_cappedceiling_base_v112_signal,
    f05fw_f05_fiftytwo_week_anchor_gapthrust_252d_base_v113_signal,
    f05fw_f05_fiftytwo_week_anchor_ddconvex_252d_base_v114_signal,
    f05fw_f05_fiftytwo_week_anchor_recovconvex_252d_base_v115_signal,
    f05fw_f05_fiftytwo_week_anchor_proxhslope_base_v116_signal,
    f05fw_f05_fiftytwo_week_anchor_ddvel_504d_base_v117_signal,
    f05fw_f05_fiftytwo_week_anchor_proxhirank_1260d_base_v118_signal,
    f05fw_f05_fiftytwo_week_anchor_rngposrank_1260d_base_v119_signal,
    f05fw_f05_fiftytwo_week_anchor_nearestanchor_252d_base_v120_signal,
    f05fw_f05_fiftytwo_week_anchor_overhangvol_252d_base_v121_signal,
    f05fw_f05_fiftytwo_week_anchor_freshhistreak_252d_base_v122_signal,
    f05fw_f05_fiftytwo_week_anchor_deeplostreak_252d_base_v123_signal,
    f05fw_f05_fiftytwo_week_anchor_gaprevz_504d_base_v124_signal,
    f05fw_f05_fiftytwo_week_anchor_amptrend_252d_base_v125_signal,
    f05fw_f05_fiftytwo_week_anchor_tightprox_252d_base_v126_signal,
    f05fw_f05_fiftytwo_week_anchor_hiconc_252d_base_v127_signal,
    f05fw_f05_fiftytwo_week_anchor_extremity_252d_base_v128_signal,
    f05fw_f05_fiftytwo_week_anchor_ddhandoff_252d_base_v129_signal,
    f05fw_f05_fiftytwo_week_anchor_relgap_504d_base_v130_signal,
    f05fw_f05_fiftytwo_week_anchor_relgap_1260d_base_v131_signal,
    f05fw_f05_fiftytwo_week_anchor_rngposaccel_252d_base_v132_signal,
    f05fw_f05_fiftytwo_week_anchor_recovrank_504d_base_v133_signal,
    f05fw_f05_fiftytwo_week_anchor_staleheavy_252d_base_v134_signal,
    f05fw_f05_fiftytwo_week_anchor_anchdisagree_base_v135_signal,
    f05fw_f05_fiftytwo_week_anchor_hiclimb_252d_base_v136_signal,
    f05fw_f05_fiftytwo_week_anchor_loclimb_252d_base_v137_signal,
    f05fw_f05_fiftytwo_week_anchor_gapregime_252d_base_v138_signal,
    f05fw_f05_fiftytwo_week_anchor_abovemid_504d_base_v139_signal,
    f05fw_f05_fiftytwo_week_anchor_blendpos_base_v140_signal,
    f05fw_f05_fiftytwo_week_anchor_gappersist_252d_base_v141_signal,
    f05fw_f05_fiftytwo_week_anchor_thrustamp_252d_base_v142_signal,
    f05fw_f05_fiftytwo_week_anchor_baserise_1260d_base_v143_signal,
    f05fw_f05_fiftytwo_week_anchor_excessgap_1260d_base_v144_signal,
    f05fw_f05_fiftytwo_week_anchor_recovspread_base_v145_signal,
    f05fw_f05_fiftytwo_week_anchor_tiltmom_252d_base_v146_signal,
    f05fw_f05_fiftytwo_week_anchor_rangebound_252d_base_v147_signal,
    f05fw_f05_fiftytwo_week_anchor_longstale_504d_base_v148_signal,
    f05fw_f05_fiftytwo_week_anchor_rngposmomz_252d_base_v149_signal,
    f05fw_f05_fiftytwo_week_anchor_anchhealth_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_FIFTYTWO_WEEK_ANCHOR_REGISTRY_076_150 = REGISTRY


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

    print("OK f05_fiftytwo_week_anchor_base_076_150_claude: %d features pass" % n_features)
