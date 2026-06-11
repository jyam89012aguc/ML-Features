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
# Cheapness of a positive multiple (pe/pb/ps/evebitda...): low multiple == cheap.
# We map cheapness so that "cheaper" tends to score HIGHER (z of the inverse, or -z).
def _f39_cheap_z(mult, w):
    # negative z of a multiple -> high when the multiple is unusually low (cheap)
    return -_z(mult, w)


def _f39_yield(num, denom):
    # earnings/fcf/book yield: positive flow over market value
    return num / denom.replace(0, np.nan)


def _f39_inv(mult):
    # inverse multiple = a yield-like cheapness level (e.g. 1/pe ~ earnings yield)
    return 1.0 / mult.replace(0, np.nan)


def _f39_rng_cheap(mult, w):
    # where the current multiple sits in its own range, inverted so cheap == high
    hi = _rmax(mult, w)
    lo = _rmin(mult, w)
    return (hi - mult) / (hi - lo).replace(0, np.nan)


def _f39_spread(a, b):
    return a - b


# ============================================================
# --- cheapness z-scores of the core multiples (252d) ---
def f39ve_f39_valuation_entry_pez_252d_base_v001_signal(pe):
    b = _f39_cheap_z(pe, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pbz_252d_base_v002_signal(pb):
    b = _f39_cheap_z(pb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_psz_252d_base_v003_signal(ps):
    b = _f39_cheap_z(ps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitdaz_252d_base_v004_signal(evebitda):
    b = _f39_cheap_z(evebitda, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitz_252d_base_v005_signal(evebit):
    b = _f39_cheap_z(evebit, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- inverse-multiple cheapness levels (yield-like) ---
def f39ve_f39_valuation_entry_earnyld_pe_base_v006_signal(pe):
    # 1/pe = earnings yield, percentile-ranked vs its own 504d history
    ey = _f39_inv(pe)
    b = _rank(ey, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_bookyld_pb_base_v007_signal(pb):
    # 1/pb = book yield level
    by = _f39_inv(pb)
    b = by
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_salesyld_ps_base_v008_signal(ps):
    # sales-yield acceleration: change in 1/ps over a quarter (cheapening velocity)
    sy = _f39_inv(ps)
    b = sy - sy.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_ebitdayld_base_v009_signal(evebitda):
    # 1/evebitda = ebitda yield on enterprise value
    ey = _f39_inv(evebitda)
    b = ey
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_ebityld_base_v010_signal(evebit):
    ey = _f39_inv(evebit)
    b = _z(ey, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- fundamental yields on market cap ---
def f39ve_f39_valuation_entry_earnyld_mc_base_v011_signal(netinc, marketcap):
    # netinc / marketcap = earnings yield from fundamentals
    b = _f39_yield(netinc, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fcfyld_mc_base_v012_signal(fcf, marketcap):
    # fcf / marketcap = free-cash-flow yield
    b = _f39_yield(fcf, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_bookyld_mc_base_v013_signal(equity, marketcap):
    # equity / marketcap = book yield (inverse P/B from fundamentals)
    b = _f39_yield(equity, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_salesyld_mc_base_v014_signal(revenue, marketcap):
    # revenue / marketcap = sales yield
    b = _f39_yield(revenue, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EV-based cheapness ---
def f39ve_f39_valuation_entry_evsales_base_v015_signal(ev, revenue):
    # EV/sales, inverted to a sales-on-EV yield (cheap == high)
    evs = _f39_yield(ev, revenue)
    b = _f39_inv(evs)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evfcf_base_v016_signal(ev, fcf):
    # FCF / EV = enterprise free-cash-flow yield
    b = _f39_yield(fcf, ev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evearn_base_v017_signal(ev, netinc):
    # netinc / ev = earnings on enterprise value
    b = _f39_yield(netinc, ev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evbook_base_v018_signal(ev, equity):
    # equity / ev = book on enterprise value, z-scored
    raw = _f39_yield(equity, ev)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- blended cheapness ranks ---
def f39ve_f39_valuation_entry_blend_pe_pb_ps_base_v019_signal(pe, pb, ps):
    # average cheapness rank across pe/pb/ps (cheap == high)
    rpe = -_rank(pe, 252)
    rpb = -_rank(pb, 252)
    rps = -_rank(ps, 252)
    b = (rpe + rpb + rps) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_blend_ev_base_v020_signal(evebitda, evebit):
    # blended EV-multiple cheapness rank
    r1 = -_rank(evebitda, 252)
    r2 = -_rank(evebit, 252)
    b = (r1 + r2) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_blend_all5_base_v021_signal(pe, pb, ps, evebitda, evebit):
    # broad value composite across all five core multiples
    parts = [-_rank(pe, 252), -_rank(pb, 252), -_rank(ps, 252),
             -_rank(evebitda, 252), -_rank(evebit, 252)]
    b = sum(parts) / 5.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- spreads between cheapness signals (relative value) ---
def f39ve_f39_valuation_entry_spr_pe_ps_base_v022_signal(pe, ps):
    # earnings-yield minus sales-yield (margin-implied relative cheapness)
    b = _f39_spread(_f39_inv(pe), _f39_inv(ps))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_spr_pb_evebitda_base_v023_signal(pb, evebitda):
    # book yield minus ebitda yield
    b = _f39_spread(_f39_inv(pb), _f39_inv(evebitda))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_spr_evebit_evebitda_base_v024_signal(evebit, evebitda):
    # ebit-vs-ebitda multiple spread (D&A burden in valuation)
    b = _f39_spread(_f39_inv(evebitda), _f39_inv(evebit))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- range-position cheapness (own multiple history) ---
def f39ve_f39_valuation_entry_perng_252d_base_v025_signal(pe):
    b = _f39_rng_cheap(pe, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pbrng_252d_base_v026_signal(pb):
    # book-yield (1/pb) momentum: change in book yield over a month (re-rating speed)
    by = _f39_inv(pb)
    b = by - by.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_psrng_504d_base_v027_signal(ps):
    b = _f39_rng_cheap(ps, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitdarng_504d_base_v028_signal(evebitda):
    b = _f39_rng_cheap(evebitda, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- yields combined / interactions ---
def f39ve_f39_valuation_entry_totyld_mc_base_v029_signal(netinc, fcf, marketcap):
    # combined earnings + fcf yield on marketcap
    b = (netinc + fcf) / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_earnfcf_gap_base_v030_signal(netinc, fcf, marketcap):
    # quality of earnings yield: fcf-yield minus earnings-yield
    b = (fcf - netinc) / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_ey_mc_z_base_v031_signal(netinc, marketcap):
    # earnings yield z-scored vs own 252d history (cheapening detector)
    ey = _f39_yield(netinc, marketcap)
    b = _z(ey, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fcfy_mc_z_base_v032_signal(fcf, marketcap):
    fy = _f39_yield(fcf, marketcap)
    b = _z(fy, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_booky_mc_rank_base_v033_signal(equity, marketcap):
    by = _f39_yield(equity, marketcap)
    b = _rank(by, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_salesy_mc_rank_base_v034_signal(revenue, marketcap):
    sy = _f39_yield(revenue, marketcap)
    b = _rank(sy, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EV/sales & EV/FCF transforms ---
def f39ve_f39_valuation_entry_evsales_z_base_v035_signal(ev, revenue):
    evs = _f39_yield(ev, revenue)
    b = -_z(evs, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evsales_rank_base_v036_signal(ev, revenue):
    evs = _f39_yield(ev, revenue)
    b = -_rank(evs, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evfcf_z_base_v037_signal(ev, fcf):
    evf = _f39_yield(ev, fcf)
    b = -_z(evf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evfcf_rank_base_v038_signal(ev, fcf):
    fy = _f39_yield(fcf, ev)
    b = _rank(fy, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multiple-vs-marketcap consistency (metrics vs raw cap) ---
def f39ve_f39_valuation_entry_pe_impl_earn_base_v039_signal(pe, marketcap):
    # implied earnings level marketcap/pe, growth of that implied earnings stream
    impl = _f39_yield(marketcap, pe)
    b = np.log(impl.replace(0, np.nan) / impl.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_ps_impl_sales_base_v040_signal(ps, marketcap, revenue):
    # cross-check: marketcap/ps (implied sales) vs reported revenue
    impl_sales = _f39_yield(marketcap, ps)
    b = _z(impl_sales / revenue.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pb_impl_book_base_v041_signal(pb, marketcap, equity):
    # marketcap/pb (implied book) vs reported equity
    impl_book = _f39_yield(marketcap, pb)
    b = _z(impl_book / equity.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite yield ranks ---
def f39ve_f39_valuation_entry_yieldblend_base_v042_signal(netinc, fcf, equity, marketcap):
    # blended yield composite: earnings + fcf + book, each ranked then averaged
    ey = _rank(_f39_yield(netinc, marketcap), 504)
    fy = _rank(_f39_yield(fcf, marketcap), 504)
    by = _rank(_f39_yield(equity, marketcap), 504)
    b = (ey + fy + by) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_ev_yieldblend_base_v043_signal(netinc, fcf, ev):
    # EV-based yield composite
    ey = _rank(_f39_yield(netinc, ev), 504)
    fy = _rank(_f39_yield(fcf, ev), 504)
    b = (ey + fy) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cheapness vs the cross-section of multiples (dispersion / agreement) ---
def f39ve_f39_valuation_entry_multdisp_base_v044_signal(pe, pb, ps):
    # disagreement across cheapness ranks: low dispersion == multiples agree
    rpe = -_rank(pe, 252)
    rpb = -_rank(pb, 252)
    rps = -_rank(ps, 252)
    stacked = pd.concat([rpe, rpb, rps], axis=1)
    b = stacked.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_multmin_base_v045_signal(pe, pb, ps, evebitda):
    # cheapest of the multiples (max cheapness rank across the set)
    parts = pd.concat([-_rank(pe, 252), -_rank(pb, 252),
                       -_rank(ps, 252), -_rank(evebitda, 252)], axis=1)
    b = parts.max(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_multworst_base_v046_signal(pe, pb, ps, evebitda):
    # least-cheap multiple (min cheapness rank) -> richness anchor
    parts = pd.concat([-_rank(pe, 252), -_rank(pb, 252),
                       -_rank(ps, 252), -_rank(evebitda, 252)], axis=1)
    b = parts.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- earnings yield vs ev-yield gap (capital structure value) ---
def f39ve_f39_valuation_entry_capstruct_gap_base_v047_signal(netinc, marketcap, ev):
    # earnings yield on equity minus on EV (leverage-driven value gap)
    eye = _f39_yield(netinc, marketcap)
    eyv = _f39_yield(netinc, ev)
    b = eye - eyv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fcf_capstruct_gap_base_v048_signal(fcf, marketcap, ev):
    fye = _f39_yield(fcf, marketcap)
    fyv = _f39_yield(fcf, ev)
    b = fye - fyv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- normalized multiple levels (sign x magnitude / squashing) ---
def f39ve_f39_valuation_entry_pe_logcheap_base_v049_signal(pe):
    # log-multiple centered on its 252d median, negated so cheap == high
    med = pe.rolling(252, min_periods=126).median()
    b = -(np.log(pe.replace(0, np.nan)) - np.log(med.replace(0, np.nan)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_ps_logcheap_base_v050_signal(ps):
    med = ps.rolling(252, min_periods=126).median()
    b = -(np.log(ps.replace(0, np.nan)) - np.log(med.replace(0, np.nan)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitda_logcheap_base_v051_signal(evebitda):
    med = evebitda.rolling(252, min_periods=126).median()
    b = -(np.log(evebitda.replace(0, np.nan)) - np.log(med.replace(0, np.nan)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pe_tanhcheap_base_v052_signal(pe):
    # bounded earnings-yield surprise: tanh of the standardized change in 1/pe
    ey = _f39_inv(pe)
    chg = ey - ey.shift(21)
    z = _z(chg, 126)
    b = np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitda_tanhcheap_base_v053_signal(evebitda):
    z = _f39_cheap_z(evebitda, 252)
    b = np.tanh(z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- yield magnitudes scaled by cross-multiple confirmation ---
def f39ve_f39_valuation_entry_ey_conf_base_v054_signal(netinc, marketcap, pe):
    # earnings yield confirmed by a cheap pe rank
    ey = _f39_yield(netinc, marketcap)
    conf = -_rank(pe, 252) + 0.5  # 0..1, 1 == cheapest
    b = ey * conf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fy_conf_base_v055_signal(fcf, marketcap, ps):
    fy = _f39_yield(fcf, marketcap)
    conf = -_rank(ps, 252) + 0.5
    b = fy * conf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- 126d (shorter) cheapness z for diversity ---
def f39ve_f39_valuation_entry_pez_126d_base_v056_signal(pe):
    b = _f39_cheap_z(pe, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pbz_126d_base_v057_signal(pb):
    b = _f39_cheap_z(pb, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_psz_126d_base_v058_signal(ps):
    b = _f39_cheap_z(ps, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- yield-on-EV with sales (sales power vs enterprise value) ---
def f39ve_f39_valuation_entry_salesev_yld_base_v059_signal(revenue, ev):
    # sales-on-EV yield momentum: change over a quarter (enterprise cheapening velocity)
    sy = _f39_yield(revenue, ev)
    b = sy - sy.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_salesev_z_base_v060_signal(revenue, ev):
    # sales-on-EV yield mean-reversion gap (level minus its 252d mean)
    sy = _f39_yield(revenue, ev)
    b = sy - sy.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite cheapness x yield (level + relative) ---
def f39ve_f39_valuation_entry_pe_x_ey_base_v061_signal(pe, netinc, marketcap):
    cheap = -_rank(pe, 252)
    ey = _rank(_f39_yield(netinc, marketcap), 504)
    b = cheap + ey
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pb_x_booky_base_v062_signal(pb, equity, marketcap):
    cheap = -_rank(pb, 252)
    by = _rank(_f39_yield(equity, marketcap), 504)
    b = cheap + by
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitda_x_fcfy_base_v063_signal(evebitda, fcf, ev):
    cheap = -_rank(evebitda, 252)
    fy = _rank(_f39_yield(fcf, ev), 504)
    b = cheap + fy
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- richness flags as continuous depth (how far above median) ---
def f39ve_f39_valuation_entry_pe_belowmed_base_v064_signal(pe):
    # fraction of the last year the pe traded below its trailing median (persistent cheapness)
    med = pe.rolling(252, min_periods=126).median()
    cheap = (pe < med).astype(float)
    b = cheap.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebit_belowmed_base_v065_signal(evebit):
    med = evebit.rolling(252, min_periods=126).median()
    b = (med - evebit) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- yield spreads across denominators (equity vs ev value) ---
def f39ve_f39_valuation_entry_book_eqev_spr_base_v066_signal(equity, marketcap, ev):
    # net-debt-to-book leverage proxy from valuation: (ev-marketcap)/equity, cheap-debt entry
    netdebt = ev - marketcap
    b = -_z(netdebt / equity.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_sales_eqev_spr_base_v067_signal(revenue, marketcap, ev):
    # equity share of enterprise value scaled by sales-on-EV (low-leverage cheap sales)
    eqshare = marketcap / ev.replace(0, np.nan)
    salesev = revenue / ev.replace(0, np.nan)
    b = _rank(eqshare * salesev, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- blended ev-multiple inverse mean (cheapness level) ---
def f39ve_f39_valuation_entry_ev_invmean_base_v068_signal(evebitda, evebit):
    b = (_f39_inv(evebitda) + _f39_inv(evebit)) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_eqmult_invmean_base_v069_signal(pe, pb, ps):
    b = (_f39_inv(pe) + _f39_inv(pb) + _f39_inv(ps)) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- deep-value extremity (how far into the cheap tail) ---
def f39ve_f39_valuation_entry_pe_deepval_base_v070_signal(pe):
    # distance below the 504d 20th percentile (deep cheapness)
    q20 = pe.rolling(504, min_periods=126).quantile(0.20)
    b = (q20 - pe).clip(lower=0) / q20.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_ps_deepval_base_v071_signal(ps):
    q20 = ps.rolling(504, min_periods=126).quantile(0.20)
    b = (q20 - ps).clip(lower=0) / q20.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitda_deepval_base_v072_signal(evebitda):
    q20 = evebitda.rolling(504, min_periods=126).quantile(0.20)
    b = (q20 - evebitda).clip(lower=0) / q20.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- yield level vs its long mean (mean-reversion entry) ---
def f39ve_f39_valuation_entry_ey_revert_base_v073_signal(netinc, marketcap):
    ey = _f39_yield(netinc, marketcap)
    b = ey - ey.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fy_revert_base_v074_signal(fcf, marketcap):
    fy = _f39_yield(fcf, marketcap)
    b = fy - fy.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_grandblend_base_v075_signal(pe, pb, ps, evebitda, netinc, fcf, equity, marketcap):
    # master entry score: multiple cheapness ranks + fundamental yield ranks
    mult = (-_rank(pe, 252) - _rank(pb, 252) - _rank(ps, 252) - _rank(evebitda, 252)) / 4.0
    yld = (_rank(_f39_yield(netinc, marketcap), 504)
           + _rank(_f39_yield(fcf, marketcap), 504)
           + _rank(_f39_yield(equity, marketcap), 504)) / 3.0
    b = mult + yld
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39ve_f39_valuation_entry_pez_252d_base_v001_signal,
    f39ve_f39_valuation_entry_pbz_252d_base_v002_signal,
    f39ve_f39_valuation_entry_psz_252d_base_v003_signal,
    f39ve_f39_valuation_entry_evebitdaz_252d_base_v004_signal,
    f39ve_f39_valuation_entry_evebitz_252d_base_v005_signal,
    f39ve_f39_valuation_entry_earnyld_pe_base_v006_signal,
    f39ve_f39_valuation_entry_bookyld_pb_base_v007_signal,
    f39ve_f39_valuation_entry_salesyld_ps_base_v008_signal,
    f39ve_f39_valuation_entry_ebitdayld_base_v009_signal,
    f39ve_f39_valuation_entry_ebityld_base_v010_signal,
    f39ve_f39_valuation_entry_earnyld_mc_base_v011_signal,
    f39ve_f39_valuation_entry_fcfyld_mc_base_v012_signal,
    f39ve_f39_valuation_entry_bookyld_mc_base_v013_signal,
    f39ve_f39_valuation_entry_salesyld_mc_base_v014_signal,
    f39ve_f39_valuation_entry_evsales_base_v015_signal,
    f39ve_f39_valuation_entry_evfcf_base_v016_signal,
    f39ve_f39_valuation_entry_evearn_base_v017_signal,
    f39ve_f39_valuation_entry_evbook_base_v018_signal,
    f39ve_f39_valuation_entry_blend_pe_pb_ps_base_v019_signal,
    f39ve_f39_valuation_entry_blend_ev_base_v020_signal,
    f39ve_f39_valuation_entry_blend_all5_base_v021_signal,
    f39ve_f39_valuation_entry_spr_pe_ps_base_v022_signal,
    f39ve_f39_valuation_entry_spr_pb_evebitda_base_v023_signal,
    f39ve_f39_valuation_entry_spr_evebit_evebitda_base_v024_signal,
    f39ve_f39_valuation_entry_perng_252d_base_v025_signal,
    f39ve_f39_valuation_entry_pbrng_252d_base_v026_signal,
    f39ve_f39_valuation_entry_psrng_504d_base_v027_signal,
    f39ve_f39_valuation_entry_evebitdarng_504d_base_v028_signal,
    f39ve_f39_valuation_entry_totyld_mc_base_v029_signal,
    f39ve_f39_valuation_entry_earnfcf_gap_base_v030_signal,
    f39ve_f39_valuation_entry_ey_mc_z_base_v031_signal,
    f39ve_f39_valuation_entry_fcfy_mc_z_base_v032_signal,
    f39ve_f39_valuation_entry_booky_mc_rank_base_v033_signal,
    f39ve_f39_valuation_entry_salesy_mc_rank_base_v034_signal,
    f39ve_f39_valuation_entry_evsales_z_base_v035_signal,
    f39ve_f39_valuation_entry_evsales_rank_base_v036_signal,
    f39ve_f39_valuation_entry_evfcf_z_base_v037_signal,
    f39ve_f39_valuation_entry_evfcf_rank_base_v038_signal,
    f39ve_f39_valuation_entry_pe_impl_earn_base_v039_signal,
    f39ve_f39_valuation_entry_ps_impl_sales_base_v040_signal,
    f39ve_f39_valuation_entry_pb_impl_book_base_v041_signal,
    f39ve_f39_valuation_entry_yieldblend_base_v042_signal,
    f39ve_f39_valuation_entry_ev_yieldblend_base_v043_signal,
    f39ve_f39_valuation_entry_multdisp_base_v044_signal,
    f39ve_f39_valuation_entry_multmin_base_v045_signal,
    f39ve_f39_valuation_entry_multworst_base_v046_signal,
    f39ve_f39_valuation_entry_capstruct_gap_base_v047_signal,
    f39ve_f39_valuation_entry_fcf_capstruct_gap_base_v048_signal,
    f39ve_f39_valuation_entry_pe_logcheap_base_v049_signal,
    f39ve_f39_valuation_entry_ps_logcheap_base_v050_signal,
    f39ve_f39_valuation_entry_evebitda_logcheap_base_v051_signal,
    f39ve_f39_valuation_entry_pe_tanhcheap_base_v052_signal,
    f39ve_f39_valuation_entry_evebitda_tanhcheap_base_v053_signal,
    f39ve_f39_valuation_entry_ey_conf_base_v054_signal,
    f39ve_f39_valuation_entry_fy_conf_base_v055_signal,
    f39ve_f39_valuation_entry_pez_126d_base_v056_signal,
    f39ve_f39_valuation_entry_pbz_126d_base_v057_signal,
    f39ve_f39_valuation_entry_psz_126d_base_v058_signal,
    f39ve_f39_valuation_entry_salesev_yld_base_v059_signal,
    f39ve_f39_valuation_entry_salesev_z_base_v060_signal,
    f39ve_f39_valuation_entry_pe_x_ey_base_v061_signal,
    f39ve_f39_valuation_entry_pb_x_booky_base_v062_signal,
    f39ve_f39_valuation_entry_evebitda_x_fcfy_base_v063_signal,
    f39ve_f39_valuation_entry_pe_belowmed_base_v064_signal,
    f39ve_f39_valuation_entry_evebit_belowmed_base_v065_signal,
    f39ve_f39_valuation_entry_book_eqev_spr_base_v066_signal,
    f39ve_f39_valuation_entry_sales_eqev_spr_base_v067_signal,
    f39ve_f39_valuation_entry_ev_invmean_base_v068_signal,
    f39ve_f39_valuation_entry_eqmult_invmean_base_v069_signal,
    f39ve_f39_valuation_entry_pe_deepval_base_v070_signal,
    f39ve_f39_valuation_entry_ps_deepval_base_v071_signal,
    f39ve_f39_valuation_entry_evebitda_deepval_base_v072_signal,
    f39ve_f39_valuation_entry_ey_revert_base_v073_signal,
    f39ve_f39_valuation_entry_fy_revert_base_v074_signal,
    f39ve_f39_valuation_entry_grandblend_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_VALUATION_ENTRY_REGISTRY_001_075 = REGISTRY


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

    # multiples: positive ~5-40
    pe = _fund(1, base=18.0, drift=0.01, vol=0.06).rename("pe")
    pb = _fund(2, base=3.0, drift=0.01, vol=0.07).rename("pb")
    ps = _fund(3, base=4.0, drift=0.01, vol=0.06).rename("ps")
    evebit = _fund(4, base=16.0, drift=0.01, vol=0.06).rename("evebit")
    evebitda = _fund(5, base=11.0, drift=0.01, vol=0.06).rename("evebitda")
    # value scales: positive
    marketcap = _fund(6, base=5e9, drift=0.02, vol=0.05).rename("marketcap")
    ev = _fund(7, base=6e9, drift=0.02, vol=0.05).rename("ev")
    revenue = _fund(8, base=2e9, drift=0.02, vol=0.05).rename("revenue")
    equity = _fund(9, base=3e9, drift=0.02, vol=0.05).rename("equity")
    # flows: allow negative
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

    print("OK f39_valuation_entry_base_001_075_claude: %d features pass" % n_features)
