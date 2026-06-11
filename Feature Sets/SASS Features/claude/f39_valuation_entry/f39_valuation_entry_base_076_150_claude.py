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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


# ===== folder domain primitives (valuation entry / cheapness) =====
def _f39_cheap_z(mult, w):
    return -_z(mult, w)


def _f39_yield(num, denom):
    return num / denom.replace(0, np.nan)


def _f39_inv(mult):
    return 1.0 / mult.replace(0, np.nan)


def _f39_rng_cheap(mult, w):
    hi = _rmax(mult, w)
    lo = _rmin(mult, w)
    return (hi - mult) / (hi - lo).replace(0, np.nan)


def _f39_zscore_pctile(s, w):
    return _rank(s, w)


# ============================================================
# --- harmonic / geometric blends of inverse multiples ---
def f39ve_f39_valuation_entry_eqmult_geomyld_base_v076_signal(pe, pb, ps):
    # geometric mean of the three equity yields (balanced cheapness level)
    prod = _f39_inv(pe) * _f39_inv(pb) * _f39_inv(ps)
    b = np.sign(prod) * (prod.abs() ** (1.0 / 3.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_ev_geomyld_base_v077_signal(evebitda, evebit):
    prod = _f39_inv(evebitda) * _f39_inv(evebit)
    b = np.sign(prod) * (prod.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- earnings-yield vs ebitda-yield spread (quality of cheapness) ---
def f39ve_f39_valuation_entry_ey_vs_ebitday_base_v078_signal(pe, evebitda):
    # earnings-yield vs ebitda-yield spread, standardized (relative cheapness of equity vs EV)
    spr = _f39_inv(pe) - _f39_inv(evebitda)
    b = _z(spr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_booky_vs_salesy_base_v079_signal(pb, ps):
    b = _f39_inv(pb) - _f39_inv(ps)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- fundamental yield interactions with multiples (confirmation rank) ---
def f39ve_f39_valuation_entry_ey_pe_confz_base_v080_signal(netinc, marketcap, pe):
    # earnings yield (fundamental) z minus pe richness z -> double-confirmed cheap
    ey = _z(_f39_yield(netinc, marketcap), 252)
    pez = _z(pe, 252)
    b = ey - pez
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_by_pb_confz_base_v081_signal(equity, marketcap, pb):
    by = _z(_f39_yield(equity, marketcap), 252)
    pbz = _z(pb, 252)
    b = by - pbz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_sy_ps_confz_base_v082_signal(revenue, marketcap, ps):
    sy = _z(_f39_yield(revenue, marketcap), 252)
    psz = _z(ps, 252)
    b = sy - psz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EV yields with cross confirmation ---
def f39ve_f39_valuation_entry_fcfev_evebitda_confz_base_v083_signal(fcf, ev, evebitda):
    fy = _z(_f39_yield(fcf, ev), 252)
    ebz = _z(evebitda, 252)
    b = fy - ebz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_earnev_evebit_confz_base_v084_signal(netinc, ev, evebit):
    ey = _z(_f39_yield(netinc, ev), 252)
    ebz = _z(evebit, 252)
    b = ey - ebz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- deep-value tail counts ---
def f39ve_f39_valuation_entry_pe_tailtime_base_v085_signal(pe):
    # fraction of last 252d spent in the cheapest quintile of its 504d range
    q20 = pe.rolling(504, min_periods=126).quantile(0.20)
    incheap = (pe <= q20).astype(float)
    b = incheap.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitda_tailtime_base_v086_signal(evebitda):
    q20 = evebitda.rolling(504, min_periods=126).quantile(0.20)
    incheap = (evebitda <= q20).astype(float)
    b = incheap.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- yield level vs sector-neutralizing self-history (long z) ---
def f39ve_f39_valuation_entry_ey_longz_base_v087_signal(netinc, marketcap):
    ey = _f39_yield(netinc, marketcap)
    b = _z(ey, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fy_longz_base_v088_signal(fcf, marketcap):
    fy = _f39_yield(fcf, marketcap)
    b = _z(fy, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_by_longz_base_v089_signal(equity, marketcap):
    by = _f39_yield(equity, marketcap)
    b = _z(by, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple compression depth (current vs 1y-ago level) ---
def f39ve_f39_valuation_entry_pe_yoycomp_base_v090_signal(pe):
    # how much cheaper than a year ago (positive == de-rated == cheaper entry)
    b = (pe.shift(252) - pe) / pe.shift(252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_ps_yoycomp_base_v091_signal(ps):
    b = (ps.shift(252) - ps) / ps.shift(252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitda_yoycomp_base_v092_signal(evebitda):
    b = (evebitda.shift(252) - evebitda) / evebitda.shift(252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- yield mean-reversion magnitude (distance below long mean, only when cheap) ---
def f39ve_f39_valuation_entry_ey_cheapdepth_base_v093_signal(netinc, marketcap):
    ey = _f39_yield(netinc, marketcap)
    m = ey.rolling(252, min_periods=126).mean()
    sd = ey.rolling(252, min_periods=126).std()
    b = ((ey - m) / sd.replace(0, np.nan)).clip(lower=0)  # only the cheap (high-yield) tail
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evfcf_cheapdepth_base_v094_signal(fcf, ev):
    fy = _f39_yield(fcf, ev)
    m = fy.rolling(252, min_periods=126).mean()
    sd = fy.rolling(252, min_periods=126).std()
    b = ((fy - m) / sd.replace(0, np.nan)).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- blended cheapness across mixed metric+fundamental ranks ---
def f39ve_f39_valuation_entry_mixblend_a_base_v095_signal(pe, evebitda, fcf, marketcap):
    a = -_rank(pe, 252)
    b1 = -_rank(evebitda, 252)
    c = _rank(_f39_yield(fcf, marketcap), 504)
    b = (a + b1 + c) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_mixblend_b_base_v096_signal(pb, ps, netinc, marketcap):
    a = -_rank(pb, 252)
    b1 = -_rank(ps, 252)
    c = _rank(_f39_yield(netinc, marketcap), 504)
    b = (a + b1 + c) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EV/sales level z and rank already in file1; here use EV/sales trajectory smoothing ---
def f39ve_f39_valuation_entry_evsales_ema_base_v097_signal(ev, revenue):
    # EV/sales cheapness rank smoothed (persistent enterprise-sales cheapness)
    evs = _f39_yield(ev, revenue)
    cheap = -_rank(evs, 252)
    b = cheap.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evsales_disp_base_v098_signal(ev, revenue):
    # EV/sales displacement from its own slow EMA (acute cheapening)
    evs = _f39_yield(ev, revenue)
    b = evs.ewm(span=63, min_periods=21).mean() - evs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- yield-weighted multiple ranks (cheap AND high-yield) ---
def f39ve_f39_valuation_entry_pe_ey_signmag_base_v099_signal(pe, netinc, marketcap):
    cheap = -_z(pe, 252)
    ey = _f39_yield(netinc, marketcap)
    b = np.sign(cheap) * (cheap.abs() ** 0.5) * np.sign(ey) * (ey.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pb_by_signmag_base_v100_signal(pb, equity, marketcap):
    cheap = -_z(pb, 252)
    by = _f39_yield(equity, marketcap)
    b = np.sign(cheap) * (cheap.abs() ** 0.5) * np.sign(by) * (by.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative cheapness across equity vs enterprise multiples ---
def f39ve_f39_valuation_entry_pe_vs_evebit_base_v101_signal(pe, evebit):
    # equity richness vs enterprise richness (leverage tilt of value)
    b = -_z(pe, 252) - (-_z(evebit, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pb_vs_evebitda_base_v102_signal(pb, evebitda):
    b = -_z(pb, 252) - (-_z(evebitda, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- yield acceleration (2nd-difference style, but as a base level) ---
def f39ve_f39_valuation_entry_ey_accel_base_v103_signal(netinc, marketcap):
    ey = _f39_yield(netinc, marketcap)
    d = ey - ey.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fy_accel_base_v104_signal(fcf, marketcap):
    fy = _f39_yield(fcf, marketcap)
    d = fy - fy.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cheapness consistency (low vol of the cheapness rank) ---
def f39ve_f39_valuation_entry_pe_cheapstab_base_v105_signal(pe):
    cheap = -_rank(pe, 252)
    b = -cheap.rolling(126, min_periods=63).std()  # high == stably cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitda_cheapstab_base_v106_signal(evebitda):
    cheap = -_rank(evebitda, 252)
    b = -cheap.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite yield minus composite multiple richness ---
def f39ve_f39_valuation_entry_yldminusrich_base_v107_signal(netinc, fcf, marketcap, pe, ps):
    yld = (_z(_f39_yield(netinc, marketcap), 252) + _z(_f39_yield(fcf, marketcap), 252)) / 2.0
    rich = (_z(pe, 252) + _z(ps, 252)) / 2.0
    b = yld - rich
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- earnings-yield x fcf-yield product (quality cheapness) ---
def f39ve_f39_valuation_entry_ey_fy_prod_base_v108_signal(netinc, fcf, marketcap):
    ey = _f39_yield(netinc, marketcap)
    fy = _f39_yield(fcf, marketcap)
    b = np.sign(ey * fy) * (ey.abs() * fy.abs()) ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EV-to-fundamental ratios as cheapness levels ---
def f39ve_f39_valuation_entry_evrev_level_base_v109_signal(ev, revenue):
    # EV/revenue level inverted (cheap == high), ranked vs 252d
    evr = _f39_yield(ev, revenue)
    b = -_rank(evr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_eveq_level_base_v110_signal(ev, equity):
    eveq = _f39_yield(ev, equity)
    b = -_rank(eveq, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evfcf_level_base_v111_signal(ev, fcf):
    evf = _f39_yield(ev, fcf)
    b = -_rank(evf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- marketcap-relative fundamental scale (size-aware cheapness) ---
def f39ve_f39_valuation_entry_rev_cap_z_base_v112_signal(revenue, marketcap):
    # revenue/marketcap z (cheap on sales basis), longer window
    sy = _f39_yield(revenue, marketcap)
    b = _z(sy, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_eq_cap_z_base_v113_signal(equity, marketcap):
    by = _f39_yield(equity, marketcap)
    b = _z(by, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- blended deep-value composite ---
def f39ve_f39_valuation_entry_deepcomposite_base_v114_signal(pe, pb, ps, evebitda):
    parts = []
    for s in (pe, pb, ps, evebitda):
        q20 = s.rolling(504, min_periods=126).quantile(0.20)
        parts.append(((q20 - s).clip(lower=0) / q20.replace(0, np.nan)))
    b = sum(parts) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- earnings-yield rank spread vs sales-yield rank (margin-aware) ---
def f39ve_f39_valuation_entry_ey_sy_rankspr_base_v115_signal(netinc, revenue, marketcap):
    eyr = _rank(_f39_yield(netinc, marketcap), 504)
    syr = _rank(_f39_yield(revenue, marketcap), 504)
    b = eyr - syr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fy_by_rankspr_base_v116_signal(fcf, equity, marketcap):
    fyr = _rank(_f39_yield(fcf, marketcap), 504)
    byr = _rank(_f39_yield(equity, marketcap), 504)
    b = fyr - byr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ev multiple range cheapness at multiple windows ---
def f39ve_f39_valuation_entry_evebit_rng_252d_base_v117_signal(evebit):
    b = _f39_rng_cheap(evebit, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pe_rng_504d_base_v118_signal(pe):
    b = _f39_rng_cheap(pe, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pb_rng_504d_base_v119_signal(pb):
    b = _f39_rng_cheap(pb, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- yield curvature: convex transform of earnings yield ---
def f39ve_f39_valuation_entry_ey_convex_base_v120_signal(netinc, marketcap):
    ey = _f39_yield(netinc, marketcap)
    z = _z(ey, 252)
    b = np.sign(z) * z ** 2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evfcf_convex_base_v121_signal(fcf, ev):
    fy = _f39_yield(fcf, ev)
    z = _z(fy, 252)
    b = np.sign(z) * z ** 2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple dispersion across windows (re-rating instability) ---
def f39ve_f39_valuation_entry_pe_windisp_base_v122_signal(pe):
    z63 = -_z(pe, 63)
    z252 = -_z(pe, 252)
    b = z63 - z252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitda_windisp_base_v123_signal(evebitda):
    z63 = -_z(evebitda, 63)
    z252 = -_z(evebitda, 252)
    b = z63 - z252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- blended EV yield level (earnings+fcf on EV) ---
def f39ve_f39_valuation_entry_ev_totyld_base_v124_signal(netinc, fcf, ev):
    b = (netinc + fcf) / ev.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_ev_totyld_z_base_v125_signal(netinc, fcf, ev):
    ty = (netinc + fcf) / ev.replace(0, np.nan)
    b = _z(ty, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- equity yield vs EV yield gap (capital structure value, fcf based, ranked) ---
def f39ve_f39_valuation_entry_fcf_struct_rank_base_v126_signal(fcf, marketcap, ev):
    gap = _f39_yield(fcf, marketcap) - _f39_yield(fcf, ev)
    b = _rank(gap, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_earn_struct_rank_base_v127_signal(netinc, marketcap, ev):
    gap = _f39_yield(netinc, marketcap) - _f39_yield(netinc, ev)
    b = _rank(gap, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cheapness momentum (cheapness rank now vs a quarter ago) ---
def f39ve_f39_valuation_entry_pe_cheapmom_base_v128_signal(pe):
    cheap = -_rank(pe, 252)
    b = cheap - cheap.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_ps_cheapmom_base_v129_signal(ps):
    cheap = -_rank(ps, 252)
    b = cheap - cheap.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitda_cheapmom_base_v130_signal(evebitda):
    cheap = -_rank(evebitda, 252)
    b = cheap - cheap.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- yield level scaled by yield stability (Sharpe-like cheapness) ---
def f39ve_f39_valuation_entry_ey_sharpe_base_v131_signal(netinc, marketcap):
    ey = _f39_yield(netinc, marketcap)
    m = ey.rolling(252, min_periods=126).mean()
    sd = ey.rolling(252, min_periods=126).std()
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fy_sharpe_base_v132_signal(fcf, marketcap):
    fy = _f39_yield(fcf, marketcap)
    m = fy.rolling(252, min_periods=126).mean()
    sd = fy.rolling(252, min_periods=126).std()
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- earnings-vs-book yield blend (Graham-style) ---
def f39ve_f39_valuation_entry_graham_base_v133_signal(pe, pb):
    # Graham number proxy: 1/(pe*pb) high == cheap on both earnings and book
    gp = 1.0 / (pe * pb).replace(0, np.nan)
    b = _rank(gp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_graham_z_base_v134_signal(pe, pb):
    gp = 1.0 / (pe * pb).replace(0, np.nan)
    b = _z(gp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- enterprise cheapness composite (EV multiples + EV yields) ---
def f39ve_f39_valuation_entry_ev_cheapcomposite_base_v135_signal(evebitda, evebit, fcf, ev):
    m = (-_rank(evebitda, 252) - _rank(evebit, 252)) / 2.0
    y = _rank(_f39_yield(fcf, ev), 504)
    b = m + y
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- value trap guard: cheap but yield deteriorating ---
def f39ve_f39_valuation_entry_valuetrap_base_v136_signal(pe, netinc, marketcap):
    cheap = -_rank(pe, 252)
    ey = _f39_yield(netinc, marketcap)
    eychg = ey - ey.shift(63)
    b = cheap * np.sign(eychg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fcftrap_base_v137_signal(ps, fcf, marketcap):
    cheap = -_rank(ps, 252)
    fy = _f39_yield(fcf, marketcap)
    fychg = fy - fy.shift(63)
    b = cheap * np.sign(fychg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple-implied vs reported fundamental drift ---
def f39ve_f39_valuation_entry_pe_impl_drift_base_v138_signal(pe, marketcap, netinc):
    # implied earnings marketcap/pe vs reported netinc, ratio drift
    impl = _f39_yield(marketcap, pe)
    r = impl / netinc.replace(0, np.nan)
    b = r - r.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_ps_impl_drift_base_v139_signal(ps, marketcap, revenue):
    impl = _f39_yield(marketcap, ps)
    r = impl / revenue.replace(0, np.nan)
    b = r - r.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- yield breadth: how many of {ey,fy,by,sy} are above their median ---
def f39ve_f39_valuation_entry_yieldbreadth_base_v140_signal(netinc, fcf, equity, revenue, marketcap):
    # disagreement across the four marketcap-yield cheapness z-scores (cross-yield dispersion)
    ys = []
    for num in (netinc, fcf, equity, revenue):
        y = _f39_yield(num, marketcap)
        ys.append(_z(y, 252))
    b = pd.concat(ys, axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- enterprise yield breadth ---
def f39ve_f39_valuation_entry_ev_yieldbreadth_base_v141_signal(netinc, fcf, revenue, ev):
    # cross-EV-yield dispersion: disagreement across earnings/fcf/sales yields on EV
    ys = []
    for num in (netinc, fcf, revenue):
        y = _f39_yield(num, ev)
        ys.append(_z(y, 252))
    b = pd.concat(ys, axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- log-spread between equity and enterprise valuation ---
def f39ve_f39_valuation_entry_eq_ev_logspr_base_v142_signal(marketcap, ev):
    # log(ev/marketcap) = leverage premium baked into EV; ranked (low == cheap equity)
    lev = np.log(ev.replace(0, np.nan) / marketcap.replace(0, np.nan))
    b = -_rank(lev, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- earnings yield minus its EV-implied counterpart, smoothed ---
def f39ve_f39_valuation_entry_ey_smooth_base_v143_signal(netinc, marketcap):
    ey = _f39_yield(netinc, marketcap)
    b = ey.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fy_smooth_base_v144_signal(fcf, marketcap):
    fy = _f39_yield(fcf, marketcap)
    b = fy.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cheapness vs own 5yr extreme (multi-year deep value) ---
def f39ve_f39_valuation_entry_pe_5yrcheap_base_v145_signal(pe):
    lo = _rmin(pe, 1260)
    hi = _rmax(pe, 1260)
    b = (hi - pe) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitda_5yrcheap_base_v146_signal(evebitda):
    lo = _rmin(evebitda, 1260)
    hi = _rmax(evebitda, 1260)
    b = (hi - evebitda) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- yield level percentile vs 5yr history ---
def f39ve_f39_valuation_entry_ey_5yrrank_base_v147_signal(netinc, marketcap):
    ey = _f39_yield(netinc, marketcap)
    b = _rank(ey, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fy_5yrrank_base_v148_signal(fcf, marketcap):
    # fcf-yield deviation from its 5yr median scaled by 5yr IQR (robust deep-value)
    fy = _f39_yield(fcf, marketcap)
    med = fy.rolling(1260, min_periods=252).median()
    q75 = fy.rolling(1260, min_periods=252).quantile(0.75)
    q25 = fy.rolling(1260, min_periods=252).quantile(0.25)
    b = (fy - med) / (q75 - q25).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- master enterprise-vs-equity value tilt ---
def f39ve_f39_valuation_entry_value_tilt_base_v149_signal(pe, evebitda, netinc, fcf, marketcap, ev):
    eqval = (-_rank(pe, 252) + _rank(_f39_yield(netinc, marketcap), 504)) / 2.0
    evval = (-_rank(evebitda, 252) + _rank(_f39_yield(fcf, ev), 504)) / 2.0
    b = eqval - evval
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- grand cheapness z composite (all multiples z + all yields z) ---
def f39ve_f39_valuation_entry_grandz_base_v150_signal(pe, pb, ps, evebitda, evebit,
                                                       netinc, fcf, equity, revenue, marketcap):
    mz = (-_z(pe, 252) - _z(pb, 252) - _z(ps, 252)
          - _z(evebitda, 252) - _z(evebit, 252)) / 5.0
    yz = (_z(_f39_yield(netinc, marketcap), 252)
          + _z(_f39_yield(fcf, marketcap), 252)
          + _z(_f39_yield(equity, marketcap), 252)
          + _z(_f39_yield(revenue, marketcap), 252)) / 4.0
    b = mz + yz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39ve_f39_valuation_entry_eqmult_geomyld_base_v076_signal,
    f39ve_f39_valuation_entry_ev_geomyld_base_v077_signal,
    f39ve_f39_valuation_entry_ey_vs_ebitday_base_v078_signal,
    f39ve_f39_valuation_entry_booky_vs_salesy_base_v079_signal,
    f39ve_f39_valuation_entry_ey_pe_confz_base_v080_signal,
    f39ve_f39_valuation_entry_by_pb_confz_base_v081_signal,
    f39ve_f39_valuation_entry_sy_ps_confz_base_v082_signal,
    f39ve_f39_valuation_entry_fcfev_evebitda_confz_base_v083_signal,
    f39ve_f39_valuation_entry_earnev_evebit_confz_base_v084_signal,
    f39ve_f39_valuation_entry_pe_tailtime_base_v085_signal,
    f39ve_f39_valuation_entry_evebitda_tailtime_base_v086_signal,
    f39ve_f39_valuation_entry_ey_longz_base_v087_signal,
    f39ve_f39_valuation_entry_fy_longz_base_v088_signal,
    f39ve_f39_valuation_entry_by_longz_base_v089_signal,
    f39ve_f39_valuation_entry_pe_yoycomp_base_v090_signal,
    f39ve_f39_valuation_entry_ps_yoycomp_base_v091_signal,
    f39ve_f39_valuation_entry_evebitda_yoycomp_base_v092_signal,
    f39ve_f39_valuation_entry_ey_cheapdepth_base_v093_signal,
    f39ve_f39_valuation_entry_evfcf_cheapdepth_base_v094_signal,
    f39ve_f39_valuation_entry_mixblend_a_base_v095_signal,
    f39ve_f39_valuation_entry_mixblend_b_base_v096_signal,
    f39ve_f39_valuation_entry_evsales_ema_base_v097_signal,
    f39ve_f39_valuation_entry_evsales_disp_base_v098_signal,
    f39ve_f39_valuation_entry_pe_ey_signmag_base_v099_signal,
    f39ve_f39_valuation_entry_pb_by_signmag_base_v100_signal,
    f39ve_f39_valuation_entry_pe_vs_evebit_base_v101_signal,
    f39ve_f39_valuation_entry_pb_vs_evebitda_base_v102_signal,
    f39ve_f39_valuation_entry_ey_accel_base_v103_signal,
    f39ve_f39_valuation_entry_fy_accel_base_v104_signal,
    f39ve_f39_valuation_entry_pe_cheapstab_base_v105_signal,
    f39ve_f39_valuation_entry_evebitda_cheapstab_base_v106_signal,
    f39ve_f39_valuation_entry_yldminusrich_base_v107_signal,
    f39ve_f39_valuation_entry_ey_fy_prod_base_v108_signal,
    f39ve_f39_valuation_entry_evrev_level_base_v109_signal,
    f39ve_f39_valuation_entry_eveq_level_base_v110_signal,
    f39ve_f39_valuation_entry_evfcf_level_base_v111_signal,
    f39ve_f39_valuation_entry_rev_cap_z_base_v112_signal,
    f39ve_f39_valuation_entry_eq_cap_z_base_v113_signal,
    f39ve_f39_valuation_entry_deepcomposite_base_v114_signal,
    f39ve_f39_valuation_entry_ey_sy_rankspr_base_v115_signal,
    f39ve_f39_valuation_entry_fy_by_rankspr_base_v116_signal,
    f39ve_f39_valuation_entry_evebit_rng_252d_base_v117_signal,
    f39ve_f39_valuation_entry_pe_rng_504d_base_v118_signal,
    f39ve_f39_valuation_entry_pb_rng_504d_base_v119_signal,
    f39ve_f39_valuation_entry_ey_convex_base_v120_signal,
    f39ve_f39_valuation_entry_evfcf_convex_base_v121_signal,
    f39ve_f39_valuation_entry_pe_windisp_base_v122_signal,
    f39ve_f39_valuation_entry_evebitda_windisp_base_v123_signal,
    f39ve_f39_valuation_entry_ev_totyld_base_v124_signal,
    f39ve_f39_valuation_entry_ev_totyld_z_base_v125_signal,
    f39ve_f39_valuation_entry_fcf_struct_rank_base_v126_signal,
    f39ve_f39_valuation_entry_earn_struct_rank_base_v127_signal,
    f39ve_f39_valuation_entry_pe_cheapmom_base_v128_signal,
    f39ve_f39_valuation_entry_ps_cheapmom_base_v129_signal,
    f39ve_f39_valuation_entry_evebitda_cheapmom_base_v130_signal,
    f39ve_f39_valuation_entry_ey_sharpe_base_v131_signal,
    f39ve_f39_valuation_entry_fy_sharpe_base_v132_signal,
    f39ve_f39_valuation_entry_graham_base_v133_signal,
    f39ve_f39_valuation_entry_graham_z_base_v134_signal,
    f39ve_f39_valuation_entry_ev_cheapcomposite_base_v135_signal,
    f39ve_f39_valuation_entry_valuetrap_base_v136_signal,
    f39ve_f39_valuation_entry_fcftrap_base_v137_signal,
    f39ve_f39_valuation_entry_pe_impl_drift_base_v138_signal,
    f39ve_f39_valuation_entry_ps_impl_drift_base_v139_signal,
    f39ve_f39_valuation_entry_yieldbreadth_base_v140_signal,
    f39ve_f39_valuation_entry_ev_yieldbreadth_base_v141_signal,
    f39ve_f39_valuation_entry_eq_ev_logspr_base_v142_signal,
    f39ve_f39_valuation_entry_ey_smooth_base_v143_signal,
    f39ve_f39_valuation_entry_fy_smooth_base_v144_signal,
    f39ve_f39_valuation_entry_pe_5yrcheap_base_v145_signal,
    f39ve_f39_valuation_entry_evebitda_5yrcheap_base_v146_signal,
    f39ve_f39_valuation_entry_ey_5yrrank_base_v147_signal,
    f39ve_f39_valuation_entry_fy_5yrrank_base_v148_signal,
    f39ve_f39_valuation_entry_value_tilt_base_v149_signal,
    f39ve_f39_valuation_entry_grandz_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_VALUATION_ENTRY_REGISTRY_076_150 = REGISTRY


def _build_inputs():
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.3
        return pd.Series(s, name=None)

    pe = _fund(1, base=18.0, drift=0.01, vol=0.06).rename("pe")
    pb = _fund(2, base=3.0, drift=0.01, vol=0.07).rename("pb")
    ps = _fund(3, base=4.0, drift=0.01, vol=0.06).rename("ps")
    evebit = _fund(4, base=16.0, drift=0.01, vol=0.06).rename("evebit")
    evebitda = _fund(5, base=11.0, drift=0.01, vol=0.06).rename("evebitda")
    marketcap = _fund(6, base=5e9, drift=0.02, vol=0.05).rename("marketcap")
    ev = _fund(7, base=6e9, drift=0.02, vol=0.05).rename("ev")
    revenue = _fund(8, base=2e9, drift=0.02, vol=0.05).rename("revenue")
    equity = _fund(9, base=3e9, drift=0.02, vol=0.05).rename("equity")
    netinc = _fund(10, base=4e8, drift=0.015, vol=0.08, allow_neg=True).rename("netinc")
    fcf = _fund(11, base=3.5e8, drift=0.015, vol=0.09, allow_neg=True).rename("fcf")

    return {"pe": pe, "pb": pb, "ps": ps, "ev": ev, "evebit": evebit,
            "evebitda": evebitda, "marketcap": marketcap, "fcf": fcf,
            "netinc": netinc, "revenue": revenue, "equity": equity}


if __name__ == "__main__":
    cols = _build_inputs()

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

    print("OK f39_valuation_entry_base_076_150_claude: %d features pass" % n_features)
