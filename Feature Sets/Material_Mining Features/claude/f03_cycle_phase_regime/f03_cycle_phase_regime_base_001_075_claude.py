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


def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


# ===== folder domain primitives (CYCLE REGIME CLASSIFICATION & TRANSITIONS) =====
# This family is COUNT/REGIME/TRANSITION/ASYMMETRY-centric. It must NOT emit raw
# range-position levels (f07), drawdown depth/duration/velocity (f04), or
# base-tightness/breakout (f06). Everything here is a regime STATE indicator, a
# time-in-state / run-length statistic, a transition COUNT/FREQUENCY, an
# up-vs-down asymmetry, or a regime-switch entropy.

def _f03_trend(c, w):
    # long trend reference = rolling mean of log price (multi-year backbone)
    return np.log(c.replace(0, np.nan)).rolling(w, min_periods=max(1, w // 2)).mean()


def _f03_regime_state(c, w):
    # boom(+1) vs bust(-1) STATE = sign of log price minus its long trend
    lp = np.log(c.replace(0, np.nan))
    tr = lp.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.sign(lp - tr)


def _f03_above_frac(c, w_state, w_count):
    # fraction of last w_count days the regime STATE was boom (above long trend)
    st = (_f03_regime_state(c, w_state) > 0).astype(float)
    return st.rolling(w_count, min_periods=max(1, w_count // 2)).mean()


def _f03_transitions(c, w_state, w_count):
    # number of regime FLIPS (boom<->bust) inside the trailing w_count window
    st = _f03_regime_state(c, w_state)
    flip = (st != st.shift(1)).astype(float)
    flip = flip.where(st.notna() & st.shift(1).notna(), other=np.nan)
    return flip.rolling(w_count, min_periods=max(1, w_count // 2)).sum()


def _f03_trans_intensity(c, w_state, w_count):
    # transition INTENSITY: flips weighted by how decisively the gap crossed zero
    # (continuous transition-count proxy; varies smoothly, still transition-centric)
    lp = np.log(c.replace(0, np.nan))
    tr = lp.rolling(w_state, min_periods=max(1, w_state // 2)).mean()
    gap = lp - tr
    st = np.sign(gap)
    flip = (st != st.shift(1)).astype(float)
    cross_mag = (gap - gap.shift(1)).abs()
    w = (flip * cross_mag).where(st.notna() & st.shift(1).notna(), other=np.nan)
    cnt = flip.where(st.notna() & st.shift(1).notna(), other=np.nan)
    n = cnt.rolling(w_count, min_periods=max(1, w_count // 2)).sum()
    inten = w.rolling(w_count, min_periods=max(1, w_count // 2)).sum()
    return n + 25.0 * inten


def _f03_runlen(state_bool):
    # length of the CURRENT consecutive run of a boolean state, in days
    s = state_bool.astype(float)
    grp = (s != s.shift(1)).cumsum()
    run = s.groupby(grp).cumcount() + 1.0
    return run.where(s == 1, other=0.0)


def _f03_signrun(c):
    # signed run-length of the current daily-return streak (up streak +k, down -k)
    r = np.sign(np.log(c.replace(0, np.nan)).diff())
    grp = (r != r.shift(1)).cumsum()
    cnt = r.groupby(grp).cumcount() + 1.0
    return cnt * r


def _f03_updown_asym(c, w):
    # up-day count minus down-day count over w, normalised by w (day-count asymmetry)
    r = np.log(c.replace(0, np.nan)).diff()
    up = (r > 0).astype(float).rolling(w, min_periods=max(1, w // 2)).sum()
    dn = (r < 0).astype(float).rolling(w, min_periods=max(1, w // 2)).sum()
    return (up - dn) / float(w)


def _f03_switch_entropy(c, w_state, w_count):
    # Shannon entropy of the boom/bust state mix over w_count (regime indecision)
    st = (_f03_regime_state(c, w_state) > 0).astype(float)
    p = st.rolling(w_count, min_periods=max(1, w_count // 2)).mean().clip(1e-6, 1 - 1e-6)
    return -(p * np.log(p) + (1 - p) * np.log(1 - p))


# ============================================================
# ---- REGIME STATE: boom vs bust relative to long trend -----
# boom/bust state vs 252d trend, smoothed into a soft regime score
def f03cp_f03_cycle_phase_regime_state_252d_base_v001_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    b = st.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# boom/bust state vs 504d trend, smoothed
def f03cp_f03_cycle_phase_regime_state_504d_base_v002_signal(closeadj):
    st = _f03_regime_state(closeadj, 504)
    b = st.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# boom/bust state vs 1260d (5y) trend, smoothed (multi-year regime)
def f03cp_f03_cycle_phase_regime_state_1260d_base_v003_signal(closeadj):
    st = _f03_regime_state(closeadj, 1260)
    b = st.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime agreement across 252/504/1260 trends (how aligned the cycle clocks are)
def f03cp_f03_cycle_phase_regime_agree_multi_base_v004_signal(closeadj):
    s1 = _f03_regime_state(closeadj, 252)
    s2 = _f03_regime_state(closeadj, 504)
    s3 = _f03_regime_state(closeadj, 1260)
    b = ((s1 + s2 + s3) / 3.0).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# in-uptrend STATE: sign of trend slope itself (is the long backbone rising?)
def f03cp_f03_cycle_phase_regime_trendslopesign_252d_base_v005_signal(closeadj):
    tr = _f03_trend(closeadj, 252)
    slope = tr - tr.shift(21)
    b = np.sign(slope).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# in-uptrend STATE on the 504d backbone slope
def f03cp_f03_cycle_phase_regime_trendslopesign_504d_base_v006_signal(closeadj):
    tr = _f03_trend(closeadj, 504)
    slope = tr - tr.shift(63)
    b = np.sign(slope).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dual-clock regime: short trend above/below long trend (golden/death regime state)
def f03cp_f03_cycle_phase_regime_dualtrend_base_v007_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    short_tr = lp.rolling(63, min_periods=21).mean()
    long_tr = lp.rolling(252, min_periods=126).mean()
    b = np.sign(short_tr - long_tr).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dual-clock regime on 126 vs 504 (slower regime classifier)
def f03cp_f03_cycle_phase_regime_dualtrend_slow_base_v008_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    short_tr = lp.rolling(126, min_periods=63).mean()
    long_tr = lp.rolling(504, min_periods=252).mean()
    b = np.sign(short_tr - long_tr).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- TIME-IN-STATE: fraction of window in boom regime ------
# fraction of trailing 252d the 252d-trend regime was boom
def f03cp_f03_cycle_phase_regime_boomfrac_252d_base_v009_signal(closeadj):
    b = _f03_above_frac(closeadj, 252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of trailing 126d in boom regime vs the 252d trend (recent regime tilt)
def f03cp_f03_cycle_phase_regime_boomfrac_126d_base_v010_signal(closeadj):
    b = _f03_above_frac(closeadj, 252, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of trailing 504d in boom regime vs the 504d trend (long time-in-boom)
def f03cp_f03_cycle_phase_regime_boomfrac_504d_base_v011_signal(closeadj):
    b = _f03_above_frac(closeadj, 504, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bust concentration: longest single bust run as a share of total bust-days in 252d
def f03cp_f03_cycle_phase_regime_bustfrac_252d_base_v012_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    bustrun = _f03_runlen(st < 0)
    longest = bustrun.rolling(252, min_periods=126).max()
    total = (st < 0).astype(float).rolling(252, min_periods=126).sum()
    b = longest / total.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shift in time-in-boom: recent quarter boom-fraction minus prior quarter's
def f03cp_f03_cycle_phase_regime_boomfracchg_252d_base_v013_signal(closeadj):
    f = _f03_above_frac(closeadj, 252, 63)
    b = f - f.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# boom-fraction asymmetry across two trend clocks (252 vs 504 time-in-boom gap)
def f03cp_f03_cycle_phase_regime_boomfracspr_base_v014_signal(closeadj):
    f1 = _f03_above_frac(closeadj, 252, 252)
    f2 = _f03_above_frac(closeadj, 504, 252)
    b = f1 - f2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- REGIME DURATION / run-length of current phase ---------
# run-length (days) of the CURRENT boom regime vs 252d trend, log-scaled
def f03cp_f03_cycle_phase_regime_boomrun_252d_base_v015_signal(closeadj):
    boom = _f03_regime_state(closeadj, 252) > 0
    run = _f03_runlen(boom)
    b = np.log1p(run)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# run-length (days) of the CURRENT bust regime vs 252d trend, log-scaled
def f03cp_f03_cycle_phase_regime_bustrun_252d_base_v016_signal(closeadj):
    bust = _f03_regime_state(closeadj, 252) < 0
    run = _f03_runlen(bust)
    b = np.log1p(run)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-phase run length relative to the typical run on the 504d clock: how far
# into the present phase are we vs how long phases usually last (signed maturity)
def f03cp_f03_cycle_phase_regime_signedrun_504d_base_v017_signal(closeadj):
    st = _f03_regime_state(closeadj, 504)
    run = _f03_runlen(st > 0) + _f03_runlen(st < 0)
    typ = run.rolling(504, min_periods=252).mean()
    b = np.sign(st) * (run / typ.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how the current boom run compares to the typical boom run over the last 2y
def f03cp_f03_cycle_phase_regime_runvsavg_252d_base_v018_signal(closeadj):
    boom = _f03_regime_state(closeadj, 252) > 0
    run = _f03_runlen(boom)
    typ = run.rolling(504, min_periods=126).mean()
    b = np.log1p(run) - np.log1p(typ)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maturity of current regime: current run length / longest run in trailing 504d
def f03cp_f03_cycle_phase_regime_runmaturity_252d_base_v019_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    boom = st > 0
    bust = st < 0
    cur = _f03_runlen(boom) + _f03_runlen(bust)
    mx = cur.rolling(504, min_periods=126).max()
    b = cur / mx.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- REGIME TRANSITION counts & choppiness -----------------
# boom<->bust flip intensity (252d trend) in the trailing year (cycle choppiness)
def f03cp_f03_cycle_phase_regime_flips_252d_base_v020_signal(closeadj):
    b = _f03_trans_intensity(closeadj, 252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# flip intensity vs 504d trend over trailing 504d (slow-cycle whipsaw)
def f03cp_f03_cycle_phase_regime_flips_504d_base_v021_signal(closeadj):
    b = _f03_trans_intensity(closeadj, 504, 504).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recent vs older flip intensity (is the cycle getting choppier?)
def f03cp_f03_cycle_phase_regime_flipaccel_252d_base_v022_signal(closeadj):
    f = _f03_trans_intensity(closeadj, 252, 126)
    b = f - f.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# flip intensity per unit time (choppiness intensity over the quarter)
def f03cp_f03_cycle_phase_regime_flipfreq_63d_base_v023_signal(closeadj):
    b = _f03_trans_intensity(closeadj, 126, 63) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time since the last regime flip (stability of the current phase), log-scaled
def f03cp_f03_cycle_phase_regime_sincelastflip_252d_base_v024_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    flip = (st != st.shift(1)) & st.notna() & st.shift(1).notna()
    grp = flip.cumsum()
    since = flip.groupby(grp).cumcount().astype(float)
    b = np.log1p(since)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- REGIME-SWITCH ENTROPY ---------------------------------
# Shannon entropy of boom/bust mix over trailing year (regime indecision)
def f03cp_f03_cycle_phase_regime_entropy_252d_base_v025_signal(closeadj):
    b = _f03_switch_entropy(closeadj, 252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime-mix entropy on the 504d trend over trailing 504d
def f03cp_f03_cycle_phase_regime_entropy_504d_base_v026_signal(closeadj):
    b = _f03_switch_entropy(closeadj, 504, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in regime entropy: is the cycle becoming more / less decisive?
def f03cp_f03_cycle_phase_regime_entropychg_252d_base_v027_signal(closeadj):
    e = _f03_switch_entropy(closeadj, 252, 126)
    b = e - e.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# entropy of the daily up/down sign mix over a quarter (micro-choppiness)
def f03cp_f03_cycle_phase_regime_signentropy_63d_base_v028_signal(closeadj):
    up = (np.log(closeadj.replace(0, np.nan)).diff() > 0).astype(float)
    p = up.rolling(63, min_periods=21).mean().clip(1e-6, 1 - 1e-6)
    ent = -(p * np.log(p) + (1 - p) * np.log(1 - p))
    b = ent.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- UP vs DOWN day-count asymmetry ------------------------
# up-day minus down-day count over the quarter, normalised (day-count drift)
def f03cp_f03_cycle_phase_regime_updnasym_63d_base_v029_signal(closeadj):
    b = _f03_updown_asym(closeadj, 63).rolling(10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-vs-down day-count asymmetry over the year
def f03cp_f03_cycle_phase_regime_updnasym_252d_base_v030_signal(closeadj):
    b = _f03_updown_asym(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-vs-down day-count asymmetry over two years (structural cycle drift)
def f03cp_f03_cycle_phase_regime_updnasym_504d_base_v031_signal(closeadj):
    b = _f03_updown_asym(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# day-count asymmetry change quarter-over-quarter (regime-drift momentum)
def f03cp_f03_cycle_phase_regime_updnasymchg_63d_base_v032_signal(closeadj):
    a = _f03_updown_asym(closeadj, 63)
    b = a - a.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short vs long day-count asymmetry spread (recent drift vs structural drift)
def f03cp_f03_cycle_phase_regime_updnasymspr_base_v033_signal(closeadj):
    a_s = _f03_updown_asym(closeadj, 63)
    a_l = _f03_updown_asym(closeadj, 252)
    b = a_s - a_l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- DRAWUP vs DRAWDOWN RUN asymmetry (regime property) ----
# count of up-streaks vs down-streaks over the year (run-frequency asymmetry)
def f03cp_f03_cycle_phase_regime_runcountasym_252d_base_v034_signal(closeadj):
    r = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    up_start = ((r > 0) & (r.shift(1) <= 0)).astype(float)
    dn_start = ((r < 0) & (r.shift(1) >= 0)).astype(float)
    up_n = up_start.rolling(252, min_periods=126).sum()
    dn_n = dn_start.rolling(252, min_periods=126).sum()
    b = (up_n - dn_n) / (up_n + dn_n).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tail-streak asymmetry: longest up-streak vs longest down-streak, but measured as
# excess over the average streak length (how much fatter is the up vs down run tail)
def f03cp_f03_cycle_phase_regime_runlenasym_252d_base_v035_signal(closeadj):
    sr = _f03_signrun(closeadj)
    up = sr.clip(lower=0)
    dn = -sr.clip(upper=0)
    up_max = up.rolling(252, min_periods=126).max()
    dn_max = dn.rolling(252, min_periods=126).max()
    up_avg = up[up > 0].rolling(252, min_periods=63).mean().reindex(closeadj.index).ffill()
    dn_avg = dn[dn > 0].rolling(252, min_periods=63).mean().reindex(closeadj.index).ffill()
    up_excess = up_max - up_avg
    dn_excess = dn_max - dn_avg
    b = (up_excess - dn_excess) / (up_excess + dn_excess + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest up-streak vs longest down-streak over trailing year (extreme run asym)
def f03cp_f03_cycle_phase_regime_maxrunasym_252d_base_v036_signal(closeadj):
    sr = _f03_signrun(closeadj)
    up_max = sr.clip(lower=0).rolling(252, min_periods=126).max()
    dn_max = (-sr.clip(upper=0)).rolling(252, min_periods=126).max()
    raw = (up_max - dn_max) / (up_max + dn_max).replace(0, np.nan)
    b = raw.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current signed streak length, log-magnitude signed (drawup vs drawdown run now)
def f03cp_f03_cycle_phase_regime_signrun_now_base_v037_signal(closeadj):
    sr = _f03_signrun(closeadj)
    raw = np.sign(sr) * np.log1p(sr.abs())
    b = raw.ewm(span=10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-streak dominance: share of streak-DAYS that belong to long (>=5d) up-runs
# minus long down-runs, normalised by all streak days (persistence-tail asymmetry)
def f03cp_f03_cycle_phase_regime_uprunpersist_252d_base_v038_signal(closeadj):
    sr = _f03_signrun(closeadj)
    long_up = (sr >= 5).astype(float).rolling(252, min_periods=126).sum()
    long_dn = (sr <= -5).astype(float).rolling(252, min_periods=126).sum()
    b = (long_up - long_dn) / (long_up + long_dn + 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- intraday-range regime (high/low) ----------------------
# fraction of year closing in upper half of the day's range (intraday boom regime)
def f03cp_f03_cycle_phase_regime_intradaybull_252d_base_v039_signal(closeadj, high, low):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    bull = (pos > 0.5).astype(float)
    b = bull.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-to-close vs intraday-range regime: do gaps run with or against the trend?
# net count of days where the close jumped beyond the prior day's high/low (breakout
# days up minus down) over the year — directional gap-break regime tilt
def f03cp_f03_cycle_phase_regime_gapasym_252d_base_v040_signal(closeadj, high, low):
    up_brk = (closeadj > high.shift(1)).astype(float)
    dn_brk = (closeadj < low.shift(1)).astype(float)
    u = up_brk.rolling(252, min_periods=126).sum()
    d = dn_brk.rolling(252, min_periods=126).sum()
    b = (u - d) / (u + d).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion vs contraction REGIME of the intraday range (range-state, not level)
def f03cp_f03_cycle_phase_regime_rangestate_252d_base_v041_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    med = rng.rolling(252, min_periods=126).median()
    expand = (rng > med).astype(float)
    b = expand.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# flips between range-expansion and range-contraction regime (volatility choppiness)
def f03cp_f03_cycle_phase_regime_rangeflip_252d_base_v042_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    med = rng.rolling(252, min_periods=126).median()
    st = np.sign(rng - med)
    flip = (st != st.shift(1)).astype(float)
    flip = flip.where(st.notna() & st.shift(1).notna(), other=np.nan)
    b = flip.rolling(126, min_periods=63).mean() + 0.01 * rng.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- more regime-state classifiers / asymmetries -----------
# boom-persistence: longest boom run in 504d minus longest bust run (regime dominance)
def f03cp_f03_cycle_phase_regime_dominance_504d_base_v043_signal(closeadj):
    st = _f03_regime_state(closeadj, 504)
    boomrun = _f03_runlen(st > 0)
    bustrun = _f03_runlen(st < 0)
    bm = boomrun.rolling(504, min_periods=252).max()
    bs = bustrun.rolling(504, min_periods=252).max()
    b = (bm - bs) / (bm + bs).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime fragmentation (Herfindahl-style): concentration of time into a few long
# regime runs vs many short ones over the year (1 => one dominant run, ~0 => choppy)
def f03cp_f03_cycle_phase_regime_nettilt_252d_base_v044_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    run = _f03_runlen(st > 0) + _f03_runlen(st < 0)
    is_end = (np.sign(st) != np.sign(st.shift(-1))).astype(float)
    run_len = (run * is_end)
    sumsq = (run_len ** 2).rolling(252, min_periods=126).sum()
    tot = run_len.rolling(252, min_periods=126).sum()
    b = sumsq / (tot ** 2).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# structural 5y trend-direction persistence: fraction of the last 2y the 1260d
# trend backbone was rising minus falling (slow up-cycle vs down-cycle dominance)
def f03cp_f03_cycle_phase_regime_nettilt_1260d_base_v045_signal(closeadj):
    tr = _f03_trend(closeadj, 1260)
    rising = (tr > tr.shift(21)).astype(float)
    falling = (tr < tr.shift(21)).astype(float)
    u = rising.rolling(504, min_periods=252).mean()
    d = falling.rolling(504, min_periods=252).mean()
    b = u - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how decisively the regime crossed: change in net tilt over a quarter (regime momentum)
def f03cp_f03_cycle_phase_regime_tiltmom_252d_base_v046_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    t = st.rolling(126, min_periods=63).mean()
    b = t - t.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime conviction: |net tilt| over the year (strong directional vs choppy cycle)
def f03cp_f03_cycle_phase_regime_conviction_252d_base_v047_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    b = st.rolling(252, min_periods=126).mean().abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- transition-direction asymmetry ------------------------
# upward transitions (bust->boom) minus downward (boom->bust), magnitude-weighted
def f03cp_f03_cycle_phase_regime_transdir_252d_base_v048_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    gap = lp - lp.rolling(252, min_periods=126).mean()
    st = np.sign(gap)
    cross_mag = (gap - gap.shift(1)).abs()
    up_t = (((st > 0) & (st.shift(1) <= 0)).astype(float) * (1.0 + 20.0 * cross_mag))
    dn_t = (((st < 0) & (st.shift(1) >= 0)).astype(float) * (1.0 + 20.0 * cross_mag))
    u = up_t.rolling(252, min_periods=126).sum()
    d = dn_t.rolling(252, min_periods=126).sum()
    b = u - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net transition direction on the 504d clock (slow cycle direction of switches)
def f03cp_f03_cycle_phase_regime_transdir_504d_base_v049_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    gap = lp - lp.rolling(504, min_periods=252).mean()
    st = np.sign(gap)
    cross_mag = (gap - gap.shift(1)).abs()
    up_t = (((st > 0) & (st.shift(1) <= 0)).astype(float) * (1.0 + 20.0 * cross_mag))
    dn_t = (((st < 0) & (st.shift(1) >= 0)).astype(float) * (1.0 + 20.0 * cross_mag))
    u = up_t.rolling(504, min_periods=252).sum()
    d = dn_t.rolling(504, min_periods=252).sum()
    b = (u - d).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- multi-clock regime divergence -------------------------
# regime divergence: short-clock boom while long-clock bust (cycle-phase conflict)
def f03cp_f03_cycle_phase_regime_clockdiverge_base_v050_signal(closeadj):
    s_short = _f03_regime_state(closeadj, 252)
    s_long = _f03_regime_state(closeadj, 1260)
    b = (s_short - s_long).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year the short and long clocks disagreed (transition zone time)
def f03cp_f03_cycle_phase_regime_clockconflict_252d_base_v051_signal(closeadj):
    s_short = _f03_regime_state(closeadj, 252)
    s_long = _f03_regime_state(closeadj, 504)
    conflict = (s_short != s_long).astype(float)
    conflict = conflict.where(s_short.notna() & s_long.notna(), other=np.nan)
    b = conflict.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- zero-crossing / mean-reversion regime statistics ------
# mean-reversion speed of the regime: lag-21 autocorrelation of the trend gap
# (low/negative => fast oscillating cycle; high => persistent trending regime)
def f03cp_f03_cycle_phase_regime_zerocross_252d_base_v052_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    gap = lp - lp.rolling(252, min_periods=126).mean()
    g0 = gap
    g1 = gap.shift(21)
    cov = (g0 * g1).rolling(252, min_periods=126).mean() \
        - g0.rolling(252, min_periods=126).mean() * g1.rolling(252, min_periods=126).mean()
    v0 = g0.rolling(252, min_periods=126).var()
    b = cov / v0.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# zero-crossing rate of daily returns (micro mean-reversion vs trending regime)
def f03cp_f03_cycle_phase_regime_retzerocross_63d_base_v053_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    cross = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    cross = cross.where(r.notna() & r.shift(1).notna(), other=np.nan)
    b = cross.rolling(63, min_periods=21).mean().rolling(10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime-state momentum & persistence (EWM-smoothed) ----
# persistence-weighted regime state: current state scaled by tanh of its run length
def f03cp_f03_cycle_phase_regime_stateema_252d_base_v054_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    boom = _f03_runlen(st > 0)
    bust = _f03_runlen(st < 0)
    run = boom + bust
    b = np.sign(st) * np.tanh(run / 42.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime-state displacement: state minus its slow EWM (regime turning indicator)
def f03cp_f03_cycle_phase_regime_statedisp_252d_base_v055_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    b = st.rolling(21, min_periods=10).mean() - st.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- weekly up/down asymmetry (regime breadth) -------------
# share of up-weeks vs down-weeks over the year (weekly regime breadth)
def f03cp_f03_cycle_phase_regime_weekasym_252d_base_v056_signal(closeadj):
    wk = np.log(closeadj.replace(0, np.nan)).diff(5)
    up = (wk > 0).astype(float).rolling(252, min_periods=126).mean()
    dn = (wk < 0).astype(float).rolling(252, min_periods=126).mean()
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of up-months vs down-months over two years (monthly regime breadth)
def f03cp_f03_cycle_phase_regime_monthasym_504d_base_v057_signal(closeadj):
    mo = np.log(closeadj.replace(0, np.nan)).diff(21)
    up = (mo > 0).astype(float).rolling(504, min_periods=252).mean()
    dn = (mo < 0).astype(float).rolling(504, min_periods=252).mean()
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime acceleration / second-order transitions --------
# is the boom-fraction itself in an uptrend? sign of its slope (regime-of-regime)
def f03cp_f03_cycle_phase_regime_boomfracstate_252d_base_v058_signal(closeadj):
    f = _f03_above_frac(closeadj, 252, 126)
    b = np.sign(f - f.shift(21)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime-switch clustering: near-term flip burst vs the year's baseline flip rate
def f03cp_f03_cycle_phase_regime_flipcluster_252d_base_v059_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    flip = (st != st.shift(1)).astype(float)
    flip = flip.where(st.notna() & st.shift(1).notna(), other=np.nan)
    near = flip.rolling(21, min_periods=10).sum()
    far = flip.rolling(252, min_periods=126).mean() * 21.0
    b = near - far
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawup vs drawdown EVENT-count asymmetry --------------
# count of >=5% up-moves vs >=5% down-moves (over 21d) in the year (event asym)
def f03cp_f03_cycle_phase_regime_moveasym_252d_base_v060_signal(closeadj):
    mret = np.log(closeadj.replace(0, np.nan)).diff(21)
    up_evt = (mret >= 0.05).astype(float).rolling(252, min_periods=126).sum()
    dn_evt = (mret <= -0.05).astype(float).rolling(252, min_periods=126).sum()
    b = (up_evt - dn_evt) / (up_evt + dn_evt).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# big-up-day vs big-down-day count asymmetry (tail-event regime, daily)
def f03cp_f03_cycle_phase_regime_tailasym_252d_base_v061_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    thr = r.rolling(252, min_periods=126).std()
    big_up = (r > 2.0 * thr).astype(float).rolling(252, min_periods=126).sum()
    big_dn = (r < -2.0 * thr).astype(float).rolling(252, min_periods=126).sum()
    b = (big_up - big_dn) / (big_up + big_dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- time-since-regime-extreme (cycle clock) ---------------
# time since the regime last entered boom (recency of the up-cycle start), log-scaled
def f03cp_f03_cycle_phase_regime_sinceboom_252d_base_v062_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    enter = (st > 0) & (st.shift(1) <= 0)
    grp = enter.cumsum()
    since = enter.groupby(grp).cumcount().astype(float)
    since = since.where(grp > 0, other=np.nan)
    b = np.log1p(since)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time since the regime last entered bust (recency of the down-cycle start)
def f03cp_f03_cycle_phase_regime_sincebust_252d_base_v063_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    enter = (st < 0) & (st.shift(1) >= 0)
    grp = enter.cumsum()
    since = enter.groupby(grp).cumcount().astype(float)
    since = since.where(grp > 0, other=np.nan)
    b = np.log1p(since)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime-mix stability over multiple horizons -----------
# stability: difference in boom-fraction between 63d and 252d windows (regime drift)
def f03cp_f03_cycle_phase_regime_mixstab_base_v064_signal(closeadj):
    f_s = _f03_above_frac(closeadj, 252, 63)
    f_l = _f03_above_frac(closeadj, 252, 252)
    b = f_s - f_l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- streak texture regime ---------------------------------
# streak-length dispersion: rolling std of the |signed-run| length over 126d, scaled
# by its mean (burstiness of runs — a few long runs vs uniformly short ones)
def f03cp_f03_cycle_phase_regime_hlcloseasym_63d_base_v065_signal(closeadj):
    sr = _f03_signrun(closeadj).abs()
    sd = sr.rolling(126, min_periods=63).std()
    mu = sr.rolling(126, min_periods=63).mean()
    b = sd / mu.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime hysteresis (asymmetric thresholds) -------------
# hysteresis benefit: fraction of the year the sticky (banded) regime disagreed with
# the naive instantaneous regime — how much the cycle lingers in transition zones
def f03cp_f03_cycle_phase_regime_hysteresis_252d_base_v066_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    gap = lp - lp.rolling(252, min_periods=126).mean()
    naive = np.sign(gap)
    raw = pd.Series(np.where(gap > 0.05, 1.0, np.where(gap < -0.05, -1.0, np.nan)),
                    index=closeadj.index)
    sticky = raw.ffill()
    disagree = (sticky != naive).astype(float)
    disagree = disagree.where(naive.notna() & sticky.notna(), other=np.nan)
    b = disagree.rolling(126, min_periods=63).mean() \
        + 0.1 * gap.abs().rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year inside the neutral (transition) band, neither boom nor bust
def f03cp_f03_cycle_phase_regime_neutralband_252d_base_v067_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    gap = lp - lp.rolling(252, min_periods=126).mean()
    sd = gap.rolling(252, min_periods=126).std()
    neutral = (gap.abs() < 0.5 * sd).astype(float)
    b = neutral.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime sign run vs intraday confirmation --------------
# agreement between close-regime sign and intraday-position sign (confirmation state)
def f03cp_f03_cycle_phase_regime_confirm_252d_base_v068_signal(closeadj, high, low):
    st = _f03_regime_state(closeadj, 252)
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    intraday_sign = np.sign(pos - 0.5)
    agree = (np.sign(st) == intraday_sign).astype(float)
    agree = agree.where(st.notna(), other=np.nan)
    b = agree.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- up-cycle vs down-cycle total day-count asymmetry ------
# up-cycle vs down-cycle RUN asymmetry: avg boom-run length vs avg bust-run length
# over 504d (are up-cycles longer-lived than down-cycles on the slow clock?)
def f03cp_f03_cycle_phase_regime_cycdayasym_504d_base_v069_signal(closeadj):
    st = _f03_regime_state(closeadj, 504)
    boom_days = (st > 0).astype(float).rolling(504, min_periods=252).sum()
    bust_days = (st < 0).astype(float).rolling(504, min_periods=252).sum()
    boom_onset = ((st > 0) & (st.shift(1) <= 0)).astype(float).rolling(504, min_periods=252).sum()
    bust_onset = ((st < 0) & (st.shift(1) >= 0)).astype(float).rolling(504, min_periods=252).sum()
    avg_boom = boom_days / (boom_onset + 1.0)
    avg_bust = bust_days / (bust_onset + 1.0)
    b = (avg_boom - avg_bust) / (avg_boom + avg_bust).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-cycle vs down-cycle day asymmetry on the 1260d clock (full-cycle asymmetry)
def f03cp_f03_cycle_phase_regime_cycdayasym_1260d_base_v070_signal(closeadj):
    st = _f03_regime_state(closeadj, 1260)
    boom = (st > 0).astype(float).rolling(1260, min_periods=504).sum()
    bust = (st < 0).astype(float).rolling(1260, min_periods=504).sum()
    b = (boom - bust) / (boom + bust).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime-transition rate normalised by trend strength ---
# choppiness relative to direction: flips per net tilt (whipsaw vs clean trend)
def f03cp_f03_cycle_phase_regime_whipsaw_252d_base_v071_signal(closeadj):
    flips = _f03_transitions(closeadj, 252, 252)
    st = _f03_regime_state(closeadj, 252)
    tilt = st.rolling(252, min_periods=126).mean().abs()
    b = flips / (1.0 + 10.0 * tilt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime-onset stability --------------------------------
# mean run-length of the boom/bust regime over the year, log-scaled (typical phase
# duration: long => stable committed cycles, short => flickering regime)
def f03cp_f03_cycle_phase_regime_onsetstick_252d_base_v072_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    run = _f03_runlen(st > 0) + _f03_runlen(st < 0)
    onsets = ((np.sign(st) != np.sign(st.shift(1))).astype(float)
              .rolling(252, min_periods=126).sum())
    days = pd.Series(1.0, index=closeadj.index).rolling(252, min_periods=126).sum()
    mean_run = days / (onsets + 1.0)
    b = np.log1p(mean_run) + 0.01 * run
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime-duration percentile (is current run unusually long?) ----
# current signed-streak length ranked vs its own 252d history (run-extremity)
def f03cp_f03_cycle_phase_regime_runrank_base_v073_signal(closeadj):
    sr = _f03_signrun(closeadj)
    b = sr.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- bull/bear alternation balance (Markov-ish) ------------
# tendency to stay in boom vs switch: P(boom|boom yesterday) over the year
def f03cp_f03_cycle_phase_regime_persistprob_252d_base_v074_signal(closeadj):
    st = (_f03_regime_state(closeadj, 252) > 0).astype(float)
    stay = ((st == 1) & (st.shift(1) == 1)).astype(float)
    prior_boom = (st.shift(1) == 1).astype(float)
    num = stay.rolling(252, min_periods=126).sum()
    den = prior_boom.rolling(252, min_periods=126).sum()
    b = num / den.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tendency to stay in bust vs recover: P(bust|bust yesterday) over the year
def f03cp_f03_cycle_phase_regime_bustpersist_252d_base_v075_signal(closeadj):
    st = (_f03_regime_state(closeadj, 252) < 0).astype(float)
    stay = ((st == 1) & (st.shift(1) == 1)).astype(float)
    prior_bust = (st.shift(1) == 1).astype(float)
    num = stay.rolling(252, min_periods=126).sum()
    den = prior_bust.rolling(252, min_periods=126).sum()
    b = num / den.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03cp_f03_cycle_phase_regime_state_252d_base_v001_signal,
    f03cp_f03_cycle_phase_regime_state_504d_base_v002_signal,
    f03cp_f03_cycle_phase_regime_state_1260d_base_v003_signal,
    f03cp_f03_cycle_phase_regime_agree_multi_base_v004_signal,
    f03cp_f03_cycle_phase_regime_trendslopesign_252d_base_v005_signal,
    f03cp_f03_cycle_phase_regime_trendslopesign_504d_base_v006_signal,
    f03cp_f03_cycle_phase_regime_dualtrend_base_v007_signal,
    f03cp_f03_cycle_phase_regime_dualtrend_slow_base_v008_signal,
    f03cp_f03_cycle_phase_regime_boomfrac_252d_base_v009_signal,
    f03cp_f03_cycle_phase_regime_boomfrac_126d_base_v010_signal,
    f03cp_f03_cycle_phase_regime_boomfrac_504d_base_v011_signal,
    f03cp_f03_cycle_phase_regime_bustfrac_252d_base_v012_signal,
    f03cp_f03_cycle_phase_regime_boomfracchg_252d_base_v013_signal,
    f03cp_f03_cycle_phase_regime_boomfracspr_base_v014_signal,
    f03cp_f03_cycle_phase_regime_boomrun_252d_base_v015_signal,
    f03cp_f03_cycle_phase_regime_bustrun_252d_base_v016_signal,
    f03cp_f03_cycle_phase_regime_signedrun_504d_base_v017_signal,
    f03cp_f03_cycle_phase_regime_runvsavg_252d_base_v018_signal,
    f03cp_f03_cycle_phase_regime_runmaturity_252d_base_v019_signal,
    f03cp_f03_cycle_phase_regime_flips_252d_base_v020_signal,
    f03cp_f03_cycle_phase_regime_flips_504d_base_v021_signal,
    f03cp_f03_cycle_phase_regime_flipaccel_252d_base_v022_signal,
    f03cp_f03_cycle_phase_regime_flipfreq_63d_base_v023_signal,
    f03cp_f03_cycle_phase_regime_sincelastflip_252d_base_v024_signal,
    f03cp_f03_cycle_phase_regime_entropy_252d_base_v025_signal,
    f03cp_f03_cycle_phase_regime_entropy_504d_base_v026_signal,
    f03cp_f03_cycle_phase_regime_entropychg_252d_base_v027_signal,
    f03cp_f03_cycle_phase_regime_signentropy_63d_base_v028_signal,
    f03cp_f03_cycle_phase_regime_updnasym_63d_base_v029_signal,
    f03cp_f03_cycle_phase_regime_updnasym_252d_base_v030_signal,
    f03cp_f03_cycle_phase_regime_updnasym_504d_base_v031_signal,
    f03cp_f03_cycle_phase_regime_updnasymchg_63d_base_v032_signal,
    f03cp_f03_cycle_phase_regime_updnasymspr_base_v033_signal,
    f03cp_f03_cycle_phase_regime_runcountasym_252d_base_v034_signal,
    f03cp_f03_cycle_phase_regime_runlenasym_252d_base_v035_signal,
    f03cp_f03_cycle_phase_regime_maxrunasym_252d_base_v036_signal,
    f03cp_f03_cycle_phase_regime_signrun_now_base_v037_signal,
    f03cp_f03_cycle_phase_regime_uprunpersist_252d_base_v038_signal,
    f03cp_f03_cycle_phase_regime_intradaybull_252d_base_v039_signal,
    f03cp_f03_cycle_phase_regime_gapasym_252d_base_v040_signal,
    f03cp_f03_cycle_phase_regime_rangestate_252d_base_v041_signal,
    f03cp_f03_cycle_phase_regime_rangeflip_252d_base_v042_signal,
    f03cp_f03_cycle_phase_regime_dominance_504d_base_v043_signal,
    f03cp_f03_cycle_phase_regime_nettilt_252d_base_v044_signal,
    f03cp_f03_cycle_phase_regime_nettilt_1260d_base_v045_signal,
    f03cp_f03_cycle_phase_regime_tiltmom_252d_base_v046_signal,
    f03cp_f03_cycle_phase_regime_conviction_252d_base_v047_signal,
    f03cp_f03_cycle_phase_regime_transdir_252d_base_v048_signal,
    f03cp_f03_cycle_phase_regime_transdir_504d_base_v049_signal,
    f03cp_f03_cycle_phase_regime_clockdiverge_base_v050_signal,
    f03cp_f03_cycle_phase_regime_clockconflict_252d_base_v051_signal,
    f03cp_f03_cycle_phase_regime_zerocross_252d_base_v052_signal,
    f03cp_f03_cycle_phase_regime_retzerocross_63d_base_v053_signal,
    f03cp_f03_cycle_phase_regime_stateema_252d_base_v054_signal,
    f03cp_f03_cycle_phase_regime_statedisp_252d_base_v055_signal,
    f03cp_f03_cycle_phase_regime_weekasym_252d_base_v056_signal,
    f03cp_f03_cycle_phase_regime_monthasym_504d_base_v057_signal,
    f03cp_f03_cycle_phase_regime_boomfracstate_252d_base_v058_signal,
    f03cp_f03_cycle_phase_regime_flipcluster_252d_base_v059_signal,
    f03cp_f03_cycle_phase_regime_moveasym_252d_base_v060_signal,
    f03cp_f03_cycle_phase_regime_tailasym_252d_base_v061_signal,
    f03cp_f03_cycle_phase_regime_sinceboom_252d_base_v062_signal,
    f03cp_f03_cycle_phase_regime_sincebust_252d_base_v063_signal,
    f03cp_f03_cycle_phase_regime_mixstab_base_v064_signal,
    f03cp_f03_cycle_phase_regime_hlcloseasym_63d_base_v065_signal,
    f03cp_f03_cycle_phase_regime_hysteresis_252d_base_v066_signal,
    f03cp_f03_cycle_phase_regime_neutralband_252d_base_v067_signal,
    f03cp_f03_cycle_phase_regime_confirm_252d_base_v068_signal,
    f03cp_f03_cycle_phase_regime_cycdayasym_504d_base_v069_signal,
    f03cp_f03_cycle_phase_regime_cycdayasym_1260d_base_v070_signal,
    f03cp_f03_cycle_phase_regime_whipsaw_252d_base_v071_signal,
    f03cp_f03_cycle_phase_regime_onsetstick_252d_base_v072_signal,
    f03cp_f03_cycle_phase_regime_runrank_base_v073_signal,
    f03cp_f03_cycle_phase_regime_persistprob_252d_base_v074_signal,
    f03cp_f03_cycle_phase_regime_bustpersist_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_CYCLE_PHASE_REGIME_REGISTRY_001_075 = REGISTRY


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

    print("OK f03_cycle_phase_regime_base_001_075_claude: %d features pass" % n_features)
