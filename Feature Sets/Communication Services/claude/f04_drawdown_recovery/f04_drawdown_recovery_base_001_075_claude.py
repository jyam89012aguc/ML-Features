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
    # underwater fraction below the rolling peak (<= 0)
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return close / peak.replace(0, np.nan) - 1.0


def _f04_maxdd(close, w):
    # worst (most negative) drawdown observed over the window
    uw = _f04_drawdown(close, w)
    return uw.rolling(w, min_periods=max(1, w // 2)).min()


def _f04_recovery_off_trough(close, w):
    # rebound off the rolling trough (>= 0)
    trough = close.rolling(w, min_periods=max(1, w // 2)).min()
    return close / trough.replace(0, np.nan) - 1.0


def _f04_underwater_frac(close, w, thr):
    # fraction of the window spent more than |thr| below the running peak
    uw = _f04_drawdown(close, w)
    deep = (uw <= thr).astype(float)
    return deep.rolling(w, min_periods=max(1, w // 2)).mean()


def _f04_pain_index(close, w):
    # average underwater depth (Pain Index), positive magnitude
    uw = _f04_drawdown(close, w)
    return (-uw).rolling(w, min_periods=max(1, w // 2)).mean()


def _f04_ulcer(close, w):
    # Ulcer Index = RMS of underwater depth
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


def _f04_dd_episodes(close, w, thr):
    # count of distinct drawdown-onset events (cross below thr) over the window
    uw = _f04_drawdown(close, w)
    in_dd = (uw <= thr).astype(float)
    entries = ((in_dd == 1) & (in_dd.shift(1) == 0)).astype(float)
    return entries.rolling(w, min_periods=max(1, w // 2)).sum()


def _f04_ret(close):
    return close.pct_change()


# ============================================================
# ---- max drawdown over the canonical windows (21/63/126/252/504) ----
def f04dr_f04_drawdown_recovery_maxdd_21d_base_v001_signal(closeadj):
    b = _f04_maxdd(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_maxdd_63d_base_v002_signal(closeadj):
    b = _f04_maxdd(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_maxdd_126d_base_v003_signal(closeadj):
    b = _f04_maxdd(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_maxdd_252d_base_v004_signal(closeadj):
    b = _f04_maxdd(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_maxdd_504d_base_v005_signal(closeadj):
    b = _f04_maxdd(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- current underwater depth (distance below running peak) ----
def f04dr_f04_drawdown_recovery_uw_63d_base_v006_signal(closeadj):
    b = _f04_drawdown(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uw_252d_base_v007_signal(closeadj):
    b = _f04_drawdown(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uw_504d_base_v008_signal(closeadj):
    b = _f04_drawdown(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- underwater duration (fraction of window > X% below peak) ----
def f04dr_f04_drawdown_recovery_uwdur05_252d_base_v009_signal(closeadj):
    b = _f04_underwater_frac(closeadj, 252, -0.05)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdur10_252d_base_v010_signal(closeadj):
    # longest consecutive underwater (>10% below peak) stretch within the year
    uw = _f04_drawdown(closeadj, 252)
    under = (uw <= -0.10).astype(float)
    grp = (under == 0).cumsum()
    run = under.groupby(grp).cumsum()
    b = run.rolling(252, min_periods=126).max() / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdur20_252d_base_v011_signal(closeadj):
    # stickiness of drawdowns: lag-21 autocorrelation of the underwater series
    # (high => slow-healing, persistent drawdowns; low/neg => quick V-recoveries)
    uw = _f04_drawdown(closeadj, 252)
    b = uw.rolling(126, min_periods=63).corr(uw.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdur10_504d_base_v012_signal(closeadj):
    b = _f04_underwater_frac(closeadj, 504, -0.10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdur10_63d_base_v013_signal(closeadj):
    b = _f04_underwater_frac(closeadj, 63, -0.10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- consecutive underwater streak length (current run below peak) ----
def f04dr_f04_drawdown_recovery_uwstreak_252d_base_v014_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    under = (uw < -0.001).astype(float)
    # length of the current run of consecutive underwater days, normalized
    grp = (under == 0).cumsum()
    streak = under.groupby(grp).cumsum()
    b = streak / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwstreak_63d_base_v015_signal(closeadj):
    uw = _f04_drawdown(closeadj, 63)
    under = (uw < -0.001).astype(float)
    grp = (under == 0).cumsum()
    streak = under.groupby(grp).cumsum()
    b = streak / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery off trough over the canonical windows ----
def f04dr_f04_drawdown_recovery_recov_63d_base_v016_signal(closeadj):
    b = _f04_recovery_off_trough(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recov_126d_base_v017_signal(closeadj):
    b = _f04_recovery_off_trough(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recov_252d_base_v018_signal(closeadj):
    b = _f04_recovery_off_trough(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recov_504d_base_v019_signal(closeadj):
    b = _f04_recovery_off_trough(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery slope off trough = rebound per day since the trough ----
def f04dr_f04_drawdown_recovery_recovslope_252d_base_v020_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 252)
    dst = _f04_days_since_trough(closeadj, 252).replace(0, np.nan)
    b = rec / dst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recovslope_504d_base_v021_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 504)
    dst = _f04_days_since_trough(closeadj, 504).replace(0, np.nan)
    b = rec / dst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recovslope_63d_base_v022_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 63)
    dst = _f04_days_since_trough(closeadj, 63).replace(0, np.nan)
    b = rec / dst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- time-to-recover proxy: how stale the running peak is ----
def f04dr_f04_drawdown_recovery_ttr_252d_base_v023_signal(closeadj):
    # days since the 252d peak, weighted by how deep we still are (deeper & older = worse)
    dsp = _f04_days_since_peak(closeadj, 252)
    uw = _f04_drawdown(closeadj, 252)
    b = dsp * (-uw)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ttr_504d_base_v024_signal(closeadj):
    dsp = _f04_days_since_peak(closeadj, 504)
    uw = _f04_drawdown(closeadj, 504)
    b = dsp * (-uw)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- days since peak / trough (anchor staleness) ----
def f04dr_f04_drawdown_recovery_dsp_252d_base_v025_signal(closeadj):
    b = _f04_days_since_peak(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_dst_252d_base_v026_signal(closeadj):
    b = _f04_days_since_trough(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_dsp_504d_base_v027_signal(closeadj):
    b = _f04_days_since_peak(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown-episode frequency (onset counts) ----
def f04dr_f04_drawdown_recovery_ddfreq10_252d_base_v028_signal(closeadj):
    cnt = _f04_dd_episodes(closeadj, 252, -0.10)
    depth = _f04_pain_index(closeadj, 63)
    b = cnt + 5.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ddfreq20_252d_base_v029_signal(closeadj):
    cnt = _f04_dd_episodes(closeadj, 252, -0.20)
    depth = (-_f04_drawdown(closeadj, 252)).rolling(21, min_periods=10).mean()
    b = cnt + 3.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ddfreq10_504d_base_v030_signal(closeadj):
    cnt = _f04_dd_episodes(closeadj, 504, -0.10)
    depth = _f04_pain_index(closeadj, 126)
    b = cnt + 4.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain index (average underwater depth) ----
def f04dr_f04_drawdown_recovery_pain_126d_base_v031_signal(closeadj):
    b = _f04_pain_index(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_pain_252d_base_v032_signal(closeadj):
    b = _f04_pain_index(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_pain_504d_base_v033_signal(closeadj):
    b = _f04_pain_index(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- ulcer index (RMS underwater) ----
def f04dr_f04_drawdown_recovery_ulcer_126d_base_v034_signal(closeadj):
    # pain concentration: ulcer (RMS depth) over pain (mean depth) -> >1 means lumpy/spiky drawdowns
    ulcer = _f04_ulcer(closeadj, 126)
    pain = _f04_pain_index(closeadj, 126).replace(0, np.nan)
    b = ulcer / pain
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ulcer_252d_base_v035_signal(closeadj):
    ulcer = _f04_ulcer(closeadj, 252)
    pain = _f04_pain_index(closeadj, 252).replace(0, np.nan)
    b = ulcer / pain
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ulcer_504d_base_v036_signal(closeadj):
    ulcer = _f04_ulcer(closeadj, 504)
    pain = _f04_pain_index(closeadj, 504).replace(0, np.nan)
    b = ulcer / pain
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Calmar ratio: trailing return over max drawdown magnitude ----
def f04dr_f04_drawdown_recovery_calmar_252d_base_v037_signal(closeadj):
    ann_ret = closeadj / closeadj.shift(252) - 1.0
    mdd = (-_f04_maxdd(closeadj, 252)).replace(0, np.nan)
    b = ann_ret / mdd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_calmar_504d_base_v038_signal(closeadj):
    ann_ret = (closeadj / closeadj.shift(504)) ** (252.0 / 504.0) - 1.0
    mdd = (-_f04_maxdd(closeadj, 504)).replace(0, np.nan)
    b = ann_ret / mdd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_calmar_126d_base_v039_signal(closeadj):
    ann_ret = (closeadj / closeadj.shift(126)) ** (252.0 / 126.0) - 1.0
    mdd = (-_f04_maxdd(closeadj, 126)).replace(0, np.nan)
    b = ann_ret / mdd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- martin ratio: trailing return over ulcer index ----
def f04dr_f04_drawdown_recovery_martin_252d_base_v040_signal(closeadj):
    # Sortino-style: trailing return over downside semi-deviation (recovery quality vs downside)
    ann_ret = closeadj / closeadj.shift(252) - 1.0
    r = _f04_ret(closeadj)
    neg = r.where(r < 0, 0.0)
    downdev = np.sqrt((neg ** 2).rolling(252, min_periods=126).mean()) * np.sqrt(252.0)
    b = ann_ret / downdev.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown z-score (how extreme is the current underwater vs its own history) ----
def f04dr_f04_drawdown_recovery_uwz_252d_base_v041_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    b = _z(uw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwz_504d_base_v042_signal(closeadj):
    uw = _f04_drawdown(closeadj, 504)
    b = _z(uw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery z-score ----
def f04dr_f04_drawdown_recovery_recovz_252d_base_v043_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 252)
    b = _z(rec, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown percentile rank vs own history ----
def f04dr_f04_drawdown_recovery_uwrank_252d_base_v044_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    b = uw.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery rank vs own history ----
def f04dr_f04_drawdown_recovery_recovrank_252d_base_v045_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 252)
    b = rec.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown delta (how fast the underwater is deepening / healing) ----
def f04dr_f04_drawdown_recovery_uwdelta_21d_base_v046_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    b = uw - uw.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_uwdelta_63d_base_v047_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    b = uw - uw.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- V-shape balance: recovery magnitude vs drawdown magnitude ----
def f04dr_f04_drawdown_recovery_vshape_252d_base_v048_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 252)
    dd = (-_f04_maxdd(closeadj, 252))
    b = (rec - dd) / (rec + dd).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_vshape_504d_base_v049_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 504)
    dd = (-_f04_maxdd(closeadj, 504))
    b = (rec - dd) / (rec + dd).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery fraction: how much of the max drawdown has been clawed back ----
def f04dr_f04_drawdown_recovery_recovfrac_252d_base_v050_signal(closeadj):
    peak = _rmax(closeadj, 252)
    trough = _rmin(closeadj, 252)
    # claw-back fraction (0 at trough, 1 at peak), measured as change over a month (heal speed)
    frac = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    b = frac - frac.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recovfrac_504d_base_v051_signal(closeadj):
    peak = _rmax(closeadj, 504)
    trough = _rmin(closeadj, 504)
    frac = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    # where the current claw-back sits vs its own 2y history
    b = frac.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- downside semi-deviation (pain of negative returns only) ----
def f04dr_f04_drawdown_recovery_downdev_63d_base_v052_signal(closeadj):
    r = _f04_ret(closeadj)
    neg = r.where(r < 0, 0.0)
    b = np.sqrt((neg ** 2).rolling(63, min_periods=21).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_downdev_252d_base_v053_signal(closeadj):
    r = _f04_ret(closeadj)
    neg = r.where(r < 0, 0.0)
    b = np.sqrt((neg ** 2).rolling(252, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- worst single-day crash over the window (these crash on misses) ----
def f04dr_f04_drawdown_recovery_worstday_63d_base_v054_signal(closeadj):
    r = _f04_ret(closeadj)
    b = r.rolling(63, min_periods=21).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_worstday_252d_base_v055_signal(closeadj):
    # average of the worst 5% of daily returns over the year (expected-shortfall style)
    r = _f04_ret(closeadj)
    q = r.rolling(252, min_periods=126).quantile(0.05)
    tail = r.where(r <= q)
    b = tail.rolling(252, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- crash-day frequency: count of large negative days ----
def f04dr_f04_drawdown_recovery_crashfreq_252d_base_v056_signal(closeadj):
    # magnitude-weighted crash intensity: summed excess depth of >7% down days
    r = _f04_ret(closeadj)
    excess = (-r - 0.05).clip(lower=0)
    b = excess.rolling(252, min_periods=126).sum() + _f04_pain_index(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_crashfreq_63d_base_v057_signal(closeadj):
    r = _f04_ret(closeadj)
    excess = (-r - 0.05).clip(lower=0)
    b = excess.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown-to-vol ratio (is the drawdown deeper than vol would suggest?) ----
def f04dr_f04_drawdown_recovery_ddvol_252d_base_v058_signal(closeadj):
    # change in the drawdown/vol stress ratio over a quarter (is stress accelerating vs vol?)
    mdd = (-_f04_maxdd(closeadj, 252))
    vol = _f04_ret(closeadj).rolling(63, min_periods=21).std()
    ratio = mdd / (vol * np.sqrt(252.0)).replace(0, np.nan)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- ratio of short to long drawdown (acute vs chronic stress) ----
def f04dr_f04_drawdown_recovery_ddratio_63v252_base_v059_signal(closeadj):
    s = _f04_maxdd(closeadj, 63)
    l = _f04_maxdd(closeadj, 252)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_ddratio_126v504_base_v060_signal(closeadj):
    s = _f04_maxdd(closeadj, 126)
    l = _f04_maxdd(closeadj, 504)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain-index spread short vs long (recent pain vs structural pain) ----
def f04dr_f04_drawdown_recovery_painspr_63v252_base_v061_signal(closeadj):
    s = _f04_pain_index(closeadj, 63)
    l = _f04_pain_index(closeadj, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery momentum: change in recovery off trough over a quarter ----
def f04dr_f04_drawdown_recovery_recovmom_252d_base_v062_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 252)
    b = rec - rec.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f04dr_f04_drawdown_recovery_recovmom_504d_base_v063_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 504)
    b = rec - rec.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- deepest-quartile time: fraction of year in the worst quartile of drawdown ----
def f04dr_f04_drawdown_recovery_deeptime_252d_base_v064_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    thr = uw.rolling(252, min_periods=126).quantile(0.25)
    deep = (uw <= thr).astype(float)
    b = deep.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- conditional drawdown at risk: mean of worst 10% underwater readings ----
def f04dr_f04_drawdown_recovery_cdar_252d_base_v065_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    q = uw.rolling(252, min_periods=126).quantile(0.10)
    tail = uw.where(uw <= q)
    b = tail.rolling(252, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- skew of returns (crash asymmetry: negative skew = crash-prone) ----
def f04dr_f04_drawdown_recovery_retskew_126d_base_v066_signal(closeadj):
    r = _f04_ret(closeadj)
    b = r.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- max run-up vs max drawdown asymmetry over the window ----
def f04dr_f04_drawdown_recovery_runupdd_252d_base_v067_signal(closeadj):
    trough = _rmin(closeadj, 252)
    runup = (_rmax(closeadj, 252) / trough.replace(0, np.nan) - 1.0)
    mdd = (-_f04_maxdd(closeadj, 252))
    b = (runup - mdd) / (runup + mdd).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- net underwater area integral over a quarter (cumulative pain) ----
def f04dr_f04_drawdown_recovery_uwarea_252d_base_v068_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    b = uw.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown acceleration: second difference of underwater (curvature) ----
def f04dr_f04_drawdown_recovery_uwcurv_252d_base_v069_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    b = (uw - uw.shift(21)) - (uw.shift(21) - uw.shift(42))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery slope smoothed (persistent rebound speed) ----
def f04dr_f04_drawdown_recovery_recovsmooth_252d_base_v070_signal(closeadj):
    rec = _f04_recovery_off_trough(closeadj, 252)
    b = rec.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- underwater persistence: how long since price was at a fresh peak ----
def f04dr_f04_drawdown_recovery_freshpeakgap_252d_base_v071_signal(closeadj):
    peak = _rmax(closeadj, 252)
    at_peak = (closeadj >= peak * 0.99999).astype(float)
    freq = at_peak.rolling(252, min_periods=126).mean()
    b = -freq + _f04_drawdown(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown tanh-squashed velocity (bounded deepening rate) ----
def f04dr_f04_drawdown_recovery_uwtanh_252d_base_v072_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    chg = uw - uw.shift(21)
    b = np.tanh(15.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- sign x magnitude of drawdown (compressed depth) ----
def f04dr_f04_drawdown_recovery_uwsignmag_252d_base_v073_signal(closeadj):
    uw = _f04_drawdown(closeadj, 252)
    b = np.sign(uw) * (uw.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain-to-recovery ratio: how much pain per unit of rebound (interaction) ----
def f04dr_f04_drawdown_recovery_painrecov_252d_base_v074_signal(closeadj):
    pain = _f04_pain_index(closeadj, 252)
    rec = _f04_recovery_off_trough(closeadj, 252).replace(0, np.nan)
    b = pain / rec
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown dispersion across 63/126/252/504 (multi-horizon stress disagreement) ----
def f04dr_f04_drawdown_recovery_dddisp_multi_base_v075_signal(closeadj):
    d1 = _f04_maxdd(closeadj, 63)
    d2 = _f04_maxdd(closeadj, 126)
    d3 = _f04_maxdd(closeadj, 252)
    d4 = _f04_maxdd(closeadj, 504)
    b = pd.concat([d1, d2, d3, d4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f04dr_f04_drawdown_recovery_maxdd_21d_base_v001_signal,
    f04dr_f04_drawdown_recovery_maxdd_63d_base_v002_signal,
    f04dr_f04_drawdown_recovery_maxdd_126d_base_v003_signal,
    f04dr_f04_drawdown_recovery_maxdd_252d_base_v004_signal,
    f04dr_f04_drawdown_recovery_maxdd_504d_base_v005_signal,
    f04dr_f04_drawdown_recovery_uw_63d_base_v006_signal,
    f04dr_f04_drawdown_recovery_uw_252d_base_v007_signal,
    f04dr_f04_drawdown_recovery_uw_504d_base_v008_signal,
    f04dr_f04_drawdown_recovery_uwdur05_252d_base_v009_signal,
    f04dr_f04_drawdown_recovery_uwdur10_252d_base_v010_signal,
    f04dr_f04_drawdown_recovery_uwdur20_252d_base_v011_signal,
    f04dr_f04_drawdown_recovery_uwdur10_504d_base_v012_signal,
    f04dr_f04_drawdown_recovery_uwdur10_63d_base_v013_signal,
    f04dr_f04_drawdown_recovery_uwstreak_252d_base_v014_signal,
    f04dr_f04_drawdown_recovery_uwstreak_63d_base_v015_signal,
    f04dr_f04_drawdown_recovery_recov_63d_base_v016_signal,
    f04dr_f04_drawdown_recovery_recov_126d_base_v017_signal,
    f04dr_f04_drawdown_recovery_recov_252d_base_v018_signal,
    f04dr_f04_drawdown_recovery_recov_504d_base_v019_signal,
    f04dr_f04_drawdown_recovery_recovslope_252d_base_v020_signal,
    f04dr_f04_drawdown_recovery_recovslope_504d_base_v021_signal,
    f04dr_f04_drawdown_recovery_recovslope_63d_base_v022_signal,
    f04dr_f04_drawdown_recovery_ttr_252d_base_v023_signal,
    f04dr_f04_drawdown_recovery_ttr_504d_base_v024_signal,
    f04dr_f04_drawdown_recovery_dsp_252d_base_v025_signal,
    f04dr_f04_drawdown_recovery_dst_252d_base_v026_signal,
    f04dr_f04_drawdown_recovery_dsp_504d_base_v027_signal,
    f04dr_f04_drawdown_recovery_ddfreq10_252d_base_v028_signal,
    f04dr_f04_drawdown_recovery_ddfreq20_252d_base_v029_signal,
    f04dr_f04_drawdown_recovery_ddfreq10_504d_base_v030_signal,
    f04dr_f04_drawdown_recovery_pain_126d_base_v031_signal,
    f04dr_f04_drawdown_recovery_pain_252d_base_v032_signal,
    f04dr_f04_drawdown_recovery_pain_504d_base_v033_signal,
    f04dr_f04_drawdown_recovery_ulcer_126d_base_v034_signal,
    f04dr_f04_drawdown_recovery_ulcer_252d_base_v035_signal,
    f04dr_f04_drawdown_recovery_ulcer_504d_base_v036_signal,
    f04dr_f04_drawdown_recovery_calmar_252d_base_v037_signal,
    f04dr_f04_drawdown_recovery_calmar_504d_base_v038_signal,
    f04dr_f04_drawdown_recovery_calmar_126d_base_v039_signal,
    f04dr_f04_drawdown_recovery_martin_252d_base_v040_signal,
    f04dr_f04_drawdown_recovery_uwz_252d_base_v041_signal,
    f04dr_f04_drawdown_recovery_uwz_504d_base_v042_signal,
    f04dr_f04_drawdown_recovery_recovz_252d_base_v043_signal,
    f04dr_f04_drawdown_recovery_uwrank_252d_base_v044_signal,
    f04dr_f04_drawdown_recovery_recovrank_252d_base_v045_signal,
    f04dr_f04_drawdown_recovery_uwdelta_21d_base_v046_signal,
    f04dr_f04_drawdown_recovery_uwdelta_63d_base_v047_signal,
    f04dr_f04_drawdown_recovery_vshape_252d_base_v048_signal,
    f04dr_f04_drawdown_recovery_vshape_504d_base_v049_signal,
    f04dr_f04_drawdown_recovery_recovfrac_252d_base_v050_signal,
    f04dr_f04_drawdown_recovery_recovfrac_504d_base_v051_signal,
    f04dr_f04_drawdown_recovery_downdev_63d_base_v052_signal,
    f04dr_f04_drawdown_recovery_downdev_252d_base_v053_signal,
    f04dr_f04_drawdown_recovery_worstday_63d_base_v054_signal,
    f04dr_f04_drawdown_recovery_worstday_252d_base_v055_signal,
    f04dr_f04_drawdown_recovery_crashfreq_252d_base_v056_signal,
    f04dr_f04_drawdown_recovery_crashfreq_63d_base_v057_signal,
    f04dr_f04_drawdown_recovery_ddvol_252d_base_v058_signal,
    f04dr_f04_drawdown_recovery_ddratio_63v252_base_v059_signal,
    f04dr_f04_drawdown_recovery_ddratio_126v504_base_v060_signal,
    f04dr_f04_drawdown_recovery_painspr_63v252_base_v061_signal,
    f04dr_f04_drawdown_recovery_recovmom_252d_base_v062_signal,
    f04dr_f04_drawdown_recovery_recovmom_504d_base_v063_signal,
    f04dr_f04_drawdown_recovery_deeptime_252d_base_v064_signal,
    f04dr_f04_drawdown_recovery_cdar_252d_base_v065_signal,
    f04dr_f04_drawdown_recovery_retskew_126d_base_v066_signal,
    f04dr_f04_drawdown_recovery_runupdd_252d_base_v067_signal,
    f04dr_f04_drawdown_recovery_uwarea_252d_base_v068_signal,
    f04dr_f04_drawdown_recovery_uwcurv_252d_base_v069_signal,
    f04dr_f04_drawdown_recovery_recovsmooth_252d_base_v070_signal,
    f04dr_f04_drawdown_recovery_freshpeakgap_252d_base_v071_signal,
    f04dr_f04_drawdown_recovery_uwtanh_252d_base_v072_signal,
    f04dr_f04_drawdown_recovery_uwsignmag_252d_base_v073_signal,
    f04dr_f04_drawdown_recovery_painrecov_252d_base_v074_signal,
    f04dr_f04_drawdown_recovery_dddisp_multi_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F04_DRAWDOWN_RECOVERY_REGISTRY_001_075 = REGISTRY


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

    print("OK f04_drawdown_recovery_base_001_075_claude: %d features pass" % n_features)
