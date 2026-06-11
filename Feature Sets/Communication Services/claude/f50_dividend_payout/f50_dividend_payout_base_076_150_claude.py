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
    return (dps > 0).astype(float)


def _f50_growth(s, w):
    return np.log(s.replace(0, np.nan).abs() / s.shift(w).replace(0, np.nan).abs())


def _f50_fcf_cover(fcf, ncfdiv):
    return fcf / ncfdiv.abs().replace(0, np.nan)


def _f50_pref_overhang(prefdivis, netinccmn):
    return prefdivis / netinccmn.replace(0, np.nan)


def _f50_payout_earn(ncfdiv, netinccmn):
    return ncfdiv.abs() / netinccmn.replace(0, np.nan)


def _f50_cut_risk(payoutratio, fcf, ncfdiv):
    over = (payoutratio > 1.0).astype(float)
    under = (fcf < ncfdiv.abs()).astype(float)
    return ((over + under) > 0).astype(float)


# ============================================================
# dividend yield level smoothed over half a year (long carry)
def f50dp_f50_dividend_payout_yieldlvl_252d_base_v076_signal(divyield):
    b = _mean(divyield, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps level vs its 126d EMA (raise momentum)
def f50dp_f50_dividend_payout_dpsmom_126d_base_v077_signal(dps):
    b = dps / dps.ewm(span=126, min_periods=42).mean() - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio percentile-rank vs 252d (relative stretch, short)
def f50dp_f50_dividend_payout_payoutrank_252d_base_v078_signal(payoutratio):
    b = _rank(payoutratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF coverage minus 1, sign x sqrt magnitude (compressed safety margin)
def f50dp_f50_dividend_payout_coversafety_63d_base_v079_signal(fcf, ncfdiv):
    margin = _f50_fcf_cover(fcf, ncfdiv) - 1.0
    sm = np.sign(margin) * margin.abs() ** 0.5
    b = _mean(sm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred overhang rank vs 504d (relative senior-claim burden)
def f50dp_f50_dividend_payout_prefoverhangrank_504d_base_v080_signal(prefdivis, netinccmn):
    o = _f50_pref_overhang(prefdivis, netinccmn)
    b = _rank(o, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend cut-risk streak length (consecutive risk days, normalized)
def f50dp_f50_dividend_payout_cutriskstreak_base_v081_signal(payoutratio, fcf, ncfdiv):
    r = _f50_cut_risk(payoutratio, fcf, ncfdiv)
    grp = (r != r.shift(1)).cumsum()
    streak = r.groupby(grp).cumcount() + 1
    b = (streak * r) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps growth over two years (long-horizon dividend CAGR proxy)
def f50dp_f50_dividend_payout_dpsgrowth_504d_base_v082_signal(dps):
    b = _f50_growth(dps, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield vs payout interaction z-scored (yield-trap intensity, de-trended)
def f50dp_f50_dividend_payout_yieldtrapz_252d_base_v083_signal(divyield, payoutratio):
    trap = divyield * payoutratio.clip(lower=0)
    b = _z(trap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps coverage of dps z-scored (de-trended earnings safety margin)
def f50dp_f50_dividend_payout_epscoverz_252d_base_v084_signal(eps, dps):
    r = eps / dps.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash dividend out of FCF, smoothed (payout-of-cashflow level)
def f50dp_f50_dividend_payout_divfcf_63d_base_v085_signal(ncfdiv, fcf):
    r = ncfdiv.abs() / fcf.abs().replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio acceleration: change-of-change over a quarter
def f50dp_f50_dividend_payout_payoutaccel_63d_base_v086_signal(payoutratio):
    d = _slope(payoutratio, 63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year as a payer at the long horizon (504d payer regime)
def f50dp_f50_dividend_payout_payerfrac_504d_base_v087_signal(dps):
    p = _f50_payer(dps)
    b = p.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield drawdown from its 252d high (yield compression)
def f50dp_f50_dividend_payout_yieldfrompeak_252d_base_v088_signal(divyield):
    pk = divyield.rolling(252, min_periods=126).max()
    b = divyield / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage trend over a quarter (short-horizon safety direction)
def f50dp_f50_dividend_payout_covertrend_63d_base_v089_signal(fcf, ncfdiv):
    c = _f50_fcf_cover(fcf, ncfdiv)
    b = _slope(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps stability: coefficient of variation of dps over a year (smooth payer)
def f50dp_f50_dividend_payout_dpsstab_252d_base_v090_signal(dps):
    b = _std(dps, 252) / _mean(dps, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of common earnings left after the preferred claim (dilution of common)
def f50dp_f50_dividend_payout_commonavailfrac_63d_base_v091_signal(netinccmn, prefdivis):
    frac = (netinccmn - prefdivis) / netinccmn.abs().replace(0, np.nan)
    b = _mean(frac, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield shock intensity: smoothed magnitude of |z| over a quarter
def f50dp_f50_dividend_payout_yieldshock_252d_base_v092_signal(divyield):
    z = _z(divyield, 126)
    b = _mean(z.abs(), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio above earnings: clipped excess of payoutratio over 1, smoothed
def f50dp_f50_dividend_payout_payoutexcess_126d_base_v093_signal(payoutratio):
    excess = (payoutratio - 1.0).clip(lower=0)
    b = _mean(excess, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend growth vs yield interaction (grower vs high-yielder profile)
def f50dp_f50_dividend_payout_growyieldmix_252d_base_v094_signal(dps, divyield):
    g = _f50_growth(dps, 252)
    b = g - _z(divyield, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash dividend per dollar of net income, trend over half a year
def f50dp_f50_dividend_payout_cashpayouttrend_126d_base_v095_signal(ncfdiv, netinccmn):
    pe = _f50_payout_earn(ncfdiv, netinccmn)
    b = _slope(pe, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-overhang spike: clipped positive z of overhang (senior stress)
def f50dp_f50_dividend_payout_prefspike_252d_base_v096_signal(prefdivis, netinccmn):
    o = _f50_pref_overhang(prefdivis, netinccmn)
    b = _z(o, 252).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage regime distance: cover minus its rolling 252d median-ish mean, ranked
def f50dp_f50_dividend_payout_coverregime_252d_base_v097_signal(fcf, ncfdiv):
    c = _f50_fcf_cover(fcf, ncfdiv)
    dev = c - _mean(c, 252)
    b = _rank(dev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps raise frequency: fraction of quarters with a higher dps over a year
def f50dp_f50_dividend_payout_raisefreq_252d_base_v098_signal(dps):
    up = (dps > dps.shift(63)).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield vs its 504d level (long yield re-rating)
def f50dp_f50_dividend_payout_yieldrerate_504d_base_v099_signal(divyield):
    b = divyield / _mean(divyield, 504).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio x cut-risk flag (stretched & at-risk intensity)
def f50dp_f50_dividend_payout_stretchrisk_63d_base_v100_signal(payoutratio, fcf, ncfdiv):
    r = _f50_cut_risk(payoutratio, fcf, ncfdiv)
    b = (payoutratio.clip(lower=0) * r).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EPS-coverage shortfall: fraction of quarter eps below dps (earnings under dividend)
def f50dp_f50_dividend_payout_epsshort_63d_base_v101_signal(eps, dps):
    short = (eps < dps).astype(float)
    b = short.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend cash growth acceleration (|ncfdiv| growth now vs a quarter ago)
def f50dp_f50_dividend_payout_divcashaccel_252d_base_v102_signal(ncfdiv):
    g = _f50_growth(ncfdiv.abs(), 252)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net payout to common after preferred, ranked vs 252d (common-holder share)
def f50dp_f50_dividend_payout_commonshare_252d_base_v103_signal(ncfdiv, prefdivis):
    share = ncfdiv.abs() / (ncfdiv.abs() + prefdivis).replace(0, np.nan)
    b = _rank(share, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield momentum risk-adjusted: yield slope over its own dispersion (quarter)
def f50dp_f50_dividend_payout_yieldmomrisk_63d_base_v104_signal(divyield):
    tr = _slope(divyield, 21)
    vol = _std(divyield, 63)
    b = _mean(tr / vol.replace(0, np.nan), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps log-level smoothed (scale of the dividend program)
def f50dp_f50_dividend_payout_dpslevel_126d_base_v105_signal(dps):
    b = _mean(np.log1p(dps.clip(lower=0)), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage volatility (instability of FCF cover) over half a year
def f50dp_f50_dividend_payout_covervol_126d_base_v106_signal(fcf, ncfdiv):
    c = _f50_fcf_cover(fcf, ncfdiv)
    b = _std(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio vs eps-payout divergence z (reported vs derived consistency)
def f50dp_f50_dividend_payout_payoutderivez_252d_base_v107_signal(payoutratio, dps, eps):
    derived = dps / eps.replace(0, np.nan)
    b = _z(payoutratio - derived, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield breadth: fraction of year yield above its 252d mean (high-carry regime)
def f50dp_f50_dividend_payout_highyieldfrac_252d_base_v108_signal(divyield):
    above = (divyield > _mean(divyield, 252)).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred drag trend: prefdivis/|ncfdiv| change over a quarter
def f50dp_f50_dividend_payout_prefdragtrend_63d_base_v109_signal(prefdivis, ncfdiv):
    r = prefdivis / ncfdiv.abs().replace(0, np.nan)
    b = _slope(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcf-covered payer & low-payout regime (high-quality income)
def f50dp_f50_dividend_payout_qualincome_252d_base_v110_signal(dps, fcf, ncfdiv, payoutratio):
    p = _f50_payer(dps)
    safe = (_f50_fcf_cover(fcf, ncfdiv) > 1.0).astype(float)
    low = (payoutratio < 0.6).astype(float)
    b = (p * safe * low).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps drawdown velocity: change in dps-from-peak over a month
def f50dp_f50_dividend_payout_dpsddvel_252d_base_v111_signal(dps):
    pk = dps.rolling(252, min_periods=126).max()
    dd = dps / pk.replace(0, np.nan) - 1.0
    b = dd - dd.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash payout out of FCF spike: clipped positive z (cash strain)
def f50dp_f50_dividend_payout_divfcfspike_252d_base_v112_signal(ncfdiv, fcf):
    r = ncfdiv.abs() / fcf.abs().replace(0, np.nan)
    b = _z(r, 252).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred dividend share of earnings trend (senior burden direction)
def f50dp_f50_dividend_payout_prefearntrend_126d_base_v113_signal(prefdivis, netinccmn):
    o = _f50_pref_overhang(prefdivis, netinccmn)
    b = o.ewm(span=63, min_periods=21).mean() - o.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend coverage by earnings: netinccmn / |ncfdiv|, smoothed (earnings cover)
def f50dp_f50_dividend_payout_earncover_63d_base_v114_signal(netinccmn, ncfdiv):
    c = netinccmn / ncfdiv.abs().replace(0, np.nan)
    b = _mean(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield z minus payout z (cheap income vs payout strain composite)
def f50dp_f50_dividend_payout_incomecomposite_252d_base_v115_signal(divyield, payoutratio):
    b = _z(divyield, 252) - _z(payoutratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps EWMA crossover signal (fast above slow = raising regime)
def f50dp_f50_dividend_payout_dpscross_126d_base_v116_signal(dps):
    fast = dps.ewm(span=21, min_periods=10).mean()
    slow = dps.ewm(span=126, min_periods=42).mean()
    b = np.tanh((fast - slow) / slow.replace(0, np.nan) * 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage and growth joint quality: tanh(cover-1) x dps growth
def f50dp_f50_dividend_payout_safegrowth_252d_base_v117_signal(fcf, ncfdiv, dps):
    cover = _f50_fcf_cover(fcf, ncfdiv)
    g = _f50_growth(dps, 252)
    b = _mean(np.tanh(cover - 1.0) * g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio dispersion relative to level (normalized instability)
def f50dp_f50_dividend_payout_payoutcv_252d_base_v118_signal(payoutratio):
    b = _std(payoutratio, 252) / _mean(payoutratio, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend initiation depth: dps level at the long horizon relative to first-quartile
def f50dp_f50_dividend_payout_initdepth_504d_base_v119_signal(dps):
    lo = dps.rolling(504, min_periods=252).quantile(0.25)
    b = dps - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-overhang acceleration (2nd diff of senior claim)
def f50dp_f50_dividend_payout_prefaccel_252d_base_v120_signal(prefdivis, netinccmn):
    o = _f50_pref_overhang(prefdivis, netinccmn)
    d = _slope(o, 63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cut-risk vs coverage interaction: risk flag minus tanh(cover-1) (net distress)
def f50dp_f50_dividend_payout_netdistress_63d_base_v121_signal(payoutratio, fcf, ncfdiv):
    r = _f50_cut_risk(payoutratio, fcf, ncfdiv)
    cover = _f50_fcf_cover(fcf, ncfdiv)
    b = _mean(r - np.tanh(cover - 1.0), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield slope over a year minus payout slope (yield outrunning payout)
def f50dp_f50_dividend_payout_yieldpayoutgap_252d_base_v122_signal(divyield, payoutratio):
    b = _slope(divyield, 252) - _slope(_z(payoutratio, 252), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps cushion over dividend, ranked vs 504d (relative per-share safety)
def f50dp_f50_dividend_payout_epscushionrank_504d_base_v123_signal(eps, dps):
    cushion = (eps - dps) / eps.abs().replace(0, np.nan)
    b = _rank(cushion, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend cash vs FCF gap sign x magnitude (cash-funded vs cash-strained)
def f50dp_f50_dividend_payout_divfcfgap_63d_base_v124_signal(ncfdiv, fcf):
    gap = (fcf.abs() - ncfdiv.abs()) / (fcf.abs() + ncfdiv.abs()).replace(0, np.nan)
    b = _mean(gap, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payer-to-nonpayer transition count over the long horizon (suspension events)
def f50dp_f50_dividend_payout_suspendcount_504d_base_v125_signal(dps):
    p = _f50_payer(dps)
    stop = ((p == 0) & (p.shift(21) == 1)).astype(float)
    b = stop.rolling(504, min_periods=252).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage trough: minimum FCF cover over a year (worst-case safety)
def f50dp_f50_dividend_payout_covertrough_252d_base_v126_signal(fcf, ncfdiv):
    c = _f50_fcf_cover(fcf, ncfdiv)
    b = c.rolling(252, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend per share scaled by earnings cover (sustainable dps magnitude)
def f50dp_f50_dividend_payout_susdps_63d_base_v127_signal(dps, netinccmn, ncfdiv):
    earncover = (netinccmn / ncfdiv.abs().replace(0, np.nan)).clip(lower=0)
    b = _mean(dps * np.tanh(earncover), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio mean over a quarter minus its long EMA (short payout displacement)
def f50dp_f50_dividend_payout_payoutdisp_126d_base_v128_signal(payoutratio):
    b = _mean(payoutratio, 63) - payoutratio.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend growth net of earnings growth, ranked (paying ahead of profit, relative)
def f50dp_f50_dividend_payout_paygrowthrank_252d_base_v129_signal(ncfdiv, netinccmn):
    gd = _f50_growth(ncfdiv.abs(), 252)
    ge = _f50_growth(netinccmn, 252)
    b = _rank(gd - ge, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield drawdown duration: fraction of year yield >10% below its 252d high
def f50dp_f50_dividend_payout_yielddddur_252d_base_v130_signal(divyield):
    pk = divyield.rolling(252, min_periods=126).max()
    under = (divyield < pk * 0.9).astype(float)
    b = under.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred claim vs FCF spike: clipped z of prefdivis/|fcf| (senior cash stress)
def f50dp_f50_dividend_payout_preffcfspike_252d_base_v131_signal(prefdivis, fcf):
    r = prefdivis / fcf.abs().replace(0, np.nan)
    b = _z(r, 252).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps yoy growth smoothed and ranked (relative dividend grower)
def f50dp_f50_dividend_payout_dpsgrowthrank_504d_base_v132_signal(dps):
    g = _f50_growth(dps, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings cover trend over half a year (earnings safety direction)
def f50dp_f50_dividend_payout_earncovertrend_126d_base_v133_signal(netinccmn, ncfdiv):
    c = netinccmn / ncfdiv.abs().replace(0, np.nan)
    b = _slope(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cut-risk frequency at the short horizon (recent distress density)
def f50dp_f50_dividend_payout_cutriskfrac_63d_base_v134_signal(payoutratio, fcf, ncfdiv):
    r = _f50_cut_risk(payoutratio, fcf, ncfdiv)
    b = r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield smoothed minus its cross-time rank center (carry de-rank)
def f50dp_f50_dividend_payout_yieldlevelrank_252d_base_v135_signal(divyield):
    sm = _mean(divyield, 63)
    b = _rank(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout sustainability score: earnings cover x (1 - payout), smoothed
def f50dp_f50_dividend_payout_sustscore_126d_base_v136_signal(netinccmn, ncfdiv, payoutratio):
    earncover = (netinccmn / ncfdiv.abs().replace(0, np.nan)).clip(lower=0)
    score = np.tanh(earncover - 1.0) * (1.0 - payoutratio.clip(upper=2.0))
    b = _mean(score, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps acceleration over half a year (dividend trajectory curvature)
def f50dp_f50_dividend_payout_dpsaccel_126d_base_v137_signal(dps):
    g = _f50_growth(dps, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-payout-exceeds-FCF regime: fraction of year (|ncfdiv|+prefdivis) > fcf
def f50dp_f50_dividend_payout_totpayexceedfrac_252d_base_v138_signal(ncfdiv, prefdivis, fcf):
    exceed = ((ncfdiv.abs() + prefdivis) > fcf).astype(float)
    b = exceed.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year dps strictly increasing month-over-month (consistent grower)
def f50dp_f50_dividend_payout_monogrow_252d_base_v139_signal(dps):
    up = (dps > dps.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps-payout (dps/eps) rank vs 252d, only when a payer (per-share strain)
def f50dp_f50_dividend_payout_epspayoutrank_252d_base_v140_signal(dps, eps):
    payout = dps / eps.replace(0, np.nan)
    b = _rank(payout, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage skew: difference of upside and downside coverage excursions
def f50dp_f50_dividend_payout_coverskew_252d_base_v141_signal(fcf, ncfdiv):
    c = _f50_fcf_cover(fcf, ncfdiv)
    up = (c - 1.0).clip(lower=0)
    dn = (1.0 - c).clip(lower=0)
    b = _mean(up, 252) - _mean(dn, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# preferred overhang above its 252d floor (cushion vs best-case senior burden)
def f50dp_f50_dividend_payout_prefoverhangfloor_252d_base_v142_signal(prefdivis, netinccmn):
    o = _f50_pref_overhang(prefdivis, netinccmn)
    floor = o.rolling(252, min_periods=126).quantile(0.1)
    b = o - floor
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield convexity: squared deviation from its 252d mean (tail-yield)
def f50dp_f50_dividend_payout_yieldconvex_252d_base_v143_signal(divyield):
    dev = divyield - _mean(divyield, 252)
    b = _mean(np.sign(dev) * dev ** 2, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funded dividend at the long horizon: fraction of 504d FCF>dividend
def f50dp_f50_dividend_payout_selffundfrac_504d_base_v144_signal(fcf, ncfdiv):
    sf = (fcf > ncfdiv.abs()).astype(float)
    b = sf.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps relative to eps trajectory cross: payout ratio implied vs reported drift
def f50dp_f50_dividend_payout_payoutdrift_252d_base_v145_signal(dps, eps, payoutratio):
    implied = dps / eps.replace(0, np.nan)
    b = _slope(implied, 252) - _slope(payoutratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage breach magnitude: how far below 1 the worst quarter cover fell, smoothed
def f50dp_f50_dividend_payout_coverbreach_126d_base_v146_signal(fcf, ncfdiv):
    c = _f50_fcf_cover(fcf, ncfdiv)
    breach = (1.0 - c.rolling(63, min_periods=21).min()).clip(lower=0)
    b = _mean(breach, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend program scale momentum: |ncfdiv| vs its 252d EMA (program expansion)
def f50dp_f50_dividend_payout_progscale_252d_base_v147_signal(ncfdiv):
    lvl = ncfdiv.abs()
    b = lvl / lvl.ewm(span=252, min_periods=63).mean() - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield-quality at long horizon: divyield x tanh(earnings cover) (sustainable carry)
def f50dp_f50_dividend_payout_sustcarry_126d_base_v148_signal(divyield, netinccmn, ncfdiv):
    earncover = (netinccmn / ncfdiv.abs().replace(0, np.nan)).clip(lower=0)
    b = _mean(divyield * np.tanh(earncover), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout-ratio regime persistence: fraction of year payout within 0.4-0.8 band (healthy)
def f50dp_f50_dividend_payout_healthyband_252d_base_v149_signal(payoutratio):
    healthy = ((payoutratio >= 0.4) & (payoutratio <= 0.8)).astype(float)
    b = healthy.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite cut-risk: blend of overpay, undercover, and pref overhang, smoothed
def f50dp_f50_dividend_payout_cutriskcomposite_126d_base_v150_signal(payoutratio, fcf, ncfdiv, prefdivis, netinccmn):
    over = (payoutratio - 1.0).clip(lower=0)
    under = (1.0 - _f50_fcf_cover(fcf, ncfdiv)).clip(lower=0)
    pref = _f50_pref_overhang(prefdivis, netinccmn).clip(lower=0)
    b = _mean(over + under + 0.5 * pref, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f50dp_f50_dividend_payout_yieldlvl_252d_base_v076_signal,
    f50dp_f50_dividend_payout_dpsmom_126d_base_v077_signal,
    f50dp_f50_dividend_payout_payoutrank_252d_base_v078_signal,
    f50dp_f50_dividend_payout_coversafety_63d_base_v079_signal,
    f50dp_f50_dividend_payout_prefoverhangrank_504d_base_v080_signal,
    f50dp_f50_dividend_payout_cutriskstreak_base_v081_signal,
    f50dp_f50_dividend_payout_dpsgrowth_504d_base_v082_signal,
    f50dp_f50_dividend_payout_yieldtrapz_252d_base_v083_signal,
    f50dp_f50_dividend_payout_epscoverz_252d_base_v084_signal,
    f50dp_f50_dividend_payout_divfcf_63d_base_v085_signal,
    f50dp_f50_dividend_payout_payoutaccel_63d_base_v086_signal,
    f50dp_f50_dividend_payout_payerfrac_504d_base_v087_signal,
    f50dp_f50_dividend_payout_yieldfrompeak_252d_base_v088_signal,
    f50dp_f50_dividend_payout_covertrend_63d_base_v089_signal,
    f50dp_f50_dividend_payout_dpsstab_252d_base_v090_signal,
    f50dp_f50_dividend_payout_commonavailfrac_63d_base_v091_signal,
    f50dp_f50_dividend_payout_yieldshock_252d_base_v092_signal,
    f50dp_f50_dividend_payout_payoutexcess_126d_base_v093_signal,
    f50dp_f50_dividend_payout_growyieldmix_252d_base_v094_signal,
    f50dp_f50_dividend_payout_cashpayouttrend_126d_base_v095_signal,
    f50dp_f50_dividend_payout_prefspike_252d_base_v096_signal,
    f50dp_f50_dividend_payout_coverregime_252d_base_v097_signal,
    f50dp_f50_dividend_payout_raisefreq_252d_base_v098_signal,
    f50dp_f50_dividend_payout_yieldrerate_504d_base_v099_signal,
    f50dp_f50_dividend_payout_stretchrisk_63d_base_v100_signal,
    f50dp_f50_dividend_payout_epsshort_63d_base_v101_signal,
    f50dp_f50_dividend_payout_divcashaccel_252d_base_v102_signal,
    f50dp_f50_dividend_payout_commonshare_252d_base_v103_signal,
    f50dp_f50_dividend_payout_yieldmomrisk_63d_base_v104_signal,
    f50dp_f50_dividend_payout_dpslevel_126d_base_v105_signal,
    f50dp_f50_dividend_payout_covervol_126d_base_v106_signal,
    f50dp_f50_dividend_payout_payoutderivez_252d_base_v107_signal,
    f50dp_f50_dividend_payout_highyieldfrac_252d_base_v108_signal,
    f50dp_f50_dividend_payout_prefdragtrend_63d_base_v109_signal,
    f50dp_f50_dividend_payout_qualincome_252d_base_v110_signal,
    f50dp_f50_dividend_payout_dpsddvel_252d_base_v111_signal,
    f50dp_f50_dividend_payout_divfcfspike_252d_base_v112_signal,
    f50dp_f50_dividend_payout_prefearntrend_126d_base_v113_signal,
    f50dp_f50_dividend_payout_earncover_63d_base_v114_signal,
    f50dp_f50_dividend_payout_incomecomposite_252d_base_v115_signal,
    f50dp_f50_dividend_payout_dpscross_126d_base_v116_signal,
    f50dp_f50_dividend_payout_safegrowth_252d_base_v117_signal,
    f50dp_f50_dividend_payout_payoutcv_252d_base_v118_signal,
    f50dp_f50_dividend_payout_initdepth_504d_base_v119_signal,
    f50dp_f50_dividend_payout_prefaccel_252d_base_v120_signal,
    f50dp_f50_dividend_payout_netdistress_63d_base_v121_signal,
    f50dp_f50_dividend_payout_yieldpayoutgap_252d_base_v122_signal,
    f50dp_f50_dividend_payout_epscushionrank_504d_base_v123_signal,
    f50dp_f50_dividend_payout_divfcfgap_63d_base_v124_signal,
    f50dp_f50_dividend_payout_suspendcount_504d_base_v125_signal,
    f50dp_f50_dividend_payout_covertrough_252d_base_v126_signal,
    f50dp_f50_dividend_payout_susdps_63d_base_v127_signal,
    f50dp_f50_dividend_payout_payoutdisp_126d_base_v128_signal,
    f50dp_f50_dividend_payout_paygrowthrank_252d_base_v129_signal,
    f50dp_f50_dividend_payout_yielddddur_252d_base_v130_signal,
    f50dp_f50_dividend_payout_preffcfspike_252d_base_v131_signal,
    f50dp_f50_dividend_payout_dpsgrowthrank_504d_base_v132_signal,
    f50dp_f50_dividend_payout_earncovertrend_126d_base_v133_signal,
    f50dp_f50_dividend_payout_cutriskfrac_63d_base_v134_signal,
    f50dp_f50_dividend_payout_yieldlevelrank_252d_base_v135_signal,
    f50dp_f50_dividend_payout_sustscore_126d_base_v136_signal,
    f50dp_f50_dividend_payout_dpsaccel_126d_base_v137_signal,
    f50dp_f50_dividend_payout_totpayexceedfrac_252d_base_v138_signal,
    f50dp_f50_dividend_payout_monogrow_252d_base_v139_signal,
    f50dp_f50_dividend_payout_epspayoutrank_252d_base_v140_signal,
    f50dp_f50_dividend_payout_coverskew_252d_base_v141_signal,
    f50dp_f50_dividend_payout_prefoverhangfloor_252d_base_v142_signal,
    f50dp_f50_dividend_payout_yieldconvex_252d_base_v143_signal,
    f50dp_f50_dividend_payout_selffundfrac_504d_base_v144_signal,
    f50dp_f50_dividend_payout_payoutdrift_252d_base_v145_signal,
    f50dp_f50_dividend_payout_coverbreach_126d_base_v146_signal,
    f50dp_f50_dividend_payout_progscale_252d_base_v147_signal,
    f50dp_f50_dividend_payout_sustcarry_126d_base_v148_signal,
    f50dp_f50_dividend_payout_healthyband_252d_base_v149_signal,
    f50dp_f50_dividend_payout_cutriskcomposite_126d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_DIVIDEND_PAYOUT_REGISTRY_076_150 = REGISTRY


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

    print("OK f50_dividend_payout_base_076_150_claude: %d features pass" % n_features)
