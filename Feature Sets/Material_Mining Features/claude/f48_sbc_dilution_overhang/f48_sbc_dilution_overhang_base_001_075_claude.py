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


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _macd(s, a, b):
    # fast-minus-slow EWM band-pass of a series
    return s.ewm(span=a, min_periods=max(2, a // 2)).mean() - s.ewm(span=b, min_periods=max(3, b // 2)).mean()


# ===== folder domain primitives (stock-based-comp dilution overhang) =====
def _f48_dilrate(sbcomp, marketcap):
    # annualized SBC dilution rate = stock comp as a fraction of market cap
    return sbcomp / marketcap.replace(0, np.nan)


def _f48_promote(sbcomp, opex):
    # promote intensity = SBC as a fraction of total operating expense
    return sbcomp / opex.replace(0, np.nan)


def _f48_sgna_load(sbcomp, sgna):
    # SBC as a fraction of SG&A (where stock comp usually books)
    return sbcomp / sgna.replace(0, np.nan)


def _f48_rev_load(sbcomp, revenue):
    # SBC per dollar of revenue (meaningful for producers)
    return sbcomp / revenue.replace(0, np.nan)


def _f48_burn_subsidy(sbcomp, ncfo):
    # non-cash comp subsidy relative to the magnitude of operating cash burn
    return sbcomp / ncfo.abs().replace(0, np.nan)


def _f48_overhang(shareswadil, shareswa):
    # diluted-vs-basic share overhang from options / RSUs / warrants
    return shareswadil / shareswa.replace(0, np.nan) - 1.0


def _f48_papermix(sbcomp, ncfcommon):
    # paper-vs-cash mix: SBC vs net cash raised from common (ncfcommon swings sign)
    return sbcomp / (sbcomp + ncfcommon.abs()).replace(0, np.nan)


def _f48_growth(s, w):
    # log growth of a (possibly negative) fundamental series over w days, on magnitude
    return np.log(s.abs().replace(0, np.nan) / s.shift(w).abs().replace(0, np.nan))


def _f48_truedil(sbcomp, marketcap, shareswa, w):
    # combined true dilution = SBC/mktcap + realized weighted-share growth
    rate = sbcomp / marketcap.replace(0, np.nan)
    grow = shareswa / shareswa.shift(w).replace(0, np.nan) - 1.0
    return rate + grow


# annualized SBC dilution rate (SBC/marketcap), smoothed over a quarter
def f48sb_f48_sbc_dilution_overhang_dilrate_63d_base_v001_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = r.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# SBC dilution rate z-scored vs its own 252d history (de-trended overhang level)
def f48sb_f48_sbc_dilution_overhang_dilrate_252d_base_v002_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# SBC dilution rate percentile-ranked vs its own 504d history
def f48sb_f48_sbc_dilution_overhang_dilrate_504d_base_v003_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = _rank(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# log SBC dilution rate (compresses the heavy right tail of overhang)
def f48sb_f48_sbc_dilution_overhang_dilratelog_252d_base_v004_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = np.log1p(r.clip(lower=0))
    return result.replace([np.inf, -np.inf], np.nan)

# dispersion (126d std) of the SBC dilution rate (overhang instability)
def f48sb_f48_sbc_dilution_overhang_dilratedisp_126d_base_v005_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = _std(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# promote intensity (SBC/opex), smoothed over a quarter
def f48sb_f48_sbc_dilution_overhang_promote_63d_base_v006_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    result = p.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# promote intensity z-scored vs its own 252d history
def f48sb_f48_sbc_dilution_overhang_promote_252d_base_v007_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    result = _z(p, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# promote intensity percentile-ranked vs its 504d history
def f48sb_f48_sbc_dilution_overhang_promote_504d_base_v008_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    result = _rank(p, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# promote intensity minus its slow 252d EMA (displacement from norm)
def f48sb_f48_sbc_dilution_overhang_promotedev_252d_base_v009_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    result = p - p.ewm(span=252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# SBC as fraction of SG&A, smoothed over a quarter
def f48sb_f48_sbc_dilution_overhang_sgnaload_63d_base_v010_signal(sbcomp, sgna):
    g = _f48_sgna_load(sbcomp, sgna)
    result = g.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# SBC/SG&A load z-scored vs its own 252d history
def f48sb_f48_sbc_dilution_overhang_sgnaload_252d_base_v011_signal(sbcomp, sgna):
    g = _f48_sgna_load(sbcomp, sgna)
    result = _z(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# tanh-squashed SBC/SG&A load deviation from its 126d median
def f48sb_f48_sbc_dilution_overhang_sgnaloadtanh_126d_base_v012_signal(sbcomp, sgna):
    g = _f48_sgna_load(sbcomp, sgna)
    med = g.rolling(126, min_periods=42).median()
    result = np.tanh(3.0 * (g - med))
    return result.replace([np.inf, -np.inf], np.nan)

# SBC per dollar of revenue (producer overhang), smoothed
def f48sb_f48_sbc_dilution_overhang_revload_63d_base_v013_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    result = rl.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# SBC/revenue load z-scored vs its own 252d history
def f48sb_f48_sbc_dilution_overhang_revload_252d_base_v014_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    result = _z(rl, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# SBC/revenue load percentile-ranked vs its 504d history
def f48sb_f48_sbc_dilution_overhang_revload_504d_base_v015_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    result = _rank(rl, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# log SBC/revenue load (tail-compressed producer dilution burden)
def f48sb_f48_sbc_dilution_overhang_revloadlog_252d_base_v016_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    result = np.log1p(rl.clip(lower=0))
    return result.replace([np.inf, -np.inf], np.nan)

# non-cash SBC subsidy to operating cash burn (SBC/|ncfo|), smoothed
def f48sb_f48_sbc_dilution_overhang_burnsub_63d_base_v017_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo)
    result = bs.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# burn-subsidy ratio z-scored vs its 252d history
def f48sb_f48_sbc_dilution_overhang_burnsub_252d_base_v018_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo)
    result = _z(bs, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# burn-subsidy ratio percentile-ranked vs its 504d history
def f48sb_f48_sbc_dilution_overhang_burnsub_504d_base_v019_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo)
    result = _rank(bs, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# capped burn-subsidy ratio: how much of cash burn is plugged by paper comp
def f48sb_f48_sbc_dilution_overhang_burnsubcap_126d_base_v020_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo)
    result = bs.clip(upper=5.0).rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# cash-burn coverage balance: (burn - SBC)/(burn + SBC), bounded [-1,1]
def f48sb_f48_sbc_dilution_overhang_burncover_252d_base_v021_signal(sbcomp, ncfo):
    burn = (-ncfo).clip(lower=0)
    bal = (burn - sbcomp) / (burn + sbcomp).replace(0, np.nan)
    result = bal.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# diluted-vs-basic share overhang (options/RSUs/warrants), current level
def f48sb_f48_sbc_dilution_overhang_overhang_1d_base_v022_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    result = o
    return result.replace([np.inf, -np.inf], np.nan)

# share overhang z-scored vs its own 252d history
def f48sb_f48_sbc_dilution_overhang_overhang_252d_base_v023_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    result = _z(o, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# share overhang percentile-ranked vs its 504d history
def f48sb_f48_sbc_dilution_overhang_overhang_504d_base_v024_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    result = _rank(o, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# share-overhang trend: current overhang minus its level 252d ago
def f48sb_f48_sbc_dilution_overhang_overhangtrend_252d_base_v025_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    result = o - o.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)

# dispersion (126d std) of share overhang (option-grant lumpiness)
def f48sb_f48_sbc_dilution_overhang_overhangdisp_126d_base_v026_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    result = _std(o, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# paper-vs-cash comp/financing mix (SBC share of SBC+|ncfcommon|), smoothed
def f48sb_f48_sbc_dilution_overhang_papermix_63d_base_v027_signal(sbcomp, ncfcommon):
    m = _f48_papermix(sbcomp, ncfcommon)
    result = m.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# paper-vs-cash mix z-scored vs its 252d history
def f48sb_f48_sbc_dilution_overhang_papermix_252d_base_v028_signal(sbcomp, ncfcommon):
    m = _f48_papermix(sbcomp, ncfcommon)
    result = _z(m, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# fraction of last year SBC dominates net cash raised (paper-dominant regime)
def f48sb_f48_sbc_dilution_overhang_paperdom_252d_base_v029_signal(sbcomp, ncfcommon):
    dom = (sbcomp > ncfcommon.abs()).astype(float)
    result = dom.rolling(252, min_periods=84).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# combined true dilution (SBC/mktcap + 252d weighted-share growth)
def f48sb_f48_sbc_dilution_overhang_truedil_252d_base_v030_signal(sbcomp, marketcap, shareswa):
    t = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    result = t.rolling(21, min_periods=7).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# combined true dilution over a two-year share-growth window
def f48sb_f48_sbc_dilution_overhang_truedil_504d_base_v031_signal(sbcomp, marketcap, shareswa):
    t = _f48_truedil(sbcomp, marketcap, shareswa, 504)
    result = t.rolling(21, min_periods=7).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# combined true dilution z-scored vs its 252d history
def f48sb_f48_sbc_dilution_overhang_truedilz_252d_base_v032_signal(sbcomp, marketcap, shareswa):
    t = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    result = _z(t, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# annual SBC growth (log), the silent-dilution expansion rate
def f48sb_f48_sbc_dilution_overhang_sbcgrow_252d_base_v033_signal(sbcomp):
    result = _f48_growth(sbcomp, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# quarterly SBC growth rate
def f48sb_f48_sbc_dilution_overhang_sbcgrow_63d_base_v034_signal(sbcomp):
    result = sbcomp / sbcomp.shift(63).replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# SBC acceleration: 63d growth now vs 63d growth a quarter ago
def f48sb_f48_sbc_dilution_overhang_sbcaccel_252d_base_v035_signal(sbcomp):
    g = sbcomp / sbcomp.shift(63).replace(0, np.nan) - 1.0
    result = g - g.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

# interaction: SBC dilution rate times share overhang (double-channel overhang)
def f48sb_f48_sbc_dilution_overhang_dilrateXoverhang_252d_base_v036_signal(sbcomp, marketcap, shareswadil, shareswa):
    r = _f48_dilrate(sbcomp, marketcap)
    o = _f48_overhang(shareswadil, shareswa)
    result = (r * o).rolling(21, min_periods=7).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# spread: promote intensity (SBC/opex) minus revenue load (SBC/revenue)
def f48sb_f48_sbc_dilution_overhang_promotevsrev_252d_base_v037_signal(sbcomp, opex, revenue):
    p = _f48_promote(sbcomp, opex)
    rl = _f48_rev_load(sbcomp, revenue)
    result = p - rl
    return result.replace([np.inf, -np.inf], np.nan)

# short-vs-long SBC dilution-rate spread (63d mean minus 252d mean)
def f48sb_f48_sbc_dilution_overhang_dilratespr_252d_base_v038_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = r.rolling(63, min_periods=21).mean() - r.rolling(252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# share-overhang short-vs-long spread (21d mean minus 252d mean)
def f48sb_f48_sbc_dilution_overhang_overhangspr_252d_base_v039_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    result = o.rolling(21, min_periods=7).mean() - o.rolling(252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# sign x sqrt-magnitude of burn-subsidy deviation from its 252d mean
def f48sb_f48_sbc_dilution_overhang_burnsubsignmag_252d_base_v040_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=8.0)
    d = bs - bs.rolling(252, min_periods=84).mean()
    result = np.sign(d) * d.abs() ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# high-promote regime distance: promote intensity vs its 252d 75th pct band
def f48sb_f48_sbc_dilution_overhang_promotergime_252d_base_v041_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    q75 = p.rolling(252, min_periods=84).quantile(0.75)
    result = (p - q75)
    return result.replace([np.inf, -np.inf], np.nan)

# EWM-smoothed SBC dilution rate minus its raw value (persistence gap)
def f48sb_f48_sbc_dilution_overhang_dilrateewm_126d_base_v042_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = r.ewm(span=126, min_periods=42).mean() - r
    return result.replace([np.inf, -np.inf], np.nan)

# interaction: SBC/revenue load times revenue-contraction depth (overhang as the top line shrinks)
def f48sb_f48_sbc_dilution_overhang_revloadXcontr_252d_base_v043_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    gr = _f48_growth(revenue, 126)
    depth = (-gr).clip(lower=0)
    result = (rl * depth).rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# share-overhang acceleration: 63d change now vs 63d change a quarter ago
def f48sb_f48_sbc_dilution_overhang_overhangaccel_252d_base_v044_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    d = o - o.shift(63)
    result = d - d.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)

# composite: paper-mix times share overhang (paper comp amplifying option overhang)
def f48sb_f48_sbc_dilution_overhang_sbcoverhangmix_252d_base_v045_signal(sbcomp, ncfcommon, shareswadil, shareswa):
    m = _f48_papermix(sbcomp, ncfcommon)
    o = _f48_overhang(shareswadil, shareswa)
    result = (m * o).rolling(21, min_periods=7).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# peak SBC dilution rate over the last year (worst overhang spike)
def f48sb_f48_sbc_dilution_overhang_dilratemax_252d_base_v046_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = _rmax(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# current SBC dilution rate relative to its 252d minimum (overhang drawup)
def f48sb_f48_sbc_dilution_overhang_dilratedrawup_252d_base_v047_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    lo = _rmin(r, 252)
    result = r / lo.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# peak promote intensity over the last year
def f48sb_f48_sbc_dilution_overhang_promotemax_252d_base_v048_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    result = _rmax(p, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# peak burn-subsidy ratio over the last year (max paper plug of cash burn)
def f48sb_f48_sbc_dilution_overhang_burnsubmax_252d_base_v049_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    result = _rmax(bs, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# peak share overhang over the last year
def f48sb_f48_sbc_dilution_overhang_overhangmax_252d_base_v050_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    result = _rmax(o, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# SBC/SG&A load percentile-ranked vs its 504d history
def f48sb_f48_sbc_dilution_overhang_sgnaloadrank_504d_base_v051_signal(sbcomp, sgna):
    g = _f48_sgna_load(sbcomp, sgna)
    result = _rank(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# paper-vs-cash mix percentile-ranked vs its 504d history
def f48sb_f48_sbc_dilution_overhang_papermixrank_504d_base_v052_signal(sbcomp, ncfcommon):
    m = _f48_papermix(sbcomp, ncfcommon)
    result = _rank(m, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# combined true dilution percentile-ranked vs its 504d history
def f48sb_f48_sbc_dilution_overhang_truedilrank_504d_base_v053_signal(sbcomp, marketcap, shareswa):
    t = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    result = _rank(t, 504)
    return result.replace([np.inf, -np.inf], np.nan)

# annual SBC growth z-scored vs its 252d history
def f48sb_f48_sbc_dilution_overhang_sbcgrowz_252d_base_v054_signal(sbcomp):
    g = _f48_growth(sbcomp, 252)
    result = _z(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# SBC growth minus market-cap growth (overhang outpacing valuation)
def f48sb_f48_sbc_dilution_overhang_sbcvsmcapgrow_252d_base_v055_signal(sbcomp, marketcap):
    gs = _f48_growth(sbcomp, 252)
    gm = _f48_growth(marketcap, 252)
    result = gs - gm
    return result.replace([np.inf, -np.inf], np.nan)

# SBC growth minus revenue growth (comp inflating faster than the business)
def f48sb_f48_sbc_dilution_overhang_sbcvsrevgrow_252d_base_v056_signal(sbcomp, revenue):
    gs = _f48_growth(sbcomp, 252)
    gr = _f48_growth(revenue, 252)
    result = gs - gr
    return result.replace([np.inf, -np.inf], np.nan)

# dispersion of promote intensity (grant-timing lumpiness)
def f48sb_f48_sbc_dilution_overhang_promotedisp_126d_base_v057_signal(sbcomp, opex):
    p = _f48_promote(sbcomp, opex)
    result = _std(p, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# dispersion of SBC/revenue load
def f48sb_f48_sbc_dilution_overhang_revloaddisp_126d_base_v058_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    result = _std(rl, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# coefficient of variation of SBC dilution rate (relative overhang volatility)
def f48sb_f48_sbc_dilution_overhang_dilratecv_252d_base_v059_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = _std(r, 252) / _mean(r, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# coefficient of variation of share overhang
def f48sb_f48_sbc_dilution_overhang_overhangcv_252d_base_v060_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    result = _std(o, 252) / _mean(o, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# current streak length of SBC-dominant comp months (paper-dominant persistence)
def f48sb_f48_sbc_dilution_overhang_paperdomstreak_252d_base_v061_signal(sbcomp, ncfcommon):
    cond = (sbcomp > ncfcommon.abs())
    grp = (~cond).cumsum()
    streak = cond.groupby(grp).cumsum()
    result = streak.rolling(21, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# streak length of consecutive rising-SBC periods (persistent silent-dilution expansion)
def f48sb_f48_sbc_dilution_overhang_sbcgrowstreak_252d_base_v062_signal(sbcomp):
    rising = (sbcomp.diff(21) > 0)
    grp = (~rising).cumsum()
    streak = rising.groupby(grp).cumsum()
    result = streak.rolling(21, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# rising-overhang regime: fraction of last year SBC dilution rate above its 252d median
def f48sb_f48_sbc_dilution_overhang_dilrateupreg_252d_base_v063_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    med = r.rolling(252, min_periods=84).median()
    result = (r > med).astype(float).rolling(252, min_periods=84).mean() - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

# spread: promote intensity (SBC/opex) minus SG&A load (SBC/sgna)
def f48sb_f48_sbc_dilution_overhang_promotevssgna_252d_base_v064_signal(sbcomp, opex, sgna):
    p = _f48_promote(sbcomp, opex)
    g = _f48_sgna_load(sbcomp, sgna)
    result = p - g
    return result.replace([np.inf, -np.inf], np.nan)

# channel dominance: standardized share overhang minus standardized SBC/revenue load
def f48sb_f48_sbc_dilution_overhang_overhangVrev_252d_base_v065_signal(shareswadil, shareswa, sbcomp, revenue):
    o = _z(_f48_overhang(shareswadil, shareswa), 252)
    rl = _z(_f48_rev_load(sbcomp, revenue), 252)
    result = o - rl
    return result.replace([np.inf, -np.inf], np.nan)

# combined true dilution scaled up when ncfo is negative (overhang during cash burn)
def f48sb_f48_sbc_dilution_overhang_truedilburn_252d_base_v066_signal(sbcomp, marketcap, shareswa, ncfo):
    t = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    neg = (ncfo < 0).astype(float)
    result = (t * (1.0 + neg)).rolling(21, min_periods=7).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# SBC dilution rate change over a half-year (overhang momentum)
def f48sb_f48_sbc_dilution_overhang_dilratehalf_126d_base_v067_signal(sbcomp, marketcap):
    r = _f48_dilrate(sbcomp, marketcap)
    result = r - r.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

# burn-subsidy change over a half-year
def f48sb_f48_sbc_dilution_overhang_burnsubhalf_126d_base_v068_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=8.0)
    result = bs - bs.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)

# SBC dilution rate as a share of combined true dilution (paper vs realized issuance mix)
def f48sb_f48_sbc_dilution_overhang_sbcsharemix_252d_base_v069_signal(sbcomp, marketcap, shareswa):
    r = _f48_dilrate(sbcomp, marketcap)
    t = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    result = r / t.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# EWM burn-subsidy ratio minus its raw level (cash-plug persistence gap)
def f48sb_f48_sbc_dilution_overhang_burnsubewm_126d_base_v070_signal(sbcomp, ncfo):
    bs = _f48_burn_subsidy(sbcomp, ncfo).clip(upper=10.0)
    result = bs.ewm(span=126, min_periods=42).mean() - bs
    return result.replace([np.inf, -np.inf], np.nan)

# peak SBC/SG&A load over the last year
def f48sb_f48_sbc_dilution_overhang_sgnaloadmax_252d_base_v071_signal(sbcomp, sgna):
    g = _f48_sgna_load(sbcomp, sgna)
    result = _rmax(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# peak SBC/revenue load over the last year
def f48sb_f48_sbc_dilution_overhang_revloadmax_252d_base_v072_signal(sbcomp, revenue):
    rl = _f48_rev_load(sbcomp, revenue)
    result = _rmax(rl, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# streak length of consecutive rising-overhang periods (dilutive securities accumulating)
def f48sb_f48_sbc_dilution_overhang_overhangrisestreak_252d_base_v073_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    cond = (o.diff(21) > 0)
    grp = (~cond).cumsum()
    streak = cond.groupby(grp).cumsum()
    result = streak.rolling(21, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# combined true dilution minus its slow EMA (overhang displacement)
def f48sb_f48_sbc_dilution_overhang_truedilewm_252d_base_v074_signal(sbcomp, marketcap, shareswa):
    t = _f48_truedil(sbcomp, marketcap, shareswa, 252)
    result = t - t.ewm(span=252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)

# share overhang relative to its 252d minimum (overhang expansion off the floor)
def f48sb_f48_sbc_dilution_overhang_overhangloratio_252d_base_v075_signal(shareswadil, shareswa):
    o = _f48_overhang(shareswadil, shareswa)
    lo = _rmin(o, 252)
    result = o / lo.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f48sb_f48_sbc_dilution_overhang_dilrate_63d_base_v001_signal,
    f48sb_f48_sbc_dilution_overhang_dilrate_252d_base_v002_signal,
    f48sb_f48_sbc_dilution_overhang_dilrate_504d_base_v003_signal,
    f48sb_f48_sbc_dilution_overhang_dilratelog_252d_base_v004_signal,
    f48sb_f48_sbc_dilution_overhang_dilratedisp_126d_base_v005_signal,
    f48sb_f48_sbc_dilution_overhang_promote_63d_base_v006_signal,
    f48sb_f48_sbc_dilution_overhang_promote_252d_base_v007_signal,
    f48sb_f48_sbc_dilution_overhang_promote_504d_base_v008_signal,
    f48sb_f48_sbc_dilution_overhang_promotedev_252d_base_v009_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaload_63d_base_v010_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaload_252d_base_v011_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaloadtanh_126d_base_v012_signal,
    f48sb_f48_sbc_dilution_overhang_revload_63d_base_v013_signal,
    f48sb_f48_sbc_dilution_overhang_revload_252d_base_v014_signal,
    f48sb_f48_sbc_dilution_overhang_revload_504d_base_v015_signal,
    f48sb_f48_sbc_dilution_overhang_revloadlog_252d_base_v016_signal,
    f48sb_f48_sbc_dilution_overhang_burnsub_63d_base_v017_signal,
    f48sb_f48_sbc_dilution_overhang_burnsub_252d_base_v018_signal,
    f48sb_f48_sbc_dilution_overhang_burnsub_504d_base_v019_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubcap_126d_base_v020_signal,
    f48sb_f48_sbc_dilution_overhang_burncover_252d_base_v021_signal,
    f48sb_f48_sbc_dilution_overhang_overhang_1d_base_v022_signal,
    f48sb_f48_sbc_dilution_overhang_overhang_252d_base_v023_signal,
    f48sb_f48_sbc_dilution_overhang_overhang_504d_base_v024_signal,
    f48sb_f48_sbc_dilution_overhang_overhangtrend_252d_base_v025_signal,
    f48sb_f48_sbc_dilution_overhang_overhangdisp_126d_base_v026_signal,
    f48sb_f48_sbc_dilution_overhang_papermix_63d_base_v027_signal,
    f48sb_f48_sbc_dilution_overhang_papermix_252d_base_v028_signal,
    f48sb_f48_sbc_dilution_overhang_paperdom_252d_base_v029_signal,
    f48sb_f48_sbc_dilution_overhang_truedil_252d_base_v030_signal,
    f48sb_f48_sbc_dilution_overhang_truedil_504d_base_v031_signal,
    f48sb_f48_sbc_dilution_overhang_truedilz_252d_base_v032_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrow_252d_base_v033_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrow_63d_base_v034_signal,
    f48sb_f48_sbc_dilution_overhang_sbcaccel_252d_base_v035_signal,
    f48sb_f48_sbc_dilution_overhang_dilrateXoverhang_252d_base_v036_signal,
    f48sb_f48_sbc_dilution_overhang_promotevsrev_252d_base_v037_signal,
    f48sb_f48_sbc_dilution_overhang_dilratespr_252d_base_v038_signal,
    f48sb_f48_sbc_dilution_overhang_overhangspr_252d_base_v039_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubsignmag_252d_base_v040_signal,
    f48sb_f48_sbc_dilution_overhang_promotergime_252d_base_v041_signal,
    f48sb_f48_sbc_dilution_overhang_dilrateewm_126d_base_v042_signal,
    f48sb_f48_sbc_dilution_overhang_revloadXcontr_252d_base_v043_signal,
    f48sb_f48_sbc_dilution_overhang_overhangaccel_252d_base_v044_signal,
    f48sb_f48_sbc_dilution_overhang_sbcoverhangmix_252d_base_v045_signal,
    f48sb_f48_sbc_dilution_overhang_dilratemax_252d_base_v046_signal,
    f48sb_f48_sbc_dilution_overhang_dilratedrawup_252d_base_v047_signal,
    f48sb_f48_sbc_dilution_overhang_promotemax_252d_base_v048_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubmax_252d_base_v049_signal,
    f48sb_f48_sbc_dilution_overhang_overhangmax_252d_base_v050_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaloadrank_504d_base_v051_signal,
    f48sb_f48_sbc_dilution_overhang_papermixrank_504d_base_v052_signal,
    f48sb_f48_sbc_dilution_overhang_truedilrank_504d_base_v053_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowz_252d_base_v054_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsmcapgrow_252d_base_v055_signal,
    f48sb_f48_sbc_dilution_overhang_sbcvsrevgrow_252d_base_v056_signal,
    f48sb_f48_sbc_dilution_overhang_promotedisp_126d_base_v057_signal,
    f48sb_f48_sbc_dilution_overhang_revloaddisp_126d_base_v058_signal,
    f48sb_f48_sbc_dilution_overhang_dilratecv_252d_base_v059_signal,
    f48sb_f48_sbc_dilution_overhang_overhangcv_252d_base_v060_signal,
    f48sb_f48_sbc_dilution_overhang_paperdomstreak_252d_base_v061_signal,
    f48sb_f48_sbc_dilution_overhang_sbcgrowstreak_252d_base_v062_signal,
    f48sb_f48_sbc_dilution_overhang_dilrateupreg_252d_base_v063_signal,
    f48sb_f48_sbc_dilution_overhang_promotevssgna_252d_base_v064_signal,
    f48sb_f48_sbc_dilution_overhang_overhangVrev_252d_base_v065_signal,
    f48sb_f48_sbc_dilution_overhang_truedilburn_252d_base_v066_signal,
    f48sb_f48_sbc_dilution_overhang_dilratehalf_126d_base_v067_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubhalf_126d_base_v068_signal,
    f48sb_f48_sbc_dilution_overhang_sbcsharemix_252d_base_v069_signal,
    f48sb_f48_sbc_dilution_overhang_burnsubewm_126d_base_v070_signal,
    f48sb_f48_sbc_dilution_overhang_sgnaloadmax_252d_base_v071_signal,
    f48sb_f48_sbc_dilution_overhang_revloadmax_252d_base_v072_signal,
    f48sb_f48_sbc_dilution_overhang_overhangrisestreak_252d_base_v073_signal,
    f48sb_f48_sbc_dilution_overhang_truedilewm_252d_base_v074_signal,
    f48sb_f48_sbc_dilution_overhang_overhangloratio_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_SBC_DILUTION_OVERHANG_REGISTRY_001_075 = REGISTRY


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

    sbcomp = _fund(201, base=1.2e7, drift=0.03, vol=0.10).rename("sbcomp")
    opex = _fund(202, base=6.0e7, drift=0.02, vol=0.07).rename("opex")
    sgna = _fund(203, base=2.4e7, drift=0.02, vol=0.08).rename("sgna")
    revenue = _fund(204, base=5.0e7, drift=0.025, vol=0.12).rename("revenue")
    marketcap = _fund(205, base=4.0e8, drift=0.01, vol=0.18).rename("marketcap")
    shareswa = _fund(206, base=7.6e7, drift=0.038, vol=0.05).rename("shareswa")
    _gap = _fund(207, base=6.0e6, drift=0.04, vol=0.09).abs()
    shareswadil = (shareswa + _gap).rename("shareswadil")
    _raise = _fund(208, base=2.0e7, drift=0.02, vol=0.5)
    _return = _fund(209, base=1.6e7, drift=0.02, vol=0.45)
    ncfcommon = (_return - _raise).rename("ncfcommon")
    _burn = _fund(210, base=3.0e7, drift=0.015, vol=0.20)
    ncfo = (_burn - 3.0e7 * 0.9).rename("ncfo")

    cols = {"sbcomp": sbcomp, "opex": opex, "sgna": sgna, "revenue": revenue,
            "marketcap": marketcap, "shareswa": shareswa,
            "shareswadil": shareswadil, "ncfcommon": ncfcommon, "ncfo": ncfo}

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

    print("OK f48_sbc_dilution_overhang_base_001_075_claude: %d features pass" % n_features)
