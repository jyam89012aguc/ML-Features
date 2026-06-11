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
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
    return s - s.shift(w)


# ===== folder domain primitives (dividend & payout sustainability) =====
def _f50_payer(dps):
    # binary dividend-payer flag from per-share dividend level
    return (dps > 0).astype(float)


def _f50_growth(s, w):
    # log growth of a (positive) series over w days
    return np.log(s.replace(0, np.nan).abs() / s.shift(w).replace(0, np.nan).abs())


def _f50_fcf_cover(fcf, ncfdiv):
    # FCF coverage of the cash dividend; ncfdiv is a cash OUTFLOW (negative) -> use magnitude
    return fcf / ncfdiv.abs().replace(0, np.nan)


def _f50_pref_overhang(prefdivis, netinccmn):
    # preferred-dividend claim relative to common net income
    return prefdivis / netinccmn.replace(0, np.nan)


def _f50_payout_earn(ncfdiv, netinccmn):
    # cash dividend paid vs common earnings (cash payout ratio)
    return ncfdiv.abs() / netinccmn.replace(0, np.nan)


def _f50_cut_risk(payoutratio, fcf, ncfdiv):
    # 1 when payout > 1 OR FCF below the cash dividend
    over = (payoutratio > 1.0).astype(float)
    under = (fcf < ncfdiv.abs()).astype(float)
    return ((over + under) > 0).astype(float)


# ============================================================
# dividend-payer flag: fraction of last year as a payer (regime)
def f50dp_f50_dividend_payout_payerfrac_252d_base_v001_signal(dps):
    p = _f50_payer(dps)
    b = p.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend initiation: dps crossing 0 -> positive within the last quarter
def f50dp_f50_dividend_payout_initiation_63d_base_v002_signal(dps):
    p = _f50_payer(dps)
    started = ((p == 1) & (p.shift(21) == 0)).astype(float)
    b = started.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield level, z-scored vs its own year of history
def f50dp_f50_dividend_payout_divyieldz_252d_base_v003_signal(divyield):
    b = _z(divyield, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield level, percentile-ranked vs 504d history
def f50dp_f50_dividend_payout_divyieldrank_504d_base_v004_signal(divyield):
    b = _rank(divyield, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raw payout-ratio level smoothed over a quarter (sustainability level)
def f50dp_f50_dividend_payout_payoutlvl_63d_base_v005_signal(payoutratio):
    b = _mean(payoutratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout-ratio trend: change over half a year
def f50dp_f50_dividend_payout_payouttrend_126d_base_v006_signal(payoutratio):
    b = _slope(payoutratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF coverage of the dividend (fcf / |ncfdiv|), smoothed
def f50dp_f50_dividend_payout_fcfcover_63d_base_v007_signal(fcf, ncfdiv):
    c = _f50_fcf_cover(fcf, ncfdiv)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF coverage downside risk: mean shortfall below 1.0 over a year (asymmetric)
def f50dp_f50_dividend_payout_coverdownside_252d_base_v008_signal(fcf, ncfdiv):
    c = _f50_fcf_cover(fcf, ncfdiv)
    short = (1.0 - c).clip(lower=0)
    b = _mean(short, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-per-share growth over a year (dps trajectory)
def f50dp_f50_dividend_payout_dpsgrowth_252d_base_v009_signal(dps):
    b = _f50_growth(dps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-per-share growth over half a year
def f50dp_f50_dividend_payout_dpsgrowth_126d_base_v010_signal(dps):
    b = _f50_growth(dps, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-dividend overhang: prefdivis / netinccmn (claim on common)
def f50dp_f50_dividend_payout_prefoverhang_63d_base_v011_signal(prefdivis, netinccmn):
    o = _f50_pref_overhang(prefdivis, netinccmn)
    b = _mean(o, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cut-risk flag fraction over the last year (payout>1 or FCF<dividend)
def f50dp_f50_dividend_payout_cutriskfrac_252d_base_v012_signal(payoutratio, fcf, ncfdiv):
    r = _f50_cut_risk(payoutratio, fcf, ncfdiv)
    b = r.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash payout vs earnings de-trended: |ncfdiv|/netinccmn minus its 252d mean
def f50dp_f50_dividend_payout_cashpayoutmr_63d_base_v013_signal(ncfdiv, netinccmn):
    pe = _f50_payout_earn(ncfdiv, netinccmn)
    b = _mean(pe, 63) - _mean(pe, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend covered by EPS: dps / eps (per-share payout)
def f50dp_f50_dividend_payout_dpseps_63d_base_v014_signal(dps, eps):
    r = dps / eps.replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield vs its own slow EMA (yield displacement; price-stress proxy)
def f50dp_f50_dividend_payout_yielddisp_126d_base_v015_signal(divyield):
    b = divyield - divyield.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout-ratio above the danger line: time spent with payoutratio>1 over a year
def f50dp_f50_dividend_payout_overpayfrac_252d_base_v016_signal(payoutratio):
    over = (payoutratio > 1.0).astype(float)
    b = over.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funded-dividend streak: fraction of last quarter FCF exceeded the dividend
def f50dp_f50_dividend_payout_selffundfrac_63d_base_v017_signal(fcf, ncfdiv):
    selffund = (fcf > ncfdiv.abs()).astype(float)
    b = selffund.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend growth acceleration: dps yoy growth now vs a quarter ago
def f50dp_f50_dividend_payout_dpsaccel_252d_base_v018_signal(dps):
    g = _f50_growth(dps, 252)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred overhang z-scored vs 252d history (rising senior claims)
def f50dp_f50_dividend_payout_prefoverhangz_252d_base_v019_signal(prefdivis, netinccmn):
    o = _f50_pref_overhang(prefdivis, netinccmn)
    b = _z(o, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio z-scored vs 252d (de-trended payout stress)
def f50dp_f50_dividend_payout_payoutz_252d_base_v020_signal(payoutratio):
    b = _z(payoutratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield momentum: change over a quarter
def f50dp_f50_dividend_payout_yieldmom_63d_base_v021_signal(divyield):
    b = _slope(divyield, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF coverage rank vs 504d history (relative safety)
def f50dp_f50_dividend_payout_fcfcoverrank_504d_base_v022_signal(fcf, ncfdiv):
    c = _f50_fcf_cover(fcf, ncfdiv)
    b = _rank(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend cash outflow growth (|ncfdiv| trajectory) over a year
def f50dp_f50_dividend_payout_divcashgrowth_252d_base_v023_signal(ncfdiv):
    b = _f50_growth(ncfdiv.abs(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings cushion above dividend: (netinccmn - |ncfdiv|) / |netinccmn|
def f50dp_f50_dividend_payout_earncushion_63d_base_v024_signal(netinccmn, ncfdiv):
    cushion = (netinccmn - ncfdiv.abs()) / netinccmn.abs().replace(0, np.nan)
    b = _mean(cushion, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-payer persistence: streak length of payer regime normalized by year
def f50dp_f50_dividend_payout_payerstreak_252d_base_v025_signal(dps):
    p = _f50_payer(dps)
    grp = (p != p.shift(1)).cumsum()
    streak = p.groupby(grp).cumcount() + 1
    b = (streak * p) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield dispersion (instability of the yield) over a quarter
def f50dp_f50_dividend_payout_yielddisp2_63d_base_v026_signal(divyield):
    b = _std(divyield, 63) / _mean(divyield, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout-ratio whipsaw: dispersion of payout ratio over half a year
def f50dp_f50_dividend_payout_payoutvol_126d_base_v027_signal(payoutratio):
    b = _std(payoutratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps level relative to its own 252d max (cut from peak distribution)
def f50dp_f50_dividend_payout_dpsfrompeak_252d_base_v028_signal(dps):
    pk = dps.rolling(252, min_periods=126).max()
    b = dps / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF coverage below 1 frequency (under-covered dividend regime)
def f50dp_f50_dividend_payout_undercover_252d_base_v029_signal(fcf, ncfdiv):
    c = _f50_fcf_cover(fcf, ncfdiv)
    under = (c < 1.0).astype(float)
    b = under.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-of-preferred payout: |ncfdiv| relative to (netinccmn - prefdivis)
def f50dp_f50_dividend_payout_netprefpay_63d_base_v030_signal(ncfdiv, netinccmn, prefdivis):
    avail = (netinccmn - prefdivis).replace(0, np.nan)
    r = ncfdiv.abs() / avail
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield interacted with payout ratio (high-yield & high-payout = trap)
def f50dp_f50_dividend_payout_yieldtrap_63d_base_v031_signal(divyield, payoutratio):
    trap = divyield * payoutratio.clip(lower=0)
    b = _mean(trap, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps growth stability: mean/std of yoy dps growth (smooth grower quality)
def f50dp_f50_dividend_payout_dpsgrowthstab_252d_base_v032_signal(dps):
    g = _f50_growth(dps, 63)
    b = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred drag: prefdivis as a fraction of |ncfdiv| (senior vs common cash)
def f50dp_f50_dividend_payout_prefdrag_63d_base_v033_signal(prefdivis, ncfdiv):
    r = prefdivis / ncfdiv.abs().replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio vs FCF-cover divergence (accrual payout > cash payout safety)
def f50dp_f50_dividend_payout_payoutfcfdiv_63d_base_v034_signal(payoutratio, fcf, ncfdiv):
    cover = _f50_fcf_cover(fcf, ncfdiv)
    div = payoutratio - 1.0 / cover.replace(0, np.nan)
    b = _mean(div, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield level smoothed (carry attractiveness)
def f50dp_f50_dividend_payout_yieldlvl_126d_base_v035_signal(divyield):
    b = _mean(divyield, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EPS coverage of dps: eps / dps (times earnings covers the dividend)
def f50dp_f50_dividend_payout_epscover_63d_base_v036_signal(eps, dps):
    r = eps / dps.replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend initiation maturity: time since first becoming a payer in window
def f50dp_f50_dividend_payout_payermature_504d_base_v037_signal(dps):
    p = _f50_payer(dps)
    cum = p.rolling(504, min_periods=126).sum()
    b = cum / 504.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-out-of-FCF z-scored (rising payout pressure on free cash flow)
def f50dp_f50_dividend_payout_divfcfz_252d_base_v038_signal(ncfdiv, fcf):
    r = ncfdiv.abs() / fcf.abs().replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage asymmetry: FCF cover minus earnings cover of the dividend
def f50dp_f50_dividend_payout_coverasym_63d_base_v039_signal(fcf, ncfdiv, netinccmn):
    fcfcover = _f50_fcf_cover(fcf, ncfdiv)
    earncover = netinccmn / ncfdiv.abs().replace(0, np.nan)
    asym = np.tanh(fcfcover - earncover)
    b = _mean(asym, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield trend / vol (risk-adjusted yield drift)
def f50dp_f50_dividend_payout_yieldtrendvol_126d_base_v040_signal(divyield):
    tr = _slope(divyield, 63)
    vol = _std(divyield, 126)
    b = tr / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout-ratio crossing above 1 events over a year (newly stretched)
def f50dp_f50_dividend_payout_overpayentries_252d_base_v041_signal(payoutratio):
    over = (payoutratio > 1.0).astype(float)
    entries = ((over == 1) & (over.shift(21) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-cut events: dps falling >5% from prior level over a quarter
def f50dp_f50_dividend_payout_cutcount_252d_base_v042_signal(dps):
    drop = (dps < dps.shift(63) * 0.95).astype(float)
    b = drop.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend growth net of preferred drag (common-holder dividend quality)
def f50dp_f50_dividend_payout_dpsnetpref_252d_base_v043_signal(dps, prefdivis, netinccmn):
    g = _f50_growth(dps, 252)
    drag = _f50_pref_overhang(prefdivis, netinccmn).clip(lower=0)
    b = g - drag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF coverage trend: change in coverage over half a year
def f50dp_f50_dividend_payout_covertrend_126d_base_v044_signal(fcf, ncfdiv):
    c = _f50_fcf_cover(fcf, ncfdiv)
    b = _slope(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield level relative to year-ago yield (yield re-rating)
def f50dp_f50_dividend_payout_yieldyoy_252d_base_v045_signal(divyield):
    b = divyield - divyield.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps/eps payout ratio trend (rising per-share payout strain)
def f50dp_f50_dividend_payout_dpsepstrend_126d_base_v046_signal(dps, eps):
    r = dps / eps.replace(0, np.nan)
    b = _slope(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total cash to holders out of free cash flow: (|ncfdiv|+prefdivis) / |fcf|
def f50dp_f50_dividend_payout_totaldistrfcf_63d_base_v047_signal(ncfdiv, prefdivis, fcf):
    tot = (ncfdiv.abs() + prefdivis) / fcf.abs().replace(0, np.nan)
    b = _mean(tot, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield extreme: distance above 252d yield mean in std units, clipped positive
def f50dp_f50_dividend_payout_yieldspike_252d_base_v048_signal(divyield):
    z = _z(divyield, 252)
    b = z.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage-weighted payer flag (safe payer vs stretched payer)
def f50dp_f50_dividend_payout_safepayer_63d_base_v049_signal(dps, fcf, ncfdiv):
    p = _f50_payer(dps)
    cover = _f50_fcf_cover(fcf, ncfdiv)
    b = p * np.tanh(cover.clip(lower=0) - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio relative to its 252d min (climbing off a low base)
def f50dp_f50_dividend_payout_payoutfrombase_252d_base_v050_signal(payoutratio):
    lo = payoutratio.rolling(252, min_periods=126).min()
    b = payoutratio / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps level scaled by eps level (smoothed retention complement)
def f50dp_f50_dividend_payout_retention_126d_base_v051_signal(dps, eps):
    payout = dps / eps.replace(0, np.nan)
    b = 1.0 - _mean(payout, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-cover dispersion (coverage instability) over a year
def f50dp_f50_dividend_payout_coverdisp_252d_base_v052_signal(fcf, ncfdiv):
    c = _f50_fcf_cover(fcf, ncfdiv)
    b = _std(c, 252) / _mean(c, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-overhang trend (rising senior dividend burden)
def f50dp_f50_dividend_payout_prefoverhangtr_126d_base_v053_signal(prefdivis, netinccmn):
    o = _f50_pref_overhang(prefdivis, netinccmn)
    b = _slope(o, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield-to-payout balance: high yield but low payout = sustainable income
def f50dp_f50_dividend_payout_yieldquality_63d_base_v054_signal(divyield, payoutratio):
    q = divyield / payoutratio.clip(lower=0.01)
    b = _mean(q, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend cash growth vs earnings growth divergence (paying ahead of profit)
def f50dp_f50_dividend_payout_paygrowthgap_252d_base_v055_signal(ncfdiv, netinccmn):
    gd = _f50_growth(ncfdiv.abs(), 252)
    ge = _f50_growth(netinccmn, 252)
    b = gd - ge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cut-risk flag interacted with yield (high-risk high-yield trap intensity)
def f50dp_f50_dividend_payout_riskyieldtrap_63d_base_v056_signal(payoutratio, fcf, ncfdiv, divyield):
    r = _f50_cut_risk(payoutratio, fcf, ncfdiv)
    b = (r * divyield).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps EWMA displacement (recent dividend acceleration vs trend)
def f50dp_f50_dividend_payout_dpsdisp_126d_base_v057_signal(dps):
    fast = dps.ewm(span=42, min_periods=21).mean()
    slow = dps.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage cushion in EPS terms: (eps - dps) / |eps|
def f50dp_f50_dividend_payout_epscushion_63d_base_v058_signal(eps, dps):
    cushion = (eps - dps) / eps.abs().replace(0, np.nan)
    b = _mean(cushion, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout-ratio rank vs 504d history (relative payout stretch)
def f50dp_f50_dividend_payout_payoutrank_504d_base_v059_signal(payoutratio):
    b = _rank(payoutratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield risk-reward: yield / yield-vol (Sharpe-like income carry)
def f50dp_f50_dividend_payout_yieldsharpe_126d_base_v060_signal(divyield):
    b = _mean(divyield, 126) / _std(divyield, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-covered & growing dividend (quality grower): cover>1 & dps rising
def f50dp_f50_dividend_payout_qualgrower_252d_base_v061_signal(fcf, ncfdiv, dps):
    cover = _f50_fcf_cover(fcf, ncfdiv)
    grow = (dps > dps.shift(63)).astype(float)
    safe = (cover > 1.0).astype(float)
    b = (safe * grow).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paying-more-than-earned regime: fraction of year |ncfdiv| exceeds common earnings
def f50dp_f50_dividend_payout_payexceedfrac_252d_base_v062_signal(ncfdiv, netinccmn):
    exceed = (ncfdiv.abs() > netinccmn).astype(float)
    b = exceed.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield acceleration (2nd-order yield change as price-stress signal)
def f50dp_f50_dividend_payout_yieldaccel_63d_base_v063_signal(divyield):
    d = _slope(divyield, 63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-dividend burden growth z-scored vs 252d (rising senior cash claim)
def f50dp_f50_dividend_payout_prefburdenz_252d_base_v064_signal(prefdivis):
    g = _f50_growth(prefdivis, 63)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps level trend vs its long EMA (sustained raise regime)
def f50dp_f50_dividend_payout_dpsraise_252d_base_v065_signal(dps):
    above = (dps > dps.ewm(span=252, min_periods=63).mean()).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-dividend growth relative to common cash-dividend growth (mix shift)
def f50dp_f50_dividend_payout_prefmixshift_252d_base_v066_signal(prefdivis, ncfdiv):
    gp = _f50_growth(prefdivis, 252)
    gc = _f50_growth(ncfdiv.abs(), 252)
    b = gp - gc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage-adjusted yield: divyield x tanh(FCF cover) (sustainable yield)
def f50dp_f50_dividend_payout_sustyield_63d_base_v067_signal(divyield, fcf, ncfdiv):
    cover = _f50_fcf_cover(fcf, ncfdiv)
    b = (divyield * np.tanh(cover.clip(lower=0))).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio mean-reversion: level minus its own 252d mean
def f50dp_f50_dividend_payout_payoutmr_252d_base_v068_signal(payoutratio):
    b = payoutratio - _mean(payoutratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend per share scaled by FCF per dividend coverage interaction
def f50dp_f50_dividend_payout_dpscoverint_63d_base_v069_signal(dps, fcf, ncfdiv):
    cover = _f50_fcf_cover(fcf, ncfdiv)
    b = (dps * cover.clip(lower=0)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout-direction disagreement: payoutratio rising while per-share payout falling
def f50dp_f50_dividend_payout_payoutdisagree_252d_base_v070_signal(payoutratio, dps, eps):
    pershare = dps / eps.replace(0, np.nan)
    disagree = (np.sign(_slope(payoutratio, 21)) != np.sign(_slope(pershare, 21))).astype(float)
    b = disagree.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year yield re-rating: current yield vs its 252d-lagged 252d mean
def f50dp_f50_dividend_payout_yieldrerate_1260d_base_v071_signal(divyield):
    anchor = _mean(divyield, 252).shift(252)
    b = divyield / anchor.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-claim share of total dividend cash, ranked vs 252d history (mix)
def f50dp_f50_dividend_payout_prefshare_252d_base_v072_signal(prefdivis, ncfdiv):
    share = prefdivis / (prefdivis + ncfdiv.abs()).replace(0, np.nan)
    b = _rank(share, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps rebound off its 504d trough (dividend reinstatement / recovery)
def f50dp_f50_dividend_payout_dpsrebound_504d_base_v073_signal(dps):
    lo = dps.rolling(504, min_periods=252).min()
    b = dps / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout sustainability composite: low payout + high cover, smoothed
def f50dp_f50_dividend_payout_sustcomposite_126d_base_v074_signal(payoutratio, fcf, ncfdiv):
    cover = _f50_fcf_cover(fcf, ncfdiv)
    comp = np.tanh(cover.clip(lower=0) - 1.0) - (payoutratio - 0.5)
    b = _mean(comp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash dividend intensity per unit FCF, ranked vs 252d history
def f50dp_f50_dividend_payout_divfcfrank_252d_base_v075_signal(ncfdiv, fcf):
    r = ncfdiv.abs() / fcf.abs().replace(0, np.nan)
    b = _rank(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f50dp_f50_dividend_payout_payerfrac_252d_base_v001_signal,
    f50dp_f50_dividend_payout_initiation_63d_base_v002_signal,
    f50dp_f50_dividend_payout_divyieldz_252d_base_v003_signal,
    f50dp_f50_dividend_payout_divyieldrank_504d_base_v004_signal,
    f50dp_f50_dividend_payout_payoutlvl_63d_base_v005_signal,
    f50dp_f50_dividend_payout_payouttrend_126d_base_v006_signal,
    f50dp_f50_dividend_payout_fcfcover_63d_base_v007_signal,
    f50dp_f50_dividend_payout_coverdownside_252d_base_v008_signal,
    f50dp_f50_dividend_payout_dpsgrowth_252d_base_v009_signal,
    f50dp_f50_dividend_payout_dpsgrowth_126d_base_v010_signal,
    f50dp_f50_dividend_payout_prefoverhang_63d_base_v011_signal,
    f50dp_f50_dividend_payout_cutriskfrac_252d_base_v012_signal,
    f50dp_f50_dividend_payout_cashpayoutmr_63d_base_v013_signal,
    f50dp_f50_dividend_payout_dpseps_63d_base_v014_signal,
    f50dp_f50_dividend_payout_yielddisp_126d_base_v015_signal,
    f50dp_f50_dividend_payout_overpayfrac_252d_base_v016_signal,
    f50dp_f50_dividend_payout_selffundfrac_63d_base_v017_signal,
    f50dp_f50_dividend_payout_dpsaccel_252d_base_v018_signal,
    f50dp_f50_dividend_payout_prefoverhangz_252d_base_v019_signal,
    f50dp_f50_dividend_payout_payoutz_252d_base_v020_signal,
    f50dp_f50_dividend_payout_yieldmom_63d_base_v021_signal,
    f50dp_f50_dividend_payout_fcfcoverrank_504d_base_v022_signal,
    f50dp_f50_dividend_payout_divcashgrowth_252d_base_v023_signal,
    f50dp_f50_dividend_payout_earncushion_63d_base_v024_signal,
    f50dp_f50_dividend_payout_payerstreak_252d_base_v025_signal,
    f50dp_f50_dividend_payout_yielddisp2_63d_base_v026_signal,
    f50dp_f50_dividend_payout_payoutvol_126d_base_v027_signal,
    f50dp_f50_dividend_payout_dpsfrompeak_252d_base_v028_signal,
    f50dp_f50_dividend_payout_undercover_252d_base_v029_signal,
    f50dp_f50_dividend_payout_netprefpay_63d_base_v030_signal,
    f50dp_f50_dividend_payout_yieldtrap_63d_base_v031_signal,
    f50dp_f50_dividend_payout_dpsgrowthstab_252d_base_v032_signal,
    f50dp_f50_dividend_payout_prefdrag_63d_base_v033_signal,
    f50dp_f50_dividend_payout_payoutfcfdiv_63d_base_v034_signal,
    f50dp_f50_dividend_payout_yieldlvl_126d_base_v035_signal,
    f50dp_f50_dividend_payout_epscover_63d_base_v036_signal,
    f50dp_f50_dividend_payout_payermature_504d_base_v037_signal,
    f50dp_f50_dividend_payout_divfcfz_252d_base_v038_signal,
    f50dp_f50_dividend_payout_coverasym_63d_base_v039_signal,
    f50dp_f50_dividend_payout_yieldtrendvol_126d_base_v040_signal,
    f50dp_f50_dividend_payout_overpayentries_252d_base_v041_signal,
    f50dp_f50_dividend_payout_cutcount_252d_base_v042_signal,
    f50dp_f50_dividend_payout_dpsnetpref_252d_base_v043_signal,
    f50dp_f50_dividend_payout_covertrend_126d_base_v044_signal,
    f50dp_f50_dividend_payout_yieldyoy_252d_base_v045_signal,
    f50dp_f50_dividend_payout_dpsepstrend_126d_base_v046_signal,
    f50dp_f50_dividend_payout_totaldistrfcf_63d_base_v047_signal,
    f50dp_f50_dividend_payout_yieldspike_252d_base_v048_signal,
    f50dp_f50_dividend_payout_safepayer_63d_base_v049_signal,
    f50dp_f50_dividend_payout_payoutfrombase_252d_base_v050_signal,
    f50dp_f50_dividend_payout_retention_126d_base_v051_signal,
    f50dp_f50_dividend_payout_coverdisp_252d_base_v052_signal,
    f50dp_f50_dividend_payout_prefoverhangtr_126d_base_v053_signal,
    f50dp_f50_dividend_payout_yieldquality_63d_base_v054_signal,
    f50dp_f50_dividend_payout_paygrowthgap_252d_base_v055_signal,
    f50dp_f50_dividend_payout_riskyieldtrap_63d_base_v056_signal,
    f50dp_f50_dividend_payout_dpsdisp_126d_base_v057_signal,
    f50dp_f50_dividend_payout_epscushion_63d_base_v058_signal,
    f50dp_f50_dividend_payout_payoutrank_504d_base_v059_signal,
    f50dp_f50_dividend_payout_yieldsharpe_126d_base_v060_signal,
    f50dp_f50_dividend_payout_qualgrower_252d_base_v061_signal,
    f50dp_f50_dividend_payout_payexceedfrac_252d_base_v062_signal,
    f50dp_f50_dividend_payout_yieldaccel_63d_base_v063_signal,
    f50dp_f50_dividend_payout_prefburdenz_252d_base_v064_signal,
    f50dp_f50_dividend_payout_dpsraise_252d_base_v065_signal,
    f50dp_f50_dividend_payout_prefmixshift_252d_base_v066_signal,
    f50dp_f50_dividend_payout_sustyield_63d_base_v067_signal,
    f50dp_f50_dividend_payout_payoutmr_252d_base_v068_signal,
    f50dp_f50_dividend_payout_dpscoverint_63d_base_v069_signal,
    f50dp_f50_dividend_payout_payoutdisagree_252d_base_v070_signal,
    f50dp_f50_dividend_payout_yieldrerate_1260d_base_v071_signal,
    f50dp_f50_dividend_payout_prefshare_252d_base_v072_signal,
    f50dp_f50_dividend_payout_dpsrebound_504d_base_v073_signal,
    f50dp_f50_dividend_payout_sustcomposite_126d_base_v074_signal,
    f50dp_f50_dividend_payout_divfcfrank_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_DIVIDEND_PAYOUT_REGISTRY_001_075 = REGISTRY


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

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False, noise=0.0,
              cycle=0.0, cyc_period=378):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if cycle > 0:
            phase = g.uniform(0, 2 * np.pi)
            s = s + base * cycle * np.sin(2 * np.pi * np.arange(n) / cyc_period + phase)
        if noise > 0:
            s = s * (1.0 + g.normal(0.0, noise, n))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    # dividend/payout small positive levels; dps/divyield/payoutratio dip to 0
    # in stretches so payer-flag / initiation / overpay features actually vary.
    dps = _fund(201, base=0.6, drift=0.02, vol=0.10, allow_neg=True, noise=0.03,
                cycle=0.8, cyc_period=340).clip(lower=0.0).rename("dps")
    divyield = _fund(202, base=0.03, drift=0.005, vol=0.12, noise=0.05,
                     cycle=0.30, cyc_period=300).clip(lower=0.0).rename("divyield")
    payoutratio = _fund(203, base=0.7, drift=0.01, vol=0.16, noise=0.06,
                        cycle=0.9, cyc_period=410).clip(lower=0.0).rename("payoutratio")
    ncfdiv = (-_fund(204, base=4e7, drift=0.02, vol=0.10, noise=0.04,
                     cycle=0.3, cyc_period=370)).rename("ncfdiv")
    prefdivis = _fund(205, base=6e6, drift=0.01, vol=0.12, noise=0.05,
                      cycle=0.4, cyc_period=440).clip(lower=0.0).rename("prefdivis")
    fcf = _fund(206, base=1.0e8, drift=0.0, vol=0.16, allow_neg=True, noise=0.05,
                cycle=0.9, cyc_period=470).rename("fcf")
    netinccmn = _fund(207, base=9e7, drift=0.0, vol=0.15, allow_neg=True, noise=0.05,
                      cycle=0.9, cyc_period=410).rename("netinccmn")
    eps = _fund(208, base=1.4, drift=0.0, vol=0.15, allow_neg=True, noise=0.05,
                cycle=0.9, cyc_period=380).rename("eps")

    cols = {"dps": dps, "divyield": divyield, "payoutratio": payoutratio,
            "ncfdiv": ncfdiv, "prefdivis": prefdivis, "fcf": fcf,
            "netinccmn": netinccmn, "eps": eps}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (
            name, set(meta["inputs"]) - ALLOW)
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

    print("OK f50_dividend_payout_base_001_075_claude: %d features pass" % n_features)
