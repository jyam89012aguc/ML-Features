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


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


# ===== family ownership-mix primitives =====
def _f51_share(num, den):
    return num / den.replace(0, np.nan)


def _f51_skew(put, cll):
    return put / (put + cll).replace(0, np.nan)


def _f51_growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f51_roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f51_logratio(a, b):
    return np.log(a.replace(0, np.nan) / b.replace(0, np.nan))


def _f51_herf(a, b, c):
    tot = (a + b + c).replace(0, np.nan)
    sa = a / tot
    sb = b / tot
    sc = c / tot
    return sa * sa + sb * sb + sc * sc


# ============================================================
# --- fund value share: longer-window and cross-window facets ---
# fund value share, percentile-ranked vs 504d history (long-run institutional positioning)
def f51om_f51_ownership_mix_concentration_fndshare_rank504_base_v076_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund value share cross-window spread: 63d mean minus 252d mean (fast vs slow tilt)
def f51om_f51_ownership_mix_concentration_fndshare_spr_base_v077_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    b = s.rolling(63, min_periods=21).mean() - s.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund value share half-year momentum (126d change)
def f51om_f51_ownership_mix_concentration_fndshare_chg126_base_v078_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    b = s - s.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund value share acceleration: 63d change now vs 63d change one quarter ago
def f51om_f51_ownership_mix_concentration_fndshare_accel_base_v079_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    c = s - s.shift(63)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund value share signed strength: sign of QoQ change x sqrt magnitude
def f51om_f51_ownership_mix_concentration_fndshare_signmag_base_v080_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    c = s - s.shift(63)
    b = np.sign(c) * np.sqrt(c.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- retail/other value share facets ---
# retail/other share half-year momentum
def f51om_f51_ownership_mix_concentration_undshare_chg126_base_v081_signal(undvalue, totalvalue):
    s = _f51_share(undvalue, totalvalue)
    b = s - s.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retail/other share dispersion over a quarter (instability of retail crowding)
def f51om_f51_ownership_mix_concentration_undshare_disp63_base_v082_signal(undvalue, totalvalue):
    s = _f51_share(undvalue, totalvalue)
    b = _std(s, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retail/other share displacement from slow EMA
def f51om_f51_ownership_mix_concentration_undshare_disp_base_v083_signal(undvalue, totalvalue):
    s = _f51_share(undvalue, totalvalue)
    b = s - s.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retail-vs-fund value log ratio, half-year change (slow rotation)
def f51om_f51_ownership_mix_concentration_undfnd_logrchg126_base_v084_signal(undvalue, fndvalue):
    r = _f51_logratio(undvalue, fndvalue)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- put-vs-call value skew: longer-window facets ---
# put-value skew, percentile-ranked vs 504d history (long-run hedging positioning)
def f51om_f51_ownership_mix_concentration_putskew_rank504_base_v085_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-value skew half-year momentum
def f51om_f51_ownership_mix_concentration_putskew_chg126_base_v086_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    b = s - s.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-value skew acceleration (change in QoQ hedging build)
def f51om_f51_ownership_mix_concentration_putskew_accel_base_v087_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    c = s - s.shift(63)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-value skew cross-window spread: 21d mean minus 126d mean (fast hedging shift)
def f51om_f51_ownership_mix_concentration_putskew_spr_base_v088_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    b = s.rolling(21, min_periods=10).mean() - s.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-value skew signed strength of QoQ change
def f51om_f51_ownership_mix_concentration_putskew_signmag_base_v089_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    c = s - s.shift(63)
    b = np.sign(c) * np.sqrt(c.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- put/call value and breadth growth facets ---
# put VALUE log growth over a quarter (hedge value building, raw)
def f51om_f51_ownership_mix_concentration_putval_grow63_base_v090_signal(putvalue, totalvalue):
    b = _f51_growth(putvalue, 63) - _f51_growth(totalvalue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call VALUE log growth over a quarter, net of ownership value growth (bullish value building)
def f51om_f51_ownership_mix_concentration_cllval_grow63_base_v091_signal(cllvalue, totalvalue):
    b = _f51_growth(cllvalue, 63) - _f51_growth(totalvalue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-holder count log growth over a quarter, net of equity holder growth (hedger breadth building)
def f51om_f51_ownership_mix_concentration_putcnt_grow63_base_v092_signal(putholders, shrholders):
    b = _f51_growth(putholders, 63) - _f51_growth(shrholders, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-holder count log growth over a quarter, net of equity holder growth (bull breadth building)
def f51om_f51_ownership_mix_concentration_cllcnt_grow63_base_v093_signal(cllholders, shrholders):
    b = _f51_growth(cllholders, 63) - _f51_growth(shrholders, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net options-holder breadth growth: call-holder growth minus put-holder growth (sentiment breadth)
def f51om_f51_ownership_mix_concentration_optcnt_netgrow_base_v094_signal(cllholders, putholders):
    b = _f51_growth(cllholders, 63) - _f51_growth(putholders, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- put/call holder skew facets ---
# put-holder skew z-scored vs 252d (de-trended bearish breadth)
def f51om_f51_ownership_mix_concentration_putcntskew_z252_base_v095_signal(putholders, cllholders):
    s = _f51_skew(putholders, cllholders)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-holder skew percentile-rank vs 504d
def f51om_f51_ownership_mix_concentration_putcntskew_rank504_base_v096_signal(putholders, cllholders):
    s = _f51_skew(putholders, cllholders)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-holder skew displacement from slow EMA (breadth hedging displacement)
def f51om_f51_ownership_mix_concentration_putcntskew_disp_base_v097_signal(putholders, cllholders):
    s = _f51_skew(putholders, cllholders)
    b = s - s.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-holder skew half-year change
def f51om_f51_ownership_mix_concentration_putcntskew_chg126_base_v098_signal(putholders, cllholders):
    s = _f51_skew(putholders, cllholders)
    b = s - s.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- options breadth vs equity breadth facets ---
# call-breadth vs equity-breadth z-scored vs 252d
def f51om_f51_ownership_mix_concentration_callbreadth_z252_base_v099_signal(cllholders, shrholders):
    r = cllholders / shrholders.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-breadth vs equity-breadth half-year change
def f51om_f51_ownership_mix_concentration_callbreadth_chg126_base_v100_signal(cllholders, shrholders):
    r = cllholders / shrholders.replace(0, np.nan)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# options-breadth percentile-rank vs 504d
def f51om_f51_ownership_mix_concentration_optbreadth_rank504_base_v101_signal(putholders, cllholders, shrholders):
    opt = putholders + cllholders
    r = opt / shrholders.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# options-breadth dispersion over 126d (instability of derivatives interest)
def f51om_f51_ownership_mix_concentration_optbreadth_disp126_base_v102_signal(putholders, cllholders, shrholders):
    opt = putholders + cllholders
    r = opt / shrholders.replace(0, np.nan)
    b = _std(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- options value footprint facets ---
# options value footprint z-scored vs 252d
def f51om_f51_ownership_mix_concentration_optfootprint_z252_base_v103_signal(cllvalue, putvalue, totalvalue):
    r = (cllvalue + putvalue) / totalvalue.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# options value footprint percentile-rank vs 504d
def f51om_f51_ownership_mix_concentration_optfootprint_rank504_base_v104_signal(cllvalue, putvalue, totalvalue):
    r = (cllvalue + putvalue) / totalvalue.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net options sentiment value share half-year change (call-minus-put value share trajectory)
def f51om_f51_ownership_mix_concentration_optnetshare_chg126_base_v105_signal(cllvalue, putvalue, totalvalue):
    r = (cllvalue - putvalue) / totalvalue.replace(0, np.nan)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net options sentiment value share z-scored vs 252d
def f51om_f51_ownership_mix_concentration_optnetshare_z252_base_v106_signal(cllvalue, putvalue, totalvalue):
    r = (cllvalue - putvalue) / totalvalue.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- percentoftotal facets ---
# percentoftotal half-year momentum
def f51om_f51_ownership_mix_concentration_pot_chg126_base_v107_signal(percentoftotal):
    b = percentoftotal - percentoftotal.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal dispersion over 126d (conviction-weighting instability)
def f51om_f51_ownership_mix_concentration_pot_disp126_base_v108_signal(percentoftotal):
    b = _std(percentoftotal, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal displacement from slow EMA
def f51om_f51_ownership_mix_concentration_pot_disp_base_v109_signal(percentoftotal):
    b = percentoftotal - percentoftotal.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal extension above its own 252d max band (new conviction high)
def f51om_f51_ownership_mix_concentration_pot_ext_base_v110_signal(percentoftotal):
    hi = _rmax(percentoftotal, 252)
    b = percentoftotal / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal acceleration: 63d change now vs 63d change a quarter ago
def f51om_f51_ownership_mix_concentration_pot_accel_base_v111_signal(percentoftotal):
    c = percentoftotal - percentoftotal.shift(63)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# conviction interaction: percentoftotal x put-skew (hedged conviction)
def f51om_f51_ownership_mix_concentration_pot_putinter_base_v112_signal(percentoftotal, putvalue, cllvalue):
    ps = _f51_skew(putvalue, cllvalue)
    b = percentoftotal * (ps - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- fund-holder breadth / accumulation facets ---
# fund-holder count half-year log growth (mid-term breadth accumulation)
def f51om_f51_ownership_mix_concentration_fndcnt_grow126_base_v113_signal(fndholders):
    b = _f51_growth(fndholders, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder count accumulation persistence: fraction of last year fund count rose MoM
def f51om_f51_ownership_mix_concentration_fndcnt_streak_base_v114_signal(fndholders):
    up = (fndholders > fndholders.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder breadth share z-scored vs 252d (de-trended institutional breadth)
def f51om_f51_ownership_mix_concentration_fndcntshare_z252_base_v115_signal(fndholders, undholders, prfholders):
    tot = (fndholders + undholders + prfholders).replace(0, np.nan)
    s = fndholders / tot
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder breadth share half-year change
def f51om_f51_ownership_mix_concentration_fndcntshare_chg126_base_v116_signal(fndholders, undholders, prfholders):
    tot = (fndholders + undholders + prfholders).replace(0, np.nan)
    s = fndholders / tot
    b = s - s.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder count vs retail-holder count log ratio, z-scored vs 126d
def f51om_f51_ownership_mix_concentration_fndundcnt_z126_base_v117_signal(fndholders, undholders):
    r = _f51_logratio(fndholders, undholders)
    b = _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- fund ticket-size facets ---
# fund ticket size z-scored vs 252d (institutional position-size extremity)
def f51om_f51_ownership_mix_concentration_fndticket_z252_base_v118_signal(fndvalue, fndholders):
    t = fndvalue / fndholders.replace(0, np.nan)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund ticket size half-year log growth
def f51om_f51_ownership_mix_concentration_fndticket_grow126_base_v119_signal(fndvalue, fndholders):
    t = fndvalue / fndholders.replace(0, np.nan)
    b = _f51_growth(t, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund ticket vs retail ticket spread, half-year change (deepening conviction gap)
def f51om_f51_ownership_mix_concentration_ticketspread_chg126_base_v120_signal(fndvalue, fndholders, undvalue, undholders):
    tf = fndvalue / fndholders.replace(0, np.nan)
    tu = undvalue / undholders.replace(0, np.nan)
    r = _f51_logratio(tf, tu)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- concentration / composition facets ---
# count-Herfindahl displacement from slow EMA (breadth concentration displacement)
def f51om_f51_ownership_mix_concentration_herfcnt_disp_base_v121_signal(fndholders, undholders, prfholders):
    h = _f51_herf(fndholders, undholders, prfholders)
    b = h - h.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count-Herfindahl percentile-rank vs 504d
def f51om_f51_ownership_mix_concentration_herfcnt_rank504_base_v122_signal(fndholders, undholders, prfholders):
    h = _f51_herf(fndholders, undholders, prfholders)
    b = _rank(h, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# non-fund VALUE imbalance (und vs prf) z-scored vs 252d
def f51om_f51_ownership_mix_concentration_nonfundimb_z252_base_v123_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    imb = (undvalue - prf).abs() / (undvalue + prf).replace(0, np.nan)
    b = _z(imb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# prf (residual/other) value share half-year change
def f51om_f51_ownership_mix_concentration_prfshare_chg126_base_v124_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    s = prf / totalvalue.replace(0, np.nan)
    b = s - s.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# prf value share z-scored vs 252d
def f51om_f51_ownership_mix_concentration_prfshare_z252_base_v125_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    s = prf / totalvalue.replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count-entropy (breadth diversity) half-year change
def f51om_f51_ownership_mix_concentration_cntentropy_chg126_base_v126_signal(fndholders, undholders, prfholders):
    tot = (fndholders + undholders + prfholders).replace(0, np.nan)
    sa = (fndholders / tot).clip(lower=1e-9)
    sb = (undholders / tot).clip(lower=1e-9)
    sc = (prfholders / tot).clip(lower=1e-9)
    e = -(sa * np.log(sa) + sb * np.log(sb) + sc * np.log(sc))
    b = e - e.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- rotation / divergence facets ---
# fund-share rotation persistence over half-year vs year sign agreement
def f51om_f51_ownership_mix_concentration_fndrot_persist_base_v127_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    c1 = s - s.shift(126)
    c2 = s - s.shift(252)
    b = np.sign(c1) * np.sign(c2) * (c1.abs() + c2.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-skew rotation persistence over quarter vs half-year
def f51om_f51_ownership_mix_concentration_putrot_persist_base_v128_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    c1 = s - s.shift(63)
    c2 = s - s.shift(126)
    b = np.sign(c1) * np.sign(c2) * (c1.abs() + c2.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composition rotation magnitude (half-year): combined |chg| of fnd & und value shares
def f51om_f51_ownership_mix_concentration_rotmag126_base_v129_signal(fndvalue, undvalue, totalvalue):
    sf = _f51_share(fndvalue, totalvalue)
    su = _f51_share(undvalue, totalvalue)
    b = (sf - sf.shift(126)).abs() + (su - su.shift(126)).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bull-vs-bear breadth rotation: call-breadth-share change minus put-breadth-share change (sentiment rotation)
def f51om_f51_ownership_mix_concentration_optrot_base_v130_signal(cllholders, putholders, shrholders):
    cs = cllholders / shrholders.replace(0, np.nan)
    ps = putholders / shrholders.replace(0, np.nan)
    b = (cs - cs.shift(63)) - (ps - ps.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divergence: hedging build (put-skew up) while fund breadth shrinks (count) over a quarter
def f51om_f51_ownership_mix_concentration_diverge_cnt_base_v131_signal(putholders, cllholders, fndholders, undholders, prfholders):
    ps = _f51_skew(putholders, cllholders)
    fc = fndholders / (fndholders + undholders + prfholders).replace(0, np.nan)
    b = (ps - ps.shift(63)) - (fc - fc.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- regime / streak facets ---
# fund-share regime persistence: fraction of last quarter fund-share sat above its 252d median
def f51om_f51_ownership_mix_concentration_fndshare_regdist_base_v132_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    med = s.rolling(252, min_periods=63).median()
    above = (s > med).astype(float)
    b = above.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-skew regime distance: level minus its own 252d median band
def f51om_f51_ownership_mix_concentration_putskew_regdist_base_v133_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    med = s.rolling(252, min_periods=63).median()
    b = s - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# options-footprint regime distance: footprint minus its own 252d median
def f51om_f51_ownership_mix_concentration_optfoot_regdist_base_v134_signal(cllvalue, putvalue, totalvalue):
    r = (cllvalue + putvalue) / totalvalue.replace(0, np.nan)
    med = r.rolling(252, min_periods=63).median()
    b = r - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retail-share streak: fraction of last year retail value-share rose MoM (crowding persistence)
def f51om_f51_ownership_mix_concentration_undshare_streak_base_v135_signal(undvalue, totalvalue):
    s = _f51_share(undvalue, totalvalue)
    up = (s > s.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-breadth streak: fraction of last year call-breadth rose MoM (bull-interest persistence)
def f51om_f51_ownership_mix_concentration_callbreadth_streak_base_v136_signal(cllholders, shrholders):
    r = cllholders / shrholders.replace(0, np.nan)
    up = (r > r.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- interaction / quality facets ---
# institutional-breadth-weighted conviction: fund count share x percentoftotal
def f51om_f51_ownership_mix_concentration_fndcntpot_base_v137_signal(fndholders, undholders, prfholders, percentoftotal):
    fc = fndholders / (fndholders + undholders + prfholders).replace(0, np.nan)
    b = fc * percentoftotal
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hedged-conviction quality: percentoftotal x (1 - put-holder skew)
def f51om_f51_ownership_mix_concentration_potcallq_base_v138_signal(percentoftotal, putholders, cllholders):
    ps = _f51_skew(putholders, cllholders)
    b = percentoftotal * (1.0 - ps)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite mix-quality: fund value share minus options hedging footprint share
def f51om_f51_ownership_mix_concentration_mixq_base_v139_signal(fndvalue, totalvalue, putvalue, cllvalue):
    fs = _f51_share(fndvalue, totalvalue)
    foot = (putvalue + cllvalue) / totalvalue.replace(0, np.nan)
    b = fs - foot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-vs-breadth concentration gap for FUND only: value share minus count share
def f51om_f51_ownership_mix_concentration_fndvcgap_base_v140_signal(fndvalue, totalvalue, fndholders, undholders, prfholders):
    vs = _f51_share(fndvalue, totalvalue)
    cs = fndholders / (fndholders + undholders + prfholders).replace(0, np.nan)
    b = vs - cs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-vs-breadth gap for RETAIL: und value share minus und count share
def f51om_f51_ownership_mix_concentration_undvcgap_base_v141_signal(undvalue, totalvalue, fndholders, undholders, prfholders):
    vs = _f51_share(undvalue, totalvalue)
    cs = undholders / (fndholders + undholders + prfholders).replace(0, np.nan)
    b = vs - cs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# options-value-to-equity-value tilt: (call+put value) relative to fund value (derivatives vs core)
def f51om_f51_ownership_mix_concentration_optvsfnd_base_v142_signal(cllvalue, putvalue, fndvalue):
    b = _f51_logratio(cllvalue + putvalue, fndvalue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-value vs fund-value log ratio, z-scored vs 252d (bullish-derivatives-vs-core extremity)
def f51om_f51_ownership_mix_concentration_cllvsfnd_chg63_base_v143_signal(cllvalue, fndvalue):
    r = _f51_logratio(cllvalue, fndvalue)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-value vs total ownership value share z-scored (hedge value footprint extremity)
def f51om_f51_ownership_mix_concentration_putvalshare_z252_base_v144_signal(putvalue, totalvalue):
    s = _f51_share(putvalue, totalvalue)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-value vs total ownership value share half-year change
def f51om_f51_ownership_mix_concentration_cllvalshare_chg126_base_v145_signal(cllvalue, totalvalue):
    s = _f51_share(cllvalue, totalvalue)
    b = s - s.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average call ticket vs average put ticket, smoothed (bull vs hedge conviction-per-holder)
def f51om_f51_ownership_mix_concentration_callputticket_sm_base_v146_signal(cllvalue, cllholders, putvalue, putholders):
    tc = cllvalue / cllholders.replace(0, np.nan)
    tp = putvalue / putholders.replace(0, np.nan)
    r = _f51_logratio(tc, tp)
    b = r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share vs put-skew co-movement over half-year (institutional resolve vs hedging)
def f51om_f51_ownership_mix_concentration_fndputco126_base_v147_signal(fndvalue, totalvalue, putvalue, cllvalue):
    fs = _f51_share(fndvalue, totalvalue)
    ps = _f51_skew(putvalue, cllvalue)
    dfs = fs - fs.shift(126)
    dps = ps - ps.shift(126)
    b = np.sign(dfs * dps) * (dfs.abs() + dps.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrholders (equity 13F) breadth growth vs non-fund holder growth (who is adding, equity vs other)
def f51om_f51_ownership_mix_concentration_shrnonfund_grow_base_v148_signal(shrholders, undholders, prfholders):
    gs = _f51_growth(shrholders, 63)
    gn = _f51_growth(undholders + prfholders, 63)
    b = gs - gn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# options-footprint acceleration: 63d change now vs 63d change a quarter ago
def f51om_f51_ownership_mix_concentration_optfoot_accel_base_v149_signal(cllvalue, putvalue, totalvalue):
    r = (cllvalue + putvalue) / totalvalue.replace(0, np.nan)
    c = r - r.shift(63)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite ownership stress: put-skew x options-footprint x retail-share (crowded-hedged-retail proxy)
def f51om_f51_ownership_mix_concentration_stress_base_v150_signal(putvalue, cllvalue, totalvalue, undvalue):
    ps = _f51_skew(putvalue, cllvalue)
    foot = (putvalue + cllvalue) / totalvalue.replace(0, np.nan)
    us = _f51_share(undvalue, totalvalue)
    b = (ps - 0.5) * foot + 0.5 * us
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f51om_f51_ownership_mix_concentration_fndshare_rank504_base_v076_signal,
    f51om_f51_ownership_mix_concentration_fndshare_spr_base_v077_signal,
    f51om_f51_ownership_mix_concentration_fndshare_chg126_base_v078_signal,
    f51om_f51_ownership_mix_concentration_fndshare_accel_base_v079_signal,
    f51om_f51_ownership_mix_concentration_fndshare_signmag_base_v080_signal,
    f51om_f51_ownership_mix_concentration_undshare_chg126_base_v081_signal,
    f51om_f51_ownership_mix_concentration_undshare_disp63_base_v082_signal,
    f51om_f51_ownership_mix_concentration_undshare_disp_base_v083_signal,
    f51om_f51_ownership_mix_concentration_undfnd_logrchg126_base_v084_signal,
    f51om_f51_ownership_mix_concentration_putskew_rank504_base_v085_signal,
    f51om_f51_ownership_mix_concentration_putskew_chg126_base_v086_signal,
    f51om_f51_ownership_mix_concentration_putskew_accel_base_v087_signal,
    f51om_f51_ownership_mix_concentration_putskew_spr_base_v088_signal,
    f51om_f51_ownership_mix_concentration_putskew_signmag_base_v089_signal,
    f51om_f51_ownership_mix_concentration_putval_grow63_base_v090_signal,
    f51om_f51_ownership_mix_concentration_cllval_grow63_base_v091_signal,
    f51om_f51_ownership_mix_concentration_putcnt_grow63_base_v092_signal,
    f51om_f51_ownership_mix_concentration_cllcnt_grow63_base_v093_signal,
    f51om_f51_ownership_mix_concentration_optcnt_netgrow_base_v094_signal,
    f51om_f51_ownership_mix_concentration_putcntskew_z252_base_v095_signal,
    f51om_f51_ownership_mix_concentration_putcntskew_rank504_base_v096_signal,
    f51om_f51_ownership_mix_concentration_putcntskew_disp_base_v097_signal,
    f51om_f51_ownership_mix_concentration_putcntskew_chg126_base_v098_signal,
    f51om_f51_ownership_mix_concentration_callbreadth_z252_base_v099_signal,
    f51om_f51_ownership_mix_concentration_callbreadth_chg126_base_v100_signal,
    f51om_f51_ownership_mix_concentration_optbreadth_rank504_base_v101_signal,
    f51om_f51_ownership_mix_concentration_optbreadth_disp126_base_v102_signal,
    f51om_f51_ownership_mix_concentration_optfootprint_z252_base_v103_signal,
    f51om_f51_ownership_mix_concentration_optfootprint_rank504_base_v104_signal,
    f51om_f51_ownership_mix_concentration_optnetshare_chg126_base_v105_signal,
    f51om_f51_ownership_mix_concentration_optnetshare_z252_base_v106_signal,
    f51om_f51_ownership_mix_concentration_pot_chg126_base_v107_signal,
    f51om_f51_ownership_mix_concentration_pot_disp126_base_v108_signal,
    f51om_f51_ownership_mix_concentration_pot_disp_base_v109_signal,
    f51om_f51_ownership_mix_concentration_pot_ext_base_v110_signal,
    f51om_f51_ownership_mix_concentration_pot_accel_base_v111_signal,
    f51om_f51_ownership_mix_concentration_pot_putinter_base_v112_signal,
    f51om_f51_ownership_mix_concentration_fndcnt_grow126_base_v113_signal,
    f51om_f51_ownership_mix_concentration_fndcnt_streak_base_v114_signal,
    f51om_f51_ownership_mix_concentration_fndcntshare_z252_base_v115_signal,
    f51om_f51_ownership_mix_concentration_fndcntshare_chg126_base_v116_signal,
    f51om_f51_ownership_mix_concentration_fndundcnt_z126_base_v117_signal,
    f51om_f51_ownership_mix_concentration_fndticket_z252_base_v118_signal,
    f51om_f51_ownership_mix_concentration_fndticket_grow126_base_v119_signal,
    f51om_f51_ownership_mix_concentration_ticketspread_chg126_base_v120_signal,
    f51om_f51_ownership_mix_concentration_herfcnt_disp_base_v121_signal,
    f51om_f51_ownership_mix_concentration_herfcnt_rank504_base_v122_signal,
    f51om_f51_ownership_mix_concentration_nonfundimb_z252_base_v123_signal,
    f51om_f51_ownership_mix_concentration_prfshare_chg126_base_v124_signal,
    f51om_f51_ownership_mix_concentration_prfshare_z252_base_v125_signal,
    f51om_f51_ownership_mix_concentration_cntentropy_chg126_base_v126_signal,
    f51om_f51_ownership_mix_concentration_fndrot_persist_base_v127_signal,
    f51om_f51_ownership_mix_concentration_putrot_persist_base_v128_signal,
    f51om_f51_ownership_mix_concentration_rotmag126_base_v129_signal,
    f51om_f51_ownership_mix_concentration_optrot_base_v130_signal,
    f51om_f51_ownership_mix_concentration_diverge_cnt_base_v131_signal,
    f51om_f51_ownership_mix_concentration_fndshare_regdist_base_v132_signal,
    f51om_f51_ownership_mix_concentration_putskew_regdist_base_v133_signal,
    f51om_f51_ownership_mix_concentration_optfoot_regdist_base_v134_signal,
    f51om_f51_ownership_mix_concentration_undshare_streak_base_v135_signal,
    f51om_f51_ownership_mix_concentration_callbreadth_streak_base_v136_signal,
    f51om_f51_ownership_mix_concentration_fndcntpot_base_v137_signal,
    f51om_f51_ownership_mix_concentration_potcallq_base_v138_signal,
    f51om_f51_ownership_mix_concentration_mixq_base_v139_signal,
    f51om_f51_ownership_mix_concentration_fndvcgap_base_v140_signal,
    f51om_f51_ownership_mix_concentration_undvcgap_base_v141_signal,
    f51om_f51_ownership_mix_concentration_optvsfnd_base_v142_signal,
    f51om_f51_ownership_mix_concentration_cllvsfnd_chg63_base_v143_signal,
    f51om_f51_ownership_mix_concentration_putvalshare_z252_base_v144_signal,
    f51om_f51_ownership_mix_concentration_cllvalshare_chg126_base_v145_signal,
    f51om_f51_ownership_mix_concentration_callputticket_sm_base_v146_signal,
    f51om_f51_ownership_mix_concentration_fndputco126_base_v147_signal,
    f51om_f51_ownership_mix_concentration_shrnonfund_grow_base_v148_signal,
    f51om_f51_ownership_mix_concentration_optfoot_accel_base_v149_signal,
    f51om_f51_ownership_mix_concentration_stress_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F51_OWNERSHIP_MIX_CONCENTRATION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "tbvps",
        "de", "ncfdiv", "ncfinv", "dps", "divyield", "payoutratio", "prefdivis",
        "netincdis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
        "fndvalue", "undvalue", "prfvalue", "fndunits", "undunits",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    fndvalue = _fund(201, base=5.0e8, drift=0.05, vol=0.10).rename("fndvalue")
    undvalue = _fund(202, base=2.5e8, drift=0.03, vol=0.12).rename("undvalue")
    prfvalue = _fund(203, base=1.2e8, drift=0.02, vol=0.13).rename("prfvalue")
    totalvalue = (fndvalue + undvalue + prfvalue
                  + _fund(204, base=1.0e8, drift=0.025, vol=0.09)).rename("totalvalue")
    fndholders = _fund(205, base=300.0, drift=0.05, vol=0.10).rename("fndholders")
    undholders = _fund(206, base=180.0, drift=0.03, vol=0.12).rename("undholders")
    prfholders = _fund(207, base=90.0, drift=0.02, vol=0.13).rename("prfholders")
    shrholders = _fund(208, base=420.0, drift=0.045, vol=0.10).rename("shrholders")
    cllholders = _fund(209, base=60.0, drift=0.04, vol=0.15).rename("cllholders")
    putholders = _fund(210, base=45.0, drift=0.035, vol=0.16).rename("putholders")
    cllvalue = _fund(211, base=8.0e7, drift=0.04, vol=0.16).rename("cllvalue")
    putvalue = _fund(212, base=6.0e7, drift=0.05, vol=0.17).rename("putvalue")
    percentoftotal = (_fund(213, base=0.04, drift=0.02, vol=0.10)
                      .clip(upper=0.95)).rename("percentoftotal")

    cols = {
        "fndvalue": fndvalue, "undvalue": undvalue, "prfvalue": prfvalue,
        "totalvalue": totalvalue, "fndholders": fndholders, "undholders": undholders,
        "prfholders": prfholders, "shrholders": shrholders, "cllholders": cllholders,
        "putholders": putholders, "cllvalue": cllvalue, "putvalue": putvalue,
        "percentoftotal": percentoftotal,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    own = {"shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
           "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
           "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue",
           "dbtvalue", "fndvalue", "undvalue", "prfvalue", "fndunits", "undunits"}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BAD INPUTS %s: %s" % (name, meta["inputs"])
        assert len(set(meta["inputs"]) & own) >= 1, "NO OWNERSHIP COL %s" % name
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

    print("OK f51_ownership_mix_concentration_base_076_150_claude: %d features pass" % n_features)
