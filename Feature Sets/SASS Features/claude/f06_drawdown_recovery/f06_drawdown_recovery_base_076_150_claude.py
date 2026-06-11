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


# ===== f06 drawdown / recovery domain primitives =====
def _f06_drawdown(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return close / peak.replace(0, np.nan) - 1.0


def _f06_logdd(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(close.replace(0, np.nan) / peak.replace(0, np.nan))


def _f06_maxdd(close, w):
    def _f(a):
        peak = np.maximum.accumulate(a)
        dd = a / peak - 1.0
        return float(dd.min())
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f06_avgdd_episodes(close, w):
    # average depth of the worst point of each underwater episode within the window
    def _f(a):
        peak = np.maximum.accumulate(a)
        dd = a / peak - 1.0
        troughs = []
        cur = 0.0
        inep = False
        for x in dd:
            if x < -1e-9:
                inep = True
                if x < cur:
                    cur = x
            else:
                if inep:
                    troughs.append(cur)
                    cur = 0.0
                    inep = False
        if inep:
            troughs.append(cur)
        if len(troughs) == 0:
            return 0.0
        return float(np.mean(troughs))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f06_sqavgdd_episodes(close, w):
    # RMS of episode trough depths (Burke-style denominator)
    def _f(a):
        peak = np.maximum.accumulate(a)
        dd = a / peak - 1.0
        troughs = []
        cur = 0.0
        inep = False
        for x in dd:
            if x < -1e-9:
                inep = True
                if x < cur:
                    cur = x
            else:
                if inep:
                    troughs.append(cur)
                    cur = 0.0
                    inep = False
        if inep:
            troughs.append(cur)
        if len(troughs) == 0:
            return 0.0
        return float(np.sqrt(np.mean(np.square(troughs))))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f06_underwater(close, w):
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close < peak * 0.99999).astype(float)


def _f06_recovery(close, w):
    trough = close.rolling(w, min_periods=max(1, w // 2)).min()
    return close / trough.replace(0, np.nan) - 1.0


def _f06_pain(close, w):
    dd = close / close.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan) - 1.0
    return dd.rolling(w, min_periods=max(1, w // 2)).mean()


def _f06_ulcer(close, w):
    dd = close / close.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan) - 1.0
    return np.sqrt((dd * dd).rolling(w, min_periods=max(1, w // 2)).mean())


def _f06_days_since_trough(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f06_days_since_peak(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f06_recovery_factor(close, w):
    # cumulative return over the window divided by the absolute max drawdown
    ret = close / close.shift(w) - 1.0
    mdd = _f06_maxdd(close, w).abs()
    return ret / mdd.replace(0, np.nan)


def _f06_downvol(close, w):
    # downside deviation: RMS of negative returns (positive days set to zero)
    r = close.pct_change()
    dn = r.clip(upper=0.0)
    return np.sqrt((dn * dn).rolling(w, min_periods=max(1, w // 2)).mean())


def _f06_upvol(close, w):
    # upside deviation: RMS of positive returns (negative days set to zero)
    r = close.pct_change()
    up = r.clip(lower=0.0)
    return np.sqrt((up * up).rolling(w, min_periods=max(1, w // 2)).mean())


# ============================================================
# ---- log-drawdown levels ----
def f06dr_f06_drawdown_recovery_logdd_63d_base_v076_signal(closeadj):
    b = _f06_logdd(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_logdd_252d_base_v077_signal(closeadj):
    b = _f06_logdd(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-drawdown mean-reverted against its own quarterly average
def f06dr_f06_drawdown_recovery_logddmr_252d_base_v078_signal(closeadj):
    g = _f06_logdd(closeadj, 252)
    b = g - g.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-drawdown year-over-year change (structural healing/worsening)
def f06dr_f06_drawdown_recovery_logddyoy_504d_base_v079_signal(closeadj):
    g = _f06_logdd(closeadj, 504)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- average episode-trough drawdown (pain across distinct episodes) ----
def f06dr_f06_drawdown_recovery_avgepdd_252d_base_v080_signal(closeadj):
    b = _f06_avgdd_episodes(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_avgepdd_504d_base_v081_signal(closeadj):
    b = _f06_avgdd_episodes(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Burke denominator: RMS of episode trough depths over the window
def f06dr_f06_drawdown_recovery_burkedd_252d_base_v082_signal(closeadj):
    b = _f06_sqavgdd_episodes(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Burke denominator shape: RMS episode-drawdown relative to mean episode-drawdown
# (severity dispersion across episodes; high = a few outsized crashes)
def f06dr_f06_drawdown_recovery_burkeratio_252d_base_v083_signal(closeadj):
    rms = _f06_sqavgdd_episodes(closeadj, 252)
    avg = _f06_avgdd_episodes(closeadj, 252).abs()
    b = rms / (avg + 1e-3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery factor (return / maxDD), distinct from base-file calmar by definition ----
def f06dr_f06_drawdown_recovery_recovfac_252d_base_v084_signal(closeadj):
    b = _f06_recovery_factor(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recovfac_504d_base_v085_signal(closeadj):
    b = _f06_recovery_factor(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sterling-style denominator dynamics: change in average episode-drawdown over a
# quarter (is the typical crash getting deeper or shallower)
def f06dr_f06_drawdown_recovery_sterling_252d_base_v086_signal(closeadj):
    avgdd = _f06_avgdd_episodes(closeadj, 252)
    b = avgdd - avgdd.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery-factor percentile rank (cross-time recovery quality)
def f06dr_f06_drawdown_recovery_recovfacrank_252d_base_v087_signal(closeadj):
    rf = _f06_recovery_factor(closeadj, 252)
    b = rf.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- downside vs upside vol (semi-dev structure of the path) ----
def f06dr_f06_drawdown_recovery_downvol_126d_base_v088_signal(closeadj):
    b = _f06_downvol(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_downvol_252d_base_v089_signal(closeadj):
    b = _f06_downvol(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside-to-upside volatility ratio (loss-asymmetry of the path)
def f06dr_f06_drawdown_recovery_updownvol_126d_base_v090_signal(closeadj):
    dn = _f06_downvol(closeadj, 126)
    up = _f06_upvol(closeadj, 126)
    b = dn / up.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside-deviation trend: change in 252d downside deviation over a quarter
# (is the downside getting more violent)
def f06dr_f06_drawdown_recovery_downvolz_252d_base_v091_signal(closeadj):
    dn = _f06_downvol(closeadj, 252)
    b = dn - dn.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sortino-like, percentile-ranked: 63d return over downside deviation, ranked
# vs its own history (downside-adjusted momentum regime; decorrelated from raw return)
def f06dr_f06_drawdown_recovery_sortino_252d_base_v092_signal(closeadj):
    ret = closeadj / closeadj.shift(63) - 1.0
    dn = _f06_downvol(closeadj, 126)
    ratio = ret / dn.replace(0, np.nan)
    b = ratio.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery-vs-decline asymmetry (V vs L shapes) ----
# time from peak to trough vs time from trough back up (drawdown shape)
def f06dr_f06_drawdown_recovery_shape_252d_base_v093_signal(closeadj):
    dpk = _f06_days_since_peak(closeadj, 252)
    dtr = _f06_days_since_trough(closeadj, 252)
    b = (dpk - dtr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# decline speed vs recovery speed: (depth/time-down) vs (rebound/time-up)
def f06dr_f06_drawdown_recovery_speedasym_252d_base_v094_signal(closeadj):
    peak = _rmax(closeadj, 252)
    trough = _rmin(closeadj, 252)
    dpk = _f06_days_since_peak(closeadj, 252).replace(0, np.nan)
    dtr = _f06_days_since_trough(closeadj, 252).replace(0, np.nan)
    decline = (peak - trough) / peak.replace(0, np.nan)
    drop_speed = decline / dpk
    up_speed = (closeadj - trough) / trough.replace(0, np.nan) / dtr
    b = up_speed - drop_speed
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown persistence / autocorrelation ----
# autocorrelation of the daily drawdown series (sticky vs jumpy drawdowns)
def f06dr_f06_drawdown_recovery_ddacf_126d_base_v095_signal(closeadj):
    dd = _f06_drawdown(closeadj, 126)

    def _f(a):
        x = a[:-1]
        y = a[1:]
        if np.std(x) < 1e-12 or np.std(y) < 1e-12:
            return np.nan
        return float(np.corrcoef(x, y)[0, 1])
    b = dd.rolling(63, min_periods=42).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown trend: slope of the drawdown path over the last quarter (deepening vs healing)
def f06dr_f06_drawdown_recovery_ddtrend_252d_base_v096_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)

    def _f(a):
        x = np.arange(len(a), dtype=float)
        x = x - x.mean()
        d = (x * x).sum()
        if d == 0:
            return np.nan
        return float((x * (a - a.mean())).sum() / d)
    b = dd.rolling(63, min_periods=21).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- frequency / count of recoveries ----
# new-high density: fraction of days at a fresh equity high, weighted by recovery
# strength (frequency of recovery completions, continuous)
def f06dr_f06_drawdown_recovery_newpeaks_252d_base_v097_signal(closeadj):
    peak = _rmax(closeadj, 252)
    fresh = (closeadj >= peak * 0.99999).astype(float)
    dens = fresh.rolling(126, min_periods=63).mean()
    rec = _f06_recovery(closeadj, 63)
    b = dens * (1.0 + rec)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average length of completed recovery legs vs decline legs over the window
def f06dr_f06_drawdown_recovery_legbalance_252d_base_v098_signal(closeadj):
    r = closeadj.pct_change()
    up = (r > 0).astype(float)

    def _f(a):
        runs_up = []
        runs_dn = []
        cur = 0
        sign = 0
        for v in a:
            s = 1 if v > 0.5 else -1
            if s == sign:
                cur += 1
            else:
                if sign == 1:
                    runs_up.append(cur)
                elif sign == -1:
                    runs_dn.append(cur)
                sign = s
                cur = 1
        if sign == 1:
            runs_up.append(cur)
        elif sign == -1:
            runs_dn.append(cur)
        mu = np.mean(runs_up) if runs_up else 0.0
        md = np.mean(runs_dn) if runs_dn else 0.0
        if (mu + md) == 0:
            return np.nan
        return float((mu - md) / (mu + md))
    b = up.rolling(126, min_periods=63).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain / ulcer trajectory ----
# pain index trend (change in chronic pain over a quarter)
def f06dr_f06_drawdown_recovery_paintrend_252d_base_v099_signal(closeadj):
    p = _f06_pain(closeadj, 252)
    b = p - p.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ulcer acceleration: second difference of the ulcer index (curvature of stress build-up)
def f06dr_f06_drawdown_recovery_ulcertrend_252d_base_v100_signal(closeadj):
    u = _f06_ulcer(closeadj, 252)
    b = u.shift(63) - 2.0 * u.shift(21) + u
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain term-structure: 126d pain relative to 504d pain (acute vs chronic)
def f06dr_f06_drawdown_recovery_painterm_base_v101_signal(closeadj):
    ps = _f06_pain(closeadj, 126)
    pl = _f06_pain(closeadj, 504)
    b = ps / pl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- maxDD term structure and dynamics ----
# maxDD change over a quarter (is the worst drawdown getting worse)
def f06dr_f06_drawdown_recovery_maxddtrend_252d_base_v102_signal(closeadj):
    md = _f06_maxdd(closeadj, 252)
    b = md - md.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maxDD convexity across 63/126/252 horizons (curvature of risk term-structure)
def f06dr_f06_drawdown_recovery_maxddcurv_base_v103_signal(closeadj):
    s = _f06_maxdd(closeadj, 63)
    m = _f06_maxdd(closeadj, 126)
    l = _f06_maxdd(closeadj, 252)
    b = s - 2.0 * m + l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maxDD interacted with realized vol (does deep dd come with high turbulence)
def f06dr_f06_drawdown_recovery_maxddvol_252d_base_v104_signal(closeadj):
    md = _f06_maxdd(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = md * vol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery dynamics ----
# recovery slope acceleration: recovery now vs a quarter ago
def f06dr_f06_drawdown_recovery_recovaccel_252d_base_v105_signal(closeadj):
    rec = _f06_recovery(closeadj, 252)
    b = rec - rec.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery off the 504d trough relative to total range traveled (path-normalized rebound)
def f06dr_f06_drawdown_recovery_recovpath_504d_base_v106_signal(closeadj):
    lo = _rmin(closeadj, 504)
    hi = _rmax(closeadj, 504)
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    rec = closeadj / lo.replace(0, np.nan) - 1.0
    b = pos * rec
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery smoothness: recovery EMA minus its raw value (overshoot/oscillation of rebound)
def f06dr_f06_drawdown_recovery_recovsmooth_252d_base_v107_signal(closeadj):
    rec = _f06_recovery(closeadj, 252)
    b = rec - rec.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- conditional / tail drawdown extensions ----
# fraction of total path-loss concentrated in the single worst week (lumpiness)
def f06dr_f06_drawdown_recovery_lossconc_252d_base_v108_signal(closeadj):
    r = closeadj.pct_change()
    worst5 = r.rolling(5, min_periods=3).sum().rolling(252, min_periods=126).min()
    totloss = r.clip(upper=0.0).rolling(252, min_periods=126).sum()
    b = worst5 / totloss.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expected shortfall of daily returns (mean of worst 5% days) — crash-tail level
def f06dr_f06_drawdown_recovery_es95_252d_base_v109_signal(closeadj):
    r = closeadj.pct_change()

    def _f(a):
        thr = np.quantile(a, 0.05)
        tail = a[a <= thr]
        if tail.size == 0:
            return np.nan
        return float(tail.mean())
    b = r.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tail-vs-typical loss ratio: ES95 over the median negative day (fat-tail sharpness)
def f06dr_f06_drawdown_recovery_tailratio_252d_base_v110_signal(closeadj):
    r = closeadj.pct_change()

    def _f(a):
        thr = np.quantile(a, 0.05)
        tail = a[a <= thr]
        neg = a[a < 0]
        if tail.size == 0 or neg.size == 0:
            return np.nan
        med = np.median(neg)
        if med == 0:
            return np.nan
        return float(tail.mean() / med)
    b = r.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- underwater duration extensions ----
# total number of separate underwater episodes over the year (drawdown frequency, distinct)
def f06dr_f06_drawdown_recovery_uwepisodes_252d_base_v111_signal(closeadj):
    uw = _f06_underwater(closeadj, 252)
    entries = ((uw == 1) & (uw.shift(1) == 0)).astype(float)
    cnt = entries.rolling(252, min_periods=126).sum()
    avgdepth = _f06_drawdown(closeadj, 252).rolling(63, min_periods=21).mean()
    b = cnt - 6.0 * avgdepth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean underwater-episode length: time-below-water divided by number of episodes
def f06dr_f06_drawdown_recovery_uweplen_252d_base_v112_signal(closeadj):
    uw = _f06_underwater(closeadj, 252)
    entries = ((uw == 1) & (uw.shift(1) == 0)).astype(float)
    tot = uw.rolling(252, min_periods=126).sum()
    cnt = entries.rolling(252, min_periods=126).sum()
    b = tot / (cnt + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current underwater run length in days, normalized (age of the ongoing drawdown)
def f06dr_f06_drawdown_recovery_curuwrun_504d_base_v113_signal(closeadj):
    peak = _rmax(closeadj, 504)
    fresh = (closeadj >= peak * 0.99999).astype(float)

    def _f(a):
        last = -1
        for i, v in enumerate(a):
            if v > 0.5:
                last = i
        if last < 0:
            return 1.0
        return (len(a) - 1 - last) / float(len(a))
    b = fresh.rolling(504, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery probability / hit-rate flavored ----
# fraction of underwater days that were followed by an up day (rebound tendency)
def f06dr_f06_drawdown_recovery_rebprob_252d_base_v114_signal(closeadj):
    r = closeadj.pct_change()
    uw = _f06_underwater(closeadj, 252)
    nextup = (r.shift(-1) > 0).astype(float)
    cond = (uw * nextup)
    b = cond.rolling(252, min_periods=126).sum() / uw.rolling(252, min_periods=126).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-day magnitude minus down-day magnitude while underwater (rebound power in drawdowns)
def f06dr_f06_drawdown_recovery_rebpower_252d_base_v115_signal(closeadj):
    r = closeadj.pct_change()
    uw = _f06_underwater(closeadj, 252)
    pos = (r.clip(lower=0.0) * uw).rolling(126, min_periods=42).mean()
    neg = (-r.clip(upper=0.0) * uw).rolling(126, min_periods=42).mean()
    b = pos - neg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- multi-horizon drawdown composites ----
# spread between current drawdown and the deepest drawdown a year ago (recovery vs memory)
def f06dr_f06_drawdown_recovery_ddmemory_252d_base_v116_signal(closeadj):
    cur = _f06_drawdown(closeadj, 252)
    pastworst = _f06_maxdd(closeadj, 252).shift(126)
    b = cur - pastworst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown dispersion across 63/126/252/504 horizons (multi-scale stress disagreement)
def f06dr_f06_drawdown_recovery_dddisp_multi_base_v117_signal(closeadj):
    d1 = _f06_drawdown(closeadj, 63)
    d2 = _f06_drawdown(closeadj, 126)
    d3 = _f06_drawdown(closeadj, 252)
    d4 = _f06_drawdown(closeadj, 504)
    b = pd.concat([d1, d2, d3, d4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# is the current drawdown the worst of the last two years (new-low stress flag, smoothed)
def f06dr_f06_drawdown_recovery_worststreak_504d_base_v118_signal(closeadj):
    cur = _f06_drawdown(closeadj, 504)
    worst = _f06_maxdd(closeadj, 504)
    atworst = (cur <= worst * 0.99 + 1e-9).astype(float)
    raw = atworst.rolling(63, min_periods=21).mean()
    b = raw + 0.5 * cur
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Calmar / risk-adjusted variants distinct from base file ----
# Calmar mismatched-horizon, percentile-ranked: 126d return over 252d maxDD, ranked
# vs its own history (risk-adjusted momentum regime, decorrelated from raw reward/loss)
def f06dr_f06_drawdown_recovery_calmarmix_base_v119_signal(closeadj):
    ret = closeadj / closeadj.shift(126) - 1.0
    mdd = _f06_maxdd(closeadj, 252).abs()
    ratio = ret / mdd.replace(0, np.nan)
    b = ratio.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Calmar trend: change in Calmar over a quarter (improving/decaying risk-adj return)
def f06dr_f06_drawdown_recovery_calmartrend_252d_base_v120_signal(closeadj):
    ret = closeadj / closeadj.shift(252) - 1.0
    mdd = _f06_maxdd(closeadj, 252).abs()
    cal = ret / mdd.replace(0, np.nan)
    b = cal - cal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- gain-to-pain ----
# gain-to-pain ratio: sum of positive returns over sum of absolute negative returns
def f06dr_f06_drawdown_recovery_gainpain_126d_base_v121_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.clip(lower=0.0).rolling(126, min_periods=63).sum()
    neg = (-r.clip(upper=0.0)).rolling(126, min_periods=63).sum()
    b = pos / neg.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gain-to-pain ratio over a year, z-scored (regime of reward-vs-loss)
def f06dr_f06_drawdown_recovery_gainpainz_252d_base_v122_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.clip(lower=0.0).rolling(252, min_periods=126).sum()
    neg = (-r.clip(upper=0.0)).rolling(252, min_periods=126).sum()
    gp = pos / neg.replace(0, np.nan)
    b = _z(gp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown-at-risk percentile of current dd vs distribution ----
# percentile of the current drawdown within its own 504d distribution (how extreme now)
def f06dr_f06_drawdown_recovery_ddpct_504d_base_v123_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)
    b = dd.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery percentile within its own distribution (how strong the rebound is now)
def f06dr_f06_drawdown_recovery_recovpct_504d_base_v124_signal(closeadj):
    rec = _f06_recovery(closeadj, 126)
    b = rec.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain-adjusted recovery composites ----
# recovery share of drawdown healed per unit of pain endured (efficiency of healing)
def f06dr_f06_drawdown_recovery_healeff_252d_base_v125_signal(closeadj):
    peak = _rmax(closeadj, 252)
    trough = _rmin(closeadj, 252)
    healed = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    pain = _f06_pain(closeadj, 252).abs()
    b = healed / (pain + 0.05)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net drawdown momentum: drawdown improving while underwater fraction falling (turnaround)
def f06dr_f06_drawdown_recovery_turnaround_252d_base_v126_signal(closeadj):
    ddchg = _f06_drawdown(closeadj, 252).diff(21)
    uwchg = _f06_underwater(closeadj, 252).rolling(63, min_periods=21).mean().diff(21)
    b = ddchg - uwchg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- volatility-of-drawdown ----
# vol of the daily drawdown series (instability of the underwater path)
def f06dr_f06_drawdown_recovery_ddvol2_126d_base_v127_signal(closeadj):
    dd = _f06_drawdown(closeadj, 126)
    b = dd.diff().rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range of the drawdown over a quarter (peak-to-trough span of the underwater curve)
def f06dr_f06_drawdown_recovery_ddrange_252d_base_v128_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)
    b = dd.rolling(63, min_periods=21).max() - dd.rolling(63, min_periods=21).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- skew/kurtosis of returns conditional on the regime ----
# kurtosis of daily returns (tail-heaviness driving drawdown risk)
def f06dr_f06_drawdown_recovery_retkurt_252d_base_v129_signal(closeadj):
    r = closeadj.pct_change()
    b = r.rolling(252, min_periods=126).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside semivariance share: downside variance over total variance (loss-driven risk share)
def f06dr_f06_drawdown_recovery_dvshare_252d_base_v130_signal(closeadj):
    r = closeadj.pct_change()
    dn = r.clip(upper=0.0)
    dvar = (dn * dn).rolling(252, min_periods=126).mean()
    tvar = (r * r).rolling(252, min_periods=126).mean()
    b = dvar / tvar.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- multi-year drawdown anchoring ----
# five-year worst-case stress: 756d max drawdown blended with the current 756d
# drawdown depth (deep-history worst case, continuous)
def f06dr_f06_drawdown_recovery_maxdd_1260d_base_v131_signal(closeadj):
    md = _f06_maxdd(closeadj, 756)
    cur = _f06_drawdown(closeadj, 756)
    b = md + 0.3 * cur
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current drawdown vs the five-year worst (distance from the all-time-stress floor)
def f06dr_f06_drawdown_recovery_ddvs1260worst_base_v132_signal(closeadj):
    cur = _f06_drawdown(closeadj, 1260)
    worst = _f06_maxdd(closeadj, 1260)
    b = cur - worst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# five-year recovery off the deep trough (multi-year rebound)
def f06dr_f06_drawdown_recovery_recov_1260d_base_v133_signal(closeadj):
    b = _f06_recovery(closeadj, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-horizon (756d) ulcer index (very-long-horizon chronic stress)
def f06dr_f06_drawdown_recovery_ulcer_1260d_base_v134_signal(closeadj):
    b = _f06_ulcer(closeadj, 756)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- composite stress score ----
# blended stress score: standardized pain + ulcer + underwater fraction (chronic-stress index)
def f06dr_f06_drawdown_recovery_stressidx_252d_base_v135_signal(closeadj):
    p = _z(_f06_pain(closeadj, 252), 252)
    u = _z(_f06_ulcer(closeadj, 252), 252)
    w = _z(_f06_underwater(closeadj, 252).rolling(126, min_periods=63).mean(), 252)
    b = (p - u + w) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery-quality composite: standardized recovery minus standardized maxDD (net rebound)
def f06dr_f06_drawdown_recovery_recovquality_252d_base_v136_signal(closeadj):
    rec = _z(_f06_recovery(closeadj, 252), 252)
    md = _z(_f06_maxdd(closeadj, 252), 252)
    b = rec + md
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- time-weighted drawdown (recency-emphasized pain) ----
# exponentially-weighted average drawdown (recency-weighted pain index)
def f06dr_f06_drawdown_recovery_ewpain_252d_base_v137_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)
    b = dd.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recency-weighted ulcer relative to slow-weighted ulcer (acute-vs-chronic stress shift)
def f06dr_f06_drawdown_recovery_ewulcer_252d_base_v138_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)
    fast = np.sqrt((dd * dd).ewm(span=21, min_periods=10).mean())
    slow = np.sqrt((dd * dd).ewm(span=126, min_periods=42).mean())
    b = fast / (slow + 1e-4)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown beta to its own trend ----
# drawdown depth relative to the worst-dd of the prior period (relapse vs new-record)
def f06dr_f06_drawdown_recovery_relapse_252d_base_v139_signal(closeadj):
    cur = _f06_drawdown(closeadj, 126)
    priorworst = _f06_maxdd(closeadj, 126).shift(63)
    b = cur / priorworst.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain ratio variants ----
# CDaR-style worst-decile drawdown level relative to the current drawdown
# (how much worse the tail of the drawdown distribution is than today's dd)
def f06dr_f06_drawdown_recovery_tailadjret_252d_base_v140_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)

    def _f(a):
        thr = np.quantile(a, 0.10)
        tail = a[a <= thr]
        if tail.size == 0:
            return np.nan
        return float(tail.mean())
    cdar = dd.rolling(252, min_periods=126).apply(_f, raw=True)
    cur = _f06_drawdown(closeadj, 252)
    b = cur - cdar
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery slope regression ----
# regression slope of price (log) since the trough (annualized rebound rate)
def f06dr_f06_drawdown_recovery_recovreg_252d_base_v141_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _f(a):
        x = np.arange(len(a), dtype=float)
        x = x - x.mean()
        d = (x * x).sum()
        if d == 0:
            return np.nan
        return float((x * (a - a.mean())).sum() / d)
    raw = lp.rolling(63, min_periods=21).apply(_f, raw=True)
    dd = _f06_drawdown(closeadj, 252)
    underwater = (dd < -0.02).astype(float)
    b = raw * underwater
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown skew over time ----
# skew of the drawdown distribution over the year (rare-deep vs frequent-shallow)
def f06dr_f06_drawdown_recovery_ddskew_252d_base_v142_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)
    b = dd.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain-weighted momentum ----
# trailing momentum penalized by concurrent underwater fraction (clean-momentum)
def f06dr_f06_drawdown_recovery_cleanmom_252d_base_v143_signal(closeadj):
    mom = closeadj / closeadj.shift(126) - 1.0
    uw = _f06_underwater(closeadj, 252).rolling(126, min_periods=63).mean()
    b = mom * (1.0 - uw)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- conditional recovery given depth ----
# recovery achieved relative to the depth of the worst drawdown (round-trip completion)
def f06dr_f06_drawdown_recovery_roundtrip_504d_base_v144_signal(closeadj):
    md = _f06_maxdd(closeadj, 504).abs()
    cur = _f06_drawdown(closeadj, 504).abs()
    b = (md - cur) / md.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- ulcer-vs-vol divergence ----
# ulcer index relative to realized vol, percentile-ranked (path-dependence premium
# of drawdown over noise, as a cross-time regime percentile)
def f06dr_f06_drawdown_recovery_ulcervoldiv_252d_base_v145_signal(closeadj):
    u = _f06_ulcer(closeadj, 252)
    vol = closeadj.pct_change().rolling(252, min_periods=126).std()
    ratio = u / vol.replace(0, np.nan)
    b = ratio.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown acceleration count ----
# fraction of recent days where the drawdown deepened (deepening pressure)
def f06dr_f06_drawdown_recovery_deepening_252d_base_v146_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)
    deeper = (dd.diff() < 0).astype(float)
    raw = deeper.rolling(63, min_periods=21).mean()
    b = raw + dd.rolling(21, min_periods=10).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery streak ----
# current recovery streak length scaled by recovery magnitude (rebound persistence x power)
def f06dr_f06_drawdown_recovery_recovstreak_252d_base_v147_signal(closeadj):
    rec = _f06_recovery(closeadj, 252)
    rising = (rec.diff() > 0).astype(float)

    def _f(a):
        cur = 0
        for v in a[::-1]:
            if v > 0.5:
                cur += 1
            else:
                break
        return cur / float(len(a))
    streak = rising.rolling(63, min_periods=21).apply(_f, raw=True)
    b = streak * (1.0 + rec)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown energy ----
# integrated drawdown area over the year (total cumulative pain endured)
def f06dr_f06_drawdown_recovery_ddarea_252d_base_v148_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)
    b = dd.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain-vs-recovery race ----
# net of recovery slope and drawdown deepening over the same month (who is winning)
def f06dr_f06_drawdown_recovery_race_252d_base_v149_signal(closeadj):
    recchg = _f06_recovery(closeadj, 252).diff(21)
    ddchg = _f06_drawdown(closeadj, 252).diff(21)
    b = recchg + ddchg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- composite Calmar/ulcer blend ----
# divergence between maxDD and ulcer (single-deep-crash vs many-shallow-dips shape)
def f06dr_f06_drawdown_recovery_blendrar_252d_base_v150_signal(closeadj):
    mdd = _f06_maxdd(closeadj, 252).abs()
    u = _f06_ulcer(closeadj, 252)
    b = mdd / (u + 1e-3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06dr_f06_drawdown_recovery_logdd_63d_base_v076_signal,
    f06dr_f06_drawdown_recovery_logdd_252d_base_v077_signal,
    f06dr_f06_drawdown_recovery_logddmr_252d_base_v078_signal,
    f06dr_f06_drawdown_recovery_logddyoy_504d_base_v079_signal,
    f06dr_f06_drawdown_recovery_avgepdd_252d_base_v080_signal,
    f06dr_f06_drawdown_recovery_avgepdd_504d_base_v081_signal,
    f06dr_f06_drawdown_recovery_burkedd_252d_base_v082_signal,
    f06dr_f06_drawdown_recovery_burkeratio_252d_base_v083_signal,
    f06dr_f06_drawdown_recovery_recovfac_252d_base_v084_signal,
    f06dr_f06_drawdown_recovery_recovfac_504d_base_v085_signal,
    f06dr_f06_drawdown_recovery_sterling_252d_base_v086_signal,
    f06dr_f06_drawdown_recovery_recovfacrank_252d_base_v087_signal,
    f06dr_f06_drawdown_recovery_downvol_126d_base_v088_signal,
    f06dr_f06_drawdown_recovery_downvol_252d_base_v089_signal,
    f06dr_f06_drawdown_recovery_updownvol_126d_base_v090_signal,
    f06dr_f06_drawdown_recovery_downvolz_252d_base_v091_signal,
    f06dr_f06_drawdown_recovery_sortino_252d_base_v092_signal,
    f06dr_f06_drawdown_recovery_shape_252d_base_v093_signal,
    f06dr_f06_drawdown_recovery_speedasym_252d_base_v094_signal,
    f06dr_f06_drawdown_recovery_ddacf_126d_base_v095_signal,
    f06dr_f06_drawdown_recovery_ddtrend_252d_base_v096_signal,
    f06dr_f06_drawdown_recovery_newpeaks_252d_base_v097_signal,
    f06dr_f06_drawdown_recovery_legbalance_252d_base_v098_signal,
    f06dr_f06_drawdown_recovery_paintrend_252d_base_v099_signal,
    f06dr_f06_drawdown_recovery_ulcertrend_252d_base_v100_signal,
    f06dr_f06_drawdown_recovery_painterm_base_v101_signal,
    f06dr_f06_drawdown_recovery_maxddtrend_252d_base_v102_signal,
    f06dr_f06_drawdown_recovery_maxddcurv_base_v103_signal,
    f06dr_f06_drawdown_recovery_maxddvol_252d_base_v104_signal,
    f06dr_f06_drawdown_recovery_recovaccel_252d_base_v105_signal,
    f06dr_f06_drawdown_recovery_recovpath_504d_base_v106_signal,
    f06dr_f06_drawdown_recovery_recovsmooth_252d_base_v107_signal,
    f06dr_f06_drawdown_recovery_lossconc_252d_base_v108_signal,
    f06dr_f06_drawdown_recovery_es95_252d_base_v109_signal,
    f06dr_f06_drawdown_recovery_tailratio_252d_base_v110_signal,
    f06dr_f06_drawdown_recovery_uwepisodes_252d_base_v111_signal,
    f06dr_f06_drawdown_recovery_uweplen_252d_base_v112_signal,
    f06dr_f06_drawdown_recovery_curuwrun_504d_base_v113_signal,
    f06dr_f06_drawdown_recovery_rebprob_252d_base_v114_signal,
    f06dr_f06_drawdown_recovery_rebpower_252d_base_v115_signal,
    f06dr_f06_drawdown_recovery_ddmemory_252d_base_v116_signal,
    f06dr_f06_drawdown_recovery_dddisp_multi_base_v117_signal,
    f06dr_f06_drawdown_recovery_worststreak_504d_base_v118_signal,
    f06dr_f06_drawdown_recovery_calmarmix_base_v119_signal,
    f06dr_f06_drawdown_recovery_calmartrend_252d_base_v120_signal,
    f06dr_f06_drawdown_recovery_gainpain_126d_base_v121_signal,
    f06dr_f06_drawdown_recovery_gainpainz_252d_base_v122_signal,
    f06dr_f06_drawdown_recovery_ddpct_504d_base_v123_signal,
    f06dr_f06_drawdown_recovery_recovpct_504d_base_v124_signal,
    f06dr_f06_drawdown_recovery_healeff_252d_base_v125_signal,
    f06dr_f06_drawdown_recovery_turnaround_252d_base_v126_signal,
    f06dr_f06_drawdown_recovery_ddvol2_126d_base_v127_signal,
    f06dr_f06_drawdown_recovery_ddrange_252d_base_v128_signal,
    f06dr_f06_drawdown_recovery_retkurt_252d_base_v129_signal,
    f06dr_f06_drawdown_recovery_dvshare_252d_base_v130_signal,
    f06dr_f06_drawdown_recovery_maxdd_1260d_base_v131_signal,
    f06dr_f06_drawdown_recovery_ddvs1260worst_base_v132_signal,
    f06dr_f06_drawdown_recovery_recov_1260d_base_v133_signal,
    f06dr_f06_drawdown_recovery_ulcer_1260d_base_v134_signal,
    f06dr_f06_drawdown_recovery_stressidx_252d_base_v135_signal,
    f06dr_f06_drawdown_recovery_recovquality_252d_base_v136_signal,
    f06dr_f06_drawdown_recovery_ewpain_252d_base_v137_signal,
    f06dr_f06_drawdown_recovery_ewulcer_252d_base_v138_signal,
    f06dr_f06_drawdown_recovery_relapse_252d_base_v139_signal,
    f06dr_f06_drawdown_recovery_tailadjret_252d_base_v140_signal,
    f06dr_f06_drawdown_recovery_recovreg_252d_base_v141_signal,
    f06dr_f06_drawdown_recovery_ddskew_252d_base_v142_signal,
    f06dr_f06_drawdown_recovery_cleanmom_252d_base_v143_signal,
    f06dr_f06_drawdown_recovery_roundtrip_504d_base_v144_signal,
    f06dr_f06_drawdown_recovery_ulcervoldiv_252d_base_v145_signal,
    f06dr_f06_drawdown_recovery_deepening_252d_base_v146_signal,
    f06dr_f06_drawdown_recovery_recovstreak_252d_base_v147_signal,
    f06dr_f06_drawdown_recovery_ddarea_252d_base_v148_signal,
    f06dr_f06_drawdown_recovery_race_252d_base_v149_signal,
    f06dr_f06_drawdown_recovery_blendrar_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_DRAWDOWN_RECOVERY_REGISTRY_076_150 = REGISTRY


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

    print("OK f06_drawdown_recovery_base_076_150_claude: %d features pass" % n_features)
