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


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        return float((idx * (a - a.mean())).sum() / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (dividend / payout policy) =====
def _f22_yield(divyield):
    return divyield


def _f22_payout(payoutratio):
    return payoutratio


def _f22_fcf_cover(ncfdiv, fcf):
    return fcf / ncfdiv.abs().replace(0, np.nan)


def _f22_div_to_netinc(ncfdiv, netinc):
    return ncfdiv.abs() / netinc.replace(0, np.nan)


def _f22_sustain(fcf, ncfdiv):
    return (fcf - ncfdiv.abs()) / fcf.abs().replace(0, np.nan)


def _f22_buffer(fcf, ncfdiv):
    return fcf - ncfdiv.abs()


# ============================================================
# yield momentum: change in dividend yield over a quarter
def f22dp_f22_dividend_payout_policy_yldmom_63d_base_v076_signal(divyield):
    y = _f22_yield(divyield).rolling(21, min_periods=10).mean()
    b = y - y.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield slope (linear-regression trend of yield over a half year)
def f22dp_f22_dividend_payout_policy_yldslope_126d_base_v077_signal(divyield):
    b = _slope(_f22_yield(divyield), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield acceleration: change in the quarterly yield change (yield inflection)
def f22dp_f22_dividend_payout_policy_yldaccel_126d_base_v078_signal(divyield):
    y = _f22_yield(divyield).rolling(21, min_periods=10).mean()
    d = y - y.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout slope (trend of payout ratio over a half year)
def f22dp_f22_dividend_payout_policy_payslope_126d_base_v079_signal(payoutratio):
    b = _slope(_f22_payout(payoutratio), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage slope (trend of FCF dividend coverage over a year)
def f22dp_f22_dividend_payout_policy_covslope_252d_base_v080_signal(ncfdiv, fcf):
    b = _slope(_f22_fcf_cover(ncfdiv, fcf), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps slope normalized by dps level (dividend growth rate)
def f22dp_f22_dividend_payout_policy_dpsgrowth_252d_base_v081_signal(dps):
    sl = _slope(dps, 252)
    b = sl / _mean(dps, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield vs payout z-spread (income-vs-policy disagreement)
def f22dp_f22_dividend_payout_policy_yldpayspread_252d_base_v082_signal(divyield, payoutratio):
    b = _z(_f22_yield(divyield), 252) - _z(_f22_payout(payoutratio), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage half-year vs full-year mean ratio (coverage term structure)
def f22dp_f22_dividend_payout_policy_covterm_252d_base_v083_signal(ncfdiv, fcf):
    cov = _f22_fcf_cover(ncfdiv, fcf)
    b = _mean(cov, 126) / _mean(cov, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield short vs long mean ratio (yield term structure)
def f22dp_f22_dividend_payout_policy_yldterm_252d_base_v084_signal(divyield):
    y = _f22_yield(divyield)
    b = _mean(y, 63) / _mean(y, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout short vs long mean ratio (payout term structure)
def f22dp_f22_dividend_payout_policy_payterm_252d_base_v085_signal(payoutratio):
    p = _f22_payout(payoutratio)
    b = _mean(p, 63) / _mean(p, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend coverage skewness proxy (mean - median of coverage)
def f22dp_f22_dividend_payout_policy_covskew_252d_base_v086_signal(ncfdiv, fcf):
    cov = _f22_fcf_cover(ncfdiv, fcf)
    med = cov.rolling(252, min_periods=126).median()
    b = (_mean(cov, 252) - med) / _std(cov, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield skewness proxy (mean minus median normalized by dispersion)
def f22dp_f22_dividend_payout_policy_yldskew_252d_base_v087_signal(divyield):
    y = _f22_yield(divyield)
    med = y.rolling(252, min_periods=126).median()
    b = (_mean(y, 252) - med) / _std(y, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income coverage of dividend slope (earnings-coverage trend)
def f22dp_f22_dividend_payout_policy_nicovslope_252d_base_v088_signal(ncfdiv, netinc):
    raw = netinc / ncfdiv.abs().replace(0, np.nan)
    b = _slope(np.tanh(raw / 5.0), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend per share x payout interaction momentum
def f22dp_f22_dividend_payout_policy_dpspaymom_252d_base_v089_signal(dps, payoutratio):
    raw = dps * _f22_payout(payoutratio)
    sm = raw.rolling(63, min_periods=21).mean()
    b = np.log(sm.clip(lower=1e-6) / sm.shift(252).clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcf per dividend dollar, demeaned by sector-free own history (relative coverage)
def f22dp_f22_dividend_payout_policy_relcov_504d_base_v090_signal(ncfdiv, fcf):
    cov = _f22_fcf_cover(ncfdiv, fcf)
    b = cov - cov.rolling(504, min_periods=126).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout vs coverage co-movement: rolling correlation of payout and coverage
def f22dp_f22_dividend_payout_policy_paycovcorr_252d_base_v091_signal(payoutratio, ncfdiv, fcf):
    p = _f22_payout(payoutratio)
    c = _f22_fcf_cover(ncfdiv, fcf)
    b = p.rolling(252, min_periods=126).corr(c)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield vs dps co-movement (yield driven by price vs dividend)
def f22dp_f22_dividend_payout_policy_ylddpscorr_252d_base_v092_signal(divyield, dps):
    b = _f22_yield(divyield).rolling(252, min_periods=126).corr(dps)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend cut depth: largest 63d drop in dps over the last year
def f22dp_f22_dividend_payout_policy_dpscut_252d_base_v093_signal(dps):
    chg = dps / dps.shift(63).replace(0, np.nan) - 1.0
    b = chg.rolling(252, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend raise frequency: fraction of months dps rose year-over-year
def f22dp_f22_dividend_payout_policy_dpsraise_252d_base_v094_signal(dps):
    rose = (dps > dps.shift(63)).astype(float)
    b = rose.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage-adjusted payout: payout ratio divided by coverage (uncovered payout intensity)
def f22dp_f22_dividend_payout_policy_uncovpay_126d_base_v095_signal(payoutratio, ncfdiv, fcf):
    cov = _f22_fcf_cover(ncfdiv, fcf).clip(lower=0.1)
    raw = _f22_payout(payoutratio) / cov
    b = raw.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield x sustainability: high yield credited only when buffer is positive
def f22dp_f22_dividend_payout_policy_yldsust_252d_base_v096_signal(divyield, fcf, ncfdiv):
    s = _f22_sustain(fcf, ncfdiv)
    raw = _f22_yield(divyield) * np.tanh(3.0 * s)
    b = raw.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout convexity momentum: change in squared deviation of payout from 0.6
def f22dp_f22_dividend_payout_policy_payconvmom_252d_base_v097_signal(payoutratio):
    conv = (_f22_payout(payoutratio) - 0.6) ** 2
    sm = conv.rolling(63, min_periods=21).mean()
    b = sm - sm.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income per dividend dollar, ranked (earnings coverage percentile)
def f22dp_f22_dividend_payout_policy_nicovrank_504d_base_v098_signal(ncfdiv, netinc):
    raw = netinc / ncfdiv.abs().replace(0, np.nan)
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buffer (fcf - dividend) absolute level z-scored vs own history
def f22dp_f22_dividend_payout_policy_bufabsz_252d_base_v099_signal(fcf, ncfdiv):
    b = _z(_f22_buffer(fcf, ncfdiv), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend coverage z minus its 1y-lagged z (coverage regime shift)
def f22dp_f22_dividend_payout_policy_covregime_252d_base_v100_signal(ncfdiv, fcf):
    z = _z(_f22_fcf_cover(ncfdiv, fcf), 252)
    b = z - z.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield mean-reversion gap: yield minus its 252d median (rich/cheap income)
def f22dp_f22_dividend_payout_policy_yldmrgap_252d_base_v101_signal(divyield):
    y = _f22_yield(divyield)
    med = y.rolling(252, min_periods=126).median()
    b = y - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout mean-reversion gap: payout minus its 252d median
def f22dp_f22_dividend_payout_policy_paymrgap_252d_base_v102_signal(payoutratio):
    p = _f22_payout(payoutratio)
    med = p.rolling(252, min_periods=126).median()
    b = p - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage volatility-of-volatility (instability of the coverage dispersion)
def f22dp_f22_dividend_payout_policy_covvov_252d_base_v103_signal(ncfdiv, fcf):
    cov = _f22_fcf_cover(ncfdiv, fcf)
    vol = _std(cov, 63)
    b = _std(vol, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend growth stability: inverse std of year-over-year dps growth
def f22dp_f22_dividend_payout_policy_dpsgrowstab_504d_base_v104_signal(dps):
    g = np.log(dps.clip(lower=1e-6) / dps.shift(63).clip(lower=1e-6))
    b = 1.0 / (1.0 + _std(g, 504))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout funded by FCF: buffer-to-fcf ratio scaled by payout (self-funded distribution)
def f22dp_f22_dividend_payout_policy_fcffunded_252d_base_v105_signal(fcf, ncfdiv, payoutratio):
    funded = _f22_buffer(fcf, ncfdiv) / fcf.abs().replace(0, np.nan)
    raw = funded * _f22_payout(payoutratio)
    b = raw.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income trajectory backing the dividend: netinc slope scaled by dividend
def f22dp_f22_dividend_payout_policy_nibackslope_252d_base_v106_signal(netinc, ncfdiv):
    sl = _slope(netinc, 252)
    b = sl / ncfdiv.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield percentile vs 252d window (shorter-history yield richness)
def f22dp_f22_dividend_payout_policy_yldrank_252d_base_v107_signal(divyield):
    b = _rank(_f22_yield(divyield), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout percentile vs 252d window
def f22dp_f22_dividend_payout_policy_payrank_252d_base_v108_signal(payoutratio):
    b = _rank(_f22_payout(payoutratio), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage percentile vs 252d window
def f22dp_f22_dividend_payout_policy_covrank_252d_base_v109_signal(ncfdiv, fcf):
    b = _rank(_f22_fcf_cover(ncfdiv, fcf), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps acceleration as level (second difference of dps over quarters)
def f22dp_f22_dividend_payout_policy_dpsaccel_252d_base_v110_signal(dps):
    d = dps - dps.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage shortfall streak: consecutive quarters of declining coverage (proxy)
def f22dp_f22_dividend_payout_policy_covdeclines_252d_base_v111_signal(ncfdiv, fcf):
    cov = _f22_fcf_cover(ncfdiv, fcf)
    decl = (cov < cov.shift(21)).astype(float)
    b = decl.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income-funded vs cash-funded payout wedge z-score
def f22dp_f22_dividend_payout_policy_fundwedge_252d_base_v112_signal(ncfdiv, netinc, fcf):
    ni_pay = ncfdiv.abs() / netinc.replace(0, np.nan)
    fcf_pay = ncfdiv.abs() / fcf.replace(0, np.nan)
    b = _z(ni_pay - fcf_pay, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield relative to payout-implied yield (mispricing of income vs policy)
def f22dp_f22_dividend_payout_policy_yldmis_126d_base_v113_signal(divyield, payoutratio):
    implied = _z(_f22_payout(payoutratio), 252)
    actual = _z(_f22_yield(divyield), 252)
    b = (actual - implied).rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend safety composite: coverage z plus buffer z minus payout z
def f22dp_f22_dividend_payout_policy_safecomp_252d_base_v114_signal(ncfdiv, fcf, payoutratio):
    cz = _z(_f22_fcf_cover(ncfdiv, fcf), 252)
    bz = _z(_f22_buffer(fcf, ncfdiv), 252)
    pz = _z(_f22_payout(payoutratio), 252)
    b = 0.5 * cz + 0.5 * bz - pz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage downside frequency: fraction of year coverage below 1.0 in continuous form
def f22dp_f22_dividend_payout_policy_covbelow_252d_base_v115_signal(ncfdiv, fcf):
    cov = _f22_fcf_cover(ncfdiv, fcf)
    shortfall = (1.0 - cov).clip(lower=0.0)
    b = shortfall.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps level normalized by yield (price-implied dividend base)
def f22dp_f22_dividend_payout_policy_dpsperyld_252d_base_v116_signal(dps, divyield):
    raw = dps / _f22_yield(divyield).replace(0, np.nan)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout-to-coverage product (aggression x risk), z-scored
def f22dp_f22_dividend_payout_policy_aggrisk_252d_base_v117_signal(payoutratio, ncfdiv, fcf):
    inv_cov = 1.0 / _f22_fcf_cover(ncfdiv, fcf).clip(lower=0.1)
    raw = _f22_payout(payoutratio) * inv_cov
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage trend rank: percentile of coverage slope (improving-coverage names)
def f22dp_f22_dividend_payout_policy_covtrendrank_504d_base_v118_signal(ncfdiv, fcf):
    sl = _slope(_f22_fcf_cover(ncfdiv, fcf), 126)
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield trend rank: percentile of yield slope (rising-income names)
def f22dp_f22_dividend_payout_policy_yldtrendrank_504d_base_v119_signal(divyield):
    sl = _slope(_f22_yield(divyield), 126)
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buffer-to-dividend ratio (years of dividend covered by surplus), compressed
def f22dp_f22_dividend_payout_policy_bufyears_126d_base_v120_signal(fcf, ncfdiv):
    raw = _f22_buffer(fcf, ncfdiv) / ncfdiv.abs().replace(0, np.nan)
    b = np.tanh(raw).rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend per share vs net income per dividend dollar interaction
def f22dp_f22_dividend_payout_policy_dpsnicross_252d_base_v121_signal(dps, ncfdiv, netinc):
    nicov = netinc / ncfdiv.abs().replace(0, np.nan)
    raw = _z(dps, 252) * np.tanh(nicov / 5.0)
    b = raw.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout dispersion trend (is policy becoming more or less stable)
def f22dp_f22_dividend_payout_policy_paydisptrend_252d_base_v122_signal(payoutratio):
    disp = _std(_f22_payout(payoutratio), 63)
    b = disp - disp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield dispersion trend
def f22dp_f22_dividend_payout_policy_ylddisptrend_252d_base_v123_signal(divyield):
    disp = _std(_f22_yield(divyield), 63)
    b = disp - disp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage dispersion trend
def f22dp_f22_dividend_payout_policy_covdisptrend_252d_base_v124_signal(ncfdiv, fcf):
    disp = _std(_f22_fcf_cover(ncfdiv, fcf), 63)
    b = disp - disp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income to dividend coverage floor over a year (worst earnings cushion)
def f22dp_f22_dividend_payout_policy_nicovfloor_252d_base_v125_signal(ncfdiv, netinc):
    raw = netinc / ncfdiv.abs().replace(0, np.nan)
    floor = raw.rolling(252, min_periods=126).min()
    b = np.tanh(floor / 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield curvature: fast-EMA vs slow-EMA ratio (income trend convexity, bounded)
def f22dp_f22_dividend_payout_policy_yldrecency_126d_base_v126_signal(divyield):
    y = _f22_yield(divyield)
    fast = y.ewm(span=21, min_periods=10).mean()
    slow = y.ewm(span=126, min_periods=42).mean()
    b = np.tanh(10.0 * (fast / slow.replace(0, np.nan) - 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout exponential-weighted level minus simple level
def f22dp_f22_dividend_payout_policy_payrecency_126d_base_v127_signal(payoutratio):
    p = _f22_payout(payoutratio)
    b = p.ewm(span=21, min_periods=10).mean() - _mean(p, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend sustainability hit-rate weighted by depth (covered AND deep)
def f22dp_f22_dividend_payout_policy_sustdepth_504d_base_v128_signal(fcf, ncfdiv):
    s = _f22_sustain(fcf, ncfdiv)
    pos_depth = s.clip(lower=0.0)
    b = pos_depth.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend stress depth: negative buffer magnitude averaged (chronic shortfall)
def f22dp_f22_dividend_payout_policy_stressdepth_504d_base_v129_signal(fcf, ncfdiv):
    s = _f22_sustain(fcf, ncfdiv)
    neg_depth = (-s).clip(lower=0.0)
    b = neg_depth.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage x yield interaction rank (quality-income composite percentile)
def f22dp_f22_dividend_payout_policy_qualincrank_504d_base_v130_signal(divyield, ncfdiv, fcf):
    raw = _f22_yield(divyield) * np.log(_f22_fcf_cover(ncfdiv, fcf).clip(lower=0.1))
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps growth minus payout growth (organic vs policy-driven dividend)
def f22dp_f22_dividend_payout_policy_organicdiv_252d_base_v131_signal(dps, payoutratio):
    dg = np.log(dps.clip(lower=1e-6) / dps.shift(252).clip(lower=1e-6))
    pg = np.log(_f22_payout(payoutratio).clip(lower=1e-6) / _f22_payout(payoutratio).shift(252).clip(lower=1e-6))
    b = dg - pg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income growth minus dividend growth (earnings-led vs dividend-led)
def f22dp_f22_dividend_payout_policy_earnled_252d_base_v132_signal(netinc, ncfdiv):
    ng = netinc / netinc.shift(252).replace(0, np.nan) - 1.0
    dg = ncfdiv.abs() / ncfdiv.abs().shift(252).replace(0, np.nan) - 1.0
    b = (ng - dg).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcf growth minus dividend growth (cash-led sustainability)
def f22dp_f22_dividend_payout_policy_cashled_252d_base_v133_signal(fcf, ncfdiv):
    fg = fcf / fcf.shift(252).replace(0, np.nan) - 1.0
    dg = ncfdiv.abs() / ncfdiv.abs().shift(252).replace(0, np.nan) - 1.0
    b = (fg - dg).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio level capped, smoothed (stable payout regime indicator)
def f22dp_f22_dividend_payout_policy_paystable_252d_base_v134_signal(payoutratio):
    p = _f22_payout(payoutratio).clip(0.0, 2.0)
    sm = p.rolling(252, min_periods=126).mean()
    b = (p - sm).abs().rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield z-score interaction with coverage z-score (high-yield-well-covered)
def f22dp_f22_dividend_payout_policy_hyqual_252d_base_v135_signal(divyield, ncfdiv, fcf):
    yz = _z(_f22_yield(divyield), 252)
    cz = _z(_f22_fcf_cover(ncfdiv, fcf), 252)
    b = yz * cz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend per share momentum scaled by yield level
def f22dp_f22_dividend_payout_policy_dpsmomyld_252d_base_v136_signal(dps, divyield):
    mom = dps / dps.shift(126).replace(0, np.nan) - 1.0
    b = mom * _f22_yield(divyield)
    b = b.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage improvement vs payout increase (safety vs aggression race)
def f22dp_f22_dividend_payout_policy_safetyrace_252d_base_v137_signal(ncfdiv, fcf, payoutratio):
    dcov = _f22_fcf_cover(ncfdiv, fcf) - _f22_fcf_cover(ncfdiv, fcf).shift(252)
    dpay = _f22_payout(payoutratio) - _f22_payout(payoutratio).shift(252)
    b = np.tanh(dcov) - np.tanh(5.0 * dpay)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income share paid out, exponential-weighted, vol-adjusted
def f22dp_f22_dividend_payout_policy_niwt_252d_base_v138_signal(ncfdiv, netinc):
    raw = _f22_div_to_netinc(ncfdiv, netinc)
    ew = raw.ewm(span=63, min_periods=21).mean()
    b = ew / (1.0 + _std(raw, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield Sharpe over a shorter window (income reward per uncertainty, 126d)
def f22dp_f22_dividend_payout_policy_yldsharpe_126d_base_v139_signal(divyield):
    y = _f22_yield(divyield)
    b = _mean(y, 126) / _std(y, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage Sharpe (coverage mean over coverage std, robustness of cushion)
def f22dp_f22_dividend_payout_policy_covsharpe_252d_base_v140_signal(ncfdiv, fcf):
    cov = _f22_fcf_cover(ncfdiv, fcf)
    b = _mean(cov, 252) / _std(cov, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend coverage range position (where coverage sits in its 252d range)
def f22dp_f22_dividend_payout_policy_covrngpos_252d_base_v141_signal(ncfdiv, fcf):
    cov = _f22_fcf_cover(ncfdiv, fcf)
    hi = cov.rolling(252, min_periods=126).max()
    lo = cov.rolling(252, min_periods=126).min()
    b = (cov - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout range position (where payout sits in its 252d range)
def f22dp_f22_dividend_payout_policy_payrngpos_252d_base_v142_signal(payoutratio):
    p = _f22_payout(payoutratio)
    hi = p.rolling(252, min_periods=126).max()
    lo = p.rolling(252, min_periods=126).min()
    b = (p - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield range position (where yield sits in its 252d range)
def f22dp_f22_dividend_payout_policy_yldrngpos_252d_base_v143_signal(divyield):
    y = _f22_yield(divyield)
    hi = y.rolling(252, min_periods=126).max()
    lo = y.rolling(252, min_periods=126).min()
    b = (y - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend per net income with fcf gating (cash-backed earnings payout)
def f22dp_f22_dividend_payout_policy_cashbacked_252d_base_v144_signal(ncfdiv, netinc, fcf):
    ni_pay = _f22_div_to_netinc(ncfdiv, netinc)
    gate = np.tanh(_f22_sustain(fcf, ncfdiv) * 3.0)
    raw = ni_pay * (1.0 + gate)
    b = raw.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage skew over a long window (asymmetry of cushion distribution)
def f22dp_f22_dividend_payout_policy_covlongskew_504d_base_v145_signal(ncfdiv, fcf):
    cov = _f22_fcf_cover(ncfdiv, fcf)
    med = cov.rolling(504, min_periods=252).median()
    b = (_mean(cov, 504) - med) / _std(cov, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend payout policy composite z (yield + payout + coverage blend)
def f22dp_f22_dividend_payout_policy_policyblend_252d_base_v146_signal(divyield, payoutratio, ncfdiv, fcf):
    yz = _z(_f22_yield(divyield), 252)
    pz = _z(_f22_payout(payoutratio), 252)
    cz = _z(_f22_fcf_cover(ncfdiv, fcf), 252)
    b = (yz + pz + cz) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps yield product percentile rank (total income generosity percentile)
def f22dp_f22_dividend_payout_policy_genrank_504d_base_v147_signal(dps, divyield):
    raw = dps * _f22_yield(divyield)
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buffer slope normalized by net income (cushion-build rate vs earnings)
def f22dp_f22_dividend_payout_policy_cushrate_252d_base_v148_signal(fcf, ncfdiv, netinc):
    sl = _slope(_f22_buffer(fcf, ncfdiv), 252)
    b = sl / netinc.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield-coverage spread momentum (income-vs-safety wedge change)
def f22dp_f22_dividend_payout_policy_ycspread_252d_base_v149_signal(divyield, ncfdiv, fcf):
    yz = _z(_f22_yield(divyield), 252)
    cz = _z(_f22_fcf_cover(ncfdiv, fcf), 252)
    spread = yz - cz
    b = spread - spread.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# all-in dividend health: covered, growing dps, conservative payout (composite)
def f22dp_f22_dividend_payout_policy_divhealth_504d_base_v150_signal(dps, payoutratio, ncfdiv, fcf):
    cov = _rank(_f22_fcf_cover(ncfdiv, fcf), 504)
    grow = _rank(dps - dps.shift(63), 504)
    conserv = 0.5 - _rank(_f22_payout(payoutratio), 504)
    b = cov + grow + conserv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22dp_f22_dividend_payout_policy_yldmom_63d_base_v076_signal,
    f22dp_f22_dividend_payout_policy_yldslope_126d_base_v077_signal,
    f22dp_f22_dividend_payout_policy_yldaccel_126d_base_v078_signal,
    f22dp_f22_dividend_payout_policy_payslope_126d_base_v079_signal,
    f22dp_f22_dividend_payout_policy_covslope_252d_base_v080_signal,
    f22dp_f22_dividend_payout_policy_dpsgrowth_252d_base_v081_signal,
    f22dp_f22_dividend_payout_policy_yldpayspread_252d_base_v082_signal,
    f22dp_f22_dividend_payout_policy_covterm_252d_base_v083_signal,
    f22dp_f22_dividend_payout_policy_yldterm_252d_base_v084_signal,
    f22dp_f22_dividend_payout_policy_payterm_252d_base_v085_signal,
    f22dp_f22_dividend_payout_policy_covskew_252d_base_v086_signal,
    f22dp_f22_dividend_payout_policy_yldskew_252d_base_v087_signal,
    f22dp_f22_dividend_payout_policy_nicovslope_252d_base_v088_signal,
    f22dp_f22_dividend_payout_policy_dpspaymom_252d_base_v089_signal,
    f22dp_f22_dividend_payout_policy_relcov_504d_base_v090_signal,
    f22dp_f22_dividend_payout_policy_paycovcorr_252d_base_v091_signal,
    f22dp_f22_dividend_payout_policy_ylddpscorr_252d_base_v092_signal,
    f22dp_f22_dividend_payout_policy_dpscut_252d_base_v093_signal,
    f22dp_f22_dividend_payout_policy_dpsraise_252d_base_v094_signal,
    f22dp_f22_dividend_payout_policy_uncovpay_126d_base_v095_signal,
    f22dp_f22_dividend_payout_policy_yldsust_252d_base_v096_signal,
    f22dp_f22_dividend_payout_policy_payconvmom_252d_base_v097_signal,
    f22dp_f22_dividend_payout_policy_nicovrank_504d_base_v098_signal,
    f22dp_f22_dividend_payout_policy_bufabsz_252d_base_v099_signal,
    f22dp_f22_dividend_payout_policy_covregime_252d_base_v100_signal,
    f22dp_f22_dividend_payout_policy_yldmrgap_252d_base_v101_signal,
    f22dp_f22_dividend_payout_policy_paymrgap_252d_base_v102_signal,
    f22dp_f22_dividend_payout_policy_covvov_252d_base_v103_signal,
    f22dp_f22_dividend_payout_policy_dpsgrowstab_504d_base_v104_signal,
    f22dp_f22_dividend_payout_policy_fcffunded_252d_base_v105_signal,
    f22dp_f22_dividend_payout_policy_nibackslope_252d_base_v106_signal,
    f22dp_f22_dividend_payout_policy_yldrank_252d_base_v107_signal,
    f22dp_f22_dividend_payout_policy_payrank_252d_base_v108_signal,
    f22dp_f22_dividend_payout_policy_covrank_252d_base_v109_signal,
    f22dp_f22_dividend_payout_policy_dpsaccel_252d_base_v110_signal,
    f22dp_f22_dividend_payout_policy_covdeclines_252d_base_v111_signal,
    f22dp_f22_dividend_payout_policy_fundwedge_252d_base_v112_signal,
    f22dp_f22_dividend_payout_policy_yldmis_126d_base_v113_signal,
    f22dp_f22_dividend_payout_policy_safecomp_252d_base_v114_signal,
    f22dp_f22_dividend_payout_policy_covbelow_252d_base_v115_signal,
    f22dp_f22_dividend_payout_policy_dpsperyld_252d_base_v116_signal,
    f22dp_f22_dividend_payout_policy_aggrisk_252d_base_v117_signal,
    f22dp_f22_dividend_payout_policy_covtrendrank_504d_base_v118_signal,
    f22dp_f22_dividend_payout_policy_yldtrendrank_504d_base_v119_signal,
    f22dp_f22_dividend_payout_policy_bufyears_126d_base_v120_signal,
    f22dp_f22_dividend_payout_policy_dpsnicross_252d_base_v121_signal,
    f22dp_f22_dividend_payout_policy_paydisptrend_252d_base_v122_signal,
    f22dp_f22_dividend_payout_policy_ylddisptrend_252d_base_v123_signal,
    f22dp_f22_dividend_payout_policy_covdisptrend_252d_base_v124_signal,
    f22dp_f22_dividend_payout_policy_nicovfloor_252d_base_v125_signal,
    f22dp_f22_dividend_payout_policy_yldrecency_126d_base_v126_signal,
    f22dp_f22_dividend_payout_policy_payrecency_126d_base_v127_signal,
    f22dp_f22_dividend_payout_policy_sustdepth_504d_base_v128_signal,
    f22dp_f22_dividend_payout_policy_stressdepth_504d_base_v129_signal,
    f22dp_f22_dividend_payout_policy_qualincrank_504d_base_v130_signal,
    f22dp_f22_dividend_payout_policy_organicdiv_252d_base_v131_signal,
    f22dp_f22_dividend_payout_policy_earnled_252d_base_v132_signal,
    f22dp_f22_dividend_payout_policy_cashled_252d_base_v133_signal,
    f22dp_f22_dividend_payout_policy_paystable_252d_base_v134_signal,
    f22dp_f22_dividend_payout_policy_hyqual_252d_base_v135_signal,
    f22dp_f22_dividend_payout_policy_dpsmomyld_252d_base_v136_signal,
    f22dp_f22_dividend_payout_policy_safetyrace_252d_base_v137_signal,
    f22dp_f22_dividend_payout_policy_niwt_252d_base_v138_signal,
    f22dp_f22_dividend_payout_policy_yldsharpe_126d_base_v139_signal,
    f22dp_f22_dividend_payout_policy_covsharpe_252d_base_v140_signal,
    f22dp_f22_dividend_payout_policy_covrngpos_252d_base_v141_signal,
    f22dp_f22_dividend_payout_policy_payrngpos_252d_base_v142_signal,
    f22dp_f22_dividend_payout_policy_yldrngpos_252d_base_v143_signal,
    f22dp_f22_dividend_payout_policy_cashbacked_252d_base_v144_signal,
    f22dp_f22_dividend_payout_policy_covlongskew_504d_base_v145_signal,
    f22dp_f22_dividend_payout_policy_policyblend_252d_base_v146_signal,
    f22dp_f22_dividend_payout_policy_genrank_504d_base_v147_signal,
    f22dp_f22_dividend_payout_policy_cushrate_252d_base_v148_signal,
    f22dp_f22_dividend_payout_policy_ycspread_252d_base_v149_signal,
    f22dp_f22_dividend_payout_policy_divhealth_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_DIVIDEND_PAYOUT_POLICY_REGISTRY_076_150 = REGISTRY


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

    dps = _fund(101, base=1.5, drift=0.01, vol=0.04).rename("dps")
    divyield = _fund(102, base=0.03, drift=0.005, vol=0.05).rename("divyield")
    payoutratio = _fund(103, base=0.95, drift=0.004, vol=0.14).rename("payoutratio")
    ncfdiv = _fund(104, base=4.5e8, drift=0.015, vol=0.12).rename("ncfdiv")
    netinc = _fund(105, base=5e8, drift=0.02, vol=0.10, allow_neg=True).rename("netinc")
    fcf = _fund(106, base=5e8, drift=0.02, vol=0.13, allow_neg=True).rename("fcf")

    cols = {"dps": dps, "divyield": divyield, "payoutratio": payoutratio,
            "ncfdiv": ncfdiv, "netinc": netinc, "fcf": fcf}

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

    print("OK f22_dividend_payout_policy_base_076_150_claude: %d features pass" % n_features)
