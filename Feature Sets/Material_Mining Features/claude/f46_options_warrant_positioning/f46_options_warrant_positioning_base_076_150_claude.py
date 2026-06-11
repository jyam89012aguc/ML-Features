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
def _put_call_holder_skew(putholders, cllholders):
    return (putholders - cllholders) / (putholders + cllholders).replace(0, np.nan)


def _put_call_value_skew(putvalue, cllvalue):
    return (putvalue - cllvalue) / (putvalue + cllvalue).replace(0, np.nan)


def _hedging_intensity(putvalue, marketcap):
    return putvalue / marketcap.replace(0, np.nan)


def _call_intensity(cllvalue, marketcap):
    return cllvalue / marketcap.replace(0, np.nan)


def _warrant_overhang_mcap(wntvalue, marketcap):
    return wntvalue / marketcap.replace(0, np.nan)


def _warrant_overhang_total(wntvalue, totalvalue):
    return wntvalue / totalvalue.replace(0, np.nan)


def _debt_overhang(dbtvalue, totalvalue):
    return dbtvalue / totalvalue.replace(0, np.nan)


def _avg_ticket(value, holders):
    return value / holders.replace(0, np.nan)


# ============================================================
# put/call holder skew smoothed (persistent breadth tilt)
def f46ow_f46_options_warrant_positioning_pcholdskewsm_base_v076_signal(putholders, cllholders):
    s = _put_call_holder_skew(putholders, cllholders)
    b = s.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put/call value skew vs its 504d mean (long de-trended tilt)
def f46ow_f46_options_warrant_positioning_pcvalskewdev_base_v077_signal(putvalue, cllvalue):
    s = _put_call_value_skew(putvalue, cllvalue)
    b = s - _mean(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hedging intensity over a half-year horizon mean (structural hedge level)
def f46ow_f46_options_warrant_positioning_hedgelvl126_base_v078_signal(putvalue, marketcap):
    h = _hedging_intensity(putvalue, marketcap)
    b = _mean(h, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call intensity ranked vs 252d history (bullish accumulation percentile)
def f46ow_f46_options_warrant_positioning_callrank_base_v079_signal(cllvalue, marketcap):
    c = _call_intensity(cllvalue, marketcap)
    b = _rank(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang (total) ranked vs 252d history
def f46ow_f46_options_warrant_positioning_wntoverTrank_base_v080_signal(wntvalue, totalvalue):
    o = _warrant_overhang_total(wntvalue, totalvalue)
    b = _rank(o, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt overhang momentum over a quarter (credit overhang build)
def f46ow_f46_options_warrant_positioning_dbtovermom_base_v081_signal(dbtvalue, totalvalue):
    o = _debt_overhang(dbtvalue, totalvalue)
    b = o - o.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put intensity vs warrant overhang ratio (hedge-vs-dilution emphasis)
def f46ow_f46_options_warrant_positioning_hedgevswnt_base_v082_signal(putvalue, wntvalue):
    b = np.log(putvalue.replace(0, np.nan) / wntvalue.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call value vs warrant value ratio (bullish optionality vs dilution overhang)
def f46ow_f46_options_warrant_positioning_callvswnt_base_v083_signal(cllvalue, wntvalue):
    b = np.log(cllvalue.replace(0, np.nan) / wntvalue.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt value vs equity value ratio z-scored (credit leverage extremity)
def f46ow_f46_options_warrant_positioning_dbtequitymom_base_v084_signal(dbtvalue, shrvalue):
    r = dbtvalue / shrvalue.replace(0, np.nan)
    b = _z(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-holder breadth ranked vs 504d history (hedge constituency percentile)
def f46ow_f46_options_warrant_positioning_putbreadthrank_base_v085_signal(putholders):
    b = _rank(putholders, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-holder breadth ranked vs 504d history
def f46ow_f46_options_warrant_positioning_callbreadthrank_base_v086_signal(cllholders):
    b = _rank(cllholders, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant-holder breadth ranked vs 504d history
def f46ow_f46_options_warrant_positioning_wntbreadthrank_base_v087_signal(wntholders):
    b = _rank(wntholders, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put ticket momentum (avg position size change over a quarter)
def f46ow_f46_options_warrant_positioning_putticketmom_base_v088_signal(putvalue, putholders):
    t = _avg_ticket(putvalue, putholders)
    b = np.log(t.replace(0, np.nan) / t.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call ticket momentum
def f46ow_f46_options_warrant_positioning_callticketmom_base_v089_signal(cllvalue, cllholders):
    t = _avg_ticket(cllvalue, cllholders)
    b = np.log(t.replace(0, np.nan) / t.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant ticket momentum
def f46ow_f46_options_warrant_positioning_wntticketmom_base_v090_signal(wntvalue, wntholders):
    t = _avg_ticket(wntvalue, wntholders)
    b = np.log(t.replace(0, np.nan) / t.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put units vs call units skew (volume-side positioning, distinct from value)
def f46ow_f46_options_warrant_positioning_unitskew_base_v091_signal(putunits, cllunits):
    b = (putunits - cllunits) / (putunits + cllunits).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant units vs (put+call) units share (latent share overhang vs traded optionality)
def f46ow_f46_options_warrant_positioning_wntunitshare_base_v092_signal(wntunits, putunits, cllunits):
    b = wntunits / (putunits + cllunits + wntunits).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross optionality intensity smoothed (structural derivative engagement)
def f46ow_f46_options_warrant_positioning_grossoptsm_base_v093_signal(putvalue, cllvalue, marketcap):
    g = (putvalue + cllvalue) / marketcap.replace(0, np.nan)
    b = g.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# latent supply (warrant+debt vs mcap) momentum over a quarter
def f46ow_f46_options_warrant_positioning_latentmom_base_v094_signal(wntvalue, dbtvalue, marketcap):
    s = (wntvalue + dbtvalue) / marketcap.replace(0, np.nan)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal z-scored (filer concentration extremity)
def f46ow_f46_options_warrant_positioning_pctz_base_v095_signal(percentoftotal):
    b = _z(percentoftotal, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal x warrant overhang momentum (concentrated dilution build)
def f46ow_f46_options_warrant_positioning_pctwntmom_base_v096_signal(percentoftotal, wntvalue, marketcap):
    o = _warrant_overhang_mcap(wntvalue, marketcap)
    prod = percentoftotal * o
    b = prod - prod.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hedge intensity exceedance over its 252d max-band (extreme hedge pressure)
def f46ow_f46_options_warrant_positioning_hedgeexceed_base_v097_signal(putvalue, marketcap):
    h = _hedging_intensity(putvalue, marketcap)
    hi = _rmax(h, 252)
    b = (h / hi.replace(0, np.nan)) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang drawup off its 252d min (dilution accretion off trough)
def f46ow_f46_options_warrant_positioning_wntdrawup_base_v098_signal(wntvalue, marketcap):
    o = _warrant_overhang_mcap(wntvalue, marketcap)
    lo = _rmin(o, 252)
    b = o / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of months (252d) put-skew flipped sign (positioning indecision count)
def f46ow_f46_options_warrant_positioning_skewflips_base_v099_signal(putvalue, cllvalue):
    s = _put_call_value_skew(putvalue, cllvalue)
    flip = (np.sign(s) != np.sign(s.shift(21))).astype(float)
    b = flip.rolling(252, min_periods=126).sum() + s.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year call accumulation exceeded put hedging intensity
def f46ow_f46_options_warrant_positioning_bullregime_base_v100_signal(cllvalue, putvalue, marketcap):
    c = _call_intensity(cllvalue, marketcap)
    h = _hedging_intensity(putvalue, marketcap)
    flag = (c > h).astype(float)
    b = flag.rolling(252, min_periods=126).mean() + 2.0 * (c - h)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang streak: consecutive quarters of rising overhang (capped)
def f46ow_f46_options_warrant_positioning_wntstreak_base_v101_signal(wntvalue, totalvalue):
    o = _warrant_overhang_total(wntvalue, totalvalue)
    up = (o.diff(21) > 0).astype(float)
    streak = up.groupby((up != up.shift()).cumsum()).cumsum() * up
    b = streak + 10.0 * o
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# derivative book turnover proxy: dispersion of total deriv value / mcap
def f46ow_f46_options_warrant_positioning_derivturn_base_v102_signal(putvalue, cllvalue, wntvalue, marketcap):
    d = (putvalue + cllvalue + wntvalue) / marketcap.replace(0, np.nan)
    b = _std(d, 126) / _mean(d, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-value share of total optionality momentum (downside weight build over a quarter)
def f46ow_f46_options_warrant_positioning_putoptshare_base_v103_signal(putvalue, cllvalue, wntvalue):
    share = putvalue / (putvalue + cllvalue + wntvalue).replace(0, np.nan)
    b = share - share.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call-value share of total optionality
def f46ow_f46_options_warrant_positioning_calloptshare_base_v104_signal(putvalue, cllvalue, wntvalue):
    b = cllvalue / (putvalue + cllvalue + wntvalue).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-holder count vs warrant-holder count tilt (credit vs dilution constituency)
def f46ow_f46_options_warrant_positioning_dbtwntholdtilt_base_v105_signal(dbtholders, wntholders):
    b = (dbtholders - wntholders) / (dbtholders + wntholders).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# avg debt ticket vs avg warrant ticket (credit sizing vs dilution sizing)
def f46ow_f46_options_warrant_positioning_dbtwntticket_base_v106_signal(dbtvalue, dbtholders, wntvalue, wntholders):
    dt = _avg_ticket(dbtvalue, dbtholders)
    wt = _avg_ticket(wntvalue, wntholders)
    b = (dt - wt) / (dt + wt).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hedge intensity vs gross optionality (hedge purity of derivatives book)
def f46ow_f46_options_warrant_positioning_hedgepurity_base_v107_signal(putvalue, cllvalue):
    b = putvalue / (putvalue + cllvalue).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net bearish intensity z-scored vs 252d history (de-trended net put pressure)
def f46ow_f46_options_warrant_positioning_netbearz_base_v108_signal(putvalue, cllvalue, marketcap):
    net = (putvalue - cllvalue) / marketcap.replace(0, np.nan)
    b = _z(net, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang acceleration: change in its quarterly momentum
def f46ow_f46_options_warrant_positioning_wntaccel_base_v109_signal(wntvalue, marketcap):
    o = _warrant_overhang_mcap(wntvalue, marketcap)
    mom = o.diff(63)
    b = mom - mom.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt overhang ranked vs 504d history (credit overhang percentile)
def f46ow_f46_options_warrant_positioning_dbtoverrank_base_v110_signal(dbtvalue, totalvalue):
    o = _debt_overhang(dbtvalue, totalvalue)
    b = _rank(o, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total holder participation ranked (engagement breadth percentile)
def f46ow_f46_options_warrant_positioning_totholdrank_base_v111_signal(putholders, cllholders, wntholders, dbtholders):
    tot = putholders + cllholders + wntholders + dbtholders
    b = _rank(tot, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-holder concentration: avg put value per holder vs total avg ticket
def f46ow_f46_options_warrant_positioning_putticketrel_base_v112_signal(putvalue, putholders, totalvalue):
    pt = _avg_ticket(putvalue, putholders)
    b = _z(pt / totalvalue.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant units to share-value ratio (latent shares vs equity, dilution per dollar)
def f46ow_f46_options_warrant_positioning_wntunitshr_base_v113_signal(wntunits, shrvalue):
    b = _z(wntunits / shrvalue.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-value to share-value hedging ratio momentum
def f46ow_f46_options_warrant_positioning_putshrmom_base_v114_signal(putvalue, shrvalue):
    r = putvalue / shrvalue.replace(0, np.nan)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross overhang (warrant+debt) vs total reported value, smoothed
def f46ow_f46_options_warrant_positioning_grossoverT_base_v115_signal(wntvalue, dbtvalue, totalvalue):
    s = (wntvalue + dbtvalue) / totalvalue.replace(0, np.nan)
    b = s.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put/call holder skew vs put/call value skew divergence (breadth vs dollar tilt)
def f46ow_f46_options_warrant_positioning_skewdiverge_base_v116_signal(putholders, cllholders, putvalue, cllvalue):
    hs = _put_call_holder_skew(putholders, cllholders)
    vs = _put_call_value_skew(putvalue, cllvalue)
    b = hs - vs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call intensity exceedance over its 252d median (bullish surge band)
def f46ow_f46_options_warrant_positioning_callsurge_base_v117_signal(cllvalue, marketcap):
    c = _call_intensity(cllvalue, marketcap)
    med = c.rolling(252, min_periods=126).median()
    b = (c - med) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang half-life proxy: 21d mean over 126d mean (recent dilution tilt)
def f46ow_f46_options_warrant_positioning_wntfast_base_v118_signal(wntvalue, marketcap):
    o = _warrant_overhang_mcap(wntvalue, marketcap)
    b = _mean(o, 21) / _mean(o, 126).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal interacted with debt overhang (concentrated credit holders)
def f46ow_f46_options_warrant_positioning_pctdbt_base_v119_signal(percentoftotal, dbtvalue, totalvalue):
    o = _debt_overhang(dbtvalue, totalvalue)
    b = percentoftotal * o
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net optionality flow vs warrant overhang (bullish offset of dilution)
def f46ow_f46_options_warrant_positioning_bulloffset_base_v120_signal(cllvalue, putvalue, wntvalue, marketcap):
    net = (cllvalue - putvalue - wntvalue) / marketcap.replace(0, np.nan)
    b = net
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put hedging intensity year-over-year ratio (long hedge growth)
def f46ow_f46_options_warrant_positioning_hedgeyoyratio_base_v121_signal(putvalue, marketcap):
    h = _hedging_intensity(putvalue, marketcap)
    b = np.log(h.replace(0, np.nan) / h.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang year-over-year ratio (long dilution growth)
def f46ow_f46_options_warrant_positioning_wntyoyratio_base_v122_signal(wntvalue, marketcap):
    o = _warrant_overhang_mcap(wntvalue, marketcap)
    b = np.log(o.replace(0, np.nan) / o.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call accumulation year-over-year ratio (long bullish build)
def f46ow_f46_options_warrant_positioning_callyoyratio_base_v123_signal(cllvalue, marketcap):
    c = _call_intensity(cllvalue, marketcap)
    b = np.log(c.replace(0, np.nan) / c.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-holder fragmentation level (holders per put dollar) ranked vs 504d history
def f46ow_f46_options_warrant_positioning_putfragmom_base_v124_signal(putholders, putvalue):
    f = putholders / putvalue.replace(0, np.nan)
    b = _rank(f, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant unit per holder concentration momentum (dilution consolidation)
def f46ow_f46_options_warrant_positioning_wntconcmom_base_v125_signal(wntunits, wntholders):
    c = wntunits / wntholders.replace(0, np.nan)
    b = np.log(c.replace(0, np.nan) / c.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# derivatives value vs equity value share z (rotation extremity, mcap-based)
def f46ow_f46_options_warrant_positioning_derivmcapz_base_v126_signal(putvalue, cllvalue, wntvalue, marketcap):
    d = (putvalue + cllvalue + wntvalue) / marketcap.replace(0, np.nan)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite bearishness: put skew + warrant overhang + debt overhang, smoothed
def f46ow_f46_options_warrant_positioning_bearcomposite_base_v127_signal(putvalue, cllvalue, wntvalue, dbtvalue, totalvalue):
    skew = _put_call_value_skew(putvalue, cllvalue)
    over = (wntvalue + dbtvalue) / totalvalue.replace(0, np.nan)
    raw = skew + 4.0 * over
    b = raw.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put intensity dispersion over a half-year (hedge instability)
def f46ow_f46_options_warrant_positioning_hedgedisp126_base_v128_signal(putvalue, marketcap):
    h = _hedging_intensity(putvalue, marketcap)
    b = _std(h, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# call intensity dispersion over a half-year (accumulation instability)
def f46ow_f46_options_warrant_positioning_calldisp126_base_v129_signal(cllvalue, marketcap):
    c = _call_intensity(cllvalue, marketcap)
    b = _std(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant-holder count vs put-holder count tilt (dilution vs hedge constituency)
def f46ow_f46_options_warrant_positioning_wntputholdtilt_base_v130_signal(wntholders, putholders):
    b = (wntholders - putholders) / (wntholders + putholders).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total optionality value per holder (avg derivative engagement size) z
def f46ow_f46_options_warrant_positioning_optsizez_base_v131_signal(putvalue, cllvalue, putholders, cllholders):
    val = putvalue + cllvalue
    hold = putholders + cllholders
    b = _z(val / hold.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt overhang vs warrant overhang spread momentum (credit/dilution rotation)
def f46ow_f46_options_warrant_positioning_dbtwntsprmom_base_v132_signal(dbtvalue, wntvalue, totalvalue):
    spr = (dbtvalue - wntvalue) / totalvalue.replace(0, np.nan)
    b = spr - spr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put value vs marketcap exceedance over 504d max (extreme hedge regime distance)
def f46ow_f46_options_warrant_positioning_hedgeextreme_base_v133_signal(putvalue, marketcap):
    h = _hedging_intensity(putvalue, marketcap)
    b = _rank(h, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang regime distance from 504d median (latent dilution stretch)
def f46ow_f46_options_warrant_positioning_wntstretch_base_v134_signal(wntvalue, marketcap):
    o = _warrant_overhang_mcap(wntvalue, marketcap)
    med = o.rolling(504, min_periods=252).median()
    sd = o.rolling(504, min_periods=252).std()
    b = (o - med) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of quarters (504d) call intensity made a new 252d high (accumulation count)
def f46ow_f46_options_warrant_positioning_callnewhi_base_v135_signal(cllvalue, marketcap):
    c = _call_intensity(cllvalue, marketcap)
    hi = _rmax(c, 252)
    is_hi = (c >= hi * 0.99999).astype(float)
    b = is_hi.rolling(504, min_periods=252).sum() + 100.0 * c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put-skew momentum sign-weighted magnitude (compressed positioning change)
def f46ow_f46_options_warrant_positioning_skewsignmag_base_v136_signal(putvalue, cllvalue):
    s = _put_call_value_skew(putvalue, cllvalue)
    chg = s.diff(63)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang sign-weighted change (dilution accretion magnitude)
def f46ow_f46_options_warrant_positioning_wntchgsignmag_base_v137_signal(wntvalue, totalvalue):
    o = _warrant_overhang_total(wntvalue, totalvalue)
    chg = o.diff(63)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total derivative + credit overhang vs equity value (full latent claim) ranked
def f46ow_f46_options_warrant_positioning_fullclaimrank_base_v138_signal(putvalue, cllvalue, wntvalue, dbtvalue, shrvalue):
    claim = (putvalue + cllvalue + wntvalue + dbtvalue) / shrvalue.replace(0, np.nan)
    b = _rank(claim, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hedge intensity minus call intensity, ranked (net bearish percentile)
def f46ow_f46_options_warrant_positioning_netbearrank_base_v139_signal(putvalue, cllvalue, marketcap):
    net = (putvalue - cllvalue) / marketcap.replace(0, np.nan)
    b = _rank(net, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentoftotal trend (slope of filer-share over a half-year via mean spread)
def f46ow_f46_options_warrant_positioning_pcttrend_base_v140_signal(percentoftotal):
    b = _mean(percentoftotal, 42) - _mean(percentoftotal, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant value per unit (implied warrant price) vs its own 252d mean
def f46ow_f46_options_warrant_positioning_wntpxdev_base_v141_signal(wntvalue, wntunits):
    px = wntvalue / wntunits.replace(0, np.nan)
    b = px / _mean(px, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# put value per unit vs call value per unit ratio momentum (relative px shift)
def f46ow_f46_options_warrant_positioning_pcpxmom_base_v142_signal(putvalue, putunits, cllvalue, cllunits):
    pp = putvalue / putunits.replace(0, np.nan)
    cp = cllvalue / cllunits.replace(0, np.nan)
    r = pp / cp.replace(0, np.nan)
    b = np.log(r.replace(0, np.nan) / r.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt value vs total optionality value (credit dominance of latent claims)
def f46ow_f46_options_warrant_positioning_dbtdominance_base_v143_signal(dbtvalue, putvalue, cllvalue, wntvalue):
    b = dbtvalue / (putvalue + cllvalue + wntvalue + dbtvalue).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross optionality breadth: total option holders vs marketcap-scaled engagement
def f46ow_f46_options_warrant_positioning_optbreadthint_base_v144_signal(putholders, cllholders, putvalue, cllvalue, marketcap):
    breadth = (putholders + cllholders)
    intensity = (putvalue + cllvalue) / marketcap.replace(0, np.nan)
    b = _z(breadth, 252) * intensity
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# warrant overhang vs hedge intensity ratio (dilution-dominance of risk book)
def f46ow_f46_options_warrant_positioning_wnthedgeratio_base_v145_signal(wntvalue, putvalue):
    r = wntvalue / (wntvalue + putvalue).replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net derivative claim acceleration (2nd diff of (call-put-wnt)/mcap)
def f46ow_f46_options_warrant_positioning_claimaccel_base_v146_signal(cllvalue, putvalue, wntvalue, marketcap):
    net = (cllvalue - putvalue - wntvalue) / marketcap.replace(0, np.nan)
    mom = net.diff(63)
    b = mom - mom.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total reported value vs marketcap (filing coverage / float overlap) z
def f46ow_f46_options_warrant_positioning_coveragez_base_v147_signal(totalvalue, marketcap):
    b = _z(totalvalue / marketcap.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt holders breadth vs total option holders (credit constituency share)
def f46ow_f46_options_warrant_positioning_dbtholdshare_base_v148_signal(dbtholders, putholders, cllholders, wntholders):
    b = dbtholders / (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite positioning momentum: change in bull/bear balance over a quarter
def f46ow_f46_options_warrant_positioning_posmomcomp_base_v149_signal(putvalue, cllvalue, wntvalue, marketcap):
    bull = _call_intensity(cllvalue, marketcap)
    bear = (putvalue + wntvalue) / marketcap.replace(0, np.nan)
    raw = (bull - bear) / (bull + bear).replace(0, np.nan)
    b = raw - raw.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang pressure ranked vs 1260d history (multi-year latent supply percentile)
def f46ow_f46_options_warrant_positioning_overhangrank_base_v150_signal(wntvalue, dbtvalue, putvalue, marketcap):
    p = (wntvalue + dbtvalue + putvalue) / marketcap.replace(0, np.nan)
    b = _rank(p, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46ow_f46_options_warrant_positioning_pcholdskewsm_base_v076_signal,
    f46ow_f46_options_warrant_positioning_pcvalskewdev_base_v077_signal,
    f46ow_f46_options_warrant_positioning_hedgelvl126_base_v078_signal,
    f46ow_f46_options_warrant_positioning_callrank_base_v079_signal,
    f46ow_f46_options_warrant_positioning_wntoverTrank_base_v080_signal,
    f46ow_f46_options_warrant_positioning_dbtovermom_base_v081_signal,
    f46ow_f46_options_warrant_positioning_hedgevswnt_base_v082_signal,
    f46ow_f46_options_warrant_positioning_callvswnt_base_v083_signal,
    f46ow_f46_options_warrant_positioning_dbtequitymom_base_v084_signal,
    f46ow_f46_options_warrant_positioning_putbreadthrank_base_v085_signal,
    f46ow_f46_options_warrant_positioning_callbreadthrank_base_v086_signal,
    f46ow_f46_options_warrant_positioning_wntbreadthrank_base_v087_signal,
    f46ow_f46_options_warrant_positioning_putticketmom_base_v088_signal,
    f46ow_f46_options_warrant_positioning_callticketmom_base_v089_signal,
    f46ow_f46_options_warrant_positioning_wntticketmom_base_v090_signal,
    f46ow_f46_options_warrant_positioning_unitskew_base_v091_signal,
    f46ow_f46_options_warrant_positioning_wntunitshare_base_v092_signal,
    f46ow_f46_options_warrant_positioning_grossoptsm_base_v093_signal,
    f46ow_f46_options_warrant_positioning_latentmom_base_v094_signal,
    f46ow_f46_options_warrant_positioning_pctz_base_v095_signal,
    f46ow_f46_options_warrant_positioning_pctwntmom_base_v096_signal,
    f46ow_f46_options_warrant_positioning_hedgeexceed_base_v097_signal,
    f46ow_f46_options_warrant_positioning_wntdrawup_base_v098_signal,
    f46ow_f46_options_warrant_positioning_skewflips_base_v099_signal,
    f46ow_f46_options_warrant_positioning_bullregime_base_v100_signal,
    f46ow_f46_options_warrant_positioning_wntstreak_base_v101_signal,
    f46ow_f46_options_warrant_positioning_derivturn_base_v102_signal,
    f46ow_f46_options_warrant_positioning_putoptshare_base_v103_signal,
    f46ow_f46_options_warrant_positioning_calloptshare_base_v104_signal,
    f46ow_f46_options_warrant_positioning_dbtwntholdtilt_base_v105_signal,
    f46ow_f46_options_warrant_positioning_dbtwntticket_base_v106_signal,
    f46ow_f46_options_warrant_positioning_hedgepurity_base_v107_signal,
    f46ow_f46_options_warrant_positioning_netbearz_base_v108_signal,
    f46ow_f46_options_warrant_positioning_wntaccel_base_v109_signal,
    f46ow_f46_options_warrant_positioning_dbtoverrank_base_v110_signal,
    f46ow_f46_options_warrant_positioning_totholdrank_base_v111_signal,
    f46ow_f46_options_warrant_positioning_putticketrel_base_v112_signal,
    f46ow_f46_options_warrant_positioning_wntunitshr_base_v113_signal,
    f46ow_f46_options_warrant_positioning_putshrmom_base_v114_signal,
    f46ow_f46_options_warrant_positioning_grossoverT_base_v115_signal,
    f46ow_f46_options_warrant_positioning_skewdiverge_base_v116_signal,
    f46ow_f46_options_warrant_positioning_callsurge_base_v117_signal,
    f46ow_f46_options_warrant_positioning_wntfast_base_v118_signal,
    f46ow_f46_options_warrant_positioning_pctdbt_base_v119_signal,
    f46ow_f46_options_warrant_positioning_bulloffset_base_v120_signal,
    f46ow_f46_options_warrant_positioning_hedgeyoyratio_base_v121_signal,
    f46ow_f46_options_warrant_positioning_wntyoyratio_base_v122_signal,
    f46ow_f46_options_warrant_positioning_callyoyratio_base_v123_signal,
    f46ow_f46_options_warrant_positioning_putfragmom_base_v124_signal,
    f46ow_f46_options_warrant_positioning_wntconcmom_base_v125_signal,
    f46ow_f46_options_warrant_positioning_derivmcapz_base_v126_signal,
    f46ow_f46_options_warrant_positioning_bearcomposite_base_v127_signal,
    f46ow_f46_options_warrant_positioning_hedgedisp126_base_v128_signal,
    f46ow_f46_options_warrant_positioning_calldisp126_base_v129_signal,
    f46ow_f46_options_warrant_positioning_wntputholdtilt_base_v130_signal,
    f46ow_f46_options_warrant_positioning_optsizez_base_v131_signal,
    f46ow_f46_options_warrant_positioning_dbtwntsprmom_base_v132_signal,
    f46ow_f46_options_warrant_positioning_hedgeextreme_base_v133_signal,
    f46ow_f46_options_warrant_positioning_wntstretch_base_v134_signal,
    f46ow_f46_options_warrant_positioning_callnewhi_base_v135_signal,
    f46ow_f46_options_warrant_positioning_skewsignmag_base_v136_signal,
    f46ow_f46_options_warrant_positioning_wntchgsignmag_base_v137_signal,
    f46ow_f46_options_warrant_positioning_fullclaimrank_base_v138_signal,
    f46ow_f46_options_warrant_positioning_netbearrank_base_v139_signal,
    f46ow_f46_options_warrant_positioning_pcttrend_base_v140_signal,
    f46ow_f46_options_warrant_positioning_wntpxdev_base_v141_signal,
    f46ow_f46_options_warrant_positioning_pcpxmom_base_v142_signal,
    f46ow_f46_options_warrant_positioning_dbtdominance_base_v143_signal,
    f46ow_f46_options_warrant_positioning_optbreadthint_base_v144_signal,
    f46ow_f46_options_warrant_positioning_wnthedgeratio_base_v145_signal,
    f46ow_f46_options_warrant_positioning_claimaccel_base_v146_signal,
    f46ow_f46_options_warrant_positioning_coveragez_base_v147_signal,
    f46ow_f46_options_warrant_positioning_dbtholdshare_base_v148_signal,
    f46ow_f46_options_warrant_positioning_posmomcomp_base_v149_signal,
    f46ow_f46_options_warrant_positioning_overhangrank_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_OPTIONS_WARRANT_POSITIONING_REGISTRY_076_150 = REGISTRY


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

    print("OK f46_options_warrant_positioning_base_076_150_claude: %d features pass" % n_features)
