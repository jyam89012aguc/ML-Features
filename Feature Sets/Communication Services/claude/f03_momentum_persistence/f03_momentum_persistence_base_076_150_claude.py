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
    return closeadj.pct_change()


def _f03_logret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f03_efficiency_ratio(closeadj, w):
    net = (closeadj - closeadj.shift(w)).abs()
    path = closeadj.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _f03_signed_efficiency(closeadj, w):
    net = closeadj - closeadj.shift(w)
    path = closeadj.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _f03_autocorr(closeadj, w, lag):
    r = closeadj.pct_change()
    return r.rolling(w, min_periods=max(3, w // 2)).apply(
        lambda a: np.corrcoef(a[lag:], a[:-lag])[0, 1]
        if (np.std(a[lag:]) > 0 and np.std(a[:-lag]) > 0) else np.nan,
        raw=True,
    )


def _f03_hurst_rs(closeadj, w):
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
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(w, min_periods=max(3, w // 2)).var()
    vq = (lr.rolling(q).sum()).rolling(w, min_periods=max(3, w // 2)).var()
    return vq / (q * v1).replace(0, np.nan)


def _f03_updown_streak(closeadj):
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
    up = (closeadj.diff() > 0).astype(float)
    return up.rolling(w, min_periods=max(2, w // 2)).mean() - 0.5


def _f03_max_run(closeadj, w, up=True):
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


def _f03_trend_slope(closeadj, w):
    lp = np.log(closeadj.replace(0, np.nan))
    x = np.arange(w)
    xm = x.mean()
    sxx = ((x - xm) ** 2).sum()

    def _slope(a):
        ym = a.mean()
        return ((x - xm) * (a - ym)).sum() / sxx

    return lp.rolling(w, min_periods=w).apply(_slope, raw=True)


# ============================================================
# efficiency ratio 5d (weekly micro-trend cleanliness)
def f03mp_f03_momentum_persistence_effratio_5d_base_v076_signal(closeadj):
    b = _f03_efficiency_ratio(closeadj, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 42d (six-week trend cleanliness)
def f03mp_f03_momentum_persistence_effratio_42d_base_v077_signal(closeadj):
    b = _f03_efficiency_ratio(closeadj, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 189d (three-quarter trend cleanliness)
def f03mp_f03_momentum_persistence_effratio_189d_base_v078_signal(closeadj):
    b = _f03_efficiency_ratio(closeadj, 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 504d (two-year trend cleanliness)
def f03mp_f03_momentum_persistence_effratio_504d_base_v079_signal(closeadj):
    b = _f03_efficiency_ratio(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency dispersion: rolling std of 21d efficiency over 126d (regime stability)
def f03mp_f03_momentum_persistence_effdisp_126d_base_v080_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 21)
    b = _std(e, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency persistence: fraction of last 126d with 21d efficiency above 0.5
def f03mp_f03_momentum_persistence_effabove_126d_base_v081_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 21)
    b = (e > 0.5).astype(float).rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency EMA over 63d (smoothed trend cleanliness)
def f03mp_f03_momentum_persistence_effema_63d_base_v082_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 63)
    b = e.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed efficiency change over a month (cleanliness momentum, direction-aware)
def f03mp_f03_momentum_persistence_signeffchg_63d_base_v083_signal(closeadj):
    se = _f03_signed_efficiency(closeadj, 63)
    b = se - se.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio acceleration: 21d eff minus its own 63d mean (short cleanliness pop)
def f03mp_f03_momentum_persistence_effaccel_21d_base_v084_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 21)
    b = e - e.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 252d ranked vs own 504d history (long cleanliness percentile)
def f03mp_f03_momentum_persistence_effrank_252d_base_v085_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 252)
    b = _rank(e, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation at lag 2 over 126d (two-day persistence)
def f03mp_f03_momentum_persistence_ac2_126d_base_v086_signal(closeadj):
    b = _f03_autocorr(closeadj, 126, 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation at lag 3 over 252d
def f03mp_f03_momentum_persistence_ac3_252d_base_v087_signal(closeadj):
    b = _f03_autocorr(closeadj, 252, 3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average of autocorrelations at lags 1..5 over 126d (short-memory strength)
def f03mp_f03_momentum_persistence_acavg_126d_base_v088_signal(closeadj):
    acc = None
    for lag in range(1, 6):
        a = _f03_autocorr(closeadj, 126, lag)
        acc = a if acc is None else acc + a
    b = acc / 5.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# decay of memory: autocorr lag1 minus lag10 over 252d (how fast persistence fades)
def f03mp_f03_momentum_persistence_acdecay_252d_base_v089_signal(closeadj):
    a1 = _f03_autocorr(closeadj, 252, 1)
    a10 = _f03_autocorr(closeadj, 252, 10)
    b = a1 - a10
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorrelation lag1 over 63d ranked vs own 252d history (relative persistence)
def f03mp_f03_momentum_persistence_acrank_63d_base_v090_signal(closeadj):
    a1 = _f03_autocorr(closeadj, 63, 1)
    b = _rank(a1, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# monthly-aggregated return autocorr lag1 over 252d (low-frequency persistence)
def f03mp_f03_momentum_persistence_acmo_252d_base_v091_signal(closeadj):
    mo = np.log(closeadj.replace(0, np.nan)).diff(21)
    b = mo.rolling(252, min_periods=126).apply(
        lambda a: np.corrcoef(a[21:], a[:-21])[0, 1]
        if (np.std(a[21:]) > 0 and np.std(a[:-21]) > 0) else np.nan,
        raw=True,
    )
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr lag1 z-scored vs own 504d history (de-trended short persistence)
def f03mp_f03_momentum_persistence_acz_126d_base_v092_signal(closeadj):
    a1 = _f03_autocorr(closeadj, 126, 1)
    b = _z(a1, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst R/S exponent over 189d (three-quarter persistence)
def f03mp_f03_momentum_persistence_hurst_189d_base_v093_signal(closeadj):
    b = _f03_hurst_rs(closeadj, 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst R/S exponent over 504d (two-year persistence)
def f03mp_f03_momentum_persistence_hurst_504d_base_v094_signal(closeadj):
    b = _f03_hurst_rs(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst EMA over 126d (smoothed persistence regime)
def f03mp_f03_momentum_persistence_hurstema_126d_base_v095_signal(closeadj):
    h = _f03_hurst_rs(closeadj, 126)
    b = h.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst rank vs own 504d history (relative persistence regime)
def f03mp_f03_momentum_persistence_hurstrank_252d_base_v096_signal(closeadj):
    h = _f03_hurst_rs(closeadj, 252)
    b = _rank(h, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst-deviation x signed trend slope sign (persistence aligned with direction)
def f03mp_f03_momentum_persistence_hurstdir_252d_base_v097_signal(closeadj):
    h = _f03_hurst_rs(closeadj, 252) - 0.5
    sl = _f03_trend_slope(closeadj, 252)
    b = h * np.sign(sl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst dispersion: std of 126d Hurst over 252d (persistence-regime instability)
def f03mp_f03_momentum_persistence_hurstdisp_252d_base_v098_signal(closeadj):
    h = _f03_hurst_rs(closeadj, 126)
    b = _std(h, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio q=3 over 126d
def f03mp_f03_momentum_persistence_vr3_126d_base_v099_signal(closeadj):
    b = _f03_variance_ratio(closeadj, 126, 3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio q=21 over 252d (monthly aggregation trend signature)
def f03mp_f03_momentum_persistence_vr21_252d_base_v100_signal(closeadj):
    b = _f03_variance_ratio(closeadj, 252, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio EMA over 126d (q=5, smoothed persistence)
def f03mp_f03_momentum_persistence_vrema_126d_base_v101_signal(closeadj):
    v = _f03_variance_ratio(closeadj, 126, 5)
    b = v.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio rank vs own 504d history (q=10, relative trendiness)
def f03mp_f03_momentum_persistence_vrrank_252d_base_v102_signal(closeadj):
    v = _f03_variance_ratio(closeadj, 252, 10)
    b = _rank(v, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio profile slope q=2->5->10 over 252d (linear trend in VR vs q)
def f03mp_f03_momentum_persistence_vrprofile_252d_base_v103_signal(closeadj):
    v2 = _f03_variance_ratio(closeadj, 252, 2)
    v5 = _f03_variance_ratio(closeadj, 252, 5)
    v10 = _f03_variance_ratio(closeadj, 252, 10)
    # OLS slope of (v2,v5,v10) vs q=(2,5,10)
    qs = np.array([2.0, 5.0, 10.0])
    qm = qs.mean()
    denom = ((qs - qm) ** 2).sum()
    b = ((v2 * (2 - qm)) + (v5 * (5 - qm)) + (v10 * (10 - qm))) / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio dispersion: std of q=5 VR (126d) over 252d (trend-regime instability)
def f03mp_f03_momentum_persistence_vrdisp_252d_base_v104_signal(closeadj):
    v = _f03_variance_ratio(closeadj, 126, 5)
    b = _std(v, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest up-run within 126d relative to random-walk expectation (smoothed)
def f03mp_f03_momentum_persistence_maxup_126d_base_v105_signal(closeadj):
    mr = _f03_max_run(closeadj, 126, up=True)
    b = (mr / np.log2(126)).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest down-run within 126d relative to random-walk expectation (smoothed)
def f03mp_f03_momentum_persistence_maxdn_126d_base_v106_signal(closeadj):
    mr = _f03_max_run(closeadj, 126, up=False)
    b = (mr / np.log2(126)).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# streak return-capture asymmetry: gain on up-runs vs loss on down-runs over 126d
def f03mp_f03_momentum_persistence_streakcap_126d_base_v107_signal(closeadj):
    r = closeadj.pct_change()
    s = _f03_updown_streak(closeadj)
    up_run = (r * (s >= 2).astype(float)).rolling(126, min_periods=63).sum()
    dn_run = (r * (s <= -2).astype(float)).rolling(126, min_periods=63).sum()
    b = up_run + dn_run
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average signed streak over 126d (net directional run bias, continuous)
def f03mp_f03_momentum_persistence_avgsignrun_126d_base_v108_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    b = s.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# streak volatility: std of signed streaks over 126d (run-length variability)
def f03mp_f03_momentum_persistence_streakvol_126d_base_v109_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    b = _std(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expected-run excess: mean abs run over 63d minus the coin-flip baseline of 2.0
def f03mp_f03_momentum_persistence_runexcess_63d_base_v110_signal(closeadj):
    s = _f03_updown_streak(closeadj).abs()
    b = s.rolling(63, min_periods=21).mean() - 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# flip-rate change over a quarter (choppiness momentum, EMA-smoothed)
def f03mp_f03_momentum_persistence_flipchg_63d_base_v111_signal(closeadj):
    d = np.sign(closeadj.diff().fillna(0.0))
    flip = (d != d.shift(1)).astype(float)
    rate = flip.rolling(63, min_periods=21).mean()
    b = (rate - rate.shift(63)).ewm(span=10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day fraction over 21d, EMA-blended for resolution (short directional bias)
def f03mp_f03_momentum_persistence_trendfrac_21d_base_v112_signal(closeadj):
    tf = _f03_trend_day_frac(closeadj, 21)
    b = 0.5 * tf + 0.5 * tf.ewm(span=10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day fraction change over a quarter (directional-bias momentum)
def f03mp_f03_momentum_persistence_trendfracchg_126d_base_v113_signal(closeadj):
    tf = _f03_trend_day_frac(closeadj, 126)
    b = tf - tf.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gain/loss size asymmetry over 126d (avg up move vs avg down move)
def f03mp_f03_momentum_persistence_glasym_126d_base_v114_signal(closeadj):
    r = closeadj.pct_change()
    up = r.where(r > 0)
    dn = (-r).where(r < 0)
    au = up.rolling(126, min_periods=63).mean()
    ad = dn.rolling(126, min_periods=63).mean()
    b = (au - ad) / (au + ad).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-quality slope t-stat over 252d (long-trend statistical significance)
def f03mp_f03_momentum_persistence_trendt_252d_base_v115_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    w = 252
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


# trend R-squared over 252d (long-trend linearity)
def f03mp_f03_momentum_persistence_trendr2_252d_base_v116_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    w = 252
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


# trend R-squared change over a quarter (trend-linearity momentum, 126d)
def f03mp_f03_momentum_persistence_trendr2chg_126d_base_v117_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    w = 126
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

    r2 = lp.rolling(w, min_periods=w).apply(_r2, raw=True)
    b = r2 - r2.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum consistency: fraction positive 5d ROC over 63d, EMA-blended
def f03mp_f03_momentum_persistence_roccons_63d_base_v118_signal(closeadj):
    roc = closeadj / closeadj.shift(5) - 1.0
    raw = (roc > 0).astype(float).rolling(63, min_periods=21).mean() - 0.5
    b = 0.5 * raw + 0.5 * raw.ewm(span=10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon momentum agreement: sign concordance of 21/63/126d ROC (smoothed)
def f03mp_f03_momentum_persistence_momagree_126d_base_v119_signal(closeadj):
    r21 = np.sign(closeadj / closeadj.shift(21) - 1.0)
    r63 = np.sign(closeadj / closeadj.shift(63) - 1.0)
    r126 = np.sign(closeadj / closeadj.shift(126) - 1.0)
    agree = (r21 + r63 + r126) / 3.0
    b = agree.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-weighted 252d momentum (clean long-trend strength)
def f03mp_f03_momentum_persistence_effmom_252d_base_v120_signal(closeadj):
    roc = closeadj / closeadj.shift(252) - 1.0
    e = _f03_efficiency_ratio(closeadj, 252)
    b = roc * e
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst-weighted 126d momentum (persistence-confirmed trend strength)
def f03mp_f03_momentum_persistence_hurstmom_126d_base_v121_signal(closeadj):
    roc = closeadj / closeadj.shift(126) - 1.0
    h = (_f03_hurst_rs(closeadj, 126) - 0.5)
    b = roc * h
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-slope per unit residual risk EMA over 126d (smoothed significance)
def f03mp_f03_momentum_persistence_slopenoise_126d_base_v122_signal(closeadj):
    sl = _f03_trend_slope(closeadj, 126)
    r = closeadj.pct_change()
    vol = _std(r, 126)
    b = (sl / vol.replace(0, np.nan)).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# path roughness over 126d (traversed distance per unit of range covered)
def f03mp_f03_momentum_persistence_roughness_126d_base_v123_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    path = lp.diff().abs().rolling(126, min_periods=63).sum()
    span = (lp.rolling(126, min_periods=63).max()
            - lp.rolling(126, min_periods=63).min())
    b = path / span.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Higuchi fractal dimension over 126d (path complexity; low = trending)
def f03mp_f03_momentum_persistence_fractal_126d_base_v124_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _fd(a):
        a = a[np.isfinite(a)]
        m = len(a)
        if m < 24:
            return np.nan

        def _L(k):
            seg = a[::k]
            if len(seg) < 2:
                return np.nan
            return np.abs(np.diff(seg)).sum() * (m - 1) / (((m - 1) // k) * k)
        l1 = _L(1)
        l4 = _L(4)
        if not (np.isfinite(l1) and np.isfinite(l4)) or l1 <= 0 or l4 <= 0:
            return np.nan
        return (np.log(l1) - np.log(l4)) / np.log(4.0)

    b = lp.rolling(126, min_periods=63).apply(_fd, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional-agreement of sub-window returns over 252d (252d net vs 21d sub-returns)
def f03mp_f03_momentum_persistence_subagree_252d_base_v125_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(252, min_periods=126).sum()
    sub = lr.rolling(21).sum()
    agree = np.sign(sub) * np.sign(net)
    b = agree.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drift-to-downside-deviation over 21d (short Sortino-style persistence)
def f03mp_f03_momentum_persistence_sortino_21d_base_v126_signal(closeadj):
    r = closeadj.pct_change()
    downside = r.where(r < 0, 0.0)
    dd = (downside ** 2).rolling(21, min_periods=10).mean() ** 0.5
    b = _mean(r, 21) / dd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Kaufman adaptive efficiency: 21d efficiency squared (smoothing-constant proxy)
def f03mp_f03_momentum_persistence_kamasc_21d_base_v127_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 21)
    fast, slow = 2.0 / (2 + 1), 2.0 / (30 + 1)
    sc = (e * (fast - slow) + slow) ** 2
    b = sc - sc.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# persistence vs reversion balance: efficiency minus |autocorr lag1| over 63d
def f03mp_f03_momentum_persistence_persbal_63d_base_v128_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 63)
    a1 = _f03_autocorr(closeadj, 63, 1)
    b = e - a1.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# run-length entropy over 126d: dispersion of run lengths (low = regular, persistent runs)
def f03mp_f03_momentum_persistence_runprofit_126d_base_v129_signal(closeadj):
    s = _f03_updown_streak(closeadj).abs()
    # coefficient of variation of absolute run length within the window
    mu = s.rolling(126, min_periods=63).mean()
    sd = s.rolling(126, min_periods=63).std()
    b = sd / mu.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend slope sign stability: fraction of last 126d where 63d slope keeps current sign
def f03mp_f03_momentum_persistence_slopestab_126d_base_v130_signal(closeadj):
    sl = _f03_trend_slope(closeadj, 63)
    cur = np.sign(sl)
    same = (np.sign(sl) == cur).astype(float)
    # use product with lagged sign for a continuous persistence measure
    prod = (np.sign(sl) * np.sign(sl.shift(5)))
    b = prod.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio vs Hurst agreement over 252d (two persistence measures combined)
def f03mp_f03_momentum_persistence_vrhurst_252d_base_v131_signal(closeadj):
    v = _f03_variance_ratio(closeadj, 252, 5) - 1.0
    h = _f03_hurst_rs(closeadj, 252) - 0.5
    b = np.sign(v) * np.sign(h) * (v.abs() + h.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorrelation curvature: ac(1) - 2*ac(2) + ac(3) over 126d (memory shape)
def f03mp_f03_momentum_persistence_accurv_126d_base_v132_signal(closeadj):
    a1 = _f03_autocorr(closeadj, 126, 1)
    a2 = _f03_autocorr(closeadj, 126, 2)
    a3 = _f03_autocorr(closeadj, 126, 3)
    b = a1 - 2.0 * a2 + a3
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trending-time fraction: share of last 252d with 63d efficiency above its median
def f03mp_f03_momentum_persistence_trendtime_252d_base_v133_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 63)
    med = e.rolling(252, min_periods=126).median()
    above = (e > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5 + 0.1 * (e - med)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum sign persistence: mean of sign(ROC63)*sign(ROC63 lagged 21) over 252d
def f03mp_f03_momentum_persistence_rochalflife_252d_base_v134_signal(closeadj):
    roc = closeadj / closeadj.shift(63) - 1.0
    prod = np.sign(roc) * np.sign(roc.shift(21))
    b = prod.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed efficiency over 252d minus over 63d (long vs short directional cleanliness)
def f03mp_f03_momentum_persistence_signeffspr_252v63_base_v135_signal(closeadj):
    l = _f03_signed_efficiency(closeadj, 252)
    s = _f03_signed_efficiency(closeadj, 63)
    b = l - s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of variance from trend: 1 - var(detrended)/var(price) over 126d
def f03mp_f03_momentum_persistence_trendvar_126d_base_v136_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    w = 126
    x = np.arange(w)
    xm = x.mean()
    sxx = ((x - xm) ** 2).sum()

    def _frac(a):
        ym = a.mean()
        slope = ((x - xm) * (a - ym)).sum() / sxx
        resid = a - (ym + slope * (x - xm))
        vr = resid.var()
        va = a.var()
        if va <= 0:
            return np.nan
        return np.sign(slope) * (1.0 - vr / va)

    b = lp.rolling(w, min_periods=w).apply(_frac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio term-structure curvature: eff21 - 2*eff63 + eff126
def f03mp_f03_momentum_persistence_effcurv_base_v137_signal(closeadj):
    e21 = _f03_efficiency_ratio(closeadj, 21)
    e63 = _f03_efficiency_ratio(closeadj, 63)
    e126 = _f03_efficiency_ratio(closeadj, 126)
    b = e21 - 2.0 * e63 + e126
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-streak vs down-streak count ratio over 252d (advance/decline run frequency)
def f03mp_f03_momentum_persistence_runfreqratio_252d_base_v138_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    # count run starts (streak resets to +1 or -1)
    up_start = ((s == 1) & (s.shift(1) <= 0)).astype(float)
    dn_start = ((s == -1) & (s.shift(1) >= 0)).astype(float)
    uc = up_start.rolling(252, min_periods=126).sum()
    dc = dn_start.rolling(252, min_periods=126).sum()
    b = (uc - dc) / (uc + dc).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum drawup persistence: longest cumulative-gain run length proxy over 126d
def f03mp_f03_momentum_persistence_drawup_126d_base_v139_signal(closeadj):
    r = closeadj.pct_change()
    cum = r.rolling(126, min_periods=63).sum()
    # distance of current cum-return from its trailing min over 126d (run-up height)
    mn = cum.rolling(63, min_periods=21).min()
    b = cum - mn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr lag1 over 252d minus VR-implied persistence (cross-method disagreement)
def f03mp_f03_momentum_persistence_methoddiff_252d_base_v140_signal(closeadj):
    a1 = _f03_autocorr(closeadj, 252, 1)
    v = _f03_variance_ratio(closeadj, 252, 2) - 1.0
    b = a1 - v
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day fraction weighted by 126d efficiency (clean directional bias, long)
def f03mp_f03_momentum_persistence_cleantrend_126d_base_v141_signal(closeadj):
    tf = _f03_trend_day_frac(closeadj, 126)
    e = _f03_efficiency_ratio(closeadj, 126)
    b = tf * e
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling skewness of daily returns over 126d (asymmetry of trend moves)
def f03mp_f03_momentum_persistence_retskew_126d_base_v142_signal(closeadj):
    r = closeadj.pct_change()
    b = r.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# persistence composite: Hurst-dev + VR-dev + efficiency over 252d (consensus trendiness)
def f03mp_f03_momentum_persistence_consensus_252d_base_v143_signal(closeadj):
    h = _f03_hurst_rs(closeadj, 252) - 0.5
    v = _f03_variance_ratio(closeadj, 252, 5) - 1.0
    e = _f03_efficiency_ratio(closeadj, 252) - 0.5
    b = h + v + e
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio z over 21d vs 126d history (short cleanliness extremity)
def f03mp_f03_momentum_persistence_effz_21d_base_v144_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 21)
    b = _z(e, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr lag1 EMA over 252d (very smooth persistence regime)
def f03mp_f03_momentum_persistence_acema_252d_base_v145_signal(closeadj):
    a1 = _f03_autocorr(closeadj, 252, 1)
    b = a1.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net cumulative return / total absolute return over 252d, z-scored (long log-efficiency)
def f03mp_f03_momentum_persistence_logeffz_252d_base_v146_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(252, min_periods=126).sum()
    path = lr.abs().rolling(252, min_periods=126).sum()
    se = net / path.replace(0, np.nan)
    b = _z(se, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling kurtosis of daily returns over 126d (fat-tailed lumpiness of trend moves)
def f03mp_f03_momentum_persistence_retkurt_126d_base_v147_signal(closeadj):
    r = closeadj.pct_change()
    b = r.rolling(126, min_periods=63).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-aligned volatility: share of variance on trend-direction days over 126d
def f03mp_f03_momentum_persistence_trendvol_126d_base_v148_signal(closeadj):
    r = closeadj.pct_change()
    net = r.rolling(126, min_periods=63).sum()
    aligned = r.where(np.sign(r) == np.sign(net), 0.0)
    av = (aligned ** 2).rolling(126, min_periods=63).sum()
    tv = (r ** 2).rolling(126, min_periods=63).sum()
    b = av / tv.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst-deviation x efficiency interaction over 126d (double-confirmed persistence)
def f03mp_f03_momentum_persistence_hursteff_126d_base_v149_signal(closeadj):
    h = _f03_hurst_rs(closeadj, 126) - 0.5
    e = _f03_efficiency_ratio(closeadj, 126)
    b = h * e
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# grand persistence score: efficiency x sign-agreement x (1+|drift/vol|) over 252d
def f03mp_f03_momentum_persistence_grand_252d_base_v150_signal(closeadj):
    e = _f03_efficiency_ratio(closeadj, 252)
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(252, min_periods=126).sum()
    sub = lr.rolling(21).sum()
    agree = (np.sign(sub) * np.sign(net)).rolling(252, min_periods=126).mean()
    r = closeadj.pct_change()
    dn = (_mean(r, 252) / _std(r, 252)).abs()
    b = e * agree * (1.0 + dn)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03mp_f03_momentum_persistence_effratio_5d_base_v076_signal,
    f03mp_f03_momentum_persistence_effratio_42d_base_v077_signal,
    f03mp_f03_momentum_persistence_effratio_189d_base_v078_signal,
    f03mp_f03_momentum_persistence_effratio_504d_base_v079_signal,
    f03mp_f03_momentum_persistence_effdisp_126d_base_v080_signal,
    f03mp_f03_momentum_persistence_effabove_126d_base_v081_signal,
    f03mp_f03_momentum_persistence_effema_63d_base_v082_signal,
    f03mp_f03_momentum_persistence_signeffchg_63d_base_v083_signal,
    f03mp_f03_momentum_persistence_effaccel_21d_base_v084_signal,
    f03mp_f03_momentum_persistence_effrank_252d_base_v085_signal,
    f03mp_f03_momentum_persistence_ac2_126d_base_v086_signal,
    f03mp_f03_momentum_persistence_ac3_252d_base_v087_signal,
    f03mp_f03_momentum_persistence_acavg_126d_base_v088_signal,
    f03mp_f03_momentum_persistence_acdecay_252d_base_v089_signal,
    f03mp_f03_momentum_persistence_acrank_63d_base_v090_signal,
    f03mp_f03_momentum_persistence_acmo_252d_base_v091_signal,
    f03mp_f03_momentum_persistence_acz_126d_base_v092_signal,
    f03mp_f03_momentum_persistence_hurst_189d_base_v093_signal,
    f03mp_f03_momentum_persistence_hurst_504d_base_v094_signal,
    f03mp_f03_momentum_persistence_hurstema_126d_base_v095_signal,
    f03mp_f03_momentum_persistence_hurstrank_252d_base_v096_signal,
    f03mp_f03_momentum_persistence_hurstdir_252d_base_v097_signal,
    f03mp_f03_momentum_persistence_hurstdisp_252d_base_v098_signal,
    f03mp_f03_momentum_persistence_vr3_126d_base_v099_signal,
    f03mp_f03_momentum_persistence_vr21_252d_base_v100_signal,
    f03mp_f03_momentum_persistence_vrema_126d_base_v101_signal,
    f03mp_f03_momentum_persistence_vrrank_252d_base_v102_signal,
    f03mp_f03_momentum_persistence_vrprofile_252d_base_v103_signal,
    f03mp_f03_momentum_persistence_vrdisp_252d_base_v104_signal,
    f03mp_f03_momentum_persistence_maxup_126d_base_v105_signal,
    f03mp_f03_momentum_persistence_maxdn_126d_base_v106_signal,
    f03mp_f03_momentum_persistence_streakcap_126d_base_v107_signal,
    f03mp_f03_momentum_persistence_avgsignrun_126d_base_v108_signal,
    f03mp_f03_momentum_persistence_streakvol_126d_base_v109_signal,
    f03mp_f03_momentum_persistence_runexcess_63d_base_v110_signal,
    f03mp_f03_momentum_persistence_flipchg_63d_base_v111_signal,
    f03mp_f03_momentum_persistence_trendfrac_21d_base_v112_signal,
    f03mp_f03_momentum_persistence_trendfracchg_126d_base_v113_signal,
    f03mp_f03_momentum_persistence_glasym_126d_base_v114_signal,
    f03mp_f03_momentum_persistence_trendt_252d_base_v115_signal,
    f03mp_f03_momentum_persistence_trendr2_252d_base_v116_signal,
    f03mp_f03_momentum_persistence_trendr2chg_126d_base_v117_signal,
    f03mp_f03_momentum_persistence_roccons_63d_base_v118_signal,
    f03mp_f03_momentum_persistence_momagree_126d_base_v119_signal,
    f03mp_f03_momentum_persistence_effmom_252d_base_v120_signal,
    f03mp_f03_momentum_persistence_hurstmom_126d_base_v121_signal,
    f03mp_f03_momentum_persistence_slopenoise_126d_base_v122_signal,
    f03mp_f03_momentum_persistence_roughness_126d_base_v123_signal,
    f03mp_f03_momentum_persistence_fractal_126d_base_v124_signal,
    f03mp_f03_momentum_persistence_subagree_252d_base_v125_signal,
    f03mp_f03_momentum_persistence_sortino_21d_base_v126_signal,
    f03mp_f03_momentum_persistence_kamasc_21d_base_v127_signal,
    f03mp_f03_momentum_persistence_persbal_63d_base_v128_signal,
    f03mp_f03_momentum_persistence_runprofit_126d_base_v129_signal,
    f03mp_f03_momentum_persistence_slopestab_126d_base_v130_signal,
    f03mp_f03_momentum_persistence_vrhurst_252d_base_v131_signal,
    f03mp_f03_momentum_persistence_accurv_126d_base_v132_signal,
    f03mp_f03_momentum_persistence_trendtime_252d_base_v133_signal,
    f03mp_f03_momentum_persistence_rochalflife_252d_base_v134_signal,
    f03mp_f03_momentum_persistence_signeffspr_252v63_base_v135_signal,
    f03mp_f03_momentum_persistence_trendvar_126d_base_v136_signal,
    f03mp_f03_momentum_persistence_effcurv_base_v137_signal,
    f03mp_f03_momentum_persistence_runfreqratio_252d_base_v138_signal,
    f03mp_f03_momentum_persistence_drawup_126d_base_v139_signal,
    f03mp_f03_momentum_persistence_methoddiff_252d_base_v140_signal,
    f03mp_f03_momentum_persistence_cleantrend_126d_base_v141_signal,
    f03mp_f03_momentum_persistence_retskew_126d_base_v142_signal,
    f03mp_f03_momentum_persistence_consensus_252d_base_v143_signal,
    f03mp_f03_momentum_persistence_effz_21d_base_v144_signal,
    f03mp_f03_momentum_persistence_acema_252d_base_v145_signal,
    f03mp_f03_momentum_persistence_logeffz_252d_base_v146_signal,
    f03mp_f03_momentum_persistence_retkurt_126d_base_v147_signal,
    f03mp_f03_momentum_persistence_trendvol_126d_base_v148_signal,
    f03mp_f03_momentum_persistence_hursteff_126d_base_v149_signal,
    f03mp_f03_momentum_persistence_grand_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_MOMENTUM_PERSISTENCE_REGISTRY_076_150 = REGISTRY


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

    print("OK f03_momentum_persistence_base_076_150_claude: %d features pass" % n_features)
