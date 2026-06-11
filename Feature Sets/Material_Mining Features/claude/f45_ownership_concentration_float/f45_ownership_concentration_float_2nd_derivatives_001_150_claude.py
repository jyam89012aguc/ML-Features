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


def _slope(s, w):
    x = pd.Series(np.arange(len(s), dtype=float), index=s.index)
    xm = x.rolling(w, min_periods=max(2, w // 2)).mean()
    ym = s.rolling(w, min_periods=max(2, w // 2)).mean()
    cov = (x * s).rolling(w, min_periods=max(2, w // 2)).mean() - xm * ym
    varx = (x * x).rolling(w, min_periods=max(2, w // 2)).mean() - xm * xm
    return cov / varx.replace(0, np.nan)


# ===== folder domain primitives (ownership concentration / float) =====
def _f45_total_holders(fnd, und, prf, dbt):
    return fnd + und + prf + dbt


def _f45_share(part, total):
    return part / total.replace(0, np.nan)


def _f45_hhi(fnd, und, prf, dbt):
    tot = (fnd + und + prf + dbt).replace(0, np.nan)
    s1, s2, s3, s4 = fnd / tot, und / tot, prf / tot, dbt / tot
    return s1 * s1 + s2 * s2 + s3 * s3 + s4 * s4


def _f45_entropy(fnd, und, prf, dbt):
    tot = (fnd + und + prf + dbt).replace(0, np.nan)
    out = pd.Series(0.0, index=fnd.index)
    for part in (fnd, und, prf, dbt):
        p = (part / tot).clip(lower=1e-12)
        out = out - p * np.log(p)
    return out


def _f45_value_per_holder(totalvalue, holders):
    return totalvalue / holders.replace(0, np.nan)



def f45of_f45_ownership_concentration_float_fndshare_lvl_slope_v001_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _f45_share(fndholders, tot)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_undshare_lvl_slope_v002_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _f45_share(undholders, tot)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_prfshare_lvl_slope_v003_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _f45_share(prfholders, tot)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_dbtshare_lvl_slope_v004_signal(fndholders, undholders, prfholders, dbtholders):
    eq = (fndholders + undholders + prfholders).replace(0, np.nan)
    b = dbtholders / eq
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_hhimix_lvl_slope_v005_signal(fndholders, undholders, prfholders, dbtholders):
    b = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_entmix_lvl_slope_v006_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    b = e - e.shift(63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_lvl_slope_v007_signal(percentoftotal):
    b = percentoftotal
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadth_lvl_slope_v008_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(tot.replace(0, np.nan))
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_valperhld_lvl_slope_v009_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(_f45_value_per_holder(totalvalue, tot).replace(0, np.nan))
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_tightfloat_lvl_slope_v010_signal(percentoftotal, shrholders):
    # ratio of concentration growth to shareholder-base growth: are few holders amassing the float?
    dconc = percentoftotal / percentoftotal.shift(126).replace(0, np.nan)
    dshr = shrholders / shrholders.shift(126).replace(0, np.nan)
    b = np.log(dconc.replace(0, np.nan)) - np.log(dshr.replace(0, np.nan))
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndshare_z252_slope_v011_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = _z(sh, 252)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_hhimix_z252_slope_v012_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = _z(h, 252)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_z252_slope_v013_signal(percentoftotal):
    b = _z(percentoftotal, 252)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadth_z252_slope_v014_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _z(np.log(tot.replace(0, np.nan)), 252)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_entmix_z252_slope_v015_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    b = _z(e, 252)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fnddbtspr_lvl_slope_v016_signal(fndholders, dbtholders):
    spr = (fndholders - dbtholders) / (fndholders + dbtholders).replace(0, np.nan)
    b = spr - spr.shift(63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndprfspr_lvl_slope_v017_signal(fndholders, prfholders):
    b = (fndholders - prfholders) / (fndholders + prfholders).replace(0, np.nan)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_unddbtspr_lvl_slope_v018_signal(undholders, dbtholders):
    b = (undholders - dbtholders) / (undholders + dbtholders).replace(0, np.nan)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndundratio_lvl_slope_v019_signal(fndholders, undholders):
    b = np.log((fndholders + 1.0) / (undholders + 1.0))
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_structshare_lvl_slope_v020_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = (prfholders + dbtholders) / tot.replace(0, np.nan)
    b = sh - sh.shift(63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_slp63_slope_v021_signal(percentoftotal):
    b = _slope(percentoftotal, 63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndshare_slp126_slope_v022_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = _slope(sh, 126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadth_slp126_slope_v023_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _slope(np.log(tot.replace(0, np.nan)), 126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_hhimix_slp126_slope_v024_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = _slope(h, 126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_totval_slp126_slope_v025_signal(totalvalue):
    b = _slope(np.log(totalvalue.replace(0, np.nan)), 126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_mom63_slope_v026_signal(percentoftotal):
    b = (percentoftotal - percentoftotal.shift(63)) / percentoftotal.shift(63).replace(0, np.nan)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadth_mom63_slope_v027_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    b = lt - lt.shift(63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndcnt_mom63_slope_v028_signal(fndholders):
    b = np.log(fndholders + 1.0) - np.log(fndholders.shift(63) + 1.0)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_dbtcnt_mom63_slope_v029_signal(dbtholders):
    b = np.log(dbtholders + 1.0) - np.log(dbtholders.shift(63) + 1.0)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_valperhld_mom63_slope_v030_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    v = np.log(_f45_value_per_holder(totalvalue, tot).replace(0, np.nan))
    b = v - v.shift(63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_accel_slope_v031_signal(percentoftotal):
    mom = percentoftotal - percentoftotal.shift(63)
    b = mom - mom.shift(63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_efftypes_lvl_slope_v032_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    eff = 1.0 / h.replace(0, np.nan)
    b = _rmax(eff, 126) - _rmin(eff, 126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_concratio_lvl_slope_v033_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = _z(percentoftotal, 252) - _z(h, 252)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_domtype_lvl_slope_v034_signal(fndholders, undholders, prfholders, dbtholders):
    stacked = pd.concat([fndholders, undholders, prfholders, dbtholders], axis=1)
    idx = stacked.values.argmax(axis=1).astype(float)
    lead = pd.Series(idx, index=fndholders.index)
    # smooth into a persistence-weighted regime so it is non-trivially varying
    b = lead.rolling(63, min_periods=21).mean()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_typedisp_lvl_slope_v035_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    stacked = pd.concat([fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot], axis=1)
    disp = stacked.std(axis=1)
    b = _slope(disp, 63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_tightcompound_slope_v036_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = percentoftotal * h
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_valtopconc_slope_v037_signal(totalvalue, percentoftotal):
    dollar = np.log((totalvalue * percentoftotal).replace(0, np.nan))
    b = dollar - dollar.shift(63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_vol126_slope_v038_signal(percentoftotal):
    b = _std(percentoftotal, 126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndshare_vol126_slope_v039_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = _std(sh, 126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadth_vol126_slope_v040_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _std(np.log(tot.replace(0, np.nan)), 126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_prfshare_slp63_slope_v041_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(prfholders, tot)
    b = _slope(sh, 63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_undshare_slp63_slope_v042_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(undholders, tot)
    b = _slope(sh, 63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_entmix_slp126_slope_v043_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    slp = _slope(e, 126)
    b = slp - slp.shift(63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_rngpos_slope_v044_signal(percentoftotal):
    hi = _rmax(percentoftotal, 1260)
    lo = _rmin(percentoftotal, 1260)
    rngpos = (percentoftotal - lo) / (hi - lo).replace(0, np.nan)
    # convexity emphasis distinguishes it from a plain z-score
    b = np.sign(rngpos - 0.5) * (rngpos - 0.5) ** 2 * 4.0
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadth_rngpos_slope_v045_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    peak = _rmax(tot, 504)
    b = tot / peak.replace(0, np.nan) - 1.0
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndshare_rank_slope_v046_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    prior_max = sh.shift(1).rolling(252, min_periods=63).max()
    b = sh / prior_max.replace(0, np.nan) - 1.0
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_rank504_slope_v047_signal(percentoftotal):
    b = percentoftotal.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_valperhld_z252_slope_v048_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    v = np.log(_f45_value_per_holder(totalvalue, tot).replace(0, np.nan))
    b = _z(v, 252)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_tightval_lvl_slope_v049_signal(totalvalue, percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    dollar = totalvalue * percentoftotal / np.log(tot.replace(0, np.nan) + np.e)
    peak = _rmax(dollar, 252)
    b = dollar / peak.replace(0, np.nan) - 1.0
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_prffndratio_slope_v050_signal(prfholders, fndholders):
    r = np.log((prfholders + 1.0) / (fndholders + 1.0))
    b = r - r.shift(63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_dbtfndratio_slope_v051_signal(dbtholders, fndholders):
    r = np.log((dbtholders + 1.0) / (fndholders + 1.0))
    b = r - r.shift(126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_mixshift_l1_slope_v052_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    parts = [fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot]
    out = pd.Series(0.0, index=fndholders.index)
    for p in parts:
        out = out + (p - p.shift(63)).abs()
    result = out - out.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_concbreadth_x_slope_v053_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    dconc = percentoftotal - percentoftotal.shift(63)
    dbreadth = np.log(tot.replace(0, np.nan)) - np.log(tot.shift(63).replace(0, np.nan))
    b = dconc * np.sign(-dbreadth) * dbreadth.abs()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_ema_slope_v054_signal(percentoftotal):
    b = percentoftotal.ewm(span=63, min_periods=21).mean()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_disp_slope_v055_signal(percentoftotal):
    med = percentoftotal.rolling(126, min_periods=42).median()
    b = (percentoftotal - med) / med.replace(0, np.nan)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndshare_disp_slope_v056_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = sh - sh.ewm(span=126, min_periods=42).mean()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_entmix_disp_slope_v057_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    b = e - e.ewm(span=126, min_periods=42).mean()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_hhinorm_lvl_slope_v058_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = (1.0 - h) * np.log(tot.replace(0, np.nan) + np.e)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_valbreadth_slope_v059_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _z(np.log(totalvalue.replace(0, np.nan)), 126) - _z(np.log(tot.replace(0, np.nan)), 126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_concregime_slope_v060_signal(percentoftotal):
    med = percentoftotal.rolling(252, min_periods=126).median()
    above = (percentoftotal > med).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_tightregime_slope_v061_signal(percentoftotal):
    med = percentoftotal.rolling(252, min_periods=126).median()
    excess = (percentoftotal / med.replace(0, np.nan) - 1.0)
    above = (excess > 0).astype(float)
    grp = (above == 0).cumsum()
    run = above.groupby(grp).cumsum()
    # run length scaled by current above-median depth -> continuous, high-cardinality
    b = (run * excess.clip(lower=0.0)).ewm(span=42, min_periods=21).mean()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadthstreak_slope_v062_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    up = (tot >= tot.shift(63)).astype(float)
    grp = (up == 0).cumsum()
    b = up.groupby(grp).cumsum()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_concstreak_slope_v063_signal(percentoftotal):
    up = (percentoftotal >= percentoftotal.shift(63)).astype(float)
    grp = (up == 0).cumsum()
    b = up.groupby(grp).cumsum()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_exittally_slope_v064_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    drop = (tot.shift(63) - tot) / tot.shift(63).replace(0, np.nan)
    contract = drop.clip(lower=0.0)
    b = contract.rolling(252, min_periods=126).sum()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_concsignmag_slope_v065_signal(percentoftotal):
    chg = percentoftotal - percentoftotal.shift(63)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_valhhi_slope_v066_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    dh = h - h.shift(21)
    dv = np.log(totalvalue.replace(0, np.nan)) - np.log(totalvalue.shift(21).replace(0, np.nan))
    b = (dh * dv).rolling(126, min_periods=42).mean()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndminusdbt_slope_v067_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    spr = fndholders / tot - dbtholders / tot
    b = spr.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_yoy_slope_v068_signal(percentoftotal):
    b = percentoftotal - percentoftotal.shift(252)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadth_yoy_slope_v069_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    b = lt - lt.shift(252)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_concqual_slope_v070_signal(percentoftotal):
    slp = _slope(percentoftotal, 126)
    vol = _std(percentoftotal, 126)
    b = slp / vol.replace(0, np.nan)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_tightslp_slope_v071_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    tight = percentoftotal / np.log(tot.replace(0, np.nan) + np.e)
    b = _std(tight.diff(), 126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_typegini_slope_v072_signal(fndholders, undholders, prfholders, dbtholders):
    minor = (undholders + prfholders + dbtholders).replace(0, np.nan)
    b = np.log((undholders + 1.0) / (prfholders + 1.0)) + 0.0 * minor
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_conctanh_slope_v073_signal(percentoftotal):
    chg = percentoftotal - percentoftotal.shift(21)
    b = np.tanh(50.0 * chg)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_entbreadth_slope_v074_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    de = e - e.shift(63)
    db = np.log(tot.replace(0, np.nan)) - np.log(tot.shift(63).replace(0, np.nan))
    b = de - db
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_totval_dd_slope_v075_signal(totalvalue):
    peak = _rmax(totalvalue, 252)
    b = totalvalue / peak.replace(0, np.nan) - 1.0
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndshare_sm126_slope_v076_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = sh.ewm(span=126, min_periods=42).mean()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_undshare_lvl_slope_v077_signal(fndholders, undholders, prfholders, dbtholders):
    rest = (fndholders + prfholders + dbtholders).replace(0, np.nan)
    ratio = undholders / rest
    b = _z(ratio, 252)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_prfshare_disp_slope_v078_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(prfholders, tot)
    b = sh - _mean(sh, 252)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_dbtshare_logodds_slope_v079_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(dbtholders, tot).clip(lower=1e-6, upper=1 - 1e-6)
    lo = np.log(sh / (1.0 - sh))
    b = lo - lo.shift(63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_hhi_sm63_slope_v080_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = h.ewm(span=63, min_periods=21).mean()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_compound_sm_slope_v081_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    raw = percentoftotal * h
    b = raw.ewm(span=63, min_periods=21).mean()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_anom504_slope_v082_signal(percentoftotal):
    med = percentoftotal.rolling(504, min_periods=126).median()
    b = percentoftotal - med
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadth_anom504_slope_v083_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = tot / _mean(tot, 504).replace(0, np.nan) - 1.0
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_valperhld_anom_slope_v084_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    vpf = totalvalue / fndholders.replace(0, np.nan)
    b = np.log(vpf.replace(0, np.nan)) - 0.5 * np.log(totalvalue.replace(0, np.nan))
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_tightfloat2_slope_v085_signal(percentoftotal, shrholders):
    inv_shr = -_z(np.log(shrholders.replace(0, np.nan)), 252)
    b = _z(percentoftotal, 252) * inv_shr
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndshare_slp252_slope_v086_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = _slope(sh, 252)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_slp252_slope_v087_signal(percentoftotal):
    b = _slope(percentoftotal, 252)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadth_slp252_slope_v088_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _slope(np.log(tot.replace(0, np.nan)), 252)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_hhi_slp252_slope_v089_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = _slope(h, 252)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_totval_slp252_slope_v090_signal(totalvalue):
    b = _slope(np.log(totalvalue.replace(0, np.nan)), 252)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndcnt_athgap_slope_v091_signal(fndholders):
    peak = _rmax(fndholders, 252)
    b = fndholders / peak.replace(0, np.nan) - 1.0
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_dbtcnt_trough_slope_v092_signal(dbtholders):
    trough = _rmin(dbtholders, 252)
    b = dbtholders / trough.replace(0, np.nan) - 1.0
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_prfcnt_mom126_slope_v093_signal(prfholders):
    b = np.log(prfholders + 1.0) - np.log(prfholders.shift(126) + 1.0)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_undcnt_mom126_slope_v094_signal(undholders):
    b = np.log(undholders + 1.0) - np.log(undholders.shift(126) + 1.0)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_shrcnt_mom126_slope_v095_signal(shrholders):
    b = np.log(shrholders + 1.0) - np.log(shrholders.shift(126) + 1.0)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndshrratio_slope_v096_signal(fndholders, shrholders):
    b = np.log((fndholders + 1.0) / (shrholders + 1.0))
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_valshr_slope_v097_signal(totalvalue, shrholders):
    b = np.log(totalvalue.replace(0, np.nan)) - np.log(shrholders.replace(0, np.nan))
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topvalshr_slope_v098_signal(totalvalue, percentoftotal, shrholders):
    dollar = totalvalue * percentoftotal
    b = np.log(dollar.replace(0, np.nan)) - np.log(shrholders.replace(0, np.nan))
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndshare_z504_slope_v099_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = _z(sh, 504)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_z504_slope_v100_signal(percentoftotal):
    b = _z(percentoftotal, 504)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_hhi_z504_slope_v101_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = _z(h, 504)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadth_rank1260_slope_v102_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = tot.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_rank1260_slope_v103_signal(percentoftotal):
    b = percentoftotal.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_vol63_slope_v104_signal(percentoftotal):
    b = _std(percentoftotal, 63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_hhi_vol126_slope_v105_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = _std(h, 126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_ent_vol126_slope_v106_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    b = _std(e, 126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_totval_vol126_slope_v107_signal(totalvalue):
    r = np.log(totalvalue.replace(0, np.nan)).diff()
    b = _std(r, 126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_topconc_cov126_slope_v108_signal(percentoftotal):
    hi = _rmax(percentoftotal, 126)
    lo = _rmin(percentoftotal, 126)
    b = (hi - lo) / _mean(percentoftotal, 126).replace(0, np.nan)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndshare_qual_slope_v109_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = _slope(sh, 126) / _std(sh, 126).replace(0, np.nan)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadth_qual_slope_v110_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    b = _slope(lt, 126) / _std(lt, 126).replace(0, np.nan)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_totval_qual_slope_v111_signal(totalvalue):
    r = np.log(totalvalue.replace(0, np.nan))
    mom = r - r.shift(126)
    vol = _std(r.diff(), 126) * np.sqrt(126.0)
    b = mom / vol.replace(0, np.nan)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_tightterc_slope_v112_signal(percentoftotal):
    q = percentoftotal.rolling(252, min_periods=126).quantile(0.6667)
    tight = (percentoftotal >= q).astype(float)
    b = tight.rolling(252, min_periods=126).mean()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadthlow_slope_v113_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    below = (tot < _mean(tot, 252)).astype(float)
    b = below.rolling(252, min_periods=126).mean()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_conchitally_slope_v114_signal(percentoftotal):
    roll_max = percentoftotal.shift(1).rolling(126, min_periods=42).max()
    is_new = (percentoftotal > roll_max).astype(float)
    tally = is_new.rolling(126, min_periods=42).sum()
    depth = (percentoftotal / percentoftotal.rolling(126, min_periods=42).mean().replace(0, np.nan))
    b = tally + depth
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadthlotally_slope_v115_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    roll_min = tot.shift(1).rolling(126, min_periods=42).min()
    is_new = (tot < roll_min).astype(float)
    tally = is_new.rolling(126, min_periods=42).sum()
    shortfall = (tot.rolling(126, min_periods=42).mean() / tot.replace(0, np.nan))
    b = tally + shortfall
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_concstreak126_slope_v116_signal(percentoftotal):
    up = (percentoftotal >= percentoftotal.shift(126)).astype(float)
    grp = (up == 0).cumsum()
    b = up.groupby(grp).cumsum()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fnddomstreak_slope_v117_signal(fndholders, undholders, prfholders, dbtholders):
    other = pd.concat([undholders, prfholders, dbtholders], axis=1).max(axis=1)
    lead = (fndholders >= other).astype(float)
    grp = (lead == 0).cumsum()
    b = lead.groupby(grp).cumsum()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadthsignmag_slope_v118_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    chg = lt - lt.shift(63)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadthtanh_slope_v119_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    chg = lt - lt.shift(21)
    b = np.tanh(10.0 * chg)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_concyoyaccel_slope_v120_signal(percentoftotal):
    yoy = percentoftotal - percentoftotal.shift(252)
    b = yoy - yoy.shift(252)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndgrip_slope_v121_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = _z(sh, 252) + _z(percentoftotal, 252)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_dbtgrip_slope_v122_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(dbtholders, tot)
    b = _z(sh, 252) * _z(percentoftotal, 252)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_valconc_div_slope_v123_signal(totalvalue, percentoftotal):
    dv = np.log(totalvalue.replace(0, np.nan)) - np.log(totalvalue.shift(63).replace(0, np.nan))
    dc = percentoftotal - percentoftotal.shift(63)
    b = _z(dv, 252) - _z(dc, 252)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_valperhld_slp_slope_v124_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    v = np.log(_f45_value_per_holder(totalvalue, tot).replace(0, np.nan))
    b = _slope(v, 126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_structbal_slope_v125_signal(fndholders, undholders, prfholders, dbtholders):
    struct = prfholders + dbtholders
    common = fndholders + undholders
    b = np.log((struct + 1.0) / (common + 1.0))
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_structbal_slp_slope_v126_signal(fndholders, undholders, prfholders, dbtholders):
    struct = prfholders + dbtholders
    common = fndholders + undholders
    r = np.log((struct + 1.0) / (common + 1.0))
    b = _slope(r, 63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_mixshift_yoy_slope_v127_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    parts = [fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot]
    out = pd.Series(0.0, index=fndholders.index)
    for p in parts:
        out = out + (p - p.shift(252)).abs()
    result = out - out.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_ent_dd_slope_v128_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    peak = _rmax(e, 504)
    b = e / peak.replace(0, np.nan) - 1.0
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_concmacd_slope_v129_signal(percentoftotal):
    fast = percentoftotal.ewm(span=21, min_periods=10).mean()
    slow = percentoftotal.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadthmacd_slope_v130_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    fast = tot.ewm(span=21, min_periods=10).mean()
    slow = tot.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_concmr_slope_v131_signal(percentoftotal):
    med = percentoftotal.rolling(252, min_periods=63).median()
    q75 = percentoftotal.rolling(252, min_periods=63).quantile(0.75)
    q25 = percentoftotal.rolling(252, min_periods=63).quantile(0.25)
    b = (percentoftotal - med) / (q75 - q25).replace(0, np.nan)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fndshare_mr_slope_v132_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    med = sh.rolling(252, min_periods=63).median()
    q75 = sh.rolling(252, min_periods=63).quantile(0.75)
    q25 = sh.rolling(252, min_periods=63).quantile(0.25)
    b = (sh - med) / (q75 - q25).replace(0, np.nan)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_undshare_rank_slope_v133_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(undholders, tot)
    b = sh.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_prfshare_rank_slope_v134_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(prfholders, tot)
    b = sh.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_compound_slp_slope_v135_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    comp = percentoftotal * h
    b = _slope(comp, 252)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_totval_dd504_slope_v136_signal(totalvalue):
    peak = _rmax(totalvalue, 504)
    b = totalvalue / peak.replace(0, np.nan) - 1.0
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_totval_recov_slope_v137_signal(totalvalue):
    trough = _rmin(totalvalue, 504)
    b = totalvalue / trough.replace(0, np.nan) - 1.0
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_smartflow_slope_v138_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    dsh = sh - sh.shift(63)
    dv = np.log(totalvalue.replace(0, np.nan)) - np.log(totalvalue.shift(63).replace(0, np.nan))
    b = np.sign(dsh) * dv.abs()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_tightenrise_slope_v139_signal(totalvalue, percentoftotal):
    dc = percentoftotal - percentoftotal.shift(63)
    dv = np.log(totalvalue.replace(0, np.nan)) - np.log(totalvalue.shift(63).replace(0, np.nan))
    b = dc * np.sign(dv) * dv.abs()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_scissors_slope_v140_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    b = _z(percentoftotal, 252) - _z(lt, 252)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_efftypes_lvl_slope_v141_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    eff_hhi = 1.0 / h.replace(0, np.nan)
    eff_ent = np.exp(e)
    b = eff_ent / eff_hhi.replace(0, np.nan)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_conccurv_slope_v142_signal(percentoftotal):
    b = percentoftotal.shift(42) - 2.0 * percentoftotal.shift(21) + percentoftotal
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_breadthcurv_slope_v143_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    b = lt.shift(42) - 2.0 * lt.shift(21) + lt
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_fnddbtratio_slope_v144_signal(fndholders, dbtholders):
    b = np.log((fndholders + 1.0) / (dbtholders + 1.0))
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_prfdbtratio_slope_v145_signal(prfholders, dbtholders):
    b = np.log((prfholders + 1.0) / (dbtholders + 1.0))
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_tightcap_slope_v146_signal(totalvalue, percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    vph = np.log(_f45_value_per_holder(totalvalue, tot).replace(0, np.nan))
    b = _z(percentoftotal, 252) + _z(vph, 252)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_theil_slope_v147_signal(totalvalue, percentoftotal):
    b = np.log(totalvalue.replace(0, np.nan)) - np.log(percentoftotal.replace(0, np.nan))
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_concpersist_slope_v148_signal(percentoftotal):
    med = percentoftotal.rolling(504, min_periods=126).median()
    above = (percentoftotal > med).astype(float)
    b = above.rolling(126, min_periods=42).mean()
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_valflow_slope_v149_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    dv = np.log(totalvalue.replace(0, np.nan)) - np.log(totalvalue.shift(126).replace(0, np.nan))
    db = np.log(tot.replace(0, np.nan)) - np.log(tot.shift(126).replace(0, np.nan))
    b = dv - db
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f45of_f45_ownership_concentration_float_floatscore_slope_v150_signal(totalvalue, percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    dv = np.log(totalvalue.replace(0, np.nan))
    b = _z(percentoftotal, 252) - _z(lt, 252) + 0.5 * _z(dv, 252)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f45of_f45_ownership_concentration_float_fndshare_lvl_slope_v001_signal,
    f45of_f45_ownership_concentration_float_undshare_lvl_slope_v002_signal,
    f45of_f45_ownership_concentration_float_prfshare_lvl_slope_v003_signal,
    f45of_f45_ownership_concentration_float_dbtshare_lvl_slope_v004_signal,
    f45of_f45_ownership_concentration_float_hhimix_lvl_slope_v005_signal,
    f45of_f45_ownership_concentration_float_entmix_lvl_slope_v006_signal,
    f45of_f45_ownership_concentration_float_topconc_lvl_slope_v007_signal,
    f45of_f45_ownership_concentration_float_breadth_lvl_slope_v008_signal,
    f45of_f45_ownership_concentration_float_valperhld_lvl_slope_v009_signal,
    f45of_f45_ownership_concentration_float_tightfloat_lvl_slope_v010_signal,
    f45of_f45_ownership_concentration_float_fndshare_z252_slope_v011_signal,
    f45of_f45_ownership_concentration_float_hhimix_z252_slope_v012_signal,
    f45of_f45_ownership_concentration_float_topconc_z252_slope_v013_signal,
    f45of_f45_ownership_concentration_float_breadth_z252_slope_v014_signal,
    f45of_f45_ownership_concentration_float_entmix_z252_slope_v015_signal,
    f45of_f45_ownership_concentration_float_fnddbtspr_lvl_slope_v016_signal,
    f45of_f45_ownership_concentration_float_fndprfspr_lvl_slope_v017_signal,
    f45of_f45_ownership_concentration_float_unddbtspr_lvl_slope_v018_signal,
    f45of_f45_ownership_concentration_float_fndundratio_lvl_slope_v019_signal,
    f45of_f45_ownership_concentration_float_structshare_lvl_slope_v020_signal,
    f45of_f45_ownership_concentration_float_topconc_slp63_slope_v021_signal,
    f45of_f45_ownership_concentration_float_fndshare_slp126_slope_v022_signal,
    f45of_f45_ownership_concentration_float_breadth_slp126_slope_v023_signal,
    f45of_f45_ownership_concentration_float_hhimix_slp126_slope_v024_signal,
    f45of_f45_ownership_concentration_float_totval_slp126_slope_v025_signal,
    f45of_f45_ownership_concentration_float_topconc_mom63_slope_v026_signal,
    f45of_f45_ownership_concentration_float_breadth_mom63_slope_v027_signal,
    f45of_f45_ownership_concentration_float_fndcnt_mom63_slope_v028_signal,
    f45of_f45_ownership_concentration_float_dbtcnt_mom63_slope_v029_signal,
    f45of_f45_ownership_concentration_float_valperhld_mom63_slope_v030_signal,
    f45of_f45_ownership_concentration_float_topconc_accel_slope_v031_signal,
    f45of_f45_ownership_concentration_float_efftypes_lvl_slope_v032_signal,
    f45of_f45_ownership_concentration_float_concratio_lvl_slope_v033_signal,
    f45of_f45_ownership_concentration_float_domtype_lvl_slope_v034_signal,
    f45of_f45_ownership_concentration_float_typedisp_lvl_slope_v035_signal,
    f45of_f45_ownership_concentration_float_tightcompound_slope_v036_signal,
    f45of_f45_ownership_concentration_float_valtopconc_slope_v037_signal,
    f45of_f45_ownership_concentration_float_topconc_vol126_slope_v038_signal,
    f45of_f45_ownership_concentration_float_fndshare_vol126_slope_v039_signal,
    f45of_f45_ownership_concentration_float_breadth_vol126_slope_v040_signal,
    f45of_f45_ownership_concentration_float_prfshare_slp63_slope_v041_signal,
    f45of_f45_ownership_concentration_float_undshare_slp63_slope_v042_signal,
    f45of_f45_ownership_concentration_float_entmix_slp126_slope_v043_signal,
    f45of_f45_ownership_concentration_float_topconc_rngpos_slope_v044_signal,
    f45of_f45_ownership_concentration_float_breadth_rngpos_slope_v045_signal,
    f45of_f45_ownership_concentration_float_fndshare_rank_slope_v046_signal,
    f45of_f45_ownership_concentration_float_topconc_rank504_slope_v047_signal,
    f45of_f45_ownership_concentration_float_valperhld_z252_slope_v048_signal,
    f45of_f45_ownership_concentration_float_tightval_lvl_slope_v049_signal,
    f45of_f45_ownership_concentration_float_prffndratio_slope_v050_signal,
    f45of_f45_ownership_concentration_float_dbtfndratio_slope_v051_signal,
    f45of_f45_ownership_concentration_float_mixshift_l1_slope_v052_signal,
    f45of_f45_ownership_concentration_float_concbreadth_x_slope_v053_signal,
    f45of_f45_ownership_concentration_float_topconc_ema_slope_v054_signal,
    f45of_f45_ownership_concentration_float_topconc_disp_slope_v055_signal,
    f45of_f45_ownership_concentration_float_fndshare_disp_slope_v056_signal,
    f45of_f45_ownership_concentration_float_entmix_disp_slope_v057_signal,
    f45of_f45_ownership_concentration_float_hhinorm_lvl_slope_v058_signal,
    f45of_f45_ownership_concentration_float_valbreadth_slope_v059_signal,
    f45of_f45_ownership_concentration_float_concregime_slope_v060_signal,
    f45of_f45_ownership_concentration_float_tightregime_slope_v061_signal,
    f45of_f45_ownership_concentration_float_breadthstreak_slope_v062_signal,
    f45of_f45_ownership_concentration_float_concstreak_slope_v063_signal,
    f45of_f45_ownership_concentration_float_exittally_slope_v064_signal,
    f45of_f45_ownership_concentration_float_concsignmag_slope_v065_signal,
    f45of_f45_ownership_concentration_float_valhhi_slope_v066_signal,
    f45of_f45_ownership_concentration_float_fndminusdbt_slope_v067_signal,
    f45of_f45_ownership_concentration_float_topconc_yoy_slope_v068_signal,
    f45of_f45_ownership_concentration_float_breadth_yoy_slope_v069_signal,
    f45of_f45_ownership_concentration_float_concqual_slope_v070_signal,
    f45of_f45_ownership_concentration_float_tightslp_slope_v071_signal,
    f45of_f45_ownership_concentration_float_typegini_slope_v072_signal,
    f45of_f45_ownership_concentration_float_conctanh_slope_v073_signal,
    f45of_f45_ownership_concentration_float_entbreadth_slope_v074_signal,
    f45of_f45_ownership_concentration_float_totval_dd_slope_v075_signal,
    f45of_f45_ownership_concentration_float_fndshare_sm126_slope_v076_signal,
    f45of_f45_ownership_concentration_float_undshare_lvl_slope_v077_signal,
    f45of_f45_ownership_concentration_float_prfshare_disp_slope_v078_signal,
    f45of_f45_ownership_concentration_float_dbtshare_logodds_slope_v079_signal,
    f45of_f45_ownership_concentration_float_hhi_sm63_slope_v080_signal,
    f45of_f45_ownership_concentration_float_compound_sm_slope_v081_signal,
    f45of_f45_ownership_concentration_float_topconc_anom504_slope_v082_signal,
    f45of_f45_ownership_concentration_float_breadth_anom504_slope_v083_signal,
    f45of_f45_ownership_concentration_float_valperhld_anom_slope_v084_signal,
    f45of_f45_ownership_concentration_float_tightfloat2_slope_v085_signal,
    f45of_f45_ownership_concentration_float_fndshare_slp252_slope_v086_signal,
    f45of_f45_ownership_concentration_float_topconc_slp252_slope_v087_signal,
    f45of_f45_ownership_concentration_float_breadth_slp252_slope_v088_signal,
    f45of_f45_ownership_concentration_float_hhi_slp252_slope_v089_signal,
    f45of_f45_ownership_concentration_float_totval_slp252_slope_v090_signal,
    f45of_f45_ownership_concentration_float_fndcnt_athgap_slope_v091_signal,
    f45of_f45_ownership_concentration_float_dbtcnt_trough_slope_v092_signal,
    f45of_f45_ownership_concentration_float_prfcnt_mom126_slope_v093_signal,
    f45of_f45_ownership_concentration_float_undcnt_mom126_slope_v094_signal,
    f45of_f45_ownership_concentration_float_shrcnt_mom126_slope_v095_signal,
    f45of_f45_ownership_concentration_float_fndshrratio_slope_v096_signal,
    f45of_f45_ownership_concentration_float_valshr_slope_v097_signal,
    f45of_f45_ownership_concentration_float_topvalshr_slope_v098_signal,
    f45of_f45_ownership_concentration_float_fndshare_z504_slope_v099_signal,
    f45of_f45_ownership_concentration_float_topconc_z504_slope_v100_signal,
    f45of_f45_ownership_concentration_float_hhi_z504_slope_v101_signal,
    f45of_f45_ownership_concentration_float_breadth_rank1260_slope_v102_signal,
    f45of_f45_ownership_concentration_float_topconc_rank1260_slope_v103_signal,
    f45of_f45_ownership_concentration_float_topconc_vol63_slope_v104_signal,
    f45of_f45_ownership_concentration_float_hhi_vol126_slope_v105_signal,
    f45of_f45_ownership_concentration_float_ent_vol126_slope_v106_signal,
    f45of_f45_ownership_concentration_float_totval_vol126_slope_v107_signal,
    f45of_f45_ownership_concentration_float_topconc_cov126_slope_v108_signal,
    f45of_f45_ownership_concentration_float_fndshare_qual_slope_v109_signal,
    f45of_f45_ownership_concentration_float_breadth_qual_slope_v110_signal,
    f45of_f45_ownership_concentration_float_totval_qual_slope_v111_signal,
    f45of_f45_ownership_concentration_float_tightterc_slope_v112_signal,
    f45of_f45_ownership_concentration_float_breadthlow_slope_v113_signal,
    f45of_f45_ownership_concentration_float_conchitally_slope_v114_signal,
    f45of_f45_ownership_concentration_float_breadthlotally_slope_v115_signal,
    f45of_f45_ownership_concentration_float_concstreak126_slope_v116_signal,
    f45of_f45_ownership_concentration_float_fnddomstreak_slope_v117_signal,
    f45of_f45_ownership_concentration_float_breadthsignmag_slope_v118_signal,
    f45of_f45_ownership_concentration_float_breadthtanh_slope_v119_signal,
    f45of_f45_ownership_concentration_float_concyoyaccel_slope_v120_signal,
    f45of_f45_ownership_concentration_float_fndgrip_slope_v121_signal,
    f45of_f45_ownership_concentration_float_dbtgrip_slope_v122_signal,
    f45of_f45_ownership_concentration_float_valconc_div_slope_v123_signal,
    f45of_f45_ownership_concentration_float_valperhld_slp_slope_v124_signal,
    f45of_f45_ownership_concentration_float_structbal_slope_v125_signal,
    f45of_f45_ownership_concentration_float_structbal_slp_slope_v126_signal,
    f45of_f45_ownership_concentration_float_mixshift_yoy_slope_v127_signal,
    f45of_f45_ownership_concentration_float_ent_dd_slope_v128_signal,
    f45of_f45_ownership_concentration_float_concmacd_slope_v129_signal,
    f45of_f45_ownership_concentration_float_breadthmacd_slope_v130_signal,
    f45of_f45_ownership_concentration_float_concmr_slope_v131_signal,
    f45of_f45_ownership_concentration_float_fndshare_mr_slope_v132_signal,
    f45of_f45_ownership_concentration_float_undshare_rank_slope_v133_signal,
    f45of_f45_ownership_concentration_float_prfshare_rank_slope_v134_signal,
    f45of_f45_ownership_concentration_float_compound_slp_slope_v135_signal,
    f45of_f45_ownership_concentration_float_totval_dd504_slope_v136_signal,
    f45of_f45_ownership_concentration_float_totval_recov_slope_v137_signal,
    f45of_f45_ownership_concentration_float_smartflow_slope_v138_signal,
    f45of_f45_ownership_concentration_float_tightenrise_slope_v139_signal,
    f45of_f45_ownership_concentration_float_scissors_slope_v140_signal,
    f45of_f45_ownership_concentration_float_efftypes_lvl_slope_v141_signal,
    f45of_f45_ownership_concentration_float_conccurv_slope_v142_signal,
    f45of_f45_ownership_concentration_float_breadthcurv_slope_v143_signal,
    f45of_f45_ownership_concentration_float_fnddbtratio_slope_v144_signal,
    f45of_f45_ownership_concentration_float_prfdbtratio_slope_v145_signal,
    f45of_f45_ownership_concentration_float_tightcap_slope_v146_signal,
    f45of_f45_ownership_concentration_float_theil_slope_v147_signal,
    f45of_f45_ownership_concentration_float_concpersist_slope_v148_signal,
    f45of_f45_ownership_concentration_float_valflow_slope_v149_signal,
    f45of_f45_ownership_concentration_float_floatscore_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_OWNERSHIP_CONCENTRATION_FLOAT_REGISTRY_001_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
    g = np.random.default_rng(seed)
    n = 1500
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.5
    return pd.Series(s, name=None)


def _own(seed, base, drift, vol, nz):
    n = 1500
    g = np.random.default_rng(seed + 9000)
    s = _fund(seed, base=base, drift=drift, vol=vol).values
    s = np.abs(s * (1.0 + g.normal(0.0, nz, n)))
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    fndholders = _own(101, 60.0, 0.008, 0.11, 0.05).rename("fndholders")
    undholders = _own(102, 45.0, 0.004, 0.13, 0.06).rename("undholders")
    prfholders = _own(103, 40.0, 0.0, 0.15, 0.07).rename("prfholders")
    dbtholders = _own(104, 50.0, 0.002, 0.14, 0.06).rename("dbtholders")
    shrholders = _own(105, 160.0, 0.01, 0.09, 0.04).rename("shrholders")
    percentoftotal = _own(106, 0.12, 0.0, 0.10, 0.05).clip(lower=1e-4, upper=1.0).rename("percentoftotal")
    totalvalue = _own(107, 5e8, 0.01, 0.10, 0.04).rename("totalvalue")

    cols = {
        "fndholders": fndholders, "undholders": undholders, "prfholders": prfholders,
        "dbtholders": dbtholders, "shrholders": shrholders,
        "percentoftotal": percentoftotal, "totalvalue": totalvalue,
    }

    own_cols = ("fndholders", "undholders", "prfholders", "dbtholders",
                "shrholders", "percentoftotal", "totalvalue")

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in own_cols for c in meta["inputs"]), name
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

    print("OK f45_ownership_concentration_float_2nd_derivatives_001_150_claude: %d features pass" % n_features)
