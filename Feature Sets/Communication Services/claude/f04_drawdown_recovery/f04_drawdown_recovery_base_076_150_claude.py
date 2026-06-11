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


# ===== folder domain primitives (drawdown & recovery) =====
def _f04_drawdown(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return close / peak.replace(0, np.nan) - 1.0


def _f04_maxdd(close, w):
    uw = _f04_drawdown(close, w)
    return uw.rolling(w, min_periods=max(1, w // 2)).min()


def _f04_recovery_off_trough(close, w):
    trough = close.rolling(w, min_periods=max(1, w // 2)).min()
    return close / trough.replace(0, np.nan) - 1.0


def _f04_pain_index(close, w):
    uw = _f04_drawdown(close, w)
    return (-uw).rolling(w, min_periods=max(1, w // 2)).mean()


def _f04_ulcer(close, w):
    uw = _f04_drawdown(close, w)
    return np.sqrt((uw ** 2).rolling(w, min_periods=max(1, w // 2)).mean())


def _f04_days_since_peak(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f04_days_since_trough(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f04_ret(close):
    return close.pct_change()


def _f04_run_length_under(close, w, thr):
    uw = _f04_drawdown(close, w)
    under = (uw <= thr).astype(float)
    grp = (under == 0).cumsum()
    return under.groupby(grp).cumsum()


# ============================================================
# ---- max drawdown z-scored vs own history (extremity of worst loss) ----
def f04dr_f04_drawdown_recovery_maxddz_252d_base_v076_signal(closeadj):
    mdd = _f04_maxdd(closeadj, 252)
    b = _z(mdd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_maxddz_504d_base_v077_signal(closeadj):
    mdd = _f04_maxdd(closeadj, 504)
    b = _z(mdd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- max drawdown percentile rank vs own history ----
def f04dr_f04_drawdown_recovery_maxddrank_252d_base_v078_signal(closeadj):
    mdd = _f04_maxdd(closeadj, 252)
    b = mdd.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- change in max drawdown over a quarter (is the worst loss getting worse?) ----
def f04dr_f04_drawdown_recovery_maxddmom_252d_base_v079_signal(closeadj):
    mdd = _f04_maxdd(closeadj, 252)
    b = mdd - mdd.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- short-window max drawdown momentum ----
def f04dr_f04_drawdown_recovery_maxddmom_63d_base_v080_signal(closeadj):
    mdd = _f04_maxdd(closeadj, 63)
    b = mdd - mdd.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery slope per ulcer (rebound quality per unit of historical pain) ----
def f04dr_f04_drawdown_recovery_recovperulcer_252d_base_v081_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 252)
    ulcer = _f04_ulcer(closeadj, 252).replace(0, np.nan)
    b = rec / ulcer
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery slope per pain (alternate normalization) ----
def f04dr_f04_drawdown_recovery_recovperpain_504d_base_v082_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 504)
    pain = _f04_pain_index(closeadj, 504).replace(0, np.nan)
    b = rec / pain
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- skew of the underwater distribution (is most of the time mildly or deeply down?) ----
def f04dr_f04_drawdown_recovery_uwskew_252d_base_v083_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    b = uw.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- dispersion of the underwater series (volatility of the drawdown itself) ----
def f04dr_f04_drawdown_recovery_uwstd_252d_base_v084_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    b = uw.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwstd_63d_base_v085_signal(closeadj):
    uw = _f04_drawdown(closeadj, 63)
    b = uw.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery-to-peak gap: how far the current price still is from full recovery ----
def f04dr_f04_drawdown_recovery_recovgap_252d_base_v086_signal(closeadj):
    peak = _rmax(closeadj, 252)
    # log distance left to reclaim the peak (0 = recovered)
    b = np.log(peak.replace(0, np.nan) / closeadj.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery-to-peak gap healing speed over a month ----
def f04dr_f04_drawdown_recovery_recovgapchg_252d_base_v087_signal(closeadj):
    peak = _rmax(closeadj, 252)
    gap = np.log(peak.replace(0, np.nan) / closeadj.replace(0, np.nan))
    b = gap - gap.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- fraction of days that set a new lower-low (deteriorating trough) over the quarter ----
def f04dr_f04_drawdown_recovery_lowerlow_252d_base_v088_signal(closeadj):
    trough = _rmin(closeadj, 252)
    at_trough = (closeadj <= trough * 1.00001).astype(float)
    freq = at_trough.rolling(63, min_periods=21).mean()
    b = freq + 0.25 * _f04_drawdown(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- time spent making progress vs total underwater time (heal efficiency) ----
def f04dr_f04_drawdown_recovery_healeff_252d_base_v089_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    under = (uw < -0.001)
    healing = ((uw > uw.shift(1)) & under).astype(float)
    under_f = under.astype(float)
    num = healing.rolling(252, min_periods=126).sum()
    den = under_f.rolling(252, min_periods=126).sum().replace(0, np.nan)
    b = num / den
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- average drawdown depth conditional on being underwater (severity when down) ----
def f04dr_f04_drawdown_recovery_condsev_252d_base_v090_signal(closeadj):
    # downside capture: how much of the year's negative-return energy lands on the worst days
    r = _f04_ret(closeadj)
    neg = (-r.where(r < 0, 0.0))
    worst5 = neg.rolling(252, min_periods=126).apply(
        lambda a: np.sort(a)[-5:].sum(), raw=True)
    total = neg.rolling(252, min_periods=126).sum().replace(0, np.nan)
    b = worst5 / total
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- maximum single underwater run length (longest unbroken drawdown) over the year ----
def f04dr_f04_drawdown_recovery_maxrun_252d_base_v091_signal(closeadj):
    run = _f04_run_length_under(closeadj, 252, -0.05)
    b = run.rolling(252, min_periods=126).max() / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- current underwater run vs its own typical run length (relative episode length) ----
def f04dr_f04_drawdown_recovery_runrel_252d_base_v092_signal(closeadj):
    run = _f04_run_length_under(closeadj, 252, -0.05)
    typ = run.rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = run / typ
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Calmar regime change: calmar now vs a quarter ago ----
def f04dr_f04_drawdown_recovery_calmarmom_252d_base_v093_signal(closeadj):
    ann_ret = closeadj / closeadj.shift(252) - 1.0
    mdd = (-_f04_maxdd(closeadj, 252)).replace(0, np.nan)
    cal = ann_ret / mdd
    b = cal - cal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain-index momentum (is structural pain building or easing?) ----
def f04dr_f04_drawdown_recovery_painmom_252d_base_v094_signal(closeadj):
    pain = _f04_pain_index(closeadj, 252)
    b = pain - pain.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain-index z (extremity of current structural pain) ----
def f04dr_f04_drawdown_recovery_painz_252d_base_v095_signal(closeadj):
    pain = _f04_pain_index(closeadj, 126)
    b = _z(pain, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown beta to its own deepening: regression-free slope of uw vs time over a month ----
def f04dr_f04_drawdown_recovery_uwtrend_252d_base_v096_signal(closeadj):
    # persistence of the underwater trend: lag-5 autocorrelation of underwater first-differences
    uw = _f04_drawdown(closeadj, 252)
    d = uw.diff()
    b = d.rolling(126, min_periods=63).corr(d.shift(5))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery acceleration: change in recovery-off-trough momentum ----
def f04dr_f04_drawdown_recovery_recovaccel_252d_base_v097_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 252)
    m1 = rec - rec.shift(21)
    m2 = rec.shift(21) - rec.shift(42)
    b = m1 - m2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- worst rolling 21d cumulative loss within the year (acute crash window) ----
def f04dr_f04_drawdown_recovery_worst21cum_252d_base_v098_signal(closeadj):
    cum21 = closeadj / closeadj.shift(21) - 1.0
    q = cum21.rolling(252, min_periods=126).quantile(0.05)
    tail = cum21.where(cum21 <= q)
    b = tail.rolling(252, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- worst rolling 5d cumulative loss within the quarter ----
def f04dr_f04_drawdown_recovery_worst5cum_63d_base_v099_signal(closeadj):
    cum5 = closeadj / closeadj.shift(5) - 1.0
    b = cum5.rolling(63, min_periods=21).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- gain-to-pain ratio: sum of positive returns over sum of abs negative returns ----
def f04dr_f04_drawdown_recovery_gainpain_126d_base_v100_signal(closeadj):
    r = _f04_ret(closeadj)
    pos = r.where(r > 0, 0.0).rolling(126, min_periods=63).sum()
    neg = (-r.where(r < 0, 0.0)).rolling(126, min_periods=63).sum().replace(0, np.nan)
    b = pos / neg - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_gainpain_252d_base_v101_signal(closeadj):
    r = _f04_ret(closeadj)
    pos = r.where(r > 0, 0.0).rolling(252, min_periods=126).sum()
    neg = (-r.where(r < 0, 0.0)).rolling(252, min_periods=126).sum().replace(0, np.nan)
    b = pos / neg - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown-at-risk: 5th percentile of the underwater distribution ----
def f04dr_f04_drawdown_recovery_dar_252d_base_v102_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    b = uw.rolling(252, min_periods=126).quantile(0.05)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- median underwater depth (typical, not worst, drawdown) ----
def f04dr_f04_drawdown_recovery_meduw_252d_base_v103_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    b = uw.rolling(252, min_periods=126).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- interquartile range of underwater (spread of drawdown states) ----
def f04dr_f04_drawdown_recovery_uwiqr_252d_base_v104_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    q75 = uw.rolling(252, min_periods=126).quantile(0.75)
    q25 = uw.rolling(252, min_periods=126).quantile(0.25)
    b = q75 - q25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery breadth: fraction of the year above the year's midpoint of the range ----
def f04dr_f04_drawdown_recovery_abovemid_252d_base_v105_signal(closeadj):
    # near-peak participation: fraction of the quarter spent within 5% of the running peak
    peak = _rmax(closeadj, 252)
    nearpeak = (closeadj >= peak * 0.95).astype(float)
    b = nearpeak.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- trough proximity: how close current price sits to the year's low (capitulation) ----
def f04dr_f04_drawdown_recovery_troughprox_252d_base_v106_signal(closeadj):
    trough = _rmin(closeadj, 252)
    b = trough.replace(0, np.nan) / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- peak proximity (1 = at fresh peak), z-scored vs its own history ----
def f04dr_f04_drawdown_recovery_peakproxz_252d_base_v107_signal(closeadj):
    peak = _rmax(closeadj, 252)
    p = closeadj / peak.replace(0, np.nan)
    b = _z(p, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown convexity: squared underwater (penalizes deep drawdowns more) ----
def f04dr_f04_drawdown_recovery_uwconvex_252d_base_v108_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    sq = -(uw ** 2)
    b = sq - sq.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- time-to-recover estimate: gap-left divided by recent recovery slope (days) ----
def f04dr_f04_drawdown_recovery_ttrest_252d_base_v109_signal(closeadj):
    peak = _rmax(closeadj, 252)
    gap = np.log(peak.replace(0, np.nan) / closeadj.replace(0, np.nan))
    slope = (np.log(closeadj.replace(0, np.nan))).diff().rolling(21, min_periods=10).mean()
    b = gap / slope.where(slope > 0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown stability: std of the max-drawdown series (regime churn) ----
def f04dr_f04_drawdown_recovery_maxddchurn_252d_base_v110_signal(closeadj):
    mdd = _f04_maxdd(closeadj, 63)
    b = mdd.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery resilience: how much of last quarter's drawdown was recovered ----
def f04dr_f04_drawdown_recovery_resilience_252d_base_v111_signal(closeadj):
    dd_then = (-_f04_drawdown(closeadj, 252)).shift(63)
    dd_now = (-_f04_drawdown(closeadj, 252))
    b = (dd_then - dd_now) / dd_then.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain spread long vs very-long (chronic deepening) ----
def f04dr_f04_drawdown_recovery_painspr_252v504_base_v112_signal(closeadj):
    s = _f04_pain_index(closeadj, 252)
    l = _f04_pain_index(closeadj, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown skew across horizons: is the 63d dd worse than 252d would imply? ----
def f04dr_f04_drawdown_recovery_ddhorizskew_base_v113_signal(closeadj):
    d63 = _f04_maxdd(closeadj, 63)
    d252 = _f04_maxdd(closeadj, 252)
    b = d63 - 0.5 * d252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery vs drawdown timing: days-since-trough minus days-since-peak ----
def f04dr_f04_drawdown_recovery_timingbal_252d_base_v114_signal(closeadj):
    dst = _f04_days_since_trough(closeadj, 252)
    dsp = _f04_days_since_peak(closeadj, 252)
    b = dst - dsp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- fresh-trough recency weighted by depth (recent capitulation severity) ----
def f04dr_f04_drawdown_recovery_capit_252d_base_v115_signal(closeadj):
    dst = _f04_days_since_trough(closeadj, 252)
    mdd = (-_f04_maxdd(closeadj, 252))
    # recent (small dst) and deep (large mdd) => high capitulation score
    b = (1.0 - dst) * mdd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- ulcer momentum (is RMS pain rising?) ----
def f04dr_f04_drawdown_recovery_ulcermom_252d_base_v116_signal(closeadj):
    ulcer = _f04_ulcer(closeadj, 126)
    b = ulcer - ulcer.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown duration asymmetry: time under vs above peak threshold ----
def f04dr_f04_drawdown_recovery_durasym_252d_base_v117_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    deep = (uw <= -0.10).astype(float).rolling(252, min_periods=126).mean()
    near = (uw >= -0.02).astype(float).rolling(252, min_periods=126).mean()
    b = deep - near
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery efficiency ratio: net rebound over path length since trough ----
def f04dr_f04_drawdown_recovery_receff_126d_base_v118_signal(closeadj):
    net = (closeadj - _rmin(closeadj, 126)).abs()
    path = closeadj.diff().abs().rolling(126, min_periods=63).sum().replace(0, np.nan)
    b = net / path
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- worst-quarter-in-window: minimum 63d return over the trailing year ----
def f04dr_f04_drawdown_recovery_worstqtr_252d_base_v119_signal(closeadj):
    q = closeadj / closeadj.shift(63) - 1.0
    b = q.rolling(252, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- best-minus-worst quarter spread (recovery amplitude vs crash amplitude) ----
def f04dr_f04_drawdown_recovery_qtrspread_252d_base_v120_signal(closeadj):
    q = closeadj / closeadj.shift(63) - 1.0
    best = q.rolling(252, min_periods=126).max()
    worst = q.rolling(252, min_periods=126).min()
    b = best + worst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- underwater excursion count: how many times it dips past -5% then recovers ----
def f04dr_f04_drawdown_recovery_excursions_252d_base_v121_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    inn = (uw <= -0.05).astype(float)
    entries = ((inn == 1) & (inn.shift(1) == 0)).astype(float)
    cnt = entries.rolling(252, min_periods=126).sum()
    b = cnt + 8.0 * _f04_pain_index(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown half-life proxy: ratio of current uw to uw 21d ago (decay rate) ----
def f04dr_f04_drawdown_recovery_ddhalflife_252d_base_v122_signal(closeadj):
    uw = (-_f04_drawdown(closeadj, 252)).replace(0, np.nan)
    b = uw / uw.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery participation: fraction of up-days while underwater ----
def f04dr_f04_drawdown_recovery_uwupdays_252d_base_v123_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    r = _f04_ret(closeadj)
    upwhile = ((r > 0) & (uw < -0.02)).astype(float)
    under = (uw < -0.02).astype(float)
    num = upwhile.rolling(126, min_periods=63).sum()
    den = under.rolling(126, min_periods=63).sum().replace(0, np.nan)
    b = num / den
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- net drawdown drift: signed area of underwater over the quarter normalized ----
def f04dr_f04_drawdown_recovery_uwdrift_504d_base_v124_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    b = uw.rolling(126, min_periods=63).mean() - uw.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- crash recovery ratio: rebound off trough relative to the prior maxdd magnitude ----
def f04dr_f04_drawdown_recovery_crashrecov_252d_base_v125_signal(closeadj):
    # post-crash snap-back: 21d return measured only when sitting deep in a drawdown
    r21 = closeadj / closeadj.shift(21) - 1.0
    deep = (_f04_drawdown(closeadj, 252) <= -0.15).astype(float)
    snap = (r21 * deep)
    b = snap.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown burstiness: max single-step deepening within the quarter ----
def f04dr_f04_drawdown_recovery_ddburst_63d_base_v126_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    step = uw.diff()
    b = step.rolling(63, min_periods=21).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery smoothness: std of daily steps during the rebound (choppy vs clean) ----
def f04dr_f04_drawdown_recovery_recovchop_252d_base_v127_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 252)
    b = rec.diff().rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- proportion of total return given back from the peak (give-back ratio) ----
def f04dr_f04_drawdown_recovery_giveback_504d_base_v128_signal(closeadj):
    peak = _rmax(closeadj, 504)
    trough_before = _rmin(closeadj, 504)
    gained = (peak - trough_before).replace(0, np.nan)
    given = (peak - closeadj)
    b = given / gained
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown tail heaviness: 1st-pctile uw over 25th-pctile uw ----
def f04dr_f04_drawdown_recovery_ddtail_252d_base_v129_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    p01 = uw.rolling(252, min_periods=126).quantile(0.01)
    p25 = uw.rolling(252, min_periods=126).quantile(0.25).replace(0, np.nan)
    b = p01 / p25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery vs drawdown speed asymmetry (up-leg slope vs down-leg slope) ----
def f04dr_f04_drawdown_recovery_speedasym_252d_base_v130_signal(closeadj):
    # asymmetry of the worst vs best single days (crash magnitude vs spike magnitude)
    r = _f04_ret(closeadj)
    worst = r.rolling(126, min_periods=63).min()
    best = r.rolling(126, min_periods=63).max()
    b = (best + worst) / (best - worst).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- underwater fraction trend (is the stock spending more time underwater?) ----
def f04dr_f04_drawdown_recovery_uwfractrend_252d_base_v131_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    frac = (uw < -0.05).astype(float).rolling(63, min_periods=21).mean()
    b = frac - frac.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- worst drawdown relative to trailing realized range (depth vs normal travel) ----
def f04dr_f04_drawdown_recovery_ddvsrange_252d_base_v132_signal(closeadj):
    mdd = (-_f04_maxdd(closeadj, 252))
    rng = (_rmax(closeadj, 63) / _rmin(closeadj, 63) - 1.0).replace(0, np.nan)
    b = mdd / rng
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery slope rank vs own history (how strong is this rebound historically) ----
def f04dr_f04_drawdown_recovery_recovsloperank_252d_base_v133_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 252)
    dst = _f04_days_since_trough(closeadj, 252).replace(0, np.nan)
    slope = rec / dst
    b = slope.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown autocovariance with returns (do drawdowns predict bounce?) ----
def f04dr_f04_drawdown_recovery_ddretcov_252d_base_v134_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    fwdlike = _f04_ret(closeadj)
    b = uw.rolling(126, min_periods=63).corr(fwdlike)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain-adjusted momentum: trailing return minus pain index (net of suffering) ----
def f04dr_f04_drawdown_recovery_painadjmom_252d_base_v135_signal(closeadj):
    # return per unit of max-drawdown risk, but z-scored vs history (regime, not level)
    ret = closeadj / closeadj.shift(252) - 1.0
    mdd = (-_f04_maxdd(closeadj, 252)).replace(0, np.nan)
    ratio = ret / mdd
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- deepest-drawdown recency: where in the window the worst uw occurred ----
def f04dr_f04_drawdown_recovery_ddrecency_252d_base_v136_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)

    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    b = uw.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery completeness over two years (reclaimed vs all-time-window peak) ----
def f04dr_f04_drawdown_recovery_recovcomplete_504d_base_v137_signal(closeadj):
    # change in proximity-to-2y-peak over a quarter (is full recovery being approached?)
    peak = _rmax(closeadj, 504)
    prox = closeadj / peak.replace(0, np.nan)
    b = prox - prox.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown count weighted by depth over two years ----
def f04dr_f04_drawdown_recovery_weighteddd_504d_base_v138_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    inn = (uw <= -0.15).astype(float)
    entries = ((inn == 1) & (inn.shift(1) == 0)).astype(float)
    depth = (-uw)
    b = (entries * depth).rolling(504, min_periods=252).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- short-vs-long recovery slope spread (acute bounce vs structural recovery) ----
def f04dr_f04_drawdown_recovery_recovslopespr_base_v139_signal(closeadj):
    rec_s = _f04_recovery_off_trough(closeadj, 63)
    dst_s = _f04_days_since_trough(closeadj, 63).replace(0, np.nan)
    rec_l = _f04_recovery_off_trough(closeadj, 252)
    dst_l = _f04_days_since_trough(closeadj, 252).replace(0, np.nan)
    b = (rec_s / dst_s) - (rec_l / dst_l)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- underwater entropy proxy: how evenly distributed the drawdown states are ----
def f04dr_f04_drawdown_recovery_uwspreadnorm_252d_base_v140_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    sd = uw.rolling(252, min_periods=126).std()
    rng = (_rmax(uw, 252) - _rmin(uw, 252)).replace(0, np.nan)
    b = sd / rng
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery off trough scaled by peak distance (reclaim efficiency) ----
def f04dr_f04_drawdown_recovery_reclaim_252d_base_v141_signal(closeadj):
    # reclaim balance: rebound-off-trough vs remaining peak-gap, normalized (signed -1..1)
    rec = _f04_recovery_off_trough(closeadj, 252)
    peakgap = (_rmax(closeadj, 252) / closeadj.replace(0, np.nan) - 1.0)
    b = (rec - peakgap) / (rec + peakgap).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown velocity z (is the deepening rate abnormal vs history) ----
def f04dr_f04_drawdown_recovery_ddvelz_252d_base_v142_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    vel = uw - uw.shift(5)
    b = _z(vel, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- ratio of underwater std to pain (volatility of the drawdown vs its level) ----
def f04dr_f04_drawdown_recovery_uwvolratio_252d_base_v143_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    sd = uw.rolling(126, min_periods=63).std()
    pain = _f04_pain_index(closeadj, 126).replace(0, np.nan)
    b = sd / pain
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- maximum recovery within the window (best rebound off any trough) ----
def f04dr_f04_drawdown_recovery_maxrecov_252d_base_v144_signal(closeadj):
    # current 63d rebound relative to the strongest 63d rebound seen this year (rebound percentile)
    rec = _f04_recovery_off_trough(closeadj, 63)
    best = rec.rolling(252, min_periods=126).max().replace(0, np.nan)
    b = rec / best
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown persistence streak normalized & signed by current state ----
def f04dr_f04_drawdown_recovery_ddstreaksig_252d_base_v145_signal(closeadj):
    run_dn = _f04_run_length_under(closeadj, 252, -0.03)
    uw = _f04_drawdown(closeadj, 252)
    b = run_dn / 126.0 * np.sign(uw)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery vs drawdown area balance over two years ----
def f04dr_f04_drawdown_recovery_areabal_504d_base_v146_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    rec = _f04_recovery_off_trough(closeadj, 504)
    a_dd = (-uw).rolling(252, min_periods=126).sum()
    a_rec = rec.rolling(252, min_periods=126).sum()
    b = (a_rec - a_dd) / (a_rec + a_dd).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- conditional recovery slope: rebound speed only counted on up-days ----
def f04dr_f04_drawdown_recovery_upslope_252d_base_v147_signal(closeadj):
    r = _f04_ret(closeadj)
    uw = _f04_drawdown(closeadj, 252)
    upwhileuw = r.where((r > 0) & (uw < -0.02), 0.0)
    b = upwhileuw.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown-frequency rank vs own history (regime of how often it crashes) ----
def f04dr_f04_drawdown_recovery_ddfreqrank_252d_base_v148_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    inn = (uw <= -0.10).astype(float)
    entries = ((inn == 1) & (inn.shift(1) == 0)).astype(float)
    freq = entries.rolling(126, min_periods=63).sum() + _f04_pain_index(closeadj, 63)
    b = freq.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain/ulcer composite stress score (multi-facet severity blend) ----
def f04dr_f04_drawdown_recovery_stresscomposite_252d_base_v149_signal(closeadj):
    # stress regime as a z-blend so it captures relative shifts, not raw depth levels
    mdd = (-_f04_maxdd(closeadj, 252))
    ulcer = _f04_ulcer(closeadj, 252)
    vel = (_f04_drawdown(closeadj, 252).diff(21))
    b = _z(mdd, 252) + _z(ulcer, 252) - _z(vel, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery-quality composite: rebound x heal-efficiency / pain ----
def f04dr_f04_drawdown_recovery_recovquality_252d_base_v150_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 252)
    pain = _f04_pain_index(closeadj, 252).replace(0, np.nan)
    dst = _f04_days_since_trough(closeadj, 252).replace(0, np.nan)
    b = (rec / dst) * (rec / pain)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04dr_f04_drawdown_recovery_maxddz_252d_base_v076_signal,
    f04dr_f04_drawdown_recovery_maxddz_504d_base_v077_signal,
    f04dr_f04_drawdown_recovery_maxddrank_252d_base_v078_signal,
    f04dr_f04_drawdown_recovery_maxddmom_252d_base_v079_signal,
    f04dr_f04_drawdown_recovery_maxddmom_63d_base_v080_signal,
    f04dr_f04_drawdown_recovery_recovperulcer_252d_base_v081_signal,
    f04dr_f04_drawdown_recovery_recovperpain_504d_base_v082_signal,
    f04dr_f04_drawdown_recovery_uwskew_252d_base_v083_signal,
    f04dr_f04_drawdown_recovery_uwstd_252d_base_v084_signal,
    f04dr_f04_drawdown_recovery_uwstd_63d_base_v085_signal,
    f04dr_f04_drawdown_recovery_recovgap_252d_base_v086_signal,
    f04dr_f04_drawdown_recovery_recovgapchg_252d_base_v087_signal,
    f04dr_f04_drawdown_recovery_lowerlow_252d_base_v088_signal,
    f04dr_f04_drawdown_recovery_healeff_252d_base_v089_signal,
    f04dr_f04_drawdown_recovery_condsev_252d_base_v090_signal,
    f04dr_f04_drawdown_recovery_maxrun_252d_base_v091_signal,
    f04dr_f04_drawdown_recovery_runrel_252d_base_v092_signal,
    f04dr_f04_drawdown_recovery_calmarmom_252d_base_v093_signal,
    f04dr_f04_drawdown_recovery_painmom_252d_base_v094_signal,
    f04dr_f04_drawdown_recovery_painz_252d_base_v095_signal,
    f04dr_f04_drawdown_recovery_uwtrend_252d_base_v096_signal,
    f04dr_f04_drawdown_recovery_recovaccel_252d_base_v097_signal,
    f04dr_f04_drawdown_recovery_worst21cum_252d_base_v098_signal,
    f04dr_f04_drawdown_recovery_worst5cum_63d_base_v099_signal,
    f04dr_f04_drawdown_recovery_gainpain_126d_base_v100_signal,
    f04dr_f04_drawdown_recovery_gainpain_252d_base_v101_signal,
    f04dr_f04_drawdown_recovery_dar_252d_base_v102_signal,
    f04dr_f04_drawdown_recovery_meduw_252d_base_v103_signal,
    f04dr_f04_drawdown_recovery_uwiqr_252d_base_v104_signal,
    f04dr_f04_drawdown_recovery_abovemid_252d_base_v105_signal,
    f04dr_f04_drawdown_recovery_troughprox_252d_base_v106_signal,
    f04dr_f04_drawdown_recovery_peakproxz_252d_base_v107_signal,
    f04dr_f04_drawdown_recovery_uwconvex_252d_base_v108_signal,
    f04dr_f04_drawdown_recovery_ttrest_252d_base_v109_signal,
    f04dr_f04_drawdown_recovery_maxddchurn_252d_base_v110_signal,
    f04dr_f04_drawdown_recovery_resilience_252d_base_v111_signal,
    f04dr_f04_drawdown_recovery_painspr_252v504_base_v112_signal,
    f04dr_f04_drawdown_recovery_ddhorizskew_base_v113_signal,
    f04dr_f04_drawdown_recovery_timingbal_252d_base_v114_signal,
    f04dr_f04_drawdown_recovery_capit_252d_base_v115_signal,
    f04dr_f04_drawdown_recovery_ulcermom_252d_base_v116_signal,
    f04dr_f04_drawdown_recovery_durasym_252d_base_v117_signal,
    f04dr_f04_drawdown_recovery_receff_126d_base_v118_signal,
    f04dr_f04_drawdown_recovery_worstqtr_252d_base_v119_signal,
    f04dr_f04_drawdown_recovery_qtrspread_252d_base_v120_signal,
    f04dr_f04_drawdown_recovery_excursions_252d_base_v121_signal,
    f04dr_f04_drawdown_recovery_ddhalflife_252d_base_v122_signal,
    f04dr_f04_drawdown_recovery_uwupdays_252d_base_v123_signal,
    f04dr_f04_drawdown_recovery_uwdrift_504d_base_v124_signal,
    f04dr_f04_drawdown_recovery_crashrecov_252d_base_v125_signal,
    f04dr_f04_drawdown_recovery_ddburst_63d_base_v126_signal,
    f04dr_f04_drawdown_recovery_recovchop_252d_base_v127_signal,
    f04dr_f04_drawdown_recovery_giveback_504d_base_v128_signal,
    f04dr_f04_drawdown_recovery_ddtail_252d_base_v129_signal,
    f04dr_f04_drawdown_recovery_speedasym_252d_base_v130_signal,
    f04dr_f04_drawdown_recovery_uwfractrend_252d_base_v131_signal,
    f04dr_f04_drawdown_recovery_ddvsrange_252d_base_v132_signal,
    f04dr_f04_drawdown_recovery_recovsloperank_252d_base_v133_signal,
    f04dr_f04_drawdown_recovery_ddretcov_252d_base_v134_signal,
    f04dr_f04_drawdown_recovery_painadjmom_252d_base_v135_signal,
    f04dr_f04_drawdown_recovery_ddrecency_252d_base_v136_signal,
    f04dr_f04_drawdown_recovery_recovcomplete_504d_base_v137_signal,
    f04dr_f04_drawdown_recovery_weighteddd_504d_base_v138_signal,
    f04dr_f04_drawdown_recovery_recovslopespr_base_v139_signal,
    f04dr_f04_drawdown_recovery_uwspreadnorm_252d_base_v140_signal,
    f04dr_f04_drawdown_recovery_reclaim_252d_base_v141_signal,
    f04dr_f04_drawdown_recovery_ddvelz_252d_base_v142_signal,
    f04dr_f04_drawdown_recovery_uwvolratio_252d_base_v143_signal,
    f04dr_f04_drawdown_recovery_maxrecov_252d_base_v144_signal,
    f04dr_f04_drawdown_recovery_ddstreaksig_252d_base_v145_signal,
    f04dr_f04_drawdown_recovery_areabal_504d_base_v146_signal,
    f04dr_f04_drawdown_recovery_upslope_252d_base_v147_signal,
    f04dr_f04_drawdown_recovery_ddfreqrank_252d_base_v148_signal,
    f04dr_f04_drawdown_recovery_stresscomposite_252d_base_v149_signal,
    f04dr_f04_drawdown_recovery_recovquality_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_DRAWDOWN_RECOVERY_REGISTRY_076_150 = REGISTRY


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

    print("OK f04_drawdown_recovery_base_076_150_claude: %d features pass" % n_features)
