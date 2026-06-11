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
    # current drawdown from the rolling peak (<= 0)
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return close / peak.replace(0, np.nan) - 1.0


def _f04_maxdd(close, w):
    # deepest drawdown experienced inside the window (<= 0)
    def _f(a):
        run = np.maximum.accumulate(a)
        dd = a / run - 1.0
        return np.min(dd)
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f04_recovery(close, w):
    # recovery off the rolling trough (>= 0)
    trough = close.rolling(w, min_periods=max(1, w // 2)).min()
    return close / trough.replace(0, np.nan) - 1.0


def _f04_underwater_frac(close, w, thr):
    # fraction of window spent more than |thr| below the running peak
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    uw = close / peak.replace(0, np.nan) - 1.0
    deep = (uw <= thr).astype(float)
    return deep.rolling(w, min_periods=max(1, w // 2)).mean()


def _f04_ulcer(close, w):
    # ulcer index: RMS of percent drawdown from the running peak
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    dd = close / peak.replace(0, np.nan) - 1.0
    return np.sqrt((dd ** 2).rolling(w, min_periods=max(1, w // 2)).mean())


def _f04_pain(close, w):
    # pain index: average depth of drawdown (mean of |dd|)
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    dd = close / peak.replace(0, np.nan) - 1.0
    return (-dd).rolling(w, min_periods=max(1, w // 2)).mean()


def _f04_days_since_trough(close, w):
    # fraction of window since the trough (time spent recovering)
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f04_days_since_peak(close, w):
    # fraction of window since the peak (time underwater)
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f04_dd_episodes(close, w, thr):
    # count of new drawdown episodes crossing below thr inside the window
    dd = _f04_drawdown(close, w)
    in_dd = (dd <= thr).astype(float)
    entries = ((in_dd == 1) & (in_dd.shift(1) == 0)).astype(float)
    return entries.rolling(w, min_periods=max(1, w // 2)).sum()


def _f04_recov_slope(close, w, k):
    # slope of recovery off trough over the last k days
    rec = _f04_recovery(close, w)
    return rec.diff(k) / float(k)


# ============================================================
# ---- deep max drawdown, level (facet 1) --------------------
# deep max drawdown over 50d
def f04dd_f04_deep_drawdown_recovery_maxdd_50d_base_v001_signal(closeadj):
    b = _f04_maxdd(closeadj, 50)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deep max drawdown over 63d
def f04dd_f04_deep_drawdown_recovery_maxdd_63d_base_v002_signal(closeadj):
    b = _f04_maxdd(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deep max drawdown over 126d
def f04dd_f04_deep_drawdown_recovery_maxdd_126d_base_v003_signal(closeadj):
    b = _f04_maxdd(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deep max drawdown over 252d
def f04dd_f04_deep_drawdown_recovery_maxdd_252d_base_v004_signal(closeadj):
    b = _f04_maxdd(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deep max drawdown over 504d (cyclical bust depth)
def f04dd_f04_deep_drawdown_recovery_maxdd_504d_base_v005_signal(closeadj):
    b = _f04_maxdd(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 1260d max-drawdown depth blended with how far price sits above the cycle trough
def f04dd_f04_deep_drawdown_recovery_maxdd_1260d_base_v006_signal(closeadj):
    md = _f04_maxdd(closeadj, 1260)
    trough = _rmin(closeadj, 1260)
    above = np.log(closeadj.replace(0, np.nan) / trough.replace(0, np.nan))
    b = md + 0.25 * above
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- current drawdown from peak, level (facet 1b) ----------
# current drawdown from 63d peak
def f04dd_f04_deep_drawdown_recovery_curdd_63d_base_v007_signal(closeadj):
    b = _f04_drawdown(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current drawdown from 252d peak
def f04dd_f04_deep_drawdown_recovery_curdd_252d_base_v008_signal(closeadj):
    b = _f04_drawdown(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current drawdown from 504d peak
def f04dd_f04_deep_drawdown_recovery_curdd_504d_base_v009_signal(closeadj):
    b = _f04_drawdown(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance below the cycle (1260d) high in log-return units, lagged-peak memory
def f04dd_f04_deep_drawdown_recovery_curdd_1260d_base_v010_signal(closeadj):
    peak_lag = _rmax(closeadj, 1260).shift(63)
    b = np.log(closeadj.replace(0, np.nan) / peak_lag.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown z-scored / ranked (facet 2: de-trended level) ----
# 252d current drawdown z-scored vs its own 252d history
def f04dd_f04_deep_drawdown_recovery_curddz_252d_base_v011_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    b = _z(dd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max drawdown z-scored vs its own 252d history
def f04dd_f04_deep_drawdown_recovery_maxddz_504d_base_v012_signal(closeadj):
    md = _f04_maxdd(closeadj, 504)
    b = _z(md, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d current drawdown percentile-ranked vs its 504d history
def f04dd_f04_deep_drawdown_recovery_curddrank_252d_base_v013_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    b = dd.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max drawdown percentile-ranked vs its 252d history
def f04dd_f04_deep_drawdown_recovery_maxddrank_126d_base_v014_signal(closeadj):
    md = _f04_maxdd(closeadj, 126)
    b = md.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- underwater duration (facet 3) -------------------------
# fraction of last 252d spent >10% underwater
def f04dd_f04_deep_drawdown_recovery_uwfrac10_252d_base_v015_signal(closeadj):
    b = _f04_underwater_frac(closeadj, 252, -0.10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest consecutive deep-underwater (>25% below 252d peak) streak, normalized
# (duration of the worst uninterrupted distress spell, not just total time)
def f04dd_f04_deep_drawdown_recovery_uwfrac25_252d_base_v016_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    deep = (dd <= -0.25)
    grp = (~deep).cumsum()
    run = deep.groupby(grp).cumsum()
    b = run.rolling(252, min_periods=126).max() / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-underwater asymmetry (504d): excess of >40%-deep time over >10%-shallow
# time, i.e. how skewed the underwater spell is toward deep distress
def f04dd_f04_deep_drawdown_recovery_uwfrac25_504d_base_v017_signal(closeadj):
    deep = _f04_underwater_frac(closeadj, 504, -0.40)
    shallow = _f04_underwater_frac(closeadj, 504, -0.10)
    b = deep / shallow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 504d spent >50% underwater (graveyard depth)
def f04dd_f04_deep_drawdown_recovery_uwfrac50_504d_base_v018_signal(closeadj):
    b = _f04_underwater_frac(closeadj, 504, -0.50)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 1260d spent >50% underwater
def f04dd_f04_deep_drawdown_recovery_uwfrac50_1260d_base_v019_signal(closeadj):
    b = _f04_underwater_frac(closeadj, 1260, -0.50)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since 252d peak (length of current underwater spell)
def f04dd_f04_deep_drawdown_recovery_dsp_252d_base_v020_signal(closeadj):
    b = _f04_days_since_peak(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since 504d peak
def f04dd_f04_deep_drawdown_recovery_dsp_504d_base_v021_signal(closeadj):
    b = _f04_days_since_peak(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cycle-high staleness spread: days since the 1260d peak minus days since the
# 504d peak (is the multi-year high far older than the recent high?)
def f04dd_f04_deep_drawdown_recovery_dsp_1260d_base_v022_signal(closeadj):
    long_age = _f04_days_since_peak(closeadj, 1260) * 1260.0
    short_age = _f04_days_since_peak(closeadj, 504) * 504.0
    b = np.log1p(long_age) - np.log1p(short_age)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery off trough (facet 4) -------------------------
# recovery off 252d trough
def f04dd_f04_deep_drawdown_recovery_recov_252d_base_v023_signal(closeadj):
    b = _f04_recovery(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery off 504d trough
def f04dd_f04_deep_drawdown_recovery_recov_504d_base_v024_signal(closeadj):
    b = _f04_recovery(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery off 1260d trough (rebound from cycle low)
def f04dd_f04_deep_drawdown_recovery_recov_1260d_base_v025_signal(closeadj):
    b = _f04_recovery(closeadj, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery slope off 252d trough over the last quarter (rebound velocity)
def f04dd_f04_deep_drawdown_recovery_recovslp_252d_base_v026_signal(closeadj):
    b = _f04_recov_slope(closeadj, 252, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery slope off 504d trough over the last quarter
def f04dd_f04_deep_drawdown_recovery_recovslp_504d_base_v027_signal(closeadj):
    b = _f04_recov_slope(closeadj, 504, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery rate off trough: recovery scaled by elapsed time since trough
def f04dd_f04_deep_drawdown_recovery_recovrate_252d_base_v028_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    dst = _f04_days_since_trough(closeadj, 252).replace(0, np.nan)
    b = rec / dst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery rate off 504d trough scaled by elapsed time
def f04dd_f04_deep_drawdown_recovery_recovrate_504d_base_v029_signal(closeadj):
    rec = _f04_recovery(closeadj, 504)
    dst = _f04_days_since_trough(closeadj, 504).replace(0, np.nan)
    b = rec / dst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- time-to-recover / recovery fraction (facet 5) ---------
# survival-from-trough multiple (504d) z-scored vs its own 252d history
def f04dd_f04_deep_drawdown_recovery_survmult_504d_base_v030_signal(closeadj):
    trough = _rmin(closeadj, 504)
    sm = closeadj / trough.replace(0, np.nan)
    b = _z(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full-cycle (1260d) survival multiple percentile-ranked vs its 504d history
def f04dd_f04_deep_drawdown_recovery_survmult_1260d_base_v031_signal(closeadj):
    trough = _rmin(closeadj, 1260)
    sm = closeadj / trough.replace(0, np.nan)
    b = sm.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery fraction of the 252d drawdown, z-scored vs its own 252d history
def f04dd_f04_deep_drawdown_recovery_recovfrac_252d_base_v032_signal(closeadj):
    peak = _rmax(closeadj, 252)
    trough = _rmin(closeadj, 252)
    frac = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    b = _z(frac, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery-fraction displacement: 504d recovery fraction minus its slow EMA
# (is the rebound running ahead of or behind its own trend?)
def f04dd_f04_deep_drawdown_recovery_recovfrac_504d_base_v033_signal(closeadj):
    peak = _rmax(closeadj, 504)
    trough = _rmin(closeadj, 504)
    frac = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    b = frac - frac.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-to-recover proxy: days since trough relative to days since peak
def f04dd_f04_deep_drawdown_recovery_ttr_252d_base_v034_signal(closeadj):
    dst = _f04_days_since_trough(closeadj, 252)
    dsp = _f04_days_since_peak(closeadj, 252)
    b = (dst - dsp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# estimated time-to-recover: remaining climb to the 504d peak divided by the
# recent recovery slope (how many quarters of rebound still needed)
def f04dd_f04_deep_drawdown_recovery_unrec_504d_base_v035_signal(closeadj):
    peak = _rmax(closeadj, 504)
    gap = np.log(peak.replace(0, np.nan) / closeadj.replace(0, np.nan))
    slope = (np.log(closeadj.replace(0, np.nan)) -
             np.log(closeadj.shift(63).replace(0, np.nan))) / 63.0
    b = gap / slope.where(slope > 0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown frequency / episodes (facet 6) ---------------
# >10% drawdown-episode count over 252d, depth-weighted (magnitude-continuous)
def f04dd_f04_deep_drawdown_recovery_ddepi10_252d_base_v036_signal(closeadj):
    cnt = _f04_dd_episodes(closeadj, 252, -0.10)
    dd = _f04_drawdown(closeadj, 252)
    b = cnt + (-dd).rolling(63, min_periods=21).mean() * 10.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# >25% drawdown-episode count over 252d, depth-weighted
def f04dd_f04_deep_drawdown_recovery_ddepi25_252d_base_v037_signal(closeadj):
    cnt = _f04_dd_episodes(closeadj, 252, -0.25)
    dd = _f04_drawdown(closeadj, 252)
    b = cnt + (-dd).clip(lower=0.25).rolling(63, min_periods=21).mean() * 5.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# >25% drawdown-episode count over 504d, depth-weighted
def f04dd_f04_deep_drawdown_recovery_ddepi25_504d_base_v038_signal(closeadj):
    cnt = _f04_dd_episodes(closeadj, 504, -0.25)
    dd = _f04_drawdown(closeadj, 504)
    b = cnt + (-dd).rolling(126, min_periods=63).mean() * 8.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# >40% drawdown-episode count over 504d (deep busts), depth-weighted
def f04dd_f04_deep_drawdown_recovery_ddepi40_504d_base_v039_signal(closeadj):
    cnt = _f04_dd_episodes(closeadj, 504, -0.40)
    dd = _f04_drawdown(closeadj, 504)
    b = cnt + (-dd).clip(lower=0.40).rolling(126, min_periods=63).mean() * 6.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain / ulcer index (facet 7) --------------------------
# ulcer index over 252d (RMS drawdown depth — canonical pain level)
def f04dd_f04_deep_drawdown_recovery_ulcer_252d_base_v040_signal(closeadj):
    b = _f04_ulcer(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ulcer index over 504d, z-scored vs its own 252d history (de-trended pain regime)
def f04dd_f04_deep_drawdown_recovery_ulcer_504d_base_v041_signal(closeadj):
    ulcer = _f04_ulcer(closeadj, 504)
    b = _z(ulcer, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ulcer index over 1260d (full-cycle pain), shorter warm-up
def f04dd_f04_deep_drawdown_recovery_ulcer_1260d_base_v042_signal(closeadj):
    peak = closeadj.rolling(1260, min_periods=252).max()
    dd = closeadj / peak.replace(0, np.nan) - 1.0
    b = np.sqrt((dd ** 2).rolling(1260, min_periods=252).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown distribution shape: ulcer (RMS) over pain (mean) — tail-heaviness of dd
def f04dd_f04_deep_drawdown_recovery_pain_252d_base_v043_signal(closeadj):
    ulcer = _f04_ulcer(closeadj, 252)
    pain = _f04_pain(closeadj, 252)
    b = ulcer / pain.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain-index displacement: 504d pain minus its own slow EMA (rising/falling pain)
def f04dd_f04_deep_drawdown_recovery_pain_504d_base_v044_signal(closeadj):
    pain = _f04_pain(closeadj, 504)
    b = pain - pain.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- interactions / spreads / ratios (facet 8) -------------
# drawdown asymmetry: 63d drawdown relative to the deeper 252d drawdown
def f04dd_f04_deep_drawdown_recovery_ddratio_63v252_base_v045_signal(closeadj):
    s = _f04_drawdown(closeadj, 63)
    l = _f04_drawdown(closeadj, 252)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery-completeness spread: how much more of the short (252d) drawdown has
# been clawed back than the long (504d) drawdown (V-shape vs grind-back)
def f04dd_f04_deep_drawdown_recovery_maxddspr_252v1260_base_v046_signal(closeadj):
    p1 = _rmax(closeadj, 252)
    t1 = _rmin(closeadj, 252)
    f1 = (closeadj - t1) / (p1 - t1).replace(0, np.nan)
    p2 = _rmax(closeadj, 504)
    t2 = _rmin(closeadj, 504)
    f2 = (closeadj - t2) / (p2 - t2).replace(0, np.nan)
    b = f1 - f2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery-minus-drawdown balance (V-shape) over 252d
def f04dd_f04_deep_drawdown_recovery_vbal_252d_base_v047_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    dd = _f04_drawdown(closeadj, 252).abs()
    b = (rec - dd) / (rec + dd).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Martin-ratio-like: 252d trailing return per unit of ulcer (pain-adjusted)
def f04dd_f04_deep_drawdown_recovery_martin_252d_base_v048_signal(closeadj):
    ret = np.log(closeadj.replace(0, np.nan) / closeadj.shift(252).replace(0, np.nan))
    ulcer = _f04_ulcer(closeadj, 252)
    b = ret / ulcer.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown depth x time underwater (deep & long stress)
def f04dd_f04_deep_drawdown_recovery_ddxuw_252d_base_v049_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    dsp = _f04_days_since_peak(closeadj, 252)
    b = dd * dsp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery depth x time recovering (matured rebound)
def f04dd_f04_deep_drawdown_recovery_recxtime_252d_base_v050_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    dst = _f04_days_since_trough(closeadj, 252)
    b = rec * dst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown velocity / momentum (facet 9) ----------------
# drawdown velocity: change in 252d drawdown over a month
def f04dd_f04_deep_drawdown_recovery_ddvel_252d_base_v051_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    b = dd - dd.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown velocity over a quarter (504d drawdown)
def f04dd_f04_deep_drawdown_recovery_ddvel_504d_base_v052_signal(closeadj):
    dd = _f04_drawdown(closeadj, 504)
    b = dd - dd.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery acceleration: how the 504d-recovery quarterly change is itself changing
def f04dd_f04_deep_drawdown_recovery_recovmom_504d_base_v053_signal(closeadj):
    rec = _f04_recovery(closeadj, 504)
    chg = rec - rec.shift(63)
    b = chg - chg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown year-over-year: 252d drawdown vs the drawdown a year ago
def f04dd_f04_deep_drawdown_recovery_ddyoy_252d_base_v054_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    b = dd - dd.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- vol-adjusted / risk-scaled drawdown (facet 10) --------
# drawdown-vs-vol divergence: how much deeper the 252d drawdown is than the
# typical daily move would explain (drawdown z minus a 63d vol z) — stress gap
def f04dd_f04_deep_drawdown_recovery_ddvoladj_252d_base_v055_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = _z(-dd, 252) - _z(vol, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-adjusted rebound off trough, percentile-ranked vs its own 252d history
def f04dd_f04_deep_drawdown_recovery_recvoladj_252d_base_v056_signal(closeadj):
    rec = _f04_recovery(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    ratio = rec / vol.replace(0, np.nan)
    b = ratio.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- conditional / regime forms (facet 11) -----------------
# average of the 5 worst single-day drops over 252d (tail-loss intensity)
def f04dd_f04_deep_drawdown_recovery_worstday_252d_base_v057_signal(closeadj):
    ret = closeadj.pct_change()

    def _f(a):
        k = max(1, int(len(a) * 0.02))
        return np.mean(np.sort(a)[:k])
    b = ret.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside semideviation over 252d (downside risk fueling drawdowns)
def f04dd_f04_deep_drawdown_recovery_semidev_252d_base_v058_signal(closeadj):
    ret = closeadj.pct_change()
    neg = ret.clip(upper=0.0)
    b = np.sqrt((neg ** 2).rolling(252, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed drawdown velocity (bounded deepening signal)
def f04dd_f04_deep_drawdown_recovery_ddveltanh_252d_base_v059_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    chg = dd - dd.shift(21)
    b = np.tanh(15.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt magnitude of 504d drawdown (compressed deep-dd scale)
def f04dd_f04_deep_drawdown_recovery_ddsignmag_504d_base_v060_signal(closeadj):
    dd = _f04_drawdown(closeadj, 504)
    b = np.sign(dd) * (dd.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown persistence / streaks (facet 12) -------------
# current consecutive-days-underwater streak (>5% below 252d peak), normalized
def f04dd_f04_deep_drawdown_recovery_uwstreak_252d_base_v061_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    deep = (dd <= -0.05)
    grp = (~deep).cumsum()
    streak = deep.groupby(grp).cumsum()
    b = streak / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 252d making lower-lows (downtrend pressure inside drawdown)
def f04dd_f04_deep_drawdown_recovery_lowerlow_252d_base_v062_signal(closeadj):
    roll_min = closeadj.rolling(21, min_periods=10).min()
    new_low = (closeadj <= roll_min * 1.00001).astype(float)
    b = new_low.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- multi-window dispersion (facet 13) --------------------
# dispersion of drawdown across 63/252/504 windows (regime disagreement)
def f04dd_f04_deep_drawdown_recovery_dddisp_multi_base_v063_signal(closeadj):
    d1 = _f04_drawdown(closeadj, 63)
    d2 = _f04_drawdown(closeadj, 252)
    d3 = _f04_drawdown(closeadj, 504)
    b = pd.concat([d1, d2, d3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deepest minus shallowest drawdown across windows (range of dd severity)
def f04dd_f04_deep_drawdown_recovery_ddspread_multi_base_v064_signal(closeadj):
    d1 = _f04_drawdown(closeadj, 252)
    d2 = _f04_drawdown(closeadj, 504)
    d3 = _f04_drawdown(closeadj, 1260)
    stacked = pd.concat([d1, d2, d3], axis=1)
    b = stacked.max(axis=1) - stacked.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- additional pain/recovery quality (facet 14) -----------
# ulcer-normalized current drawdown (how deep relative to typical pain)
def f04dd_f04_deep_drawdown_recovery_ddpernpain_252d_base_v065_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    ulcer = _f04_ulcer(closeadj, 252)
    b = dd / ulcer.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery slope off trough per unit of pain index (efficient rebound)
def f04dd_f04_deep_drawdown_recovery_recovperpain_252d_base_v066_signal(closeadj):
    slp = _f04_recov_slope(closeadj, 252, 63)
    pain = _f04_pain(closeadj, 252)
    b = slp / pain.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain concentration: deepest 504d drawdown relative to its average pain
# (one big bust vs many shallow dips)
def f04dd_f04_deep_drawdown_recovery_meandepth_504d_base_v067_signal(closeadj):
    md = _f04_maxdd(closeadj, 504)
    pain = _f04_pain(closeadj, 504)
    b = md.abs() / pain.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- de-trended pain/ulcer (facet 15) ----------------------
# ulcer index z-scored vs its own 252d history
def f04dd_f04_deep_drawdown_recovery_ulcerz_252d_base_v068_signal(closeadj):
    ulcer = _f04_ulcer(closeadj, 252)
    b = _z(ulcer, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain index percentile-ranked vs its 504d history
def f04dd_f04_deep_drawdown_recovery_painrank_252d_base_v069_signal(closeadj):
    pain = _f04_pain(closeadj, 252)
    b = pain.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- survival multiple dynamics (facet 16) -----------------
# log survival-from-trough multiple (504d) smoothed
def f04dd_f04_deep_drawdown_recovery_survlog_504d_base_v070_signal(closeadj):
    trough = _rmin(closeadj, 504)
    lm = np.log(closeadj.replace(0, np.nan) / trough.replace(0, np.nan))
    b = lm.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# annualized recovery rate: log survival multiple per year since the 504d trough
def f04dd_f04_deep_drawdown_recovery_survmom_504d_base_v071_signal(closeadj):
    trough = _rmin(closeadj, 504)
    lsm = np.log(closeadj.replace(0, np.nan) / trough.replace(0, np.nan))
    dst = _f04_days_since_trough(closeadj, 504).replace(0, np.nan)
    b = lsm / (dst * 504.0 / 252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- underwater intensity (facet 17) -----------------------
# underwater-depth extremity: current drawdown z-scored within its own 126d band
# (how unusual today's depth is vs the recent drawdown distribution)
def f04dd_f04_deep_drawdown_recovery_uwdepth_252d_base_v072_signal(closeadj):
    dd = _f04_drawdown(closeadj, 252)
    b = _z(dd, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-trough frequency: how often a fresh 252d low is set in last quarter
def f04dd_f04_deep_drawdown_recovery_newtrofreq_252d_base_v073_signal(closeadj):
    lo = closeadj.rolling(252, min_periods=126).min()
    is_low = (closeadj <= lo * 1.00001).astype(float)
    freq = is_low.rolling(63, min_periods=21).mean()
    dd = _f04_drawdown(closeadj, 252)
    b = freq + 0.25 * dd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- composite distress/recovery (facet 18) ----------------
# deep-dd survival signature: deep drawdown gated by survival multiple
def f04dd_f04_deep_drawdown_recovery_ddsurv_504d_base_v074_signal(closeadj):
    dd = _f04_maxdd(closeadj, 504)
    trough = _rmin(closeadj, 504)
    surv = closeadj / trough.replace(0, np.nan) - 1.0
    b = dd.abs() * surv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery completeness vs time: recovery fraction minus elapsed-time fraction
def f04dd_f04_deep_drawdown_recovery_recovgap_252d_base_v075_signal(closeadj):
    peak = _rmax(closeadj, 252)
    trough = _rmin(closeadj, 252)
    frac = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    dst = _f04_days_since_trough(closeadj, 252)
    b = frac - dst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04dd_f04_deep_drawdown_recovery_maxdd_50d_base_v001_signal,
    f04dd_f04_deep_drawdown_recovery_maxdd_63d_base_v002_signal,
    f04dd_f04_deep_drawdown_recovery_maxdd_126d_base_v003_signal,
    f04dd_f04_deep_drawdown_recovery_maxdd_252d_base_v004_signal,
    f04dd_f04_deep_drawdown_recovery_maxdd_504d_base_v005_signal,
    f04dd_f04_deep_drawdown_recovery_maxdd_1260d_base_v006_signal,
    f04dd_f04_deep_drawdown_recovery_curdd_63d_base_v007_signal,
    f04dd_f04_deep_drawdown_recovery_curdd_252d_base_v008_signal,
    f04dd_f04_deep_drawdown_recovery_curdd_504d_base_v009_signal,
    f04dd_f04_deep_drawdown_recovery_curdd_1260d_base_v010_signal,
    f04dd_f04_deep_drawdown_recovery_curddz_252d_base_v011_signal,
    f04dd_f04_deep_drawdown_recovery_maxddz_504d_base_v012_signal,
    f04dd_f04_deep_drawdown_recovery_curddrank_252d_base_v013_signal,
    f04dd_f04_deep_drawdown_recovery_maxddrank_126d_base_v014_signal,
    f04dd_f04_deep_drawdown_recovery_uwfrac10_252d_base_v015_signal,
    f04dd_f04_deep_drawdown_recovery_uwfrac25_252d_base_v016_signal,
    f04dd_f04_deep_drawdown_recovery_uwfrac25_504d_base_v017_signal,
    f04dd_f04_deep_drawdown_recovery_uwfrac50_504d_base_v018_signal,
    f04dd_f04_deep_drawdown_recovery_uwfrac50_1260d_base_v019_signal,
    f04dd_f04_deep_drawdown_recovery_dsp_252d_base_v020_signal,
    f04dd_f04_deep_drawdown_recovery_dsp_504d_base_v021_signal,
    f04dd_f04_deep_drawdown_recovery_dsp_1260d_base_v022_signal,
    f04dd_f04_deep_drawdown_recovery_recov_252d_base_v023_signal,
    f04dd_f04_deep_drawdown_recovery_recov_504d_base_v024_signal,
    f04dd_f04_deep_drawdown_recovery_recov_1260d_base_v025_signal,
    f04dd_f04_deep_drawdown_recovery_recovslp_252d_base_v026_signal,
    f04dd_f04_deep_drawdown_recovery_recovslp_504d_base_v027_signal,
    f04dd_f04_deep_drawdown_recovery_recovrate_252d_base_v028_signal,
    f04dd_f04_deep_drawdown_recovery_recovrate_504d_base_v029_signal,
    f04dd_f04_deep_drawdown_recovery_survmult_504d_base_v030_signal,
    f04dd_f04_deep_drawdown_recovery_survmult_1260d_base_v031_signal,
    f04dd_f04_deep_drawdown_recovery_recovfrac_252d_base_v032_signal,
    f04dd_f04_deep_drawdown_recovery_recovfrac_504d_base_v033_signal,
    f04dd_f04_deep_drawdown_recovery_ttr_252d_base_v034_signal,
    f04dd_f04_deep_drawdown_recovery_unrec_504d_base_v035_signal,
    f04dd_f04_deep_drawdown_recovery_ddepi10_252d_base_v036_signal,
    f04dd_f04_deep_drawdown_recovery_ddepi25_252d_base_v037_signal,
    f04dd_f04_deep_drawdown_recovery_ddepi25_504d_base_v038_signal,
    f04dd_f04_deep_drawdown_recovery_ddepi40_504d_base_v039_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_252d_base_v040_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_504d_base_v041_signal,
    f04dd_f04_deep_drawdown_recovery_ulcer_1260d_base_v042_signal,
    f04dd_f04_deep_drawdown_recovery_pain_252d_base_v043_signal,
    f04dd_f04_deep_drawdown_recovery_pain_504d_base_v044_signal,
    f04dd_f04_deep_drawdown_recovery_ddratio_63v252_base_v045_signal,
    f04dd_f04_deep_drawdown_recovery_maxddspr_252v1260_base_v046_signal,
    f04dd_f04_deep_drawdown_recovery_vbal_252d_base_v047_signal,
    f04dd_f04_deep_drawdown_recovery_martin_252d_base_v048_signal,
    f04dd_f04_deep_drawdown_recovery_ddxuw_252d_base_v049_signal,
    f04dd_f04_deep_drawdown_recovery_recxtime_252d_base_v050_signal,
    f04dd_f04_deep_drawdown_recovery_ddvel_252d_base_v051_signal,
    f04dd_f04_deep_drawdown_recovery_ddvel_504d_base_v052_signal,
    f04dd_f04_deep_drawdown_recovery_recovmom_504d_base_v053_signal,
    f04dd_f04_deep_drawdown_recovery_ddyoy_252d_base_v054_signal,
    f04dd_f04_deep_drawdown_recovery_ddvoladj_252d_base_v055_signal,
    f04dd_f04_deep_drawdown_recovery_recvoladj_252d_base_v056_signal,
    f04dd_f04_deep_drawdown_recovery_worstday_252d_base_v057_signal,
    f04dd_f04_deep_drawdown_recovery_semidev_252d_base_v058_signal,
    f04dd_f04_deep_drawdown_recovery_ddveltanh_252d_base_v059_signal,
    f04dd_f04_deep_drawdown_recovery_ddsignmag_504d_base_v060_signal,
    f04dd_f04_deep_drawdown_recovery_uwstreak_252d_base_v061_signal,
    f04dd_f04_deep_drawdown_recovery_lowerlow_252d_base_v062_signal,
    f04dd_f04_deep_drawdown_recovery_dddisp_multi_base_v063_signal,
    f04dd_f04_deep_drawdown_recovery_ddspread_multi_base_v064_signal,
    f04dd_f04_deep_drawdown_recovery_ddpernpain_252d_base_v065_signal,
    f04dd_f04_deep_drawdown_recovery_recovperpain_252d_base_v066_signal,
    f04dd_f04_deep_drawdown_recovery_meandepth_504d_base_v067_signal,
    f04dd_f04_deep_drawdown_recovery_ulcerz_252d_base_v068_signal,
    f04dd_f04_deep_drawdown_recovery_painrank_252d_base_v069_signal,
    f04dd_f04_deep_drawdown_recovery_survlog_504d_base_v070_signal,
    f04dd_f04_deep_drawdown_recovery_survmom_504d_base_v071_signal,
    f04dd_f04_deep_drawdown_recovery_uwdepth_252d_base_v072_signal,
    f04dd_f04_deep_drawdown_recovery_newtrofreq_252d_base_v073_signal,
    f04dd_f04_deep_drawdown_recovery_ddsurv_504d_base_v074_signal,
    f04dd_f04_deep_drawdown_recovery_recovgap_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_DEEP_DRAWDOWN_RECOVERY_REGISTRY_001_075 = REGISTRY


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

    print("OK f04_deep_drawdown_recovery_base_001_075_claude: %d features pass" % n_features)
