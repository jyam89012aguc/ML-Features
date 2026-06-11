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


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (dilution intensity) =====
def _f19_growth(shares, w):
    return np.log(shares.replace(0, np.nan) / shares.shift(w).replace(0, np.nan))


def _f19_dil_rate(shares, w):
    return shares / shares.shift(w).replace(0, np.nan) - 1.0


def _f19_creep(shareswadil, shareswa):
    return shareswadil / shareswa.replace(0, np.nan) - 1.0


def _f19_issuance(ncfcommon):
    return -ncfcommon


def _f19_streak(cond):
    grp = (~cond).cumsum()
    return cond.groupby(grp).cumsum()



def f19di_f19_dilution_intensity_basgrow_21d_jerk_v001_signal(sharesbas):
    base = _f19_dil_rate(sharesbas, 21)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basgrow_42d_jerk_v002_signal(sharesbas):
    base = _f19_growth(sharesbas, 42)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basgrow_63d_jerk_v003_signal(sharesbas):
    base = _f19_growth(sharesbas, 63)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basgrow_126d_jerk_v004_signal(sharesbas):
    base = _f19_growth(sharesbas, 126)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basgrow_189d_jerk_v005_signal(sharesbas):
    base = _f19_growth(sharesbas, 189)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basgrow_252d_jerk_v006_signal(sharesbas):
    base = _f19_growth(sharesbas, 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basgrow_378d_jerk_v007_signal(sharesbas):
    base = _f19_growth(sharesbas, 378)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basgrow_504d_jerk_v008_signal(sharesbas):
    base = _f19_growth(sharesbas, 504)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_wagrow_63d_jerk_v009_signal(shareswa):
    base = _f19_growth(shareswa, 63)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_wagrow_126d_jerk_v010_signal(shareswa):
    base = _f19_growth(shareswa, 126)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_wagrow_252d_jerk_v011_signal(shareswa):
    base = _f19_growth(shareswa, 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_wagrow_504d_jerk_v012_signal(shareswa):
    base = _f19_growth(shareswa, 504)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilgrow_63d_jerk_v013_signal(shareswadil):
    base = _f19_growth(shareswadil, 63)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilgrow_126d_jerk_v014_signal(shareswadil):
    base = _f19_growth(shareswadil, 126)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilgrow_252d_jerk_v015_signal(shareswadil):
    base = _f19_growth(shareswadil, 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilgrow_504d_jerk_v016_signal(shareswadil):
    base = _f19_growth(shareswadil, 504)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basrate_5d_jerk_v017_signal(sharesbas):
    base = _f19_dil_rate(sharesbas, 5)
    slope = base.diff(5)
    jerk = slope.diff(5)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basacc_42d_jerk_v018_signal(sharesbas):
    g = _f19_growth(sharesbas, 42)
    base = g - g.shift(42)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilrate_21d_jerk_v019_signal(shareswadil):
    base = _f19_dil_rate(shareswadil, 21)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_warate_42d_jerk_v020_signal(shareswa):
    base = _f19_dil_rate(shareswa, 42)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basgrowz_63d_jerk_v021_signal(sharesbas):
    base = _z(_f19_growth(sharesbas, 63), 252)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basgrowz_126d_jerk_v022_signal(sharesbas):
    base = _z(_f19_growth(sharesbas, 126), 252)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basgrowz_252d_jerk_v023_signal(sharesbas):
    base = _z(_f19_growth(sharesbas, 252), 504)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilgrowz_126d_jerk_v024_signal(shareswadil):
    base = _z(_f19_growth(shareswadil, 126), 252)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilgrowz_252d_jerk_v025_signal(shareswadil):
    base = _z(_f19_growth(shareswadil, 252), 504)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_wagrowz_126d_jerk_v026_signal(shareswa):
    base = _z(_f19_growth(shareswa, 126), 252)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilrank_252d_jerk_v027_signal(sharesbas):
    base = _rank(_f19_growth(sharesbas, 252), 504)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilrank_126d_jerk_v028_signal(sharesbas):
    base = _rank(_f19_growth(sharesbas, 126), 504)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilrank_63d_jerk_v029_signal(shareswadil):
    base = _rank(_f19_growth(shareswadil, 63), 504)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_warank_63d_jerk_v030_signal(shareswa):
    base = _rank(_f19_dil_rate(shareswa, 63), 504)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilcyclerank_126d_jerk_v031_signal(sharesbas):
    base = _rank(sharesbas.pct_change(126), 1260)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creep_lvl_jerk_v032_signal(shareswadil, shareswa):
    base = _f19_creep(shareswadil, shareswa)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creepz252_z_jerk_v033_signal(shareswadil, shareswa):
    base = _z(_f19_creep(shareswadil, shareswa), 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creepz504_z_jerk_v034_signal(shareswadil, shareswa):
    base = _z(_f19_creep(shareswadil, shareswa), 504)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creeprank_504d_jerk_v035_signal(shareswadil, shareswa):
    base = _rank(_f19_creep(shareswadil, shareswa), 504)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creeprank_1260d_jerk_v036_signal(shareswadil, shareswa):
    base = _rank(_f19_creep(shareswadil, shareswa), 1260)
    slope = base.diff(126)
    jerk = slope.diff(126)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creepma63_d_jerk_v037_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    base = c - _mean(c, 63)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creepma252_d_jerk_v038_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    base = c - _mean(c, 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creepdisp_252d_jerk_v039_signal(shareswadil, shareswa):
    base = _std(_f19_creep(shareswadil, shareswa), 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creepdisp_126d_jerk_v040_signal(shareswadil, shareswa):
    base = _std(_f19_creep(shareswadil, shareswa), 126)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_isscum_126d_jerk_v041_signal(ncfcommon):
    base = _rsum(_f19_issuance(ncfcommon), 126)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_isscum_252d_jerk_v042_signal(ncfcommon):
    base = _rsum(_f19_issuance(ncfcommon), 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_isscum_63d_jerk_v043_signal(ncfcommon):
    base = _rsum(_f19_issuance(ncfcommon), 63)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issz_252d_jerk_v044_signal(ncfcommon):
    base = _z(_f19_issuance(ncfcommon), 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issz_504d_jerk_v045_signal(ncfcommon):
    base = _z(_f19_issuance(ncfcommon), 504)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issnorm_d_jerk_v046_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    base = iss / iss.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issperhsh_lvl_jerk_v047_signal(ncfcommon, sharesbas):
    base = _f19_issuance(ncfcommon) / sharesbas.replace(0, np.nan)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issperhshq_63d_jerk_v048_signal(ncfcommon, sharesbas):
    ips = _rsum(_f19_issuance(ncfcommon), 63) / sharesbas.replace(0, np.nan)
    base = _z(ips, 252)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issintens_252d_jerk_v049_signal(ncfcommon, sharesbas):
    ips = _rsum(_f19_issuance(ncfcommon), 252) / sharesbas.replace(0, np.nan)
    base = ips - ips.shift(252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_isspersh_504d_jerk_v050_signal(ncfcommon, sharesbas):
    base = _rsum(_f19_issuance(ncfcommon), 504) / sharesbas.replace(0, np.nan)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issbal_252d_jerk_v051_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    pos = _rsum(iss.clip(lower=0), 252)
    neg = _rsum((-iss).clip(lower=0), 252)
    base = pos / (neg + pos.abs().rolling(252, min_periods=63).mean() * 0.01).replace(0, np.nan)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issdir_252d_jerk_v052_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    base = _rsum(iss, 252) / _rsum(iss.abs(), 252).replace(0, np.nan)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issdir_126d_jerk_v053_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    base = _rsum(iss, 126) / _rsum(iss.abs(), 126).replace(0, np.nan)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_isshhi_252d_jerk_v054_signal(ncfcommon):
    pos = _f19_issuance(ncfcommon).clip(lower=0)
    tot = _rsum(pos, 252)
    share = pos / tot.replace(0, np.nan)
    base = (share ** 2).rolling(252, min_periods=126).sum()
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issvolreg_d_jerk_v055_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    base = _std(iss, 63) / _std(iss, 252).replace(0, np.nan) - 1.0
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issskew_252d_jerk_v056_signal(ncfcommon):
    base = _f19_issuance(ncfcommon).rolling(252, min_periods=126).skew()
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issregime_504d_jerk_v057_signal(ncfcommon):
    cum = _rsum(_f19_issuance(ncfcommon), 252)
    med = cum.rolling(504, min_periods=252).median()
    scale = cum.abs().rolling(504, min_periods=126).mean()
    base = (cum - med) / scale.replace(0, np.nan)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_growspr_252d_jerk_v058_signal(shareswadil, shareswa):
    base = _f19_growth(shareswadil, 252) - _f19_growth(shareswa, 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_growspr_126d_jerk_v059_signal(shareswadil, shareswa):
    base = _f19_growth(shareswadil, 126) - _f19_growth(shareswa, 126)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_baswagap_lvl_jerk_v060_signal(sharesbas, shareswa):
    base = sharesbas / shareswa.replace(0, np.nan) - 1.0
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_baswagapz_d_jerk_v061_signal(sharesbas, shareswa):
    base = _z(sharesbas / shareswa.replace(0, np.nan) - 1.0, 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_absorb_126d_jerk_v062_signal(sharesbas, shareswadil):
    base = _f19_growth(sharesbas, 126) - _f19_growth(shareswadil, 126)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_zdiverge_63d_jerk_v063_signal(sharesbas, shareswadil):
    base = _z(sharesbas.pct_change(63), 252) - _z(shareswadil.pct_change(63), 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_amplif_63d_jerk_v064_signal(sharesbas, shareswa):
    rb = sharesbas.pct_change(63)
    rw = shareswa.pct_change(63)
    base = (rb - rw) / (rb.abs() + rw.abs() + 1e-9)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_overhangratio_lvl_jerk_v065_signal(shareswadil, sharesbas):
    base = _rank(shareswadil / sharesbas.replace(0, np.nan), 504)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dildisp252_d_jerk_v066_signal(sharesbas):
    base = _std(sharesbas.pct_change(21), 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dildisp63_d_jerk_v067_signal(sharesbas):
    base = _std(sharesbas.pct_change(5), 63)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_wadisp504_d_jerk_v068_signal(shareswa):
    base = _std(shareswa.pct_change(63), 504)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dildildisp_252d_jerk_v069_signal(shareswadil):
    base = _std(shareswadil.pct_change(21), 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilsemidev_252d_jerk_v070_signal(sharesbas):
    base = _std(sharesbas.pct_change(21).clip(lower=0), 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilskew_252d_jerk_v071_signal(sharesbas):
    base = sharesbas.pct_change(21).rolling(252, min_periods=126).skew()
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilkurt_252d_jerk_v072_signal(sharesbas):
    base = sharesbas.pct_change(21).rolling(252, min_periods=126).kurt()
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilcyclepos_504d_jerk_v073_signal(sharesbas):
    r = sharesbas.pct_change(63)
    hi = _rmax(r, 504)
    lo = _rmin(r, 504)
    base = (r - lo) / (hi - lo).replace(0, np.nan) - 0.5
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilregimedist_d_jerk_v074_signal(shareswadil):
    r = shareswadil.pct_change(63)
    med = r.rolling(504, min_periods=252).median()
    iqr = (r.rolling(504, min_periods=252).quantile(0.75) - r.rolling(504, min_periods=252).quantile(0.25))
    base = (r - med) / iqr.replace(0, np.nan)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_paceslow_d_jerk_v075_signal(sharesbas):
    pace = sharesbas.pct_change(63)
    peak = _rmax(pace, 252)
    base = pace - peak
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_pacevspeak_d_jerk_v076_signal(sharesbas):
    q = sharesbas.pct_change(63)
    peak = _rmax(q, 252)
    base = q / peak.replace(0, np.nan)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilema_d_jerk_v077_signal(sharesbas):
    rate = sharesbas.pct_change(21)
    base = rate.ewm(span=21, min_periods=10).mean() - rate.ewm(span=126, min_periods=42).mean()
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilmom_252d_jerk_v078_signal(sharesbas):
    g = _f19_growth(sharesbas, 252)
    base = g - g.shift(63)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilmom_126d_jerk_v079_signal(sharesbas):
    g = _f19_growth(sharesbas, 126)
    base = g - g.shift(63)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creepmom_63d_jerk_v080_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    base = c - c.shift(63)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creepvel_21d_jerk_v081_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    base = c - c.shift(21)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_isstilt_126d_jerk_v082_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    scale = iss.abs().rolling(252, min_periods=126).mean()
    norm = iss / scale.replace(0, np.nan)
    base = norm.ewm(span=63, min_periods=21).mean()
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issmom_126d_jerk_v083_signal(ncfcommon):
    q = _rsum(_f19_issuance(ncfcommon), 63)
    raw = q - q.shift(126)
    base = raw / q.abs().rolling(252, min_periods=63).mean().replace(0, np.nan)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_isspershema_d_jerk_v084_signal(ncfcommon, sharesbas):
    ips = _f19_issuance(ncfcommon) / sharesbas.replace(0, np.nan)
    base = ips.ewm(span=21, min_periods=10).mean() - ips.ewm(span=126, min_periods=42).mean()
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilstreak_252d_jerk_v085_signal(sharesbas):
    up = (sharesbas > sharesbas.shift(21)).astype(float)
    base = up.rolling(252, min_periods=126).mean()
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_monotone_252d_jerk_v086_signal(sharesbas):
    up = (sharesbas > sharesbas.shift(1)).astype(float)
    base = up.rolling(252, min_periods=126).mean()
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilstreakfrac_252d_jerk_v087_signal(shareswadil):
    up = (shareswadil > shareswadil.shift(21)).astype(float)
    base = up.rolling(252, min_periods=126).mean()
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_raisefrac_252d_jerk_v088_signal(ncfcommon):
    raised = (_rsum(_f19_issuance(ncfcommon), 63) > 0).astype(float)
    base = raised.rolling(252, min_periods=126).mean()
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilevents_252d_jerk_v089_signal(sharesbas):
    big = (sharesbas / sharesbas.shift(21).replace(0, np.nan) - 1.0 > 0.01).astype(float)
    base = big.rolling(252, min_periods=126).mean()
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilentropy_252d_jerk_v090_signal(sharesbas):
    up = (sharesbas.pct_change(21) > 0).astype(float)
    p = up.rolling(252, min_periods=126).mean().clip(1e-6, 1 - 1e-6)
    base = -(p * np.log(p) + (1 - p) * np.log(1 - p))
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issdilinter_252d_jerk_v091_signal(ncfcommon, sharesbas):
    iss = _z(_rsum(_f19_issuance(ncfcommon), 252), 504)
    dil = _z(_f19_growth(sharesbas, 252), 504)
    base = iss * dil
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issoverhang_d_jerk_v092_signal(ncfcommon, shareswadil, shareswa):
    issz = _z(_rsum(_f19_issuance(ncfcommon), 63), 252)
    cz = _z(_f19_creep(shareswadil, shareswa), 252)
    base = issz * cz
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_whipsaw_63d_jerk_v093_signal(sharesbas):
    noise = _std(sharesbas.pct_change(5), 63)
    trend = _f19_growth(sharesbas, 63).abs()
    base = noise / (trend + 1e-9)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilbeta_d_jerk_v094_signal(sharesbas, shareswa):
    db = sharesbas.pct_change(21)
    dw = shareswa.pct_change(21)
    cov = (db * dw).rolling(252, min_periods=126).mean() - (_mean(db, 252) * _mean(dw, 252))
    base = cov / (_std(dw, 252) ** 2).replace(0, np.nan)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basema252_d_jerk_v095_signal(sharesbas):
    ema = sharesbas.ewm(span=252, min_periods=84).mean()
    base = sharesbas / ema.replace(0, np.nan) - 1.0
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basema63_d_jerk_v096_signal(sharesbas):
    ema = sharesbas.ewm(span=63, min_periods=21).mean()
    base = sharesbas / ema.replace(0, np.nan) - 1.0
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilpacesurp_d_jerk_v097_signal(sharesbas):
    pace = _f19_growth(sharesbas, 126) * 2.0
    expect = pace.rolling(504, min_periods=252).median()
    sd = pace.rolling(504, min_periods=252).std()
    base = (pace - expect) / sd.replace(0, np.nan)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilsurprise_252d_jerk_v098_signal(sharesbas):
    g = _f19_growth(sharesbas, 252)
    base = g - g.ewm(span=126, min_periods=42).mean()
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilsignmag_252d_jerk_v099_signal(sharesbas):
    g = _f19_growth(sharesbas, 252)
    base = np.sign(g) * (g.abs() ** 0.5)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_diltanh_63d_jerk_v100_signal(sharesbas):
    g = _f19_growth(sharesbas, 63)
    base = np.tanh(50.0 * (g - g.shift(21)))
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_bddivtanh_d_jerk_v101_signal(sharesbas, shareswadil):
    db = sharesbas.pct_change(21)
    dd = shareswadil.pct_change(21)
    base = np.tanh(60.0 * (dd - db))
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilsharpe_252d_jerk_v102_signal(shareswadil):
    g = shareswadil.pct_change(63)
    base = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilriskadj_126d_jerk_v103_signal(sharesbas):
    base = _f19_growth(sharesbas, 126) / _std(sharesbas.pct_change(21), 252).replace(0, np.nan)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_cumdil_1260d_jerk_v104_signal(sharesbas):
    mn = _mean(sharesbas, 1260)
    base = np.log(sharesbas.replace(0, np.nan) / mn.replace(0, np.nan))
    slope = base.diff(126)
    jerk = slope.diff(126)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilvsmin504_d_jerk_v105_signal(shareswadil):
    mn = _rmin(shareswadil, 504)
    base = shareswadil / mn.replace(0, np.nan) - 1.0
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilvsmin252_d_jerk_v106_signal(sharesbas):
    mn = _rmin(sharesbas, 252)
    base = sharesbas / mn.replace(0, np.nan) - 1.0
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilpersist_d_jerk_v107_signal(sharesbas):
    r = sharesbas.pct_change(21)
    prod = r * r.shift(21)
    base = prod.rolling(252, min_periods=126).mean() / (_std(r, 252).replace(0, np.nan) ** 2)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dispspread_d_jerk_v108_signal(sharesbas, shareswadil):
    db = _std(sharesbas.pct_change(21), 252)
    dd = _std(shareswadil.pct_change(21), 252)
    base = dd - db
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_wamom_252d_jerk_v109_signal(shareswa):
    g = _f19_growth(shareswa, 252)
    base = g - g.shift(21)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issslope_126d_jerk_v110_signal(ncfcommon):
    cum = _f19_issuance(ncfcommon).cumsum()
    base = (cum - cum.shift(63)) / cum.abs().rolling(252, min_periods=63).mean().replace(0, np.nan)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_stepjump_63d_jerk_v111_signal(sharesbas):
    base = _rmax(sharesbas.pct_change(1), 63)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_maxdiljump_252d_jerk_v112_signal(sharesbas):
    jump = sharesbas / sharesbas.shift(21).replace(0, np.nan) - 1.0
    base = _rmax(jump, 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_diltail_252d_jerk_v113_signal(sharesbas):
    base = sharesbas.pct_change(21).rolling(252, min_periods=126).quantile(0.95)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creepconvex_d_jerk_v114_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    base = c - 2.0 * c.shift(63) + c.shift(126)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creephigh_d_jerk_v115_signal(shareswadil, shareswa):
    dc = _f19_creep(shareswadil, shareswa).diff(21)
    base = _std(dc, 63) / _std(dc, 504).replace(0, np.nan) - 1.0
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilterm_d_jerk_v116_signal(sharesbas):
    fast = _f19_growth(sharesbas, 63) * 4.0
    slow = _f19_growth(sharesbas, 504) * 0.5
    base = (fast - slow) / (fast.abs() + slow.abs() + 1e-9)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilpaceratio_d_jerk_v117_signal(sharesbas):
    short = _f19_growth(sharesbas, 126) * 4.0
    long = _f19_growth(sharesbas, 504)
    base = (short - long) / (short.abs() + long.abs() + 1e-9)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_wadisp_ema_d_jerk_v118_signal(shareswa):
    rate = shareswa.pct_change(21)
    base = rate - rate.ewm(span=126, min_periods=42).mean()
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issrecentwt_d_jerk_v119_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    raw = iss.ewm(span=42, min_periods=15).mean()
    base = raw / iss.abs().rolling(252, min_periods=63).mean().replace(0, np.nan)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creepscaled_d_jerk_v120_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    base = c / _mean(c.abs(), 252).replace(0, np.nan)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_waspreadmom_d_jerk_v121_signal(sharesbas, shareswa):
    spr = sharesbas / shareswa.replace(0, np.nan) - 1.0
    base = spr - spr.shift(63)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_coveragez_d_jerk_v122_signal(ncfcommon, sharesbas):
    iss = _rsum(_f19_issuance(ncfcommon), 126)
    add = (sharesbas - sharesbas.shift(126)).clip(lower=1.0)
    base = _z(iss / add, 504)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_netdilmom_d_jerk_v123_signal(ncfcommon, sharesbas):
    dilmom = _f19_growth(sharesbas, 126) - _f19_growth(sharesbas, 126).shift(63)
    ret = (-_f19_issuance(ncfcommon)).clip(lower=0)
    base = _z(dilmom, 504) - _z(_rsum(ret, 126), 504)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_compositez_d_jerk_v124_signal(sharesbas, shareswadil, shareswa, ncfcommon):
    z1 = _z(_f19_growth(sharesbas, 252), 504)
    z2 = _z(_f19_creep(shareswadil, shareswa).diff(252), 504)
    z3 = _z(_rsum(_f19_issuance(ncfcommon), 252) / sharesbas.replace(0, np.nan), 504)
    base = (z1 + z2 + z3) / 3.0
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilgrowchg_d_jerk_v125_signal(shareswadil):
    g = _f19_growth(shareswadil, 504)
    base = g - g.shift(252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basgrow_315d_jerk_v126_signal(sharesbas):
    base = _f19_growth(sharesbas, 315)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basgrow_441d_jerk_v127_signal(sharesbas):
    base = _f19_growth(sharesbas, 441)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilgrow_189d_jerk_v128_signal(shareswadil):
    base = _f19_growth(shareswadil, 189)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilgrow_378d_jerk_v129_signal(shareswadil):
    base = _f19_growth(shareswadil, 378)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_wagrow_189d_jerk_v130_signal(shareswa):
    base = _f19_growth(shareswa, 189)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_wagrow_378d_jerk_v131_signal(shareswa):
    base = _f19_growth(shareswa, 378)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issrng189_d_jerk_v132_signal(ncfcommon):
    q = _rsum(_f19_issuance(ncfcommon), 189)
    hi = _rmax(q, 504)
    lo = _rmin(q, 504)
    base = (q - lo) / (hi - lo).replace(0, np.nan) - 0.5
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issdir378_d_jerk_v133_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    base = _rsum(iss, 378) / _rsum(iss.abs(), 378).replace(0, np.nan)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_isspersh126_d_jerk_v134_signal(ncfcommon, sharesbas):
    ips = _rsum(_f19_issuance(ncfcommon), 126) / sharesbas.replace(0, np.nan)
    base = ips - ips.shift(126)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_isspersh189_d_jerk_v135_signal(ncfcommon, shareswadil):
    base = _rsum(_f19_issuance(ncfcommon), 189) / shareswadil.replace(0, np.nan)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creepskew_252d_jerk_v136_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    base = c.diff(21).rolling(252, min_periods=126).skew()
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creepmaxgap_252d_jerk_v137_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    base = (_rmax(c, 252) - c) / _std(c, 252).replace(0, np.nan)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilrank42_d_jerk_v138_signal(sharesbas):
    base = _rank(_f19_dil_rate(sharesbas, 42), 252)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilrank189_d_jerk_v139_signal(sharesbas):
    base = _rank(_f19_growth(sharesbas, 189), 504)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_wagrowmom252_d_jerk_v140_signal(shareswa):
    g = _f19_growth(shareswa, 252)
    base = g - g.shift(63)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilir63_d_jerk_v141_signal(sharesbas):
    g = sharesbas.pct_change(63)
    base = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilgrowz63_d_jerk_v142_signal(shareswadil):
    base = _z(_f19_growth(shareswadil, 63), 252)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_absorb252_d_jerk_v143_signal(sharesbas, shareswadil):
    base = _f19_growth(sharesbas, 252) - _f19_growth(shareswadil, 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_isspershrng_d_jerk_v144_signal(ncfcommon, sharesbas):
    ips = _rsum(_f19_issuance(ncfcommon), 63) / sharesbas.replace(0, np.nan)
    hi = _rmax(ips, 504)
    lo = _rmin(ips, 504)
    base = (ips - lo) / (hi - lo).replace(0, np.nan) - 0.5
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_wadildisp_d_jerk_v145_signal(shareswa):
    base = _std(shareswa.pct_change(21), 252)
    slope = base.diff(63)
    jerk = slope.diff(63)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basgrowsm_d_jerk_v146_signal(sharesbas):
    g = _f19_growth(sharesbas, 126)
    base = g.ewm(span=63, min_periods=21).mean()
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_dilgrowsm_d_jerk_v147_signal(shareswadil):
    g = _f19_growth(shareswadil, 126)
    base = g.ewm(span=63, min_periods=21).mean()
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_creepz126_d_jerk_v148_signal(shareswadil, shareswa):
    base = _z(_f19_creep(shareswadil, shareswa), 126)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_issz126_d_jerk_v149_signal(ncfcommon):
    base = _z(_f19_issuance(ncfcommon), 126)
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)


def f19di_f19_dilution_intensity_basrng126_d_jerk_v150_signal(sharesbas):
    r = sharesbas.pct_change(126)
    hi = _rmax(r, 504)
    lo = _rmin(r, 504)
    base = (r - lo) / (hi - lo).replace(0, np.nan) - 0.5
    slope = base.diff(21)
    jerk = slope.diff(21)
    result = jerk
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f19di_f19_dilution_intensity_basgrow_21d_jerk_v001_signal,
    f19di_f19_dilution_intensity_basgrow_42d_jerk_v002_signal,
    f19di_f19_dilution_intensity_basgrow_63d_jerk_v003_signal,
    f19di_f19_dilution_intensity_basgrow_126d_jerk_v004_signal,
    f19di_f19_dilution_intensity_basgrow_189d_jerk_v005_signal,
    f19di_f19_dilution_intensity_basgrow_252d_jerk_v006_signal,
    f19di_f19_dilution_intensity_basgrow_378d_jerk_v007_signal,
    f19di_f19_dilution_intensity_basgrow_504d_jerk_v008_signal,
    f19di_f19_dilution_intensity_wagrow_63d_jerk_v009_signal,
    f19di_f19_dilution_intensity_wagrow_126d_jerk_v010_signal,
    f19di_f19_dilution_intensity_wagrow_252d_jerk_v011_signal,
    f19di_f19_dilution_intensity_wagrow_504d_jerk_v012_signal,
    f19di_f19_dilution_intensity_dilgrow_63d_jerk_v013_signal,
    f19di_f19_dilution_intensity_dilgrow_126d_jerk_v014_signal,
    f19di_f19_dilution_intensity_dilgrow_252d_jerk_v015_signal,
    f19di_f19_dilution_intensity_dilgrow_504d_jerk_v016_signal,
    f19di_f19_dilution_intensity_basrate_5d_jerk_v017_signal,
    f19di_f19_dilution_intensity_basacc_42d_jerk_v018_signal,
    f19di_f19_dilution_intensity_dilrate_21d_jerk_v019_signal,
    f19di_f19_dilution_intensity_warate_42d_jerk_v020_signal,
    f19di_f19_dilution_intensity_basgrowz_63d_jerk_v021_signal,
    f19di_f19_dilution_intensity_basgrowz_126d_jerk_v022_signal,
    f19di_f19_dilution_intensity_basgrowz_252d_jerk_v023_signal,
    f19di_f19_dilution_intensity_dilgrowz_126d_jerk_v024_signal,
    f19di_f19_dilution_intensity_dilgrowz_252d_jerk_v025_signal,
    f19di_f19_dilution_intensity_wagrowz_126d_jerk_v026_signal,
    f19di_f19_dilution_intensity_dilrank_252d_jerk_v027_signal,
    f19di_f19_dilution_intensity_dilrank_126d_jerk_v028_signal,
    f19di_f19_dilution_intensity_dilrank_63d_jerk_v029_signal,
    f19di_f19_dilution_intensity_warank_63d_jerk_v030_signal,
    f19di_f19_dilution_intensity_dilcyclerank_126d_jerk_v031_signal,
    f19di_f19_dilution_intensity_creep_lvl_jerk_v032_signal,
    f19di_f19_dilution_intensity_creepz252_z_jerk_v033_signal,
    f19di_f19_dilution_intensity_creepz504_z_jerk_v034_signal,
    f19di_f19_dilution_intensity_creeprank_504d_jerk_v035_signal,
    f19di_f19_dilution_intensity_creeprank_1260d_jerk_v036_signal,
    f19di_f19_dilution_intensity_creepma63_d_jerk_v037_signal,
    f19di_f19_dilution_intensity_creepma252_d_jerk_v038_signal,
    f19di_f19_dilution_intensity_creepdisp_252d_jerk_v039_signal,
    f19di_f19_dilution_intensity_creepdisp_126d_jerk_v040_signal,
    f19di_f19_dilution_intensity_isscum_126d_jerk_v041_signal,
    f19di_f19_dilution_intensity_isscum_252d_jerk_v042_signal,
    f19di_f19_dilution_intensity_isscum_63d_jerk_v043_signal,
    f19di_f19_dilution_intensity_issz_252d_jerk_v044_signal,
    f19di_f19_dilution_intensity_issz_504d_jerk_v045_signal,
    f19di_f19_dilution_intensity_issnorm_d_jerk_v046_signal,
    f19di_f19_dilution_intensity_issperhsh_lvl_jerk_v047_signal,
    f19di_f19_dilution_intensity_issperhshq_63d_jerk_v048_signal,
    f19di_f19_dilution_intensity_issintens_252d_jerk_v049_signal,
    f19di_f19_dilution_intensity_isspersh_504d_jerk_v050_signal,
    f19di_f19_dilution_intensity_issbal_252d_jerk_v051_signal,
    f19di_f19_dilution_intensity_issdir_252d_jerk_v052_signal,
    f19di_f19_dilution_intensity_issdir_126d_jerk_v053_signal,
    f19di_f19_dilution_intensity_isshhi_252d_jerk_v054_signal,
    f19di_f19_dilution_intensity_issvolreg_d_jerk_v055_signal,
    f19di_f19_dilution_intensity_issskew_252d_jerk_v056_signal,
    f19di_f19_dilution_intensity_issregime_504d_jerk_v057_signal,
    f19di_f19_dilution_intensity_growspr_252d_jerk_v058_signal,
    f19di_f19_dilution_intensity_growspr_126d_jerk_v059_signal,
    f19di_f19_dilution_intensity_baswagap_lvl_jerk_v060_signal,
    f19di_f19_dilution_intensity_baswagapz_d_jerk_v061_signal,
    f19di_f19_dilution_intensity_absorb_126d_jerk_v062_signal,
    f19di_f19_dilution_intensity_zdiverge_63d_jerk_v063_signal,
    f19di_f19_dilution_intensity_amplif_63d_jerk_v064_signal,
    f19di_f19_dilution_intensity_overhangratio_lvl_jerk_v065_signal,
    f19di_f19_dilution_intensity_dildisp252_d_jerk_v066_signal,
    f19di_f19_dilution_intensity_dildisp63_d_jerk_v067_signal,
    f19di_f19_dilution_intensity_wadisp504_d_jerk_v068_signal,
    f19di_f19_dilution_intensity_dildildisp_252d_jerk_v069_signal,
    f19di_f19_dilution_intensity_dilsemidev_252d_jerk_v070_signal,
    f19di_f19_dilution_intensity_dilskew_252d_jerk_v071_signal,
    f19di_f19_dilution_intensity_dilkurt_252d_jerk_v072_signal,
    f19di_f19_dilution_intensity_dilcyclepos_504d_jerk_v073_signal,
    f19di_f19_dilution_intensity_dilregimedist_d_jerk_v074_signal,
    f19di_f19_dilution_intensity_paceslow_d_jerk_v075_signal,
    f19di_f19_dilution_intensity_pacevspeak_d_jerk_v076_signal,
    f19di_f19_dilution_intensity_dilema_d_jerk_v077_signal,
    f19di_f19_dilution_intensity_dilmom_252d_jerk_v078_signal,
    f19di_f19_dilution_intensity_dilmom_126d_jerk_v079_signal,
    f19di_f19_dilution_intensity_creepmom_63d_jerk_v080_signal,
    f19di_f19_dilution_intensity_creepvel_21d_jerk_v081_signal,
    f19di_f19_dilution_intensity_isstilt_126d_jerk_v082_signal,
    f19di_f19_dilution_intensity_issmom_126d_jerk_v083_signal,
    f19di_f19_dilution_intensity_isspershema_d_jerk_v084_signal,
    f19di_f19_dilution_intensity_dilstreak_252d_jerk_v085_signal,
    f19di_f19_dilution_intensity_monotone_252d_jerk_v086_signal,
    f19di_f19_dilution_intensity_dilstreakfrac_252d_jerk_v087_signal,
    f19di_f19_dilution_intensity_raisefrac_252d_jerk_v088_signal,
    f19di_f19_dilution_intensity_dilevents_252d_jerk_v089_signal,
    f19di_f19_dilution_intensity_dilentropy_252d_jerk_v090_signal,
    f19di_f19_dilution_intensity_issdilinter_252d_jerk_v091_signal,
    f19di_f19_dilution_intensity_issoverhang_d_jerk_v092_signal,
    f19di_f19_dilution_intensity_whipsaw_63d_jerk_v093_signal,
    f19di_f19_dilution_intensity_dilbeta_d_jerk_v094_signal,
    f19di_f19_dilution_intensity_basema252_d_jerk_v095_signal,
    f19di_f19_dilution_intensity_basema63_d_jerk_v096_signal,
    f19di_f19_dilution_intensity_dilpacesurp_d_jerk_v097_signal,
    f19di_f19_dilution_intensity_dilsurprise_252d_jerk_v098_signal,
    f19di_f19_dilution_intensity_dilsignmag_252d_jerk_v099_signal,
    f19di_f19_dilution_intensity_diltanh_63d_jerk_v100_signal,
    f19di_f19_dilution_intensity_bddivtanh_d_jerk_v101_signal,
    f19di_f19_dilution_intensity_dilsharpe_252d_jerk_v102_signal,
    f19di_f19_dilution_intensity_dilriskadj_126d_jerk_v103_signal,
    f19di_f19_dilution_intensity_cumdil_1260d_jerk_v104_signal,
    f19di_f19_dilution_intensity_dilvsmin504_d_jerk_v105_signal,
    f19di_f19_dilution_intensity_dilvsmin252_d_jerk_v106_signal,
    f19di_f19_dilution_intensity_dilpersist_d_jerk_v107_signal,
    f19di_f19_dilution_intensity_dispspread_d_jerk_v108_signal,
    f19di_f19_dilution_intensity_wamom_252d_jerk_v109_signal,
    f19di_f19_dilution_intensity_issslope_126d_jerk_v110_signal,
    f19di_f19_dilution_intensity_stepjump_63d_jerk_v111_signal,
    f19di_f19_dilution_intensity_maxdiljump_252d_jerk_v112_signal,
    f19di_f19_dilution_intensity_diltail_252d_jerk_v113_signal,
    f19di_f19_dilution_intensity_creepconvex_d_jerk_v114_signal,
    f19di_f19_dilution_intensity_creephigh_d_jerk_v115_signal,
    f19di_f19_dilution_intensity_dilterm_d_jerk_v116_signal,
    f19di_f19_dilution_intensity_dilpaceratio_d_jerk_v117_signal,
    f19di_f19_dilution_intensity_wadisp_ema_d_jerk_v118_signal,
    f19di_f19_dilution_intensity_issrecentwt_d_jerk_v119_signal,
    f19di_f19_dilution_intensity_creepscaled_d_jerk_v120_signal,
    f19di_f19_dilution_intensity_waspreadmom_d_jerk_v121_signal,
    f19di_f19_dilution_intensity_coveragez_d_jerk_v122_signal,
    f19di_f19_dilution_intensity_netdilmom_d_jerk_v123_signal,
    f19di_f19_dilution_intensity_compositez_d_jerk_v124_signal,
    f19di_f19_dilution_intensity_dilgrowchg_d_jerk_v125_signal,
    f19di_f19_dilution_intensity_basgrow_315d_jerk_v126_signal,
    f19di_f19_dilution_intensity_basgrow_441d_jerk_v127_signal,
    f19di_f19_dilution_intensity_dilgrow_189d_jerk_v128_signal,
    f19di_f19_dilution_intensity_dilgrow_378d_jerk_v129_signal,
    f19di_f19_dilution_intensity_wagrow_189d_jerk_v130_signal,
    f19di_f19_dilution_intensity_wagrow_378d_jerk_v131_signal,
    f19di_f19_dilution_intensity_issrng189_d_jerk_v132_signal,
    f19di_f19_dilution_intensity_issdir378_d_jerk_v133_signal,
    f19di_f19_dilution_intensity_isspersh126_d_jerk_v134_signal,
    f19di_f19_dilution_intensity_isspersh189_d_jerk_v135_signal,
    f19di_f19_dilution_intensity_creepskew_252d_jerk_v136_signal,
    f19di_f19_dilution_intensity_creepmaxgap_252d_jerk_v137_signal,
    f19di_f19_dilution_intensity_dilrank42_d_jerk_v138_signal,
    f19di_f19_dilution_intensity_dilrank189_d_jerk_v139_signal,
    f19di_f19_dilution_intensity_wagrowmom252_d_jerk_v140_signal,
    f19di_f19_dilution_intensity_dilir63_d_jerk_v141_signal,
    f19di_f19_dilution_intensity_dilgrowz63_d_jerk_v142_signal,
    f19di_f19_dilution_intensity_absorb252_d_jerk_v143_signal,
    f19di_f19_dilution_intensity_isspershrng_d_jerk_v144_signal,
    f19di_f19_dilution_intensity_wadildisp_d_jerk_v145_signal,
    f19di_f19_dilution_intensity_basgrowsm_d_jerk_v146_signal,
    f19di_f19_dilution_intensity_dilgrowsm_d_jerk_v147_signal,
    f19di_f19_dilution_intensity_creepz126_d_jerk_v148_signal,
    f19di_f19_dilution_intensity_issz126_d_jerk_v149_signal,
    f19di_f19_dilution_intensity_basrng126_d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_DILUTION_INTENSITY_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    sharesbas = _fund(101, base=8e7, drift=0.04, vol=0.06).rename("sharesbas")
    shareswa = _fund(102, base=7.6e7, drift=0.038, vol=0.05).rename("shareswa")
    shareswadil = _fund(103, base=8.4e7, drift=0.045, vol=0.07).rename("shareswadil")
    _raise = _fund(104, base=2e7, drift=0.02, vol=0.5)
    _return = _fund(105, base=1.6e7, drift=0.02, vol=0.45)
    ncfcommon = (_return - _raise).rename("ncfcommon")

    cols = {"sharesbas": sharesbas, "shareswa": shareswa,
            "shareswadil": shareswadil, "ncfcommon": ncfcommon}

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

    assert n_features == 150, n_features
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

    print("OK f19_dilution_intensity_3rd_derivatives_001_150_claude: %d features pass" % n_features)
