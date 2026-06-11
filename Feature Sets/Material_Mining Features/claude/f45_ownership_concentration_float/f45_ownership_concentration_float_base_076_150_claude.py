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


# ============================================================
# fund-share long-horizon level smoothed over a half-year (sticky institutional mix)
def f45of_f45_ownership_concentration_float_fndshare_sm126_base_v076_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = sh.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwriter concentration vs the rest of the holder base, z-scored (deal-money footprint extremity)
def f45of_f45_ownership_concentration_float_undshare_lvl_base_v077_signal(fndholders, undholders, prfholders, dbtholders):
    rest = (fndholders + prfholders + dbtholders).replace(0, np.nan)
    ratio = undholders / rest
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-share displacement from its own 252d mean (structured-money surge)
def f45of_f45_ownership_concentration_float_prfshare_disp_base_v078_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(prfholders, tot)
    b = sh - _mean(sh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-share log-odds momentum: quarter change in the creditor log-odds (rising creditor pressure)
def f45of_f45_ownership_concentration_float_dbtshare_logodds_base_v079_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(dbtholders, tot).clip(lower=1e-6, upper=1 - 1e-6)
    lo = np.log(sh / (1.0 - sh))
    b = lo - lo.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-type HHI smoothed over a quarter (persistent concentration regime)
def f45of_f45_ownership_concentration_float_hhi_sm63_base_v080_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = h.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration cross-check: percent-of-total times holder-type HHI, smoothed (compound float tightness)
def f45of_f45_ownership_concentration_float_compound_sm_base_v081_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    raw = percentoftotal * h
    b = raw.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percent-of-total minus its 504d median (long-horizon concentration anomaly)
def f45of_f45_ownership_concentration_float_topconc_anom504_base_v082_signal(percentoftotal):
    med = percentoftotal.rolling(504, min_periods=126).median()
    b = percentoftotal - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total holder breadth in raw counts vs 504d mean (holder-base anomaly)
def f45of_f45_ownership_concentration_float_breadth_anom504_base_v083_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = tot / _mean(tot, 504).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value per FUND holder vs total value (capital concentrated in institutional hands), log
def f45of_f45_ownership_concentration_float_valperhld_anom_base_v084_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    vpf = totalvalue / fndholders.replace(0, np.nan)
    b = np.log(vpf.replace(0, np.nan)) - 0.5 * np.log(totalvalue.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# float-tightness via shareholder base: concentration times inverse-shareholder z (few-holders tightness)
def f45of_f45_ownership_concentration_float_tightfloat2_base_v085_signal(percentoftotal, shrholders):
    inv_shr = -_z(np.log(shrholders.replace(0, np.nan)), 252)
    b = _z(percentoftotal, 252) * inv_shr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share year-long trend (slope over 252d) — secular institutionalization
def f45of_f45_ownership_concentration_float_fndshare_slp252_base_v086_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = _slope(sh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top concentration year-long trend (slope over 252d)
def f45of_f45_ownership_concentration_float_topconc_slp252_base_v087_signal(percentoftotal):
    b = _slope(percentoftotal, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth year-long trend (slope over 252d of log holder count)
def f45of_f45_ownership_concentration_float_breadth_slp252_base_v088_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _slope(np.log(tot.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# HHI year-long trend (slope over 252d) — secular concentration
def f45of_f45_ownership_concentration_float_hhi_slp252_base_v089_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = _slope(h, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-value year-long trend (ownership-value secular growth)
def f45of_f45_ownership_concentration_float_totval_slp252_base_v090_signal(totalvalue):
    b = _slope(np.log(totalvalue.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder count vs its 252d max (institutional all-time-high proxy)
def f45of_f45_ownership_concentration_float_fndcnt_athgap_base_v091_signal(fndholders):
    peak = _rmax(fndholders, 252)
    b = fndholders / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-holder count vs its 252d min (creditor-base trough recovery)
def f45of_f45_ownership_concentration_float_dbtcnt_trough_base_v092_signal(dbtholders):
    trough = _rmin(dbtholders, 252)
    b = dbtholders / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-holder count momentum over a half-year (structured-money inflow)
def f45of_f45_ownership_concentration_float_prfcnt_mom126_base_v093_signal(prfholders):
    b = np.log(prfholders + 1.0) - np.log(prfholders.shift(126) + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwriter-holder count momentum over a half-year (deal-flow footprint change)
def f45of_f45_ownership_concentration_float_undcnt_mom126_base_v094_signal(undholders):
    b = np.log(undholders + 1.0) - np.log(undholders.shift(126) + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shareholder-base momentum over a half-year (broad ownership growth)
def f45of_f45_ownership_concentration_float_shrcnt_mom126_base_v095_signal(shrholders):
    b = np.log(shrholders + 1.0) - np.log(shrholders.shift(126) + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-to-shareholder ratio (institutional density of the holder base), log
def f45of_f45_ownership_concentration_float_fndshrratio_base_v096_signal(fndholders, shrholders):
    b = np.log((fndholders + 1.0) / (shrholders + 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-value per shareholder (broad ownership value density), log
def f45of_f45_ownership_concentration_float_valshr_base_v097_signal(totalvalue, shrholders):
    b = np.log(totalvalue.replace(0, np.nan)) - np.log(shrholders.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration-weighted value per shareholder (top dollars over broad base)
def f45of_f45_ownership_concentration_float_topvalshr_base_v098_signal(totalvalue, percentoftotal, shrholders):
    dollar = totalvalue * percentoftotal
    b = np.log(dollar.replace(0, np.nan)) - np.log(shrholders.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share z vs a long 504d history (de-trended secular institutional mix)
def f45of_f45_ownership_concentration_float_fndshare_z504_base_v099_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = _z(sh, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top concentration z vs a long 504d history
def f45of_f45_ownership_concentration_float_topconc_z504_base_v100_signal(percentoftotal):
    b = _z(percentoftotal, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# HHI z vs a long 504d history (secular concentration extremity)
def f45of_f45_ownership_concentration_float_hhi_z504_base_v101_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = _z(h, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth percentile-rank vs its own 1260d history (multi-year holder-count position)
def f45of_f45_ownership_concentration_float_breadth_rank1260_base_v102_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = tot.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top concentration percentile-rank vs its own 1260d history (multi-year tightness position)
def f45of_f45_ownership_concentration_float_topconc_rank1260_base_v103_signal(percentoftotal):
    b = percentoftotal.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percent-of-total volatility over a quarter (short-horizon concentration instability)
def f45of_f45_ownership_concentration_float_topconc_vol63_base_v104_signal(percentoftotal):
    b = _std(percentoftotal, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# HHI volatility over a half-year (mix-stability regime)
def f45of_f45_ownership_concentration_float_hhi_vol126_base_v105_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    b = _std(h, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# entropy volatility over a half-year (diversity-stability regime)
def f45of_f45_ownership_concentration_float_ent_vol126_base_v106_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    b = _std(e, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-value volatility (ownership-value instability), log-scale
def f45of_f45_ownership_concentration_float_totval_vol126_base_v107_signal(totalvalue):
    r = np.log(totalvalue.replace(0, np.nan)).diff()
    b = _std(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration range-width: 126d high-minus-low band of percent-of-total relative to its level
def f45of_f45_ownership_concentration_float_topconc_cov126_base_v108_signal(percentoftotal):
    hi = _rmax(percentoftotal, 126)
    lo = _rmin(percentoftotal, 126)
    b = (hi - lo) / _mean(percentoftotal, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share trend per unit of its own volatility (clean institutional drift)
def f45of_f45_ownership_concentration_float_fndshare_qual_base_v109_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = _slope(sh, 126) / _std(sh, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth trend per unit of its own volatility (clean holder-base drift)
def f45of_f45_ownership_concentration_float_breadth_qual_base_v110_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    b = _slope(lt, 126) / _std(lt, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-value momentum risk-adjusted (value inflow per unit value-vol)
def f45of_f45_ownership_concentration_float_totval_qual_base_v111_signal(totalvalue):
    r = np.log(totalvalue.replace(0, np.nan))
    mom = r - r.shift(126)
    vol = _std(r.diff(), 126) * np.sqrt(126.0)
    b = mom / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tight-float regime: fraction of last year in top tercile of percent-of-total
def f45of_f45_ownership_concentration_float_tightterc_base_v112_signal(percentoftotal):
    q = percentoftotal.rolling(252, min_periods=126).quantile(0.6667)
    tight = (percentoftotal >= q).astype(float)
    b = tight.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth-contraction regime: fraction of last year with holder count below its 252d mean
def f45of_f45_ownership_concentration_float_breadthlow_base_v113_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    below = (tot < _mean(tot, 252)).astype(float)
    b = below.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tightening-event tally weighted by concentration depth (new 126d highs over the last half-year)
def f45of_f45_ownership_concentration_float_conchitally_base_v114_signal(percentoftotal):
    roll_max = percentoftotal.shift(1).rolling(126, min_periods=42).max()
    is_new = (percentoftotal > roll_max).astype(float)
    tally = is_new.rolling(126, min_periods=42).sum()
    depth = (percentoftotal / percentoftotal.rolling(126, min_periods=42).mean().replace(0, np.nan))
    b = tally + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-exit-event tally weighted by breadth shortfall (new 126d lows over the last half-year)
def f45of_f45_ownership_concentration_float_breadthlotally_base_v115_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    roll_min = tot.shift(1).rolling(126, min_periods=42).min()
    is_new = (tot < roll_min).astype(float)
    tally = is_new.rolling(126, min_periods=42).sum()
    shortfall = (tot.rolling(126, min_periods=42).mean() / tot.replace(0, np.nan))
    b = tally + shortfall
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration-tightening streak vs a half-year ago (sustained float tightening)
def f45of_f45_ownership_concentration_float_concstreak126_base_v116_signal(percentoftotal):
    up = (percentoftotal >= percentoftotal.shift(126)).astype(float)
    grp = (up == 0).cumsum()
    b = up.groupby(grp).cumsum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-dominance streak: consecutive days fund is the largest holder type
def f45of_f45_ownership_concentration_float_fnddomstreak_base_v117_signal(fndholders, undholders, prfholders, dbtholders):
    other = pd.concat([undholders, prfholders, dbtholders], axis=1).max(axis=1)
    lead = (fndholders >= other).astype(float)
    grp = (lead == 0).cumsum()
    b = lead.groupby(grp).cumsum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x magnitude of breadth trend (directional holder-base intensity)
def f45of_f45_ownership_concentration_float_breadthsignmag_base_v118_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    chg = lt - lt.shift(63)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed breadth momentum over a month (bounded holder-flow signal)
def f45of_f45_ownership_concentration_float_breadthtanh_base_v119_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    chg = lt - lt.shift(21)
    b = np.tanh(10.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration year-over-year acceleration (yoy change of the yoy change)
def f45of_f45_ownership_concentration_float_concyoyaccel_base_v120_signal(percentoftotal):
    yoy = percentoftotal - percentoftotal.shift(252)
    b = yoy - yoy.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share interaction with concentration (institutional grip on the float)
def f45of_f45_ownership_concentration_float_fndgrip_base_v121_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    b = _z(sh, 252) + _z(percentoftotal, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-share interaction with concentration (creditor grip on the float)
def f45of_f45_ownership_concentration_float_dbtgrip_base_v122_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(dbtholders, tot)
    b = _z(sh, 252) * _z(percentoftotal, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-flow vs concentration-flow divergence (dollars moving against tightening)
def f45of_f45_ownership_concentration_float_valconc_div_base_v123_signal(totalvalue, percentoftotal):
    dv = np.log(totalvalue.replace(0, np.nan)) - np.log(totalvalue.shift(63).replace(0, np.nan))
    dc = percentoftotal - percentoftotal.shift(63)
    b = _z(dv, 252) - _z(dc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder trend over a half-year (capital concentration drift)
def f45of_f45_ownership_concentration_float_valperhld_slp_base_v124_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    v = np.log(_f45_value_per_holder(totalvalue, tot).replace(0, np.nan))
    b = _slope(v, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred+debt vs fund+underwriter holder balance (structured vs common money), log
def f45of_f45_ownership_concentration_float_structbal_base_v125_signal(fndholders, undholders, prfholders, dbtholders):
    struct = prfholders + dbtholders
    common = fndholders + undholders
    b = np.log((struct + 1.0) / (common + 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# structured-vs-common balance trend over a quarter (rotation into protective money)
def f45of_f45_ownership_concentration_float_structbal_slp_base_v126_signal(fndholders, undholders, prfholders, dbtholders):
    struct = prfholders + dbtholders
    common = fndholders + undholders
    r = np.log((struct + 1.0) / (common + 1.0))
    b = _slope(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-type mix shift over a year (L1 distance vs one year ago — slow rotation)
def f45of_f45_ownership_concentration_float_mixshift_yoy_base_v127_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    parts = [fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot]
    out = pd.Series(0.0, index=fndholders.index)
    for p in parts:
        out = out + (p - p.shift(252)).abs()
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


# entropy of the mix relative to its own 504d max (diversity drawdown)
def f45of_f45_ownership_concentration_float_ent_dd_base_v128_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    peak = _rmax(e, 504)
    b = e / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percent-of-total exponential trend acceleration (fast vs slow EMA spread)
def f45of_f45_ownership_concentration_float_concmacd_base_v129_signal(percentoftotal):
    fast = percentoftotal.ewm(span=21, min_periods=10).mean()
    slow = percentoftotal.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth exponential trend (fast vs slow EMA spread of holder count)
def f45of_f45_ownership_concentration_float_breadthmacd_base_v130_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    fast = tot.ewm(span=21, min_periods=10).mean()
    slow = tot.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration mean-reversion gap: distance from 252d median scaled by 252d inter-quartile range
def f45of_f45_ownership_concentration_float_concmr_base_v131_signal(percentoftotal):
    med = percentoftotal.rolling(252, min_periods=63).median()
    q75 = percentoftotal.rolling(252, min_periods=63).quantile(0.75)
    q25 = percentoftotal.rolling(252, min_periods=63).quantile(0.25)
    b = (percentoftotal - med) / (q75 - q25).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share mean-reversion gap: distance from 252d median scaled by 252d inter-quartile range
def f45of_f45_ownership_concentration_float_fndshare_mr_base_v132_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    med = sh.rolling(252, min_periods=63).median()
    q75 = sh.rolling(252, min_periods=63).quantile(0.75)
    q25 = sh.rolling(252, min_periods=63).quantile(0.25)
    b = (sh - med) / (q75 - q25).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwriter-share rank vs its own 252d history (deal-money footprint position)
def f45of_f45_ownership_concentration_float_undshare_rank_base_v133_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(undholders, tot)
    b = sh.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-share rank vs its own 252d history (structured-money footprint position)
def f45of_f45_ownership_concentration_float_prfshare_rank_base_v134_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(prfholders, tot)
    b = sh.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration-to-breadth product trend (compound tightness slope over a year)
def f45of_f45_ownership_concentration_float_compound_slp_base_v135_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    comp = percentoftotal * h
    b = _slope(comp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-value drawdown from 504d peak (long-horizon ownership-value erosion)
def f45of_f45_ownership_concentration_float_totval_dd504_base_v136_signal(totalvalue):
    peak = _rmax(totalvalue, 504)
    b = totalvalue / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-value recovery off 504d trough (ownership-value rebound multiple)
def f45of_f45_ownership_concentration_float_totval_recov_base_v137_signal(totalvalue):
    trough = _rmin(totalvalue, 504)
    b = totalvalue / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder share momentum interacted with value momentum (smart-money inflow signature)
def f45of_f45_ownership_concentration_float_smartflow_base_v138_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    sh = _f45_share(fndholders, tot)
    dsh = sh - sh.shift(63)
    dv = np.log(totalvalue.replace(0, np.nan)) - np.log(totalvalue.shift(63).replace(0, np.nan))
    b = np.sign(dsh) * dv.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration-on-rising-value flag intensity (tightening while value climbs)
def f45of_f45_ownership_concentration_float_tightenrise_base_v139_signal(totalvalue, percentoftotal):
    dc = percentoftotal - percentoftotal.shift(63)
    dv = np.log(totalvalue.replace(0, np.nan)) - np.log(totalvalue.shift(63).replace(0, np.nan))
    b = dc * np.sign(dv) * dv.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth-vs-concentration scissors (holders leaving while top tightens), z-spread
def f45of_f45_ownership_concentration_float_scissors_base_v140_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    b = _z(percentoftotal, 252) - _z(lt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diversity efficiency: ratio of entropy-effective-types to HHI-effective-types (mix-shape signature)
def f45of_f45_ownership_concentration_float_efftypes_lvl_base_v141_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f45_hhi(fndholders, undholders, prfholders, dbtholders)
    e = _f45_entropy(fndholders, undholders, prfholders, dbtholders)
    eff_hhi = 1.0 / h.replace(0, np.nan)
    eff_ent = np.exp(e)
    b = eff_ent / eff_hhi.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration curvature: second difference of percent-of-total over months (bend in tightening)
def f45of_f45_ownership_concentration_float_conccurv_base_v142_signal(percentoftotal):
    b = percentoftotal.shift(42) - 2.0 * percentoftotal.shift(21) + percentoftotal
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth curvature: second difference of log holder count over months
def f45of_f45_ownership_concentration_float_breadthcurv_base_v143_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    b = lt.shift(42) - 2.0 * lt.shift(21) + lt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-vs-debt holder count ratio level (equity-vs-credit ownership tilt), log
def f45of_f45_ownership_concentration_float_fnddbtratio_base_v144_signal(fndholders, dbtholders):
    b = np.log((fndholders + 1.0) / (dbtholders + 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-vs-debt holder ratio level (equity-linked vs straight-credit structured money), log
def f45of_f45_ownership_concentration_float_prfdbtratio_base_v145_signal(prfholders, dbtholders):
    b = np.log((prfholders + 1.0) / (dbtholders + 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration vs value-per-holder coupling (both-tightening composite), z-sum
def f45of_f45_ownership_concentration_float_tightcap_base_v146_signal(totalvalue, percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    vph = np.log(_f45_value_per_holder(totalvalue, tot).replace(0, np.nan))
    b = _z(percentoftotal, 252) + _z(vph, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total ownership value per unit of top concentration (dollars behind each point of concentration), log
def f45of_f45_ownership_concentration_float_theil_base_v147_signal(totalvalue, percentoftotal):
    b = np.log(totalvalue.replace(0, np.nan)) - np.log(percentoftotal.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration regime persistence: fraction of last half-year above 504d median
def f45of_f45_ownership_concentration_float_concpersist_base_v148_signal(percentoftotal):
    med = percentoftotal.rolling(504, min_periods=126).median()
    above = (percentoftotal > med).astype(float)
    b = above.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-flow into the holder base: total-value momentum minus breadth momentum (value per new holder)
def f45of_f45_ownership_concentration_float_valflow_base_v149_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    dv = np.log(totalvalue.replace(0, np.nan)) - np.log(totalvalue.shift(126).replace(0, np.nan))
    db = np.log(tot.replace(0, np.nan)) - np.log(tot.shift(126).replace(0, np.nan))
    b = dv - db
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite float-tightness score: high concentration + low breadth + rising value (z-blend)
def f45of_f45_ownership_concentration_float_floatscore_base_v150_signal(totalvalue, percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f45_total_holders(fndholders, undholders, prfholders, dbtholders)
    lt = np.log(tot.replace(0, np.nan))
    dv = np.log(totalvalue.replace(0, np.nan))
    b = _z(percentoftotal, 252) - _z(lt, 252) + 0.5 * _z(dv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45of_f45_ownership_concentration_float_fndshare_sm126_base_v076_signal,
    f45of_f45_ownership_concentration_float_undshare_lvl_base_v077_signal,
    f45of_f45_ownership_concentration_float_prfshare_disp_base_v078_signal,
    f45of_f45_ownership_concentration_float_dbtshare_logodds_base_v079_signal,
    f45of_f45_ownership_concentration_float_hhi_sm63_base_v080_signal,
    f45of_f45_ownership_concentration_float_compound_sm_base_v081_signal,
    f45of_f45_ownership_concentration_float_topconc_anom504_base_v082_signal,
    f45of_f45_ownership_concentration_float_breadth_anom504_base_v083_signal,
    f45of_f45_ownership_concentration_float_valperhld_anom_base_v084_signal,
    f45of_f45_ownership_concentration_float_tightfloat2_base_v085_signal,
    f45of_f45_ownership_concentration_float_fndshare_slp252_base_v086_signal,
    f45of_f45_ownership_concentration_float_topconc_slp252_base_v087_signal,
    f45of_f45_ownership_concentration_float_breadth_slp252_base_v088_signal,
    f45of_f45_ownership_concentration_float_hhi_slp252_base_v089_signal,
    f45of_f45_ownership_concentration_float_totval_slp252_base_v090_signal,
    f45of_f45_ownership_concentration_float_fndcnt_athgap_base_v091_signal,
    f45of_f45_ownership_concentration_float_dbtcnt_trough_base_v092_signal,
    f45of_f45_ownership_concentration_float_prfcnt_mom126_base_v093_signal,
    f45of_f45_ownership_concentration_float_undcnt_mom126_base_v094_signal,
    f45of_f45_ownership_concentration_float_shrcnt_mom126_base_v095_signal,
    f45of_f45_ownership_concentration_float_fndshrratio_base_v096_signal,
    f45of_f45_ownership_concentration_float_valshr_base_v097_signal,
    f45of_f45_ownership_concentration_float_topvalshr_base_v098_signal,
    f45of_f45_ownership_concentration_float_fndshare_z504_base_v099_signal,
    f45of_f45_ownership_concentration_float_topconc_z504_base_v100_signal,
    f45of_f45_ownership_concentration_float_hhi_z504_base_v101_signal,
    f45of_f45_ownership_concentration_float_breadth_rank1260_base_v102_signal,
    f45of_f45_ownership_concentration_float_topconc_rank1260_base_v103_signal,
    f45of_f45_ownership_concentration_float_topconc_vol63_base_v104_signal,
    f45of_f45_ownership_concentration_float_hhi_vol126_base_v105_signal,
    f45of_f45_ownership_concentration_float_ent_vol126_base_v106_signal,
    f45of_f45_ownership_concentration_float_totval_vol126_base_v107_signal,
    f45of_f45_ownership_concentration_float_topconc_cov126_base_v108_signal,
    f45of_f45_ownership_concentration_float_fndshare_qual_base_v109_signal,
    f45of_f45_ownership_concentration_float_breadth_qual_base_v110_signal,
    f45of_f45_ownership_concentration_float_totval_qual_base_v111_signal,
    f45of_f45_ownership_concentration_float_tightterc_base_v112_signal,
    f45of_f45_ownership_concentration_float_breadthlow_base_v113_signal,
    f45of_f45_ownership_concentration_float_conchitally_base_v114_signal,
    f45of_f45_ownership_concentration_float_breadthlotally_base_v115_signal,
    f45of_f45_ownership_concentration_float_concstreak126_base_v116_signal,
    f45of_f45_ownership_concentration_float_fnddomstreak_base_v117_signal,
    f45of_f45_ownership_concentration_float_breadthsignmag_base_v118_signal,
    f45of_f45_ownership_concentration_float_breadthtanh_base_v119_signal,
    f45of_f45_ownership_concentration_float_concyoyaccel_base_v120_signal,
    f45of_f45_ownership_concentration_float_fndgrip_base_v121_signal,
    f45of_f45_ownership_concentration_float_dbtgrip_base_v122_signal,
    f45of_f45_ownership_concentration_float_valconc_div_base_v123_signal,
    f45of_f45_ownership_concentration_float_valperhld_slp_base_v124_signal,
    f45of_f45_ownership_concentration_float_structbal_base_v125_signal,
    f45of_f45_ownership_concentration_float_structbal_slp_base_v126_signal,
    f45of_f45_ownership_concentration_float_mixshift_yoy_base_v127_signal,
    f45of_f45_ownership_concentration_float_ent_dd_base_v128_signal,
    f45of_f45_ownership_concentration_float_concmacd_base_v129_signal,
    f45of_f45_ownership_concentration_float_breadthmacd_base_v130_signal,
    f45of_f45_ownership_concentration_float_concmr_base_v131_signal,
    f45of_f45_ownership_concentration_float_fndshare_mr_base_v132_signal,
    f45of_f45_ownership_concentration_float_undshare_rank_base_v133_signal,
    f45of_f45_ownership_concentration_float_prfshare_rank_base_v134_signal,
    f45of_f45_ownership_concentration_float_compound_slp_base_v135_signal,
    f45of_f45_ownership_concentration_float_totval_dd504_base_v136_signal,
    f45of_f45_ownership_concentration_float_totval_recov_base_v137_signal,
    f45of_f45_ownership_concentration_float_smartflow_base_v138_signal,
    f45of_f45_ownership_concentration_float_tightenrise_base_v139_signal,
    f45of_f45_ownership_concentration_float_scissors_base_v140_signal,
    f45of_f45_ownership_concentration_float_efftypes_lvl_base_v141_signal,
    f45of_f45_ownership_concentration_float_conccurv_base_v142_signal,
    f45of_f45_ownership_concentration_float_breadthcurv_base_v143_signal,
    f45of_f45_ownership_concentration_float_fnddbtratio_base_v144_signal,
    f45of_f45_ownership_concentration_float_prfdbtratio_base_v145_signal,
    f45of_f45_ownership_concentration_float_tightcap_base_v146_signal,
    f45of_f45_ownership_concentration_float_theil_base_v147_signal,
    f45of_f45_ownership_concentration_float_concpersist_base_v148_signal,
    f45of_f45_ownership_concentration_float_valflow_base_v149_signal,
    f45of_f45_ownership_concentration_float_floatscore_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_OWNERSHIP_CONCENTRATION_FLOAT_REGISTRY_076_150 = REGISTRY


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

    print("OK f45_ownership_concentration_float_base_076_150_claude: %d features pass" % n_features)
