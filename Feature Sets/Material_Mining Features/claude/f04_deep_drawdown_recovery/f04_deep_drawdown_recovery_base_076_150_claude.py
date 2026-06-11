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


# ===== folder domain primitives (deep drawdown & recovery) =====
def _f04_drawdown(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return close / peak.replace(0, np.nan) - 1.0


def _f04_maxdd(close, w):
    def _f(a):
        run = np.maximum.accumulate(a)
        dd = a / run - 1.0
        return np.min(dd)
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f04_recovery(close, w):
    trough = close.rolling(w, min_periods=max(1, w // 2)).min()
    return close / trough.replace(0, np.nan) - 1.0


def _f04_underwater_frac(close, w, thr):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    uw = close / peak.replace(0, np.nan) - 1.0
    deep = (uw <= thr).astype(float)
    return deep.rolling(w, min_periods=max(1, w // 2)).mean()


def _f04_ulcer(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    dd = close / peak.replace(0, np.nan) - 1.0
    return np.sqrt((dd ** 2).rolling(w, min_periods=max(1, w // 2)).mean())


def _f04_pain(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    dd = close / peak.replace(0, np.nan) - 1.0
    return (-dd).rolling(w, min_periods=max(1, w // 2)).mean()


def _f04_days_since_trough(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f04_days_since_peak(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f04_recov_slope(close, w, k):
    rec = _f04_recovery(close, w)
    return rec.diff(k) / float(k)


def _f04_max_run_up(close, w):
    # largest peak-to-recovery run-up inside the window (>= 0)
    def _f(a):
        run = np.minimum.accumulate(a)
        ru = a / run - 1.0
        return np.max(ru)
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


# ============================================================
# ---- short-window (50d) deep drawdown facet ----------------
# 50d current drawdown from peak
def f04dd_f04_deep_drawdown_recovery_curdd_50d_base_v076_signal(closeadj):
    b = _f04_drawdown(closeadj, 50)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 50d max drawdown z-scored vs its own 252d history (acute-bust extremity)
def f04dd_f04_deep_drawdown_recovery_maxddz_50d_base_v077_signal(closeadj):
    md = _f04_maxdd(closeadj, 50)
    b = _z(md, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 50d recovery off trough
def f04dd_f04_deep_drawdown_recovery_recov_50d_base_v078_signal(closeadj):
    b = _f04_recovery(closeadj, 50)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 50d drawdown relative to 252d drawdown (acute vs cyclical severity)
def f04dd_f04_deep_drawdown_recovery_ddratio_50v252_base_v079_signal(closeadj):
    s = _f04_drawdown(closeadj, 50)
    l = _f04_drawdown(closeadj, 252)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 50d ulcer index (acute pain)
def f04dd_f04_deep_drawdown_recovery_ulcer_50d_base_v080_signal(closeadj):
    b = _f04_ulcer(closeadj, 50)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery slope variants (facet 4b) --------------------
# vol-normalized recovery slope off 252d trough (risk-adjusted rebound velocity)
def f04dd_f04_deep_drawdown_recovery_recovslp21_252d_base_v081_signal(closeadj):
    slp = _f04_recov_slope(closeadj, 252, 21)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = slp / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery slope off 126d trough over the last month
def f04dd_f04_deep_drawdown_recovery_recovslp21_126d_base_v082_signal(closeadj):
    b = _f04_recov_slope(closeadj, 126, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery slope off 1260d trough over the last quarter (cycle-rebound speed)
def f04dd_f04_deep_drawdown_recovery_recovslp63_1260d_base_v083_signal(closeadj):
    b = _f04_recov_slope(closeadj, 1260, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of recovery off 252d trough (slope-of-slope, monthly)
def f04dd_f04_deep_drawdown_recovery_recovacc_252d_base_v084_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    slp = rec.diff(21) / 21.0
    b = slp.diff(21) / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown depth ranks / regime (facet 2b) --------------
# 504d current drawdown percentile-ranked vs its 1260d history
def f04dd_f04_deep_drawdown_recovery_curddrank_504d_base_v085_signal(closeadj):
    dd = _f04_drawdown(closeadj, 504)
    b = dd.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max drawdown percentile-ranked vs its 252d history
def f04dd_f04_deep_drawdown_recovery_maxddrank_63d_base_v086_signal(closeadj):
    md = _f04_maxdd(closeadj, 63)
    b = md.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 1260d current drawdown z-scored vs its own 504d history
def f04dd_f04_deep_drawdown_recovery_curddz_1260d_base_v087_signal(closeadj):
    dd = _f04_drawdown(closeadj, 1260)
    b = _z(dd, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt magnitude of current 252d drawdown (compressed deep-dd scale)
def f04dd_f04_deep_drawdown_recovery_ddsignmag_252d_base_v088_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    b = np.sign(dd) * (dd.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- underwater duration variants (facet 3b) ---------------
# fraction of last 126d spent >10% underwater
def f04dd_f04_deep_drawdown_recovery_uwfrac10_126d_base_v089_signal(closeadj):
    b = _f04_underwater_frac(closeadj, 126, -0.10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 1260d spent >25% underwater (chronic distress)
def f04dd_f04_deep_drawdown_recovery_uwfrac25_1260d_base_v090_signal(closeadj):
    b = _f04_underwater_frac(closeadj, 1260, -0.25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# near-wipeout pressure: fraction of 1260d >55% underwater, blended with the
# worst depth reached (graveyard tail-time, kept non-degenerate)
def f04dd_f04_deep_drawdown_recovery_uwfrac70_1260d_base_v091_signal(closeadj):
    frac = _f04_underwater_frac(closeadj, 1260, -0.55)
    worst = -_f04_maxdd(closeadj, 1260)
    b = frac + worst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest consecutive >50%-underwater streak over 1260d, normalized
def f04dd_f04_deep_drawdown_recovery_uwstreak50_1260d_base_v092_signal(closeadj):
    dd = _f04_drawdown(closeadj, 1260)
    deep = (dd <= -0.50)
    grp = (~deep).cumsum()
    run = deep.groupby(grp).cumsum()
    b = run.rolling(1260, min_periods=252).max() / 1260.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend in time-underwater: change over a quarter in >25%-underwater 504d fraction
def f04dd_f04_deep_drawdown_recovery_uwtrend_504d_base_v093_signal(closeadj):
    uw = _f04_underwater_frac(closeadj, 504, -0.25)
    b = uw - uw.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- days-since-peak / underwater spell (facet 17b) --------
# days since 126d peak (length of recent underwater spell)
def f04dd_f04_deep_drawdown_recovery_dsp_126d_base_v094_signal(closeadj):
    b = _f04_days_since_peak(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since 252d trough (length of current recovery phase)
def f04dd_f04_deep_drawdown_recovery_dst_252d_base_v095_signal(closeadj):
    b = _f04_days_since_trough(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since 1260d trough (maturity of the cycle rebound)
def f04dd_f04_deep_drawdown_recovery_dst_1260d_base_v096_signal(closeadj):
    b = _f04_days_since_trough(closeadj, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current consecutive underwater streak (>5% below 504d peak), normalized
def f04dd_f04_deep_drawdown_recovery_uwstreak_504d_base_v097_signal(closeadj):
    dd = _f04_drawdown(closeadj, 504)
    deep = (dd <= -0.05)
    grp = (~deep).cumsum()
    streak = deep.groupby(grp).cumsum()
    b = streak / 504.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain / ulcer dynamics (facet 7b) ----------------------
# ulcer index slope over a quarter (rising/falling pain regime, 252d)
def f04dd_f04_deep_drawdown_recovery_ulcerslp_252d_base_v098_signal(closeadj):
    ulcer = _f04_ulcer(closeadj, 252)
    b = ulcer.diff(63) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain index percentile-ranked vs 1260d history (504d window)
def f04dd_f04_deep_drawdown_recovery_painrank_504d_base_v099_signal(closeadj):
    pain = _f04_pain(closeadj, 504)
    b = pain.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ulcer 126d relative to ulcer 504d (short pain vs long pain term structure)
def f04dd_f04_deep_drawdown_recovery_ulcerterm_base_v100_signal(closeadj):
    s = _f04_ulcer(closeadj, 126)
    l = _f04_ulcer(closeadj, 504)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain index 126d minus its 252d mean (pain displacement)
def f04dd_f04_deep_drawdown_recovery_paindisp_126d_base_v101_signal(closeadj):
    pain = _f04_pain(closeadj, 126)
    b = pain - pain.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown frequency / episodes (facet 6b) --------------
# count of new >15% drawdown episodes over 252d, depth-weighted
def f04dd_f04_deep_drawdown_recovery_ddepi15_252d_base_v102_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    in_dd = (dd <= -0.15).astype(float)
    entries = ((in_dd == 1) & (in_dd.shift(1) == 0)).astype(float)
    cnt = entries.rolling(252, min_periods=126).sum()
    b = cnt + (-dd).rolling(63, min_periods=21).mean() * 8.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of new >30% drawdown episodes over 504d, depth-weighted
def f04dd_f04_deep_drawdown_recovery_ddepi30_504d_base_v103_signal(closeadj):
    dd = _f04_drawdown(closeadj, 504)
    in_dd = (dd <= -0.30).astype(float)
    entries = ((in_dd == 1) & (in_dd.shift(1) == 0)).astype(float)
    cnt = entries.rolling(504, min_periods=252).sum()
    b = cnt + (-dd).clip(lower=0.30).rolling(126, min_periods=63).mean() * 5.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 252d setting a fresh deeper drawdown (worsening regime)
def f04dd_f04_deep_drawdown_recovery_newddfrac_252d_base_v104_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    run_min = dd.rolling(63, min_periods=21).min()
    new_deep = (dd <= run_min * 0.99999).astype(float)
    freq = new_deep.rolling(252, min_periods=126).mean()
    b = freq + 0.25 * dd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- survival / trough multiple (facet 16b) ----------------
# log survival-from-trough multiple off 252d trough, smoothed
def f04dd_f04_deep_drawdown_recovery_survlog_252d_base_v105_signal(closeadj):
    trough = _rmin(closeadj, 252)
    lm = np.log(closeadj.replace(0, np.nan) / trough.replace(0, np.nan))
    b = lm.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survival multiple off 1260d trough z-scored vs its own 252d history
def f04dd_f04_deep_drawdown_recovery_survz_1260d_base_v106_signal(closeadj):
    trough = _rmin(closeadj, 1260)
    sm = closeadj / trough.replace(0, np.nan)
    b = _z(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how far above the 504d trough relative to how far below the 504d peak (bal)
def f04dd_f04_deep_drawdown_recovery_troughpeakbal_504d_base_v107_signal(closeadj):
    up = np.log(closeadj.replace(0, np.nan) / _rmin(closeadj, 504).replace(0, np.nan))
    down = np.log(_rmax(closeadj, 504).replace(0, np.nan) / closeadj.replace(0, np.nan))
    b = (up - down) / (up + down).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- interactions (facet 8b) -------------------------------
# deep 252d drawdown gated by long underwater duration (deep & chronic)
def f04dd_f04_deep_drawdown_recovery_deepchronic_252d_base_v108_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    uw = _f04_underwater_frac(closeadj, 252, -0.10)
    b = dd * uw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery slope x how deep the prior trough was (rebound strength from deep low)
def f04dd_f04_deep_drawdown_recovery_reboundpow_252d_base_v109_signal(closeadj):
    slp = _f04_recov_slope(closeadj, 252, 63)
    depth = -_f04_maxdd(closeadj, 252)
    b = slp * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Martin ratio over 504d: trailing 1y return per unit of 504d ulcer
def f04dd_f04_deep_drawdown_recovery_martin_504d_base_v110_signal(closeadj):
    ret = np.log(closeadj.replace(0, np.nan) / closeadj.shift(252).replace(0, np.nan))
    ulcer = _f04_ulcer(closeadj, 504)
    b = ret / ulcer.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current drawdown minus the typical drawdown depth (excess distress vs normal)
def f04dd_f04_deep_drawdown_recovery_ddexcess_252d_base_v111_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    typ = dd.rolling(504, min_periods=126).mean()
    b = dd - typ
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- velocity / momentum (facet 9b) ------------------------
# drawdown velocity over a week (acute deepening, 63d drawdown)
def f04dd_f04_deep_drawdown_recovery_ddvel5_63d_base_v112_signal(closeadj):
    dd = _f04_drawdown(closeadj, 63)
    b = dd - dd.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rebound-dominance regime: fraction of the last quarter on which recovery off
# the 252d trough exceeded the drawdown from the 252d peak (V-dominant days)
def f04dd_f04_deep_drawdown_recovery_recovmom21_252d_base_v113_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    dd = -_f04_drawdown(closeadj, 252)
    dom = (rec > dd).astype(float)
    b = dom.rolling(63, min_periods=21).mean() + 0.1 * (rec - dd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed recovery momentum (bounded rebound impulse)
def f04dd_f04_deep_drawdown_recovery_recovtanh_252d_base_v114_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    chg = rec - rec.shift(21)
    b = np.tanh(8.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown velocity year-over-year (504d drawdown vs a year ago)
def f04dd_f04_deep_drawdown_recovery_ddyoy_504d_base_v115_signal(closeadj):
    dd = _f04_drawdown(closeadj, 504)
    b = dd - dd.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- downside risk forms (facet 10b) -----------------------
# downside semideviation over 126d (acute downside engine)
def f04dd_f04_deep_drawdown_recovery_semidev_126d_base_v116_signal(closeadj):
    ret = closeadj.pct_change()
    neg = ret.clip(upper=0.0)
    b = np.sqrt((neg ** 2).rolling(126, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside/upside semideviation ratio over 252d (drawdown skew engine)
def f04dd_f04_deep_drawdown_recovery_semiskew_252d_base_v117_signal(closeadj):
    ret = closeadj.pct_change()
    down = np.sqrt((ret.clip(upper=0.0) ** 2).rolling(252, min_periods=126).mean())
    up = np.sqrt((ret.clip(lower=0.0) ** 2).rolling(252, min_periods=126).mean())
    b = down / up.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# avg of the worst 5% daily drops over 504d (deep-tail loss intensity)
def f04dd_f04_deep_drawdown_recovery_worstday_504d_base_v118_signal(closeadj):
    ret = closeadj.pct_change()

    def _f(a):
        k = max(1, int(len(a) * 0.05))
        return np.mean(np.sort(a)[:k])
    b = ret.rolling(504, min_periods=252).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# conditional drawdown at risk: mean depth of the worst 10% of 252d drawdowns
def f04dd_f04_deep_drawdown_recovery_cdar_252d_base_v119_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)

    def _f(a):
        k = max(1, int(len(a) * 0.10))
        return np.mean(np.sort(a)[:k])
    b = dd.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- dispersion / multi-window (facet 13b) -----------------
# recovery coefficient-of-variation across 63/252/504 windows (rebound
# consistency: low CV = uniform rebound, high CV = single-window spike)
def f04dd_f04_deep_drawdown_recovery_recovdisp_multi_base_v120_signal(closeadj):
    r1 = _f04_recovery(closeadj, 63)
    r2 = _f04_recovery(closeadj, 252)
    r3 = _f04_recovery(closeadj, 504)
    stacked = pd.concat([r1, r2, r3], axis=1)
    b = stacked.std(axis=1) / stacked.mean(axis=1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread of max drawdown across 50/126/252 windows (severity range)
def f04dd_f04_deep_drawdown_recovery_maxdddisp_multi_base_v121_signal(closeadj):
    d1 = _f04_maxdd(closeadj, 50)
    d2 = _f04_maxdd(closeadj, 126)
    d3 = _f04_maxdd(closeadj, 252)
    stacked = pd.concat([d1, d2, d3], axis=1)
    b = stacked.max(axis=1) - stacked.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- run-up vs drawdown asymmetry (facet 19) ---------------
# 252d max run-up minus |max drawdown| (boom-vs-bust amplitude asymmetry)
def f04dd_f04_deep_drawdown_recovery_runupasym_252d_base_v122_signal(closeadj):
    ru = _f04_max_run_up(closeadj, 252)
    dd = -_f04_maxdd(closeadj, 252)
    b = (ru - dd) / (ru + dd).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cyclical rebound ratio: 504d max run-up vs max drawdown, log-compressed and
# z-scored vs history (boom-amplitude relative to bust-amplitude regime)
def f04dd_f04_deep_drawdown_recovery_runupratio_504d_base_v123_signal(closeadj):
    ru = _f04_max_run_up(closeadj, 504)
    dd = -_f04_maxdd(closeadj, 504)
    ratio = np.log((1.0 + ru) / (1.0 + dd))
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- de-trended drawdown level (facet 2c) ------------------
# 504d current drawdown minus its slow EMA (drawdown displacement)
def f04dd_f04_deep_drawdown_recovery_dddisp_504d_base_v124_signal(closeadj):
    dd = _f04_drawdown(closeadj, 504)
    b = dd - dd.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max drawdown z-scored vs its own 252d history
def f04dd_f04_deep_drawdown_recovery_maxddz_126d_base_v125_signal(closeadj):
    md = _f04_maxdd(closeadj, 126)
    b = _z(md, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery quality / completeness (facet 5b) ------------
# 504d recovery-fraction displacement vs its slow EMA (rebound ahead-of-trend)
def f04dd_f04_deep_drawdown_recovery_recovfracrank_504d_base_v126_signal(closeadj):
    peak = _rmax(closeadj, 504)
    trough = _rmin(closeadj, 504)
    frac = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    b = frac - frac.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery efficiency: 252d recovery fraction per day elapsed since trough
def f04dd_f04_deep_drawdown_recovery_recoveff_252d_base_v127_signal(closeadj):
    peak = _rmax(closeadj, 252)
    trough = _rmin(closeadj, 252)
    frac = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    dst = _f04_days_since_trough(closeadj, 252).replace(0, np.nan)
    b = frac / dst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unrecovered fraction of the 1260d drawdown, percentile-ranked vs 504d history
# (how stuck-underwater the cycle position is vs its own recent norm)
def f04dd_f04_deep_drawdown_recovery_unrecfrac_1260d_base_v128_signal(closeadj):
    peak = _rmax(closeadj, 1260)
    trough = _rmin(closeadj, 1260)
    frac = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    unrec = 1.0 - frac
    b = unrec.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- composite distress/recovery (facet 18b) ---------------
# graveyard-distress: deep 1260d drawdown x fraction of time deeply underwater
def f04dd_f04_deep_drawdown_recovery_graveyard_1260d_base_v129_signal(closeadj):
    dd = _f04_maxdd(closeadj, 1260)
    uw = _f04_underwater_frac(closeadj, 1260, -0.50)
    b = dd.abs() * uw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# V-recovery sharpness: recovery off 504d trough per unit of time spent
# recovering (steep V-rebound vs slow grind back), bounded by log
def f04dd_f04_deep_drawdown_recovery_vquality_504d_base_v130_signal(closeadj):
    rec = np.log1p(_f04_recovery(closeadj, 504))
    dst = _f04_days_since_trough(closeadj, 504).replace(0, np.nan)
    b = rec / (dst ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distress trajectory: drawdown deepening velocity x current drawdown depth
def f04dd_f04_deep_drawdown_recovery_distrajn_252d_base_v131_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    vel = dd - dd.shift(21)
    b = vel * (-dd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- additional ranks / regime (facet 11b) -----------------
# is price in the bottom decile of its 504d range while underwater (deep regime)
def f04dd_f04_deep_drawdown_recovery_bottomdecile_504d_base_v132_signal(closeadj):
    peak = _rmax(closeadj, 504)
    trough = _rmin(closeadj, 504)
    pos = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    inbottom = (pos <= 0.10).astype(float)
    freq = inbottom.rolling(252, min_periods=126).mean()
    b = freq + 0.5 * (0.10 - pos).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 252d in a deep (>30%) drawdown state (distress-time tally)
def f04dd_f04_deep_drawdown_recovery_distresstime_252d_base_v133_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    deep = (dd <= -0.30).astype(float)
    b = deep.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain-adjusted recovery / efficiency (facet 14b) -------
# recovery slope per unit of ulcer (pain-efficient rebound, 504d)
def f04dd_f04_deep_drawdown_recovery_recovperulcer_504d_base_v134_signal(closeadj):
    slp = _f04_recov_slope(closeadj, 504, 63)
    ulcer = _f04_ulcer(closeadj, 504)
    b = slp / ulcer.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current drawdown depth per unit of pain (how extreme vs typical, 504d)
def f04dd_f04_deep_drawdown_recovery_ddperpain_504d_base_v135_signal(closeadj):
    dd = _f04_drawdown(closeadj, 504)
    pain = _f04_pain(closeadj, 504)
    b = dd / pain.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- multi-anchor drawdown (facet 13c) ---------------------
# anchor disagreement: dispersion of current drawdown across 63/252/504/1260
# anchors (acute-vs-cyclical drawdown spread — regime transition signal)
def f04dd_f04_deep_drawdown_recovery_worstanchor_base_v136_signal(closeadj):
    d1 = _f04_drawdown(closeadj, 63)
    d2 = _f04_drawdown(closeadj, 252)
    d3 = _f04_drawdown(closeadj, 504)
    d4 = _f04_drawdown(closeadj, 1260)
    b = pd.concat([d1, d2, d3, d4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery breadth z: how the cross-anchor average recovery sits vs its history
# (broad rebound across all trough horizons or just one), de-trended
def f04dd_f04_deep_drawdown_recovery_bestrecov_base_v137_signal(closeadj):
    r1 = _f04_recovery(closeadj, 63)
    r2 = _f04_recovery(closeadj, 252)
    r3 = _f04_recovery(closeadj, 504)
    avg = pd.concat([r1, r2, r3], axis=1).mean(axis=1)
    b = _z(avg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown shape / curvature (facet 20) -----------------
# drawdown convexity: squared upper/lower bias of 252d recovery fraction
def f04dd_f04_deep_drawdown_recovery_ddconvex_252d_base_v138_signal(closeadj):
    peak = _rmax(closeadj, 252)
    trough = _rmin(closeadj, 252)
    frac = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    b = np.sign(frac - 0.5) * (frac - 0.5) ** 2 * 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain trend acceleration: 252d pain quarterly-change minus prior quarter-change
def f04dd_f04_deep_drawdown_recovery_painacc_252d_base_v139_signal(closeadj):
    pain = _f04_pain(closeadj, 252)
    chg = pain - pain.shift(63)
    b = chg - chg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- smoothed / EMA forms (facet 21) -----------------------
# smoothed current 252d drawdown (persistent distress level)
def f04dd_f04_deep_drawdown_recovery_ddema_252d_base_v140_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    b = dd.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery impulse vs its own trend: smoothed recovery minus a slower EMA
# (is the rebound accelerating above its baseline?)
def f04dd_f04_deep_drawdown_recovery_recovema_252d_base_v141_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    b = rec.ewm(span=21, min_periods=10).mean() - rec.ewm(span=84, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- worst-case path (facet 22) ----------------------------
# worst peak-to-trough log loss inside 504d (deep bust magnitude, log scale)
def f04dd_f04_deep_drawdown_recovery_logmaxdd_504d_base_v142_signal(closeadj):
    def _f(a):
        run = np.maximum.accumulate(a)
        return np.min(np.log(a / run))
    b = closeadj.rolling(504, min_periods=252).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how recent the worst 504d drop was: time since the deepest drawdown day
def f04dd_f04_deep_drawdown_recovery_ddrecency_504d_base_v143_signal(closeadj):
    peak = _rmax(closeadj, 504)
    dd = closeadj / peak.replace(0, np.nan) - 1.0

    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    b = dd.rolling(504, min_periods=252).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery vs drawdown balance dynamics (facet 23) ------
# change over a quarter in the 252d recovery-minus-drawdown balance (V-shift)
def f04dd_f04_deep_drawdown_recovery_vshift_252d_base_v144_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    dd = _f04_drawdown(closeadj, 252).abs()
    bal = (rec - dd) / (rec + dd).replace(0, np.nan)
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain-vs-distance shape: 504d ulcer per unit of distance below the 1260d high
# (is the current deep drawdown choppy/painful or a clean one-way slide?)
def f04dd_f04_deep_drawdown_recovery_ulcerdist_1260d_base_v145_signal(closeadj):
    dist = (-_f04_drawdown(closeadj, 1260)).clip(lower=0.01)
    ulcer = _f04_ulcer(closeadj, 504)
    b = ulcer / dist
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- terminal facets (24) ----------------------------------
# drawdown term-structure ratio: acute (63d) drawdown as a share of the cyclical
# (504d) drawdown (is the recent dip already most of the cycle bust?)
def f04dd_f04_deep_drawdown_recovery_ddterm_63v504_base_v146_signal(closeadj):
    s = _f04_drawdown(closeadj, 63)
    l = _f04_drawdown(closeadj, 504)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery term structure: 63d recovery minus 504d recovery
def f04dd_f04_deep_drawdown_recovery_recovterm_63v504_base_v147_signal(closeadj):
    s = _f04_recovery(closeadj, 63)
    l = _f04_recovery(closeadj, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain term structure: 126d pain minus 504d pain (is pain concentrating recently)
def f04dd_f04_deep_drawdown_recovery_painterm_126v504_base_v148_signal(closeadj):
    s = _f04_pain(closeadj, 126)
    l = _f04_pain(closeadj, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trough-freshness: log gap between the 1260d trough and the 252d trough
# (is the recent low far above the cycle low? deep-cycle survival cushion)
def f04dd_f04_deep_drawdown_recovery_survterm_252v1260_base_v149_signal(closeadj):
    lo252 = _rmin(closeadj, 252)
    lo1260 = _rmin(closeadj, 1260)
    b = np.log(lo252.replace(0, np.nan) / lo1260.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deep-bust survival score: (1 - unrecovered fraction) gated by survival multiple
def f04dd_f04_deep_drawdown_recovery_survscore_504d_base_v150_signal(closeadj):
    peak = _rmax(closeadj, 504)
    trough = _rmin(closeadj, 504)
    frac = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    surv = np.log(closeadj.replace(0, np.nan) / trough.replace(0, np.nan))
    b = frac * surv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04dd_f04_deep_drawdown_recovery_curdd_50d_base_v076_signal,
    f04dd_f04_deep_drawdown_recovery_maxddz_50d_base_v077_signal,
    f04dd_f04_deep_drawdown_recovery_recov_50d_base_v078_signal,
    f04dd_f04_deep_drawdown_recovery_ddratio_50v252_base_v079_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_50d_base_v080_signal,
    f04dd_f04_deep_drawdown_recovery_recovslp21_252d_base_v081_signal,
    f04dd_f04_deep_drawdown_recovery_recovslp21_126d_base_v082_signal,
    f04dd_f04_deep_drawdown_recovery_recovslp63_1260d_base_v083_signal,
    f04dd_f04_deep_drawdown_recovery_recovacc_252d_base_v084_signal,
    f04dd_f04_deep_drawdown_recovery_curddrank_504d_base_v085_signal,
    f04dd_f04_deep_drawdown_recovery_maxddrank_63d_base_v086_signal,
    f04dd_f04_deep_drawdown_recovery_curddz_1260d_base_v087_signal,
    f04dd_f04_deep_drawdown_recovery_ddsignmag_252d_base_v088_signal,
    f04dd_f04_deep_drawdown_recovery_uwfrac10_126d_base_v089_signal,
    f04dd_f04_deep_drawdown_recovery_uwfrac25_1260d_base_v090_signal,
    f04dd_f04_deep_drawdown_recovery_uwfrac70_1260d_base_v091_signal,
    f04dd_f04_deep_drawdown_recovery_uwstreak50_1260d_base_v092_signal,
    f04dd_f04_deep_drawdown_recovery_uwtrend_504d_base_v093_signal,
    f04dd_f04_deep_drawdown_recovery_dsp_126d_base_v094_signal,
    f04dd_f04_deep_drawdown_recovery_dst_252d_base_v095_signal,
    f04dd_f04_deep_drawdown_recovery_dst_1260d_base_v096_signal,
    f04dd_f04_deep_drawdown_recovery_uwstreak_504d_base_v097_signal,
    f04dd_f04_deep_drawdown_recovery_ulcerslp_252d_base_v098_signal,
    f04dd_f04_deep_drawdown_recovery_painrank_504d_base_v099_signal,
    f04dd_f04_deep_drawdown_recovery_ulcerterm_base_v100_signal,
    f04dd_f04_deep_drawdown_recovery_paindisp_126d_base_v101_signal,
    f04dd_f04_deep_drawdown_recovery_ddepi15_252d_base_v102_signal,
    f04dd_f04_deep_drawdown_recovery_ddepi30_504d_base_v103_signal,
    f04dd_f04_deep_drawdown_recovery_newddfrac_252d_base_v104_signal,
    f04dd_f04_deep_drawdown_recovery_survlog_252d_base_v105_signal,
    f04dd_f04_deep_drawdown_recovery_survz_1260d_base_v106_signal,
    f04dd_f04_deep_drawdown_recovery_troughpeakbal_504d_base_v107_signal,
    f04dd_f04_deep_drawdown_recovery_deepchronic_252d_base_v108_signal,
    f04dd_f04_deep_drawdown_recovery_reboundpow_252d_base_v109_signal,
    f04dd_f04_deep_drawdown_recovery_martin_504d_base_v110_signal,
    f04dd_f04_deep_drawdown_recovery_ddexcess_252d_base_v111_signal,
    f04dd_f04_deep_drawdown_recovery_ddvel5_63d_base_v112_signal,
    f04dd_f04_deep_drawdown_recovery_recovmom21_252d_base_v113_signal,
    f04dd_f04_deep_drawdown_recovery_recovtanh_252d_base_v114_signal,
    f04dd_f04_deep_drawdown_recovery_ddyoy_504d_base_v115_signal,
    f04dd_f04_deep_drawdown_recovery_semidev_126d_base_v116_signal,
    f04dd_f04_deep_drawdown_recovery_semiskew_252d_base_v117_signal,
    f04dd_f04_deep_drawdown_recovery_worstday_504d_base_v118_signal,
    f04dd_f04_deep_drawdown_recovery_cdar_252d_base_v119_signal,
    f04dd_f04_deep_drawdown_recovery_recovdisp_multi_base_v120_signal,
    f04dd_f04_deep_drawdown_recovery_maxdddisp_multi_base_v121_signal,
    f04dd_f04_deep_drawdown_recovery_runupasym_252d_base_v122_signal,
    f04dd_f04_deep_drawdown_recovery_runupratio_504d_base_v123_signal,
    f04dd_f04_deep_drawdown_recovery_dddisp_504d_base_v124_signal,
    f04dd_f04_deep_drawdown_recovery_maxddz_126d_base_v125_signal,
    f04dd_f04_deep_drawdown_recovery_recovfracrank_504d_base_v126_signal,
    f04dd_f04_deep_drawdown_recovery_recoveff_252d_base_v127_signal,
    f04dd_f04_deep_drawdown_recovery_unrecfrac_1260d_base_v128_signal,
    f04dd_f04_deep_drawdown_recovery_graveyard_1260d_base_v129_signal,
    f04dd_f04_deep_drawdown_recovery_vquality_504d_base_v130_signal,
    f04dd_f04_deep_drawdown_recovery_distrajn_252d_base_v131_signal,
    f04dd_f04_deep_drawdown_recovery_bottomdecile_504d_base_v132_signal,
    f04dd_f04_deep_drawdown_recovery_distresstime_252d_base_v133_signal,
    f04dd_f04_deep_drawdown_recovery_recovperulcer_504d_base_v134_signal,
    f04dd_f04_deep_drawdown_recovery_ddperpain_504d_base_v135_signal,
    f04dd_f04_deep_drawdown_recovery_worstanchor_base_v136_signal,
    f04dd_f04_deep_drawdown_recovery_bestrecov_base_v137_signal,
    f04dd_f04_deep_drawdown_recovery_ddconvex_252d_base_v138_signal,
    f04dd_f04_deep_drawdown_recovery_painacc_252d_base_v139_signal,
    f04dd_f04_deep_drawdown_recovery_ddema_252d_base_v140_signal,
    f04dd_f04_deep_drawdown_recovery_recovema_252d_base_v141_signal,
    f04dd_f04_deep_drawdown_recovery_logmaxdd_504d_base_v142_signal,
    f04dd_f04_deep_drawdown_recovery_ddrecency_504d_base_v143_signal,
    f04dd_f04_deep_drawdown_recovery_vshift_252d_base_v144_signal,
    f04dd_f04_deep_drawdown_recovery_ulcerdist_1260d_base_v145_signal,
    f04dd_f04_deep_drawdown_recovery_ddterm_63v504_base_v146_signal,
    f04dd_f04_deep_drawdown_recovery_recovterm_63v504_base_v147_signal,
    f04dd_f04_deep_drawdown_recovery_painterm_126v504_base_v148_signal,
    f04dd_f04_deep_drawdown_recovery_survterm_252v1260_base_v149_signal,
    f04dd_f04_deep_drawdown_recovery_survscore_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_DEEP_DRAWDOWN_RECOVERY_REGISTRY_076_150 = REGISTRY


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

    print("OK f04_deep_drawdown_recovery_base_076_150_claude: %d features pass" % n_features)
