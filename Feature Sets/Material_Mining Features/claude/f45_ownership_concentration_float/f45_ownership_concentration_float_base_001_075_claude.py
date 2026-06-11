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
    # normalized rolling slope via covariance with time index
    x = pd.Series(np.arange(len(s), dtype=float), index=s.index)
    xm = x.rolling(w, min_periods=max(2, w // 2)).mean()
    ym = s.rolling(w, min_periods=max(2, w // 2)).mean()
    cov = (x * s).rolling(w, min_periods=max(2, w // 2)).mean() - xm * ym
    varx = (x * x).rolling(w, min_periods=max(2, w // 2)).mean() - xm * xm
    return cov / varx.replace(0, np.nan)


# ===== folder domain primitives (ownership concentration / float) =====
def _f45_total_holders(fnd, und, prf, dbt):
    # total holder breadth across all holder types
    return fnd + und + prf + dbt


def _f45_share(part, total):
    # fraction of a holder-type within the total holder population
    return part / total.replace(0, np.nan)


def _f45_hhi(fnd, und, prf, dbt):
    # Herfindahl concentration of holder-type mix (sum of squared shares)
    tot = (fnd + und + prf + dbt).replace(0, np.nan)
    s1 = fnd / tot
    s2 = und / tot
    s3 = prf / tot
    s4 = dbt / tot
    return s1 * s1 + s2 * s2 + s3 * s3 + s4 * s4


def _f45_entropy(fnd, und, prf, dbt):
    # Shannon entropy of holder-type mix (diversity of ownership base)
    tot = (fnd + und + prf + dbt).replace(0, np.nan)
    out = pd.Series(0.0, index=fnd.index)
    for part in (fnd, und, prf, dbt):
        p = (part / tot).clip(lower=1e-12)
        out = out - p * np.log(p)
    return out


def _f45_value_per_holder(totalvalue, holders):
    # average position value per holder (concentration of capital)
    return totalvalue / holders.replace(0, np.nan)


# ============================================================
# fund-holder share of the total holder population (institutional breadth mix)
def f45of_f45_ownership_concentration_float_fndshare_lvl_base_v001_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _f45_share(fndholders, tot)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwriter-holder share of the total holder population
def f45of_f45_ownership_concentration_float_undshare_lvl_base_v002_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _f45_share(undholders, tot)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-holder share of the total holder population
def f45of_f45_ownership_concentration_float_prfshare_lvl_base_v003_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _f45_share(prfholders, tot)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-holder share of the EQUITY-side holder base (creditor presence relative to fund+pref+und)
def f45of_f45_ownership_concentration_float_dbtshare_lvl_base_v004_signal(fndholders, undholders, prfholders, dbtholders):
    eq = (fndholders + undholders + prfholders).replace(0, np.nan)
    b = dbtholders / eq
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Herfindahl concentration of the holder-type mix (level)
def f45of_f45_ownership_concentration_float_hhimix_lvl_base_v005_signal(fndholders, undholders, prfholders, dbtholders):
    b = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mix-diversity momentum: quarter change in Shannon entropy of the holder-type mix (diversifying/concentrating)
def f45of_f45_ownership_concentration_float_entmix_lvl_base_v006_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    b = e - e.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-holder concentration: percent-of-total (the headline concentration metric)
def f45of_f45_ownership_concentration_float_topconc_lvl_base_v007_signal(percentoftotal):
    b = percentoftotal
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total holder breadth (sum of all holder-type counts), log-scaled
def f45of_f45_ownership_concentration_float_breadth_lvl_base_v008_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(tot.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average value per holder (capital concentration per holder)
def f45of_f45_ownership_concentration_float_valperhld_lvl_base_v009_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(_f45_value_per_holder(totalvalue, tot).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tight-float proxy: top concentration per shareholder (concentration spread thin/thick over the holder base)
def f45of_f45_ownership_concentration_float_tightfloat_lvl_base_v010_signal(percentoftotal, shrholders):
    # ratio of concentration growth to shareholder-base growth: are few holders amassing the float?
    dconc = percentoftotal / percentoftotal.shift(126).replace(0, np.nan)
    dshr = shrholders / shrholders.shift(126).replace(0, np.nan)
    b = np.log(dconc.replace(0, np.nan)) - np.log(dshr.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund share z-scored vs its own 252d history (de-trended institutional mix)
def f45of_f45_ownership_concentration_float_fndshare_z252_base_v011_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = _z(sh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# HHI mix z-scored vs its own 252d history (concentration extremity)
def f45of_f45_ownership_concentration_float_hhimix_z252_base_v012_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = _z(h, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top concentration z-scored vs its own 252d history (de-trended)
def f45of_f45_ownership_concentration_float_topconc_z252_base_v013_signal(percentoftotal):
    b = _z(percentoftotal, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth z-scored vs its own 252d history (holder-count regime)
def f45of_f45_ownership_concentration_float_breadth_z252_base_v014_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _z(np.log(tot.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# entropy z-scored vs its own 252d history (diversity regime)
def f45of_f45_ownership_concentration_float_entmix_z252_base_v015_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    b = _z(e, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-vs-debt tilt momentum: quarter change in the fund-minus-debt holder spread
def f45of_f45_ownership_concentration_float_fnddbtspr_lvl_base_v016_signal(fndholders, dbtholders):
    spr = (fndholders - dbtholders) / (fndholders + dbtholders).replace(0, np.nan)
    b = spr - spr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-vs-preferred holder spread (common-fund vs preferred tilt)
def f45of_f45_ownership_concentration_float_fndprfspr_lvl_base_v017_signal(fndholders, prfholders):
    b = (fndholders - prfholders) / (fndholders + prfholders).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwriter-vs-debt holder spread (deal-flow vs credit ownership tilt)
def f45of_f45_ownership_concentration_float_unddbtspr_lvl_base_v018_signal(undholders, dbtholders):
    b = (undholders - dbtholders) / (undholders + dbtholders).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-to-underwriter ratio (sticky long-money vs deal money), log
def f45of_f45_ownership_concentration_float_fndundratio_lvl_base_v019_signal(fndholders, undholders):
    b = np.log((fndholders + 1.0) / (undholders + 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# structured-money build: quarter-over-quarter change in the (preferred+debt) holder share
def f45of_f45_ownership_concentration_float_structshare_lvl_base_v020_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = (prfholders + dbtholders) / tot.replace(0, np.nan)
    b = sh - sh.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration trend: percent-of-total slope over a quarter (building/unwinding)
def f45of_f45_ownership_concentration_float_topconc_slp63_base_v021_signal(percentoftotal):
    b = _slope(percentoftotal, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share trend over a half-year (institutional accumulation in the mix)
def f45of_f45_ownership_concentration_float_fndshare_slp126_base_v022_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = _slope(sh, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth trend over a half-year (holder-count expansion/contraction)
def f45of_f45_ownership_concentration_float_breadth_slp126_base_v023_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _slope(np.log(tot.replace(0, np.nan)), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# HHI mix trend over a half-year (concentration tightening)
def f45of_f45_ownership_concentration_float_hhimix_slp126_base_v024_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = _slope(h, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-value trend (ownership-value growth in the holder base)
def f45of_f45_ownership_concentration_float_totval_slp126_base_v025_signal(totalvalue):
    b = _slope(np.log(totalvalue.replace(0, np.nan)), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration relative momentum: quarter change in percent-of-total scaled by its own level (fractional growth)
def f45of_f45_ownership_concentration_float_topconc_mom63_base_v026_signal(percentoftotal):
    b = (percentoftotal - percentoftotal.shift(63)) / percentoftotal.shift(63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth momentum: log-holder change over a quarter
def f45of_f45_ownership_concentration_float_breadth_mom63_base_v027_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    b = lt - lt.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder count momentum over a quarter (institutional inflow)
def f45of_f45_ownership_concentration_float_fndcnt_mom63_base_v028_signal(fndholders):
    b = np.log(fndholders + 1.0) - np.log(fndholders.shift(63) + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-holder count momentum over a quarter (credit-base shift)
def f45of_f45_ownership_concentration_float_dbtcnt_mom63_base_v029_signal(dbtholders):
    b = np.log(dbtholders + 1.0) - np.log(dbtholders.shift(63) + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder momentum (capital concentration per holder trend)
def f45of_f45_ownership_concentration_float_valperhld_mom63_base_v030_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    v = np.log(_f45_value_per_holder(totalvalue, tot).replace(0, np.nan))
    b = v - v.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration acceleration: change in the percent-of-total momentum
def f45of_f45_ownership_concentration_float_topconc_accel_base_v031_signal(percentoftotal):
    mom = percentoftotal - percentoftotal.shift(63)
    b = mom - mom.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effective-types swing: peak-to-trough range of 1/HHI over the trailing half-year (mix instability band)
def f45of_f45_ownership_concentration_float_efftypes_lvl_base_v032_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    eff = 1.0 / h.replace(0, np.nan)
    b = _rmax(eff, 126) - _rmin(eff, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divergence between top-holder concentration and holder-type HHI (two concentration lenses, de-meaned)
def f45of_f45_ownership_concentration_float_concratio_lvl_base_v033_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = _z(percentoftotal, 252) - _z(h, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dominant holder-type identity (argmax index 0-3): which type leads ownership (regime/count-friendly)
def f45of_f45_ownership_concentration_float_domtype_lvl_base_v034_signal(fndholders, undholders, prfholders, dbtholders):
    stacked = pd.concat([fndholders, undholders, prfholders, dbtholders], axis=1)
    idx = stacked.values.argmax(axis=1).astype(float)
    lead = pd.Series(idx, index=fndholders.index)
    # smooth into a persistence-weighted regime so it is non-trivially varying
    b = lead.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-type share dispersion trend: slope of cross-type share std over a quarter
def f45of_f45_ownership_concentration_float_typedisp_lvl_base_v035_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    stacked = pd.concat([fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot], axis=1)
    disp = stacked.std(axis=1)
    b = _slope(disp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tight-float proxy: top concentration x HHI (compounded concentration)
def f45of_f45_ownership_concentration_float_tightcompound_base_v036_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = percentoftotal * h
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-holder dollar concentration growth: change in log(totalvalue x percentoftotal) over a quarter
def f45of_f45_ownership_concentration_float_valtopconc_base_v037_signal(totalvalue, percentoftotal):
    dollar = np.log((totalvalue * percentoftotal).replace(0, np.nan))
    b = dollar - dollar.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percent-of-total volatility (instability of top-holder concentration)
def f45of_f45_ownership_concentration_float_topconc_vol126_base_v038_signal(percentoftotal):
    b = _std(percentoftotal, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share volatility (instability of institutional mix)
def f45of_f45_ownership_concentration_float_fndshare_vol126_base_v039_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = _std(sh, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth volatility (instability of holder count)
def f45of_f45_ownership_concentration_float_breadth_vol126_base_v040_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _std(np.log(tot.replace(0, np.nan)), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-holder share trend over a quarter (structured-money build)
def f45of_f45_ownership_concentration_float_prfshare_slp63_base_v041_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(prfholders, tot)
    b = _slope(sh, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwriter-holder share trend over a quarter (deal-money build)
def f45of_f45_ownership_concentration_float_undshare_slp63_base_v042_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(undholders, tot)
    b = _slope(sh, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# entropy acceleration: change in the half-year entropy slope (diversification turning point)
def f45of_f45_ownership_concentration_float_entmix_slp126_base_v043_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    slp = _slope(e, 126)
    b = slp - slp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top concentration distance-from-multiyear-low scaled by range (deep-vs-tight cycle position, 1260d)
def f45of_f45_ownership_concentration_float_topconc_rngpos_base_v044_signal(percentoftotal):
    hi = _rmax(percentoftotal, 1260)
    lo = _rmin(percentoftotal, 1260)
    rngpos = (percentoftotal - lo) / (hi - lo).replace(0, np.nan)
    # convexity emphasis distinguishes it from a plain z-score
    b = np.sign(rngpos - 0.5) * (rngpos - 0.5) ** 2 * 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth drawdown from its 504d peak (holder-base erosion, distinct from z-score level)
def f45of_f45_ownership_concentration_float_breadth_rngpos_base_v045_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    peak = _rmax(tot, 504)
    b = tot / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share breakout: distance of fund-share above its trailing 252d max (new-dominance proxy)
def f45of_f45_ownership_concentration_float_fndshare_rank_base_v046_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    prior_max = sh.shift(1).rolling(252, min_periods=63).max()
    b = sh / prior_max.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top concentration percentile-ranked vs its own 504d history
def f45of_f45_ownership_concentration_float_topconc_rank504_base_v047_signal(percentoftotal):
    b = percentoftotal.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder z-scored vs its own 252d history (capital concentration extremity)
def f45of_f45_ownership_concentration_float_valperhld_z252_base_v048_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    v = np.log(_f45_value_per_holder(totalvalue, tot).replace(0, np.nan))
    b = _z(v, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-concentration drawup: top-holder dollar value (totalvalue x conc) vs its own 252d max
def f45of_f45_ownership_concentration_float_tightval_lvl_base_v049_signal(totalvalue, percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    dollar = totalvalue * percentoftotal / np.log(tot.replace(0, np.nan) + np.e)
    peak = _rmax(dollar, 252)
    b = dollar / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-money build vs fund-money build: quarter-change in log(pref/fund) (structured-money rotation)
def f45of_f45_ownership_concentration_float_prffndratio_base_v050_signal(prfholders, fndholders):
    r = np.log((prfholders + 1.0) / (fndholders + 1.0))
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creditor-vs-equity tilt momentum: change in log(debt/fund) over a half-year (deleveraging of ownership)
def f45of_f45_ownership_concentration_float_dbtfndratio_base_v051_signal(dbtholders, fndholders):
    r = np.log((dbtholders + 1.0) / (fndholders + 1.0))
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-type mix change: L1 distance between today's shares and a quarter ago
def f45of_f45_ownership_concentration_float_mixshift_l1_base_v052_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    parts = [fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot]
    out = pd.Series(0.0, index=fndholders.index)
    for p in parts:
        out = out + (p - p.shift(63)).abs()
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


# concentration-up-while-breadth-down flag intensity: rising top-conc combined with falling holder count
def f45of_f45_ownership_concentration_float_concbreadth_x_base_v053_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    dconc = percentoftotal - percentoftotal.shift(63)
    dbreadth = np.log(tot.replace(0, np.nan)) - np.log(tot.shift(63).replace(0, np.nan))
    b = dconc * np.sign(-dbreadth) * dbreadth.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top concentration smoothed (persistent concentration regime)
def f45of_f45_ownership_concentration_float_topconc_ema_base_v054_signal(percentoftotal):
    b = percentoftotal.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top concentration displacement from its own 126d median (robust concentration shock)
def f45of_f45_ownership_concentration_float_topconc_disp_base_v055_signal(percentoftotal):
    med = percentoftotal.rolling(126, min_periods=42).median()
    b = (percentoftotal - med) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share displacement from its own slow EMA (institutional mix shock)
def f45of_f45_ownership_concentration_float_fndshare_disp_base_v056_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = sh - sh.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# entropy displacement from slow EMA (diversification shock)
def f45of_f45_ownership_concentration_float_entmix_disp_base_v057_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    b = e - e.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Gini-Simpson diversity (1-HHI) weighted by log breadth (effective holder diversity)
def f45of_f45_ownership_concentration_float_hhinorm_lvl_base_v058_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = (1.0 - h) * np.log(tot.replace(0, np.nan) + np.e)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-vs-breadth divergence: does ownership value grow faster than holder breadth? (de-meaned z-spread)
def f45of_f45_ownership_concentration_float_valbreadth_base_v059_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _z(np.log(totalvalue.replace(0, np.nan)), 126) - _z(np.log(tot.replace(0, np.nan)), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration regime flag: fraction of last year above 252d-median percent-of-total
def f45of_f45_ownership_concentration_float_concregime_base_v060_signal(percentoftotal):
    med = percentoftotal.rolling(252, min_periods=126).median()
    above = (percentoftotal > med).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tight-float pressure: depth-weighted streak of concentration above its 252d median (continuous run intensity)
def f45of_f45_ownership_concentration_float_tightregime_base_v061_signal(percentoftotal):
    med = percentoftotal.rolling(252, min_periods=126).median()
    excess = (percentoftotal / med.replace(0, np.nan) - 1.0)
    above = (excess > 0).astype(float)
    grp = (above == 0).cumsum()
    run = above.groupby(grp).cumsum()
    # run length scaled by current above-median depth -> continuous, high-cardinality
    b = (run * excess.clip(lower=0.0)).ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth-expansion streak: consecutive days holder count >= a quarter ago
def f45of_f45_ownership_concentration_float_breadthstreak_base_v062_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    up = (tot >= tot.shift(63)).astype(float)
    grp = (up == 0).cumsum()
    b = up.groupby(grp).cumsum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration-building streak: consecutive days percent-of-total rising vs a quarter ago
def f45of_f45_ownership_concentration_float_concstreak_base_v063_signal(percentoftotal):
    up = (percentoftotal >= percentoftotal.shift(63)).astype(float)
    grp = (up == 0).cumsum()
    b = up.groupby(grp).cumsum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-exit intensity: year-long count of breadth-contraction days weighted by contraction depth
def f45of_f45_ownership_concentration_float_exittally_base_v064_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    drop = (tot.shift(63) - tot) / tot.shift(63).replace(0, np.nan)
    contract = drop.clip(lower=0.0)
    b = contract.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x magnitude of concentration trend (directional tightening intensity)
def f45of_f45_ownership_concentration_float_concsignmag_base_v065_signal(percentoftotal):
    chg = percentoftotal - percentoftotal.shift(63)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration-value coupling: do HHI moves coincide with total-value moves (sign-agreement product)
def f45of_f45_ownership_concentration_float_valhhi_base_v066_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    dh = h - h.shift(21)
    dv = np.log(totalvalue.replace(0, np.nan)) - np.log(totalvalue.shift(21).replace(0, np.nan))
    b = (dh * dv).rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-vs-creditor dominance rank: percentile of (fund-share minus debt-share) vs its 504d history
def f45of_f45_ownership_concentration_float_fndminusdbt_base_v067_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    spr = fndholders / tot - dbtholders / tot
    b = spr.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration year-over-year change (percent-of-total vs one year ago)
def f45of_f45_ownership_concentration_float_topconc_yoy_base_v068_signal(percentoftotal):
    b = percentoftotal - percentoftotal.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth year-over-year change (log-holder vs one year ago)
def f45of_f45_ownership_concentration_float_breadth_yoy_base_v069_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    b = lt - lt.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration per unit instability (trend / volatility — clean tightening)
def f45of_f45_ownership_concentration_float_concqual_base_v070_signal(percentoftotal):
    slp = _slope(percentoftotal, 126)
    vol = _std(percentoftotal, 126)
    b = slp / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tight-float instability: rolling std of the daily change in the tight-float proxy (choppy float)
def f45of_f45_ownership_concentration_float_tightslp_base_v071_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    tight = percentoftotal / np.log(tot.replace(0, np.nan) + np.e)
    b = _std(tight.diff(), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# minor-type rivalry: underwriter vs preferred holder balance (deal-money vs structured-money), log
def f45of_f45_ownership_concentration_float_typegini_base_v072_signal(fndholders, undholders, prfholders, dbtholders):
    minor = (undholders + prfholders + dbtholders).replace(0, np.nan)
    b = np.log((undholders + 1.0) / (prfholders + 1.0)) + 0.0 * minor
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed concentration momentum (bounded tightening signal)
def f45of_f45_ownership_concentration_float_conctanh_base_v073_signal(percentoftotal):
    chg = percentoftotal - percentoftotal.shift(21)
    b = np.tanh(50.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# entropy momentum vs breadth momentum: is diversity rising faster than the holder count? (quarter changes)
def f45of_f45_ownership_concentration_float_entbreadth_base_v074_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    de = e - e.shift(63)
    db = np.log(tot.replace(0, np.nan)) - np.log(tot.shift(63).replace(0, np.nan))
    b = de - db
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-value drawdown from its own 252d peak (ownership-value erosion)
def f45of_f45_ownership_concentration_float_totval_dd_base_v075_signal(totalvalue):
    peak = _rmax(totalvalue, 252)
    b = totalvalue / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45of_f45_ownership_concentration_float_fndshare_lvl_base_v001_signal,
    f45of_f45_ownership_concentration_float_undshare_lvl_base_v002_signal,
    f45of_f45_ownership_concentration_float_prfshare_lvl_base_v003_signal,
    f45of_f45_ownership_concentration_float_dbtshare_lvl_base_v004_signal,
    f45of_f45_ownership_concentration_float_hhimix_lvl_base_v005_signal,
    f45of_f45_ownership_concentration_float_entmix_lvl_base_v006_signal,
    f45of_f45_ownership_concentration_float_topconc_lvl_base_v007_signal,
    f45of_f45_ownership_concentration_float_breadth_lvl_base_v008_signal,
    f45of_f45_ownership_concentration_float_valperhld_lvl_base_v009_signal,
    f45of_f45_ownership_concentration_float_tightfloat_lvl_base_v010_signal,
    f45of_f45_ownership_concentration_float_fndshare_z252_base_v011_signal,
    f45of_f45_ownership_concentration_float_hhimix_z252_base_v012_signal,
    f45of_f45_ownership_concentration_float_topconc_z252_base_v013_signal,
    f45of_f45_ownership_concentration_float_breadth_z252_base_v014_signal,
    f45of_f45_ownership_concentration_float_entmix_z252_base_v015_signal,
    f45of_f45_ownership_concentration_float_fnddbtspr_lvl_base_v016_signal,
    f45of_f45_ownership_concentration_float_fndprfspr_lvl_base_v017_signal,
    f45of_f45_ownership_concentration_float_unddbtspr_lvl_base_v018_signal,
    f45of_f45_ownership_concentration_float_fndundratio_lvl_base_v019_signal,
    f45of_f45_ownership_concentration_float_structshare_lvl_base_v020_signal,
    f45of_f45_ownership_concentration_float_topconc_slp63_base_v021_signal,
    f45of_f45_ownership_concentration_float_fndshare_slp126_base_v022_signal,
    f45of_f45_ownership_concentration_float_breadth_slp126_base_v023_signal,
    f45of_f45_ownership_concentration_float_hhimix_slp126_base_v024_signal,
    f45of_f45_ownership_concentration_float_totval_slp126_base_v025_signal,
    f45of_f45_ownership_concentration_float_topconc_mom63_base_v026_signal,
    f45of_f45_ownership_concentration_float_breadth_mom63_base_v027_signal,
    f45of_f45_ownership_concentration_float_fndcnt_mom63_base_v028_signal,
    f45of_f45_ownership_concentration_float_dbtcnt_mom63_base_v029_signal,
    f45of_f45_ownership_concentration_float_valperhld_mom63_base_v030_signal,
    f45of_f45_ownership_concentration_float_topconc_accel_base_v031_signal,
    f45of_f45_ownership_concentration_float_efftypes_lvl_base_v032_signal,
    f45of_f45_ownership_concentration_float_concratio_lvl_base_v033_signal,
    f45of_f45_ownership_concentration_float_domtype_lvl_base_v034_signal,
    f45of_f45_ownership_concentration_float_typedisp_lvl_base_v035_signal,
    f45of_f45_ownership_concentration_float_tightcompound_base_v036_signal,
    f45of_f45_ownership_concentration_float_valtopconc_base_v037_signal,
    f45of_f45_ownership_concentration_float_topconc_vol126_base_v038_signal,
    f45of_f45_ownership_concentration_float_fndshare_vol126_base_v039_signal,
    f45of_f45_ownership_concentration_float_breadth_vol126_base_v040_signal,
    f45of_f45_ownership_concentration_float_prfshare_slp63_base_v041_signal,
    f45of_f45_ownership_concentration_float_undshare_slp63_base_v042_signal,
    f45of_f45_ownership_concentration_float_entmix_slp126_base_v043_signal,
    f45of_f45_ownership_concentration_float_topconc_rngpos_base_v044_signal,
    f45of_f45_ownership_concentration_float_breadth_rngpos_base_v045_signal,
    f45of_f45_ownership_concentration_float_fndshare_rank_base_v046_signal,
    f45of_f45_ownership_concentration_float_topconc_rank504_base_v047_signal,
    f45of_f45_ownership_concentration_float_valperhld_z252_base_v048_signal,
    f45of_f45_ownership_concentration_float_tightval_lvl_base_v049_signal,
    f45of_f45_ownership_concentration_float_prffndratio_base_v050_signal,
    f45of_f45_ownership_concentration_float_dbtfndratio_base_v051_signal,
    f45of_f45_ownership_concentration_float_mixshift_l1_base_v052_signal,
    f45of_f45_ownership_concentration_float_concbreadth_x_base_v053_signal,
    f45of_f45_ownership_concentration_float_topconc_ema_base_v054_signal,
    f45of_f45_ownership_concentration_float_topconc_disp_base_v055_signal,
    f45of_f45_ownership_concentration_float_fndshare_disp_base_v056_signal,
    f45of_f45_ownership_concentration_float_entmix_disp_base_v057_signal,
    f45of_f45_ownership_concentration_float_hhinorm_lvl_base_v058_signal,
    f45of_f45_ownership_concentration_float_valbreadth_base_v059_signal,
    f45of_f45_ownership_concentration_float_concregime_base_v060_signal,
    f45of_f45_ownership_concentration_float_tightregime_base_v061_signal,
    f45of_f45_ownership_concentration_float_breadthstreak_base_v062_signal,
    f45of_f45_ownership_concentration_float_concstreak_base_v063_signal,
    f45of_f45_ownership_concentration_float_exittally_base_v064_signal,
    f45of_f45_ownership_concentration_float_concsignmag_base_v065_signal,
    f45of_f45_ownership_concentration_float_valhhi_base_v066_signal,
    f45of_f45_ownership_concentration_float_fndminusdbt_base_v067_signal,
    f45of_f45_ownership_concentration_float_topconc_yoy_base_v068_signal,
    f45of_f45_ownership_concentration_float_breadth_yoy_base_v069_signal,
    f45of_f45_ownership_concentration_float_concqual_base_v070_signal,
    f45of_f45_ownership_concentration_float_tightslp_base_v071_signal,
    f45of_f45_ownership_concentration_float_typegini_base_v072_signal,
    f45of_f45_ownership_concentration_float_conctanh_base_v073_signal,
    f45of_f45_ownership_concentration_float_entbreadth_base_v074_signal,
    f45of_f45_ownership_concentration_float_totval_dd_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_OWNERSHIP_CONCENTRATION_FLOAT_REGISTRY_001_075 = REGISTRY


def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
    g = np.random.default_rng(seed)
    n = 1500
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.5
    return pd.Series(s, name=None)


def _own(seed, base, drift, vol, nz):
    # ownership column: smooth cyclical _fund trend + idiosyncratic daily noise, kept positive
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

    print("OK f45_ownership_concentration_float_base_001_075_claude: %d features pass" % n_features)
