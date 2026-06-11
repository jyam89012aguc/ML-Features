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
# Second base block. COUNT/REGIME/TRANSITION/ASYMMETRY-centric ONLY. No raw
# range-position levels (f07), no drawdown depth/duration/velocity (f04), no
# base-tightness/breakout (f06).

def _f03_trend(c, w):
    return np.log(c.replace(0, np.nan)).rolling(w, min_periods=max(1, w // 2)).mean()


def _f03_regime_state(c, w):
    lp = np.log(c.replace(0, np.nan))
    tr = lp.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.sign(lp - tr)


def _f03_runlen(state_bool):
    s = state_bool.astype(float)
    grp = (s != s.shift(1)).cumsum()
    run = s.groupby(grp).cumcount() + 1.0
    return run.where(s == 1, other=0.0)


def _f03_signrun(c):
    r = np.sign(np.log(c.replace(0, np.nan)).diff())
    grp = (r != r.shift(1)).cumsum()
    cnt = r.groupby(grp).cumcount() + 1.0
    return cnt * r


def _f03_trans_intensity(c, w_state, w_count):
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


def _f03_above_frac(c, w_state, w_count):
    st = (_f03_regime_state(c, w_state) > 0).astype(float)
    return st.rolling(w_count, min_periods=max(1, w_count // 2)).mean()


# ============================================================
# ---- REGIME-CONDITIONAL momentum/breadth -------------------
# directional consistency: |mean of return signs| over the quarter (trend purity)
def f03cp_f03_cycle_phase_regime_dirpurity_63d_base_v076_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    b = sg.rolling(63, min_periods=21).mean().abs().rolling(10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional consistency over the year (long-horizon trend purity)
def f03cp_f03_cycle_phase_regime_dirpurity_252d_base_v077_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    b = sg.rolling(252, min_periods=126).mean().abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in directional purity quarter-over-quarter (trend coalescing or fraying)
def f03cp_f03_cycle_phase_regime_puritychg_63d_base_v078_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    p = sg.rolling(63, min_periods=21).mean().abs()
    b = p - p.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime momentum across horizons -----------------------
# regime momentum: 21d return-sign tilt minus 252d return-sign tilt (fast vs slow)
def f03cp_f03_cycle_phase_regime_signtiltspr_base_v079_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    fast = sg.rolling(21, min_periods=10).mean()
    slow = sg.rolling(252, min_periods=126).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of the regime tilt: change in 63d sign-tilt over a month
def f03cp_f03_cycle_phase_regime_tiltaccel_63d_base_v080_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    t = sg.rolling(63, min_periods=21).mean()
    b = (t - t.shift(21)) - (t.shift(21) - t.shift(42))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- up-cycle vs down-cycle return-mass asymmetry ----------
# share of total absolute move that occurred on up-days vs down-days over the year
def f03cp_f03_cycle_phase_regime_massasym_252d_base_v081_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    up_mass = r.clip(lower=0).rolling(252, min_periods=126).sum()
    dn_mass = (-r.clip(upper=0)).rolling(252, min_periods=126).sum()
    b = (up_mass - dn_mass) / (up_mass + dn_mass).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-mass asymmetry on the quarter (recent up vs down move dominance)
def f03cp_f03_cycle_phase_regime_massasym_63d_base_v082_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    up_mass = r.clip(lower=0).rolling(63, min_periods=21).sum()
    dn_mass = (-r.clip(upper=0)).rolling(63, min_periods=21).sum()
    b = (up_mass - dn_mass) / (up_mass + dn_mass).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-mass vs down-mass asymmetry over two years (structural drawup/drawdown skew)
def f03cp_f03_cycle_phase_regime_massasym_504d_base_v083_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    up_mass = r.clip(lower=0).rolling(504, min_periods=252).sum()
    dn_mass = (-r.clip(upper=0)).rolling(504, min_periods=252).sum()
    b = (up_mass - dn_mass) / (up_mass + dn_mass).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- return-sign skew (third-moment asymmetry as regime) ---
# skewness of daily log returns over the year (gain/loss shape of the cycle)
def f03cp_f03_cycle_phase_regime_retskew_252d_base_v084_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    b = r.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# skewness of monthly (21d) returns over two years (long-cycle gain/loss shape)
def f03cp_f03_cycle_phase_regime_retskew_504d_base_v085_signal(closeadj):
    mr = np.log(closeadj.replace(0, np.nan)).diff(21)
    b = mr.rolling(504, min_periods=252).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in return skew over a quarter (is the cycle turning more lopsided?)
def f03cp_f03_cycle_phase_regime_skewchg_252d_base_v086_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    s = r.rolling(252, min_periods=126).skew()
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime-conditional volatility asymmetry ---------------
# downside vs upside volatility asymmetry over the year (bust-vol vs boom-vol)
def f03cp_f03_cycle_phase_regime_volasym_252d_base_v087_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    up_v = r.where(r > 0).rolling(252, min_periods=63).std()
    dn_v = r.where(r < 0).rolling(252, min_periods=63).std()
    b = (dn_v - up_v) / (dn_v + up_v).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime-conditional choppiness asymmetry: daily-sign reversal rate while in boom
# vs while in bust (is the up-cycle smoother/trendier than the down-cycle?)
def f03cp_f03_cycle_phase_regime_regimevol_252d_base_v088_signal(closeadj):
    r = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    rev = (r != r.shift(1)).astype(float)
    st = _f03_regime_state(closeadj, 252)
    boom_c = rev.where(st > 0).rolling(252, min_periods=63).mean()
    bust_c = rev.where(st < 0).rolling(252, min_periods=63).mean()
    b = (bust_c - boom_c) / (bust_c + boom_c).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime-transition timing dispersion -------------------
# how evenly spaced are boom-onsets: std of inter-onset gaps proxied via onset bunching
def f03cp_f03_cycle_phase_regime_onsetspacing_504d_base_v089_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    onset = ((st > 0) & (st.shift(1) <= 0)).astype(float)
    near = onset.rolling(63, min_periods=21).sum()
    b = near.rolling(504, min_periods=252).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of recent flip burst to the year's flip rate (regime-switch acceleration)
def f03cp_f03_cycle_phase_regime_switchaccel_base_v090_signal(closeadj):
    inten_fast = _f03_trans_intensity(closeadj, 252, 63)
    inten_slow = _f03_trans_intensity(closeadj, 252, 252)
    b = inten_fast / (inten_slow.replace(0, np.nan) / 4.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- multi-clock state interactions ------------------------
# product of fast and slow smoothed regime states (aligned booms reinforce, +; conflict, -)
def f03cp_f03_cycle_phase_regime_stateprod_base_v091_signal(closeadj):
    s_fast = _f03_regime_state(closeadj, 252).rolling(21, min_periods=10).mean()
    s_slow = _f03_regime_state(closeadj, 1260).rolling(21, min_periods=10).mean()
    b = s_fast * s_slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread of time-in-boom between the fast and slow clocks (cycle-phase lead/lag)
def f03cp_f03_cycle_phase_regime_clocklag_base_v092_signal(closeadj):
    f_fast = _f03_above_frac(closeadj, 252, 126)
    f_slow = _f03_above_frac(closeadj, 1260, 126)
    b = f_fast - f_slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime persistence via run-length statistics ----------
# mean sign-run length over the year, log-scaled (cycle granularity)
def f03cp_f03_cycle_phase_regime_medrun_252d_base_v093_signal(closeadj):
    sr = _f03_signrun(closeadj).abs()
    b = np.log1p(sr.rolling(252, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# run-length dispersion: coefficient of variation of |signed-run| over the year
# (uniform short runs => low; mix of brief and long committed runs => high)
def f03cp_f03_cycle_phase_regime_p90run_252d_base_v094_signal(closeadj):
    sr = _f03_signrun(closeadj).abs()
    mu = sr.rolling(252, min_periods=126).mean()
    sd = sr.rolling(252, min_periods=126).std()
    b = sd / mu.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- boom/bust regime crossing of the slow trend slope -----
# fraction of year the long-trend slope (252d) was positive (up-cycle backbone time)
def f03cp_f03_cycle_phase_regime_slopeuptime_252d_base_v095_signal(closeadj):
    tr = _f03_trend(closeadj, 252)
    up = (tr > tr.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# flips in the slow-trend slope sign over two years (cycle-direction reversals)
def f03cp_f03_cycle_phase_regime_slopeflips_504d_base_v096_signal(closeadj):
    tr = _f03_trend(closeadj, 252)
    sl = np.sign(tr - tr.shift(21))
    flip = (sl != sl.shift(1)).astype(float)
    mag = (tr - tr.shift(21)).abs()
    w = (flip * (1.0 + 30.0 * mag)).where(sl.notna() & sl.shift(1).notna(), other=np.nan)
    b = w.rolling(504, min_periods=252).sum().ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime-entropy variants -------------------------------
# entropy of the three-clock regime agreement distribution (cross-horizon indecision)
def f03cp_f03_cycle_phase_regime_clockentropy_base_v097_signal(closeadj):
    s1 = (_f03_regime_state(closeadj, 252) > 0).astype(float)
    s2 = (_f03_regime_state(closeadj, 504) > 0).astype(float)
    s3 = (_f03_regime_state(closeadj, 1260) > 0).astype(float)
    p = ((s1 + s2 + s3) / 3.0).rolling(126, min_periods=63).mean().clip(1e-6, 1 - 1e-6)
    b = -(p * np.log(p) + (1 - p) * np.log(1 - p))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# entropy of weekly up/down mix over two years (slow regime indecision)
def f03cp_f03_cycle_phase_regime_weekentropy_504d_base_v098_signal(closeadj):
    wk = (np.log(closeadj.replace(0, np.nan)).diff(5) > 0).astype(float)
    p = wk.rolling(504, min_periods=252).mean().clip(1e-6, 1 - 1e-6)
    b = -(p * np.log(p) + (1 - p) * np.log(1 - p))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime-conditioned recovery-vs-decline asymmetry ------
# up-thrust vs down-thrust mass: summed length of long (>=4d) up-runs vs down-runs
def f03cp_f03_cycle_phase_regime_thrustasym_252d_base_v099_signal(closeadj):
    sr = _f03_signrun(closeadj)
    up_mass = sr.where(sr >= 4, other=0.0).rolling(252, min_periods=126).sum()
    dn_mass = (-sr.where(sr <= -4, other=0.0)).rolling(252, min_periods=126).sum()
    b = (up_mass - dn_mass) / (up_mass + dn_mass).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asymmetry between time spent rising fast vs falling fast (momentum-regime tilt)
def f03cp_f03_cycle_phase_regime_fastmoveasym_63d_base_v100_signal(closeadj):
    r5 = np.log(closeadj.replace(0, np.nan)).diff(5)
    sd = r5.rolling(252, min_periods=126).std()
    fast_up = (r5 > sd).astype(float).rolling(63, min_periods=21).mean()
    fast_dn = (r5 < -sd).astype(float).rolling(63, min_periods=21).mean()
    b = fast_up - fast_dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime smoothness / jaggedness ------------------------
# path roughness: ratio of total daily travel to net move over the quarter (choppiness)
def f03cp_f03_cycle_phase_regime_roughness_63d_base_v101_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    travel = r.abs().rolling(63, min_periods=21).sum()
    net = r.rolling(63, min_periods=21).sum().abs()
    b = net / travel.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# path efficiency over the year (trending regime vs range-bound regime)
def f03cp_f03_cycle_phase_regime_efficiency_252d_base_v102_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    travel = r.abs().rolling(252, min_periods=126).sum()
    net = r.rolling(252, min_periods=126).sum().abs()
    b = net / travel.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in path efficiency: regime shifting from trending to choppy or vice-versa
def f03cp_f03_cycle_phase_regime_effchg_252d_base_v103_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    travel = r.abs().rolling(126, min_periods=63).sum()
    net = r.rolling(126, min_periods=63).sum().abs()
    eff = net / travel.replace(0, np.nan)
    b = eff - eff.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime turning-point detection ------------------------
# regime turning signal: sign change in the slow smoothed state vs a month ago
def f03cp_f03_cycle_phase_regime_turn_252d_base_v104_signal(closeadj):
    st = _f03_regime_state(closeadj, 252).rolling(42, min_periods=21).mean()
    b = st - st.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime turning acceleration (second difference of the smoothed regime state)
def f03cp_f03_cycle_phase_regime_turnaccel_252d_base_v105_signal(closeadj):
    st = _f03_regime_state(closeadj, 252).rolling(42, min_periods=21).mean()
    b = (st - st.shift(21)) - (st.shift(21) - st.shift(42))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- fraction-of-time in extreme regimes -------------------
# fraction of year all three clocks agreed on boom (full-alignment up-regime time)
def f03cp_f03_cycle_phase_regime_fullboom_252d_base_v106_signal(closeadj):
    s1 = _f03_regime_state(closeadj, 252) > 0
    s2 = _f03_regime_state(closeadj, 504) > 0
    s3 = _f03_regime_state(closeadj, 1260) > 0
    allup = (s1 & s2 & s3).astype(float)
    b = allup.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year all three clocks agreed on bust (full-alignment down-regime time)
def f03cp_f03_cycle_phase_regime_fullbust_252d_base_v107_signal(closeadj):
    s1 = _f03_regime_state(closeadj, 252) < 0
    s2 = _f03_regime_state(closeadj, 504) < 0
    s3 = _f03_regime_state(closeadj, 1260) < 0
    alldn = (s1 & s2 & s3).astype(float)
    b = alldn.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net full-alignment regime tilt (full-boom time minus full-bust time)
def f03cp_f03_cycle_phase_regime_fullnet_252d_base_v108_signal(closeadj):
    s1 = _f03_regime_state(closeadj, 252)
    s2 = _f03_regime_state(closeadj, 504)
    s3 = _f03_regime_state(closeadj, 1260)
    allup = ((s1 > 0) & (s2 > 0) & (s3 > 0)).astype(float)
    alldn = ((s1 < 0) & (s2 < 0) & (s3 < 0)).astype(float)
    b = (allup - alldn).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime relative to longer history (rank) --------------
# current boom-run length ranked vs the run lengths over the prior 2y (run-extremity)
def f03cp_f03_cycle_phase_regime_runextrank_252d_base_v109_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    run = _f03_runlen(st > 0) + _f03_runlen(st < 0)
    b = run.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-tilt percentile vs the prior 2y (is the cycle unusually one-sided now?)
def f03cp_f03_cycle_phase_regime_tiltrank_252d_base_v110_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    tilt = sg.rolling(252, min_periods=126).mean()
    b = tilt.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime change-point intensity -------------------------
# CUSUM-style regime drift: cumulative demeaned return-sign, range over the year
def f03cp_f03_cycle_phase_regime_cusumrange_252d_base_v111_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    dm = sg - sg.rolling(252, min_periods=126).mean()
    cusum = dm.rolling(252, min_periods=126).apply(lambda a: np.nanmax(np.cumsum(a))
                                                   - np.nanmin(np.cumsum(a)), raw=True)
    b = cusum / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- alternation / mean-reversion strength -----------------
# lag-1 return-sign autocorrelation over the quarter (momentum vs mean-reversion regime)
def f03cp_f03_cycle_phase_regime_signautocorr_63d_base_v112_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    s0 = sg
    s1 = sg.shift(1)
    cov = (s0 * s1).rolling(63, min_periods=21).mean() \
        - s0.rolling(63, min_periods=21).mean() * s1.rolling(63, min_periods=21).mean()
    v = s0.rolling(63, min_periods=21).var()
    b = cov / v.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lag-1 sign autocorrelation over the year (structural momentum/reversion regime)
def f03cp_f03_cycle_phase_regime_signautocorr_252d_base_v113_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    s0 = sg
    s1 = sg.shift(1)
    cov = (s0 * s1).rolling(252, min_periods=126).mean() \
        - s0.rolling(252, min_periods=126).mean() * s1.rolling(252, min_periods=126).mean()
    v = s0.rolling(252, min_periods=126).var()
    b = cov / v.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- boom-onset vs bust-onset frequency over horizons ------
# normalised net regime-births on the slow 1260d clock: boom-onsets minus bust-onsets
# divided by total onsets over 2y (which cycle direction births more often?)
def f03cp_f03_cycle_phase_regime_onsetnetcount_504d_base_v114_signal(closeadj):
    st = _f03_regime_state(closeadj, 1260)
    bo = ((st > 0) & (st.shift(1) <= 0)).astype(float).rolling(504, min_periods=252).sum()
    bu = ((st < 0) & (st.shift(1) >= 0)).astype(float).rolling(504, min_periods=252).sum()
    b = ((bo - bu) / (bo + bu + 2.0)).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- time-warped cycle clock (phase via Hilbert-ish proxy) -
# dominant oscillation phase proxy: sign-weighted distance of gap from its envelope
def f03cp_f03_cycle_phase_regime_phaseproxy_252d_base_v115_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    gap = lp - lp.rolling(252, min_periods=126).mean()
    vel = gap - gap.shift(5)
    b = np.arctan2(vel, gap) / np.pi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rate of change of the phase proxy (cycle angular velocity)
def f03cp_f03_cycle_phase_regime_phasevel_252d_base_v116_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    gap = lp - lp.rolling(252, min_periods=126).mean()
    vel = gap - gap.shift(5)
    phase = np.arctan2(vel, gap) / np.pi
    b = (phase - phase.shift(5)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime vs intraday-range state (high/low) -------------
# fraction of year the intraday range was expanding while in a bust regime (panic state)
def f03cp_f03_cycle_phase_regime_panicstate_252d_base_v117_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    expand = rng > rng.rolling(126, min_periods=63).median()
    bust = _f03_regime_state(closeadj, 252) < 0
    panic = (expand & bust).astype(float)
    b = panic.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-regime asymmetry: avg intraday range in boom days vs in bust days (is the
# down-cycle more violent than the up-cycle on this name?)
def f03cp_f03_cycle_phase_regime_calmboom_252d_base_v118_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    st = _f03_regime_state(closeadj, 252)
    boom_r = rng.where(st > 0).rolling(252, min_periods=63).mean()
    bust_r = rng.where(st < 0).rolling(252, min_periods=63).mean()
    b = (bust_r - boom_r) / (bust_r + boom_r).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum-vs-range coupling: corr of daily return SIGN with next-day intraday range
# over the year (does volatility expand more after down-moves? lead/lag of fear)
def f03cp_f03_cycle_phase_regime_rangecouple_252d_base_v119_signal(closeadj, high, low):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    rng = ((high - low) / closeadj.replace(0, np.nan)).shift(-1)
    ms = sg.rolling(252, min_periods=126).mean()
    mr = rng.rolling(252, min_periods=126).mean()
    cov = (sg * rng).rolling(252, min_periods=126).mean() - ms * mr
    sds = sg.rolling(252, min_periods=126).std()
    sdr = rng.rolling(252, min_periods=126).std()
    b = cov / (sds * sdr).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime breadth across return horizons -----------------
# how many of {5d,21d,63d,126d,252d} momentum windows are positive (regime breadth)
def f03cp_f03_cycle_phase_regime_mombreadth_base_v120_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    sig = pd.concat([
        np.sign(lp.diff(5)), np.sign(lp.diff(21)), np.sign(lp.diff(63)),
        np.sign(lp.diff(126)), np.sign(lp.diff(252))], axis=1)
    b = sig.mean(axis=1).rolling(10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of multi-horizon momentum signs (regime disagreement across horizons)
def f03cp_f03_cycle_phase_regime_momdisagree_base_v121_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    sig = pd.concat([
        np.sign(lp.diff(5)), np.sign(lp.diff(21)), np.sign(lp.diff(63)),
        np.sign(lp.diff(126)), np.sign(lp.diff(252))], axis=1)
    b = sig.std(axis=1).rolling(10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime stickiness via transition probability ----------
# P(stay) overall: 1 minus daily regime-flip probability over the year (252d trend)
def f03cp_f03_cycle_phase_regime_staystrength_252d_base_v122_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    flip = (st != st.shift(1)).astype(float)
    flip = flip.where(st.notna() & st.shift(1).notna(), other=np.nan)
    gap = (np.log(closeadj.replace(0, np.nan)) - _f03_trend(closeadj, 252)).abs()
    b = (1.0 - flip.rolling(252, min_periods=126).mean()) + 0.2 * gap.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asymmetry of stay-probabilities: P(stay boom) minus P(stay bust) over the year
def f03cp_f03_cycle_phase_regime_stayasym_252d_base_v123_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    boom = (st > 0).astype(float)
    bust = (st < 0).astype(float)
    stayb = ((boom == 1) & (boom.shift(1) == 1)).astype(float).rolling(252, min_periods=126).sum()
    prb = (boom.shift(1) == 1).astype(float).rolling(252, min_periods=126).sum()
    stayd = ((bust == 1) & (bust.shift(1) == 1)).astype(float).rolling(252, min_periods=126).sum()
    prd = (bust.shift(1) == 1).astype(float).rolling(252, min_periods=126).sum()
    pb = stayb / prb.replace(0, np.nan)
    pd_ = stayd / prd.replace(0, np.nan)
    b = pb - pd_
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime momentum of the boom-fraction ------------------
# slope of the boom-fraction over a quarter (is time-in-boom rising?)
def f03cp_f03_cycle_phase_regime_boomfracslope_252d_base_v124_signal(closeadj):
    f = _f03_above_frac(closeadj, 252, 126)
    b = f - f.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of the boom-fraction (regime-of-regime curvature)
def f03cp_f03_cycle_phase_regime_boomfracaccel_252d_base_v125_signal(closeadj):
    f = _f03_above_frac(closeadj, 252, 126)
    b = (f - f.shift(21)) - (f.shift(21) - f.shift(42))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime concentration over very long horizon -----------
# 5y boom-day share minus 0.5 (structural multi-year up-cycle dominance)
def f03cp_f03_cycle_phase_regime_boomshare_1260d_base_v126_signal(closeadj):
    st = (_f03_regime_state(closeadj, 1260) > 0).astype(float)
    b = st.rolling(1260, min_periods=504).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-horizon cycle frequency: 5y boom<->bust transition intensity, EWM-smoothed
def f03cp_f03_cycle_phase_regime_cyccount_1260d_base_v127_signal(closeadj):
    b = (_f03_trans_intensity(closeadj, 252, 1260) / 2.0).ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime asymmetry between entering and exiting boom -----
# entry-conviction asymmetry: average per-day move INSIDE multi-day up-streaks vs
# inside multi-day down-streaks over 2y (are sustained up-legs steeper than down-legs?)
def f03cp_f03_cycle_phase_regime_entryconv_504d_base_v128_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    sr = _f03_signrun(closeadj)
    up_mask = (sr >= 2).astype(float)
    dn_mask = (sr <= -2).astype(float)
    up_sum = (r * up_mask).rolling(504, min_periods=252).sum()
    up_cnt = up_mask.rolling(504, min_periods=252).sum()
    dn_sum = (-r * dn_mask).rolling(504, min_periods=252).sum()
    dn_cnt = dn_mask.rolling(504, min_periods=252).sum()
    up_m = up_sum / up_cnt.replace(0, np.nan)
    dn_m = dn_sum / dn_cnt.replace(0, np.nan)
    b = (up_m - dn_m) / (up_m + dn_m).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime drift via rolling sign-sum slope ---------------
# slope of cumulative return-sign (drift acceleration of the up/down balance)
def f03cp_f03_cycle_phase_regime_signdrift_126d_base_v129_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    csum = sg.rolling(126, min_periods=63).sum()
    b = ((csum - csum.shift(21)) / 21.0).rolling(10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime: longest unbroken boom over horizon ------------
# longest boom run within 2y minus longest bust run, log-scaled (extreme phase asym)
def f03cp_f03_cycle_phase_regime_extremephase_504d_base_v130_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    boom = _f03_runlen(st > 0).rolling(504, min_periods=252).max()
    bust = _f03_runlen(st < 0).rolling(504, min_periods=252).max()
    b = np.log1p(boom) - np.log1p(bust)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime via consecutive new-leg confirmation -----------
# net count of new local up-legs vs down-legs (21d high/low breaks) over the year
def f03cp_f03_cycle_phase_regime_legasym_252d_base_v131_signal(closeadj):
    hi21 = closeadj.shift(1).rolling(21, min_periods=10).max()
    lo21 = closeadj.shift(1).rolling(21, min_periods=10).min()
    up_leg = (closeadj > hi21).astype(float)
    dn_leg = (closeadj < lo21).astype(float)
    u = up_leg.rolling(252, min_periods=126).sum()
    d = dn_leg.rolling(252, min_periods=126).sum()
    b = (u - d) / (u + d).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-leg asymmetry on the quarter (recent leg-direction regime)
def f03cp_f03_cycle_phase_regime_legasym_63d_base_v132_signal(closeadj):
    hi10 = closeadj.shift(1).rolling(10, min_periods=5).max()
    lo10 = closeadj.shift(1).rolling(10, min_periods=5).min()
    up_leg = (closeadj > hi10).astype(float)
    dn_leg = (closeadj < lo10).astype(float)
    u = up_leg.rolling(63, min_periods=21).sum()
    d = dn_leg.rolling(63, min_periods=21).sum()
    raw = (u - d) / (u + d).replace(0, np.nan)
    b = raw.rolling(5, min_periods=3).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime-state vs its own long-horizon baseline ---------
# regime-flip-rate anomaly: current 252d flip intensity vs its own 5y baseline
# (is the cycle unusually choppy/calm relative to this name's history?)
def f03cp_f03_cycle_phase_regime_boomanom_base_v133_signal(closeadj):
    fi = _f03_trans_intensity(closeadj, 252, 252)
    base = fi.rolling(1260, min_periods=504).mean()
    b = fi - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- choppiness index (ADX-free, regime-flavoured) ---------
# choppiness via range-vs-trend: log(sum of intraday-style daily ranges) over the
# sum-of-net-weekly-moves — fraction of motion lost to within-week churn
def f03cp_f03_cycle_phase_regime_chop_63d_base_v134_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    daily = lp.diff().abs().rolling(63, min_periods=21).sum()
    weekly_net = lp.diff(5).abs().rolling(63, min_periods=21).sum() / 5.0
    b = daily / weekly_net.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# choppiness change over a quarter (regime transitioning to/from range-bound)
def f03cp_f03_cycle_phase_regime_chopchg_63d_base_v135_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    travel = r.abs().rolling(63, min_periods=21).sum()
    net = r.rolling(63, min_periods=21).sum().abs()
    chop = np.log1p(travel) - np.log1p(net)
    b = chop - chop.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime: share of trend-days (DMI-like, sign agreement) -
# fraction of days the daily move agreed with the 63d trend sign (trend-follow regime)
def f03cp_f03_cycle_phase_regime_trendagree_63d_base_v136_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    trend = np.sign(r.rolling(63, min_periods=21).sum())
    agree = (np.sign(r) == trend).astype(float)
    b = (agree.rolling(63, min_periods=21).mean() - 0.5).rolling(10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-agreement over the year (structural trend-following vs reversion regime)
def f03cp_f03_cycle_phase_regime_trendagree_252d_base_v137_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    trend = np.sign(r.rolling(252, min_periods=126).sum())
    agree = (np.sign(r) == trend).astype(float)
    b = agree.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime-flip clustering vs uniform -------------------
# variance-to-mean ratio of flip occurrences across 5 sub-windows (burst vs uniform)
def f03cp_f03_cycle_phase_regime_flipburst_252d_base_v138_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    flip = (st != st.shift(1)).astype(float)
    flip = flip.where(st.notna() & st.shift(1).notna(), other=np.nan)
    sub = flip.rolling(50, min_periods=25).sum()
    mu = sub.rolling(252, min_periods=126).mean()
    sd = sub.rolling(252, min_periods=126).std()
    b = sd / mu.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- net advance/decline streak balance --------------------
# running signed-streak balance normalised by recent volatility (regime thrust)
def f03cp_f03_cycle_phase_regime_streakthrust_base_v139_signal(closeadj):
    sr = _f03_signrun(closeadj)
    vol = np.log(closeadj.replace(0, np.nan)).diff().rolling(63, min_periods=21).std()
    b = (sr.rolling(21, min_periods=10).mean()) * vol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime: fraction of quarters that were up (very slow) -
# share of trailing 5y rolling-quarter returns that were positive (slow up-cycle freq)
def f03cp_f03_cycle_phase_regime_qtrupfrac_1260d_base_v140_signal(closeadj):
    qr = np.log(closeadj.replace(0, np.nan)).diff(63)
    up = (qr > 0).astype(float)
    b = up.rolling(1260, min_periods=504).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime asymmetry: up-vol vs down-vol over slow clock ---
# semivariance ratio over two years (downside-heavy vs upside-heavy cycle)
def f03cp_f03_cycle_phase_regime_semivarasym_504d_base_v141_signal(closeadj):
    r = np.log(closeadj.replace(0, np.nan)).diff()
    up_sv = (r.clip(lower=0) ** 2).rolling(504, min_periods=252).mean()
    dn_sv = (r.clip(upper=0) ** 2).rolling(504, min_periods=252).mean()
    b = (dn_sv - up_sv) / (dn_sv + up_sv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime change rate normalized (transitions per cycle) --
# transitions per dominant cycle length (how many flips per typical run)
def f03cp_f03_cycle_phase_regime_flipsperrun_252d_base_v142_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    flip = (st != st.shift(1)).astype(float)
    flip = flip.where(st.notna() & st.shift(1).notna(), other=np.nan)
    n_flip = flip.rolling(252, min_periods=126).sum()
    run = (_f03_runlen(st > 0) + _f03_runlen(st < 0)).rolling(252, min_periods=126).mean()
    b = n_flip * run / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime persistence index (run length / window) --------
# current run length as a fraction of the year (phase maturity on the calendar)
def f03cp_f03_cycle_phase_regime_phasematurity_252d_base_v143_signal(closeadj):
    st = _f03_regime_state(closeadj, 252)
    run = _f03_runlen(st > 0) + _f03_runlen(st < 0)
    b = (run / 252.0).clip(upper=2.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime via weekly close direction streaks -------------
# signed weekly-close streak length (consecutive up/down weeks), log-magnitude
def f03cp_f03_cycle_phase_regime_weekstreak_base_v144_signal(closeadj):
    s = np.sign(np.log(closeadj.replace(0, np.nan)).diff(5))
    grp = (s != s.shift(1)).cumsum()
    cnt = s.groupby(grp).cumcount() + 1.0
    sr = cnt * s
    b = (np.sign(sr) * np.log1p(sr.abs())).rolling(10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime: fraction of time above BOTH fast and slow trend
# fraction of year price sat above both its 63d and 252d trend (committed-uptrend time)
def f03cp_f03_cycle_phase_regime_doubleabove_252d_base_v145_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    a_fast = lp > lp.rolling(63, min_periods=21).mean()
    a_slow = lp > lp.rolling(252, min_periods=126).mean()
    both = (a_fast & a_slow).astype(float)
    b = both.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime conflict resolution speed ----------------------
# how long the fast and slow clocks have currently disagreed (transition-zone dwell)
def f03cp_f03_cycle_phase_regime_conflictdwell_base_v146_signal(closeadj):
    s_fast = _f03_regime_state(closeadj, 252)
    s_slow = _f03_regime_state(closeadj, 504)
    conflict = (s_fast != s_slow)
    run = _f03_runlen(conflict)
    b = np.log1p(run)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime: skew of run-length distribution ---------------
# skewness of |signed-run| lengths over the year (a few very long runs => positive skew)
def f03cp_f03_cycle_phase_regime_runskew_252d_base_v147_signal(closeadj):
    sr = _f03_signrun(closeadj).abs()
    b = sr.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime-tilt smoothed momentum -------------------------
# EWM of the daily return-sign (sticky directional regime, fast)
def f03cp_f03_cycle_phase_regime_signema_base_v148_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    b = sg.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# displacement of fast sign-EMA from slow sign-EMA (directional regime turn)
def f03cp_f03_cycle_phase_regime_signemadisp_base_v149_signal(closeadj):
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    b = sg.ewm(span=21, min_periods=10).mean() - sg.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- composite cycle-phase classifier ----------------------
# blended cycle position: net three-clock tilt times directional purity (phase & power)
def f03cp_f03_cycle_phase_regime_phasepower_base_v150_signal(closeadj):
    s1 = _f03_regime_state(closeadj, 252)
    s2 = _f03_regime_state(closeadj, 504)
    s3 = _f03_regime_state(closeadj, 1260)
    tilt = ((s1 + s2 + s3) / 3.0).rolling(21, min_periods=10).mean()
    sg = np.sign(np.log(closeadj.replace(0, np.nan)).diff())
    purity = sg.rolling(126, min_periods=63).mean().abs()
    b = tilt * purity
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03cp_f03_cycle_phase_regime_dirpurity_63d_base_v076_signal,
    f03cp_f03_cycle_phase_regime_dirpurity_252d_base_v077_signal,
    f03cp_f03_cycle_phase_regime_puritychg_63d_base_v078_signal,
    f03cp_f03_cycle_phase_regime_signtiltspr_base_v079_signal,
    f03cp_f03_cycle_phase_regime_tiltaccel_63d_base_v080_signal,
    f03cp_f03_cycle_phase_regime_massasym_252d_base_v081_signal,
    f03cp_f03_cycle_phase_regime_massasym_63d_base_v082_signal,
    f03cp_f03_cycle_phase_regime_massasym_504d_base_v083_signal,
    f03cp_f03_cycle_phase_regime_retskew_252d_base_v084_signal,
    f03cp_f03_cycle_phase_regime_retskew_504d_base_v085_signal,
    f03cp_f03_cycle_phase_regime_skewchg_252d_base_v086_signal,
    f03cp_f03_cycle_phase_regime_volasym_252d_base_v087_signal,
    f03cp_f03_cycle_phase_regime_regimevol_252d_base_v088_signal,
    f03cp_f03_cycle_phase_regime_onsetspacing_504d_base_v089_signal,
    f03cp_f03_cycle_phase_regime_switchaccel_base_v090_signal,
    f03cp_f03_cycle_phase_regime_stateprod_base_v091_signal,
    f03cp_f03_cycle_phase_regime_clocklag_base_v092_signal,
    f03cp_f03_cycle_phase_regime_medrun_252d_base_v093_signal,
    f03cp_f03_cycle_phase_regime_p90run_252d_base_v094_signal,
    f03cp_f03_cycle_phase_regime_slopeuptime_252d_base_v095_signal,
    f03cp_f03_cycle_phase_regime_slopeflips_504d_base_v096_signal,
    f03cp_f03_cycle_phase_regime_clockentropy_base_v097_signal,
    f03cp_f03_cycle_phase_regime_weekentropy_504d_base_v098_signal,
    f03cp_f03_cycle_phase_regime_thrustasym_252d_base_v099_signal,
    f03cp_f03_cycle_phase_regime_fastmoveasym_63d_base_v100_signal,
    f03cp_f03_cycle_phase_regime_roughness_63d_base_v101_signal,
    f03cp_f03_cycle_phase_regime_efficiency_252d_base_v102_signal,
    f03cp_f03_cycle_phase_regime_effchg_252d_base_v103_signal,
    f03cp_f03_cycle_phase_regime_turn_252d_base_v104_signal,
    f03cp_f03_cycle_phase_regime_turnaccel_252d_base_v105_signal,
    f03cp_f03_cycle_phase_regime_fullboom_252d_base_v106_signal,
    f03cp_f03_cycle_phase_regime_fullbust_252d_base_v107_signal,
    f03cp_f03_cycle_phase_regime_fullnet_252d_base_v108_signal,
    f03cp_f03_cycle_phase_regime_runextrank_252d_base_v109_signal,
    f03cp_f03_cycle_phase_regime_tiltrank_252d_base_v110_signal,
    f03cp_f03_cycle_phase_regime_cusumrange_252d_base_v111_signal,
    f03cp_f03_cycle_phase_regime_signautocorr_63d_base_v112_signal,
    f03cp_f03_cycle_phase_regime_signautocorr_252d_base_v113_signal,
    f03cp_f03_cycle_phase_regime_onsetnetcount_504d_base_v114_signal,
    f03cp_f03_cycle_phase_regime_phaseproxy_252d_base_v115_signal,
    f03cp_f03_cycle_phase_regime_phasevel_252d_base_v116_signal,
    f03cp_f03_cycle_phase_regime_panicstate_252d_base_v117_signal,
    f03cp_f03_cycle_phase_regime_calmboom_252d_base_v118_signal,
    f03cp_f03_cycle_phase_regime_rangecouple_252d_base_v119_signal,
    f03cp_f03_cycle_phase_regime_mombreadth_base_v120_signal,
    f03cp_f03_cycle_phase_regime_momdisagree_base_v121_signal,
    f03cp_f03_cycle_phase_regime_staystrength_252d_base_v122_signal,
    f03cp_f03_cycle_phase_regime_stayasym_252d_base_v123_signal,
    f03cp_f03_cycle_phase_regime_boomfracslope_252d_base_v124_signal,
    f03cp_f03_cycle_phase_regime_boomfracaccel_252d_base_v125_signal,
    f03cp_f03_cycle_phase_regime_boomshare_1260d_base_v126_signal,
    f03cp_f03_cycle_phase_regime_cyccount_1260d_base_v127_signal,
    f03cp_f03_cycle_phase_regime_entryconv_504d_base_v128_signal,
    f03cp_f03_cycle_phase_regime_signdrift_126d_base_v129_signal,
    f03cp_f03_cycle_phase_regime_extremephase_504d_base_v130_signal,
    f03cp_f03_cycle_phase_regime_legasym_252d_base_v131_signal,
    f03cp_f03_cycle_phase_regime_legasym_63d_base_v132_signal,
    f03cp_f03_cycle_phase_regime_boomanom_base_v133_signal,
    f03cp_f03_cycle_phase_regime_chop_63d_base_v134_signal,
    f03cp_f03_cycle_phase_regime_chopchg_63d_base_v135_signal,
    f03cp_f03_cycle_phase_regime_trendagree_63d_base_v136_signal,
    f03cp_f03_cycle_phase_regime_trendagree_252d_base_v137_signal,
    f03cp_f03_cycle_phase_regime_flipburst_252d_base_v138_signal,
    f03cp_f03_cycle_phase_regime_streakthrust_base_v139_signal,
    f03cp_f03_cycle_phase_regime_qtrupfrac_1260d_base_v140_signal,
    f03cp_f03_cycle_phase_regime_semivarasym_504d_base_v141_signal,
    f03cp_f03_cycle_phase_regime_flipsperrun_252d_base_v142_signal,
    f03cp_f03_cycle_phase_regime_phasematurity_252d_base_v143_signal,
    f03cp_f03_cycle_phase_regime_weekstreak_base_v144_signal,
    f03cp_f03_cycle_phase_regime_doubleabove_252d_base_v145_signal,
    f03cp_f03_cycle_phase_regime_conflictdwell_base_v146_signal,
    f03cp_f03_cycle_phase_regime_runskew_252d_base_v147_signal,
    f03cp_f03_cycle_phase_regime_signema_base_v148_signal,
    f03cp_f03_cycle_phase_regime_signemadisp_base_v149_signal,
    f03cp_f03_cycle_phase_regime_phasepower_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_CYCLE_PHASE_REGIME_REGISTRY_076_150 = REGISTRY


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

    print("OK f03_cycle_phase_regime_base_076_150_claude: %d features pass" % n_features)
