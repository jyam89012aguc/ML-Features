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
    # dividend yield level (already a small positive ratio)
    return divyield


def _f22_payout(payoutratio):
    # payout ratio level (dividends / earnings)
    return payoutratio


def _f22_fcf_cover(ncfdiv, fcf):
    # FCF dividend coverage: how many times FCF covers cash dividends paid
    return fcf / ncfdiv.abs().replace(0, np.nan)


def _f22_div_to_netinc(ncfdiv, netinc):
    # cash dividends as a share of net income (cash payout ratio)
    return ncfdiv.abs() / netinc.replace(0, np.nan)


def _f22_sustain(fcf, ncfdiv):
    # dividend sustainability buffer: FCF left after dividends, scaled by |FCF|
    return (fcf - ncfdiv.abs()) / fcf.abs().replace(0, np.nan)


def _f22_buffer(fcf, ncfdiv):
    # absolute retained cash after paying the dividend
    return fcf - ncfdiv.abs()


# ============================================================
# dividend yield level (raw)
def f22dp_f22_dividend_payout_policy_dyld_21d_base_v001_signal(divyield):
    b = _f22_yield(divyield).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield z-scored vs its own 252d history (rich/cheap yield)
def f22dp_f22_dividend_payout_policy_dyldz_252d_base_v002_signal(divyield):
    b = _z(_f22_yield(divyield), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield percentile rank vs its own 504d history
def f22dp_f22_dividend_payout_policy_dyldrank_504d_base_v003_signal(divyield):
    b = _rank(_f22_yield(divyield), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio level (smoothed)
def f22dp_f22_dividend_payout_policy_payout_63d_base_v004_signal(payoutratio):
    b = _f22_payout(payoutratio).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio z-scored vs its own 252d history (distention of payout)
def f22dp_f22_dividend_payout_policy_payoutz_252d_base_v005_signal(payoutratio):
    b = _z(_f22_payout(payoutratio), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio percentile rank vs its own 504d history
def f22dp_f22_dividend_payout_policy_payoutrank_504d_base_v006_signal(payoutratio):
    b = _rank(_f22_payout(payoutratio), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF dividend coverage level (fcf / |ncfdiv|)
def f22dp_f22_dividend_payout_policy_fcfcov_63d_base_v007_signal(ncfdiv, fcf):
    b = _f22_fcf_cover(ncfdiv, fcf).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF coverage z-scored vs its own 252d history
def f22dp_f22_dividend_payout_policy_fcfcovz_252d_base_v008_signal(ncfdiv, fcf):
    b = _z(_f22_fcf_cover(ncfdiv, fcf), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log FCF coverage (compress the heavy tail of the coverage ratio)
def f22dp_f22_dividend_payout_policy_fcfcovlog_126d_base_v009_signal(ncfdiv, fcf):
    cov = _f22_fcf_cover(ncfdiv, fcf)
    b = np.log(cov.clip(lower=0.01)).rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash dividends / net income (cash payout ratio)
def f22dp_f22_dividend_payout_policy_divni_63d_base_v010_signal(ncfdiv, netinc):
    b = _f22_div_to_netinc(ncfdiv, netinc).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# div/netinc z-scored vs own 252d history
def f22dp_f22_dividend_payout_policy_diniz_252d_base_v011_signal(ncfdiv, netinc):
    b = _z(_f22_div_to_netinc(ncfdiv, netinc), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# div/netinc percentile rank vs own 504d history
def f22dp_f22_dividend_payout_policy_dinirank_504d_base_v012_signal(ncfdiv, netinc):
    b = _rank(_f22_div_to_netinc(ncfdiv, netinc), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps level z-scored (dividend per share level vs own history)
def f22dp_f22_dividend_payout_policy_dpsz_252d_base_v013_signal(dps):
    b = _z(dps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps level percentile rank vs own 504d history
def f22dp_f22_dividend_payout_policy_dpsrank_504d_base_v014_signal(dps):
    b = _rank(dps, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustainability buffer momentum: change over a month in the (fcf-div)/|fcf| buffer
def f22dp_f22_dividend_payout_policy_sustain_63d_base_v015_signal(fcf, ncfdiv):
    s = _f22_sustain(fcf, ncfdiv).rolling(63, min_periods=21).mean()
    b = s - s.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustainability net of payout pressure: buffer z minus payout z (cushion after aggression)
def f22dp_f22_dividend_payout_policy_sustainz_252d_base_v016_signal(fcf, ncfdiv, payoutratio):
    sz = _z(_f22_sustain(fcf, ncfdiv), 252)
    pz = _z(_f22_payout(payoutratio), 252)
    b = sz + pz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustainability buffer trend rank: percentile of the buffer's quarter-over-quarter change
def f22dp_f22_dividend_payout_policy_sustrank_504d_base_v017_signal(fcf, ncfdiv):
    s = _f22_sustain(fcf, ncfdiv)
    chg = s - s.shift(63)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retained-cash buffer per net income, z-scored momentum (cushion-build vs earnings)
def f22dp_f22_dividend_payout_policy_bufni_63d_base_v018_signal(fcf, ncfdiv, netinc):
    raw = _f22_buffer(fcf, ncfdiv) / netinc.abs().replace(0, np.nan)
    z = _z(raw, 252)
    b = z - z.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retention strength scaled by coverage: (1-payout) x FCF coverage (funded retention)
def f22dp_f22_dividend_payout_policy_retain_63d_base_v019_signal(payoutratio, ncfdiv, fcf):
    retain = (1.0 - _f22_payout(payoutratio)).clip(lower=-1.0)
    cov = _f22_fcf_cover(ncfdiv, fcf).clip(lower=0.0)
    b = (retain * np.tanh(cov)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield x payout interaction (income-distribution intensity)
def f22dp_f22_dividend_payout_policy_yldpay_63d_base_v020_signal(divyield, payoutratio):
    raw = _f22_yield(divyield) * _f22_payout(payoutratio)
    b = raw.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield-to-payout ratio (yield achieved per unit of payout aggressiveness)
def f22dp_f22_dividend_payout_policy_yldperpay_126d_base_v021_signal(divyield, payoutratio):
    raw = _f22_yield(divyield) / _f22_payout(payoutratio).replace(0, np.nan)
    b = raw.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage minus payout (cash backing vs earnings backing disagreement)
def f22dp_f22_dividend_payout_policy_covminuspay_252d_base_v022_signal(ncfdiv, fcf, payoutratio):
    cov = _z(_f22_fcf_cover(ncfdiv, fcf), 252)
    pay = _z(_f22_payout(payoutratio), 252)
    b = cov - pay
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage-gap momentum: change over a quarter in the FCF-over-dividend surplus
def f22dp_f22_dividend_payout_policy_covgap_126d_base_v023_signal(ncfdiv, fcf):
    raw = (fcf - ncfdiv.abs()) / ncfdiv.abs().replace(0, np.nan)
    sm = raw.rolling(126, min_periods=42).mean()
    b = sm - sm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps level relative to its own 252d mean (dps stretch)
def f22dp_f22_dividend_payout_policy_dpsstretch_252d_base_v024_signal(dps):
    m = _mean(dps, 252)
    b = dps / m.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield dispersion (volatility of the dividend yield over a year)
def f22dp_f22_dividend_payout_policy_ylddisp_252d_base_v025_signal(divyield):
    b = _std(_f22_yield(divyield), 252) / _mean(_f22_yield(divyield), 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio dispersion (policy stability; low = steady payout)
def f22dp_f22_dividend_payout_policy_paydisp_252d_base_v026_signal(payoutratio):
    b = _std(_f22_payout(payoutratio), 252) / _mean(_f22_payout(payoutratio), 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage dispersion (how variable FCF dividend coverage has been)
def f22dp_f22_dividend_payout_policy_covdisp_252d_base_v027_signal(ncfdiv, fcf):
    cov = _f22_fcf_cover(ncfdiv, fcf)
    b = _std(cov, 252) / _mean(cov, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income cash payout vs accrual payout ratio spread
def f22dp_f22_dividend_payout_policy_cashaccr_252d_base_v028_signal(ncfdiv, netinc, payoutratio):
    cash = _f22_div_to_netinc(ncfdiv, netinc)
    b = _z(cash, 252) - _z(_f22_payout(payoutratio), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-adjusted yield: yield z-score minus coverage z-score (cheap-but-risky tilt)
def f22dp_f22_dividend_payout_policy_qualyld_126d_base_v029_signal(divyield, ncfdiv, fcf):
    yz = _z(_f22_yield(divyield), 126)
    cz = _z(_f22_fcf_cover(ncfdiv, fcf), 126)
    b = yz - 0.5 * cz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage-conditioned payout stress: payout level deflated by tanh(coverage cushion)
def f22dp_f22_dividend_payout_policy_sustsignmag_252d_base_v030_signal(fcf, ncfdiv, payoutratio):
    cov = _f22_fcf_cover(ncfdiv, fcf).clip(lower=0.0)
    stress = _f22_payout(payoutratio) / (0.5 + np.tanh(cov))
    b = stress.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF shortfall magnitude: average dollar gap when FCF fails to cover the dividend
def f22dp_f22_dividend_payout_policy_uncoverfreq_252d_base_v031_signal(ncfdiv, fcf, netinc):
    shortfall = (ncfdiv.abs() - fcf).clip(lower=0.0) / netinc.abs().replace(0, np.nan)
    b = shortfall.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed magnitude of over-distribution: payout excess above 1.0 (continuous)
def f22dp_f22_dividend_payout_policy_overpaymag_252d_base_v032_signal(payoutratio):
    excess = (_f22_payout(payoutratio) - 1.0).clip(lower=0.0)
    b = excess.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps relative to sqrt net income (per-share generosity normalized), z-scored
def f22dp_f22_dividend_payout_policy_dpsni_126d_base_v033_signal(dps, netinc):
    raw = dps / (netinc.abs().replace(0, np.nan) ** 0.5)
    b = _z(raw, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield minus its own slow EMA (yield displacement)
def f22dp_f22_dividend_payout_policy_ylddisplace_base_v034_signal(divyield):
    y = _f22_yield(divyield)
    b = y - y.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout minus its own slow EMA (payout displacement)
def f22dp_f22_dividend_payout_policy_paydisplace_base_v035_signal(payoutratio):
    p = _f22_payout(payoutratio)
    b = p - p.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage minus its own slow EMA (coverage displacement)
def f22dp_f22_dividend_payout_policy_covdisplace_base_v036_signal(ncfdiv, fcf):
    c = _f22_fcf_cover(ncfdiv, fcf)
    b = c - c.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout aggressiveness acceleration: change in |ncfdiv|/|fcf| rank vs a year ago
def f22dp_f22_dividend_payout_policy_payaggr_504d_base_v037_signal(ncfdiv, fcf):
    raw = ncfdiv.abs() / fcf.abs().replace(0, np.nan)
    r = _rank(raw, 504)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended distribution score: avg rank of yield and payout (income posture)
def f22dp_f22_dividend_payout_policy_distscore_504d_base_v038_signal(divyield, payoutratio):
    b = 0.5 * _rank(_f22_yield(divyield), 504) + 0.5 * _rank(_f22_payout(payoutratio), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended safety score: coverage rank gated by low payout (well-covered AND conservative)
def f22dp_f22_dividend_payout_policy_safescore_504d_base_v039_signal(ncfdiv, fcf, payoutratio):
    cov = _rank(_f22_fcf_cover(ncfdiv, fcf), 504) + 0.5
    low_pay = 0.5 - _rank(_f22_payout(payoutratio), 504)
    b = cov * low_pay
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout acceleration: second difference of payout ratio (policy inflection-as-level)
def f22dp_f22_dividend_payout_policy_paytanh_126d_base_v040_signal(payoutratio):
    p = _f22_payout(payoutratio).rolling(21, min_periods=10).mean()
    b = (p - p.shift(63)) - (p.shift(63) - p.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# div/netinc minus div/fcf (earnings vs cashflow payout wedge)
def f22dp_f22_dividend_payout_policy_niwedge_252d_base_v041_signal(ncfdiv, netinc, fcf):
    a = ncfdiv.abs() / netinc.replace(0, np.nan)
    b2 = ncfdiv.abs() / fcf.replace(0, np.nan)
    b = (a - b2).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield robustness vs net-income volatility (income yield robustness)
def f22dp_f22_dividend_payout_policy_yldnivol_252d_base_v042_signal(divyield, netinc):
    nivol = _std(netinc, 252) / _mean(netinc, 252).abs().replace(0, np.nan)
    raw = _f22_yield(divyield) / (1.0 + nivol)
    b = _z(raw, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcf coverage buffer relative to net income (deep cushion)
def f22dp_f22_dividend_payout_policy_deepcush_252d_base_v043_signal(fcf, ncfdiv, netinc):
    raw = (fcf - ncfdiv.abs()) / netinc.abs().replace(0, np.nan)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-dps anchor: dps vs dps a year ago (dividend growth memory)
def f22dp_f22_dividend_payout_policy_dpsanchor_252d_base_v044_signal(dps):
    b = np.log(dps.clip(lower=1e-6) / dps.shift(252).clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio vs payout a year ago (policy drift)
def f22dp_f22_dividend_payout_policy_paydrift_252d_base_v045_signal(payoutratio):
    p = _f22_payout(payoutratio)
    b = p - p.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage vs coverage a year ago (coverage drift)
def f22dp_f22_dividend_payout_policy_covdrift_252d_base_v046_signal(ncfdiv, fcf):
    c = _f22_fcf_cover(ncfdiv, fcf)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield vs yield a year ago (yield re-rating)
def f22dp_f22_dividend_payout_policy_yldrerate_252d_base_v047_signal(divyield):
    y = _f22_yield(divyield)
    b = np.log(y.clip(lower=1e-6) / y.shift(252).clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-drain momentum: change in |ncfdiv|/|netinc| over a quarter (rising payout burden)
def f22dp_f22_dividend_payout_policy_cashdrain_126d_base_v048_signal(ncfdiv, netinc):
    raw = (ncfdiv.abs() / netinc.abs().replace(0, np.nan)).ewm(span=63, min_periods=21).mean()
    b = raw - raw.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustainability hit-rate: fraction of last 2y with positive buffer
def f22dp_f22_dividend_payout_policy_sustainhit_504d_base_v049_signal(fcf, ncfdiv):
    pos = ((fcf - ncfdiv.abs()) > 0).astype(float)
    b = pos.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage-weighted yield rank (high yield only credited if well covered)
def f22dp_f22_dividend_payout_policy_covwtyld_504d_base_v050_signal(divyield, ncfdiv, fcf):
    yr = _rank(_f22_yield(divyield), 504)
    cr = _rank(_f22_fcf_cover(ncfdiv, fcf), 504)
    b = yr * (0.5 + cr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio convexity around 0.5 (stress when payout far from balanced)
def f22dp_f22_dividend_payout_policy_payconvex_252d_base_v051_signal(payoutratio):
    dev = _f22_payout(payoutratio) - 0.5
    conv = np.sign(dev) * dev ** 2
    b = conv.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage drawdown: current coverage vs its trailing-year peak (cushion erosion)
def f22dp_f22_dividend_payout_policy_covfloor_252d_base_v052_signal(ncfdiv, fcf):
    cov = _f22_fcf_cover(ncfdiv, fcf)
    peak = cov.rolling(252, min_periods=126).max()
    b = cov / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield ceiling: rolling max yield over a year vs current (peak income offering)
def f22dp_f22_dividend_payout_policy_yldceil_252d_base_v053_signal(divyield):
    y = _f22_yield(divyield)
    b = y.rolling(252, min_periods=126).max() / y.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps drawdown: current dps vs its trailing-year peak (dividend cut detection)
def f22dp_f22_dividend_payout_policy_dpsrngpos_252d_base_v054_signal(dps):
    peak = dps.rolling(252, min_periods=126).max()
    b = dps / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# danger score: high payout rank AND low coverage rank
def f22dp_f22_dividend_payout_policy_dangerscore_504d_base_v055_signal(payoutratio, ncfdiv, fcf):
    pay = _rank(_f22_payout(payoutratio), 504)
    inv_cov = -_rank(_f22_fcf_cover(ncfdiv, fcf), 504)
    b = pay + inv_cov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income payout dispersion: variability of cash payout ratio (policy volatility)
def f22dp_f22_dividend_payout_policy_nipayoutnorm_252d_base_v056_signal(ncfdiv, netinc):
    raw = _f22_div_to_netinc(ncfdiv, netinc)
    b = _std(raw, 252) / (1.0 + _mean(raw, 252).abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# structural surplus dispersion: variability of the buffer/fcf ratio (surplus reliability)
def f22dp_f22_dividend_payout_policy_structsurplus_252d_base_v057_signal(fcf, ncfdiv):
    raw = (fcf - ncfdiv.abs()) / fcf.abs().replace(0, np.nan)
    b = _std(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite tension: yield z + payout z - coverage z
def f22dp_f22_dividend_payout_policy_tension_252d_base_v058_signal(divyield, payoutratio, ncfdiv, fcf):
    yz = _z(_f22_yield(divyield), 252)
    pz = _z(_f22_payout(payoutratio), 252)
    cz = _z(_f22_fcf_cover(ncfdiv, fcf), 252)
    b = yz + pz - cz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-coverage percentile rank (covered-ness percentile)
def f22dp_f22_dividend_payout_policy_logcovrank_504d_base_v059_signal(ncfdiv, fcf):
    cov = np.log(_f22_fcf_cover(ncfdiv, fcf).clip(lower=0.01))
    b = _rank(cov, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# div/fcf payout momentum: quarter-over-quarter change in the cash-payout-of-FCF ratio
def f22dp_f22_dividend_payout_policy_divfcf_63d_base_v060_signal(ncfdiv, fcf):
    raw = (ncfdiv.abs() / fcf.abs().replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = raw - raw.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield spread vs its 504d median (cheap-income anomaly)
def f22dp_f22_dividend_payout_policy_yldmedspread_504d_base_v061_signal(divyield):
    y = _f22_yield(divyield)
    med = y.rolling(504, min_periods=126).median()
    b = (y - med) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout spread vs its 504d median (policy anomaly)
def f22dp_f22_dividend_payout_policy_paymedspread_504d_base_v062_signal(payoutratio):
    p = _f22_payout(payoutratio)
    med = p.rolling(504, min_periods=126).median()
    b = (p - med) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps x yield (total income intensity proxy), z-scored
def f22dp_f22_dividend_payout_policy_incomeintens_252d_base_v063_signal(dps, divyield):
    raw = dps * _f22_yield(divyield)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net income coverage of dividend: netinc / |ncfdiv| (earnings times-covered)
def f22dp_f22_dividend_payout_policy_nicover_126d_base_v064_signal(ncfdiv, netinc):
    raw = netinc / ncfdiv.abs().replace(0, np.nan)
    b = np.tanh(raw / 5.0).rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage downside semideviation (asymmetric coverage risk)
def f22dp_f22_dividend_payout_policy_covsemidev_252d_base_v065_signal(ncfdiv, fcf):
    cov = _f22_fcf_cover(ncfdiv, fcf)
    m = _mean(cov, 252)
    downs = (cov - m).clip(upper=0)
    b = (downs ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustainability buffer trend strength (slope of buffer over a quarter)
def f22dp_f22_dividend_payout_policy_sustslope_63d_base_v066_signal(fcf, ncfdiv):
    s = _f22_sustain(fcf, ncfdiv)
    b = _slope(s, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps stability: inverse coefficient of variation of dps (steady-dividend)
def f22dp_f22_dividend_payout_policy_dpsstab_252d_base_v067_signal(dps):
    cv = _std(dps, 252) / _mean(dps, 252).replace(0, np.nan)
    b = 1.0 / (1.0 + cv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout-vs-coverage headroom: how far the cash payout sits below FCF capacity
def f22dp_f22_dividend_payout_policy_headroom_252d_base_v068_signal(ncfdiv, fcf, payoutratio):
    capacity = np.log(_f22_fcf_cover(ncfdiv, fcf).clip(lower=0.05))
    pay = _z(_f22_payout(payoutratio), 252)
    b = (capacity - pay).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield rank minus its own 1y-lagged rank (income re-rating momentum)
def f22dp_f22_dividend_payout_policy_yldrankmom_504d_base_v069_signal(divyield):
    r = _rank(_f22_yield(divyield), 504)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage rank minus 1y-lagged coverage rank (safety re-rating)
def f22dp_f22_dividend_payout_policy_covrankmom_504d_base_v070_signal(ncfdiv, fcf):
    r = _rank(_f22_fcf_cover(ncfdiv, fcf), 504)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-vs-accrual payout drift: change in (cash payout - accrual payout) over a year
def f22dp_f22_dividend_payout_policy_cashreturn_252d_base_v071_signal(ncfdiv, netinc, payoutratio):
    wedge = (ncfdiv.abs() / netinc.replace(0, np.nan)).clip(-2.0, 3.0) - _f22_payout(payoutratio)
    sm = wedge.rolling(63, min_periods=21).mean()
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buffer instability via downside swings: mean absolute negative buffer change
def f22dp_f22_dividend_payout_policy_sustinstab_252d_base_v072_signal(fcf, ncfdiv):
    s = _f22_sustain(fcf, ncfdiv)
    drops = (s - s.shift(21)).clip(upper=0.0).abs()
    b = drops.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share generosity: dps x payout normalized by netinc^0.25, z-scored
def f22dp_f22_dividend_payout_policy_generosity_252d_base_v073_signal(dps, payoutratio, netinc):
    raw = dps * _f22_payout(payoutratio) / (netinc.abs().replace(0, np.nan) ** 0.25)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield Sharpe-like: yield mean over yield std (reward per income uncertainty)
def f22dp_f22_dividend_payout_policy_yldsharpe_252d_base_v074_signal(divyield):
    y = _f22_yield(divyield)
    b = _mean(y, 252) / _std(y, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite payout posture: distribution rank plus sustainability rank
def f22dp_f22_dividend_payout_policy_posture_504d_base_v075_signal(divyield, payoutratio, ncfdiv, fcf):
    income = 0.5 * _rank(_f22_yield(divyield), 504) + 0.5 * _rank(_f22_payout(payoutratio), 504)
    safety = _rank(_f22_sustain(fcf, ncfdiv), 504)
    b = income + safety
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22dp_f22_dividend_payout_policy_dyld_21d_base_v001_signal,
    f22dp_f22_dividend_payout_policy_dyldz_252d_base_v002_signal,
    f22dp_f22_dividend_payout_policy_dyldrank_504d_base_v003_signal,
    f22dp_f22_dividend_payout_policy_payout_63d_base_v004_signal,
    f22dp_f22_dividend_payout_policy_payoutz_252d_base_v005_signal,
    f22dp_f22_dividend_payout_policy_payoutrank_504d_base_v006_signal,
    f22dp_f22_dividend_payout_policy_fcfcov_63d_base_v007_signal,
    f22dp_f22_dividend_payout_policy_fcfcovz_252d_base_v008_signal,
    f22dp_f22_dividend_payout_policy_fcfcovlog_126d_base_v009_signal,
    f22dp_f22_dividend_payout_policy_divni_63d_base_v010_signal,
    f22dp_f22_dividend_payout_policy_diniz_252d_base_v011_signal,
    f22dp_f22_dividend_payout_policy_dinirank_504d_base_v012_signal,
    f22dp_f22_dividend_payout_policy_dpsz_252d_base_v013_signal,
    f22dp_f22_dividend_payout_policy_dpsrank_504d_base_v014_signal,
    f22dp_f22_dividend_payout_policy_sustain_63d_base_v015_signal,
    f22dp_f22_dividend_payout_policy_sustainz_252d_base_v016_signal,
    f22dp_f22_dividend_payout_policy_sustrank_504d_base_v017_signal,
    f22dp_f22_dividend_payout_policy_bufni_63d_base_v018_signal,
    f22dp_f22_dividend_payout_policy_retain_63d_base_v019_signal,
    f22dp_f22_dividend_payout_policy_yldpay_63d_base_v020_signal,
    f22dp_f22_dividend_payout_policy_yldperpay_126d_base_v021_signal,
    f22dp_f22_dividend_payout_policy_covminuspay_252d_base_v022_signal,
    f22dp_f22_dividend_payout_policy_covgap_126d_base_v023_signal,
    f22dp_f22_dividend_payout_policy_dpsstretch_252d_base_v024_signal,
    f22dp_f22_dividend_payout_policy_ylddisp_252d_base_v025_signal,
    f22dp_f22_dividend_payout_policy_paydisp_252d_base_v026_signal,
    f22dp_f22_dividend_payout_policy_covdisp_252d_base_v027_signal,
    f22dp_f22_dividend_payout_policy_cashaccr_252d_base_v028_signal,
    f22dp_f22_dividend_payout_policy_qualyld_126d_base_v029_signal,
    f22dp_f22_dividend_payout_policy_sustsignmag_252d_base_v030_signal,
    f22dp_f22_dividend_payout_policy_uncoverfreq_252d_base_v031_signal,
    f22dp_f22_dividend_payout_policy_overpaymag_252d_base_v032_signal,
    f22dp_f22_dividend_payout_policy_dpsni_126d_base_v033_signal,
    f22dp_f22_dividend_payout_policy_ylddisplace_base_v034_signal,
    f22dp_f22_dividend_payout_policy_paydisplace_base_v035_signal,
    f22dp_f22_dividend_payout_policy_covdisplace_base_v036_signal,
    f22dp_f22_dividend_payout_policy_payaggr_504d_base_v037_signal,
    f22dp_f22_dividend_payout_policy_distscore_504d_base_v038_signal,
    f22dp_f22_dividend_payout_policy_safescore_504d_base_v039_signal,
    f22dp_f22_dividend_payout_policy_paytanh_126d_base_v040_signal,
    f22dp_f22_dividend_payout_policy_niwedge_252d_base_v041_signal,
    f22dp_f22_dividend_payout_policy_yldnivol_252d_base_v042_signal,
    f22dp_f22_dividend_payout_policy_deepcush_252d_base_v043_signal,
    f22dp_f22_dividend_payout_policy_dpsanchor_252d_base_v044_signal,
    f22dp_f22_dividend_payout_policy_paydrift_252d_base_v045_signal,
    f22dp_f22_dividend_payout_policy_covdrift_252d_base_v046_signal,
    f22dp_f22_dividend_payout_policy_yldrerate_252d_base_v047_signal,
    f22dp_f22_dividend_payout_policy_cashdrain_126d_base_v048_signal,
    f22dp_f22_dividend_payout_policy_sustainhit_504d_base_v049_signal,
    f22dp_f22_dividend_payout_policy_covwtyld_504d_base_v050_signal,
    f22dp_f22_dividend_payout_policy_payconvex_252d_base_v051_signal,
    f22dp_f22_dividend_payout_policy_covfloor_252d_base_v052_signal,
    f22dp_f22_dividend_payout_policy_yldceil_252d_base_v053_signal,
    f22dp_f22_dividend_payout_policy_dpsrngpos_252d_base_v054_signal,
    f22dp_f22_dividend_payout_policy_dangerscore_504d_base_v055_signal,
    f22dp_f22_dividend_payout_policy_nipayoutnorm_252d_base_v056_signal,
    f22dp_f22_dividend_payout_policy_structsurplus_252d_base_v057_signal,
    f22dp_f22_dividend_payout_policy_tension_252d_base_v058_signal,
    f22dp_f22_dividend_payout_policy_logcovrank_504d_base_v059_signal,
    f22dp_f22_dividend_payout_policy_divfcf_63d_base_v060_signal,
    f22dp_f22_dividend_payout_policy_yldmedspread_504d_base_v061_signal,
    f22dp_f22_dividend_payout_policy_paymedspread_504d_base_v062_signal,
    f22dp_f22_dividend_payout_policy_incomeintens_252d_base_v063_signal,
    f22dp_f22_dividend_payout_policy_nicover_126d_base_v064_signal,
    f22dp_f22_dividend_payout_policy_covsemidev_252d_base_v065_signal,
    f22dp_f22_dividend_payout_policy_sustslope_63d_base_v066_signal,
    f22dp_f22_dividend_payout_policy_dpsstab_252d_base_v067_signal,
    f22dp_f22_dividend_payout_policy_headroom_252d_base_v068_signal,
    f22dp_f22_dividend_payout_policy_yldrankmom_504d_base_v069_signal,
    f22dp_f22_dividend_payout_policy_covrankmom_504d_base_v070_signal,
    f22dp_f22_dividend_payout_policy_cashreturn_252d_base_v071_signal,
    f22dp_f22_dividend_payout_policy_sustinstab_252d_base_v072_signal,
    f22dp_f22_dividend_payout_policy_generosity_252d_base_v073_signal,
    f22dp_f22_dividend_payout_policy_yldsharpe_252d_base_v074_signal,
    f22dp_f22_dividend_payout_policy_posture_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_DIVIDEND_PAYOUT_POLICY_REGISTRY_001_075 = REGISTRY


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

    print("OK f22_dividend_payout_policy_base_001_075_claude: %d features pass" % n_features)
