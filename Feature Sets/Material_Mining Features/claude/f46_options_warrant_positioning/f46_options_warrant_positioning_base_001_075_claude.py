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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (options / warrant positioning) =====
# All inputs are non-negative ownership/value columns from the sf3a holder breakdown.
def _put_call_holder_skew(putholders, cllholders):
    # >0 means put-holder dominance (bearish/hedged positioning breadth)
    return (putholders - cllholders) / (putholders + cllholders).replace(0, np.nan)


def _put_call_value_skew(putvalue, cllvalue):
    return (putvalue - cllvalue) / (putvalue + cllvalue).replace(0, np.nan)


def _hedging_intensity(putvalue, marketcap):
    # put notional held vs equity market cap (downside hedging pressure)
    return putvalue / marketcap.replace(0, np.nan)


def _call_intensity(cllvalue, marketcap):
    return cllvalue / marketcap.replace(0, np.nan)


def _warrant_overhang_mcap(wntvalue, marketcap):
    # latent dilution: warrant notional vs market cap (overhead supply)
    return wntvalue / marketcap.replace(0, np.nan)


def _warrant_overhang_total(wntvalue, totalvalue):
    return wntvalue / totalvalue.replace(0, np.nan)


def _debt_overhang(dbtvalue, totalvalue):
    # convert / credit overhang share
    return dbtvalue / totalvalue.replace(0, np.nan)


def _deriv_equity_share(putvalue, cllvalue, wntvalue, shrvalue):
    deriv = putvalue + cllvalue + wntvalue
    return deriv / shrvalue.replace(0, np.nan)


def _avg_ticket(value, holders):
    # average position size per holder
    return value / holders.replace(0, np.nan)


def _breadth(holders, w):
    return _z(holders, w)


# ============================================================
# put/call holder skew, level
def f46ow_f46_options_warrant_positioning_pcholdskew_base_v001_signal(putholders, cllholders):
    b = _put_call_holder_skew(putholders, cllholders)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put/call value skew, level
def f46ow_f46_options_warrant_positioning_pcvalskew_base_v002_signal(putvalue, cllvalue):
    b = _put_call_value_skew(putvalue, cllvalue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put/call value skew z-scored vs its 252d history (de-trended positioning)
def f46ow_f46_options_warrant_positioning_pcvalskewz_base_v003_signal(putvalue, cllvalue):
    s = _put_call_value_skew(putvalue, cllvalue)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hedging intensity: put notional vs market cap
def f46ow_f46_options_warrant_positioning_hedgeint_base_v004_signal(putvalue, marketcap):
    b = _hedging_intensity(putvalue, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hedging intensity z-scored vs its own 252d history
def f46ow_f46_options_warrant_positioning_hedgeintz_base_v005_signal(putvalue, marketcap):
    h = _hedging_intensity(putvalue, marketcap)
    b = _z(h, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call accumulation intensity: call notional vs market cap
def f46ow_f46_options_warrant_positioning_callint_base_v006_signal(cllvalue, marketcap):
    b = _call_intensity(cllvalue, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang vs market cap (latent dilution / overhead supply)
def f46ow_f46_options_warrant_positioning_wntoverM_base_v007_signal(wntvalue, marketcap):
    b = _warrant_overhang_mcap(wntvalue, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang vs total reported holder value
def f46ow_f46_options_warrant_positioning_wntoverT_base_v008_signal(wntvalue, totalvalue):
    b = _warrant_overhang_total(wntvalue, totalvalue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang (mcap) z-scored vs 252d history (dilution build-up)
def f46ow_f46_options_warrant_positioning_wntoverMz_base_v009_signal(wntvalue, marketcap):
    o = _warrant_overhang_mcap(wntvalue, marketcap)
    b = _z(o, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-holder credit overhang share
def f46ow_f46_options_warrant_positioning_dbtover_base_v010_signal(dbtvalue, totalvalue):
    b = _debt_overhang(dbtvalue, totalvalue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# derivatives-vs-equity value share (put+call+warrant vs shrvalue)
def f46ow_f46_options_warrant_positioning_derivshare_base_v011_signal(putvalue, cllvalue, wntvalue, shrvalue):
    b = _deriv_equity_share(putvalue, cllvalue, wntvalue, shrvalue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# positioning breadth: put-holder count z-scored (how many institutions hold puts)
def f46ow_f46_options_warrant_positioning_putbreadth_base_v012_signal(putholders):
    b = _breadth(putholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# positioning breadth: call-holder count z-scored
def f46ow_f46_options_warrant_positioning_callbreadth_base_v013_signal(cllholders):
    b = _breadth(cllholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# positioning breadth: warrant-holder count z-scored
def f46ow_f46_options_warrant_positioning_wntbreadth_base_v014_signal(wntholders):
    b = _breadth(wntholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average put ticket size (put value per holder), de-trended
def f46ow_f46_options_warrant_positioning_putticketz_base_v015_signal(putvalue, putholders):
    t = _avg_ticket(putvalue, putholders)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average call ticket size (call value per holder), de-trended
def f46ow_f46_options_warrant_positioning_callticketz_base_v016_signal(cllvalue, cllholders):
    t = _avg_ticket(cllvalue, cllholders)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average warrant ticket size (warrant value per holder), de-trended
def f46ow_f46_options_warrant_positioning_wntticketz_base_v017_signal(wntvalue, wntholders):
    t = _avg_ticket(wntvalue, wntholders)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-unit per holder concentration (units, not value) ranked
def f46ow_f46_options_warrant_positioning_putunitconc_base_v018_signal(putunits, putholders):
    c = putunits / putholders.replace(0, np.nan)
    b = _rank(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-unit per holder concentration ranked
def f46ow_f46_options_warrant_positioning_callunitconc_base_v019_signal(cllunits, cllholders):
    c = cllunits / cllholders.replace(0, np.nan)
    b = _rank(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant-unit per holder concentration ranked
def f46ow_f46_options_warrant_positioning_wntunitconc_base_v020_signal(wntunits, wntholders):
    c = wntunits / wntholders.replace(0, np.nan)
    b = _rank(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Δ put positioning intensity: change in put/mcap over a quarter
def f46ow_f46_options_warrant_positioning_dputint_base_v021_signal(putvalue, marketcap):
    h = _hedging_intensity(putvalue, marketcap)
    b = h - h.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Δ call positioning intensity: change in call/mcap over a quarter
def f46ow_f46_options_warrant_positioning_dcallint_base_v022_signal(cllvalue, marketcap):
    h = _call_intensity(cllvalue, marketcap)
    b = h - h.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Δ warrant overhang over a quarter (dilution accretion)
def f46ow_f46_options_warrant_positioning_dwntover_base_v023_signal(wntvalue, marketcap):
    o = _warrant_overhang_mcap(wntvalue, marketcap)
    b = o - o.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-minus-call intensity spread (net bearish derivatives pressure)
def f46ow_f46_options_warrant_positioning_netbearint_base_v024_signal(putvalue, cllvalue, marketcap):
    b = (putvalue - cllvalue) / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put+call total optionality vs market cap (gross derivatives engagement)
def f46ow_f46_options_warrant_positioning_grossopt_base_v025_signal(putvalue, cllvalue, marketcap):
    b = (putvalue + cllvalue) / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-holder share of all option (put+call) holders, ranked (breadth percentile)
def f46ow_f46_options_warrant_positioning_pcholdratio_base_v026_signal(putholders, cllholders):
    share = putholders / (putholders + cllholders).replace(0, np.nan)
    b = _rank(share, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put/call value ratio vs its own slow EMA (value-tilt displacement)
def f46ow_f46_options_warrant_positioning_pcvalratio_base_v027_signal(putvalue, cllvalue):
    r = np.log(putvalue.replace(0, np.nan) / cllvalue.replace(0, np.nan))
    b = r - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant value share of total optionality (warrant vs put+call value)
def f46ow_f46_options_warrant_positioning_wntoptshare_base_v028_signal(wntvalue, putvalue, cllvalue):
    b = wntvalue / (putvalue + cllvalue + wntvalue).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt vs warrant overhang balance (credit vs dilution latent supply)
def f46ow_f46_options_warrant_positioning_dbtwntbal_base_v029_signal(dbtvalue, wntvalue):
    b = (dbtvalue - wntvalue) / (dbtvalue + wntvalue).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined latent supply: (warrant+debt) vs market cap (total dilution+credit overhang)
def f46ow_f46_options_warrant_positioning_latentsupply_base_v030_signal(wntvalue, dbtvalue, marketcap):
    b = (wntvalue + dbtvalue) / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal level (filer's share of total reported value), centered
def f46ow_f46_options_warrant_positioning_pctlevel_base_v031_signal(percentoftotal):
    b = percentoftotal - _mean(percentoftotal, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal interacted with hedging intensity (concentrated hedgers)
def f46ow_f46_options_warrant_positioning_pcthedge_base_v032_signal(percentoftotal, putvalue, marketcap):
    h = _hedging_intensity(putvalue, marketcap)
    b = percentoftotal * h
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang ranked vs its own 504d history (extreme dilution percentile)
def f46ow_f46_options_warrant_positioning_wntoverrank_base_v033_signal(wntvalue, marketcap):
    o = _warrant_overhang_mcap(wntvalue, marketcap)
    b = _rank(o, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hedging intensity ranked vs 504d history
def f46ow_f46_options_warrant_positioning_hedgerank_base_v034_signal(putvalue, marketcap):
    h = _hedging_intensity(putvalue, marketcap)
    b = _rank(h, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-holder breadth minus call-holder breadth (divergent positioning breadth)
def f46ow_f46_options_warrant_positioning_breadthdiv_base_v035_signal(putholders, cllholders):
    b = _z(putholders, 252) - _z(cllholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total holder participation across all derivative books, de-trended
def f46ow_f46_options_warrant_positioning_totholders_base_v036_signal(putholders, cllholders, wntholders, dbtholders):
    tot = putholders + cllholders + wntholders + dbtholders
    b = _z(tot, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant-holder share of total derivative holders (dilution constituency)
def f46ow_f46_options_warrant_positioning_wntholdshare_base_v037_signal(wntholders, putholders, cllholders, dbtholders):
    b = wntholders / (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-value vs total reported value (downside book weight in filings)
def f46ow_f46_options_warrant_positioning_putvaltot_base_v038_signal(putvalue, totalvalue):
    b = putvalue / totalvalue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-value vs total reported value
def f46ow_f46_options_warrant_positioning_callvaltot_base_v039_signal(cllvalue, totalvalue):
    b = cllvalue / totalvalue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total optionality (put+call) value vs equity value, ranked (engagement percentile)
def f46ow_f46_options_warrant_positioning_optvsequity_base_v040_signal(putvalue, cllvalue, shrvalue):
    eng = (cllvalue + putvalue) / shrvalue.replace(0, np.nan)
    b = _rank(eng, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Δ put/call value skew over a quarter (positioning momentum)
def f46ow_f46_options_warrant_positioning_dpcvalskew_base_v041_signal(putvalue, cllvalue):
    s = _put_call_value_skew(putvalue, cllvalue)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Δ put/call holder skew over a quarter
def f46ow_f46_options_warrant_positioning_dpcholdskew_base_v042_signal(putholders, cllholders):
    s = _put_call_holder_skew(putholders, cllholders)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Δ derivatives-vs-equity share over a quarter (rotation into derivatives)
def f46ow_f46_options_warrant_positioning_dderivshare_base_v043_signal(putvalue, cllvalue, wntvalue, shrvalue):
    s = _deriv_equity_share(putvalue, cllvalue, wntvalue, shrvalue)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put unit notional vs market cap (units-based hedge pressure, distinct from value)
def f46ow_f46_options_warrant_positioning_putunitint_base_v044_signal(putunits, marketcap):
    b = _z(putunits / marketcap.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call unit notional vs market cap z-scored
def f46ow_f46_options_warrant_positioning_callunitint_base_v045_signal(cllunits, marketcap):
    b = _z(cllunits / marketcap.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant units vs market cap (latent share count overhang) z-scored
def f46ow_f46_options_warrant_positioning_wntunitint_base_v046_signal(wntunits, marketcap):
    b = _z(wntunits / marketcap.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put unit/value price proxy vs call (avg strike-rich positioning) skew
def f46ow_f46_options_warrant_positioning_unitvalpx_base_v047_signal(putvalue, putunits, cllvalue, cllunits):
    pp = putvalue / putunits.replace(0, np.nan)
    cp = cllvalue / cllunits.replace(0, np.nan)
    b = (pp - cp) / (pp + cp).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant per-unit value vs equity per-unit (warrant pricing intensity)
def f46ow_f46_options_warrant_positioning_wntunitpx_base_v048_signal(wntvalue, wntunits, marketcap):
    px = wntvalue / wntunits.replace(0, np.nan)
    b = _z(px / marketcap.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hedging intensity acceleration vs longer baseline (62/126 spread of put/mcap)
def f46ow_f46_options_warrant_positioning_hedgespr_base_v049_signal(putvalue, marketcap):
    h = _hedging_intensity(putvalue, marketcap)
    b = _mean(h, 63) - _mean(h, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang short vs long mean spread (dilution build acceleration)
def f46ow_f46_options_warrant_positioning_wntspr_base_v050_signal(wntvalue, totalvalue):
    o = _warrant_overhang_total(wntvalue, totalvalue)
    b = _mean(o, 63) - _mean(o, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt overhang z-scored (credit positioning extremity)
def f46ow_f46_options_warrant_positioning_dbtoverz_base_v051_signal(dbtvalue, totalvalue):
    o = _debt_overhang(dbtvalue, totalvalue)
    b = _z(o, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt holders presence breadth (count of credit/convert holders) z
def f46ow_f46_options_warrant_positioning_dbtbreadth_base_v052_signal(dbtholders):
    b = _breadth(dbtholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net latent dilution: (warrant+debt) overhang minus call accumulation cover
def f46ow_f46_options_warrant_positioning_netdilution_base_v053_signal(wntvalue, dbtvalue, cllvalue, marketcap):
    b = (wntvalue + dbtvalue - cllvalue) / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put dominance regime fraction: share of last year put-skew was positive
def f46ow_f46_options_warrant_positioning_putregime_base_v054_signal(putvalue, cllvalue):
    s = _put_call_value_skew(putvalue, cllvalue)
    flag = (s > 0).astype(float)
    b = flag.rolling(252, min_periods=126).mean() + 0.25 * s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang regime: fraction of last year overhang sat above its own 252d median
def f46ow_f46_options_warrant_positioning_wntregime_base_v055_signal(wntvalue, marketcap):
    o = _warrant_overhang_mcap(wntvalue, marketcap)
    med = o.rolling(252, min_periods=126).median()
    flag = (o >= med).astype(float)
    b = flag.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of quarters (over 504d) warrant overhang stepped up (dilution accretion count)
def f46ow_f46_options_warrant_positioning_wntstepcount_base_v056_signal(wntvalue, totalvalue):
    o = _warrant_overhang_total(wntvalue, totalvalue)
    up = (o.diff(63) > 0).astype(float)
    b = up.rolling(504, min_periods=252).sum() + 5.0 * o
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-hedging entries: count of times hedge intensity newly crossed its 252d median
def f46ow_f46_options_warrant_positioning_hedgeentries_base_v057_signal(putvalue, marketcap):
    h = _hedging_intensity(putvalue, marketcap)
    med = h.rolling(252, min_periods=126).median()
    above = (h > med).astype(float)
    entries = ((above == 1) & (above.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + 3.0 * (h - med)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# derivatives concentration: avg derivative ticket vs equity ticket (per-holder)
def f46ow_f46_options_warrant_positioning_ticketconc_base_v058_signal(putvalue, cllvalue, wntvalue, putholders, cllholders, wntholders, shrvalue):
    dval = putvalue + cllvalue + wntvalue
    dhold = putholders + cllholders + wntholders
    dticket = dval / dhold.replace(0, np.nan)
    b = _z(dticket / shrvalue.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hedge tilt vs warrant overhang interaction (bearish + dilutive double pressure)
def f46ow_f46_options_warrant_positioning_bearishdilute_base_v059_signal(putvalue, wntvalue, marketcap):
    h = putvalue / marketcap.replace(0, np.nan)
    o = wntvalue / marketcap.replace(0, np.nan)
    b = np.sqrt(h.clip(lower=0) * o.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call accumulation acceleration: change in call/mcap momentum (quarter-over-quarter)
def f46ow_f46_options_warrant_positioning_callmomtanh_base_v060_signal(cllvalue, marketcap):
    c = _call_intensity(cllvalue, marketcap)
    mom = c.diff(63)
    b = mom - mom.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put/call value skew dispersion (instability of positioning) over 252d
def f46ow_f46_options_warrant_positioning_skewdisp_base_v061_signal(putvalue, cllvalue):
    s = _put_call_value_skew(putvalue, cllvalue)
    b = _std(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang dispersion (volatility of latent dilution)
def f46ow_f46_options_warrant_positioning_wntdisp_base_v062_signal(wntvalue, marketcap):
    o = _warrant_overhang_mcap(wntvalue, marketcap)
    b = _std(o, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal x warrant overhang (concentrated dilutive holders)
def f46ow_f46_options_warrant_positioning_pctdilute_base_v063_signal(percentoftotal, wntvalue, totalvalue):
    o = _warrant_overhang_total(wntvalue, totalvalue)
    b = percentoftotal * o
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-vs-equity holder value (credit holders' notional vs shr value)
def f46ow_f46_options_warrant_positioning_dbtequity_base_v064_signal(dbtvalue, shrvalue):
    b = _z(dbtvalue / shrvalue.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total derivatives value share of total reported value, z-scored (de-trended rotation)
def f46ow_f46_options_warrant_positioning_derivtotshare_base_v065_signal(putvalue, cllvalue, wntvalue, totalvalue):
    share = (putvalue + cllvalue + wntvalue) / totalvalue.replace(0, np.nan)
    b = _z(share, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-holder count per unit of put value (fragmentation of hedge book) ranked
def f46ow_f46_options_warrant_positioning_putfragment_base_v066_signal(putholders, putvalue):
    f = putholders / putvalue.replace(0, np.nan)
    b = _rank(f, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant-holder count per unit warrant value (fragmentation of dilution book) ranked
def f46ow_f46_options_warrant_positioning_wntfragment_base_v067_signal(wntholders, wntvalue):
    f = wntholders / wntvalue.replace(0, np.nan)
    b = _rank(f, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bullish minus bearish breadth tilt scaled by gross optionality
def f46ow_f46_options_warrant_positioning_breadthtilt_base_v068_signal(cllholders, putholders, cllvalue, putvalue, marketcap):
    tilt = (cllholders - putholders) / (cllholders + putholders).replace(0, np.nan)
    gross = (cllvalue + putvalue) / marketcap.replace(0, np.nan)
    b = tilt * gross
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang relative to its level one year ago (YoY dilution change)
def f46ow_f46_options_warrant_positioning_wntyoy_base_v069_signal(wntvalue, marketcap):
    o = _warrant_overhang_mcap(wntvalue, marketcap)
    b = o - o.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hedging intensity relative to one year ago (YoY hedge build)
def f46ow_f46_options_warrant_positioning_hedgeyoy_base_v070_signal(putvalue, marketcap):
    h = _hedging_intensity(putvalue, marketcap)
    b = h - h.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net derivative dollar flow momentum: change in (call-put)/mcap over a quarter
def f46ow_f46_options_warrant_positioning_netflowsm_base_v071_signal(cllvalue, putvalue, marketcap):
    net = (cllvalue - putvalue) / marketcap.replace(0, np.nan)
    b = net - net.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total latent supply (warrant+debt) ranked vs 504d history (overhang percentile)
def f46ow_f46_options_warrant_positioning_latentrank_base_v072_signal(wntvalue, dbtvalue, marketcap):
    s = (wntvalue + dbtvalue) / marketcap.replace(0, np.nan)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# avg put ticket vs avg call ticket (smart-money sizing skew toward downside)
def f46ow_f46_options_warrant_positioning_ticketskew_base_v073_signal(putvalue, putholders, cllvalue, cllholders):
    pt = _avg_ticket(putvalue, putholders)
    ct = _avg_ticket(cllvalue, cllholders)
    b = (pt - ct) / (pt + ct).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal momentum (change in filer share over a quarter)
def f46ow_f46_options_warrant_positioning_pctmom_base_v074_signal(percentoftotal):
    b = percentoftotal - percentoftotal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite overhang pressure: warrant + debt + put-hedge vs market cap, smoothed
def f46ow_f46_options_warrant_positioning_overhangpress_base_v075_signal(wntvalue, dbtvalue, putvalue, marketcap):
    raw = (wntvalue + dbtvalue + putvalue) / marketcap.replace(0, np.nan)
    b = raw.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46ow_f46_options_warrant_positioning_pcholdskew_base_v001_signal,
    f46ow_f46_options_warrant_positioning_pcvalskew_base_v002_signal,
    f46ow_f46_options_warrant_positioning_pcvalskewz_base_v003_signal,
    f46ow_f46_options_warrant_positioning_hedgeint_base_v004_signal,
    f46ow_f46_options_warrant_positioning_hedgeintz_base_v005_signal,
    f46ow_f46_options_warrant_positioning_callint_base_v006_signal,
    f46ow_f46_options_warrant_positioning_wntoverM_base_v007_signal,
    f46ow_f46_options_warrant_positioning_wntoverT_base_v008_signal,
    f46ow_f46_options_warrant_positioning_wntoverMz_base_v009_signal,
    f46ow_f46_options_warrant_positioning_dbtover_base_v010_signal,
    f46ow_f46_options_warrant_positioning_derivshare_base_v011_signal,
    f46ow_f46_options_warrant_positioning_putbreadth_base_v012_signal,
    f46ow_f46_options_warrant_positioning_callbreadth_base_v013_signal,
    f46ow_f46_options_warrant_positioning_wntbreadth_base_v014_signal,
    f46ow_f46_options_warrant_positioning_putticketz_base_v015_signal,
    f46ow_f46_options_warrant_positioning_callticketz_base_v016_signal,
    f46ow_f46_options_warrant_positioning_wntticketz_base_v017_signal,
    f46ow_f46_options_warrant_positioning_putunitconc_base_v018_signal,
    f46ow_f46_options_warrant_positioning_callunitconc_base_v019_signal,
    f46ow_f46_options_warrant_positioning_wntunitconc_base_v020_signal,
    f46ow_f46_options_warrant_positioning_dputint_base_v021_signal,
    f46ow_f46_options_warrant_positioning_dcallint_base_v022_signal,
    f46ow_f46_options_warrant_positioning_dwntover_base_v023_signal,
    f46ow_f46_options_warrant_positioning_netbearint_base_v024_signal,
    f46ow_f46_options_warrant_positioning_grossopt_base_v025_signal,
    f46ow_f46_options_warrant_positioning_pcholdratio_base_v026_signal,
    f46ow_f46_options_warrant_positioning_pcvalratio_base_v027_signal,
    f46ow_f46_options_warrant_positioning_wntoptshare_base_v028_signal,
    f46ow_f46_options_warrant_positioning_dbtwntbal_base_v029_signal,
    f46ow_f46_options_warrant_positioning_latentsupply_base_v030_signal,
    f46ow_f46_options_warrant_positioning_pctlevel_base_v031_signal,
    f46ow_f46_options_warrant_positioning_pcthedge_base_v032_signal,
    f46ow_f46_options_warrant_positioning_wntoverrank_base_v033_signal,
    f46ow_f46_options_warrant_positioning_hedgerank_base_v034_signal,
    f46ow_f46_options_warrant_positioning_breadthdiv_base_v035_signal,
    f46ow_f46_options_warrant_positioning_totholders_base_v036_signal,
    f46ow_f46_options_warrant_positioning_wntholdshare_base_v037_signal,
    f46ow_f46_options_warrant_positioning_putvaltot_base_v038_signal,
    f46ow_f46_options_warrant_positioning_callvaltot_base_v039_signal,
    f46ow_f46_options_warrant_positioning_optvsequity_base_v040_signal,
    f46ow_f46_options_warrant_positioning_dpcvalskew_base_v041_signal,
    f46ow_f46_options_warrant_positioning_dpcholdskew_base_v042_signal,
    f46ow_f46_options_warrant_positioning_dderivshare_base_v043_signal,
    f46ow_f46_options_warrant_positioning_putunitint_base_v044_signal,
    f46ow_f46_options_warrant_positioning_callunitint_base_v045_signal,
    f46ow_f46_options_warrant_positioning_wntunitint_base_v046_signal,
    f46ow_f46_options_warrant_positioning_unitvalpx_base_v047_signal,
    f46ow_f46_options_warrant_positioning_wntunitpx_base_v048_signal,
    f46ow_f46_options_warrant_positioning_hedgespr_base_v049_signal,
    f46ow_f46_options_warrant_positioning_wntspr_base_v050_signal,
    f46ow_f46_options_warrant_positioning_dbtoverz_base_v051_signal,
    f46ow_f46_options_warrant_positioning_dbtbreadth_base_v052_signal,
    f46ow_f46_options_warrant_positioning_netdilution_base_v053_signal,
    f46ow_f46_options_warrant_positioning_putregime_base_v054_signal,
    f46ow_f46_options_warrant_positioning_wntregime_base_v055_signal,
    f46ow_f46_options_warrant_positioning_wntstepcount_base_v056_signal,
    f46ow_f46_options_warrant_positioning_hedgeentries_base_v057_signal,
    f46ow_f46_options_warrant_positioning_ticketconc_base_v058_signal,
    f46ow_f46_options_warrant_positioning_bearishdilute_base_v059_signal,
    f46ow_f46_options_warrant_positioning_callmomtanh_base_v060_signal,
    f46ow_f46_options_warrant_positioning_skewdisp_base_v061_signal,
    f46ow_f46_options_warrant_positioning_wntdisp_base_v062_signal,
    f46ow_f46_options_warrant_positioning_pctdilute_base_v063_signal,
    f46ow_f46_options_warrant_positioning_dbtequity_base_v064_signal,
    f46ow_f46_options_warrant_positioning_derivtotshare_base_v065_signal,
    f46ow_f46_options_warrant_positioning_putfragment_base_v066_signal,
    f46ow_f46_options_warrant_positioning_wntfragment_base_v067_signal,
    f46ow_f46_options_warrant_positioning_breadthtilt_base_v068_signal,
    f46ow_f46_options_warrant_positioning_wntyoy_base_v069_signal,
    f46ow_f46_options_warrant_positioning_hedgeyoy_base_v070_signal,
    f46ow_f46_options_warrant_positioning_netflowsm_base_v071_signal,
    f46ow_f46_options_warrant_positioning_latentrank_base_v072_signal,
    f46ow_f46_options_warrant_positioning_ticketskew_base_v073_signal,
    f46ow_f46_options_warrant_positioning_pctmom_base_v074_signal,
    f46ow_f46_options_warrant_positioning_overhangpress_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_OPTIONS_WARRANT_POSITIONING_REGISTRY_001_075 = REGISTRY


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

    putholders = _fund(101, base=40.0, drift=0.01, vol=0.10).rename("putholders")
    cllholders = _fund(102, base=55.0, drift=0.012, vol=0.10).rename("cllholders")
    wntholders = _fund(103, base=18.0, drift=-0.005, vol=0.12).rename("wntholders")
    dbtholders = _fund(104, base=12.0, drift=0.004, vol=0.13).rename("dbtholders")
    putunits = _fund(105, base=2.0e6, drift=0.006, vol=0.14).rename("putunits")
    cllunits = _fund(106, base=2.6e6, drift=0.009, vol=0.14).rename("cllunits")
    wntunits = _fund(107, base=1.4e6, drift=0.002, vol=0.16).rename("wntunits")
    putvalue = _fund(108, base=9.0e6, drift=0.005, vol=0.13).rename("putvalue")
    cllvalue = _fund(109, base=1.1e7, drift=0.011, vol=0.13).rename("cllvalue")
    wntvalue = _fund(110, base=6.0e6, drift=0.003, vol=0.15).rename("wntvalue")
    dbtvalue = _fund(111, base=8.0e6, drift=0.004, vol=0.14).rename("dbtvalue")
    shrvalue = _fund(112, base=1.2e8, drift=0.010, vol=0.09).rename("shrvalue")
    totalvalue = (putvalue + cllvalue + wntvalue + dbtvalue + shrvalue).rename("totalvalue")
    marketcap = _fund(113, base=4.0e8, drift=0.008, vol=0.11).rename("marketcap")
    percentoftotal = (_fund(114, base=0.4, drift=0.0, vol=0.10)
                      .clip(0.01, 0.99)).rename("percentoftotal")

    cols = {
        "putholders": putholders, "cllholders": cllholders, "wntholders": wntholders,
        "dbtholders": dbtholders, "putunits": putunits, "cllunits": cllunits,
        "wntunits": wntunits, "putvalue": putvalue, "cllvalue": cllvalue,
        "wntvalue": wntvalue, "dbtvalue": dbtvalue, "shrvalue": shrvalue,
        "totalvalue": totalvalue, "marketcap": marketcap, "percentoftotal": percentoftotal,
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

    print("OK f46_options_warrant_positioning_base_001_075_claude: %d features pass" % n_features)
