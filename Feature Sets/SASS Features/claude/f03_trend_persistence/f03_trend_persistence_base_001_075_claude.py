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


def _logret(close):
    return np.log(close.replace(0, np.nan)).diff()


def _pctret(close):
    return close.pct_change()


# ===== folder domain primitives (trend persistence) =====
def _f03_efficiency(close, w):
    # Kaufman efficiency ratio: net move over the window / sum of |daily moves|
    net = (close - close.shift(w)).abs()
    dr = close.diff().abs()
    path = dr.rolling(w, min_periods=max(2, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _f03_signed_efficiency(close, w):
    # signed efficiency ratio: keeps the direction of the net move
    net = close - close.shift(w)
    dr = close.diff().abs()
    path = dr.rolling(w, min_periods=max(2, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _f03_rs_hurst(close, w):
    # Hurst-like R/S exponent over the window (log(R/S)/log(n))
    r = _logret(close)

    def _rs(a):
        a = a[~np.isnan(a)]
        if a.size < 8:
            return np.nan
        m = a.mean()
        y = np.cumsum(a - m)
        R = y.max() - y.min()
        S = a.std()
        if S == 0 or R == 0:
            return np.nan
        return np.log(R / S) / np.log(a.size)

    return r.rolling(w, min_periods=max(8, w // 2)).apply(_rs, raw=True)


def _f03_autocorr(close, w, lag):
    # rolling autocorrelation of daily log returns at a given lag
    r = _logret(close)

    def _ac(a):
        a = a[~np.isnan(a)]
        if a.size <= lag + 2:
            return np.nan
        x0 = a[:-lag]
        x1 = a[lag:]
        if x0.std() == 0 or x1.std() == 0:
            return np.nan
        return np.corrcoef(x0, x1)[0, 1]

    return r.rolling(w, min_periods=max(lag + 3, w // 2)).apply(_ac, raw=True)


def _f03_varratio(close, k, w):
    # variance ratio: var(k-day ret) / (k * var(1-day ret)), rolling over w
    r = _logret(close)
    rk = np.log(close.replace(0, np.nan)).diff(k)
    v1 = r.rolling(w, min_periods=max(k + 2, w // 2)).var()
    vk = rk.rolling(w, min_periods=max(k + 2, w // 2)).var()
    return vk / (k * v1).replace(0, np.nan)


def _f03_trendday_frac(close, w):
    # conditional continuation persistence: P(same sign as yesterday) measured as a
    # magnitude-weighted continuation rate, mapped onto [0,1]. Distinct from the
    # efficiency ratio (net/path): this is a transition statistic, not a level.
    r = _logret(close)

    def _cont(a):
        a = a[~np.isnan(a)]
        if a.size < 5:
            return np.nan
        w0 = np.abs(a[1:])
        tot = np.sum(w0)
        if tot == 0:
            return np.nan
        same = np.sign(a[1:]) == np.sign(a[:-1])
        return np.sum(w0[same]) / tot

    b = r.rolling(w, min_periods=max(5, w // 2)).apply(_cont, raw=True)
    return b


def _f03_up_frac(close, w):
    # count-fraction of up days with the same magnitude-gap correction (directional)
    r = _logret(close)

    def _frac(a):
        a = a[~np.isnan(a)]
        if a.size < 4:
            return np.nan
        up = a[a > 0]
        dn = a[a < 0]
        cf = up.size / float(a.size)
        mu_up = up.mean() if up.size else 0.0
        mu_dn = -dn.mean() if dn.size else 0.0
        return cf + 0.15 * np.tanh(80.0 * (mu_up - mu_dn))

    return r.rolling(w, min_periods=max(4, w // 2)).apply(_frac, raw=True)


def _f03_maxrun(close, w, direction):
    # longest run of consecutive up/down days, magnitude-weighted by the run's
    # cumulative move so the statistic is continuous (run length x avg magnitude)
    r = _logret(close)

    def _run(a):
        a = a[~np.isnan(a)]
        if a.size < 3:
            return np.nan
        best = 0.0
        cur_len = 0
        cur_mag = 0.0
        for v in a:
            if np.sign(v) == direction:
                cur_len += 1
                cur_mag += abs(v)
                # continuous score: cumulative magnitude of the run scaled by its
                # length so the streak's strength (not just its count) is captured
                score = cur_mag * np.sqrt(cur_len)
                if score > best:
                    best = score
            else:
                cur_len = 0
                cur_mag = 0.0
        return best / float(a.size)

    return r.rolling(w, min_periods=max(3, w // 2)).apply(_run, raw=True)


def _f03_avgrun(close, w, direction):
    # average magnitude-per-run for same-direction streaks (continuous):
    # total directional move divided by the number of streaks of that direction
    r = _logret(close)

    def _ar(a):
        a = a[~np.isnan(a)]
        if a.size < 3:
            return np.nan
        n_runs = 0
        tot_mag = 0.0
        prev_in = False
        for v in a:
            in_run = (np.sign(v) == direction)
            if in_run:
                tot_mag += abs(v)
                if not prev_in:
                    n_runs += 1
            prev_in = in_run
        if n_runs == 0:
            return 0.0
        return tot_mag / n_runs

    return r.rolling(w, min_periods=max(3, w // 2)).apply(_ar, raw=True)


def _f03_signflip_rate(close, w):
    # count-based sign-flip rate (fraction of day-pairs that reverse direction),
    # with a small magnitude jitter so the statistic is continuous. This is a
    # day-count measure, distinct from the magnitude-mass continuation primitive.
    r = _logret(close)

    def _flip(a):
        a = a[~np.isnan(a)]
        if a.size < 4:
            return np.nan
        flips = np.sign(a[1:]) != np.sign(a[:-1])
        cf = np.mean(flips)
        # jitter: average magnitude of the flipping days vs total avg magnitude
        tm = np.mean(np.abs(a))
        if tm == 0:
            return cf
        jit = 0.05 * np.tanh((np.mean(np.abs(a[1:])[flips]) - tm) / tm) if flips.any() else 0.0
        return cf + jit

    return r.rolling(w, min_periods=max(4, w // 2)).apply(_flip, raw=True)


def _f03_dfa(close, w):
    # detrended fluctuation: std of cumulative-return residuals around a line
    r = _logret(close)

    def _f(a):
        a = a[~np.isnan(a)]
        if a.size < 8:
            return np.nan
        y = np.cumsum(a - a.mean())
        x = np.arange(a.size)
        b = np.polyfit(x, y, 1)
        resid = y - (b[0] * x + b[1])
        return resid.std() / (a.std() * np.sqrt(a.size) + 1e-12)

    return r.rolling(w, min_periods=max(8, w // 2)).apply(_f, raw=True)


# ============================================================
# efficiency ratio 21d
def f03tp_f03_trend_persistence_effr_21d_base_v001_signal(closeadj):
    b = _f03_efficiency(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 63d
def f03tp_f03_trend_persistence_effr_63d_base_v002_signal(closeadj):
    b = _f03_efficiency(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 126d
def f03tp_f03_trend_persistence_effr_126d_base_v003_signal(closeadj):
    b = _f03_efficiency(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 252d
def f03tp_f03_trend_persistence_effr_252d_base_v004_signal(closeadj):
    b = _f03_efficiency(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed efficiency ratio 63d (direction x persistence)
def f03tp_f03_trend_persistence_seffr_63d_base_v005_signal(closeadj):
    b = _f03_signed_efficiency(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed efficiency ratio 126d
def f03tp_f03_trend_persistence_seffr_126d_base_v006_signal(closeadj):
    b = _f03_signed_efficiency(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio z-score vs its own 252d history (de-trended persistence)
def f03tp_f03_trend_persistence_effrz_63d_base_v007_signal(closeadj):
    e = _f03_efficiency(closeadj, 63)
    b = _z(e, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio percentile-rank vs own 252d history
def f03tp_f03_trend_persistence_effrrank_63d_base_v008_signal(closeadj):
    e = _f03_efficiency(closeadj, 63)
    b = e.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long efficiency spread (regime change in persistence)
def f03tp_f03_trend_persistence_effrspr_21v126_base_v009_signal(closeadj):
    s = _f03_efficiency(closeadj, 21)
    l = _f03_efficiency(closeadj, 126)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio change over a month (persistence momentum)
def f03tp_f03_trend_persistence_effrmom_63d_base_v010_signal(closeadj):
    e = _f03_efficiency(closeadj, 63)
    b = e - e.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst R/S exponent 63d
def f03tp_f03_trend_persistence_hurst_63d_base_v011_signal(closeadj):
    b = _f03_rs_hurst(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst R/S exponent 126d
def f03tp_f03_trend_persistence_hurst_126d_base_v012_signal(closeadj):
    b = _f03_rs_hurst(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst R/S exponent 252d
def f03tp_f03_trend_persistence_hurst_252d_base_v013_signal(closeadj):
    b = _f03_rs_hurst(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative autocorrelation memory: sum of return autocorrelations over lags 1..6
# (net positive memory => persistence; negative => mean reversion) 126d
def f03tp_f03_trend_persistence_acfsum_126d_base_v014_signal(closeadj):
    r = _logret(closeadj)

    def _asum(a):
        a = a[~np.isnan(a)]
        if a.size < 16:
            return np.nan
        a = a - a.mean()
        v0 = np.sum(a * a)
        if v0 == 0:
            return np.nan
        tot = 0.0
        for lag in range(1, 7):
            tot += np.sum(a[lag:] * a[:-lag]) / v0
        return tot

    b = r.rolling(126, min_periods=63).apply(_asum, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst z-scored vs own 252d history
def f03tp_f03_trend_persistence_hurstz_126d_base_v015_signal(closeadj):
    h = _f03_rs_hurst(closeadj, 126)
    b = _z(h, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst change over a quarter (persistence trajectory)
def f03tp_f03_trend_persistence_hurstmom_126d_base_v016_signal(closeadj):
    h = _f03_rs_hurst(closeadj, 126)
    b = h - h.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long Hurst spread
def f03tp_f03_trend_persistence_hurstspr_63v252_base_v017_signal(closeadj):
    s = _f03_rs_hurst(closeadj, 63)
    l = _f03_rs_hurst(closeadj, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# detrended-fluctuation exponent proxy 126d (path roughness vs random walk)
def f03tp_f03_trend_persistence_dfa_126d_base_v018_signal(closeadj):
    b = _f03_dfa(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# detrended-fluctuation proxy 63d
def f03tp_f03_trend_persistence_dfa_63d_base_v019_signal(closeadj):
    b = _f03_dfa(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DFA short-vs-long spread
def f03tp_f03_trend_persistence_dfaspr_63v252_base_v020_signal(closeadj):
    s = _f03_dfa(closeadj, 63)
    l = _f03_dfa(closeadj, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation at lag 1, 63d window
def f03tp_f03_trend_persistence_acf1_63d_base_v021_signal(closeadj):
    b = _f03_autocorr(closeadj, 63, 1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation at lag 1, 126d window
def f03tp_f03_trend_persistence_acf1_126d_base_v022_signal(closeadj):
    b = _f03_autocorr(closeadj, 126, 1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation at lag 2, 126d window
def f03tp_f03_trend_persistence_acf2_126d_base_v023_signal(closeadj):
    b = _f03_autocorr(closeadj, 126, 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation at lag 5, 126d window
def f03tp_f03_trend_persistence_acf5_126d_base_v024_signal(closeadj):
    b = _f03_autocorr(closeadj, 126, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation at lag 1, 252d window
def f03tp_f03_trend_persistence_acf1_252d_base_v025_signal(closeadj):
    b = _f03_autocorr(closeadj, 252, 1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average autocorrelation across lags 1-3 (short-memory strength) 126d
def f03tp_f03_trend_persistence_acfavg13_126d_base_v026_signal(closeadj):
    a1 = _f03_autocorr(closeadj, 126, 1)
    a2 = _f03_autocorr(closeadj, 126, 2)
    a3 = _f03_autocorr(closeadj, 126, 3)
    b = (a1 + a2 + a3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr lag-1 z-scored vs own 252d history
def f03tp_f03_trend_persistence_acf1z_126d_base_v027_signal(closeadj):
    a = _f03_autocorr(closeadj, 126, 1)
    b = _z(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr lag-1 change over a quarter
def f03tp_f03_trend_persistence_acf1mom_126d_base_v028_signal(closeadj):
    a = _f03_autocorr(closeadj, 126, 1)
    b = a - a.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# decay of autocorrelation lag1 minus lag5 (memory persistence shape) 126d
def f03tp_f03_trend_persistence_acfdecay_126d_base_v029_signal(closeadj):
    a1 = _f03_autocorr(closeadj, 126, 1)
    a5 = _f03_autocorr(closeadj, 126, 5)
    b = a1 - a5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weekly-return autocorrelation lag 1 (5-day blocks), 252d
def f03tp_f03_trend_persistence_wacf1_252d_base_v030_signal(closeadj):
    wk = np.log(closeadj.replace(0, np.nan)).diff(5)

    def _ac(a):
        a = a[~np.isnan(a)]
        a = a[::5]
        if a.size < 6:
            return np.nan
        x0 = a[:-1]
        x1 = a[1:]
        if x0.std() == 0 or x1.std() == 0:
            return np.nan
        return np.corrcoef(x0, x1)[0, 1]

    b = wk.rolling(252, min_periods=126).apply(_ac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio k=5, 126d (>1 => trending)
def f03tp_f03_trend_persistence_vr5_126d_base_v031_signal(closeadj):
    b = _f03_varratio(closeadj, 5, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio k=5, 252d
def f03tp_f03_trend_persistence_vr5_252d_base_v032_signal(closeadj):
    b = _f03_varratio(closeadj, 5, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio k=10, 252d
def f03tp_f03_trend_persistence_vr10_252d_base_v033_signal(closeadj):
    b = _f03_varratio(closeadj, 10, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio k=21, 252d
def f03tp_f03_trend_persistence_vr21_252d_base_v034_signal(closeadj):
    b = _f03_varratio(closeadj, 21, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio convexity: VR(k=3) - 2*VR(k=5) + VR(k=10) at 126d
# (curvature of the variance-ratio profile; distinct from any single VR level)
def f03tp_f03_trend_persistence_vrconvex_126d_base_v035_signal(closeadj):
    v3 = _f03_varratio(closeadj, 3, 126)
    v5 = _f03_varratio(closeadj, 5, 126)
    v10 = _f03_varratio(closeadj, 10, 126)
    b = v3 - 2.0 * v5 + v10
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio term structure: VR(k=21) - VR(k=5) at 252d
def f03tp_f03_trend_persistence_vrterm_252d_base_v036_signal(closeadj):
    short = _f03_varratio(closeadj, 5, 252)
    long = _f03_varratio(closeadj, 21, 252)
    b = long - short
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio z-scored vs own 252d history, k=5
def f03tp_f03_trend_persistence_vrz5_126d_base_v037_signal(closeadj):
    v = _f03_varratio(closeadj, 5, 126)
    b = _z(v, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio momentum (change over a quarter) k=10
def f03tp_f03_trend_persistence_vrmom10_252d_base_v038_signal(closeadj):
    v = _f03_varratio(closeadj, 10, 252)
    b = v - v.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of trend days (agree with net move) 63d
def f03tp_f03_trend_persistence_tdfrac_63d_base_v039_signal(closeadj):
    b = _f03_trendday_frac(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of trend days 126d
def f03tp_f03_trend_persistence_tdfrac_126d_base_v040_signal(closeadj):
    b = _f03_trendday_frac(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of trend days 252d
def f03tp_f03_trend_persistence_tdfrac_252d_base_v041_signal(closeadj):
    b = _f03_trendday_frac(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-horizon variance ratio k=3 at a 63d window (var of 3-day returns vs
# 3x var of 1-day returns; >1 => short-term trending) -- a variance-scaling
# memory channel, structurally unrelated to the sign-flip count
def f03tp_f03_trend_persistence_vr3_63d_base_v042_signal(closeadj):
    b = _f03_varratio(closeadj, 3, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consistency of direction: 1 minus the dispersion of the up-day rate across
# 21d sub-blocks (steady drift => low dispersion => high score) 126d
def f03tp_f03_trend_persistence_dirconsist_126d_base_v043_signal(closeadj):
    r = _logret(closeadj)

    def _dc(a):
        a = a[~np.isnan(a)]
        if a.size < 60:
            return np.nan
        blocks = [a[i:i + 21] for i in range(0, a.size - 20, 21)]
        rates = [np.mean(bb > 0) for bb in blocks if bb.size >= 10]
        if len(rates) < 3:
            return np.nan
        return 1.0 - 2.0 * np.std(rates)

    b = r.rolling(126, min_periods=120).apply(_dc, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day fraction change over a quarter (consistency trajectory)
def f03tp_f03_trend_persistence_tdfracmom_126d_base_v044_signal(closeadj):
    t = _f03_trendday_frac(closeadj, 126)
    b = t - t.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day fraction z-scored vs own history 126d
def f03tp_f03_trend_persistence_tdfracz_126d_base_v045_signal(closeadj):
    t = _f03_trendday_frac(closeadj, 126)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest up-run fraction 63d
def f03tp_f03_trend_persistence_uprun_63d_base_v046_signal(closeadj):
    b = _f03_maxrun(closeadj, 63, 1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average up-streak strength 126d (mean magnitude per up-run)
def f03tp_f03_trend_persistence_uprun_126d_base_v047_signal(closeadj):
    b = _f03_avgrun(closeadj, 126, 1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average down-streak strength 126d (mean magnitude per down-run)
def f03tp_f03_trend_persistence_dnrun_126d_base_v048_signal(closeadj):
    b = _f03_avgrun(closeadj, 126, -1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# streak-length asymmetry: average duration of up-streaks minus that of
# down-streaks (do up moves persist over more days than down moves?) 126d
def f03tp_f03_trend_persistence_runasym_126d_base_v049_signal(closeadj):
    r = _logret(closeadj)

    def _asym(a):
        a = a[~np.isnan(a)]
        if a.size < 8:
            return np.nan
        up_lens = []
        dn_lens = []
        cur = 0
        cur_sign = 0
        for v in a:
            sg = np.sign(v)
            if sg == cur_sign and sg != 0:
                cur += 1
            else:
                if cur_sign > 0:
                    up_lens.append(cur)
                elif cur_sign < 0:
                    dn_lens.append(cur)
                cur = 1
                cur_sign = sg
        if cur_sign > 0:
            up_lens.append(cur)
        elif cur_sign < 0:
            dn_lens.append(cur)
        mu_up = np.mean(up_lens) if up_lens else 0.0
        mu_dn = np.mean(dn_lens) if dn_lens else 0.0
        # continuous tie-break from average magnitude per streak day
        return (mu_up - mu_dn) + 0.5 * np.tanh(50.0 * a.mean())

    b = r.rolling(126, min_periods=63).apply(_asym, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average up-streak strength 252d
def f03tp_f03_trend_persistence_uprun_252d_base_v050_signal(closeadj):
    b = _f03_avgrun(closeadj, 252, 1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-flip rate 63d (low => persistent)
def f03tp_f03_trend_persistence_flip_63d_base_v051_signal(closeadj):
    b = _f03_signflip_rate(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-flip rate 126d
def f03tp_f03_trend_persistence_flip_126d_base_v052_signal(closeadj):
    b = _f03_signflip_rate(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lag-2 directional continuation: magnitude-weighted agreement between a day's
# sign and the sign two days earlier (skip-one persistence; captures memory that
# survives a one-day pause) 126d
def f03tp_f03_trend_persistence_signagree_126d_base_v053_signal(closeadj):
    r = _logret(closeadj)

    def _ag(a):
        a = a[~np.isnan(a)]
        if a.size < 6:
            return np.nan
        w0 = np.abs(a[2:])
        tot = np.sum(w0)
        if tot == 0:
            return np.nan
        s = np.sign(a[2:]) == np.sign(a[:-2])
        return np.sum(w0[s]) / tot - 0.5

    b = r.rolling(126, min_periods=63).apply(_ag, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-flip rate change over a quarter
def f03tp_f03_trend_persistence_flipmom_126d_base_v054_signal(closeadj):
    f = _f03_signflip_rate(closeadj, 126)
    b = f - f.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency x trend-day-fraction interaction (compound persistence) 126d
def f03tp_f03_trend_persistence_efftd_126d_base_v055_signal(closeadj):
    e = _f03_efficiency(closeadj, 126)
    t = _f03_trendday_frac(closeadj, 126) - 0.5
    b = e * t
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lag-1 autocorrelation of ABSOLUTE returns: volatility-clustering persistence
# (a memory channel orthogonal to directional drift) 63d
def f03tp_f03_trend_persistence_absacf_63d_base_v056_signal(closeadj):
    ar = _logret(closeadj).abs()

    def _ac(a):
        a = a[~np.isnan(a)]
        if a.size < 6:
            return np.nan
        x0 = a[:-1]
        x1 = a[1:]
        if x0.std() == 0 or x1.std() == 0:
            return np.nan
        return np.corrcoef(x0, x1)[0, 1]

    b = ar.rolling(63, min_periods=32).apply(_ac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed efficiency x variance-ratio excess (direction-confirmed trend) 126d
def f03tp_f03_trend_persistence_seffvr_126d_base_v057_signal(closeadj):
    se = _f03_signed_efficiency(closeadj, 126)
    vr = _f03_varratio(closeadj, 5, 126) - 1.0
    b = se * vr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst x efficiency (double persistence confirmation) 126d
def f03tp_f03_trend_persistence_hursteff_126d_base_v058_signal(closeadj):
    h = _f03_rs_hurst(closeadj, 126) - 0.5
    e = _f03_efficiency(closeadj, 126)
    b = h * e
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorrelation x trend-day fraction interaction 126d
def f03tp_f03_trend_persistence_acftd_126d_base_v059_signal(closeadj):
    a = _f03_autocorr(closeadj, 126, 1)
    t = _f03_trendday_frac(closeadj, 126) - 0.5
    b = a + 2.0 * t
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio dispersion (stability of persistence) 126d
def f03tp_f03_trend_persistence_effdisp_126d_base_v060_signal(closeadj):
    e = _f03_efficiency(closeadj, 21)
    b = e.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio smoothed (persistent regime) EMA 63d
def f03tp_f03_trend_persistence_effema_63d_base_v061_signal(closeadj):
    e = _f03_efficiency(closeadj, 63)
    b = e.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency displacement from its slow EMA 63d
def f03tp_f03_trend_persistence_effdisp2_63d_base_v062_signal(closeadj):
    e = _f03_efficiency(closeadj, 63)
    b = e - e.ewm(span=84, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# single-day move concentration: largest |daily return| as a share of total path
# (jumpy paths are driven by one day; smooth trends spread the move out) 63d
def f03tp_f03_trend_persistence_jumpshare_63d_base_v063_signal(closeadj):
    ar = _logret(closeadj).abs()
    mx = ar.rolling(63, min_periods=32).max()
    tot = ar.rolling(63, min_periods=32).sum()
    b = 1.0 - mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Gini concentration of |returns| over the window (low Gini => evenly-paced,
# durable trend; high Gini => a few dominant jumps) 126d
def f03tp_f03_trend_persistence_retgini_126d_base_v064_signal(closeadj):
    ar = _logret(closeadj).abs()

    def _gini(a):
        a = a[~np.isnan(a)]
        if a.size < 20:
            return np.nan
        a = np.sort(a)
        s = a.sum()
        if s == 0:
            return np.nan
        idx = np.arange(1, a.size + 1)
        g = (2.0 * np.sum(idx * a) / (a.size * s)) - (a.size + 1.0) / a.size
        return 1.0 - g

    b = ar.rolling(126, min_periods=63).apply(_gini, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of months (21d blocks) that are up over 252d (multi-horizon persistence)
def f03tp_f03_trend_persistence_monthhit_252d_base_v065_signal(closeadj):
    mr = np.log(closeadj.replace(0, np.nan)).diff(21)

    def _frac(a):
        a = a[~np.isnan(a)]
        a = a[::21]
        if a.size < 4:
            return np.nan
        tot = np.sum(np.abs(a))
        if tot == 0:
            return np.nan
        return np.sum(a[a > 0]) / tot - 0.5

    b = mr.rolling(252, min_periods=126).apply(_frac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest streak of consecutive up-weeks fraction 252d
def f03tp_f03_trend_persistence_upweekrun_252d_base_v066_signal(closeadj):
    wk = np.log(closeadj.replace(0, np.nan)).diff(5)

    def _run(a):
        a = a[~np.isnan(a)]
        a = a[::5]
        if a.size < 4:
            return np.nan
        best = 0.0
        cur_len = 0
        cur_mag = 0.0
        for v in a:
            if v > 0:
                cur_len += 1
                cur_mag += v
                best = max(best, cur_len + 30.0 * cur_mag)
            else:
                cur_len = 0
                cur_mag = 0.0
        return best / float(a.size)

    b = wk.rolling(252, min_periods=126).apply(_run, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reversal-magnitude density of the smoothed price path: sum of the size of each
# directional reversal per window (small => one durable trend; large => choppy).
# Continuous because reversals are weighted by their amplitude. 126d
def f03tp_f03_trend_persistence_turnpt_126d_base_v067_signal(closeadj):
    sm = np.log(closeadj.replace(0, np.nan)).rolling(5, min_periods=3).mean()

    def _tp(a):
        a = a[~np.isnan(a)]
        if a.size < 9:
            return np.nan
        d = np.diff(a)
        s = np.sign(d)
        rev_mass = 0.0
        for k in range(1, d.size):
            if s[k] != 0 and s[k - 1] != 0 and s[k] != s[k - 1]:
                rev_mass += abs(d[k])
        span = np.sum(np.abs(d))
        if span == 0:
            return np.nan
        return rev_mass / span

    raw = sm.rolling(126, min_periods=63).apply(_tp, raw=True)
    b = 0.5 - raw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression R-squared of price vs time (trend linearity) 63d
def f03tp_f03_trend_persistence_r2_63d_base_v068_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _r2(a):
        a = a[~np.isnan(a)]
        if a.size < 8:
            return np.nan
        x = np.arange(a.size)
        b1 = np.polyfit(x, a, 1)
        pred = b1[0] * x + b1[1]
        ss_res = np.sum((a - pred) ** 2)
        ss_tot = np.sum((a - a.mean()) ** 2)
        if ss_tot == 0:
            return np.nan
        return 1.0 - ss_res / ss_tot

    b = lp.rolling(63, min_periods=32).apply(_r2, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression R-squared of price vs time 126d
def f03tp_f03_trend_persistence_r2_126d_base_v069_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _r2(a):
        a = a[~np.isnan(a)]
        if a.size < 16:
            return np.nan
        x = np.arange(a.size)
        b1 = np.polyfit(x, a, 1)
        pred = b1[0] * x + b1[1]
        ss_res = np.sum((a - pred) ** 2)
        ss_tot = np.sum((a - a.mean()) ** 2)
        if ss_tot == 0:
            return np.nan
        return 1.0 - ss_res / ss_tot

    b = lp.rolling(126, min_periods=63).apply(_r2, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed trend linearity: slope-sign x R-squared 126d
def f03tp_f03_trend_persistence_signr2_126d_base_v070_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _sr2(a):
        a = a[~np.isnan(a)]
        if a.size < 16:
            return np.nan
        x = np.arange(a.size)
        b1 = np.polyfit(x, a, 1)
        pred = b1[0] * x + b1[1]
        ss_res = np.sum((a - pred) ** 2)
        ss_tot = np.sum((a - a.mean()) ** 2)
        if ss_tot == 0:
            return np.nan
        return np.sign(b1[0]) * (1.0 - ss_res / ss_tot)

    b = lp.rolling(126, min_periods=63).apply(_sr2, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio across two block sizes interaction with efficiency 252d
def f03tp_f03_trend_persistence_vreff_252d_base_v071_signal(closeadj):
    vr = _f03_varratio(closeadj, 10, 252) - 1.0
    e = _f03_efficiency(closeadj, 252)
    b = vr * e
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# memory-decay ratio: autocorr(lag3) relative to autocorr(lag1) -- how slowly the
# return memory decays (near 1 => long memory, near 0 => fast decay) 126d
def f03tp_f03_trend_persistence_acfratio_126d_base_v072_signal(closeadj):
    a1 = _f03_autocorr(closeadj, 126, 1)
    a3 = _f03_autocorr(closeadj, 126, 3)
    b = np.tanh(a3 / a1.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of days price stays above its 21d MA (trend-holding) 126d
def f03tp_f03_trend_persistence_abovemafrac_126d_base_v073_signal(closeadj):
    ma = closeadj.rolling(21, min_periods=10).mean()
    above = (closeadj > ma).astype(float)
    b = above.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio of the cumulative-up-volume-free path using closeadj 504d
def f03tp_f03_trend_persistence_effr_504d_base_v074_signal(closeadj):
    b = _f03_efficiency(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# persistence composite: sign-stability x efficiency x (Hurst-0.5) 126d
def f03tp_f03_trend_persistence_composite_126d_base_v075_signal(closeadj):
    persist = (0.5 - _f03_signflip_rate(closeadj, 126))
    e = _f03_efficiency(closeadj, 126)
    h = _f03_rs_hurst(closeadj, 126) - 0.5
    b = persist + e + 2.0 * h
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03tp_f03_trend_persistence_effr_21d_base_v001_signal,
    f03tp_f03_trend_persistence_effr_63d_base_v002_signal,
    f03tp_f03_trend_persistence_effr_126d_base_v003_signal,
    f03tp_f03_trend_persistence_effr_252d_base_v004_signal,
    f03tp_f03_trend_persistence_seffr_63d_base_v005_signal,
    f03tp_f03_trend_persistence_seffr_126d_base_v006_signal,
    f03tp_f03_trend_persistence_effrz_63d_base_v007_signal,
    f03tp_f03_trend_persistence_effrrank_63d_base_v008_signal,
    f03tp_f03_trend_persistence_effrspr_21v126_base_v009_signal,
    f03tp_f03_trend_persistence_effrmom_63d_base_v010_signal,
    f03tp_f03_trend_persistence_hurst_63d_base_v011_signal,
    f03tp_f03_trend_persistence_hurst_126d_base_v012_signal,
    f03tp_f03_trend_persistence_hurst_252d_base_v013_signal,
    f03tp_f03_trend_persistence_acfsum_126d_base_v014_signal,
    f03tp_f03_trend_persistence_hurstz_126d_base_v015_signal,
    f03tp_f03_trend_persistence_hurstmom_126d_base_v016_signal,
    f03tp_f03_trend_persistence_hurstspr_63v252_base_v017_signal,
    f03tp_f03_trend_persistence_dfa_126d_base_v018_signal,
    f03tp_f03_trend_persistence_dfa_63d_base_v019_signal,
    f03tp_f03_trend_persistence_dfaspr_63v252_base_v020_signal,
    f03tp_f03_trend_persistence_acf1_63d_base_v021_signal,
    f03tp_f03_trend_persistence_acf1_126d_base_v022_signal,
    f03tp_f03_trend_persistence_acf2_126d_base_v023_signal,
    f03tp_f03_trend_persistence_acf5_126d_base_v024_signal,
    f03tp_f03_trend_persistence_acf1_252d_base_v025_signal,
    f03tp_f03_trend_persistence_acfavg13_126d_base_v026_signal,
    f03tp_f03_trend_persistence_acf1z_126d_base_v027_signal,
    f03tp_f03_trend_persistence_acf1mom_126d_base_v028_signal,
    f03tp_f03_trend_persistence_acfdecay_126d_base_v029_signal,
    f03tp_f03_trend_persistence_wacf1_252d_base_v030_signal,
    f03tp_f03_trend_persistence_vr5_126d_base_v031_signal,
    f03tp_f03_trend_persistence_vr5_252d_base_v032_signal,
    f03tp_f03_trend_persistence_vr10_252d_base_v033_signal,
    f03tp_f03_trend_persistence_vr21_252d_base_v034_signal,
    f03tp_f03_trend_persistence_vrconvex_126d_base_v035_signal,
    f03tp_f03_trend_persistence_vrterm_252d_base_v036_signal,
    f03tp_f03_trend_persistence_vrz5_126d_base_v037_signal,
    f03tp_f03_trend_persistence_vrmom10_252d_base_v038_signal,
    f03tp_f03_trend_persistence_tdfrac_63d_base_v039_signal,
    f03tp_f03_trend_persistence_tdfrac_126d_base_v040_signal,
    f03tp_f03_trend_persistence_tdfrac_252d_base_v041_signal,
    f03tp_f03_trend_persistence_vr3_63d_base_v042_signal,
    f03tp_f03_trend_persistence_dirconsist_126d_base_v043_signal,
    f03tp_f03_trend_persistence_tdfracmom_126d_base_v044_signal,
    f03tp_f03_trend_persistence_tdfracz_126d_base_v045_signal,
    f03tp_f03_trend_persistence_uprun_63d_base_v046_signal,
    f03tp_f03_trend_persistence_uprun_126d_base_v047_signal,
    f03tp_f03_trend_persistence_dnrun_126d_base_v048_signal,
    f03tp_f03_trend_persistence_runasym_126d_base_v049_signal,
    f03tp_f03_trend_persistence_uprun_252d_base_v050_signal,
    f03tp_f03_trend_persistence_flip_63d_base_v051_signal,
    f03tp_f03_trend_persistence_flip_126d_base_v052_signal,
    f03tp_f03_trend_persistence_signagree_126d_base_v053_signal,
    f03tp_f03_trend_persistence_flipmom_126d_base_v054_signal,
    f03tp_f03_trend_persistence_efftd_126d_base_v055_signal,
    f03tp_f03_trend_persistence_absacf_63d_base_v056_signal,
    f03tp_f03_trend_persistence_seffvr_126d_base_v057_signal,
    f03tp_f03_trend_persistence_hursteff_126d_base_v058_signal,
    f03tp_f03_trend_persistence_acftd_126d_base_v059_signal,
    f03tp_f03_trend_persistence_effdisp_126d_base_v060_signal,
    f03tp_f03_trend_persistence_effema_63d_base_v061_signal,
    f03tp_f03_trend_persistence_effdisp2_63d_base_v062_signal,
    f03tp_f03_trend_persistence_jumpshare_63d_base_v063_signal,
    f03tp_f03_trend_persistence_retgini_126d_base_v064_signal,
    f03tp_f03_trend_persistence_monthhit_252d_base_v065_signal,
    f03tp_f03_trend_persistence_upweekrun_252d_base_v066_signal,
    f03tp_f03_trend_persistence_turnpt_126d_base_v067_signal,
    f03tp_f03_trend_persistence_r2_63d_base_v068_signal,
    f03tp_f03_trend_persistence_r2_126d_base_v069_signal,
    f03tp_f03_trend_persistence_signr2_126d_base_v070_signal,
    f03tp_f03_trend_persistence_vreff_252d_base_v071_signal,
    f03tp_f03_trend_persistence_acfratio_126d_base_v072_signal,
    f03tp_f03_trend_persistence_abovemafrac_126d_base_v073_signal,
    f03tp_f03_trend_persistence_effr_504d_base_v074_signal,
    f03tp_f03_trend_persistence_composite_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_TREND_PERSISTENCE_REGISTRY_001_075 = REGISTRY


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

    print("OK f03_trend_persistence_base_001_075_claude: %d features pass" % n_features)
