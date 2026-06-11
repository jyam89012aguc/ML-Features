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
    return fndholders + undholders + prfholders + dbtholders


def _f43_share(part, fndholders, undholders, prfholders, dbtholders):
    tot = fndholders + undholders + prfholders + dbtholders
    return part / tot.replace(0, np.nan)


def _f43_hhi(fndholders, undholders, prfholders, dbtholders):
    tot = (fndholders + undholders + prfholders + dbtholders).replace(0, np.nan)
    return (fndholders / tot) ** 2 + (undholders / tot) ** 2 + (prfholders / tot) ** 2 + (dbtholders / tot) ** 2


def _f43_entropy(fndholders, undholders, prfholders, dbtholders):
    tot = (fndholders + undholders + prfholders + dbtholders).replace(0, np.nan)
    out = None
    for part in (fndholders, undholders, prfholders, dbtholders):
        s = (part / tot).clip(lower=1e-12)
        term = -s * np.log(s)
        out = term if out is None else out + term
    return out


def _f43_smart_dumb(fndholders, undholders, prfholders, dbtholders):
    dumb = (undholders + prfholders + dbtholders).replace(0, np.nan)
    return fndholders / dumb


def _f43_avg_value(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = (fndholders + undholders + prfholders + dbtholders).replace(0, np.nan)
    return totalvalue / tot


# ============================================================
# breadth level over a longer window context: log total holders smoothed (persistent breadth)
def f43oc_f43_ownership_concentration_breadth_breadthema_63d_base_v076_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = np.log(tot.replace(0, np.nan)).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth displacement: log breadth minus its slow EMA (breadth deviation)
def f43oc_f43_ownership_concentration_breadth_breadthdisp_63d_base_v077_signal(fndholders, undholders, prfholders, dbtholders):
    lt = np.log(_f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan))
    b = lt - lt.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth half-year momentum: log change over 126d (medium-horizon accumulation breadth)
def f43oc_f43_ownership_concentration_breadth_breadthmom_126d_base_v078_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    b = np.log(tot) - np.log(tot.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share level over a half-year z-window (smart-money tilt, longer regime)
def f43oc_f43_ownership_concentration_breadth_fndsharez2_252d_base_v079_signal(fndholders, undholders, prfholders, dbtholders):
    sh = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    b = _z(sh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwriter-share momentum over a half-year (placement-base rotation)
def f43oc_f43_ownership_concentration_breadth_undsharemom_126d_base_v080_signal(fndholders, undholders, prfholders, dbtholders):
    sh = _f43_share(undholders, fndholders, undholders, prfholders, dbtholders)
    b = sh - sh.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-share momentum over a quarter (preferred-base rotation)
def f43oc_f43_ownership_concentration_breadth_prfsharemom_63d_base_v081_signal(fndholders, undholders, prfholders, dbtholders):
    sh = _f43_share(prfholders, fndholders, undholders, prfholders, dbtholders)
    b = sh - sh.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-mix HHI smoothed (persistent concentration regime)
def f43oc_f43_ownership_concentration_breadth_hhiema_63d_base_v082_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f43_hhi(fndholders, undholders, prfholders, dbtholders)
    b = h.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-mix HHI displacement vs its slow EMA (concentration impulse)
def f43oc_f43_ownership_concentration_breadth_hhidisp_63d_base_v083_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f43_hhi(fndholders, undholders, prfholders, dbtholders)
    b = h - h.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# entropy-vs-HHI gap smoothed: diversity minus an inverse-concentration baseline (mix shape)
def f43oc_f43_ownership_concentration_breadth_entropyema_63d_base_v084_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    h = _f43_hhi(fndholders, undholders, prfholders, dbtholders)
    gap = e - (1.0 - h) * np.log(4.0)
    b = gap.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-holder concentration smoothed (persistent dominance level)
def f43oc_f43_ownership_concentration_breadth_concema_63d_base_v085_signal(percentoftotal):
    b = percentoftotal.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-holder concentration displacement vs slow EMA (concentration deviation)
def f43oc_f43_ownership_concentration_breadth_concdisp_63d_base_v086_signal(percentoftotal):
    b = percentoftotal - percentoftotal.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-holder concentration half-year trend (slow re-rating of dominance)
def f43oc_f43_ownership_concentration_breadth_conctrd_126d_base_v087_signal(percentoftotal):
    b = percentoftotal - percentoftotal.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-dumb ratio smoothed and logged (persistent smart-money tilt)
def f43oc_f43_ownership_concentration_breadth_smartdumbema_63d_base_v088_signal(fndholders, undholders, prfholders, dbtholders):
    r = _f43_smart_dumb(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    b = np.log(r).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-dumb ratio half-year log-trend (slow smart-money rotation)
def f43oc_f43_ownership_concentration_breadth_smartdumbmom_126d_base_v089_signal(fndholders, undholders, prfholders, dbtholders):
    r = _f43_smart_dumb(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    b = np.log(r) - np.log(r.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value per holder half-year growth (per-holder dollar expansion)
def f43oc_f43_ownership_concentration_breadth_avgvalmom_126d_base_v090_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    av = _f43_avg_value(totalvalue, fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    b = np.log(av) - np.log(av.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value concentration (value x pct) half-year growth (concentrated-dollar expansion)
def f43oc_f43_ownership_concentration_breadth_valconcmom_126d_base_v091_signal(totalvalue, percentoftotal):
    vc = (totalvalue * percentoftotal).replace(0, np.nan)
    b = np.log(vc) - np.log(vc.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share monthly change (short-horizon rotation toward funds)
def f43oc_f43_ownership_concentration_breadth_fndsharemom_21d_base_v092_signal(fndholders, undholders, prfholders, dbtholders):
    sh = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    b = sh - sh.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-share monthly change (short-horizon creditor rotation)
def f43oc_f43_ownership_concentration_breadth_dbtsharemom_21d_base_v093_signal(fndholders, undholders, prfholders, dbtholders):
    sh = _f43_share(dbtholders, fndholders, undholders, prfholders, dbtholders)
    b = sh - sh.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# HHI monthly change (short-horizon concentration impulse)
def f43oc_f43_ownership_concentration_breadth_hhitrd_21d_base_v094_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f43_hhi(fndholders, undholders, prfholders, dbtholders)
    b = h - h.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# entropy monthly change (short-horizon diversification impulse)
def f43oc_f43_ownership_concentration_breadth_entropytrd_21d_base_v095_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    b = e - e.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder count half-year z (smart-money base regime)
def f43oc_f43_ownership_concentration_breadth_fndcountz_126d_base_v096_signal(fndholders):
    b = _z(np.log(fndholders.replace(0, np.nan)), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-holder count half-year momentum (creditor-base expansion)
def f43oc_f43_ownership_concentration_breadth_dbtcountmom_126d_base_v097_signal(dbtholders):
    d = dbtholders.replace(0, np.nan)
    b = np.log(d) - np.log(d.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-holder count z (preferred-base regime)
def f43oc_f43_ownership_concentration_breadth_prfcountz_252d_base_v098_signal(prfholders):
    b = _z(np.log(prfholders.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwriter-holder count momentum (placement-base expansion)
def f43oc_f43_ownership_concentration_breadth_undcountmom_63d_base_v099_signal(undholders):
    u = undholders.replace(0, np.nan)
    b = np.log(u) - np.log(u.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-to-debt log ratio half-year change (equity-vs-creditor rotation)
def f43oc_f43_ownership_concentration_breadth_fnddbtmom_126d_base_v100_signal(fndholders, dbtholders):
    r = np.log(fndholders.replace(0, np.nan) / dbtholders.replace(0, np.nan))
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-to-preferred log ratio z (common-vs-preferred tilt regime)
def f43oc_f43_ownership_concentration_breadth_fndprfz_252d_base_v101_signal(fndholders, prfholders):
    r = np.log(fndholders.replace(0, np.nan) / prfholders.replace(0, np.nan))
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwriter-to-fund log ratio momentum (placement-vs-organic rotation)
def f43oc_f43_ownership_concentration_breadth_undfndmom_63d_base_v102_signal(undholders, fndholders):
    r = np.log(undholders.replace(0, np.nan) / fndholders.replace(0, np.nan))
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value per fund holder z (conviction-dollar regime)
def f43oc_f43_ownership_concentration_breadth_valperfndz_252d_base_v103_signal(totalvalue, fndholders):
    v = np.log((totalvalue / fndholders.replace(0, np.nan)).replace(0, np.nan))
    b = _z(v, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# totalvalue half-year momentum (ownership-value growth, medium horizon)
def f43oc_f43_ownership_concentration_breadth_valmom_126d_base_v104_signal(totalvalue):
    v = totalvalue.replace(0, np.nan)
    b = np.log(v) - np.log(v.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value growth vs HHI growth over half-year (value scaling with or against concentration)
def f43oc_f43_ownership_concentration_breadth_valbreadthspr_126d_base_v105_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    v = totalvalue.replace(0, np.nan)
    h = _f43_hhi(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    b = (np.log(v) - np.log(v.shift(126))) - (np.log(h) - np.log(h.shift(126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Gini-like concentration of holder mix (mean abs difference of shares)
def f43oc_f43_ownership_concentration_breadth_mixgini_21d_base_v106_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    s = [fndholders / tot, undholders / tot, prfholders / tot, dbtholders / tot]
    mad = None
    for a in range(4):
        for bb in range(a + 1, 4):
            d = (s[a] - s[bb]).abs()
            mad = d if mad is None else mad + d
    b = mad / 6.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share dominance gap half-year change (smart-money pulling ahead of next type)
def f43oc_f43_ownership_concentration_breadth_fnddomgapmom_126d_base_v107_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sf = fndholders / tot
    others = pd.concat([undholders / tot, prfholders / tot, dbtholders / tot], axis=1).max(axis=1)
    gap = sf - others
    b = gap - gap.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration range position: where pct sits within its own 126d hi-lo range
def f43oc_f43_ownership_concentration_breadth_concexcess_126d_base_v108_signal(percentoftotal):
    hi = _rmax(percentoftotal, 126)
    lo = _rmin(percentoftotal, 126)
    b = (percentoftotal - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration percentile-ranked vs 252d history (medium-horizon dominance rank)
def f43oc_f43_ownership_concentration_breadth_concrank_252d_base_v109_signal(percentoftotal):
    b = percentoftotal.rolling(252, min_periods=84).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration-value coupling: pct x log avg value per holder z (concentrated rich holders)
def f43oc_f43_ownership_concentration_breadth_concvalz_252d_base_v110_signal(percentoftotal, totalvalue, fndholders, undholders, prfholders, dbtholders):
    av = _f43_avg_value(totalvalue, fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    raw = percentoftotal * np.log(av)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share volatility over 126d (instability of the smart-money tilt)
def f43oc_f43_ownership_concentration_breadth_fndsharerank_252d_base_v111_signal(fndholders, undholders, prfholders, dbtholders):
    sh = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    b = _std(sh.diff(), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# income-vs-growth holder tilt (preferred+debt share minus fund share), half-year change
def f43oc_f43_ownership_concentration_breadth_incomeshare_mom_126d_base_v112_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    tilt = (prfholders + dbtholders) / tot - fndholders / tot
    b = tilt - tilt.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-type rotation magnitude over a month (short-horizon mix churn)
def f43oc_f43_ownership_concentration_breadth_rotmag_21d_base_v113_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    out = None
    for part in (fndholders, undholders, prfholders, dbtholders):
        s = part / tot
        d = (s - s.shift(21)).abs()
        out = d if out is None else out + d
    b = out
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth stability over 252d (longer-horizon inverse coefficient of variation)
def f43oc_f43_ownership_concentration_breadth_breadthstab_252d_base_v114_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _mean(tot, 252) / _std(tot, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration churn over 63d (short-horizon dominance instability)
def f43oc_f43_ownership_concentration_breadth_concchurn_63d_base_v115_signal(percentoftotal):
    b = _std(percentoftotal, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-share entropy contribution (creditor diversity weight)
def f43oc_f43_ownership_concentration_breadth_dbtentcontrib_21d_base_v116_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sd = (dbtholders / tot).clip(lower=1e-12)
    b = -sd * np.log(sd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-vs-equal dominance half-year change (rising concentration above equal weight)
def f43oc_f43_ownership_concentration_breadth_topvsequalmom_126d_base_v117_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    dom = percentoftotal * tot
    b = np.log(dom.replace(0, np.nan)).diff(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creditor-vs-equity rotation over a month (short-horizon)
def f43oc_f43_ownership_concentration_breadth_credeqrot_21d_base_v118_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sd = dbtholders / tot
    sf = fndholders / tot
    b = (sd - sd.shift(21)) - (sf - sf.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth slope over 63d (short-horizon regression slope of log breadth)
def f43oc_f43_ownership_concentration_breadth_breadthslope_63d_base_v119_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _slope(np.log(tot.replace(0, np.nan)), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration slope over 63d (short-horizon regression slope of percentoftotal)
def f43oc_f43_ownership_concentration_breadth_concslope_63d_base_v120_signal(percentoftotal):
    b = _slope(percentoftotal, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share slope over 126d (smart-money tilt regression trend)
def f43oc_f43_ownership_concentration_breadth_fndshareslope_126d_base_v121_signal(fndholders, undholders, prfholders, dbtholders):
    sh = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    b = _slope(sh, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# entropy slope over 126d (diversification regression trend)
def f43oc_f43_ownership_concentration_breadth_entropyslope_126d_base_v122_signal(fndholders, undholders, prfholders, dbtholders):
    e = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    b = _slope(e, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-weighted breadth half-year change (size of broad ownership growth)
def f43oc_f43_ownership_concentration_breadth_valbreadthmom_126d_base_v123_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    vb = np.log(totalvalue.replace(0, np.nan)) + np.log(tot.replace(0, np.nan))
    b = vb - vb.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-vs-debt entropy weight spread half-year change (smart-vs-creditor diversity rotation)
def f43oc_f43_ownership_concentration_breadth_fnddbtentmom_126d_base_v124_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sf = (fndholders / tot).clip(lower=1e-12)
    sd = (dbtholders / tot).clip(lower=1e-12)
    spread = (-sf * np.log(sf)) - (-sd * np.log(sd))
    b = spread - spread.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-dumb ratio percentile-ranked vs 504d (long-horizon smart-money tilt rank)
def f43oc_f43_ownership_concentration_breadth_smartdumbrank_504d_base_v125_signal(fndholders, undholders, prfholders, dbtholders):
    r = np.log(_f43_smart_dumb(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan))
    b = r.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-concentration tanh momentum over a quarter (bounded dominance change)
def f43oc_f43_ownership_concentration_breadth_conctanh_63d_base_v126_signal(percentoftotal):
    chg = percentoftotal - percentoftotal.shift(63)
    b = np.tanh(15.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth tanh momentum over a quarter (bounded breadth change, medium horizon)
def f43oc_f43_ownership_concentration_breadth_breadthtanh_63d_base_v127_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    chg = np.log(tot) - np.log(tot.shift(63))
    b = np.tanh(6.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# HHI percentile-ranked vs 252d (medium-horizon concentration regime rank)
def f43oc_f43_ownership_concentration_breadth_hhirank_252d_base_v128_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f43_hhi(fndholders, undholders, prfholders, dbtholders)
    b = h.rolling(252, min_periods=84).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder half-year vs concentration half-year spread (broadening-vs-crowding value)
def f43oc_f43_ownership_concentration_breadth_concdollar_126d_base_v129_signal(totalvalue, percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    av = (totalvalue / tot).replace(0, np.nan)
    avg = np.log(av).diff(126)
    cg = np.log(percentoftotal.replace(0, np.nan)).diff(126)
    b = avg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration sign-magnitude excess (convex dominance signal, half-year base)
def f43oc_f43_ownership_concentration_breadth_concsignmag_126d_base_v130_signal(percentoftotal):
    exc = percentoftotal - _mean(percentoftotal, 126)
    b = np.sign(exc) * (exc.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share up-day fraction over 126d minus 0.5 (smart-money accumulation persistence)
def f43oc_f43_ownership_concentration_breadth_fndshareasym_126d_base_v131_signal(fndholders, undholders, prfholders, dbtholders):
    sh = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    up = (sh.diff() > 0).astype(float)
    hit = up.rolling(126, min_periods=42).mean() - 0.5
    rng = (sh.rolling(126, min_periods=42).max() - sh.rolling(126, min_periods=42).min())
    b = hit * (1.0 + 10.0 * rng)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-holder hit-rate plus magnitude (steady smart-money accumulation breadth)
def f43oc_f43_ownership_concentration_breadth_fndhit_63d_base_v132_signal(fndholders):
    up = (fndholders.diff() > 0).astype(float)
    hit = up.rolling(63, min_periods=21).mean() - 0.5
    mag = fndholders.pct_change().rolling(63, min_periods=21).mean()
    b = hit + 5.0 * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-vs-preferred income-holder balance momentum (income-class rotation)
def f43oc_f43_ownership_concentration_breadth_incomebalmom_63d_base_v133_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    bal = (prfholders - dbtholders) / tot
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration acceleration: change in 21d concentration trend (dominance impulse)
def f43oc_f43_ownership_concentration_breadth_concrevert_126d_base_v134_signal(percentoftotal):
    g = percentoftotal.diff(21)
    b = g - g.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth vs value rank spread over 252d (broadening with or without value)
def f43oc_f43_ownership_concentration_breadth_breadthvalrank_252d_base_v135_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    br = np.log(tot.replace(0, np.nan)).rolling(252, min_periods=84).rank(pct=True)
    vr = np.log(totalvalue.replace(0, np.nan)).rolling(252, min_periods=84).rank(pct=True)
    b = br - vr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-count-to-breadth elasticity: fund growth divided by breadth growth (63d)
def f43oc_f43_ownership_concentration_breadth_fndelastic_63d_base_v136_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    fg = np.log(fndholders.replace(0, np.nan)).diff(63)
    bg = np.log(tot).diff(63)
    b = fg / bg.replace(0, np.nan)
    b = b.clip(lower=-10, upper=10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-fund-holder half-year growth (conviction dollars per smart holder, medium)
def f43oc_f43_ownership_concentration_breadth_valperfndmom_126d_base_v137_signal(totalvalue, fndholders):
    v = (totalvalue / fndholders.replace(0, np.nan)).replace(0, np.nan)
    b = np.log(v) - np.log(v.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred+debt income-holder count log level (income-base breadth)
def f43oc_f43_ownership_concentration_breadth_incomecount_21d_base_v138_signal(prfholders, dbtholders):
    b = np.log((prfholders + dbtholders).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# income-holder count half-year momentum (income-base expansion)
def f43oc_f43_ownership_concentration_breadth_incomecountmom_126d_base_v139_signal(prfholders, dbtholders):
    ic = (prfholders + dbtholders).replace(0, np.nan)
    b = np.log(ic) - np.log(ic.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-holder (fund+underwriter) share of total holders (equity-base breadth slice)
def f43oc_f43_ownership_concentration_breadth_equityshare_21d_base_v140_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    b = (fndholders + undholders) / tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-share z over 252d (equity-base regime)
def f43oc_f43_ownership_concentration_breadth_equitysharez_252d_base_v141_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    sh = (fndholders + undholders) / tot
    b = _z(sh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-concentration vs avg-value coupling change (concentration with rising per-holder value)
def f43oc_f43_ownership_concentration_breadth_concvalcouple_63d_base_v142_signal(percentoftotal, totalvalue, fndholders, undholders, prfholders, dbtholders):
    av = _f43_avg_value(totalvalue, fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    cc = percentoftotal.diff()
    ag = np.log(av).diff()
    b = cc.rolling(126, min_periods=42).corr(ag)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth quarter-over-quarter acceleration (change in 63d breadth growth)
def f43oc_f43_ownership_concentration_breadth_breadthaccel_63d_base_v143_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    g = np.log(tot).diff(63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fund-share entropy-normalized dominance (fund share scaled by inverse entropy)
def f43oc_f43_ownership_concentration_breadth_fndnorment_21d_base_v144_signal(fndholders, undholders, prfholders, dbtholders):
    sh = _f43_share(fndholders, fndholders, undholders, prfholders, dbtholders)
    e = _f43_entropy(fndholders, undholders, prfholders, dbtholders)
    b = sh * (1.5 - e).clip(lower=-2, upper=2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration vs breadth z-spread over 252d (long-horizon crowding regime)
def f43oc_f43_ownership_concentration_breadth_crowdz_252d_base_v145_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    b = _z(percentoftotal, 252) - _z(np.log(tot.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rotation magnitude over half-year (medium-horizon mix churn)
def f43oc_f43_ownership_concentration_breadth_rotmag_126d_base_v146_signal(fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    out = None
    for part in (fndholders, undholders, prfholders, dbtholders):
        s = part / tot
        d = (s - s.shift(126)).abs()
        out = d if out is None else out + d
    b = out
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value per holder smoothed displacement (per-holder dollar deviation)
def f43oc_f43_ownership_concentration_breadth_avgvaldisp_63d_base_v147_signal(totalvalue, fndholders, undholders, prfholders, dbtholders):
    av = _f43_avg_value(totalvalue, fndholders, undholders, prfholders, dbtholders).replace(0, np.nan)
    la = np.log(av)
    b = la - la.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-share slope over 126d (creditor-base tilt regression trend)
def f43oc_f43_ownership_concentration_breadth_dbtshareslope_126d_base_v148_signal(fndholders, undholders, prfholders, dbtholders):
    sh = _f43_share(dbtholders, fndholders, undholders, prfholders, dbtholders)
    b = _slope(sh, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effective-types (inverse HHI) z over 252d (mix breadth regime)
def f43oc_f43_ownership_concentration_breadth_efftypesz_252d_base_v149_signal(fndholders, undholders, prfholders, dbtholders):
    h = _f43_hhi(fndholders, undholders, prfholders, dbtholders)
    inv = 1.0 / h.replace(0, np.nan)
    b = _z(inv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentration-breadth product slope: regression trend of pct*log(tot) over 126d
def f43oc_f43_ownership_concentration_breadth_concbreadthslope_126d_base_v150_signal(percentoftotal, fndholders, undholders, prfholders, dbtholders):
    tot = _f43_total_holders(fndholders, undholders, prfholders, dbtholders)
    prod = percentoftotal * np.log(tot.replace(0, np.nan))
    b = _slope(prod, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43oc_f43_ownership_concentration_breadth_breadthema_63d_base_v076_signal,
    f43oc_f43_ownership_concentration_breadth_breadthdisp_63d_base_v077_signal,
    f43oc_f43_ownership_concentration_breadth_breadthmom_126d_base_v078_signal,
    f43oc_f43_ownership_concentration_breadth_fndsharez2_252d_base_v079_signal,
    f43oc_f43_ownership_concentration_breadth_undsharemom_126d_base_v080_signal,
    f43oc_f43_ownership_concentration_breadth_prfsharemom_63d_base_v081_signal,
    f43oc_f43_ownership_concentration_breadth_hhiema_63d_base_v082_signal,
    f43oc_f43_ownership_concentration_breadth_hhidisp_63d_base_v083_signal,
    f43oc_f43_ownership_concentration_breadth_entropyema_63d_base_v084_signal,
    f43oc_f43_ownership_concentration_breadth_concema_63d_base_v085_signal,
    f43oc_f43_ownership_concentration_breadth_concdisp_63d_base_v086_signal,
    f43oc_f43_ownership_concentration_breadth_conctrd_126d_base_v087_signal,
    f43oc_f43_ownership_concentration_breadth_smartdumbema_63d_base_v088_signal,
    f43oc_f43_ownership_concentration_breadth_smartdumbmom_126d_base_v089_signal,
    f43oc_f43_ownership_concentration_breadth_avgvalmom_126d_base_v090_signal,
    f43oc_f43_ownership_concentration_breadth_valconcmom_126d_base_v091_signal,
    f43oc_f43_ownership_concentration_breadth_fndsharemom_21d_base_v092_signal,
    f43oc_f43_ownership_concentration_breadth_dbtsharemom_21d_base_v093_signal,
    f43oc_f43_ownership_concentration_breadth_hhitrd_21d_base_v094_signal,
    f43oc_f43_ownership_concentration_breadth_entropytrd_21d_base_v095_signal,
    f43oc_f43_ownership_concentration_breadth_fndcountz_126d_base_v096_signal,
    f43oc_f43_ownership_concentration_breadth_dbtcountmom_126d_base_v097_signal,
    f43oc_f43_ownership_concentration_breadth_prfcountz_252d_base_v098_signal,
    f43oc_f43_ownership_concentration_breadth_undcountmom_63d_base_v099_signal,
    f43oc_f43_ownership_concentration_breadth_fnddbtmom_126d_base_v100_signal,
    f43oc_f43_ownership_concentration_breadth_fndprfz_252d_base_v101_signal,
    f43oc_f43_ownership_concentration_breadth_undfndmom_63d_base_v102_signal,
    f43oc_f43_ownership_concentration_breadth_valperfndz_252d_base_v103_signal,
    f43oc_f43_ownership_concentration_breadth_valmom_126d_base_v104_signal,
    f43oc_f43_ownership_concentration_breadth_valbreadthspr_126d_base_v105_signal,
    f43oc_f43_ownership_concentration_breadth_mixgini_21d_base_v106_signal,
    f43oc_f43_ownership_concentration_breadth_fnddomgapmom_126d_base_v107_signal,
    f43oc_f43_ownership_concentration_breadth_concexcess_126d_base_v108_signal,
    f43oc_f43_ownership_concentration_breadth_concrank_252d_base_v109_signal,
    f43oc_f43_ownership_concentration_breadth_concvalz_252d_base_v110_signal,
    f43oc_f43_ownership_concentration_breadth_fndsharerank_252d_base_v111_signal,
    f43oc_f43_ownership_concentration_breadth_incomeshare_mom_126d_base_v112_signal,
    f43oc_f43_ownership_concentration_breadth_rotmag_21d_base_v113_signal,
    f43oc_f43_ownership_concentration_breadth_breadthstab_252d_base_v114_signal,
    f43oc_f43_ownership_concentration_breadth_concchurn_63d_base_v115_signal,
    f43oc_f43_ownership_concentration_breadth_dbtentcontrib_21d_base_v116_signal,
    f43oc_f43_ownership_concentration_breadth_topvsequalmom_126d_base_v117_signal,
    f43oc_f43_ownership_concentration_breadth_credeqrot_21d_base_v118_signal,
    f43oc_f43_ownership_concentration_breadth_breadthslope_63d_base_v119_signal,
    f43oc_f43_ownership_concentration_breadth_concslope_63d_base_v120_signal,
    f43oc_f43_ownership_concentration_breadth_fndshareslope_126d_base_v121_signal,
    f43oc_f43_ownership_concentration_breadth_entropyslope_126d_base_v122_signal,
    f43oc_f43_ownership_concentration_breadth_valbreadthmom_126d_base_v123_signal,
    f43oc_f43_ownership_concentration_breadth_fnddbtentmom_126d_base_v124_signal,
    f43oc_f43_ownership_concentration_breadth_smartdumbrank_504d_base_v125_signal,
    f43oc_f43_ownership_concentration_breadth_conctanh_63d_base_v126_signal,
    f43oc_f43_ownership_concentration_breadth_breadthtanh_63d_base_v127_signal,
    f43oc_f43_ownership_concentration_breadth_hhirank_252d_base_v128_signal,
    f43oc_f43_ownership_concentration_breadth_concdollar_126d_base_v129_signal,
    f43oc_f43_ownership_concentration_breadth_concsignmag_126d_base_v130_signal,
    f43oc_f43_ownership_concentration_breadth_fndshareasym_126d_base_v131_signal,
    f43oc_f43_ownership_concentration_breadth_fndhit_63d_base_v132_signal,
    f43oc_f43_ownership_concentration_breadth_incomebalmom_63d_base_v133_signal,
    f43oc_f43_ownership_concentration_breadth_concrevert_126d_base_v134_signal,
    f43oc_f43_ownership_concentration_breadth_breadthvalrank_252d_base_v135_signal,
    f43oc_f43_ownership_concentration_breadth_fndelastic_63d_base_v136_signal,
    f43oc_f43_ownership_concentration_breadth_valperfndmom_126d_base_v137_signal,
    f43oc_f43_ownership_concentration_breadth_incomecount_21d_base_v138_signal,
    f43oc_f43_ownership_concentration_breadth_incomecountmom_126d_base_v139_signal,
    f43oc_f43_ownership_concentration_breadth_equityshare_21d_base_v140_signal,
    f43oc_f43_ownership_concentration_breadth_equitysharez_252d_base_v141_signal,
    f43oc_f43_ownership_concentration_breadth_concvalcouple_63d_base_v142_signal,
    f43oc_f43_ownership_concentration_breadth_breadthaccel_63d_base_v143_signal,
    f43oc_f43_ownership_concentration_breadth_fndnorment_21d_base_v144_signal,
    f43oc_f43_ownership_concentration_breadth_crowdz_252d_base_v145_signal,
    f43oc_f43_ownership_concentration_breadth_rotmag_126d_base_v146_signal,
    f43oc_f43_ownership_concentration_breadth_avgvaldisp_63d_base_v147_signal,
    f43oc_f43_ownership_concentration_breadth_dbtshareslope_126d_base_v148_signal,
    f43oc_f43_ownership_concentration_breadth_efftypesz_252d_base_v149_signal,
    f43oc_f43_ownership_concentration_breadth_concbreadthslope_126d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_OWNERSHIP_CONCENTRATION_BREADTH_REGISTRY_076_150 = REGISTRY


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
        g = np.random.default_rng(seed)
        e = g.normal(0.0, sd, n)
        out = np.empty(n)
        acc = 0.0
        for k in range(n):
            acc = 0.85 * acc + e[k]
            out[k] = acc
        return np.exp(out)

    fndholders = pd.Series(np.maximum(_fund(101, 120.0, 0.018, 0.07).values * _jit(201, 0.045), 1.0), name="fndholders")
    undholders = pd.Series(np.maximum(_fund(102, 85.0, -0.004, 0.08).values * _jit(202, 0.060), 1.0), name="undholders")
    prfholders = pd.Series(np.maximum(_fund(103, 70.0, 0.002, 0.09).values * _jit(203, 0.070), 1.0), name="prfholders")
    dbtholders = pd.Series(np.maximum(_fund(104, 95.0, -0.001, 0.075).values * _jit(204, 0.055), 1.0), name="dbtholders")
    shrholders = pd.Series(np.maximum(_fund(105, 300.0, 0.012, 0.06).values * _jit(205, 0.030), 1.0), name="shrholders")
    percentoftotal = pd.Series(np.clip(_fund(106, 0.18, 0.003, 0.05).values * _jit(206, 0.040), 0.001, 0.95), name="percentoftotal")
    totalvalue = pd.Series(np.maximum(_fund(107, 5e8, 0.018, 0.05).values * _jit(207, 0.035), 1.0), name="totalvalue")

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

    print("OK f43_ownership_concentration_breadth_base_076_150_claude: %d features pass" % n_features)
