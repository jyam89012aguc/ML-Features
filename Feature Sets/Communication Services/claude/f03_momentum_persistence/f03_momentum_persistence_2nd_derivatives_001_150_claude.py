import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _d1(base, k):
    # first math derivative: k-step rate of change
    return base - base.shift(k)


def _d2(base, k):
    # second math derivative (jerk): exact second difference at step k
    return base - 2.0 * base.shift(k) + base.shift(2 * k)


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
        out = [np.log(R / S) / np.log(m)]
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


def _f03_trend_day_frac(closeadj, w):
    up = (closeadj.diff() > 0).astype(float)
    return up.rolling(w, min_periods=max(2, w // 2)).mean() - 0.5


def _f03_trend_slope(closeadj, w):
    lp = np.log(closeadj.replace(0, np.nan))
    x = np.arange(w)
    xm = x.mean()
    sxx = ((x - xm) ** 2).sum()

    def _slope(a):
        ym = a.mean()
        return ((x - xm) * (a - ym)).sum() / sxx

    return lp.rolling(w, min_periods=w).apply(_slope, raw=True)


def _f03_updown_streak(closeadj):
    d = np.sign(closeadj.diff().fillna(0.0))
    out = np.zeros(len(d))
    vals = d.values
    run = 0.0
    prev = 0.0
    for i in range(len(vals)):
        sgn = vals[i]
        if sgn == 0:
            run = 0.0
        elif sgn == prev:
            run += sgn
        else:
            run = sgn
        out[i] = run
        prev = sgn
    res = pd.Series(out, index=closeadj.index)
    res.iloc[0] = np.nan
    return res



# eff f-step slope of 21d base
def f03mp_f03_momentum_persistence_efff_21d_slope_v001_signal(closeadj):
    base = _f03_efficiency_ratio(closeadj, 21)
    scale = _std(base, 63)
    deriv = _d1(base, 3)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# eff m-step slope of 21d base
def f03mp_f03_momentum_persistence_effm_21d_slope_v002_signal(closeadj):
    base = _f03_efficiency_ratio(closeadj, 21)
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# eff s-step slope of 21d base
def f03mp_f03_momentum_persistence_effs_21d_slope_v003_signal(closeadj):
    base = _f03_efficiency_ratio(closeadj, 21)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# eff f-step slope of 63d base
def f03mp_f03_momentum_persistence_efff_63d_slope_v004_signal(closeadj):
    base = _f03_efficiency_ratio(closeadj, 63)
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# eff m-step slope of 63d base
def f03mp_f03_momentum_persistence_effm_63d_slope_v005_signal(closeadj):
    base = _f03_efficiency_ratio(closeadj, 63)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# eff s-step slope of 63d base
def f03mp_f03_momentum_persistence_effs_63d_slope_v006_signal(closeadj):
    base = _f03_efficiency_ratio(closeadj, 63)
    scale = _std(base, 63)
    deriv = _d1(base, 20)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# eff f-step slope of 126d base
def f03mp_f03_momentum_persistence_efff_126d_slope_v007_signal(closeadj):
    base = _f03_efficiency_ratio(closeadj, 126)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# eff m-step slope of 126d base
def f03mp_f03_momentum_persistence_effm_126d_slope_v008_signal(closeadj):
    base = _f03_efficiency_ratio(closeadj, 126)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# eff s-step slope of 126d base
def f03mp_f03_momentum_persistence_effs_126d_slope_v009_signal(closeadj):
    base = _f03_efficiency_ratio(closeadj, 126)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# signeff f-step slope of 42d base
def f03mp_f03_momentum_persistence_signefff_42d_slope_v010_signal(closeadj):
    base = _f03_signed_efficiency(closeadj, 42)
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# signeff m-step slope of 42d base
def f03mp_f03_momentum_persistence_signeffm_42d_slope_v011_signal(closeadj):
    base = _f03_signed_efficiency(closeadj, 42)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# signeff s-step slope of 42d base
def f03mp_f03_momentum_persistence_signeffs_42d_slope_v012_signal(closeadj):
    base = _f03_signed_efficiency(closeadj, 42)
    scale = _std(base, 63)
    deriv = _d1(base, 20)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# signeff f-step slope of 84d base
def f03mp_f03_momentum_persistence_signefff_84d_slope_v013_signal(closeadj):
    base = _f03_signed_efficiency(closeadj, 84)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# signeff m-step slope of 84d base
def f03mp_f03_momentum_persistence_signeffm_84d_slope_v014_signal(closeadj):
    base = _f03_signed_efficiency(closeadj, 84)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# signeff s-step slope of 84d base
def f03mp_f03_momentum_persistence_signeffs_84d_slope_v015_signal(closeadj):
    base = _f03_signed_efficiency(closeadj, 84)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# signeff f-step slope of 168d base
def f03mp_f03_momentum_persistence_signefff_168d_slope_v016_signal(closeadj):
    base = _f03_signed_efficiency(closeadj, 168)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# signeff m-step slope of 168d base
def f03mp_f03_momentum_persistence_signeffm_168d_slope_v017_signal(closeadj):
    base = _f03_signed_efficiency(closeadj, 168)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# signeff s-step slope of 168d base
def f03mp_f03_momentum_persistence_signeffs_168d_slope_v018_signal(closeadj):
    base = _f03_signed_efficiency(closeadj, 168)
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac1 f-step slope of 63d base
def f03mp_f03_momentum_persistence_ac1f_63d_slope_v019_signal(closeadj):
    base = _f03_autocorr(closeadj, 63, 1)
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac1 m-step slope of 63d base
def f03mp_f03_momentum_persistence_ac1m_63d_slope_v020_signal(closeadj):
    base = _f03_autocorr(closeadj, 63, 1)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac1 s-step slope of 63d base
def f03mp_f03_momentum_persistence_ac1s_63d_slope_v021_signal(closeadj):
    base = _f03_autocorr(closeadj, 63, 1)
    scale = _std(base, 63)
    deriv = _d1(base, 20)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac1 f-step slope of 126d base
def f03mp_f03_momentum_persistence_ac1f_126d_slope_v022_signal(closeadj):
    base = _f03_autocorr(closeadj, 126, 1)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac1 m-step slope of 126d base
def f03mp_f03_momentum_persistence_ac1m_126d_slope_v023_signal(closeadj):
    base = _f03_autocorr(closeadj, 126, 1)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac1 s-step slope of 126d base
def f03mp_f03_momentum_persistence_ac1s_126d_slope_v024_signal(closeadj):
    base = _f03_autocorr(closeadj, 126, 1)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac1 f-step slope of 252d base
def f03mp_f03_momentum_persistence_ac1f_252d_slope_v025_signal(closeadj):
    base = _f03_autocorr(closeadj, 252, 1)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac1 m-step slope of 252d base
def f03mp_f03_momentum_persistence_ac1m_252d_slope_v026_signal(closeadj):
    base = _f03_autocorr(closeadj, 252, 1)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac1 s-step slope of 252d base
def f03mp_f03_momentum_persistence_ac1s_252d_slope_v027_signal(closeadj):
    base = _f03_autocorr(closeadj, 252, 1)
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac5 f-step slope of 126d base
def f03mp_f03_momentum_persistence_ac5f_126d_slope_v028_signal(closeadj):
    base = _f03_autocorr(closeadj, 126, 5)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac5 m-step slope of 126d base
def f03mp_f03_momentum_persistence_ac5m_126d_slope_v029_signal(closeadj):
    base = _f03_autocorr(closeadj, 126, 5)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac5 s-step slope of 126d base
def f03mp_f03_momentum_persistence_ac5s_126d_slope_v030_signal(closeadj):
    base = _f03_autocorr(closeadj, 126, 5)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac5 f-step slope of 189d base
def f03mp_f03_momentum_persistence_ac5f_189d_slope_v031_signal(closeadj):
    base = _f03_autocorr(closeadj, 189, 5)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac5 m-step slope of 189d base
def f03mp_f03_momentum_persistence_ac5m_189d_slope_v032_signal(closeadj):
    base = _f03_autocorr(closeadj, 189, 5)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac5 s-step slope of 189d base
def f03mp_f03_momentum_persistence_ac5s_189d_slope_v033_signal(closeadj):
    base = _f03_autocorr(closeadj, 189, 5)
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac5 f-step slope of 252d base
def f03mp_f03_momentum_persistence_ac5f_252d_slope_v034_signal(closeadj):
    base = _f03_autocorr(closeadj, 252, 5)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac5 m-step slope of 252d base
def f03mp_f03_momentum_persistence_ac5m_252d_slope_v035_signal(closeadj):
    base = _f03_autocorr(closeadj, 252, 5)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ac5 s-step slope of 252d base
def f03mp_f03_momentum_persistence_ac5s_252d_slope_v036_signal(closeadj):
    base = _f03_autocorr(closeadj, 252, 5)
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# hurst f-step slope of 63d base
def f03mp_f03_momentum_persistence_hurstf_63d_slope_v037_signal(closeadj):
    base = _f03_hurst_rs(closeadj, 63)
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# hurst m-step slope of 63d base
def f03mp_f03_momentum_persistence_hurstm_63d_slope_v038_signal(closeadj):
    base = _f03_hurst_rs(closeadj, 63)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# hurst s-step slope of 63d base
def f03mp_f03_momentum_persistence_hursts_63d_slope_v039_signal(closeadj):
    base = _f03_hurst_rs(closeadj, 63)
    scale = _std(base, 63)
    deriv = _d1(base, 20)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# hurst f-step slope of 126d base
def f03mp_f03_momentum_persistence_hurstf_126d_slope_v040_signal(closeadj):
    base = _f03_hurst_rs(closeadj, 126)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# hurst m-step slope of 126d base
def f03mp_f03_momentum_persistence_hurstm_126d_slope_v041_signal(closeadj):
    base = _f03_hurst_rs(closeadj, 126)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# hurst s-step slope of 126d base
def f03mp_f03_momentum_persistence_hursts_126d_slope_v042_signal(closeadj):
    base = _f03_hurst_rs(closeadj, 126)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# hurst f-step slope of 252d base
def f03mp_f03_momentum_persistence_hurstf_252d_slope_v043_signal(closeadj):
    base = _f03_hurst_rs(closeadj, 252)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# hurst m-step slope of 252d base
def f03mp_f03_momentum_persistence_hurstm_252d_slope_v044_signal(closeadj):
    base = _f03_hurst_rs(closeadj, 252)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# hurst s-step slope of 252d base
def f03mp_f03_momentum_persistence_hursts_252d_slope_v045_signal(closeadj):
    base = _f03_hurst_rs(closeadj, 252)
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr5 f-step slope of 63d base
def f03mp_f03_momentum_persistence_vr5f_63d_slope_v046_signal(closeadj):
    base = _f03_variance_ratio(closeadj, 63, 5)
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr5 m-step slope of 63d base
def f03mp_f03_momentum_persistence_vr5m_63d_slope_v047_signal(closeadj):
    base = _f03_variance_ratio(closeadj, 63, 5)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr5 s-step slope of 63d base
def f03mp_f03_momentum_persistence_vr5s_63d_slope_v048_signal(closeadj):
    base = _f03_variance_ratio(closeadj, 63, 5)
    scale = _std(base, 63)
    deriv = _d1(base, 20)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr5 f-step slope of 126d base
def f03mp_f03_momentum_persistence_vr5f_126d_slope_v049_signal(closeadj):
    base = _f03_variance_ratio(closeadj, 126, 5)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr5 m-step slope of 126d base
def f03mp_f03_momentum_persistence_vr5m_126d_slope_v050_signal(closeadj):
    base = _f03_variance_ratio(closeadj, 126, 5)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr5 s-step slope of 126d base
def f03mp_f03_momentum_persistence_vr5s_126d_slope_v051_signal(closeadj):
    base = _f03_variance_ratio(closeadj, 126, 5)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr5 f-step slope of 252d base
def f03mp_f03_momentum_persistence_vr5f_252d_slope_v052_signal(closeadj):
    base = _f03_variance_ratio(closeadj, 252, 5)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr5 m-step slope of 252d base
def f03mp_f03_momentum_persistence_vr5m_252d_slope_v053_signal(closeadj):
    base = _f03_variance_ratio(closeadj, 252, 5)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr5 s-step slope of 252d base
def f03mp_f03_momentum_persistence_vr5s_252d_slope_v054_signal(closeadj):
    base = _f03_variance_ratio(closeadj, 252, 5)
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr2 f-step slope of 63d base
def f03mp_f03_momentum_persistence_vr2f_63d_slope_v055_signal(closeadj):
    v2 = _f03_variance_ratio(closeadj, 63, 2)
    v3 = _f03_variance_ratio(closeadj, 63, 3)
    base = v3 - 2.0 * v2 + 1.0
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr2 m-step slope of 63d base
def f03mp_f03_momentum_persistence_vr2m_63d_slope_v056_signal(closeadj):
    v2 = _f03_variance_ratio(closeadj, 63, 2)
    v3 = _f03_variance_ratio(closeadj, 63, 3)
    base = v3 - 2.0 * v2 + 1.0
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr2 s-step slope of 63d base
def f03mp_f03_momentum_persistence_vr2s_63d_slope_v057_signal(closeadj):
    v2 = _f03_variance_ratio(closeadj, 63, 2)
    v3 = _f03_variance_ratio(closeadj, 63, 3)
    base = v3 - 2.0 * v2 + 1.0
    scale = _std(base, 63)
    deriv = _d1(base, 20)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr2 f-step slope of 126d base
def f03mp_f03_momentum_persistence_vr2f_126d_slope_v058_signal(closeadj):
    v2 = _f03_variance_ratio(closeadj, 126, 2)
    v3 = _f03_variance_ratio(closeadj, 126, 3)
    base = v3 - 2.0 * v2 + 1.0
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr2 m-step slope of 126d base
def f03mp_f03_momentum_persistence_vr2m_126d_slope_v059_signal(closeadj):
    v2 = _f03_variance_ratio(closeadj, 126, 2)
    v3 = _f03_variance_ratio(closeadj, 126, 3)
    base = v3 - 2.0 * v2 + 1.0
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr2 s-step slope of 126d base
def f03mp_f03_momentum_persistence_vr2s_126d_slope_v060_signal(closeadj):
    v2 = _f03_variance_ratio(closeadj, 126, 2)
    v3 = _f03_variance_ratio(closeadj, 126, 3)
    base = v3 - 2.0 * v2 + 1.0
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr2 f-step slope of 252d base
def f03mp_f03_momentum_persistence_vr2f_252d_slope_v061_signal(closeadj):
    v2 = _f03_variance_ratio(closeadj, 252, 2)
    v3 = _f03_variance_ratio(closeadj, 252, 3)
    base = v3 - 2.0 * v2 + 1.0
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr2 m-step slope of 252d base
def f03mp_f03_momentum_persistence_vr2m_252d_slope_v062_signal(closeadj):
    v2 = _f03_variance_ratio(closeadj, 252, 2)
    v3 = _f03_variance_ratio(closeadj, 252, 3)
    base = v3 - 2.0 * v2 + 1.0
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# vr2 s-step slope of 252d base
def f03mp_f03_momentum_persistence_vr2s_252d_slope_v063_signal(closeadj):
    v2 = _f03_variance_ratio(closeadj, 252, 2)
    v3 = _f03_variance_ratio(closeadj, 252, 3)
    base = v3 - 2.0 * v2 + 1.0
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# trendfrac f-step slope of 42d base
def f03mp_f03_momentum_persistence_trendfracf_42d_slope_v064_signal(closeadj):
    raw = _f03_trend_day_frac(closeadj, 42)
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# trendfrac m-step slope of 42d base
def f03mp_f03_momentum_persistence_trendfracm_42d_slope_v065_signal(closeadj):
    raw = _f03_trend_day_frac(closeadj, 42)
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# trendfrac s-step slope of 42d base
def f03mp_f03_momentum_persistence_trendfracs_42d_slope_v066_signal(closeadj):
    raw = _f03_trend_day_frac(closeadj, 42)
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 20)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# trendfrac f-step slope of 84d base
def f03mp_f03_momentum_persistence_trendfracf_84d_slope_v067_signal(closeadj):
    raw = _f03_trend_day_frac(closeadj, 84)
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# trendfrac m-step slope of 84d base
def f03mp_f03_momentum_persistence_trendfracm_84d_slope_v068_signal(closeadj):
    raw = _f03_trend_day_frac(closeadj, 84)
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# trendfrac s-step slope of 84d base
def f03mp_f03_momentum_persistence_trendfracs_84d_slope_v069_signal(closeadj):
    raw = _f03_trend_day_frac(closeadj, 84)
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# trendfrac f-step slope of 168d base
def f03mp_f03_momentum_persistence_trendfracf_168d_slope_v070_signal(closeadj):
    raw = _f03_trend_day_frac(closeadj, 168)
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# trendfrac m-step slope of 168d base
def f03mp_f03_momentum_persistence_trendfracm_168d_slope_v071_signal(closeadj):
    raw = _f03_trend_day_frac(closeadj, 168)
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# trendfrac s-step slope of 168d base
def f03mp_f03_momentum_persistence_trendfracs_168d_slope_v072_signal(closeadj):
    raw = _f03_trend_day_frac(closeadj, 168)
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope f-step slope of 42d base
def f03mp_f03_momentum_persistence_slopef_42d_slope_v073_signal(closeadj):
    base = _f03_trend_slope(closeadj, 42)
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope m-step slope of 42d base
def f03mp_f03_momentum_persistence_slopem_42d_slope_v074_signal(closeadj):
    base = _f03_trend_slope(closeadj, 42)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope s-step slope of 42d base
def f03mp_f03_momentum_persistence_slopes_42d_slope_v075_signal(closeadj):
    base = _f03_trend_slope(closeadj, 42)
    scale = _std(base, 63)
    deriv = _d1(base, 20)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope f-step slope of 84d base
def f03mp_f03_momentum_persistence_slopef_84d_slope_v076_signal(closeadj):
    base = _f03_trend_slope(closeadj, 84)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope m-step slope of 84d base
def f03mp_f03_momentum_persistence_slopem_84d_slope_v077_signal(closeadj):
    base = _f03_trend_slope(closeadj, 84)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope s-step slope of 84d base
def f03mp_f03_momentum_persistence_slopes_84d_slope_v078_signal(closeadj):
    base = _f03_trend_slope(closeadj, 84)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope f-step slope of 168d base
def f03mp_f03_momentum_persistence_slopef_168d_slope_v079_signal(closeadj):
    base = _f03_trend_slope(closeadj, 168)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope m-step slope of 168d base
def f03mp_f03_momentum_persistence_slopem_168d_slope_v080_signal(closeadj):
    base = _f03_trend_slope(closeadj, 168)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# slope s-step slope of 168d base
def f03mp_f03_momentum_persistence_slopes_168d_slope_v081_signal(closeadj):
    base = _f03_trend_slope(closeadj, 168)
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# spearman f-step slope of 42d base
def f03mp_f03_momentum_persistence_spearmanf_42d_slope_v082_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = lp.rolling(42, min_periods=max(8, 42 // 2)).apply(
        lambda a: np.corrcoef(np.argsort(np.argsort(a)),
                              np.arange(len(a)))[0, 1], raw=True)
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# spearman m-step slope of 42d base
def f03mp_f03_momentum_persistence_spearmanm_42d_slope_v083_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = lp.rolling(42, min_periods=max(8, 42 // 2)).apply(
        lambda a: np.corrcoef(np.argsort(np.argsort(a)),
                              np.arange(len(a)))[0, 1], raw=True)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# spearman s-step slope of 42d base
def f03mp_f03_momentum_persistence_spearmans_42d_slope_v084_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = lp.rolling(42, min_periods=max(8, 42 // 2)).apply(
        lambda a: np.corrcoef(np.argsort(np.argsort(a)),
                              np.arange(len(a)))[0, 1], raw=True)
    scale = _std(base, 63)
    deriv = _d1(base, 20)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# spearman f-step slope of 84d base
def f03mp_f03_momentum_persistence_spearmanf_84d_slope_v085_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = lp.rolling(84, min_periods=max(8, 84 // 2)).apply(
        lambda a: np.corrcoef(np.argsort(np.argsort(a)),
                              np.arange(len(a)))[0, 1], raw=True)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# spearman m-step slope of 84d base
def f03mp_f03_momentum_persistence_spearmanm_84d_slope_v086_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = lp.rolling(84, min_periods=max(8, 84 // 2)).apply(
        lambda a: np.corrcoef(np.argsort(np.argsort(a)),
                              np.arange(len(a)))[0, 1], raw=True)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# spearman s-step slope of 84d base
def f03mp_f03_momentum_persistence_spearmans_84d_slope_v087_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = lp.rolling(84, min_periods=max(8, 84 // 2)).apply(
        lambda a: np.corrcoef(np.argsort(np.argsort(a)),
                              np.arange(len(a)))[0, 1], raw=True)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# spearman f-step slope of 168d base
def f03mp_f03_momentum_persistence_spearmanf_168d_slope_v088_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = lp.rolling(168, min_periods=max(8, 168 // 2)).apply(
        lambda a: np.corrcoef(np.argsort(np.argsort(a)),
                              np.arange(len(a)))[0, 1], raw=True)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# spearman m-step slope of 168d base
def f03mp_f03_momentum_persistence_spearmanm_168d_slope_v089_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = lp.rolling(168, min_periods=max(8, 168 // 2)).apply(
        lambda a: np.corrcoef(np.argsort(np.argsort(a)),
                              np.arange(len(a)))[0, 1], raw=True)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# spearman s-step slope of 168d base
def f03mp_f03_momentum_persistence_spearmans_168d_slope_v090_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    base = lp.rolling(168, min_periods=max(8, 168 // 2)).apply(
        lambda a: np.corrcoef(np.argsort(np.argsort(a)),
                              np.arange(len(a)))[0, 1], raw=True)
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# magpersist f-step slope of 42d base
def f03mp_f03_momentum_persistence_magpersistf_42d_slope_v091_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(42, min_periods=max(3, 42 // 2)).apply(
        lambda a: np.corrcoef(a[1:], a[:-1])[0, 1]
        if (np.std(a[1:]) > 0 and np.std(a[:-1]) > 0) else np.nan, raw=True)
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# magpersist m-step slope of 42d base
def f03mp_f03_momentum_persistence_magpersistm_42d_slope_v092_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(42, min_periods=max(3, 42 // 2)).apply(
        lambda a: np.corrcoef(a[1:], a[:-1])[0, 1]
        if (np.std(a[1:]) > 0 and np.std(a[:-1]) > 0) else np.nan, raw=True)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# magpersist s-step slope of 42d base
def f03mp_f03_momentum_persistence_magpersists_42d_slope_v093_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(42, min_periods=max(3, 42 // 2)).apply(
        lambda a: np.corrcoef(a[1:], a[:-1])[0, 1]
        if (np.std(a[1:]) > 0 and np.std(a[:-1]) > 0) else np.nan, raw=True)
    scale = _std(base, 63)
    deriv = _d1(base, 20)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# magpersist f-step slope of 84d base
def f03mp_f03_momentum_persistence_magpersistf_84d_slope_v094_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(84, min_periods=max(3, 84 // 2)).apply(
        lambda a: np.corrcoef(a[1:], a[:-1])[0, 1]
        if (np.std(a[1:]) > 0 and np.std(a[:-1]) > 0) else np.nan, raw=True)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# magpersist m-step slope of 84d base
def f03mp_f03_momentum_persistence_magpersistm_84d_slope_v095_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(84, min_periods=max(3, 84 // 2)).apply(
        lambda a: np.corrcoef(a[1:], a[:-1])[0, 1]
        if (np.std(a[1:]) > 0 and np.std(a[:-1]) > 0) else np.nan, raw=True)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# magpersist s-step slope of 84d base
def f03mp_f03_momentum_persistence_magpersists_84d_slope_v096_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(84, min_periods=max(3, 84 // 2)).apply(
        lambda a: np.corrcoef(a[1:], a[:-1])[0, 1]
        if (np.std(a[1:]) > 0 and np.std(a[:-1]) > 0) else np.nan, raw=True)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# magpersist f-step slope of 168d base
def f03mp_f03_momentum_persistence_magpersistf_168d_slope_v097_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(168, min_periods=max(3, 168 // 2)).apply(
        lambda a: np.corrcoef(a[1:], a[:-1])[0, 1]
        if (np.std(a[1:]) > 0 and np.std(a[:-1]) > 0) else np.nan, raw=True)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# magpersist m-step slope of 168d base
def f03mp_f03_momentum_persistence_magpersistm_168d_slope_v098_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(168, min_periods=max(3, 168 // 2)).apply(
        lambda a: np.corrcoef(a[1:], a[:-1])[0, 1]
        if (np.std(a[1:]) > 0 and np.std(a[:-1]) > 0) else np.nan, raw=True)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# magpersist s-step slope of 168d base
def f03mp_f03_momentum_persistence_magpersists_168d_slope_v099_signal(closeadj):
    r2 = closeadj.pct_change() ** 2
    base = r2.rolling(168, min_periods=max(3, 168 // 2)).apply(
        lambda a: np.corrcoef(a[1:], a[:-1])[0, 1]
        if (np.std(a[1:]) > 0 and np.std(a[:-1]) > 0) else np.nan, raw=True)
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgrun f-step slope of 42d base
def f03mp_f03_momentum_persistence_avgrunf_42d_slope_v100_signal(closeadj):
    s = _f03_updown_streak(closeadj).abs()
    raw = s.rolling(42, min_periods=21).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgrun m-step slope of 42d base
def f03mp_f03_momentum_persistence_avgrunm_42d_slope_v101_signal(closeadj):
    s = _f03_updown_streak(closeadj).abs()
    raw = s.rolling(42, min_periods=21).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgrun s-step slope of 42d base
def f03mp_f03_momentum_persistence_avgruns_42d_slope_v102_signal(closeadj):
    s = _f03_updown_streak(closeadj).abs()
    raw = s.rolling(42, min_periods=21).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 20)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgrun f-step slope of 84d base
def f03mp_f03_momentum_persistence_avgrunf_84d_slope_v103_signal(closeadj):
    s = _f03_updown_streak(closeadj).abs()
    raw = s.rolling(84, min_periods=42).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgrun m-step slope of 84d base
def f03mp_f03_momentum_persistence_avgrunm_84d_slope_v104_signal(closeadj):
    s = _f03_updown_streak(closeadj).abs()
    raw = s.rolling(84, min_periods=42).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgrun s-step slope of 84d base
def f03mp_f03_momentum_persistence_avgruns_84d_slope_v105_signal(closeadj):
    s = _f03_updown_streak(closeadj).abs()
    raw = s.rolling(84, min_periods=42).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgrun f-step slope of 168d base
def f03mp_f03_momentum_persistence_avgrunf_168d_slope_v106_signal(closeadj):
    s = _f03_updown_streak(closeadj).abs()
    raw = s.rolling(168, min_periods=84).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgrun m-step slope of 168d base
def f03mp_f03_momentum_persistence_avgrunm_168d_slope_v107_signal(closeadj):
    s = _f03_updown_streak(closeadj).abs()
    raw = s.rolling(168, min_periods=84).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgrun s-step slope of 168d base
def f03mp_f03_momentum_persistence_avgruns_168d_slope_v108_signal(closeadj):
    s = _f03_updown_streak(closeadj).abs()
    raw = s.rolling(168, min_periods=84).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgsignrun f-step slope of 63d base
def f03mp_f03_momentum_persistence_avgsignrunf_63d_slope_v109_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    raw = s.rolling(63, min_periods=31).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgsignrun m-step slope of 63d base
def f03mp_f03_momentum_persistence_avgsignrunm_63d_slope_v110_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    raw = s.rolling(63, min_periods=31).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgsignrun s-step slope of 63d base
def f03mp_f03_momentum_persistence_avgsignruns_63d_slope_v111_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    raw = s.rolling(63, min_periods=31).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 20)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgsignrun f-step slope of 126d base
def f03mp_f03_momentum_persistence_avgsignrunf_126d_slope_v112_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    raw = s.rolling(126, min_periods=63).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgsignrun m-step slope of 126d base
def f03mp_f03_momentum_persistence_avgsignrunm_126d_slope_v113_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    raw = s.rolling(126, min_periods=63).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgsignrun s-step slope of 126d base
def f03mp_f03_momentum_persistence_avgsignruns_126d_slope_v114_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    raw = s.rolling(126, min_periods=63).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgsignrun f-step slope of 252d base
def f03mp_f03_momentum_persistence_avgsignrunf_252d_slope_v115_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    raw = s.rolling(252, min_periods=126).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgsignrun m-step slope of 252d base
def f03mp_f03_momentum_persistence_avgsignrunm_252d_slope_v116_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    raw = s.rolling(252, min_periods=126).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# avgsignrun s-step slope of 252d base
def f03mp_f03_momentum_persistence_avgsignruns_252d_slope_v117_signal(closeadj):
    s = _f03_updown_streak(closeadj)
    raw = s.rolling(252, min_periods=126).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# upshare f-step slope of 42d base
def f03mp_f03_momentum_persistence_upsharef_42d_slope_v118_signal(closeadj):
    r = closeadj.pct_change()
    au = r.where(r > 0).rolling(42, min_periods=10).mean()
    ad = (-r).where(r < 0).rolling(42, min_periods=10).mean()
    base = (au - ad) / (au + ad).replace(0, np.nan)
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# upshare m-step slope of 42d base
def f03mp_f03_momentum_persistence_upsharem_42d_slope_v119_signal(closeadj):
    r = closeadj.pct_change()
    au = r.where(r > 0).rolling(42, min_periods=10).mean()
    ad = (-r).where(r < 0).rolling(42, min_periods=10).mean()
    base = (au - ad) / (au + ad).replace(0, np.nan)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# upshare s-step slope of 42d base
def f03mp_f03_momentum_persistence_upshares_42d_slope_v120_signal(closeadj):
    r = closeadj.pct_change()
    au = r.where(r > 0).rolling(42, min_periods=10).mean()
    ad = (-r).where(r < 0).rolling(42, min_periods=10).mean()
    base = (au - ad) / (au + ad).replace(0, np.nan)
    scale = _std(base, 63)
    deriv = _d1(base, 20)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# upshare f-step slope of 84d base
def f03mp_f03_momentum_persistence_upsharef_84d_slope_v121_signal(closeadj):
    r = closeadj.pct_change()
    au = r.where(r > 0).rolling(84, min_periods=21).mean()
    ad = (-r).where(r < 0).rolling(84, min_periods=21).mean()
    base = (au - ad) / (au + ad).replace(0, np.nan)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# upshare m-step slope of 84d base
def f03mp_f03_momentum_persistence_upsharem_84d_slope_v122_signal(closeadj):
    r = closeadj.pct_change()
    au = r.where(r > 0).rolling(84, min_periods=21).mean()
    ad = (-r).where(r < 0).rolling(84, min_periods=21).mean()
    base = (au - ad) / (au + ad).replace(0, np.nan)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# upshare s-step slope of 84d base
def f03mp_f03_momentum_persistence_upshares_84d_slope_v123_signal(closeadj):
    r = closeadj.pct_change()
    au = r.where(r > 0).rolling(84, min_periods=21).mean()
    ad = (-r).where(r < 0).rolling(84, min_periods=21).mean()
    base = (au - ad) / (au + ad).replace(0, np.nan)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# upshare f-step slope of 168d base
def f03mp_f03_momentum_persistence_upsharef_168d_slope_v124_signal(closeadj):
    r = closeadj.pct_change()
    au = r.where(r > 0).rolling(168, min_periods=42).mean()
    ad = (-r).where(r < 0).rolling(168, min_periods=42).mean()
    base = (au - ad) / (au + ad).replace(0, np.nan)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# upshare m-step slope of 168d base
def f03mp_f03_momentum_persistence_upsharem_168d_slope_v125_signal(closeadj):
    r = closeadj.pct_change()
    au = r.where(r > 0).rolling(168, min_periods=42).mean()
    ad = (-r).where(r < 0).rolling(168, min_periods=42).mean()
    base = (au - ad) / (au + ad).replace(0, np.nan)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# upshare s-step slope of 168d base
def f03mp_f03_momentum_persistence_upshares_168d_slope_v126_signal(closeadj):
    r = closeadj.pct_change()
    au = r.where(r > 0).rolling(168, min_periods=42).mean()
    ad = (-r).where(r < 0).rolling(168, min_periods=42).mean()
    base = (au - ad) / (au + ad).replace(0, np.nan)
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# roughness f-step slope of 42d base
def f03mp_f03_momentum_persistence_roughnessf_42d_slope_v127_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    path = lp.diff().abs().rolling(42, min_periods=21).sum()
    span = (lp.rolling(42, min_periods=21).max()
            - lp.rolling(42, min_periods=21).min())
    base = path / span.replace(0, np.nan)
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# roughness m-step slope of 42d base
def f03mp_f03_momentum_persistence_roughnessm_42d_slope_v128_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    path = lp.diff().abs().rolling(42, min_periods=21).sum()
    span = (lp.rolling(42, min_periods=21).max()
            - lp.rolling(42, min_periods=21).min())
    base = path / span.replace(0, np.nan)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# roughness s-step slope of 42d base
def f03mp_f03_momentum_persistence_roughnesss_42d_slope_v129_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    path = lp.diff().abs().rolling(42, min_periods=21).sum()
    span = (lp.rolling(42, min_periods=21).max()
            - lp.rolling(42, min_periods=21).min())
    base = path / span.replace(0, np.nan)
    scale = _std(base, 63)
    deriv = _d1(base, 20)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# roughness f-step slope of 84d base
def f03mp_f03_momentum_persistence_roughnessf_84d_slope_v130_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    path = lp.diff().abs().rolling(84, min_periods=42).sum()
    span = (lp.rolling(84, min_periods=42).max()
            - lp.rolling(84, min_periods=42).min())
    base = path / span.replace(0, np.nan)
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# roughness m-step slope of 84d base
def f03mp_f03_momentum_persistence_roughnessm_84d_slope_v131_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    path = lp.diff().abs().rolling(84, min_periods=42).sum()
    span = (lp.rolling(84, min_periods=42).max()
            - lp.rolling(84, min_periods=42).min())
    base = path / span.replace(0, np.nan)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# roughness s-step slope of 84d base
def f03mp_f03_momentum_persistence_roughnesss_84d_slope_v132_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    path = lp.diff().abs().rolling(84, min_periods=42).sum()
    span = (lp.rolling(84, min_periods=42).max()
            - lp.rolling(84, min_periods=42).min())
    base = path / span.replace(0, np.nan)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# roughness f-step slope of 168d base
def f03mp_f03_momentum_persistence_roughnessf_168d_slope_v133_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    path = lp.diff().abs().rolling(168, min_periods=84).sum()
    span = (lp.rolling(168, min_periods=84).max()
            - lp.rolling(168, min_periods=84).min())
    base = path / span.replace(0, np.nan)
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# roughness m-step slope of 168d base
def f03mp_f03_momentum_persistence_roughnessm_168d_slope_v134_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    path = lp.diff().abs().rolling(168, min_periods=84).sum()
    span = (lp.rolling(168, min_periods=84).max()
            - lp.rolling(168, min_periods=84).min())
    base = path / span.replace(0, np.nan)
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# roughness s-step slope of 168d base
def f03mp_f03_momentum_persistence_roughnesss_168d_slope_v135_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    path = lp.diff().abs().rolling(168, min_periods=84).sum()
    span = (lp.rolling(168, min_periods=84).max()
            - lp.rolling(168, min_periods=84).min())
    base = path / span.replace(0, np.nan)
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# subagree f-step slope of 126d base
def f03mp_f03_momentum_persistence_subagreef_126d_slope_v136_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(126, min_periods=63).sum()
    sub = lr.rolling(21).sum()
    agree = np.sign(sub) * np.sign(net)
    raw = agree.rolling(126, min_periods=63).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# subagree m-step slope of 126d base
def f03mp_f03_momentum_persistence_subagreem_126d_slope_v137_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(126, min_periods=63).sum()
    sub = lr.rolling(21).sum()
    agree = np.sign(sub) * np.sign(net)
    raw = agree.rolling(126, min_periods=63).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# subagree s-step slope of 126d base
def f03mp_f03_momentum_persistence_subagrees_126d_slope_v138_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(126, min_periods=63).sum()
    sub = lr.rolling(21).sum()
    agree = np.sign(sub) * np.sign(net)
    raw = agree.rolling(126, min_periods=63).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# subagree f-step slope of 189d base
def f03mp_f03_momentum_persistence_subagreef_189d_slope_v139_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(189, min_periods=94).sum()
    sub = lr.rolling(21).sum()
    agree = np.sign(sub) * np.sign(net)
    raw = agree.rolling(189, min_periods=94).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# subagree m-step slope of 189d base
def f03mp_f03_momentum_persistence_subagreem_189d_slope_v140_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(189, min_periods=94).sum()
    sub = lr.rolling(21).sum()
    agree = np.sign(sub) * np.sign(net)
    raw = agree.rolling(189, min_periods=94).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# subagree s-step slope of 189d base
def f03mp_f03_momentum_persistence_subagrees_189d_slope_v141_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(189, min_periods=94).sum()
    sub = lr.rolling(21).sum()
    agree = np.sign(sub) * np.sign(net)
    raw = agree.rolling(189, min_periods=94).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# subagree f-step slope of 252d base
def f03mp_f03_momentum_persistence_subagreef_252d_slope_v142_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(252, min_periods=126).sum()
    sub = lr.rolling(21).sum()
    agree = np.sign(sub) * np.sign(net)
    raw = agree.rolling(252, min_periods=126).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# subagree m-step slope of 252d base
def f03mp_f03_momentum_persistence_subagreem_252d_slope_v143_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(252, min_periods=126).sum()
    sub = lr.rolling(21).sum()
    agree = np.sign(sub) * np.sign(net)
    raw = agree.rolling(252, min_periods=126).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# subagree s-step slope of 252d base
def f03mp_f03_momentum_persistence_subagrees_252d_slope_v144_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    net = lr.rolling(252, min_periods=126).sum()
    sub = lr.rolling(21).sum()
    agree = np.sign(sub) * np.sign(net)
    raw = agree.rolling(252, min_periods=126).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 252)
    deriv = _d1(base, 84)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# dirpersist f-step slope of 63d base
def f03mp_f03_momentum_persistence_dirpersistf_63d_slope_v145_signal(closeadj):
    d = np.sign(closeadj.diff())
    raw = (d * d.shift(1)).rolling(63, min_periods=31).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 5)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# dirpersist m-step slope of 63d base
def f03mp_f03_momentum_persistence_dirpersistm_63d_slope_v146_signal(closeadj):
    d = np.sign(closeadj.diff())
    raw = (d * d.shift(1)).rolling(63, min_periods=31).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# dirpersist s-step slope of 63d base
def f03mp_f03_momentum_persistence_dirpersists_63d_slope_v147_signal(closeadj):
    d = np.sign(closeadj.diff())
    raw = (d * d.shift(1)).rolling(63, min_periods=31).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 20)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# dirpersist f-step slope of 126d base
def f03mp_f03_momentum_persistence_dirpersistf_126d_slope_v148_signal(closeadj):
    d = np.sign(closeadj.diff())
    raw = (d * d.shift(1)).rolling(126, min_periods=63).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 10)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# dirpersist m-step slope of 126d base
def f03mp_f03_momentum_persistence_dirpersistm_126d_slope_v149_signal(closeadj):
    d = np.sign(closeadj.diff())
    raw = (d * d.shift(1)).rolling(126, min_periods=63).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 63)
    deriv = _d1(base, 21)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# dirpersist s-step slope of 126d base
def f03mp_f03_momentum_persistence_dirpersists_126d_slope_v150_signal(closeadj):
    d = np.sign(closeadj.diff())
    raw = (d * d.shift(1)).rolling(126, min_periods=63).mean()
    base = raw.ewm(span=11, min_periods=5).mean()
    scale = _std(base, 126)
    deriv = _d1(base, 42)
    result = deriv / scale.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f03mp_f03_momentum_persistence_efff_21d_slope_v001_signal,
    f03mp_f03_momentum_persistence_effm_21d_slope_v002_signal,
    f03mp_f03_momentum_persistence_effs_21d_slope_v003_signal,
    f03mp_f03_momentum_persistence_efff_63d_slope_v004_signal,
    f03mp_f03_momentum_persistence_effm_63d_slope_v005_signal,
    f03mp_f03_momentum_persistence_effs_63d_slope_v006_signal,
    f03mp_f03_momentum_persistence_efff_126d_slope_v007_signal,
    f03mp_f03_momentum_persistence_effm_126d_slope_v008_signal,
    f03mp_f03_momentum_persistence_effs_126d_slope_v009_signal,
    f03mp_f03_momentum_persistence_signefff_42d_slope_v010_signal,
    f03mp_f03_momentum_persistence_signeffm_42d_slope_v011_signal,
    f03mp_f03_momentum_persistence_signeffs_42d_slope_v012_signal,
    f03mp_f03_momentum_persistence_signefff_84d_slope_v013_signal,
    f03mp_f03_momentum_persistence_signeffm_84d_slope_v014_signal,
    f03mp_f03_momentum_persistence_signeffs_84d_slope_v015_signal,
    f03mp_f03_momentum_persistence_signefff_168d_slope_v016_signal,
    f03mp_f03_momentum_persistence_signeffm_168d_slope_v017_signal,
    f03mp_f03_momentum_persistence_signeffs_168d_slope_v018_signal,
    f03mp_f03_momentum_persistence_ac1f_63d_slope_v019_signal,
    f03mp_f03_momentum_persistence_ac1m_63d_slope_v020_signal,
    f03mp_f03_momentum_persistence_ac1s_63d_slope_v021_signal,
    f03mp_f03_momentum_persistence_ac1f_126d_slope_v022_signal,
    f03mp_f03_momentum_persistence_ac1m_126d_slope_v023_signal,
    f03mp_f03_momentum_persistence_ac1s_126d_slope_v024_signal,
    f03mp_f03_momentum_persistence_ac1f_252d_slope_v025_signal,
    f03mp_f03_momentum_persistence_ac1m_252d_slope_v026_signal,
    f03mp_f03_momentum_persistence_ac1s_252d_slope_v027_signal,
    f03mp_f03_momentum_persistence_ac5f_126d_slope_v028_signal,
    f03mp_f03_momentum_persistence_ac5m_126d_slope_v029_signal,
    f03mp_f03_momentum_persistence_ac5s_126d_slope_v030_signal,
    f03mp_f03_momentum_persistence_ac5f_189d_slope_v031_signal,
    f03mp_f03_momentum_persistence_ac5m_189d_slope_v032_signal,
    f03mp_f03_momentum_persistence_ac5s_189d_slope_v033_signal,
    f03mp_f03_momentum_persistence_ac5f_252d_slope_v034_signal,
    f03mp_f03_momentum_persistence_ac5m_252d_slope_v035_signal,
    f03mp_f03_momentum_persistence_ac5s_252d_slope_v036_signal,
    f03mp_f03_momentum_persistence_hurstf_63d_slope_v037_signal,
    f03mp_f03_momentum_persistence_hurstm_63d_slope_v038_signal,
    f03mp_f03_momentum_persistence_hursts_63d_slope_v039_signal,
    f03mp_f03_momentum_persistence_hurstf_126d_slope_v040_signal,
    f03mp_f03_momentum_persistence_hurstm_126d_slope_v041_signal,
    f03mp_f03_momentum_persistence_hursts_126d_slope_v042_signal,
    f03mp_f03_momentum_persistence_hurstf_252d_slope_v043_signal,
    f03mp_f03_momentum_persistence_hurstm_252d_slope_v044_signal,
    f03mp_f03_momentum_persistence_hursts_252d_slope_v045_signal,
    f03mp_f03_momentum_persistence_vr5f_63d_slope_v046_signal,
    f03mp_f03_momentum_persistence_vr5m_63d_slope_v047_signal,
    f03mp_f03_momentum_persistence_vr5s_63d_slope_v048_signal,
    f03mp_f03_momentum_persistence_vr5f_126d_slope_v049_signal,
    f03mp_f03_momentum_persistence_vr5m_126d_slope_v050_signal,
    f03mp_f03_momentum_persistence_vr5s_126d_slope_v051_signal,
    f03mp_f03_momentum_persistence_vr5f_252d_slope_v052_signal,
    f03mp_f03_momentum_persistence_vr5m_252d_slope_v053_signal,
    f03mp_f03_momentum_persistence_vr5s_252d_slope_v054_signal,
    f03mp_f03_momentum_persistence_vr2f_63d_slope_v055_signal,
    f03mp_f03_momentum_persistence_vr2m_63d_slope_v056_signal,
    f03mp_f03_momentum_persistence_vr2s_63d_slope_v057_signal,
    f03mp_f03_momentum_persistence_vr2f_126d_slope_v058_signal,
    f03mp_f03_momentum_persistence_vr2m_126d_slope_v059_signal,
    f03mp_f03_momentum_persistence_vr2s_126d_slope_v060_signal,
    f03mp_f03_momentum_persistence_vr2f_252d_slope_v061_signal,
    f03mp_f03_momentum_persistence_vr2m_252d_slope_v062_signal,
    f03mp_f03_momentum_persistence_vr2s_252d_slope_v063_signal,
    f03mp_f03_momentum_persistence_trendfracf_42d_slope_v064_signal,
    f03mp_f03_momentum_persistence_trendfracm_42d_slope_v065_signal,
    f03mp_f03_momentum_persistence_trendfracs_42d_slope_v066_signal,
    f03mp_f03_momentum_persistence_trendfracf_84d_slope_v067_signal,
    f03mp_f03_momentum_persistence_trendfracm_84d_slope_v068_signal,
    f03mp_f03_momentum_persistence_trendfracs_84d_slope_v069_signal,
    f03mp_f03_momentum_persistence_trendfracf_168d_slope_v070_signal,
    f03mp_f03_momentum_persistence_trendfracm_168d_slope_v071_signal,
    f03mp_f03_momentum_persistence_trendfracs_168d_slope_v072_signal,
    f03mp_f03_momentum_persistence_slopef_42d_slope_v073_signal,
    f03mp_f03_momentum_persistence_slopem_42d_slope_v074_signal,
    f03mp_f03_momentum_persistence_slopes_42d_slope_v075_signal,
    f03mp_f03_momentum_persistence_slopef_84d_slope_v076_signal,
    f03mp_f03_momentum_persistence_slopem_84d_slope_v077_signal,
    f03mp_f03_momentum_persistence_slopes_84d_slope_v078_signal,
    f03mp_f03_momentum_persistence_slopef_168d_slope_v079_signal,
    f03mp_f03_momentum_persistence_slopem_168d_slope_v080_signal,
    f03mp_f03_momentum_persistence_slopes_168d_slope_v081_signal,
    f03mp_f03_momentum_persistence_spearmanf_42d_slope_v082_signal,
    f03mp_f03_momentum_persistence_spearmanm_42d_slope_v083_signal,
    f03mp_f03_momentum_persistence_spearmans_42d_slope_v084_signal,
    f03mp_f03_momentum_persistence_spearmanf_84d_slope_v085_signal,
    f03mp_f03_momentum_persistence_spearmanm_84d_slope_v086_signal,
    f03mp_f03_momentum_persistence_spearmans_84d_slope_v087_signal,
    f03mp_f03_momentum_persistence_spearmanf_168d_slope_v088_signal,
    f03mp_f03_momentum_persistence_spearmanm_168d_slope_v089_signal,
    f03mp_f03_momentum_persistence_spearmans_168d_slope_v090_signal,
    f03mp_f03_momentum_persistence_magpersistf_42d_slope_v091_signal,
    f03mp_f03_momentum_persistence_magpersistm_42d_slope_v092_signal,
    f03mp_f03_momentum_persistence_magpersists_42d_slope_v093_signal,
    f03mp_f03_momentum_persistence_magpersistf_84d_slope_v094_signal,
    f03mp_f03_momentum_persistence_magpersistm_84d_slope_v095_signal,
    f03mp_f03_momentum_persistence_magpersists_84d_slope_v096_signal,
    f03mp_f03_momentum_persistence_magpersistf_168d_slope_v097_signal,
    f03mp_f03_momentum_persistence_magpersistm_168d_slope_v098_signal,
    f03mp_f03_momentum_persistence_magpersists_168d_slope_v099_signal,
    f03mp_f03_momentum_persistence_avgrunf_42d_slope_v100_signal,
    f03mp_f03_momentum_persistence_avgrunm_42d_slope_v101_signal,
    f03mp_f03_momentum_persistence_avgruns_42d_slope_v102_signal,
    f03mp_f03_momentum_persistence_avgrunf_84d_slope_v103_signal,
    f03mp_f03_momentum_persistence_avgrunm_84d_slope_v104_signal,
    f03mp_f03_momentum_persistence_avgruns_84d_slope_v105_signal,
    f03mp_f03_momentum_persistence_avgrunf_168d_slope_v106_signal,
    f03mp_f03_momentum_persistence_avgrunm_168d_slope_v107_signal,
    f03mp_f03_momentum_persistence_avgruns_168d_slope_v108_signal,
    f03mp_f03_momentum_persistence_avgsignrunf_63d_slope_v109_signal,
    f03mp_f03_momentum_persistence_avgsignrunm_63d_slope_v110_signal,
    f03mp_f03_momentum_persistence_avgsignruns_63d_slope_v111_signal,
    f03mp_f03_momentum_persistence_avgsignrunf_126d_slope_v112_signal,
    f03mp_f03_momentum_persistence_avgsignrunm_126d_slope_v113_signal,
    f03mp_f03_momentum_persistence_avgsignruns_126d_slope_v114_signal,
    f03mp_f03_momentum_persistence_avgsignrunf_252d_slope_v115_signal,
    f03mp_f03_momentum_persistence_avgsignrunm_252d_slope_v116_signal,
    f03mp_f03_momentum_persistence_avgsignruns_252d_slope_v117_signal,
    f03mp_f03_momentum_persistence_upsharef_42d_slope_v118_signal,
    f03mp_f03_momentum_persistence_upsharem_42d_slope_v119_signal,
    f03mp_f03_momentum_persistence_upshares_42d_slope_v120_signal,
    f03mp_f03_momentum_persistence_upsharef_84d_slope_v121_signal,
    f03mp_f03_momentum_persistence_upsharem_84d_slope_v122_signal,
    f03mp_f03_momentum_persistence_upshares_84d_slope_v123_signal,
    f03mp_f03_momentum_persistence_upsharef_168d_slope_v124_signal,
    f03mp_f03_momentum_persistence_upsharem_168d_slope_v125_signal,
    f03mp_f03_momentum_persistence_upshares_168d_slope_v126_signal,
    f03mp_f03_momentum_persistence_roughnessf_42d_slope_v127_signal,
    f03mp_f03_momentum_persistence_roughnessm_42d_slope_v128_signal,
    f03mp_f03_momentum_persistence_roughnesss_42d_slope_v129_signal,
    f03mp_f03_momentum_persistence_roughnessf_84d_slope_v130_signal,
    f03mp_f03_momentum_persistence_roughnessm_84d_slope_v131_signal,
    f03mp_f03_momentum_persistence_roughnesss_84d_slope_v132_signal,
    f03mp_f03_momentum_persistence_roughnessf_168d_slope_v133_signal,
    f03mp_f03_momentum_persistence_roughnessm_168d_slope_v134_signal,
    f03mp_f03_momentum_persistence_roughnesss_168d_slope_v135_signal,
    f03mp_f03_momentum_persistence_subagreef_126d_slope_v136_signal,
    f03mp_f03_momentum_persistence_subagreem_126d_slope_v137_signal,
    f03mp_f03_momentum_persistence_subagrees_126d_slope_v138_signal,
    f03mp_f03_momentum_persistence_subagreef_189d_slope_v139_signal,
    f03mp_f03_momentum_persistence_subagreem_189d_slope_v140_signal,
    f03mp_f03_momentum_persistence_subagrees_189d_slope_v141_signal,
    f03mp_f03_momentum_persistence_subagreef_252d_slope_v142_signal,
    f03mp_f03_momentum_persistence_subagreem_252d_slope_v143_signal,
    f03mp_f03_momentum_persistence_subagrees_252d_slope_v144_signal,
    f03mp_f03_momentum_persistence_dirpersistf_63d_slope_v145_signal,
    f03mp_f03_momentum_persistence_dirpersistm_63d_slope_v146_signal,
    f03mp_f03_momentum_persistence_dirpersists_63d_slope_v147_signal,
    f03mp_f03_momentum_persistence_dirpersistf_126d_slope_v148_signal,
    f03mp_f03_momentum_persistence_dirpersistm_126d_slope_v149_signal,
    f03mp_f03_momentum_persistence_dirpersists_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F03_MOMENTUM_PERSISTENCE_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s not subset" % (name, meta["inputs"])
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

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx2 = ai.index.intersection(aj.index)
            if len(idx2) < 30:
                continue
            c = ai.loc[idx2].corr(aj.loc[idx2])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f03_momentum_persistence_2nd_derivatives_001_150_claude: %d features pass" % n_features)
