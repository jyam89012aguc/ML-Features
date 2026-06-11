"""f11_raw_roc_family slope features 001-150 (1st derivative of bases).

Each slope feature is base.diff(k) where k is chosen by the ROC bracket
of the base feature's primary window. k is varied within bracket. Bases
are re-inlined; no calls into the base modules.
NaN policy: replace([inf,-inf], nan) at the final return only.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# v001 base: pct_change(1), window=1, k=5
def f11rc_f11_raw_roc_family_roc_1d_slope_v001_signal(close):
    b = close.pct_change(1)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


# v002 base: pct_change(5), window=5, k=5
def f11rc_f11_raw_roc_family_roc_5d_slope_v002_signal(close):
    b = close.pct_change(5)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


# v003 base: pct_change(21), window=21, k=10
def f11rc_f11_raw_roc_family_roc_21d_slope_v003_signal(close):
    b = close.pct_change(21)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v004 base: pct_change(252), k=63
def f11rc_f11_raw_roc_family_roc_252d_slope_v004_signal(closeadj):
    b = closeadj.pct_change(252)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


# v005 base: log(close/shift(3)), w=3, k=5
def f11rc_f11_raw_roc_family_logret_3d_slope_v005_signal(close):
    b = np.log(close / close.shift(3).replace(0.0, np.nan))
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


# v006 base: log(close/shift(63)), w=63, k=10 (vary from rocrank k=63)
def f11rc_f11_raw_roc_family_logret_63d_slope_v006_signal(closeadj):
    b = np.log(closeadj / closeadj.shift(63).replace(0.0, np.nan))
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v007 base: log(close/shift(126)), w=126, k=63
def f11rc_f11_raw_roc_family_logret_126d_slope_v007_signal(closeadj):
    b = np.log(closeadj / closeadj.shift(126).replace(0.0, np.nan))
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


# v008 base: volatildiff_63 (std(r,21)-std(r,63)), w=63, k=21
def f11rc_f11_raw_roc_family_volatildiff_63d_slope_v008_signal(closeadj):
    r = closeadj.pct_change(1)
    b = r.rolling(21, min_periods=21).std() - r.rolling(63, min_periods=63).std()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v009 base: rocatrnrm_50d, w=50, k=21
def f11rc_f11_raw_roc_family_rocatrnrm_50d_slope_v009_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs(); bb = (high - pc).abs(); c = (low - pc).abs()
    tr = pd.concat([a, bb, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0/50.0, adjust=False, min_periods=50).mean()
    b = closeadj.pct_change(50) / (atr / closeadj.replace(0.0, np.nan)).replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v010 base: roczsc_60d, k=10, normalized
def f11rc_f11_raw_roc_family_roczsc_60d_slope_v010_signal(closeadj):
    roc = closeadj.pct_change(5)
    b = (roc - roc.rolling(60, min_periods=60).mean()) / roc.rolling(60, min_periods=60).std().replace(0.0, np.nan)
    raw = b.diff(10)
    nm = b.abs().rolling(10, min_periods=10).mean()
    return (raw / nm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# v011 base: rocrank_120d, w=120, k=63
def f11rc_f11_raw_roc_family_rocrank_120d_slope_v011_signal(closeadj):
    roc = closeadj.pct_change(21)
    b = roc.rolling(120, min_periods=60).rank(pct=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


# v012 base: rocrgrng_50d, w=50, k=21
def f11rc_f11_raw_roc_family_rocrgrng_50d_slope_v012_signal(closeadj):
    rng = (closeadj.rolling(50, min_periods=50).max() - closeadj.rolling(50, min_periods=50).min()) / closeadj.replace(0.0, np.nan)
    b = closeadj.pct_change(10) / rng.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v013 base: rocdf521_21d, w=21, k=10
def f11rc_f11_raw_roc_family_rocdf521_21d_slope_v013_signal(close):
    b = close.pct_change(5) - close.pct_change(21)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v014 base: rocdf2163_63d, w=63, k=21
def f11rc_f11_raw_roc_family_rocdf2163_63d_slope_v014_signal(closeadj):
    b = closeadj.pct_change(21) - closeadj.pct_change(63)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v015 base: rocdf63252_252d, k=63
def f11rc_f11_raw_roc_family_rocdf63252_252d_slope_v015_signal(closeadj):
    b = closeadj.pct_change(63) - closeadj.pct_change(252)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


# v016 base: rocrat521_21d, w=21, k=5
def f11rc_f11_raw_roc_family_rocrat521_21d_slope_v016_signal(close):
    p5 = close.pct_change(5); p21 = close.pct_change(21)
    same = (np.sign(p5) == np.sign(p21)).astype(float)
    b = same * p5.abs() / p21.abs().replace(0.0, np.nan) * np.sign(p5)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


# v017 base: rocavgmom_63d, k=21
def f11rc_f11_raw_roc_family_rocavgmom_63d_slope_v017_signal(closeadj):
    b = (closeadj.pct_change(5) + closeadj.pct_change(21) + closeadj.pct_change(63)) / 3.0
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v018 base: signroc_5d, w=5, k=5
def f11rc_f11_raw_roc_family_signroc_5d_slope_v018_signal(close):
    b = np.sign(close.pct_change(5))
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


# v019 base: signroc_21d, k=10
def f11rc_f11_raw_roc_family_signroc_21d_slope_v019_signal(close):
    b = np.sign(close.pct_change(21))
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v020 base: signroc_63d, k=21
def f11rc_f11_raw_roc_family_signroc_63d_slope_v020_signal(closeadj):
    b = np.sign(closeadj.pct_change(63))
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v021 base: uprtcnt_21d, k=5
def f11rc_f11_raw_roc_family_uprtcnt_21d_slope_v021_signal(close):
    r = close.pct_change(1)
    b = (r > 0).astype(float).rolling(21, min_periods=21).sum()
    b[r.isna()] = np.nan
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


# v022 base: dnrtcnt_63d, k=21
def f11rc_f11_raw_roc_family_dnrtcnt_63d_slope_v022_signal(closeadj):
    r = closeadj.pct_change(1)
    b = (r < 0).astype(float).rolling(63, min_periods=63).sum()
    b[r.isna()] = np.nan
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v023 base: uprstk_30d (streak), k=10
def f11rc_f11_raw_roc_family_uprstk_30d_slope_v023_signal(close):
    d = close.diff(1)
    up = (d > 0).astype(int)
    grp = (up == 0).cumsum()
    cnt = up.groupby(grp).cumcount() + 1
    b = cnt.where(up == 1, 0).astype(float)
    b[d.isna()] = np.nan
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v024 base: dnstk_30d, k=10
def f11rc_f11_raw_roc_family_dnstk_30d_slope_v024_signal(close):
    d = close.diff(1)
    dn = (d < 0).astype(int)
    grp = (dn == 0).cumsum()
    cnt = dn.groupby(grp).cumcount() + 1
    b = cnt.where(dn == 1, 0).astype(float)
    b[d.isna()] = np.nan
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v025 base: dssince2pct_60d, k=21
def f11rc_f11_raw_roc_family_dssince2pct_60d_slope_v025_signal(close):
    r = close.pct_change(1)
    flag = (r.abs() > 0.02).astype(float)
    def _since(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0: return 60.0
        return float(len(x) - 1 - idx[-1])
    b = flag.rolling(60, min_periods=60).apply(_since, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v026 base: retskew_30d, k=10
def f11rc_f11_raw_roc_family_retskew_30d_slope_v026_signal(closeadj):
    r = closeadj.pct_change(1)
    b = r.rolling(30, min_periods=30).skew()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v027 base: retkurt_60d, k=21
def f11rc_f11_raw_roc_family_retkurt_60d_slope_v027_signal(closeadj):
    r = closeadj.pct_change(1)
    b = r.rolling(60, min_periods=60).kurt()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v028 base: madstd_40d, k=21
def f11rc_f11_raw_roc_family_madstd_40d_slope_v028_signal(closeadj):
    r = closeadj.pct_change(1)
    mad = (r - r.rolling(40, min_periods=40).mean()).abs().rolling(40, min_periods=40).mean()
    sd = r.rolling(40, min_periods=40).std()
    b = mad / sd.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v029 base: winrate_50d, k=10
def f11rc_f11_raw_roc_family_winrate_50d_slope_v029_signal(closeadj):
    r = closeadj.pct_change(1)
    b = (r > 0).astype(float).rolling(50, min_periods=50).mean()
    b[r.isna()] = np.nan
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v030 base: sortino_30d, k=10, normalized
def f11rc_f11_raw_roc_family_sortino_30d_slope_v030_signal(closeadj):
    r = closeadj.pct_change(1)
    mu = r.rolling(30, min_periods=30).mean()
    neg = r.where(r < 0, 0.0)
    dd = (neg ** 2).rolling(30, min_periods=30).mean() ** 0.5
    b = mu / dd.replace(0.0, np.nan)
    raw = b.diff(10)
    nm = b.abs().rolling(10, min_periods=10).mean()
    return (raw / nm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# v031 base: thirdmom_45d, k=10
def f11rc_f11_raw_roc_family_thirdmom_45d_slope_v031_signal(closeadj):
    r = closeadj.pct_change(1)
    mu = r.rolling(45, min_periods=45).mean()
    b = ((r - mu) ** 3).rolling(45, min_periods=45).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v032 base: fourthmom_45d, k=21
def f11rc_f11_raw_roc_family_fourthmom_45d_slope_v032_signal(closeadj):
    r = closeadj.pct_change(1)
    mu = r.rolling(45, min_periods=45).mean()
    b = ((r - mu) ** 4).rolling(45, min_periods=45).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v033 base: absretq75_60d, k=21
def f11rc_f11_raw_roc_family_absretq75_60d_slope_v033_signal(closeadj):
    r = closeadj.pct_change(1).abs()
    b = r.rolling(60, min_periods=60).quantile(0.75)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v034 base: retac1_40d, k=10
def f11rc_f11_raw_roc_family_retac1_40d_slope_v034_signal(closeadj):
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    b = r.rolling(40, min_periods=40).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan, raw=False)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v035 base: retac5_60d, k=21
def f11rc_f11_raw_roc_family_retac5_60d_slope_v035_signal(closeadj):
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    b = r.rolling(60, min_periods=60).apply(
        lambda x: float(pd.Series(x).autocorr(lag=5)) if pd.Series(x).std() > 0 else np.nan, raw=False)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v036 base: volclust_30d, k=10
def f11rc_f11_raw_roc_family_volclust_30d_slope_v036_signal(closeadj):
    r = closeadj.pct_change(1).abs()
    b = r.rolling(30, min_periods=30).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan, raw=False)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v037 base: hurstret_80d, k=21
def f11rc_f11_raw_roc_family_hurstret_80d_slope_v037_signal(closeadj):
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    def _h(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 8: return np.nan
        m = x.mean(); z = np.cumsum(x - m)
        R = float(z.max() - z.min()); S = float(np.std(x, ddof=1))
        if R <= 0 or S <= 0: return np.nan
        return float(np.log(R / S) / np.log(len(x)))
    b = r.rolling(80, min_periods=80).apply(_h, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v038 base: varratio_q10_60d, k=21
def f11rc_f11_raw_roc_family_varratio_q10_60d_slope_v038_signal(closeadj):
    r1 = closeadj.pct_change(1); r10 = closeadj.pct_change(10)
    v1 = r1.rolling(60, min_periods=60).var(ddof=1)
    v10 = r10.rolling(60, min_periods=60).var(ddof=1)
    b = v10 / (10.0 * v1.replace(0.0, np.nan)) - 1.0
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v039 base: pathlen_21d, k=10
def f11rc_f11_raw_roc_family_pathlen_21d_slope_v039_signal(close):
    r = close.pct_change(1).abs()
    b = r.rolling(21, min_periods=21).sum()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v040 base: efficiency_30d, k=10
def f11rc_f11_raw_roc_family_efficiency_30d_slope_v040_signal(closeadj):
    num = (closeadj - closeadj.shift(30)).abs()
    den = closeadj.diff(1).abs().rolling(30, min_periods=30).sum()
    b = num / den.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v041 base: inveff_60d, k=21
def f11rc_f11_raw_roc_family_inveff_60d_slope_v041_signal(closeadj):
    r = closeadj.pct_change(1).abs()
    num = r.rolling(60, min_periods=60).sum()
    den = closeadj.pct_change(60).abs()
    b = num / den.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v042 base: maxdd_60d, k=21
def f11rc_f11_raw_roc_family_maxdd_60d_slope_v042_signal(closeadj):
    def _mdd(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size == 0: return np.nan
        cm = np.maximum.accumulate(x); dd = (x - cm) / cm
        return float(dd.min())
    b = closeadj.rolling(60, min_periods=60).apply(_mdd, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v043 base: recovery_45d, k=10
def f11rc_f11_raw_roc_family_recovery_45d_slope_v043_signal(closeadj):
    lo = closeadj.rolling(45, min_periods=45).min()
    b = closeadj / lo.replace(0.0, np.nan) - 1.0
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v044 base: avgupmag_45d, k=21
def f11rc_f11_raw_roc_family_avgupmag_45d_slope_v044_signal(closeadj):
    r = closeadj.pct_change(1)
    pos_sum = r.where(r > 0, 0.0).rolling(45, min_periods=45).sum()
    pos_cnt = (r > 0).astype(float).rolling(45, min_periods=45).sum()
    b = pos_sum / pos_cnt.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v045 base: maxret_21d, k=5
def f11rc_f11_raw_roc_family_maxret_21d_slope_v045_signal(close):
    r = close.pct_change(1)
    b = r.rolling(21, min_periods=21).max()
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


# v046 base: minret_45d, k=10
def f11rc_f11_raw_roc_family_minret_45d_slope_v046_signal(closeadj):
    r = closeadj.pct_change(1)
    b = r.rolling(45, min_periods=45).min()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v047 base: avgtop5_60d, k=21
def f11rc_f11_raw_roc_family_avgtop5_60d_slope_v047_signal(closeadj):
    r = closeadj.pct_change(1)
    def _top5(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 5: return np.nan
        return float(np.mean(np.sort(x)[-5:]))
    b = r.rolling(60, min_periods=60).apply(_top5, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v048 base: avgbot5_60d, k=10
def f11rc_f11_raw_roc_family_avgbot5_60d_slope_v048_signal(closeadj):
    r = closeadj.pct_change(1)
    def _bot5(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 5: return np.nan
        return float(np.mean(np.sort(x)[:5]))
    b = r.rolling(60, min_periods=60).apply(_bot5, raw=True)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v049 base: upsemivar_40d, k=10
def f11rc_f11_raw_roc_family_upsemivar_40d_slope_v049_signal(closeadj):
    r = closeadj.pct_change(1)
    up = r.where(r > 0)
    b = up.rolling(40, min_periods=10).var(ddof=1)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v050 base: dnsemivar_40d, k=21
def f11rc_f11_raw_roc_family_dnsemivar_40d_slope_v050_signal(closeadj):
    r = closeadj.pct_change(1)
    up = r.where(r > 0).rolling(40, min_periods=10).var(ddof=1)
    dn = r.where(r < 0).rolling(40, min_periods=10).var(ddof=1)
    tot = r.rolling(40, min_periods=10).var(ddof=1)
    b = (dn - up) / tot.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v051 base: tstat_45d, k=10
def f11rc_f11_raw_roc_family_tstat_45d_slope_v051_signal(closeadj):
    r = closeadj.pct_change(1)
    mu = r.rolling(45, min_periods=45).mean()
    se = r.rolling(45, min_periods=45).std() / (45.0 ** 0.5)
    b = mu / se.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v052 base: tstat_120d, k=63
def f11rc_f11_raw_roc_family_tstat_120d_slope_v052_signal(closeadj):
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    mu = r.rolling(120, min_periods=120).mean()
    se = r.rolling(120, min_periods=120).std() / (120.0 ** 0.5)
    b = mu / se.replace(0.0, np.nan)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


# v053 base: vrm2_30d, k=10
def f11rc_f11_raw_roc_family_vrm2_30d_slope_v053_signal(closeadj):
    r1 = closeadj.diff(1); r2 = closeadj.diff(2)
    v1 = r1.rolling(30, min_periods=30).var(ddof=1)
    v2 = r2.rolling(30, min_periods=30).var(ddof=1)
    b = v2 / (2.0 * v1.replace(0.0, np.nan)) - 1.0
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v054 base: arctandiff_84d, k=21
def f11rc_f11_raw_roc_family_arctandiff_84d_slope_v054_signal(closeadj):
    b = np.arctan(5.0 * (closeadj.pct_change(21) - closeadj.pct_change(84)))
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v055 base: tanhzsc_40d, k=10
def f11rc_f11_raw_roc_family_tanhzsc_40d_slope_v055_signal(closeadj):
    r = closeadj.pct_change(5)
    z = (r - r.rolling(40, min_periods=40).mean()) / r.rolling(40, min_periods=40).std().replace(0.0, np.nan)
    b = np.tanh(z)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v056 base: sigeffic_30d, k=10
def f11rc_f11_raw_roc_family_sigeffic_30d_slope_v056_signal(closeadj):
    num = closeadj - closeadj.shift(30)
    den = closeadj.diff(1).abs().rolling(30, min_periods=30).sum()
    z = num / den.replace(0.0, np.nan)
    b = 1.0 / (1.0 + np.exp(-10.0 * z))
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v057 base: tanhskew_60d, k=21
def f11rc_f11_raw_roc_family_tanhskew_60d_slope_v057_signal(closeadj):
    r = closeadj.pct_change(1)
    mu = r.rolling(60, min_periods=60).mean()
    m3 = ((r - mu) ** 3).rolling(60, min_periods=60).mean()
    s = r.rolling(60, min_periods=60).std()
    sk = m3 / (s ** 3).replace(0.0, np.nan)
    b = np.tanh(sk)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v058 base: pctrnkabs_252d, k=63
def f11rc_f11_raw_roc_family_pctrnkabs_252d_slope_v058_signal(closeadj):
    r = closeadj.pct_change(1).abs()
    b = r.rolling(252, min_periods=120).rank(pct=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


# v059 base: emaroc_10d, k=5
def f11rc_f11_raw_roc_family_emaroc_10d_slope_v059_signal(close):
    r = close.pct_change(10)
    b = r.ewm(span=3, adjust=False, min_periods=3).mean()
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


# v060 base: wmadrocbias_21d, k=10
def f11rc_f11_raw_roc_family_wmadrocbias_21d_slope_v060_signal(close):
    r = close.pct_change(21)
    w = np.arange(1, 6, dtype=float); w /= w.sum()
    wma = r.rolling(5, min_periods=5).apply(lambda x: float(np.dot(x, w)), raw=True)
    sma = r.rolling(5, min_periods=5).mean()
    b = wma - sma
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v061 base: medroc_15d, k=10
def f11rc_f11_raw_roc_family_medroc_15d_slope_v061_signal(close):
    r = close.pct_change(15)
    b = r.rolling(5, min_periods=5).median()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v062 base: trmroc_42d, k=21
def f11rc_f11_raw_roc_family_trmroc_42d_slope_v062_signal(closeadj):
    r = closeadj.pct_change(42)
    def _trim(x):
        if np.any(~np.isfinite(x)): return np.nan
        lo, hi = np.quantile(x, 0.1), np.quantile(x, 0.9)
        z = x[(x >= lo) & (x <= hi)]
        if z.size == 0: return np.nan
        return float(np.mean(z))
    b = r.rolling(7, min_periods=7).apply(_trim, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v063 base: trendscore_63d, k=21
def f11rc_f11_raw_roc_family_trendscore_63d_slope_v063_signal(closeadj):
    b = np.sign(closeadj.pct_change(5)) + np.sign(closeadj.pct_change(21)) + np.sign(closeadj.pct_change(63))
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v064 base: signagree5_63d, k=10
def f11rc_f11_raw_roc_family_signagree5_63d_slope_v064_signal(closeadj):
    b = (np.sign(closeadj.pct_change(3)) + np.sign(closeadj.pct_change(10)) +
         np.sign(closeadj.pct_change(21)) + np.sign(closeadj.pct_change(42)) +
         np.sign(closeadj.pct_change(63)))
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v065 base: wavgroc_252d, k=63
def f11rc_f11_raw_roc_family_wavgroc_252d_slope_v065_signal(closeadj):
    p5 = closeadj.pct_change(5); p21 = closeadj.pct_change(21)
    p63 = closeadj.pct_change(63); p126 = closeadj.pct_change(126)
    p252 = closeadj.pct_change(252)
    b = (5.0 * p5 + 4.0 * p21 + 3.0 * p63 + 2.0 * p126 + 1.0 * p252) / 15.0
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


# v066 base: upqtcnt_30d, k=10
def f11rc_f11_raw_roc_family_upqtcnt_30d_slope_v066_signal(closeadj):
    r = closeadj.pct_change(1)
    q75 = r.rolling(60, min_periods=60).quantile(0.75)
    flag = (r > q75).astype(float)
    b = flag.rolling(30, min_periods=30).sum()
    b[q75.isna()] = np.nan
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v067 base: quadrnt_30d, k=10
def f11rc_f11_raw_roc_family_quadrnt_30d_slope_v067_signal(closeadj):
    b = 2.0 * np.sign(closeadj.pct_change(21)) + np.sign(closeadj.pct_change(5))
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v068 base: highrocstk_42d (streak), k=21
def f11rc_f11_raw_roc_family_highrocstk_42d_slope_v068_signal(high):
    d = high.diff(1)
    up = (d > 0).astype(int)
    grp = (up == 0).cumsum()
    cnt = up.groupby(grp).cumcount() + 1
    b = cnt.where(up == 1, 0).astype(float)
    b[d.isna()] = np.nan
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v069 base: lowstkdwn_42d, k=10
def f11rc_f11_raw_roc_family_lowstkdwn_42d_slope_v069_signal(low):
    d = low.diff(1)
    dn = (d < 0).astype(int)
    grp = (dn == 0).cumsum()
    cnt = dn.groupby(grp).cumcount() + 1
    b = cnt.where(dn == 1, 0).astype(float)
    b[d.isna()] = np.nan
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v070 base: hlrocdiff_21d, k=5
def f11rc_f11_raw_roc_family_hlrocdiff_21d_slope_v070_signal(high, low):
    b = high.pct_change(21) - low.pct_change(21)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


# v071 base: openclrocdf_5d, k=5
def f11rc_f11_raw_roc_family_openclrocdf_5d_slope_v071_signal(open_, close):
    b = close.pct_change(5) - open_.pct_change(5)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)




# v073 base: rocclz_50d, k=21
def f11rc_f11_raw_roc_family_rocclz_50d_slope_v073_signal(closeadj):
    r = closeadj.pct_change(1)
    sd = r.rolling(50, min_periods=50).std()
    flag = (r.abs() < 0.25 * sd).astype(float)
    b = flag.rolling(50, min_periods=50).sum()
    b[sd.isna()] = np.nan
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v074 base: logvar_30d, k=21, normalized by base mean to decorrelate from rocsq
def f11rc_f11_raw_roc_family_logvar_30d_slope_v074_signal(closeadj):
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    b = r.rolling(30, min_periods=30).var(ddof=1)
    raw = b.diff(21)
    nm = b.abs().rolling(21, min_periods=21).mean()
    return (raw / nm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# v075 base: jumpfrac_60d, k=21
def f11rc_f11_raw_roc_family_jumpfrac_60d_slope_v075_signal(closeadj):
    r = closeadj.pct_change(1)
    sd = r.rolling(60, min_periods=60).std()
    big = (r.abs() > 2.0 * sd).astype(float)
    rsq = r * r
    jn = (rsq * big).rolling(60, min_periods=60).sum()
    tot = rsq.rolling(60, min_periods=60).sum()
    b = jn / tot.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v076 base: roc_2d, k=5
def f11rc_f11_raw_roc_family_roc_2d_slope_v076_signal(close):
    b = close.pct_change(2)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


# v077 base: roc_10d, k=5 (vary from rocrgrng k=10)
def f11rc_f11_raw_roc_family_roc_10d_slope_v077_signal(close):
    b = close.pct_change(10)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


# v078 base: logret_42d, k=21
def f11rc_f11_raw_roc_family_logret_42d_slope_v078_signal(closeadj):
    b = np.log(closeadj / closeadj.shift(42).replace(0.0, np.nan))
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v079 base: logretkurt_45d, k=10
def f11rc_f11_raw_roc_family_logretkurt_45d_slope_v079_signal(closeadj):
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    b = r.rolling(45, min_periods=45).kurt()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v080 base: rocsemi_40d, k=21
def f11rc_f11_raw_roc_family_rocsemi_40d_slope_v080_signal(closeadj):
    r = closeadj.pct_change(1)
    dn = r.where(r < 0)
    dnstd = dn.rolling(40, min_periods=10).std(ddof=1)
    b = closeadj.pct_change(40) / dnstd.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v081 base: updnstdratio_60d, k=21
def f11rc_f11_raw_roc_family_updnstdratio_60d_slope_v081_signal(closeadj):
    r = closeadj.pct_change(1)
    upstd = r.where(r > 0).rolling(60, min_periods=15).std(ddof=1)
    dnstd = r.where(r < 0).rolling(60, min_periods=15).std(ddof=1)
    b = upstd / dnstd.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v082 base: signsqret_30d, k=10
def f11rc_f11_raw_roc_family_signsqret_30d_slope_v082_signal(closeadj):
    r = closeadj.pct_change(1)
    sw = np.sign(r) * (r ** 2)
    b = sw.rolling(30, min_periods=30).sum()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v083 base: rocsignal_30d, k=21
def f11rc_f11_raw_roc_family_rocsignal_30d_slope_v083_signal(closeadj):
    r = closeadj.pct_change(1)
    mu = r.rolling(30, min_periods=30).mean()
    am = r.abs().rolling(30, min_periods=30).mean()
    b = mu / am.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v084 base: rocdf_15d (3-15), k=5
def f11rc_f11_raw_roc_family_rocdf_15d_slope_v084_signal(close):
    b = close.pct_change(3) - close.pct_change(15)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


# v085 base: rocdf_42d (10-42), k=21
def f11rc_f11_raw_roc_family_rocdf_42d_slope_v085_signal(closeadj):
    b = closeadj.pct_change(10) - closeadj.pct_change(42)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v086 base: rocdf_126d (42-126), k=63
def f11rc_f11_raw_roc_family_rocdf_126d_slope_v086_signal(closeadj):
    b = closeadj.pct_change(42) - closeadj.pct_change(126)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


# v087 base: rocdfsign_63d, k=21
def f11rc_f11_raw_roc_family_rocdfsign_63d_slope_v087_signal(closeadj):
    b = np.sign(closeadj.pct_change(21)) * np.sign(closeadj.pct_change(63))
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v088 base: rocdrop_63d, k=21
def f11rc_f11_raw_roc_family_rocdrop_63d_slope_v088_signal(closeadj):
    b = closeadj.pct_change(21) - 0.5 * closeadj.pct_change(63)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v089 base: uprtcnt_10d, k=10
def f11rc_f11_raw_roc_family_uprtcnt_10d_slope_v089_signal(close):
    r = close.pct_change(1)
    b = (r > 0).astype(float).rolling(10, min_periods=10).sum()
    b[r.isna()] = np.nan
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v090 base: dnrtcnt_21d, k=10 (different from uprtcnt k=5 to break linear-symmetry)
def f11rc_f11_raw_roc_family_dnrtcnt_21d_slope_v090_signal(close):
    r = close.pct_change(1)
    b = (r < 0).astype(float).rolling(21, min_periods=21).sum()
    b[r.isna()] = np.nan
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v091 base: alterncnt_45d, k=21
def f11rc_f11_raw_roc_family_alterncnt_45d_slope_v091_signal(closeadj):
    r = closeadj.pct_change(1)
    s = np.sign(r)
    flip = (s != s.shift(1)).astype(float)
    flip[s.isna() | s.shift(1).isna()] = 0.0
    b = flip.rolling(45, min_periods=45).sum()
    b[r.isna()] = np.nan
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v092 base: dssince5pct_120d, k=63
def f11rc_f11_raw_roc_family_dssince5pct_120d_slope_v092_signal(closeadj):
    r = closeadj.pct_change(5).abs()
    flag = (r > 0.05).astype(float)
    def _since(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0: return 120.0
        return float(len(x) - 1 - idx[-1])
    b = flag.rolling(120, min_periods=120).apply(_since, raw=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


# v093 base: signstreak_30d, k=10
def f11rc_f11_raw_roc_family_signstreak_30d_slope_v093_signal(close):
    r = close.pct_change(1)
    s = np.sign(r)
    chg = (s != s.shift(1)).astype(int)
    chg[s.isna() | s.shift(1).isna()] = 0
    grp = chg.cumsum()
    cnt = s.groupby(grp).cumcount() + 1
    b = cnt.astype(float) * s
    b[r.isna()] = np.nan
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v094 base: bigupcnt_60d, k=21
def f11rc_f11_raw_roc_family_bigupcnt_60d_slope_v094_signal(closeadj):
    r = closeadj.pct_change(1)
    sd = r.rolling(60, min_periods=60).std()
    big = (r > 1.5 * sd).astype(float)
    b = big.rolling(60, min_periods=60).sum()
    b[sd.isna()] = np.nan
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v095 base: retskew_90d, k=21
def f11rc_f11_raw_roc_family_retskew_90d_slope_v095_signal(closeadj):
    r = closeadj.pct_change(1)
    b = r.rolling(90, min_periods=90).skew()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v096 base: retkurt_30d, k=10
def f11rc_f11_raw_roc_family_retkurt_30d_slope_v096_signal(closeadj):
    r = closeadj.pct_change(1)
    b = r.rolling(30, min_periods=30).kurt()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v097 base: logretskew_50d, k=10
def f11rc_f11_raw_roc_family_logretskew_50d_slope_v097_signal(closeadj):
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    b = r.rolling(50, min_periods=50).skew()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v098 base: winratio_90d, k=21
def f11rc_f11_raw_roc_family_winratio_90d_slope_v098_signal(closeadj):
    r = closeadj.pct_change(1)
    pos = r.where(r > 0, 0.0).rolling(90, min_periods=90).sum()
    neg = r.where(r < 0, 0.0).rolling(90, min_periods=90).sum().abs()
    b = pos / neg.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v099 base: avgdnmag_45d, k=10
def f11rc_f11_raw_roc_family_avgdnmag_45d_slope_v099_signal(closeadj):
    r = closeadj.pct_change(1)
    ns = r.where(r < 0, 0.0).rolling(45, min_periods=45).sum().abs()
    nc = (r < 0).astype(float).rolling(45, min_periods=45).sum()
    b = ns / nc.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v100 base: retac3_50d, k=21
def f11rc_f11_raw_roc_family_retac3_50d_slope_v100_signal(closeadj):
    r = closeadj.pct_change(1)
    b = r.rolling(50, min_periods=50).apply(
        lambda x: float(pd.Series(x).autocorr(lag=3)) if pd.Series(x).std() > 0 else np.nan, raw=False)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v101 base: signac1_60d, k=10
def f11rc_f11_raw_roc_family_signac1_60d_slope_v101_signal(closeadj):
    s = np.sign(closeadj.pct_change(1))
    b = s.rolling(60, min_periods=60).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan, raw=False)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v102 base: sqrac1_45d, k=21
def f11rc_f11_raw_roc_family_sqrac1_45d_slope_v102_signal(closeadj):
    r = closeadj.pct_change(1) ** 2
    b = r.rolling(45, min_periods=45).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan, raw=False)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v103 base: pathlen_60d, k=21
def f11rc_f11_raw_roc_family_pathlen_60d_slope_v103_signal(closeadj):
    r = closeadj.pct_change(1).abs()
    b = r.rolling(60, min_periods=60).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)




# v105 base: pathvsstd_30d, k=10
def f11rc_f11_raw_roc_family_pathvsstd_30d_slope_v105_signal(closeadj):
    r = closeadj.pct_change(1)
    path = r.abs().rolling(30, min_periods=30).sum()
    sd = r.rolling(30, min_periods=30).std()
    b = path / (sd * (30.0 ** 0.5)).replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v106 base: maxdd_120d, k=63
def f11rc_f11_raw_roc_family_maxdd_120d_slope_v106_signal(closeadj):
    def _mdd(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size == 0: return np.nan
        cm = np.maximum.accumulate(x); dd = (x - cm) / cm
        return float(dd.min())
    b = closeadj.rolling(120, min_periods=120).apply(_mdd, raw=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


# v107 base: drwdwn_30d, k=10
def f11rc_f11_raw_roc_family_drwdwn_30d_slope_v107_signal(closeadj):
    hi = closeadj.rolling(30, min_periods=30).max()
    b = (closeadj - hi) / hi.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v108 base: topbotrng_45d, k=21
def f11rc_f11_raw_roc_family_topbotrng_45d_slope_v108_signal(closeadj):
    r = closeadj.pct_change(1)
    b = r.rolling(45, min_periods=45).max() - r.rolling(45, min_periods=45).min()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v109 base: avgtop3_30d, k=10
def f11rc_f11_raw_roc_family_avgtop3_30d_slope_v109_signal(closeadj):
    r = closeadj.pct_change(1)
    def _top3(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 3: return np.nan
        return float(np.mean(np.sort(x)[-3:]))
    b = r.rolling(30, min_periods=30).apply(_top3, raw=True)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v110 base: avgbot3_30d, k=21
def f11rc_f11_raw_roc_family_avgbot3_30d_slope_v110_signal(closeadj):
    r = closeadj.pct_change(1)
    def _bot3(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 3: return np.nan
        return float(np.mean(np.sort(x)[:3]))
    b = r.rolling(30, min_periods=30).apply(_bot3, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v111 base: iqrret_60d, k=10
def f11rc_f11_raw_roc_family_iqrret_60d_slope_v111_signal(closeadj):
    r = closeadj.pct_change(1)
    q75 = r.rolling(60, min_periods=60).quantile(0.75)
    q25 = r.rolling(60, min_periods=60).quantile(0.25)
    b = q75 - q25
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v112 base: tanharctan_30d, k=10
def f11rc_f11_raw_roc_family_tanharctan_30d_slope_v112_signal(closeadj):
    r = closeadj.pct_change(10)
    z = (r - r.rolling(30, min_periods=30).mean()) / r.rolling(30, min_periods=30).std().replace(0.0, np.nan)
    b = np.tanh(z)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v113 base: arctan_long, k=63, normalized to decorrelate from raw pct(252).diff
def f11rc_f11_raw_roc_family_arctan_long_slope_v113_signal(closeadj):
    b = np.arctan(3.0 * closeadj.pct_change(252))
    raw = b.diff(63)
    # normalize by 63-bar rolling std of |b| to reshape distribution
    nm = b.abs().rolling(63, min_periods=63).mean()
    return (raw / nm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# v114 base: rkdf_60d, k=21
def f11rc_f11_raw_roc_family_rkdf_60d_slope_v114_signal(closeadj):
    rk21 = closeadj.pct_change(21).rolling(120, min_periods=60).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(120, min_periods=60).rank(pct=True)
    b = rk21 - rk63
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v115 base: pctrnk21_60d, k=21
def f11rc_f11_raw_roc_family_pctrnk21_60d_slope_v115_signal(closeadj):
    r = closeadj.pct_change(21)
    b = r.rolling(60, min_periods=30).rank(pct=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v116 base: sigsharpe_90d, k=21
def f11rc_f11_raw_roc_family_sigsharpe_90d_slope_v116_signal(closeadj):
    r = closeadj.pct_change(1)
    mu = r.rolling(90, min_periods=90).mean()
    sd = r.rolling(90, min_periods=90).std()
    z = mu / sd.replace(0.0, np.nan)
    b = 1.0 / (1.0 + np.exp(-50.0 * z))
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v117 base: signalign3_42d, k=10
def f11rc_f11_raw_roc_family_signalign3_42d_slope_v117_signal(closeadj):
    b = np.sign(closeadj.pct_change(10)) * np.sign(closeadj.pct_change(21)) * np.sign(closeadj.pct_change(42))
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v118 base: signsum5_84d, k=21
def f11rc_f11_raw_roc_family_signsum5_84d_slope_v118_signal(closeadj):
    b = (np.sign(closeadj.pct_change(7)) + np.sign(closeadj.pct_change(14)) +
         np.sign(closeadj.pct_change(28)) + np.sign(closeadj.pct_change(56)) +
         np.sign(closeadj.pct_change(84)))
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v119 base: minabs5_30d, k=10
def f11rc_f11_raw_roc_family_minabs5_30d_slope_v119_signal(close):
    r = close.pct_change(1).abs()
    b = r.rolling(30, min_periods=30).min()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v120 base: centmin_pct_60d, k=10
def f11rc_f11_raw_roc_family_centmin_pct_60d_slope_v120_signal(closeadj):
    r = closeadj.pct_change(1)
    sd = r.rolling(60, min_periods=60).std()
    flag = (r.abs() < 0.5 * sd).astype(float)
    b = flag.rolling(60, min_periods=60).sum()
    b[sd.isna()] = np.nan
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v121 base: vrq5_60d, k=21
def f11rc_f11_raw_roc_family_vrq5_60d_slope_v121_signal(closeadj):
    r1 = closeadj.pct_change(1); r5 = closeadj.pct_change(5)
    v1 = r1.rolling(60, min_periods=60).var(ddof=1)
    v5 = r5.rolling(60, min_periods=60).var(ddof=1)
    b = v5 / (5.0 * v1.replace(0.0, np.nan)) - 1.0
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v122 base: vrq20_120d, k=63
def f11rc_f11_raw_roc_family_vrq20_120d_slope_v122_signal(closeadj):
    r1 = closeadj.pct_change(1); r20 = closeadj.pct_change(20)
    v1 = r1.rolling(120, min_periods=120).var(ddof=1)
    v20 = r20.rolling(120, min_periods=120).var(ddof=1)
    b = v20 / (20.0 * v1.replace(0.0, np.nan)) - 1.0
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


# v123 base: tstat_21d, k=5
def f11rc_f11_raw_roc_family_tstat_21d_slope_v123_signal(close):
    r = close.pct_change(1)
    mu = r.rolling(21, min_periods=21).mean()
    se = r.rolling(21, min_periods=21).std() / (21.0 ** 0.5)
    b = mu / se.replace(0.0, np.nan)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


# v124 base: clcldiff_5d, k=5, normalized to decorrelate from raw roc_5 slope
def f11rc_f11_raw_roc_family_clcldiff_5d_slope_v124_signal(open_, close):
    intra = (close - open_) / open_.replace(0.0, np.nan)
    b = close.pct_change(5) - 5.0 * intra.rolling(5, min_periods=5).mean()
    raw = b.diff(5)
    nm = b.abs().rolling(5, min_periods=5).mean()
    return (raw / nm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# v125 base: loretdiff_21d, k=10
def f11rc_f11_raw_roc_family_loretdiff_21d_slope_v125_signal(low, close):
    b = close.pct_change(21) - low.pct_change(21)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v126 base: hiretdiff_21d, k=5
def f11rc_f11_raw_roc_family_hiretdiff_21d_slope_v126_signal(high, close):
    b = close.pct_change(21) - high.pct_change(21)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


# v127 base: openrocstk_42d, k=10
def f11rc_f11_raw_roc_family_openrocstk_42d_slope_v127_signal(open_):
    d = open_.diff(1)
    up = (d > 0).astype(int)
    grp = (up == 0).cumsum()
    cnt = up.groupby(grp).cumcount() + 1
    b = cnt.where(up == 1, 0).astype(float)
    b[d.isna()] = np.nan
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v128 base: emaabsdf_42d, k=21
def f11rc_f11_raw_roc_family_emaabsdf_42d_slope_v128_signal(closeadj):
    a42 = closeadj.pct_change(42).abs()
    a10 = closeadj.pct_change(10).abs()
    b = a42.ewm(span=5, adjust=False, min_periods=5).mean() - a10.ewm(span=5, adjust=False, min_periods=5).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v129 base: medroc_63d, k=21
def f11rc_f11_raw_roc_family_medroc_63d_slope_v129_signal(closeadj):
    r = closeadj.pct_change(63)
    b = r.rolling(7, min_periods=7).median()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v130 base: emaabsret_30d, k=10
def f11rc_f11_raw_roc_family_emaabsret_30d_slope_v130_signal(closeadj):
    r = closeadj.pct_change(1).abs()
    b = r.ewm(span=10, adjust=False, min_periods=10).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v131 base: signdiff_30d, k=21
def f11rc_f11_raw_roc_family_signdiff_30d_slope_v131_signal(closeadj):
    b = np.sign(closeadj.pct_change(21)).diff(1)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v132 base: signmean_15d, k=5
def f11rc_f11_raw_roc_family_signmean_15d_slope_v132_signal(close):
    s = np.sign(close.pct_change(1))
    b = s.rolling(15, min_periods=15).mean()
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


# v133 base: signagree2_21d, k=10
def f11rc_f11_raw_roc_family_signagree2_21d_slope_v133_signal(close):
    b = np.sign(close.pct_change(5)) + np.sign(close.pct_change(21))
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v134 base: signlongdiff_252d, k=63
def f11rc_f11_raw_roc_family_signlongdiff_252d_slope_v134_signal(closeadj):
    b = np.sign(closeadj.pct_change(63)) - np.sign(closeadj.pct_change(252))
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


# v135 base: bigdncnt_60d, k=10
def f11rc_f11_raw_roc_family_bigdncnt_60d_slope_v135_signal(closeadj):
    r = closeadj.pct_change(1)
    sd = r.rolling(60, min_periods=60).std()
    big = (r < -1.5 * sd).astype(float)
    b = big.rolling(60, min_periods=60).sum()
    b[sd.isna()] = np.nan
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v136 base: wgtroc6_180d, k=63
def f11rc_f11_raw_roc_family_wgtroc6_180d_slope_v136_signal(closeadj):
    p1 = closeadj.pct_change(7); p2 = closeadj.pct_change(14)
    p3 = closeadj.pct_change(21); p4 = closeadj.pct_change(42)
    p5 = closeadj.pct_change(84); p6 = closeadj.pct_change(180)
    b = (p1 + p2 + p3 + p4 + p5 + p6) / 6.0
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


# v137 base: difflogvar_60d, k=10
def f11rc_f11_raw_roc_family_difflogvar_60d_slope_v137_signal(closeadj):
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    v30 = r.rolling(30, min_periods=30).var(ddof=1)
    v60 = r.rolling(60, min_periods=60).var(ddof=1)
    b = v30 - v60
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v138 base: kurtdiff_60d, k=21
def f11rc_f11_raw_roc_family_kurtdiff_60d_slope_v138_signal(closeadj):
    r = closeadj.pct_change(1)
    k30 = r.rolling(30, min_periods=30).kurt()
    k60 = r.rolling(60, min_periods=60).kurt()
    b = k30 - k60
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v139 base: skewdiff_60d, k=10
def f11rc_f11_raw_roc_family_skewdiff_60d_slope_v139_signal(closeadj):
    r = closeadj.pct_change(1)
    s30 = r.rolling(30, min_periods=30).skew()
    s60 = r.rolling(60, min_periods=60).skew()
    b = s30 - s60
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v140 base: normmaxmin_45d, k=21
def f11rc_f11_raw_roc_family_normmaxmin_45d_slope_v140_signal(closeadj):
    r = closeadj.pct_change(1)
    b = r.rolling(45, min_periods=45).max() + r.rolling(45, min_periods=45).min()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v141 base: dnpathlen_45d, k=10
def f11rc_f11_raw_roc_family_dnpathlen_45d_slope_v141_signal(closeadj):
    r = closeadj.pct_change(1)
    dn = r.where(r < 0, 0.0).abs()
    b = dn.rolling(45, min_periods=45).sum()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v142 base: uppathlen_45d, k=21
def f11rc_f11_raw_roc_family_uppathlen_45d_slope_v142_signal(closeadj):
    r = closeadj.pct_change(1)
    up = r.where(r > 0, 0.0)
    b = up.rolling(45, min_periods=45).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v143 base: rallyrecov_60d, k=21
def f11rc_f11_raw_roc_family_rallyrecov_60d_slope_v143_signal(closeadj):
    num = closeadj - closeadj.shift(60)
    rng = closeadj.rolling(60, min_periods=60).max() - closeadj.rolling(60, min_periods=60).min()
    b = num / rng.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v144 base: drawdepth_120d, k=63
def f11rc_f11_raw_roc_family_drawdepth_120d_slope_v144_signal(closeadj):
    hi = closeadj.rolling(120, min_periods=120).max()
    lo = closeadj.rolling(120, min_periods=120).min()
    b = (lo - hi) / hi.replace(0.0, np.nan)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


# v145 base: rocsq_30d, k=10
def f11rc_f11_raw_roc_family_rocsq_30d_slope_v145_signal(closeadj):
    r = closeadj.pct_change(1)
    b = (r ** 2).rolling(30, min_periods=30).sum()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# v146 base: medabsret_30d, k=21
def f11rc_f11_raw_roc_family_medabsret_30d_slope_v146_signal(closeadj):
    r = closeadj.pct_change(1).abs()
    b = r.rolling(30, min_periods=30).median()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v147 base: tailwt_50d, k=21
def f11rc_f11_raw_roc_family_tailwt_50d_slope_v147_signal(closeadj):
    r = closeadj.pct_change(1).abs()
    num = (r ** 3).rolling(50, min_periods=50).sum()
    den = r.rolling(50, min_periods=50).sum()
    b = num / den.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v148 base: corretrng_60d, k=21
def f11rc_f11_raw_roc_family_corretrng_60d_slope_v148_signal(closeadj):
    r = closeadj.pct_change(1)
    b = r.rolling(60, min_periods=60).corr(r.abs())
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# v149 base: logvol_120d, k=63
def f11rc_f11_raw_roc_family_logvol_120d_slope_v149_signal(closeadj):
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    b = r.rolling(120, min_periods=120).std(ddof=1)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


# v150 base: normret_45d, k=10
def f11rc_f11_raw_roc_family_normret_45d_slope_v150_signal(closeadj):
    num = closeadj - closeadj.shift(45)
    rng = closeadj.rolling(45, min_periods=45).max() - closeadj.rolling(45, min_periods=45).min()
    b = num / rng.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f11_raw_roc_family_slope_001_150_REGISTRY = {
    "f11rc_f11_raw_roc_family_roc_1d_slope_v001_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_roc_1d_slope_v001_signal},
    "f11rc_f11_raw_roc_family_roc_5d_slope_v002_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_roc_5d_slope_v002_signal},
    "f11rc_f11_raw_roc_family_roc_21d_slope_v003_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_roc_21d_slope_v003_signal},
    "f11rc_f11_raw_roc_family_roc_252d_slope_v004_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_roc_252d_slope_v004_signal},
    "f11rc_f11_raw_roc_family_logret_3d_slope_v005_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_logret_3d_slope_v005_signal},
    "f11rc_f11_raw_roc_family_logret_63d_slope_v006_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_logret_63d_slope_v006_signal},
    "f11rc_f11_raw_roc_family_logret_126d_slope_v007_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_logret_126d_slope_v007_signal},
    "f11rc_f11_raw_roc_family_volatildiff_63d_slope_v008_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_volatildiff_63d_slope_v008_signal},
    "f11rc_f11_raw_roc_family_rocatrnrm_50d_slope_v009_signal": {"inputs": ["high", "low", "closeadj"], "func": f11rc_f11_raw_roc_family_rocatrnrm_50d_slope_v009_signal},
    "f11rc_f11_raw_roc_family_roczsc_60d_slope_v010_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_roczsc_60d_slope_v010_signal},
    "f11rc_f11_raw_roc_family_rocrank_120d_slope_v011_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocrank_120d_slope_v011_signal},
    "f11rc_f11_raw_roc_family_rocrgrng_50d_slope_v012_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocrgrng_50d_slope_v012_signal},
    "f11rc_f11_raw_roc_family_rocdf521_21d_slope_v013_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_rocdf521_21d_slope_v013_signal},
    "f11rc_f11_raw_roc_family_rocdf2163_63d_slope_v014_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocdf2163_63d_slope_v014_signal},
    "f11rc_f11_raw_roc_family_rocdf63252_252d_slope_v015_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocdf63252_252d_slope_v015_signal},
    "f11rc_f11_raw_roc_family_rocrat521_21d_slope_v016_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_rocrat521_21d_slope_v016_signal},
    "f11rc_f11_raw_roc_family_rocavgmom_63d_slope_v017_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocavgmom_63d_slope_v017_signal},
    "f11rc_f11_raw_roc_family_signroc_5d_slope_v018_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_signroc_5d_slope_v018_signal},
    "f11rc_f11_raw_roc_family_signroc_21d_slope_v019_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_signroc_21d_slope_v019_signal},
    "f11rc_f11_raw_roc_family_signroc_63d_slope_v020_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signroc_63d_slope_v020_signal},
    "f11rc_f11_raw_roc_family_uprtcnt_21d_slope_v021_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_uprtcnt_21d_slope_v021_signal},
    "f11rc_f11_raw_roc_family_dnrtcnt_63d_slope_v022_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_dnrtcnt_63d_slope_v022_signal},
    "f11rc_f11_raw_roc_family_uprstk_30d_slope_v023_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_uprstk_30d_slope_v023_signal},
    "f11rc_f11_raw_roc_family_dnstk_30d_slope_v024_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_dnstk_30d_slope_v024_signal},
    "f11rc_f11_raw_roc_family_dssince2pct_60d_slope_v025_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_dssince2pct_60d_slope_v025_signal},
    "f11rc_f11_raw_roc_family_retskew_30d_slope_v026_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_retskew_30d_slope_v026_signal},
    "f11rc_f11_raw_roc_family_retkurt_60d_slope_v027_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_retkurt_60d_slope_v027_signal},
    "f11rc_f11_raw_roc_family_madstd_40d_slope_v028_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_madstd_40d_slope_v028_signal},
    "f11rc_f11_raw_roc_family_winrate_50d_slope_v029_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_winrate_50d_slope_v029_signal},
    "f11rc_f11_raw_roc_family_sortino_30d_slope_v030_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_sortino_30d_slope_v030_signal},
    "f11rc_f11_raw_roc_family_thirdmom_45d_slope_v031_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_thirdmom_45d_slope_v031_signal},
    "f11rc_f11_raw_roc_family_fourthmom_45d_slope_v032_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_fourthmom_45d_slope_v032_signal},
    "f11rc_f11_raw_roc_family_absretq75_60d_slope_v033_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_absretq75_60d_slope_v033_signal},
    "f11rc_f11_raw_roc_family_retac1_40d_slope_v034_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_retac1_40d_slope_v034_signal},
    "f11rc_f11_raw_roc_family_retac5_60d_slope_v035_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_retac5_60d_slope_v035_signal},
    "f11rc_f11_raw_roc_family_volclust_30d_slope_v036_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_volclust_30d_slope_v036_signal},
    "f11rc_f11_raw_roc_family_hurstret_80d_slope_v037_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_hurstret_80d_slope_v037_signal},
    "f11rc_f11_raw_roc_family_varratio_q10_60d_slope_v038_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_varratio_q10_60d_slope_v038_signal},
    "f11rc_f11_raw_roc_family_pathlen_21d_slope_v039_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_pathlen_21d_slope_v039_signal},
    "f11rc_f11_raw_roc_family_efficiency_30d_slope_v040_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_efficiency_30d_slope_v040_signal},
    "f11rc_f11_raw_roc_family_inveff_60d_slope_v041_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_inveff_60d_slope_v041_signal},
    "f11rc_f11_raw_roc_family_maxdd_60d_slope_v042_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_maxdd_60d_slope_v042_signal},
    "f11rc_f11_raw_roc_family_recovery_45d_slope_v043_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_recovery_45d_slope_v043_signal},
    "f11rc_f11_raw_roc_family_avgupmag_45d_slope_v044_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_avgupmag_45d_slope_v044_signal},
    "f11rc_f11_raw_roc_family_maxret_21d_slope_v045_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_maxret_21d_slope_v045_signal},
    "f11rc_f11_raw_roc_family_minret_45d_slope_v046_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_minret_45d_slope_v046_signal},
    "f11rc_f11_raw_roc_family_avgtop5_60d_slope_v047_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_avgtop5_60d_slope_v047_signal},
    "f11rc_f11_raw_roc_family_avgbot5_60d_slope_v048_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_avgbot5_60d_slope_v048_signal},
    "f11rc_f11_raw_roc_family_upsemivar_40d_slope_v049_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_upsemivar_40d_slope_v049_signal},
    "f11rc_f11_raw_roc_family_dnsemivar_40d_slope_v050_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_dnsemivar_40d_slope_v050_signal},
    "f11rc_f11_raw_roc_family_tstat_45d_slope_v051_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_tstat_45d_slope_v051_signal},
    "f11rc_f11_raw_roc_family_tstat_120d_slope_v052_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_tstat_120d_slope_v052_signal},
    "f11rc_f11_raw_roc_family_vrm2_30d_slope_v053_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_vrm2_30d_slope_v053_signal},
    "f11rc_f11_raw_roc_family_arctandiff_84d_slope_v054_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_arctandiff_84d_slope_v054_signal},
    "f11rc_f11_raw_roc_family_tanhzsc_40d_slope_v055_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_tanhzsc_40d_slope_v055_signal},
    "f11rc_f11_raw_roc_family_sigeffic_30d_slope_v056_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_sigeffic_30d_slope_v056_signal},
    "f11rc_f11_raw_roc_family_tanhskew_60d_slope_v057_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_tanhskew_60d_slope_v057_signal},
    "f11rc_f11_raw_roc_family_pctrnkabs_252d_slope_v058_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_pctrnkabs_252d_slope_v058_signal},
    "f11rc_f11_raw_roc_family_emaroc_10d_slope_v059_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_emaroc_10d_slope_v059_signal},
    "f11rc_f11_raw_roc_family_wmadrocbias_21d_slope_v060_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_wmadrocbias_21d_slope_v060_signal},
    "f11rc_f11_raw_roc_family_medroc_15d_slope_v061_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_medroc_15d_slope_v061_signal},
    "f11rc_f11_raw_roc_family_trmroc_42d_slope_v062_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_trmroc_42d_slope_v062_signal},
    "f11rc_f11_raw_roc_family_trendscore_63d_slope_v063_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_trendscore_63d_slope_v063_signal},
    "f11rc_f11_raw_roc_family_signagree5_63d_slope_v064_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signagree5_63d_slope_v064_signal},
    "f11rc_f11_raw_roc_family_wavgroc_252d_slope_v065_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_wavgroc_252d_slope_v065_signal},
    "f11rc_f11_raw_roc_family_upqtcnt_30d_slope_v066_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_upqtcnt_30d_slope_v066_signal},
    "f11rc_f11_raw_roc_family_quadrnt_30d_slope_v067_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_quadrnt_30d_slope_v067_signal},
    "f11rc_f11_raw_roc_family_highrocstk_42d_slope_v068_signal": {"inputs": ["high"], "func": f11rc_f11_raw_roc_family_highrocstk_42d_slope_v068_signal},
    "f11rc_f11_raw_roc_family_lowstkdwn_42d_slope_v069_signal": {"inputs": ["low"], "func": f11rc_f11_raw_roc_family_lowstkdwn_42d_slope_v069_signal},
    "f11rc_f11_raw_roc_family_hlrocdiff_21d_slope_v070_signal": {"inputs": ["high", "low"], "func": f11rc_f11_raw_roc_family_hlrocdiff_21d_slope_v070_signal},
    "f11rc_f11_raw_roc_family_openclrocdf_5d_slope_v071_signal": {"inputs": ["open", "close"], "func": f11rc_f11_raw_roc_family_openclrocdf_5d_slope_v071_signal},
    "f11rc_f11_raw_roc_family_rocclz_50d_slope_v073_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocclz_50d_slope_v073_signal},
    "f11rc_f11_raw_roc_family_logvar_30d_slope_v074_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_logvar_30d_slope_v074_signal},
    "f11rc_f11_raw_roc_family_jumpfrac_60d_slope_v075_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_jumpfrac_60d_slope_v075_signal},
    "f11rc_f11_raw_roc_family_roc_2d_slope_v076_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_roc_2d_slope_v076_signal},
    "f11rc_f11_raw_roc_family_roc_10d_slope_v077_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_roc_10d_slope_v077_signal},
    "f11rc_f11_raw_roc_family_logret_42d_slope_v078_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_logret_42d_slope_v078_signal},
    "f11rc_f11_raw_roc_family_logretkurt_45d_slope_v079_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_logretkurt_45d_slope_v079_signal},
    "f11rc_f11_raw_roc_family_rocsemi_40d_slope_v080_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocsemi_40d_slope_v080_signal},
    "f11rc_f11_raw_roc_family_updnstdratio_60d_slope_v081_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_updnstdratio_60d_slope_v081_signal},
    "f11rc_f11_raw_roc_family_signsqret_30d_slope_v082_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signsqret_30d_slope_v082_signal},
    "f11rc_f11_raw_roc_family_rocsignal_30d_slope_v083_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocsignal_30d_slope_v083_signal},
    "f11rc_f11_raw_roc_family_rocdf_15d_slope_v084_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_rocdf_15d_slope_v084_signal},
    "f11rc_f11_raw_roc_family_rocdf_42d_slope_v085_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocdf_42d_slope_v085_signal},
    "f11rc_f11_raw_roc_family_rocdf_126d_slope_v086_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocdf_126d_slope_v086_signal},
    "f11rc_f11_raw_roc_family_rocdfsign_63d_slope_v087_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocdfsign_63d_slope_v087_signal},
    "f11rc_f11_raw_roc_family_rocdrop_63d_slope_v088_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocdrop_63d_slope_v088_signal},
    "f11rc_f11_raw_roc_family_uprtcnt_10d_slope_v089_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_uprtcnt_10d_slope_v089_signal},
    "f11rc_f11_raw_roc_family_dnrtcnt_21d_slope_v090_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_dnrtcnt_21d_slope_v090_signal},
    "f11rc_f11_raw_roc_family_alterncnt_45d_slope_v091_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_alterncnt_45d_slope_v091_signal},
    "f11rc_f11_raw_roc_family_dssince5pct_120d_slope_v092_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_dssince5pct_120d_slope_v092_signal},
    "f11rc_f11_raw_roc_family_signstreak_30d_slope_v093_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_signstreak_30d_slope_v093_signal},
    "f11rc_f11_raw_roc_family_bigupcnt_60d_slope_v094_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_bigupcnt_60d_slope_v094_signal},
    "f11rc_f11_raw_roc_family_retskew_90d_slope_v095_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_retskew_90d_slope_v095_signal},
    "f11rc_f11_raw_roc_family_retkurt_30d_slope_v096_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_retkurt_30d_slope_v096_signal},
    "f11rc_f11_raw_roc_family_logretskew_50d_slope_v097_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_logretskew_50d_slope_v097_signal},
    "f11rc_f11_raw_roc_family_winratio_90d_slope_v098_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_winratio_90d_slope_v098_signal},
    "f11rc_f11_raw_roc_family_avgdnmag_45d_slope_v099_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_avgdnmag_45d_slope_v099_signal},
    "f11rc_f11_raw_roc_family_retac3_50d_slope_v100_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_retac3_50d_slope_v100_signal},
    "f11rc_f11_raw_roc_family_signac1_60d_slope_v101_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signac1_60d_slope_v101_signal},
    "f11rc_f11_raw_roc_family_sqrac1_45d_slope_v102_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_sqrac1_45d_slope_v102_signal},
    "f11rc_f11_raw_roc_family_pathlen_60d_slope_v103_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_pathlen_60d_slope_v103_signal},
    "f11rc_f11_raw_roc_family_pathvsstd_30d_slope_v105_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_pathvsstd_30d_slope_v105_signal},
    "f11rc_f11_raw_roc_family_maxdd_120d_slope_v106_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_maxdd_120d_slope_v106_signal},
    "f11rc_f11_raw_roc_family_drwdwn_30d_slope_v107_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_drwdwn_30d_slope_v107_signal},
    "f11rc_f11_raw_roc_family_topbotrng_45d_slope_v108_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_topbotrng_45d_slope_v108_signal},
    "f11rc_f11_raw_roc_family_avgtop3_30d_slope_v109_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_avgtop3_30d_slope_v109_signal},
    "f11rc_f11_raw_roc_family_avgbot3_30d_slope_v110_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_avgbot3_30d_slope_v110_signal},
    "f11rc_f11_raw_roc_family_iqrret_60d_slope_v111_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_iqrret_60d_slope_v111_signal},
    "f11rc_f11_raw_roc_family_tanharctan_30d_slope_v112_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_tanharctan_30d_slope_v112_signal},
    "f11rc_f11_raw_roc_family_arctan_long_slope_v113_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_arctan_long_slope_v113_signal},
    "f11rc_f11_raw_roc_family_rkdf_60d_slope_v114_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rkdf_60d_slope_v114_signal},
    "f11rc_f11_raw_roc_family_pctrnk21_60d_slope_v115_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_pctrnk21_60d_slope_v115_signal},
    "f11rc_f11_raw_roc_family_sigsharpe_90d_slope_v116_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_sigsharpe_90d_slope_v116_signal},
    "f11rc_f11_raw_roc_family_signalign3_42d_slope_v117_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signalign3_42d_slope_v117_signal},
    "f11rc_f11_raw_roc_family_signsum5_84d_slope_v118_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signsum5_84d_slope_v118_signal},
    "f11rc_f11_raw_roc_family_minabs5_30d_slope_v119_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_minabs5_30d_slope_v119_signal},
    "f11rc_f11_raw_roc_family_centmin_pct_60d_slope_v120_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_centmin_pct_60d_slope_v120_signal},
    "f11rc_f11_raw_roc_family_vrq5_60d_slope_v121_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_vrq5_60d_slope_v121_signal},
    "f11rc_f11_raw_roc_family_vrq20_120d_slope_v122_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_vrq20_120d_slope_v122_signal},
    "f11rc_f11_raw_roc_family_tstat_21d_slope_v123_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_tstat_21d_slope_v123_signal},
    "f11rc_f11_raw_roc_family_clcldiff_5d_slope_v124_signal": {"inputs": ["open", "close"], "func": f11rc_f11_raw_roc_family_clcldiff_5d_slope_v124_signal},
    "f11rc_f11_raw_roc_family_loretdiff_21d_slope_v125_signal": {"inputs": ["low", "close"], "func": f11rc_f11_raw_roc_family_loretdiff_21d_slope_v125_signal},
    "f11rc_f11_raw_roc_family_hiretdiff_21d_slope_v126_signal": {"inputs": ["high", "close"], "func": f11rc_f11_raw_roc_family_hiretdiff_21d_slope_v126_signal},
    "f11rc_f11_raw_roc_family_openrocstk_42d_slope_v127_signal": {"inputs": ["open"], "func": f11rc_f11_raw_roc_family_openrocstk_42d_slope_v127_signal},
    "f11rc_f11_raw_roc_family_emaabsdf_42d_slope_v128_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_emaabsdf_42d_slope_v128_signal},
    "f11rc_f11_raw_roc_family_medroc_63d_slope_v129_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_medroc_63d_slope_v129_signal},
    "f11rc_f11_raw_roc_family_emaabsret_30d_slope_v130_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_emaabsret_30d_slope_v130_signal},
    "f11rc_f11_raw_roc_family_signdiff_30d_slope_v131_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signdiff_30d_slope_v131_signal},
    "f11rc_f11_raw_roc_family_signmean_15d_slope_v132_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_signmean_15d_slope_v132_signal},
    "f11rc_f11_raw_roc_family_signagree2_21d_slope_v133_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_signagree2_21d_slope_v133_signal},
    "f11rc_f11_raw_roc_family_signlongdiff_252d_slope_v134_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signlongdiff_252d_slope_v134_signal},
    "f11rc_f11_raw_roc_family_bigdncnt_60d_slope_v135_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_bigdncnt_60d_slope_v135_signal},
    "f11rc_f11_raw_roc_family_wgtroc6_180d_slope_v136_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_wgtroc6_180d_slope_v136_signal},
    "f11rc_f11_raw_roc_family_difflogvar_60d_slope_v137_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_difflogvar_60d_slope_v137_signal},
    "f11rc_f11_raw_roc_family_kurtdiff_60d_slope_v138_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_kurtdiff_60d_slope_v138_signal},
    "f11rc_f11_raw_roc_family_skewdiff_60d_slope_v139_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_skewdiff_60d_slope_v139_signal},
    "f11rc_f11_raw_roc_family_normmaxmin_45d_slope_v140_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_normmaxmin_45d_slope_v140_signal},
    "f11rc_f11_raw_roc_family_dnpathlen_45d_slope_v141_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_dnpathlen_45d_slope_v141_signal},
    "f11rc_f11_raw_roc_family_uppathlen_45d_slope_v142_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_uppathlen_45d_slope_v142_signal},
    "f11rc_f11_raw_roc_family_rallyrecov_60d_slope_v143_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rallyrecov_60d_slope_v143_signal},
    "f11rc_f11_raw_roc_family_drawdepth_120d_slope_v144_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_drawdepth_120d_slope_v144_signal},
    "f11rc_f11_raw_roc_family_rocsq_30d_slope_v145_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocsq_30d_slope_v145_signal},
    "f11rc_f11_raw_roc_family_medabsret_30d_slope_v146_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_medabsret_30d_slope_v146_signal},
    "f11rc_f11_raw_roc_family_tailwt_50d_slope_v147_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_tailwt_50d_slope_v147_signal},
    "f11rc_f11_raw_roc_family_corretrng_60d_slope_v148_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_corretrng_60d_slope_v148_signal},
    "f11rc_f11_raw_roc_family_logvol_120d_slope_v149_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_logvol_120d_slope_v149_signal},
    "f11rc_f11_raw_roc_family_normret_45d_slope_v150_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_normret_45d_slope_v150_signal},
}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f11_raw_roc_family_slope_001_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        s = corr.unstack().sort_values(ascending=False)
        s = s[s > 0.94].head(40)
        seen = set()
        for (a, b), v in s.items():
            if a < b and (a, b) not in seen:
                seen.add((a, b))
                print(f"  {a}  vs  {b}  ->  {v:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK slope_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
