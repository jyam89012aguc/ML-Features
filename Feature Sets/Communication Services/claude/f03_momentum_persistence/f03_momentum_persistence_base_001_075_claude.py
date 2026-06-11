import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (momentum / trend persistence) =====
def _f03_ret(closeadj):
    # simple daily return
    return closeadj.pct_change()


def _f03_logret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f03_efficiency_ratio(closeadj, w):
    # Kaufman efficiency ratio: |net move| / total path length over window w
    net = (closeadj - closeadj.shift(w)).abs()
    path = closeadj.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _f03_signed_efficiency(closeadj, w):
    # signed efficiency: net move (with direction) / total path length
    net = closeadj - closeadj.shift(w)
    path = closeadj.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _f03_autocorr(closeadj, w, lag):
    # rolling autocorrelation of daily returns at given lag
    r = closeadj.pct_change()
    return r.rolling(w, min_periods=max(3, w // 2)).apply(
        lambda a: np.corrcoef(a[lag:], a[:-lag])[0, 1]
        if (np.std(a[lag:]) > 0 and np.std(a[:-lag]) > 0) else np.nan,
        raw=True,
    )


def _f03_hurst_rs(closeadj, w):
    # Hurst exponent via rescaled-range (R/S) over a single window of log returns
    lr = np.log(closeadj.replace(0, np.nan)).diff()

    def _rs(a):
        a = a[np.isfinite(a)]
        m = len(a)
        if m < 16:
            return np.nan
        mean = a.mean()
        dev = np.cumsum(a - mean)
        R = dev.max() - dev.min()
        S = a.std()
        if S <= 0 or R <= 0:
            return np.nan
        # two scales: full window and half window -> slope of log(R/S) vs log(n)
        half = m // 2
        a1, a2 = a[:half], a[half:]
        rs_full = R / S
        out = [np.log(rs_full) / np.log(m)]
        for sub in (a1, a2):
            mn = sub.mean()
            dv = np.cumsum(sub - mn)
            Rh = dv.max() - dv.min()
            Sh = sub.std()
            if Sh > 0 and Rh > 0:
                out.append(np.log(Rh / Sh) / np.log(len(sub)))
        return float(np.nanmean(out))

    return lr.rolling(w, min_periods=max(16, w // 2)).apply(_rs, raw=True)


def _f03_variance_ratio(closeadj, w, q):
    # Lo-MacKinlay variance ratio: var(q-period ret)/(q*var(1-period ret))
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(w, min_periods=max(3, w // 2)).var()
    vq = (lr.rolling(q).sum()).rolling(w, min_periods=max(3, w // 2)).var()
    return vq / (q * v1).replace(0, np.nan)


def _f03_updown_streak(closeadj):
    # signed current run length of consecutive up(+)/down(-) days
    d = np.sign(closeadj.diff().fillna(0.0))
    out = np.zeros(len(d))
    vals = d.values
    run = 0.0
    prev = 0.0
    for i in range(len(vals)):
        s = vals[i]
        if s == 0:
            run = 0.0
        elif s == prev:
            run += s
        else:
            run = s
        out[i] = run
        prev = s
    res = pd.Series(out, index=closeadj.index)
    res.iloc[0] = np.nan
    return res


def _f03_trend_day_frac(closeadj, w):
    # fraction of up days minus 0.5 (directional bias of trend days)
    up = (closeadj.diff() > 0).astype(float)
    return up.rolling(w, min_periods=max(2, w // 2)).mean() - 0.5


def _f03_max_run(closeadj, w, up=True):
    # longest up-run (or down-run) length within window w
    d = np.sign(closeadj.diff().fillna(0.0))
    target = 1.0 if up else -1.0

    def _maxrun(a):
        best = 0
        cur = 0
        for x in a:
            if x == target:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)

    return d.rolling(w, min_periods=max(2, w // 2)).apply(_maxrun, raw=True)


# ============================================================
# efficiency ratio 21d (Kaufman) — core trend cleanliness
def f03mp_f03_momentum_persistence_effratio_21d_base_v001_signal(closeadj):
    b = _f03_efficiency_ratio(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 63d
def f03mp_f03_momentum_persistence_effratio_63d_base_v002_signal(closeadj):
    b = _f03_efficiency_ratio(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 126d
def f03mp_f03_momentum_persistence_effratio_126d_base_v003_signal(closeadj):
    b = _f03_efficiency_ratio(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 252d
def f03mp_f03_momentum_persistence_effratio_252d_base_v004_signal(closeadj):
    b = _f03_efficiency_ratio(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sub-window directional agreement 63d: share of 21d sub-returns matching the net sign
def f03mp_f03_momentum_persistence_signeff_63d_base_v005_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(63, min_periods=32).sum()
    sub = lr.rolling(21).sum()  # overlapping 21d sub-period returns
    agree = np.sign(sub) * np.sign(net)
    b = agree.rolling(63, min_periods=32).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sub-window directional agreement 126d: share of 21d sub-returns matching net sign
def f03mp_f03_momentum_persistence_signeff_126d_base_v006_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(126, min_periods=63).sum()
    sub = lr.rolling(21).sum()
    agree = np.sign(sub) * np.sign(net)
    b = agree.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio term spread: short minus long (regime cleanliness shift)
def f03mp_f03_momentum_persistence_effspr_21v126_base_v007_signal(closeadj):
    s = _f03_efficiency_ratio(closeadj, 21)
    l = _f03_efficiency_ratio(closeadj, 126)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio term spread 63 vs 252
def f03mp_f03_momentum_persistence_effspr_63v252_base_v008_signal(closeadj):
    s = _f03_efficiency_ratio(closeadj, 63)
    l = _f03_efficiency_ratio(closeadj, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 63d z-scored vs own 252d history (de-trended cleanliness)
def f03mp_f03_momentum_persistence_effz_63d_base_v009_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 63)
    b = _z(e, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 126d percentile-ranked vs own 504d history
def f03mp_f03_momentum_persistence_effrank_126d_base_v010_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 126)
    b = _rank(e, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation at lag 1 over 63d (short persistence vs reversal)
def f03mp_f03_momentum_persistence_ac1_63d_base_v011_signal(closeadj):
    b = _f03_autocorr(closeadj, 63, 1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation at lag 1 over 126d
def f03mp_f03_momentum_persistence_ac1_126d_base_v012_signal(closeadj):
    b = _f03_autocorr(closeadj, 126, 1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation at lag 1 over 252d
def f03mp_f03_momentum_persistence_ac1_252d_base_v013_signal(closeadj):
    b = _f03_autocorr(closeadj, 252, 1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation at lag 5 over 126d (weekly persistence)
def f03mp_f03_momentum_persistence_ac5_126d_base_v014_signal(closeadj):
    b = _f03_autocorr(closeadj, 126, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation at lag 10 over 252d
def f03mp_f03_momentum_persistence_ac10_252d_base_v015_signal(closeadj):
    b = _f03_autocorr(closeadj, 252, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation at lag 21 over 252d (monthly persistence)
def f03mp_f03_momentum_persistence_ac21_252d_base_v016_signal(closeadj):
    b = _f03_autocorr(closeadj, 252, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr spread: lag1 minus lag5 over 126d (term structure of persistence)
def f03mp_f03_momentum_persistence_acspr_1v5_126d_base_v017_signal(closeadj):
    a1 = _f03_autocorr(closeadj, 126, 1)
    a5 = _f03_autocorr(closeadj, 126, 5)
    b = a1 - a5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weekly-aggregated return autocorrelation lag1 over 252d (lower-frequency persistence)
def f03mp_f03_momentum_persistence_acwk_252d_base_v018_signal(closeadj):
    wk = np.log(closeadj.replace(0, np.nan)).diff(5)
    b = wk.rolling(252, min_periods=126).apply(
        lambda a: np.corrcoef(a[5:], a[:-5])[0, 1]
        if (np.std(a[5:]) > 0 and np.std(a[:-5]) > 0) else np.nan,
        raw=True,
    )
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst R/S exponent over 126d (trending if >0.5, mean-reverting if <0.5)
def f03mp_f03_momentum_persistence_hurst_126d_base_v019_signal(closeadj):
    b = _f03_hurst_rs(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst R/S exponent over 252d
def f03mp_f03_momentum_persistence_hurst_252d_base_v020_signal(closeadj):
    b = _f03_hurst_rs(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst R/S exponent over 63d (short-horizon persistence)
def f03mp_f03_momentum_persistence_hurst_63d_base_v021_signal(closeadj):
    b = _f03_hurst_rs(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst-deviation significance over 126d: (H-0.5) normalized by its own 252d volatility
def f03mp_f03_momentum_persistence_hurstdev_126d_base_v022_signal(closeadj):
    h = _f03_hurst_rs(closeadj, 126)
    dev = h - 0.5
    b = dev / _std(h, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst term spread: 63d minus 252d (horizon-dependent persistence)
def f03mp_f03_momentum_persistence_hurstspr_63v252_base_v023_signal(closeadj):
    s = _f03_hurst_rs(closeadj, 63)
    l = _f03_hurst_rs(closeadj, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst 252d z-scored vs own 504d history
def f03mp_f03_momentum_persistence_hurstz_252d_base_v024_signal(closeadj):
    h = _f03_hurst_rs(closeadj, 252)
    b = _z(h, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio profile slope over 126d: VR(10) - VR(2) (long vs short trend signature)
def f03mp_f03_momentum_persistence_vr2_126d_base_v025_signal(closeadj):
    v2 = _f03_variance_ratio(closeadj, 126, 2)
    v10 = _f03_variance_ratio(closeadj, 126, 10)
    b = v10 - v2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio q=5 over 126d
def f03mp_f03_momentum_persistence_vr5_126d_base_v026_signal(closeadj):
    b = _f03_variance_ratio(closeadj, 126, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio q=5 over 252d
def f03mp_f03_momentum_persistence_vr5_252d_base_v027_signal(closeadj):
    b = _f03_variance_ratio(closeadj, 252, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio q=10 over 252d (lower-frequency trend signature)
def f03mp_f03_momentum_persistence_vr10_252d_base_v028_signal(closeadj):
    b = _f03_variance_ratio(closeadj, 252, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio change over 126d: how the VR(5) trend signature is evolving (quarter delta)
def f03mp_f03_momentum_persistence_vrdev_126d_base_v029_signal(closeadj):
    v = _f03_variance_ratio(closeadj, 126, 5)
    b = v - v.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio term spread: q=2 minus q=10 over 252d (horizon dependence)
def f03mp_f03_momentum_persistence_vrspr_2v10_252d_base_v030_signal(closeadj):
    a = _f03_variance_ratio(closeadj, 252, 2)
    b2 = _f03_variance_ratio(closeadj, 252, 10)
    b = a - b2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio q=5 z-scored vs own 252d history
def f03mp_f03_momentum_persistence_vrz_126d_base_v031_signal(closeadj):
    v = _f03_variance_ratio(closeadj, 126, 5)
    b = _z(v, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed streak weighted by the cumulative return earned during the run (continuous)
def f03mp_f03_momentum_persistence_streak_1d_base_v032_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    r = closeadj.pct_change()
    # accumulate same-direction return magnitude over the current run length
    accel = (r.abs() * s).ewm(span=10, min_periods=3).mean()
    b = np.sign(s) * (s.abs() ** 0.5) + 50.0 * accel
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current streak normalized by its typical magnitude over 63d
def f03mp_f03_momentum_persistence_streakz_63d_base_v033_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    b = _z(s, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest up-run within 63d relative to that expected under random walk (smoothed)
def f03mp_f03_momentum_persistence_maxup_63d_base_v034_signal(closeadj):
    mr = _f03_max_run(closeadj, 63, up=True)
    # expected longest run under coin-flip ~ log2(n/2); ratio is continuous after smoothing
    b = (mr / np.log2(63)).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest down-run within 63d relative to random-walk expectation (smoothed)
def f03mp_f03_momentum_persistence_maxdn_63d_base_v035_signal(closeadj):
    mr = _f03_max_run(closeadj, 63, up=False)
    b = (mr / np.log2(63)).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# run asymmetry: longest up-run minus longest down-run over 126d (smoothed continuous)
def f03mp_f03_momentum_persistence_runasym_126d_base_v036_signal(closeadj):
    u = _f03_max_run(closeadj, 126, up=True)
    d = _f03_max_run(closeadj, 126, up=False)
    b = (u - d).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average run length: mean absolute streak over 63d (clustering of direction)
def f03mp_f03_momentum_persistence_avgrun_63d_base_v037_signal(closeadj):
    s = _f03_updown_streak(closeadj).abs()
    b = s.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direction-flip rate over 63d, magnitude-weighted by the return at each flip
def f03mp_f03_momentum_persistence_flips_63d_base_v038_signal(closeadj):
    r = closeadj.pct_change()
    d = np.sign(r.fillna(0.0))
    flip = (d != d.shift(1)).astype(float)
    # weight each flip by the size of the reversal move -> continuous choppiness cost
    wflip = (flip * r.abs()).rolling(63, min_periods=21).sum()
    rate = flip.rolling(63, min_periods=21).mean()
    b = -(rate + 20.0 * wflip)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day fraction over 63d, blended with a slow EMA for continuous resolution
def f03mp_f03_momentum_persistence_trendfrac_63d_base_v039_signal(closeadj):
    tf = _f03_trend_day_frac(closeadj, 63)
    b = 0.5 * tf + 0.5 * tf.ewm(span=15, min_periods=8).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day fraction over 126d
def f03mp_f03_momentum_persistence_trendfrac_126d_base_v040_signal(closeadj):
    b = _f03_trend_day_frac(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day fraction over 252d (long directional bias)
def f03mp_f03_momentum_persistence_trendfrac_252d_base_v041_signal(closeadj):
    b = _f03_trend_day_frac(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gain/loss asymmetry over 63d: avg up-day move vs avg down-day move (trend texture)
def f03mp_f03_momentum_persistence_upshare_63d_base_v042_signal(closeadj):
    r = closeadj.pct_change()
    up = r.where(r > 0)
    dn = (-r).where(r < 0)
    avg_up = up.rolling(63, min_periods=21).mean()
    avg_dn = dn.rolling(63, min_periods=21).mean()
    b = (avg_up - avg_dn) / (avg_up + avg_dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# streak-conditioned return capture over 126d: return earned on multi-day runs vs total
def f03mp_f03_momentum_persistence_upshare_126d_base_v043_signal(closeadj):
    r = closeadj.pct_change()
    s = _f03_updown_streak(closeadj)
    # returns occurring while in an established run (|streak|>=2) -> trend-captured move
    in_run = (s.abs() >= 2).astype(float)
    run_ret = (r * in_run).rolling(126, min_periods=63).sum()
    tot_ret = r.rolling(126, min_periods=63).sum()
    b = run_ret / tot_ret.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# same-sign consecutive-day persistence over 63d, weighted by paired return magnitude
def f03mp_f03_momentum_persistence_signpersist_63d_base_v044_signal(closeadj):
    r = closeadj.pct_change()
    prod = r * r.shift(1)
    # magnitude-weighted: positive products (continuation) vs negative (reversal)
    num = prod.rolling(63, min_periods=21).sum()
    den = (r.abs() * r.shift(1).abs()).rolling(63, min_periods=21).sum()
    b = num / den.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# continuation-vs-reversal net count over 126d, EMA-smoothed for continuous resolution
def f03mp_f03_momentum_persistence_signpersist_126d_base_v045_signal(closeadj):
    d = np.sign(closeadj.diff())
    cont = (d * d.shift(1))  # +1 continuation, -1 reversal, 0 flat
    b = (cont.rolling(126, min_periods=63).mean()).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend slope t-stat proxy: OLS slope / residual std over 63d (trend significance)
def f03mp_f03_momentum_persistence_trendt_63d_base_v046_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    w = 63
    x = np.arange(w)
    xm = x.mean()
    sxx = ((x - xm) ** 2).sum()

    def _t(a):
        ym = a.mean()
        slope = ((x - xm) * (a - ym)).sum() / sxx
        resid = a - (ym + slope * (x - xm))
        rs = resid.std()
        if rs <= 0:
            return np.nan
        return slope * np.sqrt(sxx) / rs

    b = lp.rolling(w, min_periods=w).apply(_t, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend slope t-stat proxy over 126d
def f03mp_f03_momentum_persistence_trendt_126d_base_v047_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    w = 126
    x = np.arange(w)
    xm = x.mean()
    sxx = ((x - xm) ** 2).sum()

    def _t(a):
        ym = a.mean()
        slope = ((x - xm) * (a - ym)).sum() / sxx
        resid = a - (ym + slope * (x - xm))
        rs = resid.std()
        if rs <= 0:
            return np.nan
        return slope * np.sqrt(sxx) / rs

    b = lp.rolling(w, min_periods=w).apply(_t, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R-squared of log-price trend regression over 63d (how linear the trend is)
def f03mp_f03_momentum_persistence_trendr2_63d_base_v048_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    w = 63
    x = np.arange(w)
    xm = x.mean()
    sxx = ((x - xm) ** 2).sum()

    def _r2(a):
        ym = a.mean()
        slope = ((x - xm) * (a - ym)).sum() / sxx
        fitted = ym + slope * (x - xm)
        ssr = ((a - fitted) ** 2).sum()
        sst = ((a - ym) ** 2).sum()
        if sst <= 0:
            return np.nan
        return 1.0 - ssr / sst

    b = lp.rolling(w, min_periods=w).apply(_r2, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R-squared of trend regression over 126d, signed by slope direction
def f03mp_f03_momentum_persistence_trendr2s_126d_base_v049_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    w = 126
    x = np.arange(w)
    xm = x.mean()
    sxx = ((x - xm) ** 2).sum()

    def _r2s(a):
        ym = a.mean()
        slope = ((x - xm) * (a - ym)).sum() / sxx
        fitted = ym + slope * (x - xm)
        ssr = ((a - fitted) ** 2).sum()
        sst = ((a - ym) ** 2).sum()
        if sst <= 0:
            return np.nan
        return np.sign(slope) * (1.0 - ssr / sst)

    b = lp.rolling(w, min_periods=w).apply(_r2s, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum consistency: fraction of positive 21d ROC over the last 126d
def f03mp_f03_momentum_persistence_roccons_126d_base_v050_signal(closeadj):
    roc = closeadj / closeadj.shift(21) - 1.0
    b = (roc > 0).astype(float).rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum consistency: fraction of positive 63d ROC over 252d
def f03mp_f03_momentum_persistence_roccons_252d_base_v051_signal(closeadj):
    roc = closeadj / closeadj.shift(63) - 1.0
    b = (roc > 0).astype(float).rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-weighted momentum: 63d ROC scaled by 63d efficiency ratio
def f03mp_f03_momentum_persistence_effmom_63d_base_v052_signal(closeadj):
    roc = closeadj / closeadj.shift(63) - 1.0
    e = _f03_efficiency_ratio(closeadj, 63)
    b = roc * e
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-weighted momentum 126d
def f03mp_f03_momentum_persistence_effmom_126d_base_v053_signal(closeadj):
    roc = closeadj / closeadj.shift(126) - 1.0
    e = _f03_efficiency_ratio(closeadj, 126)
    b = roc * e
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drift-to-downside-deviation over 63d (Sortino-style persistence, asymmetric noise)
def f03mp_f03_momentum_persistence_driftnoise_63d_base_v054_signal(closeadj):
    r = closeadj.pct_change()
    downside = r.where(r < 0, 0.0)
    dd = (downside ** 2).rolling(63, min_periods=21).mean() ** 0.5
    b = _mean(r, 63) / dd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drift-to-downside-deviation over 126d (Sortino-style persistence)
def f03mp_f03_momentum_persistence_driftnoise_126d_base_v055_signal(closeadj):
    r = closeadj.pct_change()
    downside = r.where(r < 0, 0.0)
    dd = (downside ** 2).rolling(126, min_periods=63).mean() ** 0.5
    b = _mean(r, 126) / dd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drift-to-downside-deviation over 252d (Sortino-style persistence)
def f03mp_f03_momentum_persistence_driftnoise_252d_base_v056_signal(closeadj):
    r = closeadj.pct_change()
    downside = r.where(r < 0, 0.0)
    dd = (downside ** 2).rolling(252, min_periods=126).mean() ** 0.5
    b = _mean(r, 252) / dd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# path roughness over 63d: total traversed distance relative to the spanned price range
def f03mp_f03_momentum_persistence_logeff_63d_base_v057_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    path = lp.diff().abs().rolling(63, min_periods=32).sum()
    span = (lp.rolling(63, min_periods=32).max()
            - lp.rolling(63, min_periods=32).min())
    # >=1 always; larger = more back-and-forth churn per unit of range covered
    b = path / span.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Higuchi-style fractal dimension over 63d via path-length scaling at two strides
def f03mp_f03_momentum_persistence_fractal_63d_base_v058_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _fd(a):
        a = a[np.isfinite(a)]
        m = len(a)
        if m < 16:
            return np.nan
        # mean curve length at stride k=1 and k=4; FD ~ slope of log(L) vs log(1/k)
        def _L(k):
            seg = a[::k]
            if len(seg) < 2:
                return np.nan
            return np.abs(np.diff(seg)).sum() * (m - 1) / (((m - 1) // k) * k)
        l1 = _L(1)
        l4 = _L(4)
        if not (np.isfinite(l1) and np.isfinite(l4)) or l1 <= 0 or l4 <= 0:
            return np.nan
        return (np.log(l1) - np.log(l4)) / (np.log(4.0))

    b = lp.rolling(63, min_periods=32).apply(_fd, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr lag1 of weekly-summed returns over 126d (medium-frequency persistence)
def f03mp_f03_momentum_persistence_acwk_126d_base_v059_signal(closeadj):
    wk = np.log(closeadj.replace(0, np.nan)).diff(5)
    b = wk.rolling(126, min_periods=63).apply(
        lambda a: np.corrcoef(a[5:], a[:-5])[0, 1]
        if (np.std(a[5:]) > 0 and np.std(a[:-5]) > 0) else np.nan,
        raw=True,
    )
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional persistence as excess continuation probability scaled by trend strength
def f03mp_f03_momentum_persistence_dirpersist_126d_base_v060_signal(closeadj):
    r = closeadj.pct_change()
    d = np.sign(r)
    cont = (d * d.shift(1)).rolling(126, min_periods=63).mean()
    # scale by the realized drift-to-noise so it varies continuously with regime strength
    strength = _mean(r, 126) / _std(r, 126)
    b = cont * (1.0 + strength.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day fraction weighted by 63d efficiency (clean directional bias)
def f03mp_f03_momentum_persistence_cleantrend_63d_base_v061_signal(closeadj):
    tf = _f03_trend_day_frac(closeadj, 63)
    e = _f03_efficiency_ratio(closeadj, 63)
    b = tf * e
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio q=5 minus efficiency ratio (two persistence views disagreement)
def f03mp_f03_momentum_persistence_vrminuseff_126d_base_v062_signal(closeadj):
    v = _f03_variance_ratio(closeadj, 126, 5)
    e = _f03_efficiency_ratio(closeadj, 126)
    b = (v - 1.0) - (e - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# streak energy: sum of squared signed streaks over 63d (momentum clustering)
def f03mp_f03_momentum_persistence_streaken_63d_base_v063_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    b = (s ** 2 * np.sign(s)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in efficiency ratio over a quarter (trend cleanliness momentum)
def f03mp_f03_momentum_persistence_effchg_63d_base_v064_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 63)
    b = e - e.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in Hurst over a quarter (persistence regime shift)
def f03mp_f03_momentum_persistence_hurstchg_126d_base_v065_signal(closeadj):
    h = _f03_hurst_rs(closeadj, 126)
    b = h - h.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorrelation lag1 smoothed by EMA (persistent persistence signal)
def f03mp_f03_momentum_persistence_acema_126d_base_v066_signal(closeadj):
    a1 = _f03_autocorr(closeadj, 126, 1)
    b = a1.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time spent in sustained up-streaks (>=3) over 126d, weighted by streak depth
def f03mp_f03_momentum_persistence_longup_126d_base_v067_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    deep = s.where(s >= 3, 0.0)
    b = deep.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time spent in sustained down-streaks (<=-3) over 126d, weighted by streak depth
def f03mp_f03_momentum_persistence_longdn_126d_base_v068_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    deep = (-s).where(s <= -3, 0.0)
    b = deep.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency x positive-autocorrelation interaction over 63d (clean AND self-reinforcing)
def f03mp_f03_momentum_persistence_effdrift_63d_base_v069_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 63)
    a1 = _f03_autocorr(closeadj, 63, 1)
    b = e * a1
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio curvature over 63d: VR(3) - 2*VR(2) + 1 (second difference of VR profile)
def f03mp_f03_momentum_persistence_vr2_63d_base_v070_signal(closeadj):
    v2 = _f03_variance_ratio(closeadj, 63, 2)
    v3 = _f03_variance_ratio(closeadj, 63, 3)
    b = v3 - 2.0 * v2 + 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst-implied trend confidence: (hurst-0.5) * signed efficiency 126d
def f03mp_f03_momentum_persistence_hurstconf_126d_base_v071_signal(closeadj):
    h = _f03_hurst_rs(closeadj, 126) - 0.5
    se = _f03_signed_efficiency(closeadj, 126)
    b = h * se
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr lag1 over 63d minus its 252d typical (de-meaned short persistence)
def f03mp_f03_momentum_persistence_acdemean_63d_base_v072_signal(closeadj):
    a1 = _f03_autocorr(closeadj, 63, 1)
    b = a1 - a1.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day fraction year-over-year change (directional-bias evolution)
def f03mp_f03_momentum_persistence_trendyoy_252d_base_v073_signal(closeadj):
    tf = _f03_trend_day_frac(closeadj, 252)
    b = tf - tf.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-vs-path on 21d window ranked vs 252d history (short cleanliness percentile)
def f03mp_f03_momentum_persistence_effrank_21d_base_v074_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 21)
    b = _rank(e, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# persistence composite: efficiency + (hurst-0.5) + trend-day-bias over 126d
def f03mp_f03_momentum_persistence_composite_126d_base_v075_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 126)
    h = _f03_hurst_rs(closeadj, 126) - 0.5
    tf = _f03_trend_day_frac(closeadj, 126)
    b = e + h + tf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03mp_f03_momentum_persistence_effratio_21d_base_v001_signal,
    f03mp_f03_momentum_persistence_effratio_63d_base_v002_signal,
    f03mp_f03_momentum_persistence_effratio_126d_base_v003_signal,
    f03mp_f03_momentum_persistence_effratio_252d_base_v004_signal,
    f03mp_f03_momentum_persistence_signeff_63d_base_v005_signal,
    f03mp_f03_momentum_persistence_signeff_126d_base_v006_signal,
    f03mp_f03_momentum_persistence_effspr_21v126_base_v007_signal,
    f03mp_f03_momentum_persistence_effspr_63v252_base_v008_signal,
    f03mp_f03_momentum_persistence_effz_63d_base_v009_signal,
    f03mp_f03_momentum_persistence_effrank_126d_base_v010_signal,
    f03mp_f03_momentum_persistence_ac1_63d_base_v011_signal,
    f03mp_f03_momentum_persistence_ac1_126d_base_v012_signal,
    f03mp_f03_momentum_persistence_ac1_252d_base_v013_signal,
    f03mp_f03_momentum_persistence_ac5_126d_base_v014_signal,
    f03mp_f03_momentum_persistence_ac10_252d_base_v015_signal,
    f03mp_f03_momentum_persistence_ac21_252d_base_v016_signal,
    f03mp_f03_momentum_persistence_acspr_1v5_126d_base_v017_signal,
    f03mp_f03_momentum_persistence_acwk_252d_base_v018_signal,
    f03mp_f03_momentum_persistence_hurst_126d_base_v019_signal,
    f03mp_f03_momentum_persistence_hurst_252d_base_v020_signal,
    f03mp_f03_momentum_persistence_hurst_63d_base_v021_signal,
    f03mp_f03_momentum_persistence_hurstdev_126d_base_v022_signal,
    f03mp_f03_momentum_persistence_hurstspr_63v252_base_v023_signal,
    f03mp_f03_momentum_persistence_hurstz_252d_base_v024_signal,
    f03mp_f03_momentum_persistence_vr2_126d_base_v025_signal,
    f03mp_f03_momentum_persistence_vr5_126d_base_v026_signal,
    f03mp_f03_momentum_persistence_vr5_252d_base_v027_signal,
    f03mp_f03_momentum_persistence_vr10_252d_base_v028_signal,
    f03mp_f03_momentum_persistence_vrdev_126d_base_v029_signal,
    f03mp_f03_momentum_persistence_vrspr_2v10_252d_base_v030_signal,
    f03mp_f03_momentum_persistence_vrz_126d_base_v031_signal,
    f03mp_f03_momentum_persistence_streak_1d_base_v032_signal,
    f03mp_f03_momentum_persistence_streakz_63d_base_v033_signal,
    f03mp_f03_momentum_persistence_maxup_63d_base_v034_signal,
    f03mp_f03_momentum_persistence_maxdn_63d_base_v035_signal,
    f03mp_f03_momentum_persistence_runasym_126d_base_v036_signal,
    f03mp_f03_momentum_persistence_avgrun_63d_base_v037_signal,
    f03mp_f03_momentum_persistence_flips_63d_base_v038_signal,
    f03mp_f03_momentum_persistence_trendfrac_63d_base_v039_signal,
    f03mp_f03_momentum_persistence_trendfrac_126d_base_v040_signal,
    f03mp_f03_momentum_persistence_trendfrac_252d_base_v041_signal,
    f03mp_f03_momentum_persistence_upshare_63d_base_v042_signal,
    f03mp_f03_momentum_persistence_upshare_126d_base_v043_signal,
    f03mp_f03_momentum_persistence_signpersist_63d_base_v044_signal,
    f03mp_f03_momentum_persistence_signpersist_126d_base_v045_signal,
    f03mp_f03_momentum_persistence_trendt_63d_base_v046_signal,
    f03mp_f03_momentum_persistence_trendt_126d_base_v047_signal,
    f03mp_f03_momentum_persistence_trendr2_63d_base_v048_signal,
    f03mp_f03_momentum_persistence_trendr2s_126d_base_v049_signal,
    f03mp_f03_momentum_persistence_roccons_126d_base_v050_signal,
    f03mp_f03_momentum_persistence_roccons_252d_base_v051_signal,
    f03mp_f03_momentum_persistence_effmom_63d_base_v052_signal,
    f03mp_f03_momentum_persistence_effmom_126d_base_v053_signal,
    f03mp_f03_momentum_persistence_driftnoise_63d_base_v054_signal,
    f03mp_f03_momentum_persistence_driftnoise_126d_base_v055_signal,
    f03mp_f03_momentum_persistence_driftnoise_252d_base_v056_signal,
    f03mp_f03_momentum_persistence_logeff_63d_base_v057_signal,
    f03mp_f03_momentum_persistence_fractal_63d_base_v058_signal,
    f03mp_f03_momentum_persistence_acwk_126d_base_v059_signal,
    f03mp_f03_momentum_persistence_dirpersist_126d_base_v060_signal,
    f03mp_f03_momentum_persistence_cleantrend_63d_base_v061_signal,
    f03mp_f03_momentum_persistence_vrminuseff_126d_base_v062_signal,
    f03mp_f03_momentum_persistence_streaken_63d_base_v063_signal,
    f03mp_f03_momentum_persistence_effchg_63d_base_v064_signal,
    f03mp_f03_momentum_persistence_hurstchg_126d_base_v065_signal,
    f03mp_f03_momentum_persistence_acema_126d_base_v066_signal,
    f03mp_f03_momentum_persistence_longup_126d_base_v067_signal,
    f03mp_f03_momentum_persistence_longdn_126d_base_v068_signal,
    f03mp_f03_momentum_persistence_effdrift_63d_base_v069_signal,
    f03mp_f03_momentum_persistence_vr2_63d_base_v070_signal,
    f03mp_f03_momentum_persistence_hurstconf_126d_base_v071_signal,
    f03mp_f03_momentum_persistence_acdemean_63d_base_v072_signal,
    f03mp_f03_momentum_persistence_trendyoy_252d_base_v073_signal,
    f03mp_f03_momentum_persistence_effrank_21d_base_v074_signal,
    f03mp_f03_momentum_persistence_composite_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_MOMENTUM_PERSISTENCE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
    }

    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s not subset of allowlist" % (
            name, meta["inputs"])
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

    print("OK f03_momentum_persistence_base_001_075_claude: %d features pass" % n_features)
