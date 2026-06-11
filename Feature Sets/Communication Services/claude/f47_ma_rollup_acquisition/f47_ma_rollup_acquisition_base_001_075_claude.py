import inspect
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# f47_ma_rollup_acquisition -- BASE file 001..075.
# Domain: M&A / ROLL-UP & ACQUISITION CADENCE for serial-acquirer comm-services
# names. Signals quantify acquisition intensity, cadence, ops-vs-external funding
# of deals, goodwill/intangible build (overpayment proxy), stake-building via the
# investments balance, net acquirer-vs-divestor sign, trailing deal spend vs
# marketcap, and post-deal revenue acceleration.
#
# Columns consumed (exact trading.duckdb names):
#   ncfbus      signed net cash for business acquisitions/divestitures
#               (negative = cash OUT for an acquisition; positive = divestiture in)
#   ncfinv      signed net cash from investing in securities/stakes
#   investments investments balance (positive level)
#   intangibles intangibles + goodwill balance (positive level)
#   revenue     revenue (positive level)
#   marketcap   market capitalisation (positive level)
#   ncfo        operating cash flow (signed; comm-services often negative)
# Every feature uses >=1 fundamental column.
# ---------------------------------------------------------------------------

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _sum(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).sum()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    return s - s.shift(w)


# ===== folder domain primitives (M&A / roll-up acquisition) =====
# Convention: ncfbus is signed. An ACQUISITION is cash OUT -> ncfbus < 0.
# "spend" = (-ncfbus) clipped to positive; a divestiture is ncfbus > 0.

def _f47_acq_spend(ncfbus):
    # acquisition cash deployed (positive when buying)
    return (-ncfbus).clip(lower=0)


def _f47_divest_in(ncfbus):
    # cash received from divestitures (positive when selling)
    return ncfbus.clip(lower=0)


def _f47_intensity(ncfbus, revenue, w):
    # acquisition intensity: trailing deal spend relative to trailing revenue
    spend = _sum(_f47_acq_spend(ncfbus), w)
    rev = _sum(revenue, w).replace(0, np.nan)
    return spend / rev


def _f47_material_q(ncfbus, revenue, thresh):
    # boolean-ish: a quarter is a "material deal" if |ncfbus| > thresh * revenue
    return (ncfbus.abs() > (thresh * revenue)).astype(float)


def _f47_ops_funding(ncfbus, ncfo, w):
    # share of deal spend that trailing operating cash could fund (ops vs external)
    spend = _sum(_f47_acq_spend(ncfbus), w)
    ops = _sum(ncfo.clip(lower=0), w)
    return ops / spend.replace(0, np.nan)


def _f47_goodwill_build(intangibles, revenue, w):
    # intangible/goodwill build from deals scaled by revenue (overpayment proxy)
    build = intangibles - intangibles.shift(w)
    rev = _mean(revenue, w).replace(0, np.nan)
    return build / rev


def _f47_acquirer_sign(ncfbus, w):
    # net acquirer (-1) vs divestor (+1) tilt in [-1, 1] over the window
    s = _mean(ncfbus, w)
    turn = _mean(ncfbus.abs(), w).replace(0, np.nan)
    return s / turn


def _f47_deal_vs_cap(ncfbus, marketcap, w):
    # cumulative trailing deal spend relative to current market cap
    spend = _sum(_f47_acq_spend(ncfbus), w)
    return spend / marketcap.replace(0, np.nan)


# ============================================================
# ---- ACQUISITION INTENSITY (|ncfbus|/revenue) ----

# acquisition intensity over 252d (annual deal spend / annual revenue)
def f47ma_f47_ma_rollup_acquisition_intensity_252d_base_v001_signal(ncfbus, revenue):
    b = _f47_intensity(ncfbus, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acquisition intensity over 126d
def f47ma_f47_ma_rollup_acquisition_intensity_126d_base_v002_signal(ncfbus, revenue):
    b = _f47_intensity(ncfbus, revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acquisition intensity over 63d, z-scored vs its own 252d history (de-trended)
def f47ma_f47_ma_rollup_acquisition_intensityz_63d_base_v003_signal(ncfbus, revenue):
    r = _f47_intensity(ncfbus, revenue, 63)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-spend skewness: 252d skew of daily acquisition-spend/revenue (a few mega-deals vs many small)
def f47ma_f47_ma_rollup_acquisition_dealskew_252d_base_v004_signal(ncfbus, revenue):
    si = _safe_div(_f47_acq_spend(ncfbus), _mean(revenue, 21))
    b = si.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short vs long intensity spread (252d minus 504d) -- acquisition acceleration
def f47ma_f47_ma_rollup_acquisition_intenspr_252v504_base_v005_signal(ncfbus, revenue):
    s = _f47_intensity(ncfbus, revenue, 252)
    l = _f47_intensity(ncfbus, revenue, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acquisition intensity percentile-ranked vs its own 504d history
def f47ma_f47_ma_rollup_acquisition_intensrank_252d_base_v006_signal(ncfbus, revenue):
    r = _f47_intensity(ncfbus, revenue, 252)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intensity ratio: 63d run-rate annualised vs trailing-252d level (surge ratio)
def f47ma_f47_ma_rollup_acquisition_intensburst_63d_base_v007_signal(ncfbus, revenue):
    fast = _f47_intensity(ncfbus, revenue, 63)
    slow = _f47_intensity(ncfbus, revenue, 252).replace(0, np.nan)
    b = fast / slow - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# peak deal intensity vs average deal intensity within the trailing year (biggest-deal skew)
def f47ma_f47_ma_rollup_acquisition_peakdeal_252d_base_v008_signal(ncfbus, revenue):
    spend = _f47_acq_spend(ncfbus)
    si = _safe_div(spend, _mean(revenue, 21))
    peak = si.rolling(252, min_periods=126).max()
    avg = _mean(si, 252).replace(0, np.nan)
    b = peak / avg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- ACQUISITION CADENCE (count of material-ncfbus quarters) ----

# count of material-deal quarters in trailing 252d (cadence, thresh 5% of revenue)
def f47ma_f47_ma_rollup_acquisition_cadence_252d_base_v009_signal(ncfbus, revenue):
    mat = _f47_material_q(ncfbus, revenue, 0.05)
    b = mat.rolling(252, min_periods=126).sum() / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of material-deal quarters in trailing 504d (longer cadence)
def f47ma_f47_ma_rollup_acquisition_cadence_504d_base_v010_signal(ncfbus, revenue):
    mat = _f47_material_q(ncfbus, revenue, 0.05)
    b = mat.rolling(504, min_periods=252).sum() / 504.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of LARGE-deal quarters (thresh 15% of revenue) over trailing year
def f47ma_f47_ma_rollup_acquisition_bigcadence_252d_base_v011_signal(ncfbus, revenue):
    mat = _f47_material_q(ncfbus, revenue, 0.15)
    b = mat.rolling(252, min_periods=126).sum() / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-spend Gini-like concentration: std/mean of active-day deal spend (few-big vs many-small)
def f47ma_f47_ma_rollup_acquisition_dealconc_252d_base_v012_signal(ncfbus):
    spend = _f47_acq_spend(ncfbus).replace(0, np.nan)
    b = _safe_div(_std(spend, 252), _mean(spend, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cadence acceleration: 126d material-quarter rate minus 504d rate
def f47ma_f47_ma_rollup_acquisition_cadenceacc_base_v013_signal(ncfbus, revenue):
    mat = _f47_material_q(ncfbus, revenue, 0.05)
    fast = mat.rolling(126, min_periods=63).mean()
    slow = mat.rolling(504, min_periods=252).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-recency staleness: EMA-decayed time since material deals, scaled by intensity
def f47ma_f47_ma_rollup_acquisition_drystreak_252d_base_v014_signal(ncfbus, revenue):
    mat = _f47_material_q(ncfbus, revenue, 0.05)
    # decaying "freshness": recent material deals push toward 1, gaps decay toward 0
    fresh = mat.ewm(span=126, min_periods=42).mean()
    intens = _f47_intensity(ncfbus, revenue, 252)
    b = (1.0 - fresh) * (1.0 + intens)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-spend concentration: max-quarter spend over trailing-year total spend (lumpy?)
def f47ma_f47_ma_rollup_acquisition_lumpiness_252d_base_v015_signal(ncfbus):
    spend = _f47_acq_spend(ncfbus)
    peak = spend.rolling(252, min_periods=126).max()
    tot = _sum(spend, 252).replace(0, np.nan)
    b = peak / tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- M&A FUNDED BY OPS vs EXTERNAL (ncfbus/ncfo) ----

# operating-cash deal coverage over 252d (ops vs external funding of deals)
def f47ma_f47_ma_rollup_acquisition_opscover_252d_base_v016_signal(ncfbus, ncfo):
    b = _f47_ops_funding(ncfbus, ncfo, 252).clip(upper=10.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash deal coverage over 126d
def f47ma_f47_ma_rollup_acquisition_opscover_126d_base_v017_signal(ncfbus, ncfo):
    b = _f47_ops_funding(ncfbus, ncfo, 126).clip(upper=10.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-spend share of total cash usage: |ncfbus out| vs (|ncfbus out| + |ops|), 126d regime
def f47ma_f47_ma_rollup_acquisition_dealshare_126d_base_v018_signal(ncfbus, ncfo):
    spend = _mean(_f47_acq_spend(ncfbus), 126)
    ops = _mean(ncfo.abs(), 126)
    b = spend / (spend + ops).replace(0, np.nan)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# externally-funded-deal flag rate: deals while ops is negative (burn + buying)
def f47ma_f47_ma_rollup_acquisition_burnbuy_252d_base_v019_signal(ncfbus, ncfo):
    buying = (_f47_acq_spend(ncfbus) > 0).astype(float)
    burning = (ncfo < 0).astype(float)
    both = (buying * burning)
    b = both.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap: trailing (ncfo - acq spend) scaled by deal turnover
def f47ma_f47_ma_rollup_acquisition_selffund_252d_base_v020_signal(ncfbus, ncfo):
    gap = _sum(ncfo, 252) - _sum(_f47_acq_spend(ncfbus), 252)
    scale = (_sum(ncfo.abs(), 252) + _sum(_f47_acq_spend(ncfbus), 252)).replace(0, np.nan)
    b = gap / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ops-coverage trend: change in 126d ops-coverage over a quarter
def f47ma_f47_ma_rollup_acquisition_covertrend_126d_base_v021_signal(ncfbus, ncfo):
    cov = _f47_ops_funding(ncfbus, ncfo, 126).clip(upper=10.0)
    b = cov - cov.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- GOODWILL / INTANGIBLE BUILD FROM DEALS (overpayment proxy) ----

# intangible/goodwill build over 252d scaled by revenue (overpayment proxy)
def f47ma_f47_ma_rollup_acquisition_gwbuild_252d_base_v022_signal(intangibles, revenue):
    b = _f47_goodwill_build(intangibles, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible/goodwill build over 126d scaled by revenue
def f47ma_f47_ma_rollup_acquisition_gwbuild_126d_base_v023_signal(intangibles, revenue):
    b = _f47_goodwill_build(intangibles, revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# QoQ intangible build z-scored vs its own 252d history (deal-pulse de-trended)
def f47ma_f47_ma_rollup_acquisition_gwpulsez_63d_base_v024_signal(intangibles, revenue):
    g = _f47_goodwill_build(intangibles, revenue, 63)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill build per dollar of deal spend (overpayment efficiency)
def f47ma_f47_ma_rollup_acquisition_gwperspend_252d_base_v025_signal(intangibles, ncfbus):
    build = (intangibles - intangibles.shift(252)).clip(lower=0)
    spend = _sum(_f47_acq_spend(ncfbus), 252).replace(0, np.nan)
    b = build / spend
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible base as a multiple of revenue (cumulative roll-up footprint)
def f47ma_f47_ma_rollup_acquisition_gwfootprint_252d_base_v026_signal(intangibles, revenue):
    b = _safe_div(_mean(intangibles, 252), _mean(revenue, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible build growth (log-change of intangibles over 252d) -- roll-up speed
def f47ma_f47_ma_rollup_acquisition_gwgrowth_252d_base_v027_signal(intangibles):
    b = np.log(intangibles.replace(0, np.nan) / intangibles.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill build acceleration: 126d build rate minus prior 126d build rate
def f47ma_f47_ma_rollup_acquisition_gwaccel_base_v028_signal(intangibles, revenue):
    g = _f47_goodwill_build(intangibles, revenue, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of intangibles in revenue-scaled build that is "step" (jump quarters)
def f47ma_f47_ma_rollup_acquisition_gwstep_252d_base_v029_signal(intangibles, revenue):
    qbuild = (intangibles - intangibles.shift(63)).clip(lower=0)
    big = (qbuild > (0.10 * _mean(revenue, 63))).astype(float)
    b = big.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- STAKE-BUILDING via INVESTMENTS BALANCE & ncfinv ----

# investments-balance build over 252d scaled by revenue (stake-building)
def f47ma_f47_ma_rollup_acquisition_stakebuild_252d_base_v030_signal(investments, revenue):
    build = investments - investments.shift(252)
    b = build / _mean(revenue, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stake-build acceleration: change in 126d investments log-growth over a quarter
def f47ma_f47_ma_rollup_acquisition_stakeaccel_126d_base_v031_signal(investments):
    g = np.log(investments.replace(0, np.nan) / investments.shift(126).replace(0, np.nan))
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net investing flow (ncfinv) intensity vs revenue, 252d (securities deployment)
def f47ma_f47_ma_rollup_acquisition_invflowint_252d_base_v032_signal(ncfinv, revenue):
    out = _sum((-ncfinv).clip(lower=0), 252)
    rev = _sum(revenue, 252).replace(0, np.nan)
    b = out / rev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfinv net acquirer-vs-realiser sign over 252d (building vs liquidating stakes)
def f47ma_f47_ma_rollup_acquisition_invsign_252d_base_v033_signal(ncfinv):
    s = _mean(ncfinv, 252)
    turn = _mean(ncfinv.abs(), 252).replace(0, np.nan)
    b = -s / turn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined deployment: deal spend + securities deployment over revenue (total M&A)
def f47ma_f47_ma_rollup_acquisition_totaldeploy_252d_base_v034_signal(ncfbus, ncfinv, revenue):
    deploy = _sum(_f47_acq_spend(ncfbus) + (-ncfinv).clip(lower=0), 252)
    rev = _sum(revenue, 252).replace(0, np.nan)
    b = deploy / rev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments-balance build z-scored vs its own 252d history
def f47ma_f47_ma_rollup_acquisition_stakez_126d_base_v035_signal(investments, revenue):
    build = (investments - investments.shift(126)) / _mean(revenue, 126).replace(0, np.nan)
    b = _z(build, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stake-building vs deal-making mix in [-1,1]: securities (+1) vs whole-company (-1)
def f47ma_f47_ma_rollup_acquisition_stakevsdeal_252d_base_v036_signal(ncfinv, ncfbus):
    stake = _mean((-ncfinv).clip(lower=0), 252)
    deal = _mean(_f47_acq_spend(ncfbus), 252)
    b = (stake - deal) / (stake + deal).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- NET ACQUIRER vs DIVESTOR SIGN of ncfbus ----

# net acquirer (-1) vs divestor (+1) tilt over 252d
def f47ma_f47_ma_rollup_acquisition_acqsign_252d_base_v037_signal(ncfbus):
    b = _f47_acquirer_sign(ncfbus, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net acquirer vs divestor tilt over 504d (regime)
def f47ma_f47_ma_rollup_acquisition_acqsign_504d_base_v038_signal(ncfbus):
    b = _f47_acquirer_sign(ncfbus, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divestiture intensity: trailing divestiture inflow over revenue, 252d
def f47ma_f47_ma_rollup_acquisition_divestint_252d_base_v039_signal(ncfbus, revenue):
    din = _sum(_f47_divest_in(ncfbus), 252)
    rev = _sum(revenue, 252).replace(0, np.nan)
    b = din / rev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divestiture burst: peak single-quarter divestiture proceeds vs trailing-year average
def f47ma_f47_ma_rollup_acquisition_divburst_252d_base_v040_signal(ncfbus, revenue):
    di = _safe_div(_f47_divest_in(ncfbus), _mean(revenue, 21))
    peak = di.rolling(252, min_periods=126).max()
    avg = _mean(di, 252).replace(0, np.nan)
    b = peak / avg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pruning regime: fraction of trailing year that is net-divestor by quarter
def f47ma_f47_ma_rollup_acquisition_pruning_252d_base_v041_signal(ncfbus):
    qnet = _mean(ncfbus, 63)
    pruning = (qnet > 0).astype(float)
    b = pruning.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acquirer-sign change: 252d tilt minus its own value a year ago (regime flip)
def f47ma_f47_ma_rollup_acquisition_signflip_252d_base_v042_signal(ncfbus):
    s = _f47_acquirer_sign(ncfbus, 252)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- TRAILING DEAL SPEND / MARKETCAP ----

# cumulative trailing deal spend / marketcap over 252d
def f47ma_f47_ma_rollup_acquisition_dealvscap_252d_base_v043_signal(ncfbus, marketcap):
    b = _f47_deal_vs_cap(ncfbus, marketcap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative trailing deal spend / marketcap over 504d (multi-year roll-up scale)
def f47ma_f47_ma_rollup_acquisition_dealvscap_504d_base_v044_signal(ncfbus, marketcap):
    b = _f47_deal_vs_cap(ncfbus, marketcap, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-spend/marketcap z-scored vs its own 252d history (de-trended deal scale)
def f47ma_f47_ma_rollup_acquisition_dealcapz_126d_base_v045_signal(ncfbus, marketcap):
    r = _f47_deal_vs_cap(ncfbus, marketcap, 126)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible base / marketcap (how much of the cap is acquired goodwill)
def f47ma_f47_ma_rollup_acquisition_gwvscap_252d_base_v046_signal(intangibles, marketcap):
    b = _safe_div(_mean(intangibles, 252), _mean(marketcap, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net M&A deployment (deals + stakes) over marketcap, 252d (total capital at risk)
def f47ma_f47_ma_rollup_acquisition_deployvscap_252d_base_v047_signal(ncfbus, ncfinv, marketcap):
    deploy = _sum(_f47_acq_spend(ncfbus) + (-ncfinv).clip(lower=0), 252)
    b = deploy / _mean(marketcap, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-spend/marketcap percentile-ranked vs 504d history (relative deal aggression)
def f47ma_f47_ma_rollup_acquisition_dealcaprank_252d_base_v048_signal(ncfbus, marketcap):
    r = _f47_deal_vs_cap(ncfbus, marketcap, 252)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- POST-DEAL REVENUE ACCELERATION ----

# revenue acceleration following deal spend: 126d rev growth vs prior 126d, dealful
def f47ma_f47_ma_rollup_acquisition_postdealacc_126d_base_v049_signal(revenue, ncfbus):
    g1 = np.log(_mean(revenue, 63).replace(0, np.nan) / _mean(revenue, 63).shift(126).replace(0, np.nan))
    dealt = (_sum(_f47_acq_spend(ncfbus), 252) > 0).astype(float)
    b = g1 * dealt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth per dollar of trailing deal spend (acquisition ROI proxy)
def f47ma_f47_ma_rollup_acquisition_revperdeal_252d_base_v050_signal(revenue, ncfbus):
    rev_gain = (_mean(revenue, 63) - _mean(revenue, 63).shift(252)).clip(lower=0)
    spend = _sum(_f47_acq_spend(ncfbus), 252).replace(0, np.nan)
    b = rev_gain / spend
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration vs goodwill build (organic-vs-bought growth balance)
def f47ma_f47_ma_rollup_acquisition_revvsgw_252d_base_v051_signal(revenue, intangibles):
    revg = np.log(_mean(revenue, 63).replace(0, np.nan) / _mean(revenue, 63).shift(252).replace(0, np.nan))
    gwg = np.log(_mean(intangibles, 63).replace(0, np.nan) / _mean(intangibles, 63).shift(252).replace(0, np.nan))
    b = revg - gwg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# post-deal revenue acceleration: change in 126d revenue growth (2nd diff of level)
def f47ma_f47_ma_rollup_acquisition_revaccel_126d_base_v052_signal(revenue, ncfbus):
    rl = np.log(revenue.replace(0, np.nan))
    g = rl.shift(0) - rl.shift(126)
    acc = g - g.shift(126)
    intens = _f47_intensity(ncfbus, revenue, 252)
    b = acc * (1.0 + intens)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inorganic revenue lift: revenue growth scaled by acquisition cadence
def f47ma_f47_ma_rollup_acquisition_inorglift_252d_base_v053_signal(revenue, ncfbus):
    revg = np.log(_mean(revenue, 63).replace(0, np.nan) / _mean(revenue, 63).shift(252).replace(0, np.nan))
    cad = _f47_material_q(ncfbus, revenue, 0.05).rolling(252, min_periods=126).mean()
    b = revg * cad
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- INTERACTIONS / COMPOSITES ----

# roll-up signature: intensity x cadence (serial acquirer composite)
def f47ma_f47_ma_rollup_acquisition_rollupsig_252d_base_v054_signal(ncfbus, revenue):
    intens = _f47_intensity(ncfbus, revenue, 252)
    cad = _f47_material_q(ncfbus, revenue, 0.05).rolling(252, min_periods=126).mean()
    b = intens * cad
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill-build momentum vs revenue-build momentum (bought growth outpacing organic), 126d
def f47ma_f47_ma_rollup_acquisition_gwmomgap_126d_base_v055_signal(intangibles, revenue):
    gwm = np.log(_mean(intangibles, 21).replace(0, np.nan) / _mean(intangibles, 21).shift(126).replace(0, np.nan))
    revm = np.log(_mean(revenue, 21).replace(0, np.nan) / _mean(revenue, 21).shift(126).replace(0, np.nan))
    b = gwm - revm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# externally-funded roll-up risk: intensity x (1 - ops coverage)
def f47ma_f47_ma_rollup_acquisition_extrollrisk_252d_base_v056_signal(ncfbus, revenue, ncfo):
    intens = _f47_intensity(ncfbus, revenue, 252)
    cover = _f47_ops_funding(ncfbus, ncfo, 252).clip(0.0, 1.0)
    b = intens * (1.0 - cover)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-spend autocorrelation: persistence of quarterly spend vs prior quarter (programmatic acquirer)
def f47ma_f47_ma_rollup_acquisition_dealpersist_252d_base_v057_signal(ncfbus, revenue):
    qs = _safe_div(_mean(_f47_acq_spend(ncfbus), 63), _mean(revenue, 63))
    cur = qs - _mean(qs, 252)
    lag = qs.shift(63) - _mean(qs.shift(63), 252)
    cov = _mean(cur * lag, 252)
    denom = (_std(qs, 252) * _std(qs.shift(63), 252)).replace(0, np.nan)
    b = cov / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-funding stress: deal spend vs (ops + divestiture proceeds) self-cover
def f47ma_f47_ma_rollup_acquisition_fundstress_252d_base_v058_signal(ncfbus, ncfo):
    spend = _sum(_f47_acq_spend(ncfbus), 252)
    internal = _sum(ncfo.clip(lower=0) + _f47_divest_in(ncfbus), 252).replace(0, np.nan)
    b = spend / internal
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- DISPERSION / VOLATILITY of DEAL FLOW ----

# deal-flow volatility: 252d std of quarterly deal spend over revenue (lumpy serial)
def f47ma_f47_ma_rollup_acquisition_dealvol_252d_base_v059_signal(ncfbus, revenue):
    qspend = _safe_div(_f47_acq_spend(ncfbus), _mean(revenue, 63))
    b = _std(qspend, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-ncfbus volatility scaled by turnover (steady-vs-episodic acquirer)
def f47ma_f47_ma_rollup_acquisition_busvol_252d_base_v060_signal(ncfbus):
    b = _safe_div(_std(ncfbus, 252), _mean(ncfbus.abs(), 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-build volatility (deal-pulse irregularity), 252d
def f47ma_f47_ma_rollup_acquisition_gwvol_252d_base_v061_signal(intangibles, revenue):
    qbuild = _safe_div(intangibles - intangibles.shift(63), _mean(revenue, 63))
    b = _std(qbuild, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- LONGER-HORIZON CUMULATIVE FOOTPRINT ----

# cumulative 504d deal spend over 504d revenue (multi-year roll-up intensity)
def f47ma_f47_ma_rollup_acquisition_cumintens_504d_base_v062_signal(ncfbus, revenue):
    b = _f47_intensity(ncfbus, revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year intangible build over revenue (504d goodwill accretion)
def f47ma_f47_ma_rollup_acquisition_gwbuild_504d_base_v063_signal(intangibles, revenue):
    b = _f47_goodwill_build(intangibles, revenue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year stake build over revenue (504d investments-balance accretion)
def f47ma_f47_ma_rollup_acquisition_stakebuild_504d_base_v064_signal(investments, revenue):
    build = investments - investments.shift(504)
    b = build / _mean(revenue, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year ops coverage of deal spend (504d sustainability)
def f47ma_f47_ma_rollup_acquisition_opscover_504d_base_v065_signal(ncfbus, ncfo):
    b = _f47_ops_funding(ncfbus, ncfo, 504).clip(upper=10.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- ADDITIONAL DISTINCT FACETS ----

# deal-spend EMA displacement: spend/rev minus its slow EMA (acquisition impulse)
def f47ma_f47_ma_rollup_acquisition_impulse_63d_base_v066_signal(ncfbus, revenue):
    si = _safe_div(_f47_acq_spend(ncfbus), _mean(revenue, 63))
    b = si - si.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acquired-asset mix: intangibles (whole-co goodwill) vs investments (minority stakes) in [-1,1]
def f47ma_f47_ma_rollup_acquisition_assetmix_252d_base_v067_signal(intangibles, investments):
    g = _mean(intangibles, 252)
    s = _mean(investments, 252)
    b = (g - s) / (g + s).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acquirer persistence: fraction of trailing year that is acquiring AND ops-positive (healthy serial)
def f47ma_f47_ma_rollup_acquisition_healthyacq_252d_base_v068_signal(ncfbus, ncfo):
    healthy = ((_f47_acq_spend(ncfbus) > 0) & (ncfo > 0)).astype(float)
    b = healthy.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-spend tanh impulse: bounded change in 126d deal intensity over a quarter
def f47ma_f47_ma_rollup_acquisition_intenstanh_126d_base_v069_signal(ncfbus, revenue):
    intens = _f47_intensity(ncfbus, revenue, 126)
    chg = intens - intens.shift(63)
    b = np.tanh(8.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill-build vs deal-spend gap (build exceeding cash = non-cash/stock deals)
def f47ma_f47_ma_rollup_acquisition_stockdeal_252d_base_v070_signal(intangibles, ncfbus, revenue):
    build = (intangibles - intangibles.shift(252)).clip(lower=0)
    spend = _sum(_f47_acq_spend(ncfbus), 252)
    rev = _mean(revenue, 252).replace(0, np.nan)
    b = (build - spend) / rev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# minority-stake portfolio weight: investments balance over marketcap, change over a year
def f47ma_f47_ma_rollup_acquisition_stakeweight_252d_base_v071_signal(investments, marketcap):
    w = _safe_div(_mean(investments, 63), _mean(marketcap, 63))
    b = w - w.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-cadence streak quality: cadence x ops coverage (durable serial acquirer)
def f47ma_f47_ma_rollup_acquisition_durserial_252d_base_v072_signal(ncfbus, revenue, ncfo):
    cad = _f47_material_q(ncfbus, revenue, 0.05).rolling(252, min_periods=126).mean()
    cover = _f47_ops_funding(ncfbus, ncfo, 252).clip(0.0, 2.0)
    b = cad * cover
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stake-flow vs deal-flow correlation proxy: co-deployment alignment, 252d
def f47ma_f47_ma_rollup_acquisition_codeploy_252d_base_v073_signal(ncfinv, ncfbus):
    stake = (-ncfinv).clip(lower=0)
    deal = _f47_acq_spend(ncfbus)
    sm = stake - _mean(stake, 252)
    dm = deal - _mean(deal, 252)
    cov = _mean(sm * dm, 252)
    denom = (_std(stake, 252) * _std(deal, 252)).replace(0, np.nan)
    b = cov / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# securities realisation tilt: net ncfinv inflow (selling stakes) vs investments-balance drawdown
def f47ma_f47_ma_rollup_acquisition_realisetilt_252d_base_v074_signal(ncfinv, investments):
    inflow = _sum(ncfinv.clip(lower=0), 252)
    outflow = _sum((-ncfinv).clip(lower=0), 252)
    direction = (inflow - outflow) / (inflow + outflow).replace(0, np.nan)
    bal_chg = np.sign(investments - investments.shift(252))
    b = direction * (1.0 + 0.5 * bal_chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# churn-and-replace: how synchronised divestiture and acquisition are within the same year
def f47ma_f47_ma_rollup_acquisition_churnrepl_252d_base_v075_signal(ncfbus, revenue):
    spend = _safe_div(_mean(_f47_acq_spend(ncfbus), 63), _mean(revenue, 63))
    div = _safe_div(_mean(_f47_divest_in(ncfbus), 63), _mean(revenue, 63))
    sm = spend - _mean(spend, 252)
    dm = div - _mean(div, 252)
    cov = _mean(sm * dm, 252)
    denom = (_std(spend, 252) * _std(div, 252)).replace(0, np.nan)
    b = cov / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47ma_f47_ma_rollup_acquisition_intensity_252d_base_v001_signal,
    f47ma_f47_ma_rollup_acquisition_intensity_126d_base_v002_signal,
    f47ma_f47_ma_rollup_acquisition_intensityz_63d_base_v003_signal,
    f47ma_f47_ma_rollup_acquisition_dealskew_252d_base_v004_signal,
    f47ma_f47_ma_rollup_acquisition_intenspr_252v504_base_v005_signal,
    f47ma_f47_ma_rollup_acquisition_intensrank_252d_base_v006_signal,
    f47ma_f47_ma_rollup_acquisition_intensburst_63d_base_v007_signal,
    f47ma_f47_ma_rollup_acquisition_peakdeal_252d_base_v008_signal,
    f47ma_f47_ma_rollup_acquisition_cadence_252d_base_v009_signal,
    f47ma_f47_ma_rollup_acquisition_cadence_504d_base_v010_signal,
    f47ma_f47_ma_rollup_acquisition_bigcadence_252d_base_v011_signal,
    f47ma_f47_ma_rollup_acquisition_dealconc_252d_base_v012_signal,
    f47ma_f47_ma_rollup_acquisition_cadenceacc_base_v013_signal,
    f47ma_f47_ma_rollup_acquisition_drystreak_252d_base_v014_signal,
    f47ma_f47_ma_rollup_acquisition_lumpiness_252d_base_v015_signal,
    f47ma_f47_ma_rollup_acquisition_opscover_252d_base_v016_signal,
    f47ma_f47_ma_rollup_acquisition_opscover_126d_base_v017_signal,
    f47ma_f47_ma_rollup_acquisition_dealshare_126d_base_v018_signal,
    f47ma_f47_ma_rollup_acquisition_burnbuy_252d_base_v019_signal,
    f47ma_f47_ma_rollup_acquisition_selffund_252d_base_v020_signal,
    f47ma_f47_ma_rollup_acquisition_covertrend_126d_base_v021_signal,
    f47ma_f47_ma_rollup_acquisition_gwbuild_252d_base_v022_signal,
    f47ma_f47_ma_rollup_acquisition_gwbuild_126d_base_v023_signal,
    f47ma_f47_ma_rollup_acquisition_gwpulsez_63d_base_v024_signal,
    f47ma_f47_ma_rollup_acquisition_gwperspend_252d_base_v025_signal,
    f47ma_f47_ma_rollup_acquisition_gwfootprint_252d_base_v026_signal,
    f47ma_f47_ma_rollup_acquisition_gwgrowth_252d_base_v027_signal,
    f47ma_f47_ma_rollup_acquisition_gwaccel_base_v028_signal,
    f47ma_f47_ma_rollup_acquisition_gwstep_252d_base_v029_signal,
    f47ma_f47_ma_rollup_acquisition_stakebuild_252d_base_v030_signal,
    f47ma_f47_ma_rollup_acquisition_stakeaccel_126d_base_v031_signal,
    f47ma_f47_ma_rollup_acquisition_invflowint_252d_base_v032_signal,
    f47ma_f47_ma_rollup_acquisition_invsign_252d_base_v033_signal,
    f47ma_f47_ma_rollup_acquisition_totaldeploy_252d_base_v034_signal,
    f47ma_f47_ma_rollup_acquisition_stakez_126d_base_v035_signal,
    f47ma_f47_ma_rollup_acquisition_stakevsdeal_252d_base_v036_signal,
    f47ma_f47_ma_rollup_acquisition_acqsign_252d_base_v037_signal,
    f47ma_f47_ma_rollup_acquisition_acqsign_504d_base_v038_signal,
    f47ma_f47_ma_rollup_acquisition_divestint_252d_base_v039_signal,
    f47ma_f47_ma_rollup_acquisition_divburst_252d_base_v040_signal,
    f47ma_f47_ma_rollup_acquisition_pruning_252d_base_v041_signal,
    f47ma_f47_ma_rollup_acquisition_signflip_252d_base_v042_signal,
    f47ma_f47_ma_rollup_acquisition_dealvscap_252d_base_v043_signal,
    f47ma_f47_ma_rollup_acquisition_dealvscap_504d_base_v044_signal,
    f47ma_f47_ma_rollup_acquisition_dealcapz_126d_base_v045_signal,
    f47ma_f47_ma_rollup_acquisition_gwvscap_252d_base_v046_signal,
    f47ma_f47_ma_rollup_acquisition_deployvscap_252d_base_v047_signal,
    f47ma_f47_ma_rollup_acquisition_dealcaprank_252d_base_v048_signal,
    f47ma_f47_ma_rollup_acquisition_postdealacc_126d_base_v049_signal,
    f47ma_f47_ma_rollup_acquisition_revperdeal_252d_base_v050_signal,
    f47ma_f47_ma_rollup_acquisition_revvsgw_252d_base_v051_signal,
    f47ma_f47_ma_rollup_acquisition_revaccel_126d_base_v052_signal,
    f47ma_f47_ma_rollup_acquisition_inorglift_252d_base_v053_signal,
    f47ma_f47_ma_rollup_acquisition_rollupsig_252d_base_v054_signal,
    f47ma_f47_ma_rollup_acquisition_gwmomgap_126d_base_v055_signal,
    f47ma_f47_ma_rollup_acquisition_extrollrisk_252d_base_v056_signal,
    f47ma_f47_ma_rollup_acquisition_dealpersist_252d_base_v057_signal,
    f47ma_f47_ma_rollup_acquisition_fundstress_252d_base_v058_signal,
    f47ma_f47_ma_rollup_acquisition_dealvol_252d_base_v059_signal,
    f47ma_f47_ma_rollup_acquisition_busvol_252d_base_v060_signal,
    f47ma_f47_ma_rollup_acquisition_gwvol_252d_base_v061_signal,
    f47ma_f47_ma_rollup_acquisition_cumintens_504d_base_v062_signal,
    f47ma_f47_ma_rollup_acquisition_gwbuild_504d_base_v063_signal,
    f47ma_f47_ma_rollup_acquisition_stakebuild_504d_base_v064_signal,
    f47ma_f47_ma_rollup_acquisition_opscover_504d_base_v065_signal,
    f47ma_f47_ma_rollup_acquisition_impulse_63d_base_v066_signal,
    f47ma_f47_ma_rollup_acquisition_assetmix_252d_base_v067_signal,
    f47ma_f47_ma_rollup_acquisition_healthyacq_252d_base_v068_signal,
    f47ma_f47_ma_rollup_acquisition_intenstanh_126d_base_v069_signal,
    f47ma_f47_ma_rollup_acquisition_stockdeal_252d_base_v070_signal,
    f47ma_f47_ma_rollup_acquisition_stakeweight_252d_base_v071_signal,
    f47ma_f47_ma_rollup_acquisition_durserial_252d_base_v072_signal,
    f47ma_f47_ma_rollup_acquisition_codeploy_252d_base_v073_signal,
    f47ma_f47_ma_rollup_acquisition_realisetilt_252d_base_v074_signal,
    f47ma_f47_ma_rollup_acquisition_churnrepl_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_MA_ROLLUP_ACQUISITION_REGISTRY_001_075 = REGISTRY


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
        "netincdis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
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

    # ncfbus / ncfinv are SIGNED investing flows that must genuinely swing sign
    # (acquisition spend OUT vs divestiture / realisation IN). Build a centered
    # level plus a deal-cycle component plus episodic lumpy jitter.
    def _signed(seed, base, phase, amp, period):
        raw = _fund(seed, base=base, drift=0.0, vol=0.08, allow_neg=True)
        centered = raw - raw.rolling(252, min_periods=1).mean()
        gn = np.random.default_rng(seed + 9000)
        cyc = amp * base * 0.4 * np.sin(np.arange(n) / period * 2 * np.pi + phase)
        jitter = gn.normal(0.0, base * 0.12, n)
        return centered + pd.Series(cyc) + pd.Series(jitter)

    ncfbus = _signed(201, 6e7, 0.0, 1.0, 73.0).rename("ncfbus")
    ncfinv = _signed(202, 5e7, 1.3, 1.1, 91.0).rename("ncfinv")
    ncfo = _signed(203, 8e7, 2.1, 0.9, 67.0).rename("ncfo")

    # positive-level balances / scales
    revenue = _fund(204, base=1.5e8, drift=0.030, vol=0.07).rename("revenue")
    intangibles = _fund(205, base=4.0e8, drift=0.040, vol=0.10).rename("intangibles")
    investments = _fund(206, base=2.0e8, drift=0.025, vol=0.11).rename("investments")
    marketcap = _fund(207, base=2.0e9, drift=0.020, vol=0.09).rename("marketcap")

    cols = {"ncfbus": ncfbus, "ncfinv": ncfinv, "ncfo": ncfo,
            "revenue": revenue, "intangibles": intangibles,
            "investments": investments, "marketcap": marketcap}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BADCOL %s: %s" % (name, meta["inputs"])
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

    print("OK f47_ma_rollup_acquisition_base_001_075_claude: %d features pass" % n_features)
