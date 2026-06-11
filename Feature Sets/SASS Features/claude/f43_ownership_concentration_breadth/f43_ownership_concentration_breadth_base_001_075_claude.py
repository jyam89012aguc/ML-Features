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
    def _f(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xd = x - x.mean()
        den = (xd ** 2).sum()
        if den == 0:
            return np.nan
        return float((xd * (a - a.mean())).sum() / den)
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives (ownership concentration & breadth) =====
def _f43_total_holders(fndholders, undholders, prfholders, dbtholders):
    # breadth = total holder count across all holder types
    return fndholders + undholders + prfholders + dbtholders


def _f43_share(part, fndholders, undholders, prfholders, dbtholders):
    # holder-type share = one holder-type count / total holders
    tot = fndholders + undholders + prfholders + dbtholders
    return part / tot.replace(0, np.nan)


def _f43_hhi(fndholders, undholders, prfholders, dbtholders):
    # Herfindahl across the 4 holder-type buckets (concentration of holder mix)
    tot = (fndholders + undholders + prfholders + dbtholders).replace(0, np.nan)
    sf = (fndholders / tot)
    su = (undholders / tot)
    sp = (prfholders / tot)
    sd = (dbtholders / tot)
    return sf ** 2 + su ** 2 + sp ** 2 + sd ** 2


def _f43_entropy(fndholders, undholders, prfholders, dbtholders):
    # Shannon entropy of holder-type mix (breadth of holder composition)
    tot = (fndholders + undholders + prfholders + dbtholders).replace(0, np.nan)
    out = None
    for part in (fndholders, undholders, prfholders, dbtholders):
        s = (part / tot).clip(lower=1e-12)
        term = -s * np.log(s)
        out = term if out is None else out + term
    return out


def _f43_smart_dumb(fndholders, undholders, prfholders, dbtholders):
    # smart (fund) vs dumb (underwriter+preferred+debt) holder ratio
    dumb = (undholders + prfholders + dbtholders).replace(0, np.nan)
    return fndholders / dumb


def _f43_avg_value(totalvalue, fndholders, undholders, prfholders, dbtholders):
    # average position value per holder (concentration of value over breadth)
    tot = (fndholders + undholders + prfholders + dbtholders).replace(0, np.nan)
    return totalvalue / tot


# ============================================================
# breadth: total holder count level (log), the core breadth measure
def f43oc_f43_ownership_concentration_breadth_breadth_21d_base_v001_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(tot.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth z-scored vs its own 252d history (de-trended holder breadth)
def f43oc_f43_ownership_concentration_breadth_breadthz_252d_base_v002_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _z(np.log(tot.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth momentum: log-change in total holders over a quarter (breadth expansion)
def f43oc_f43_ownership_concentration_breadth_breadthmom_63d_base_v003_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    b = np.log(tot) - np.log(tot.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder share of total holders (smart-money breadth)
def f43oc_f43_ownership_concentration_breadth_fndshare_21d_base_v004_signal(fndholders, undholders, prfholders, dbtholders):
    b = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwriter-holder share of total holders
def f43oc_f43_ownership_concentration_breadth_undshare_21d_base_v005_signal(fndholders, undholders, prfholders, dbtholders):
    b = _f43_share(undholders, fndholders, undholders, prfholders, dbtholders)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-holder share of total holders
def f43oc_f43_ownership_concentration_breadth_prfshare_21d_base_v006_signal(fndholders, undholders, prfholders, dbtholders):
    b = _f43_share(prfholders, fndholders, undholders, prfholders, dbtholders)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-holder share of total holders
def f43oc_f43_ownership_concentration_breadth_dbtshare_21d_base_v007_signal(fndholders, undholders, prfholders, dbtholders):
    b = _f43_share(dbtholders, fndholders, undholders, prfholders, dbtholders)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-mix HHI: concentration of the holder-type composition
def f43oc_f43_ownership_concentration_breadth_mixhhi_21d_base_v008_signal(fndholders, undholders, prfholders, dbtholders):
    b = _f43_hhi(fndholders, undholders, prfholders, dbtholders)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-mix Shannon entropy: breadth/diversity of the holder composition
def f43oc_f43_ownership_concentration_breadth_mixentropy_21d_base_v009_signal(fndholders, undholders, prfholders, dbtholders):
    b = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-holder concentration level: percentoftotal held by the single largest holder
def f43oc_f43_ownership_concentration_breadth_topconc_21d_base_v010_signal(percentoftotal):
    b = percentoftotal
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-holder concentration z-scored vs its own 252d history (de-trended)
def f43oc_f43_ownership_concentration_breadth_topconcz_252d_base_v011_signal(percentoftotal):
    b = _z(percentoftotal, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-holder concentration trend: change in percentoftotal over a quarter
def f43oc_f43_ownership_concentration_breadth_topconctrd_63d_base_v012_signal(percentoftotal):
    b = percentoftotal - percentoftotal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-money entropy share: fund's normalized contribution to total mix entropy
def f43oc_f43_ownership_concentration_breadth_smartdumb_21d_base_v013_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sf = (fndholders / tot).clip(lower=1e-12)
    fnd_ent = -sf * np.log(sf)
    b = fnd_ent / e.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-vs-dumb ratio log-trend over a quarter (smart-money rotation in)
def f43oc_f43_ownership_concentration_breadth_smartdumbmom_63d_base_v014_signal(fndholders, undholders, prfholders, dbtholders):
    r = _f43_smart_dumb(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    b = np.log(r) - np.log(r.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average value per holder (value concentration over holder breadth), logged
def f43oc_f43_ownership_concentration_breadth_avgval_21d_base_v015_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    av = _f43_avg_value(totalvalue, fndholders, undholders, prfholders, dbtholders)
    b = np.log(av.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value concentration: totalvalue x top-holder percentoftotal (dollar concentration proxy)
def f43oc_f43_ownership_concentration_breadth_valconc_21d_base_v016_signal(totalvalue, percentoftotal):
    b = np.log((totalvalue * percentoftotal).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share acceleration: second difference of fund share over monthly steps (rotation impulse)
def f43oc_f43_ownership_concentration_breadth_fndsharemom_63d_base_v017_signal(fndholders, undholders, prfholders, dbtholders):
    sh = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    d1 = sh - sh.shift(21)
    b = d1 - d1.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-share momentum: change in debt-holder share over a quarter (creditor rotation)
def f43oc_f43_ownership_concentration_breadth_dbtsharemom_63d_base_v018_signal(fndholders, undholders, prfholders, dbtholders):
    sh = _f43_share(dbtholders, fndholders, undholders, prfholders, dbtholders)
    b = sh - sh.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-mix HHI trend: change in mix concentration over a quarter
def f43oc_f43_ownership_concentration_breadth_hhitrd_63d_base_v019_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f43_hhi(fndholders, undholders, prfholders, dbtholders)
    b = h - h.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-mix entropy trend: change in mix diversity over a quarter
def f43oc_f43_ownership_concentration_breadth_entropytrd_63d_base_v020_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    b = e - e.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder count level (log), the smart-money breadth count
def f43oc_f43_ownership_concentration_breadth_fndcount_21d_base_v021_signal(fndholders):
    b = np.log(fndholders.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder count momentum over a quarter (smart-money breadth expansion)
def f43oc_f43_ownership_concentration_breadth_fndcountmom_63d_base_v022_signal(fndholders):
    f = fndholders.replace(0, np.nan)
    b = np.log(f) - np.log(f.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-holder count z-scored vs its own 252d history (creditor crowding)
def f43oc_f43_ownership_concentration_breadth_dbtcountz_252d_base_v023_signal(dbtholders):
    b = _z(np.log(dbtholders.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# non-top holder base growth: log change in implied (1-pct)*total holders over a quarter
def f43oc_f43_ownership_concentration_breadth_concbreadth_21d_base_v024_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    nontop = (tot * (1.0 - percentoftotal).clip(lower=0)).replace(0, np.nan)
    b = np.log(nontop).diff(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration paradox: top-conc rank minus mix-entropy rank (concentrated yet diverse-typed)
def f43oc_f43_ownership_concentration_breadth_concperbreadth_21d_base_v025_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    e = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    cr = percentoftotal.rolling(252, min_periods=84).rank(pct=True)
    er = e.rolling(252, min_periods=84).rank(pct=True)
    b = cr - er
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-to-debt holder ratio (equity-conviction vs creditor presence)
def f43oc_f43_ownership_concentration_breadth_fnddbt_21d_base_v026_signal(fndholders, dbtholders):
    b = np.log(fndholders.replace(0, np.nan) / dbtholders.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-to-preferred holder ratio (common-equity vs preferred presence)
def f43oc_f43_ownership_concentration_breadth_fndprf_21d_base_v027_signal(fndholders, prfholders):
    b = np.log(fndholders.replace(0, np.nan) / prfholders.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwriter-to-fund holder ratio (placement vs organic ownership)
def f43oc_f43_ownership_concentration_breadth_undfnd_21d_base_v028_signal(undholders, fndholders):
    b = np.log(undholders.replace(0, np.nan) / fndholders.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value per fund holder (conviction value behind each smart holder), logged
def f43oc_f43_ownership_concentration_breadth_valperfnd_21d_base_v029_signal(totalvalue, fndholders):
    b = np.log((totalvalue / fndholders.replace(0, np.nan)).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# totalvalue momentum (ownership-value growth) over a quarter
def f43oc_f43_ownership_concentration_breadth_valmom_63d_base_v030_signal(totalvalue):
    v = totalvalue.replace(0, np.nan)
    b = np.log(v) - np.log(v.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth-adjusted value growth: value growth minus breadth growth (value per holder drift)
def f43oc_f43_ownership_concentration_breadth_valbreadthspr_63d_base_v031_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    v = totalvalue.replace(0, np.nan)
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    vg = np.log(v) - np.log(v.shift(63))
    bg = np.log(tot) - np.log(tot.shift(63))
    b = vg - bg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt+preferred (income) holder count vs fund+underwriter (equity) holder count, log ratio
def f43oc_f43_ownership_concentration_breadth_efftypes_21d_base_v032_signal(fndholders, undholders, prfholders, dbtholders):
    income = (prfholders + dbtholders).replace(0, np.nan)
    equity = (fndholders + undholders).replace(0, np.nan)
    b = np.log(income / equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share dominance gap: fund-share minus the next largest holder-type share
def f43oc_f43_ownership_concentration_breadth_fnddomgap_21d_base_v033_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sf = fndholders / tot
    others = pd.concat([undholders / tot, prfholders / tot, dbtholders / tot], axis=1).max(axis=1)
    b = sf - others
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-mix range: max holder-type share minus min holder-type share (dominance spread)
def f43oc_f43_ownership_concentration_breadth_mixdisp_21d_base_v034_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    shares = pd.concat([fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot], axis=1)
    rng = shares.max(axis=1) - shares.min(axis=1)
    b = rng - _mean(rng, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-concentration acceleration-as-level: percentoftotal minus its 63d mean (excess concentration)
def f43oc_f43_ownership_concentration_breadth_concexcess_63d_base_v035_signal(percentoftotal):
    b = percentoftotal - _mean(percentoftotal, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-concentration percentile-ranked vs its own 504d history
def f43oc_f43_ownership_concentration_breadth_concrank_504d_base_v036_signal(percentoftotal):
    b = percentoftotal.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration risk per dollar: co-movement of concentration changes with value changes
def f43oc_f43_ownership_concentration_breadth_concrisk_21d_base_v037_signal(percentoftotal, totalvalue):
    cc = percentoftotal.diff()
    vv = np.log(totalvalue.replace(0, np.nan)).diff()
    b = cc.rolling(126, min_periods=42).corr(vv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-money breadth share: fund holders as share of total, z-scored over 126d
def f43oc_f43_ownership_concentration_breadth_fndsharez_126d_base_v038_signal(fndholders, undholders, prfholders, dbtholders):
    sh = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    b = _z(sh, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred+debt (income holders) combined share vs fund share (income vs growth tilt)
def f43oc_f43_ownership_concentration_breadth_incomeshare_21d_base_v039_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    income = (prfholders + dbtholders) / tot
    growth = fndholders / tot
    b = income - growth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-type rotation magnitude: total absolute change in shares over a quarter
def f43oc_f43_ownership_concentration_breadth_rotmag_63d_base_v040_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    out = None
    for part in (fndholders, undholders, prfholders, dbtholders):
        s = part / tot
        d = (s - s.shift(63)).abs()
        out = d if out is None else out + d
    b = out
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth-vs-concentration regime spread: breadth z-score minus concentration z-score
def f43oc_f43_ownership_concentration_breadth_breadthconc_21d_base_v041_signal(fndholders, undholders, prfholders, dbtholders, percentoftotal):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _z(np.log(tot.replace(0, np.nan)), 126) - _z(percentoftotal, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-driven breadth: share of 63d net holder additions that came from fund holders
def f43oc_f43_ownership_concentration_breadth_fndbreadthz_252d_base_v042_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    dfnd = fndholders - fndholders.shift(63)
    dtot = (tot - tot.shift(63))
    b = dfnd / dtot.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-weighted concentration: percentoftotal squared (convex concentration penalty)
def f43oc_f43_ownership_concentration_breadth_concconvex_21d_base_v043_signal(percentoftotal):
    b = np.sign(percentoftotal - _mean(percentoftotal, 63)) * (percentoftotal ** 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth stability: inverse coefficient of variation of total holders over 126d
def f43oc_f43_ownership_concentration_breadth_breadthstab_126d_base_v044_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    m = _mean(tot, 126)
    sd = _std(tot, 126)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration stability: rolling std of percentoftotal over 126d (concentration churn)
def f43oc_f43_ownership_concentration_breadth_concchurn_126d_base_v045_signal(percentoftotal):
    b = _std(percentoftotal, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share entropy contribution: fund-share x -log(fund-share) (smart-money diversity weight)
def f43oc_f43_ownership_concentration_breadth_fndentcontrib_21d_base_v046_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sf = (fndholders / tot).clip(lower=1e-12)
    b = -sf * np.log(sf)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# avg value per holder z-scored vs 252d (value concentration regime)
def f43oc_f43_ownership_concentration_breadth_avgvalz_252d_base_v047_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    av = _f43_avg_value(totalvalue, fndholders, undholders, prfholders, dbtholders)
    b = _z(np.log(av.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-holder concentration vs average holder weight (1/total): dominance over equal-weight
def f43oc_f43_ownership_concentration_breadth_topvsequal_21d_base_v048_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    equal = 1.0 / tot.replace(0, np.nan)
    b = percentoftotal / equal.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-holder share momentum minus fund-holder share momentum (creditor-vs-equity rotation)
def f43oc_f43_ownership_concentration_breadth_credeqrot_63d_base_v049_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sd = dbtholders / tot
    sf = fndholders / tot
    b = (sd - sd.shift(63)) - (sf - sf.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth growth dispersion: rolling std of daily log-breadth changes (breadth turnover)
def f43oc_f43_ownership_concentration_breadth_breadthexcess_252d_base_v050_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    chg = np.log(tot.replace(0, np.nan)).diff()
    b = _std(chg, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-breadth z-score: detrended log effective non-top breadth vs its own 252d history
def f43oc_f43_ownership_concentration_breadth_freebreadth_21d_base_v051_signal(fndholders, undholders, prfholders, dbtholders, percentoftotal):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    fb = np.log((tot * (1.0 - percentoftotal).clip(lower=0)).replace(0, np.nan))
    b = _z(fb, 252) - _z(np.log(tot.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share rank vs cross-time history (percentile of smart-money tilt)
def f43oc_f43_ownership_concentration_breadth_fndsharerank_504d_base_v052_signal(fndholders, undholders, prfholders, dbtholders):
    sh = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    b = sh.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-mix entropy z-scored vs 252d (diversity regime)
def f43oc_f43_ownership_concentration_breadth_entropyz_252d_base_v053_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    b = _z(e, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-share level (income-holder breadth slice)
def f43oc_f43_ownership_concentration_breadth_prfshare2_126d_base_v054_signal(fndholders, undholders, prfholders, dbtholders):
    sh = _f43_share(prfholders, fndholders, undholders, prfholders, dbtholders)
    b = _z(sh, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar concentration trend: 63d change in (value-per-holder growth minus concentration growth)
def f43oc_f43_ownership_concentration_breadth_concdollar_21d_base_v055_signal(totalvalue, percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    av = (totalvalue / tot).replace(0, np.nan)
    avg = np.log(av).diff(63)
    cg = np.log(percentoftotal.replace(0, np.nan)).diff(63)
    b = avg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth tanh momentum: bounded log-change in total holders over a month
def f43oc_f43_ownership_concentration_breadth_breadthtanh_21d_base_v056_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    chg = np.log(tot) - np.log(tot.shift(21))
    b = np.tanh(8.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-dumb ratio z-scored vs 252d (smart-money tilt regime)
def f43oc_f43_ownership_concentration_breadth_smartdumbz_252d_base_v057_signal(fndholders, undholders, prfholders, dbtholders):
    r = _f43_smart_dumb(fndholders, undholders, prfholders, dbtholders)
    b = _z(np.log(r.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration-trend asymmetry: positive vs negative percentoftotal changes over 126d
def f43oc_f43_ownership_concentration_breadth_concasym_126d_base_v058_signal(percentoftotal):
    d = percentoftotal.diff()
    up = d.clip(lower=0).rolling(126, min_periods=42).sum()
    dn = (-d.clip(upper=0)).rolling(126, min_periods=42).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth hit-rate: fraction of last quarter total holders rose (steady accumulation breadth)
def f43oc_f43_ownership_concentration_breadth_breadthhit_63d_base_v059_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    up = (tot.diff() > 0).astype(float)
    hit = up.rolling(63, min_periods=21).mean() - 0.5
    mag = (tot.pct_change()).rolling(63, min_periods=21).mean()
    b = hit + 5.0 * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-vs-debt income-holder balance share (which income class dominates the base)
def f43oc_f43_ownership_concentration_breadth_orgplace_21d_base_v060_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    b = (prfholders - dbtholders) / tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration vs breadth rolling correlation (do top holders crowd as breadth shrinks?)
def f43oc_f43_ownership_concentration_breadth_concrevert_252d_base_v061_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    cc = percentoftotal.diff()
    bb = np.log(tot.replace(0, np.nan)).diff()
    b = cc.rolling(252, min_periods=84).corr(bb)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mix-diversification volatility: rolling std of entropy (instability of holder composition)
def f43oc_f43_ownership_concentration_breadth_efftypestrd_63d_base_v062_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    b = _std(e, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-vs-concentration regime spread: value z-score minus concentration z-score
def f43oc_f43_ownership_concentration_breadth_valdilution_21d_base_v063_signal(totalvalue, percentoftotal):
    b = _z(np.log(totalvalue.replace(0, np.nan)), 252) - _z(percentoftotal, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-holder count momentum (creditor-base expansion over a quarter)
def f43oc_f43_ownership_concentration_breadth_dbtcountmom_63d_base_v064_signal(dbtholders):
    d = dbtholders.replace(0, np.nan)
    b = np.log(d) - np.log(d.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-holder count momentum (preferred-base expansion over a quarter)
def f43oc_f43_ownership_concentration_breadth_prfcountmom_63d_base_v065_signal(prfholders):
    p = prfholders.replace(0, np.nan)
    b = np.log(p) - np.log(p.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwriter-holder count z vs 252d (placement-base regime)
def f43oc_f43_ownership_concentration_breadth_undcountz_252d_base_v066_signal(undholders):
    b = _z(np.log(undholders.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-weighted breadth: totalvalue x log total holders (size of broad ownership)
def f43oc_f43_ownership_concentration_breadth_valbreadth_21d_base_v067_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(totalvalue.replace(0, np.nan)) + np.log(tot.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# crowding flag persistence: fraction of last quarter with rising conc AND falling breadth
def f43oc_f43_ownership_concentration_breadth_crowddiv_63d_base_v068_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    conc_up = (percentoftotal.diff(21) > 0)
    breadth_dn = (np.log(tot).diff(21) < 0)
    crowd = (conc_up & breadth_dn).astype(float)
    freq = crowd.rolling(63, min_periods=21).mean() - 0.5
    intensity = (percentoftotal.diff(21) - np.log(tot).diff(21)).rolling(63, min_periods=21).mean()
    b = freq + 3.0 * intensity
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share Shannon weight relative to debt-share weight (smart vs creditor diversity)
def f43oc_f43_ownership_concentration_breadth_fnddbtent_21d_base_v069_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sf = (fndholders / tot).clip(lower=1e-12)
    sd = (dbtholders / tot).clip(lower=1e-12)
    b = (-sf * np.log(sf)) - (-sd * np.log(sd))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth slope (regression slope of log total holders over 126d)
def f43oc_f43_ownership_concentration_breadth_breadthslope_126d_base_v070_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _slope(np.log(tot.replace(0, np.nan)), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration slope (regression slope of percentoftotal over 126d)
def f43oc_f43_ownership_concentration_breadth_concslope_126d_base_v071_signal(percentoftotal):
    b = _slope(percentoftotal, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-mix HHI percentile-ranked vs 504d history (concentration regime rank)
def f43oc_f43_ownership_concentration_breadth_hhirank_504d_base_v072_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f43_hhi(fndholders, undholders, prfholders, dbtholders)
    b = h.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-fund-holder trend over a quarter (conviction dollars per smart holder)
def f43oc_f43_ownership_concentration_breadth_valperfndmom_63d_base_v073_signal(totalvalue, fndholders):
    v = (totalvalue / fndholders.replace(0, np.nan)).replace(0, np.nan)
    b = np.log(v) - np.log(v.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-money breadth divergence: fund-count growth minus top-concentration growth (63d)
def f43oc_f43_ownership_concentration_breadth_smartfree_21d_base_v074_signal(fndholders, undholders, prfholders, dbtholders, percentoftotal):
    fg = np.log(fndholders.replace(0, np.nan)).diff(63)
    cg = np.log(percentoftotal.replace(0, np.nan)).diff(63)
    b = fg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-type rotation dispersion: cross-sectional std of 63d share changes (rotation breadth)
def f43oc_f43_ownership_concentration_breadth_fndtilt_63d_base_v075_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sf = fndholders / tot
    su = undholders / tot
    sp = prfholders / tot
    sd = dbtholders / tot
    chg = pd.concat([sf - sf.shift(63), su - su.shift(63), sp - sp.shift(63), sd - sd.shift(63)], axis=1)
    b = chg.std(axis=1) * np.sign(sf - sf.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43oc_f43_ownership_concentration_breadth_breadth_21d_base_v001_signal,
    f43oc_f43_ownership_concentration_breadth_breadthz_252d_base_v002_signal,
    f43oc_f43_ownership_concentration_breadth_breadthmom_63d_base_v003_signal,
    f43oc_f43_ownership_concentration_breadth_fndshare_21d_base_v004_signal,
    f43oc_f43_ownership_concentration_breadth_undshare_21d_base_v005_signal,
    f43oc_f43_ownership_concentration_breadth_prfshare_21d_base_v006_signal,
    f43oc_f43_ownership_concentration_breadth_dbtshare_21d_base_v007_signal,
    f43oc_f43_ownership_concentration_breadth_mixhhi_21d_base_v008_signal,
    f43oc_f43_ownership_concentration_breadth_mixentropy_21d_base_v009_signal,
    f43oc_f43_ownership_concentration_breadth_topconc_21d_base_v010_signal,
    f43oc_f43_ownership_concentration_breadth_topconcz_252d_base_v011_signal,
    f43oc_f43_ownership_concentration_breadth_topconctrd_63d_base_v012_signal,
    f43oc_f43_ownership_concentration_breadth_smartdumb_21d_base_v013_signal,
    f43oc_f43_ownership_concentration_breadth_smartdumbmom_63d_base_v014_signal,
    f43oc_f43_ownership_concentration_breadth_avgval_21d_base_v015_signal,
    f43oc_f43_ownership_concentration_breadth_valconc_21d_base_v016_signal,
    f43oc_f43_ownership_concentration_breadth_fndsharemom_63d_base_v017_signal,
    f43oc_f43_ownership_concentration_breadth_dbtsharemom_63d_base_v018_signal,
    f43oc_f43_ownership_concentration_breadth_hhitrd_63d_base_v019_signal,
    f43oc_f43_ownership_concentration_breadth_entropytrd_63d_base_v020_signal,
    f43oc_f43_ownership_concentration_breadth_fndcount_21d_base_v021_signal,
    f43oc_f43_ownership_concentration_breadth_fndcountmom_63d_base_v022_signal,
    f43oc_f43_ownership_concentration_breadth_dbtcountz_252d_base_v023_signal,
    f43oc_f43_ownership_concentration_breadth_concbreadth_21d_base_v024_signal,
    f43oc_f43_ownership_concentration_breadth_concperbreadth_21d_base_v025_signal,
    f43oc_f43_ownership_concentration_breadth_fnddbt_21d_base_v026_signal,
    f43oc_f43_ownership_concentration_breadth_fndprf_21d_base_v027_signal,
    f43oc_f43_ownership_concentration_breadth_undfnd_21d_base_v028_signal,
    f43oc_f43_ownership_concentration_breadth_valperfnd_21d_base_v029_signal,
    f43oc_f43_ownership_concentration_breadth_valmom_63d_base_v030_signal,
    f43oc_f43_ownership_concentration_breadth_valbreadthspr_63d_base_v031_signal,
    f43oc_f43_ownership_concentration_breadth_efftypes_21d_base_v032_signal,
    f43oc_f43_ownership_concentration_breadth_fnddomgap_21d_base_v033_signal,
    f43oc_f43_ownership_concentration_breadth_mixdisp_21d_base_v034_signal,
    f43oc_f43_ownership_concentration_breadth_concexcess_63d_base_v035_signal,
    f43oc_f43_ownership_concentration_breadth_concrank_504d_base_v036_signal,
    f43oc_f43_ownership_concentration_breadth_concrisk_21d_base_v037_signal,
    f43oc_f43_ownership_concentration_breadth_fndsharez_126d_base_v038_signal,
    f43oc_f43_ownership_concentration_breadth_incomeshare_21d_base_v039_signal,
    f43oc_f43_ownership_concentration_breadth_rotmag_63d_base_v040_signal,
    f43oc_f43_ownership_concentration_breadth_breadthconc_21d_base_v041_signal,
    f43oc_f43_ownership_concentration_breadth_fndbreadthz_252d_base_v042_signal,
    f43oc_f43_ownership_concentration_breadth_concconvex_21d_base_v043_signal,
    f43oc_f43_ownership_concentration_breadth_breadthstab_126d_base_v044_signal,
    f43oc_f43_ownership_concentration_breadth_concchurn_126d_base_v045_signal,
    f43oc_f43_ownership_concentration_breadth_fndentcontrib_21d_base_v046_signal,
    f43oc_f43_ownership_concentration_breadth_avgvalz_252d_base_v047_signal,
    f43oc_f43_ownership_concentration_breadth_topvsequal_21d_base_v048_signal,
    f43oc_f43_ownership_concentration_breadth_credeqrot_63d_base_v049_signal,
    f43oc_f43_ownership_concentration_breadth_breadthexcess_252d_base_v050_signal,
    f43oc_f43_ownership_concentration_breadth_freebreadth_21d_base_v051_signal,
    f43oc_f43_ownership_concentration_breadth_fndsharerank_504d_base_v052_signal,
    f43oc_f43_ownership_concentration_breadth_entropyz_252d_base_v053_signal,
    f43oc_f43_ownership_concentration_breadth_prfshare2_126d_base_v054_signal,
    f43oc_f43_ownership_concentration_breadth_concdollar_21d_base_v055_signal,
    f43oc_f43_ownership_concentration_breadth_breadthtanh_21d_base_v056_signal,
    f43oc_f43_ownership_concentration_breadth_smartdumbz_252d_base_v057_signal,
    f43oc_f43_ownership_concentration_breadth_concasym_126d_base_v058_signal,
    f43oc_f43_ownership_concentration_breadth_breadthhit_63d_base_v059_signal,
    f43oc_f43_ownership_concentration_breadth_orgplace_21d_base_v060_signal,
    f43oc_f43_ownership_concentration_breadth_concrevert_252d_base_v061_signal,
    f43oc_f43_ownership_concentration_breadth_efftypestrd_63d_base_v062_signal,
    f43oc_f43_ownership_concentration_breadth_valdilution_21d_base_v063_signal,
    f43oc_f43_ownership_concentration_breadth_dbtcountmom_63d_base_v064_signal,
    f43oc_f43_ownership_concentration_breadth_prfcountmom_63d_base_v065_signal,
    f43oc_f43_ownership_concentration_breadth_undcountz_252d_base_v066_signal,
    f43oc_f43_ownership_concentration_breadth_valbreadth_21d_base_v067_signal,
    f43oc_f43_ownership_concentration_breadth_crowddiv_63d_base_v068_signal,
    f43oc_f43_ownership_concentration_breadth_fnddbtent_21d_base_v069_signal,
    f43oc_f43_ownership_concentration_breadth_breadthslope_126d_base_v070_signal,
    f43oc_f43_ownership_concentration_breadth_concslope_126d_base_v071_signal,
    f43oc_f43_ownership_concentration_breadth_hhirank_504d_base_v072_signal,
    f43oc_f43_ownership_concentration_breadth_valperfndmom_63d_base_v073_signal,
    f43oc_f43_ownership_concentration_breadth_smartfree_21d_base_v074_signal,
    f43oc_f43_ownership_concentration_breadth_fndtilt_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_OWNERSHIP_CONCENTRATION_BREADTH_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.3
        return pd.Series(s, name=None)

    def _jit(seed, sd):
        # AR(1) idiosyncratic daily noise (persistent jitter), de-correlated per column
        g = np.random.default_rng(seed)
        e = g.normal(0.0, sd, n)
        out = np.empty(n)
        acc = 0.0
        for k in range(n):
            acc = 0.85 * acc + e[k]
            out[k] = acc
        return np.exp(out)

    fndholders = (_fund(101, base=120.0, drift=0.018, vol=0.07).values * _jit(201, 0.045))
    fndholders = pd.Series(np.maximum(fndholders, 1.0), name="fndholders")
    undholders = (_fund(102, base=85.0, drift=-0.004, vol=0.08).values * _jit(202, 0.060))
    undholders = pd.Series(np.maximum(undholders, 1.0), name="undholders")
    prfholders = (_fund(103, base=70.0, drift=0.002, vol=0.09).values * _jit(203, 0.070))
    prfholders = pd.Series(np.maximum(prfholders, 1.0), name="prfholders")
    dbtholders = (_fund(104, base=95.0, drift=-0.001, vol=0.075).values * _jit(204, 0.055))
    dbtholders = pd.Series(np.maximum(dbtholders, 1.0), name="dbtholders")
    shrholders = (_fund(105, base=300.0, drift=0.012, vol=0.06).values * _jit(205, 0.030))
    shrholders = pd.Series(np.maximum(shrholders, 1.0), name="shrholders")
    percentoftotal = (_fund(106, base=0.18, drift=0.003, vol=0.05).values * _jit(206, 0.040))
    percentoftotal = pd.Series(np.clip(percentoftotal, 0.001, 0.95), name="percentoftotal")
    totalvalue = (_fund(107, base=5e8, drift=0.018, vol=0.05).values * _jit(207, 0.035))
    totalvalue = pd.Series(np.maximum(totalvalue, 1.0), name="totalvalue")

    cols = {
        "fndholders": fndholders, "undholders": undholders, "prfholders": prfholders,
        "dbtholders": dbtholders, "shrholders": shrholders,
        "percentoftotal": percentoftotal, "totalvalue": totalvalue,
    }

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

    print("OK f43_ownership_concentration_breadth_base_001_075_claude: %d features pass" % n_features)
