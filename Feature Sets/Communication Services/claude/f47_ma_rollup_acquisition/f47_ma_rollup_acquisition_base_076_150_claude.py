import inspect
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# f47_ma_rollup_acquisition -- BASE file 076..150.
# Second half of the M&A / roll-up base family. Same column conventions and
# domain (acquisition intensity / cadence / ops-vs-external funding / goodwill
# build / stake-building / acquirer-divestor sign / deal-spend vs marketcap /
# post-deal revenue acceleration), with structurally distinct formulas and
# different windows / facets from file 001..075.
#
# Columns: ncfbus, ncfinv, investments, intangibles, revenue, marketcap, ncfo.
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
def _f47_acq_spend(ncfbus):
    return (-ncfbus).clip(lower=0)


def _f47_divest_in(ncfbus):
    return ncfbus.clip(lower=0)


def _f47_intensity(ncfbus, revenue, w):
    spend = _sum(_f47_acq_spend(ncfbus), w)
    rev = _sum(revenue, w).replace(0, np.nan)
    return spend / rev


def _f47_material_q(ncfbus, revenue, thresh):
    return (ncfbus.abs() > (thresh * revenue)).astype(float)


def _f47_ops_funding(ncfbus, ncfo, w):
    spend = _sum(_f47_acq_spend(ncfbus), w)
    ops = _sum(ncfo.clip(lower=0), w)
    return ops / spend.replace(0, np.nan)


def _f47_goodwill_build(intangibles, revenue, w):
    build = intangibles - intangibles.shift(w)
    rev = _mean(revenue, w).replace(0, np.nan)
    return build / rev


def _f47_acquirer_sign(ncfbus, w):
    s = _mean(ncfbus, w)
    turn = _mean(ncfbus.abs(), w).replace(0, np.nan)
    return s / turn


def _f47_deal_vs_cap(ncfbus, marketcap, w):
    spend = _sum(_f47_acq_spend(ncfbus), w)
    return spend / marketcap.replace(0, np.nan)


# ============================================================
# ---- INTENSITY (alternative facets) ----

# acquisition intensity over 63d (quarterly run-rate / revenue)
def f47ma_f47_ma_rollup_acquisition_intensity_63d_base_v076_signal(ncfbus, revenue):
    b = _f47_intensity(ncfbus, revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intensity dispersion: rolling std of 63d-intensity over 504d (steady vs episodic)
def f47ma_f47_ma_rollup_acquisition_intensdisp_504d_base_v077_signal(ncfbus, revenue):
    qi = _f47_intensity(ncfbus, revenue, 63)
    b = _std(qi, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intensity vs its 504d median (regime distance above/below typical deal load)
def f47ma_f47_ma_rollup_acquisition_intensregime_252d_base_v078_signal(ncfbus, revenue):
    intens = _f47_intensity(ncfbus, revenue, 252)
    med = intens.rolling(504, min_periods=252).median()
    b = intens - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-spend share of investing outflow: ncfbus-out vs total investing outflow, 252d
def f47ma_f47_ma_rollup_acquisition_busshareinv_252d_base_v079_signal(ncfbus, ncfinv):
    bus = _sum(_f47_acq_spend(ncfbus), 252)
    inv = _sum((-ncfinv).clip(lower=0), 252)
    b = bus / (bus + inv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intensity log-change year over year (acquisition program ramp)
def f47ma_f47_ma_rollup_acquisition_intensyoy_252d_base_v080_signal(ncfbus, revenue):
    intens = _f47_intensity(ncfbus, revenue, 252)
    b = np.log((intens + 0.01) / (intens.shift(252) + 0.01))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- CADENCE (alternative thresholds / streaks) ----

# count of small bolt-on quarters (2%-8% of revenue) over trailing year (tuck-in cadence)
def f47ma_f47_ma_rollup_acquisition_boltoncad_252d_base_v081_signal(ncfbus, revenue):
    spend = _f47_acq_spend(ncfbus)
    bolt = ((spend > 0.02 * revenue) & (spend < 0.08 * revenue)).astype(float)
    b = bolt.rolling(252, min_periods=126).sum() / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest consecutive acquiring streak (quarters) over trailing year, normalised
def f47ma_f47_ma_rollup_acquisition_acqstreak_252d_base_v082_signal(ncfbus, revenue):
    mat = _f47_material_q(ncfbus, revenue, 0.05)

    def _maxrun(a):
        best = run = 0
        for v in a:
            if v > 0:
                run += 1
                best = max(best, run)
            else:
                run = 0
        return best / float(len(a))
    b = mat.rolling(252, min_periods=126).apply(_maxrun, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-size dispersion across material quarters: std of quarterly deal-intensity, 504d
def f47ma_f47_ma_rollup_acquisition_sizedisp_504d_base_v083_signal(ncfbus, revenue):
    qsize = _safe_div(_mean(_f47_acq_spend(ncfbus), 63), _mean(revenue, 63))
    b = _safe_div(_std(qsize, 504), _mean(qsize, 504))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cadence stability: 1 - std of quarterly material-deal indicator over 504d
def f47ma_f47_ma_rollup_acquisition_cadstab_504d_base_v084_signal(ncfbus, revenue):
    mat = _f47_material_q(ncfbus, revenue, 0.05)
    b = -_std(mat, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# entries into acquiring regime: transitions into material-deal quarters, 252d
def f47ma_f47_ma_rollup_acquisition_acqentries_252d_base_v085_signal(ncfbus, revenue):
    mat = _f47_material_q(ncfbus, revenue, 0.05)
    entries = ((mat == 1) & (mat.shift(63) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- OPS-vs-EXTERNAL FUNDING (alternative) ----

# free-cash-after-deals: (ncfo - acq spend) over revenue, 252d (post-M&A cash margin)
def f47ma_f47_ma_rollup_acquisition_fcafterdeal_252d_base_v086_signal(ncfbus, ncfo, revenue):
    fc = _sum(ncfo, 252) - _sum(_f47_acq_spend(ncfbus), 252)
    b = fc / _sum(revenue, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ops-coverage shortfall flag rate: deal spend exceeds operating cash, 252d
def f47ma_f47_ma_rollup_acquisition_coverfail_252d_base_v087_signal(ncfbus, ncfo):
    short = (_f47_acq_spend(ncfbus) > ncfo.clip(lower=0)).astype(float)
    active = (_f47_acq_spend(ncfbus) > 0).astype(float)
    num = (short * active).rolling(252, min_periods=126).sum()
    den = active.rolling(252, min_periods=126).sum().replace(0, np.nan)
    b = num / den
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash deal coverage trend over 252d vs prior 252d (sustainability shift)
def f47ma_f47_ma_rollup_acquisition_coveryoy_252d_base_v088_signal(ncfbus, ncfo):
    cov = _f47_ops_funding(ncfbus, ncfo, 252).clip(upper=10.0)
    b = cov - cov.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal spend funded by ops vs investing-flow swing (internal vs portfolio recycling)
def f47ma_f47_ma_rollup_acquisition_internalfund_252d_base_v089_signal(ncfbus, ncfo, ncfinv):
    spend = _sum(_f47_acq_spend(ncfbus), 252)
    internal = _sum(ncfo.clip(lower=0) + ncfinv.clip(lower=0), 252).replace(0, np.nan)
    b = (internal - spend) / (internal + spend).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- GOODWILL / INTANGIBLE BUILD (alternative) ----

# intangible build rank vs its own 504d history (relative deal-pulse magnitude)
def f47ma_f47_ma_rollup_acquisition_gwbuildrank_252d_base_v090_signal(intangibles, revenue):
    g = _f47_goodwill_build(intangibles, revenue, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill drag: negative intangible-balance changes (impairments/divest write-offs), rev-scaled
def f47ma_f47_ma_rollup_acquisition_gwimpair_252d_base_v091_signal(intangibles, revenue):
    chg = intangibles - intangibles.shift(63)
    impair = (-chg).clip(lower=0)
    b = _sum(impair, 252) / _sum(revenue, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible intensity vs marketcap change (goodwill build vs equity value created)
def f47ma_f47_ma_rollup_acquisition_gwvscapchg_252d_base_v092_signal(intangibles, marketcap, revenue):
    gw = _f47_goodwill_build(intangibles, revenue, 252)
    capg = np.log(_mean(marketcap, 21).replace(0, np.nan) / _mean(marketcap, 21).shift(252).replace(0, np.nan))
    b = gw - capg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill build smoothed EMA displacement (deal-pulse vs trend)
def f47ma_f47_ma_rollup_acquisition_gwdisp_126d_base_v093_signal(intangibles, revenue):
    g = _f47_goodwill_build(intangibles, revenue, 126)
    b = g - g.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative goodwill multiple of cumulative revenue (long-horizon roll-up footprint)
def f47ma_f47_ma_rollup_acquisition_gwcumfoot_504d_base_v094_signal(intangibles, revenue):
    b = _safe_div(_mean(intangibles, 504), _sum(revenue, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- STAKE-BUILDING / ncfinv (alternative) ----

# net ncfinv deployment over marketcap, 252d (securities portfolio scale)
def f47ma_f47_ma_rollup_acquisition_invdeploycap_252d_base_v095_signal(ncfinv, marketcap):
    out = _sum((-ncfinv).clip(lower=0), 252)
    b = out / _mean(marketcap, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfinv flow volatility scaled by turnover (episodic stake activity)
def f47ma_f47_ma_rollup_acquisition_invvol_252d_base_v096_signal(ncfinv):
    b = _safe_div(_std(ncfinv, 252), _mean(ncfinv.abs(), 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments-balance acceleration vs revenue (stake-building 2nd diff), rev-scaled
def f47ma_f47_ma_rollup_acquisition_stakeaccrev_126d_base_v097_signal(investments, revenue):
    build = _safe_div(investments - investments.shift(126), _mean(revenue, 126))
    b = build - build.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments balance share of acquired-asset base (stakes vs goodwill weight)
def f47ma_f47_ma_rollup_acquisition_stakeshare_252d_base_v098_signal(investments, intangibles):
    inv = _mean(investments, 252)
    intang = _mean(intangibles, 252)
    b = inv / (inv + intang).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfinv net direction over 504d (multi-year accumulation vs liquidation)
def f47ma_f47_ma_rollup_acquisition_invsign_504d_base_v099_signal(ncfinv):
    s = _mean(ncfinv, 504)
    turn = _mean(ncfinv.abs(), 504).replace(0, np.nan)
    b = -s / turn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- ACQUIRER vs DIVESTOR SIGN (alternative) ----

# acquirer-sign smoothed EMA (persistent strategic tilt)
def f47ma_f47_ma_rollup_acquisition_signsmooth_252d_base_v100_signal(ncfbus):
    s = _f47_acquirer_sign(ncfbus, 126)
    b = s.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net deal flow per dollar of revenue (signed; negative = net buyer), 252d
def f47ma_f47_ma_rollup_acquisition_netflowrev_252d_base_v101_signal(ncfbus, revenue):
    b = _sum(ncfbus, 252) / _sum(revenue, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divestiture-to-acquisition ratio over 504d (capital recycling intensity)
def f47ma_f47_ma_rollup_acquisition_recyc_504d_base_v102_signal(ncfbus):
    div = _sum(_f47_divest_in(ncfbus), 504)
    spend = _sum(_f47_acq_spend(ncfbus), 504).replace(0, np.nan)
    b = div / spend
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acquirer-regime persistence: fraction of trailing year net-acquiring by quarter
def f47ma_f47_ma_rollup_acquisition_acqregime_252d_base_v103_signal(ncfbus):
    qnet = _mean(ncfbus, 63)
    acquiring = (qnet < 0).astype(float)
    b = acquiring.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- DEAL SPEND vs MARKETCAP (alternative) ----

# deal spend / marketcap over 126d (recent deal scale)
def f47ma_f47_ma_rollup_acquisition_dealvscap_126d_base_v104_signal(ncfbus, marketcap):
    b = _f47_deal_vs_cap(ncfbus, marketcap, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acquisition appetite vs valuation: deal/cap interacted with goodwill/cap (rich-buying)
def f47ma_f47_ma_rollup_acquisition_richbuy_252d_base_v105_signal(ncfbus, intangibles, marketcap):
    dvc = _f47_deal_vs_cap(ncfbus, marketcap, 252)
    gvc = _safe_div(_mean(intangibles, 252), _mean(marketcap, 252))
    b = dvc * gvc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal spend / marketcap momentum: change over a quarter (appetite ramp)
def f47ma_f47_ma_rollup_acquisition_dealcapmom_252d_base_v106_signal(ncfbus, marketcap):
    dvc = _f47_deal_vs_cap(ncfbus, marketcap, 252)
    b = dvc - dvc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total acquired-asset base (intangibles) vs marketcap, z-scored vs 252d history
def f47ma_f47_ma_rollup_acquisition_gwcapz_252d_base_v107_signal(intangibles, marketcap):
    r = _safe_div(intangibles, marketcap)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- POST-DEAL REVENUE ACCELERATION (alternative) ----

# revenue growth conditional on high deal intensity (inorganic growth signature)
def f47ma_f47_ma_rollup_acquisition_inorgsig_252d_base_v108_signal(revenue, ncfbus):
    revg = np.log(_mean(revenue, 63).replace(0, np.nan) / _mean(revenue, 63).shift(252).replace(0, np.nan))
    intens = _f47_intensity(ncfbus, revenue, 252)
    hi = (intens > intens.rolling(504, min_periods=252).median()).astype(float)
    b = revg * hi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration lagged after deal pulse: rev growth now vs deal spend 2 quarters ago
def f47ma_f47_ma_rollup_acquisition_lagdealrev_252d_base_v109_signal(revenue, ncfbus):
    revg = np.log(_mean(revenue, 63).replace(0, np.nan) / _mean(revenue, 63).shift(126).replace(0, np.nan))
    past_intens = _f47_intensity(ncfbus, revenue, 126).shift(126)
    b = revg * (1.0 + past_intens)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per cumulative deal spend (multi-year acquisition revenue efficiency)
def f47ma_f47_ma_rollup_acquisition_revperspend_504d_base_v110_signal(revenue, ncfbus):
    revgain = (_mean(revenue, 63) - _mean(revenue, 63).shift(504)).clip(lower=0)
    spend = _sum(_f47_acq_spend(ncfbus), 504).replace(0, np.nan)
    b = revgain / spend
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# organic-vs-inorganic balance: revenue growth minus intensity (organic residual)
def f47ma_f47_ma_rollup_acquisition_organicres_252d_base_v111_signal(revenue, ncfbus):
    revg = np.log(_mean(revenue, 63).replace(0, np.nan) / _mean(revenue, 63).shift(252).replace(0, np.nan))
    intens = _f47_intensity(ncfbus, revenue, 252)
    b = revg - 2.0 * intens
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- INTERACTIONS / COMPOSITES (alternative) ----

# roll-up health composite: cadence x ops-coverage minus goodwill drag
def f47ma_f47_ma_rollup_acquisition_rollhealth_252d_base_v112_signal(ncfbus, revenue, ncfo, intangibles):
    cad = _f47_material_q(ncfbus, revenue, 0.05).rolling(252, min_periods=126).mean()
    cover = _f47_ops_funding(ncfbus, ncfo, 252).clip(0.0, 2.0)
    gw = _f47_goodwill_build(intangibles, revenue, 252).clip(lower=0)
    b = cad * cover - gw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overpayment stress: goodwill build per deal x deal-vs-cap (rich serial acquirer risk)
def f47ma_f47_ma_rollup_acquisition_overpay_252d_base_v113_signal(intangibles, ncfbus, marketcap):
    build = (intangibles - intangibles.shift(252)).clip(lower=0)
    spend = _sum(_f47_acq_spend(ncfbus), 252).replace(0, np.nan)
    gwps = build / spend
    dvc = _f47_deal_vs_cap(ncfbus, marketcap, 252)
    b = gwps * dvc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deployment breadth: combined deal + stake activity over revenue, z-scored
def f47ma_f47_ma_rollup_acquisition_deploybreadthz_252d_base_v114_signal(ncfbus, ncfinv, revenue):
    deploy = _safe_div(_sum(_f47_acq_spend(ncfbus) + (-ncfinv).clip(lower=0), 252), _sum(revenue, 252))
    b = _z(deploy, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# funding mix x intensity: externally-funded intensity flagged by negative ops, 126d
def f47ma_f47_ma_rollup_acquisition_extintens_126d_base_v115_signal(ncfbus, revenue, ncfo):
    intens = _f47_intensity(ncfbus, revenue, 126)
    burnfrac = (ncfo < 0).astype(float).rolling(126, min_periods=63).mean()
    b = intens * burnfrac
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- DISPERSION / VOLATILITY (alternative) ----

# net-ncfbus skew over 252d (asymmetry: occasional big buys vs steady small)
def f47ma_f47_ma_rollup_acquisition_busskew_252d_base_v116_signal(ncfbus):
    b = ncfbus.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-ncfbus kurtosis over 252d (deal lumpiness / fat-tailed mega-deals)
def f47ma_f47_ma_rollup_acquisition_buskurt_252d_base_v117_signal(ncfbus):
    b = ncfbus.rolling(252, min_periods=126).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-build dispersion over 504d (irregular vs programmatic deal cadence)
def f47ma_f47_ma_rollup_acquisition_gwdisp504_base_v118_signal(intangibles, revenue):
    qbuild = _safe_div(intangibles - intangibles.shift(63), _mean(revenue, 63))
    b = _std(qbuild, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments-balance build volatility scaled by level (stake-program jitter)
def f47ma_f47_ma_rollup_acquisition_stakevol_252d_base_v119_signal(investments):
    chg = investments - investments.shift(63)
    b = _safe_div(_std(chg, 252), _mean(investments, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- LONGER-HORIZON / MULTI-WINDOW SPREADS ----

# intensity spread 126d vs 504d (short vs long deal-load gap)
def f47ma_f47_ma_rollup_acquisition_intspr_126v504_base_v120_signal(ncfbus, revenue):
    s = _f47_intensity(ncfbus, revenue, 126)
    l = _f47_intensity(ncfbus, revenue, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill-build spread 126d vs 504d (recent deal pulse vs structural accretion)
def f47ma_f47_ma_rollup_acquisition_gwspr_126v504_base_v121_signal(intangibles, revenue):
    s = _f47_goodwill_build(intangibles, revenue, 126)
    l = _f47_goodwill_build(intangibles, revenue, 504)
    b = s - 0.5 * l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal/cap spread 252d vs 504d (recent appetite vs structural deal scale)
def f47ma_f47_ma_rollup_acquisition_dealcapspr_252v504_base_v122_signal(ncfbus, marketcap):
    s = _f47_deal_vs_cap(ncfbus, marketcap, 252)
    l = _f47_deal_vs_cap(ncfbus, marketcap, 504)
    b = s - 0.5 * l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ops-coverage spread 126d vs 504d (recent vs structural deal sustainability)
def f47ma_f47_ma_rollup_acquisition_coverspr_126v504_base_v123_signal(ncfbus, ncfo):
    s = _f47_ops_funding(ncfbus, ncfo, 126).clip(upper=10.0)
    l = _f47_ops_funding(ncfbus, ncfo, 504).clip(upper=10.0)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- ADDITIONAL DISTINCT FACETS ----

# acquisition-vs-divestiture wave phase: sign of 126d net flow vs 504d net flow agreement
def f47ma_f47_ma_rollup_acquisition_wavephase_base_v124_signal(ncfbus):
    short = np.sign(_mean(ncfbus, 126))
    long = np.sign(_mean(ncfbus, 504))
    agree = (short == long).astype(float)
    b = agree.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-spend percentile within trailing-2y distribution (relative deal aggression)
def f47ma_f47_ma_rollup_acquisition_spendpct_504d_base_v125_signal(ncfbus, revenue):
    si = _safe_div(_f47_acq_spend(ncfbus), _mean(revenue, 21))
    b = _rank(si, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale-up vs intangible scale-up correlation, 252d (paired roll-up growth)
def f47ma_f47_ma_rollup_acquisition_revgwcorr_252d_base_v126_signal(revenue, intangibles):
    rg = np.log(revenue.replace(0, np.nan)).diff(21)
    gg = np.log(intangibles.replace(0, np.nan)).diff(21)
    rm = rg - _mean(rg, 252)
    gm = gg - _mean(gg, 252)
    cov = _mean(rm * gm, 252)
    denom = (_std(rg, 252) * _std(gg, 252)).replace(0, np.nan)
    b = cov / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acquisition burst detector: 21d deal spend vs 252d typical, tanh-bounded
def f47ma_f47_ma_rollup_acquisition_burst_21d_base_v127_signal(ncfbus, revenue):
    fast = _safe_div(_mean(_f47_acq_spend(ncfbus), 21), _mean(revenue, 21))
    slow = _safe_div(_mean(_f47_acq_spend(ncfbus), 252), _mean(revenue, 252))
    b = np.tanh(3.0 * (fast - slow))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill build / marketcap, 252d (acquired-value loading per unit equity value)
def f47ma_f47_ma_rollup_acquisition_gwbuildcap_252d_base_v128_signal(intangibles, marketcap):
    build = (intangibles - intangibles.shift(252)).clip(lower=0)
    b = build / _mean(marketcap, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles-to-revenue trajectory slope (roll-up footprint trend), 252d
def f47ma_f47_ma_rollup_acquisition_footslope_252d_base_v129_signal(intangibles, revenue):
    foot = _safe_div(intangibles, revenue)
    b = foot - foot.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-funded growth ratio: revenue growth attributable per unit goodwill build
def f47ma_f47_ma_rollup_acquisition_revpergw_252d_base_v130_signal(revenue, intangibles):
    revg = (_mean(revenue, 63) - _mean(revenue, 63).shift(252)).clip(lower=0)
    gwb = (intangibles - intangibles.shift(252)).clip(lower=0).replace(0, np.nan)
    b = revg / gwb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-deal discipline: fraction of trailing year where deal spend < operating cash
def f47ma_f47_ma_rollup_acquisition_discipline_252d_base_v131_signal(ncfbus, ncfo):
    disc = (_f47_acq_spend(ncfbus) <= ncfo).astype(float)
    b = disc.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stake-flow vs deal-flow lead/lag: 126d stake deployment minus prior 126d deal spend, rev-scaled
def f47ma_f47_ma_rollup_acquisition_stakeleaddeal_base_v132_signal(ncfinv, ncfbus, revenue):
    stake = _safe_div(_sum((-ncfinv).clip(lower=0), 126), _sum(revenue, 126))
    deal_prior = _safe_div(_sum(_f47_acq_spend(ncfbus), 126), _sum(revenue, 126)).shift(126)
    b = stake - deal_prior
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acquisition intensity acceleration (2nd difference of intensity), 63d steps
def f47ma_f47_ma_rollup_acquisition_intensacc_base_v133_signal(ncfbus, revenue):
    intens = _f47_intensity(ncfbus, revenue, 126)
    g = intens - intens.shift(63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill footprint vs marketcap multiple, ranked (relative acquired-value loading)
def f47ma_f47_ma_rollup_acquisition_gwloadrank_252d_base_v134_signal(intangibles, marketcap):
    r = _safe_div(_mean(intangibles, 126), _mean(marketcap, 126))
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal spend relative to its own EWMA, vol-normalised (acquisition impulse z), 63d
def f47ma_f47_ma_rollup_acquisition_impulsez_63d_base_v135_signal(ncfbus, revenue):
    si = _safe_div(_mean(_f47_acq_spend(ncfbus), 63), _mean(revenue, 63))
    ema = si.ewm(span=252, min_periods=63).mean()
    vol = _std(si, 252).replace(0, np.nan)
    b = (si - ema) / vol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divestiture-driven deleveraging: divestiture proceeds vs marketcap, 252d
def f47ma_f47_ma_rollup_acquisition_divestcap_252d_base_v136_signal(ncfbus, marketcap):
    din = _sum(_f47_divest_in(ncfbus), 252)
    b = din / _mean(marketcap, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acquired-asset turnover trend: change in revenue/(intangibles+investments) over a year
def f47ma_f47_ma_rollup_acquisition_acqturntrend_252d_base_v137_signal(revenue, intangibles, investments):
    turn = _safe_div(_mean(revenue, 63), _mean(intangibles + investments, 63))
    b = turn - turn.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill build momentum z-score (deal-cycle phase indicator), 252d
def f47ma_f47_ma_rollup_acquisition_gwmomz_252d_base_v138_signal(intangibles):
    g = np.log(intangibles.replace(0, np.nan)).diff(63)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# externally-funded deal ratio: deal spend vs (ncfo + ncfinv inflow + divest), 252d
def f47ma_f47_ma_rollup_acquisition_extreliance_252d_base_v139_signal(ncfbus, ncfo, ncfinv):
    spend = _sum(_f47_acq_spend(ncfbus), 252)
    internal = _sum(ncfo.clip(lower=0) + ncfinv.clip(lower=0) + _f47_divest_in(ncfbus), 252)
    b = (spend - internal) / (spend + internal).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acquisition cadence weighted by average deal size (serial-acquirer scale composite)
def f47ma_f47_ma_rollup_acquisition_serialscale_252d_base_v140_signal(ncfbus, revenue):
    cad = _f47_material_q(ncfbus, revenue, 0.05).rolling(252, min_periods=126).mean()
    size = _safe_div(_mean(_f47_acq_spend(ncfbus), 252), _mean(revenue, 252))
    b = np.sqrt(cad.clip(lower=0) * size.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-spend trend vs goodwill-build trend divergence (cash now, goodwill later)
def f47ma_f47_ma_rollup_acquisition_spendgwlag_252d_base_v141_signal(ncfbus, intangibles, revenue):
    spendt = _safe_div(_sum(_f47_acq_spend(ncfbus), 126), _sum(revenue, 126))
    gwt = _f47_goodwill_build(intangibles, revenue, 126)
    b = spendt - gwt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net investing outflow (ncfbus + ncfinv) over revenue, signed, 252d (total M&A direction)
def f47ma_f47_ma_rollup_acquisition_netinvest_252d_base_v142_signal(ncfbus, ncfinv, revenue):
    b = _sum(ncfbus + ncfinv, 252) / _sum(revenue, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acquisition activity entropy proxy: 1 - concentration of spend over trailing year
def f47ma_f47_ma_rollup_acquisition_spendspread_252d_base_v143_signal(ncfbus):
    spend = _f47_acq_spend(ncfbus)
    peak = spend.rolling(252, min_periods=126).max()
    mean = _mean(spend, 252)
    b = mean / peak.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration around deal-cadence peaks (post-deal organic lift), 126d
def f47ma_f47_ma_rollup_acquisition_postacc_126d_base_v144_signal(revenue, ncfbus):
    rl = np.log(revenue.replace(0, np.nan))
    g = rl.diff(63)
    acc = g - g.shift(63)
    cad = _f47_material_q(ncfbus, revenue, 0.05).rolling(126, min_periods=63).mean()
    b = acc * (0.5 + cad)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill-per-marketcap year-over-year change (acquired-value loading trend)
def f47ma_f47_ma_rollup_acquisition_gwcapyoy_252d_base_v145_signal(intangibles, marketcap):
    r = _safe_div(_mean(intangibles, 21), _mean(marketcap, 21))
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deal-spend run-rate vs revenue run-rate growth gap (acquisition outpacing topline)
def f47ma_f47_ma_rollup_acquisition_spendvsrevg_252d_base_v146_signal(ncfbus, revenue):
    spendg = np.log((_mean(_f47_acq_spend(ncfbus), 63) + 1.0) / (_mean(_f47_acq_spend(ncfbus), 63).shift(252) + 1.0))
    revg = np.log(_mean(revenue, 63).replace(0, np.nan) / _mean(revenue, 63).shift(252).replace(0, np.nan))
    b = spendg - revg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ops-funding buffer trend: change in (ncfo - deal spend)/marketcap over a year
def f47ma_f47_ma_rollup_acquisition_buftrend_252d_base_v147_signal(ncfo, ncfbus, marketcap):
    buf = _safe_div(_sum(ncfo, 252) - _sum(_f47_acq_spend(ncfbus), 252), _mean(marketcap, 252))
    b = buf - buf.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-build to investments-build ratio (whole-co vs stake deployment mix), 252d
def f47ma_f47_ma_rollup_acquisition_buildmix_252d_base_v148_signal(intangibles, investments):
    gwb = (intangibles - intangibles.shift(252)).clip(lower=0)
    stb = (investments - investments.shift(252)).clip(lower=0)
    b = (gwb - stb) / (gwb + stb).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acquisition program maturity: long-horizon goodwill base growth smoothness, 504d
def f47ma_f47_ma_rollup_acquisition_progmaturity_504d_base_v149_signal(intangibles, revenue):
    g = np.log(intangibles.replace(0, np.nan)).diff(63)
    smooth = -_safe_div(_std(g, 504), _mean(g, 504).abs())
    foot = _safe_div(_mean(intangibles, 504), _mean(revenue, 504))
    b = smooth + 0.1 * foot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total deployment burden vs operating engine: (deal + stake out) over |ncfo|, 252d
def f47ma_f47_ma_rollup_acquisition_deployburden_252d_base_v150_signal(ncfbus, ncfinv, ncfo):
    deploy = _sum(_f47_acq_spend(ncfbus) + (-ncfinv).clip(lower=0), 252)
    ops = _sum(ncfo.abs(), 252).replace(0, np.nan)
    b = deploy / ops
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47ma_f47_ma_rollup_acquisition_intensity_63d_base_v076_signal,
    f47ma_f47_ma_rollup_acquisition_intensdisp_504d_base_v077_signal,
    f47ma_f47_ma_rollup_acquisition_intensregime_252d_base_v078_signal,
    f47ma_f47_ma_rollup_acquisition_busshareinv_252d_base_v079_signal,
    f47ma_f47_ma_rollup_acquisition_intensyoy_252d_base_v080_signal,
    f47ma_f47_ma_rollup_acquisition_boltoncad_252d_base_v081_signal,
    f47ma_f47_ma_rollup_acquisition_acqstreak_252d_base_v082_signal,
    f47ma_f47_ma_rollup_acquisition_sizedisp_504d_base_v083_signal,
    f47ma_f47_ma_rollup_acquisition_cadstab_504d_base_v084_signal,
    f47ma_f47_ma_rollup_acquisition_acqentries_252d_base_v085_signal,
    f47ma_f47_ma_rollup_acquisition_fcafterdeal_252d_base_v086_signal,
    f47ma_f47_ma_rollup_acquisition_coverfail_252d_base_v087_signal,
    f47ma_f47_ma_rollup_acquisition_coveryoy_252d_base_v088_signal,
    f47ma_f47_ma_rollup_acquisition_internalfund_252d_base_v089_signal,
    f47ma_f47_ma_rollup_acquisition_gwbuildrank_252d_base_v090_signal,
    f47ma_f47_ma_rollup_acquisition_gwimpair_252d_base_v091_signal,
    f47ma_f47_ma_rollup_acquisition_gwvscapchg_252d_base_v092_signal,
    f47ma_f47_ma_rollup_acquisition_gwdisp_126d_base_v093_signal,
    f47ma_f47_ma_rollup_acquisition_gwcumfoot_504d_base_v094_signal,
    f47ma_f47_ma_rollup_acquisition_invdeploycap_252d_base_v095_signal,
    f47ma_f47_ma_rollup_acquisition_invvol_252d_base_v096_signal,
    f47ma_f47_ma_rollup_acquisition_stakeaccrev_126d_base_v097_signal,
    f47ma_f47_ma_rollup_acquisition_stakeshare_252d_base_v098_signal,
    f47ma_f47_ma_rollup_acquisition_invsign_504d_base_v099_signal,
    f47ma_f47_ma_rollup_acquisition_signsmooth_252d_base_v100_signal,
    f47ma_f47_ma_rollup_acquisition_netflowrev_252d_base_v101_signal,
    f47ma_f47_ma_rollup_acquisition_recyc_504d_base_v102_signal,
    f47ma_f47_ma_rollup_acquisition_acqregime_252d_base_v103_signal,
    f47ma_f47_ma_rollup_acquisition_dealvscap_126d_base_v104_signal,
    f47ma_f47_ma_rollup_acquisition_richbuy_252d_base_v105_signal,
    f47ma_f47_ma_rollup_acquisition_dealcapmom_252d_base_v106_signal,
    f47ma_f47_ma_rollup_acquisition_gwcapz_252d_base_v107_signal,
    f47ma_f47_ma_rollup_acquisition_inorgsig_252d_base_v108_signal,
    f47ma_f47_ma_rollup_acquisition_lagdealrev_252d_base_v109_signal,
    f47ma_f47_ma_rollup_acquisition_revperspend_504d_base_v110_signal,
    f47ma_f47_ma_rollup_acquisition_organicres_252d_base_v111_signal,
    f47ma_f47_ma_rollup_acquisition_rollhealth_252d_base_v112_signal,
    f47ma_f47_ma_rollup_acquisition_overpay_252d_base_v113_signal,
    f47ma_f47_ma_rollup_acquisition_deploybreadthz_252d_base_v114_signal,
    f47ma_f47_ma_rollup_acquisition_extintens_126d_base_v115_signal,
    f47ma_f47_ma_rollup_acquisition_busskew_252d_base_v116_signal,
    f47ma_f47_ma_rollup_acquisition_buskurt_252d_base_v117_signal,
    f47ma_f47_ma_rollup_acquisition_gwdisp504_base_v118_signal,
    f47ma_f47_ma_rollup_acquisition_stakevol_252d_base_v119_signal,
    f47ma_f47_ma_rollup_acquisition_intspr_126v504_base_v120_signal,
    f47ma_f47_ma_rollup_acquisition_gwspr_126v504_base_v121_signal,
    f47ma_f47_ma_rollup_acquisition_dealcapspr_252v504_base_v122_signal,
    f47ma_f47_ma_rollup_acquisition_coverspr_126v504_base_v123_signal,
    f47ma_f47_ma_rollup_acquisition_wavephase_base_v124_signal,
    f47ma_f47_ma_rollup_acquisition_spendpct_504d_base_v125_signal,
    f47ma_f47_ma_rollup_acquisition_revgwcorr_252d_base_v126_signal,
    f47ma_f47_ma_rollup_acquisition_burst_21d_base_v127_signal,
    f47ma_f47_ma_rollup_acquisition_gwbuildcap_252d_base_v128_signal,
    f47ma_f47_ma_rollup_acquisition_footslope_252d_base_v129_signal,
    f47ma_f47_ma_rollup_acquisition_revpergw_252d_base_v130_signal,
    f47ma_f47_ma_rollup_acquisition_discipline_252d_base_v131_signal,
    f47ma_f47_ma_rollup_acquisition_stakeleaddeal_base_v132_signal,
    f47ma_f47_ma_rollup_acquisition_intensacc_base_v133_signal,
    f47ma_f47_ma_rollup_acquisition_gwloadrank_252d_base_v134_signal,
    f47ma_f47_ma_rollup_acquisition_impulsez_63d_base_v135_signal,
    f47ma_f47_ma_rollup_acquisition_divestcap_252d_base_v136_signal,
    f47ma_f47_ma_rollup_acquisition_acqturntrend_252d_base_v137_signal,
    f47ma_f47_ma_rollup_acquisition_gwmomz_252d_base_v138_signal,
    f47ma_f47_ma_rollup_acquisition_extreliance_252d_base_v139_signal,
    f47ma_f47_ma_rollup_acquisition_serialscale_252d_base_v140_signal,
    f47ma_f47_ma_rollup_acquisition_spendgwlag_252d_base_v141_signal,
    f47ma_f47_ma_rollup_acquisition_netinvest_252d_base_v142_signal,
    f47ma_f47_ma_rollup_acquisition_spendspread_252d_base_v143_signal,
    f47ma_f47_ma_rollup_acquisition_postacc_126d_base_v144_signal,
    f47ma_f47_ma_rollup_acquisition_gwcapyoy_252d_base_v145_signal,
    f47ma_f47_ma_rollup_acquisition_spendvsrevg_252d_base_v146_signal,
    f47ma_f47_ma_rollup_acquisition_buftrend_252d_base_v147_signal,
    f47ma_f47_ma_rollup_acquisition_buildmix_252d_base_v148_signal,
    f47ma_f47_ma_rollup_acquisition_progmaturity_504d_base_v149_signal,
    f47ma_f47_ma_rollup_acquisition_deployburden_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_MA_ROLLUP_ACQUISITION_REGISTRY_076_150 = REGISTRY


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

    print("OK f47_ma_rollup_acquisition_base_076_150_claude: %d features pass" % n_features)
