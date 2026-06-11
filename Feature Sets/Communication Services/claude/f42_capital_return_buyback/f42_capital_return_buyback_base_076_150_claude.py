import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (capital return / buyback) =====
def _f42_buyback(ncfcommon):
    return (-ncfcommon).clip(lower=0)


def _f42_issuance(ncfcommon):
    return ncfcommon.clip(lower=0)


def _f42_buyback_yield(ncfcommon, marketcap):
    return _f42_buyback(ncfcommon) / marketcap.replace(0, np.nan)


def _f42_div_yield(ncfdiv, marketcap):
    return ncfdiv.abs() / marketcap.replace(0, np.nan)


def _f42_total_yield(ncfcommon, ncfdiv, marketcap):
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    return ret / marketcap.replace(0, np.nan)


def _f42_div_cover(ncfdiv, fcf):
    return fcf / ncfdiv.abs().replace(0, np.nan)


# ============================================================
# buyback yield smoothed over a year (multi-year repurchase base rate)
def f42rb_f42_capital_return_buyback_byyieldyr_base_v076_signal(ncfcommon, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = by.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback yield acceleration: half-year change of the quarterly buyback yield
def f42rb_f42_capital_return_buyback_byaccel2_base_v077_signal(ncfcommon, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap).rolling(63, min_periods=21).mean()
    b = by - by.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-yield curvature: quarter-over-quarter change of its own quarterly change
def f42rb_f42_capital_return_buyback_bycurv_base_v078_signal(ncfcommon, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    d = by - by.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# annual-buyback growth: this year's summed buyback dollars vs last year's (program scale-up)
def f42rb_f42_capital_return_buyback_bbcumyield_base_v079_signal(ncfcommon):
    bb = _f42_buyback(ncfcommon).rolling(252, min_periods=84).sum()
    b = bb / bb.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-intensity skew: signed-root of buyback yield minus its smooth norm (extremity)
def f42rb_f42_capital_return_buyback_byskew_base_v080_signal(ncfcommon, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    typ = by.rolling(252, min_periods=84).median()
    b = np.sqrt(by) - np.sqrt(typ.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yearly dividend yield z-scored vs 504d (multi-year income-yield regime, marketcap-detrended)
def f42rb_f42_capital_return_buyback_divyieldyr_base_v081_signal(ncfdiv, marketcap):
    dy = _f42_div_yield(ncfdiv, marketcap).rolling(252, min_periods=84).mean()
    b = _z(dy, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-yield acceleration: half-year change of quarterly dividend yield
def f42rb_f42_capital_return_buyback_dyaccel_base_v082_signal(ncfdiv, marketcap):
    dy = _f42_div_yield(ncfdiv, marketcap).rolling(63, min_periods=21).mean()
    b = dy - dy.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-yield curvature: change in the change of dividend yield (income inflection)
def f42rb_f42_capital_return_buyback_dycurv_base_v083_signal(ncfdiv, marketcap):
    dy = _f42_div_yield(ncfdiv, marketcap)
    d = dy - dy.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend dollars cumulative over a year vs marketcap, z-scored (annual income regime)
def f42rb_f42_capital_return_buyback_divcumyield_base_v084_signal(ncfdiv, marketcap):
    dv = ncfdiv.abs().rolling(252, min_periods=84).sum()
    cy = dv / (marketcap * 4.0).replace(0, np.nan)
    b = _z(cy, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-yield dispersion over a year (income variability)
def f42rb_f42_capital_return_buyback_dydisp_base_v085_signal(ncfdiv, marketcap):
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = _std(dy, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-yield yearly base rate vs its prior-year level (multi-year return expansion)
def f42rb_f42_capital_return_buyback_tyyrz_base_v086_signal(ncfcommon, ncfdiv, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap).rolling(252, min_periods=84).mean()
    b = ty / ty.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-yield acceleration over a quarter (capital-return inflection)
def f42rb_f42_capital_return_buyback_tyaccel_base_v087_signal(ncfcommon, ncfdiv, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    d = ty - ty.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative total payout over a year vs marketcap (annual shareholder return)
def f42rb_f42_capital_return_buyback_tycumyield_base_v088_signal(ncfcommon, ncfdiv, marketcap):
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).rolling(252, min_periods=84).sum()
    b = ret / (marketcap * 4.0).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-yield dispersion over a year (variability of capital return)
def f42rb_f42_capital_return_buyback_tydisp_base_v089_signal(ncfcommon, ncfdiv, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = _std(ty, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-mix smoothed over a half-year (steady buyback-vs-dividend posture)
def f42rb_f42_capital_return_buyback_mixsm_base_v090_signal(ncfcommon, ncfdiv):
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    mix = (bb - dv) / (bb + dv).replace(0, np.nan)
    b = mix.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-mix dispersion (how unstable the buyback/dividend split is over a year)
def f42rb_f42_capital_return_buyback_mixdisp_base_v091_signal(ncfcommon, ncfdiv):
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    mix = (bb - dv) / (bb + dv).replace(0, np.nan)
    b = _std(mix, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-mix rank vs 504d history (relative repurchase tilt percentile)
def f42rb_f42_capital_return_buyback_mixrank_base_v092_signal(ncfcommon, ncfdiv):
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    mix = (bb - dv) / (bb + dv).replace(0, np.nan)
    b = _rank(mix, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend coverage minimum over a year (worst-case sustainability cushion)
def f42rb_f42_capital_return_buyback_covmin_base_v093_signal(ncfdiv, fcf):
    cov = _f42_div_cover(ncfdiv, fcf)
    b = cov.rolling(252, min_periods=84).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend coverage dispersion (volatility of the coverage ratio over a year)
def f42rb_f42_capital_return_buyback_covdisp_base_v094_signal(ncfdiv, fcf):
    cov = _f42_div_cover(ncfdiv, fcf)
    b = _std(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend coverage rank vs 504d history (relative safety percentile)
def f42rb_f42_capital_return_buyback_covrank_base_v095_signal(ncfdiv, fcf):
    cov = _f42_div_cover(ncfdiv, fcf)
    b = _rank(cov, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage trend acceleration: change in the half-year coverage slope (improving safety)
def f42rb_f42_capital_return_buyback_covaccel_base_v096_signal(ncfdiv, fcf):
    cov = _f42_div_cover(ncfdiv, fcf)
    sl = _slope(cov, 126)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-return coverage by FCF, half-year momentum (improving/eroding self-funding)
def f42rb_f42_capital_return_buyback_retcovmin_base_v097_signal(ncfcommon, ncfdiv, fcf):
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    cov = (fcf / ret).rolling(63, min_periods=21).mean()
    b = cov - cov.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-payout ratio momentum: change in the distribution rate over a year (rising/falling payout)
def f42rb_f42_capital_return_buyback_fcfpayoutsm_base_v098_signal(ncfcommon, ncfdiv, fcf):
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    pr = (ret / fcf.clip(lower=0).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = pr - pr.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-payout ratio rank vs 504d history (relative distribution-rate percentile)
def f42rb_f42_capital_return_buyback_fcfpayoutrank_base_v099_signal(ncfcommon, ncfdiv, fcf):
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    pr = ret / fcf.clip(lower=0).replace(0, np.nan)
    b = _rank(pr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-out-of-FCF ratio, smoothed (steady repurchase-funding share)
def f42rb_f42_capital_return_buyback_bbfcfsm_base_v100_signal(ncfcommon, fcf):
    r = _f42_buyback(ncfcommon) / fcf.clip(lower=0).replace(0, np.nan)
    b = r.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-out-of-OCF ratio, yearly momentum (rising repurchase claim on operating cash)
def f42rb_f42_capital_return_buyback_bbocfz2_base_v101_signal(ncfcommon, ncfo):
    r = (_f42_buyback(ncfcommon) / ncfo.clip(lower=0).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-out-of-OCF, smoothed over a year (durable OCF dividend load)
def f42rb_f42_capital_return_buyback_divocfsm_base_v102_signal(ncfdiv, ncfo):
    r = ncfdiv.abs() / ncfo.clip(lower=0).replace(0, np.nan)
    b = r.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-payout-out-of-OCF, ranked (relative OCF burden percentile)
def f42rb_f42_capital_return_buyback_retocfrank_base_v103_signal(ncfcommon, ncfdiv, ncfo):
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    r = ret / ncfo.clip(lower=0).replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps acceleration: change in dps growth rate (dividend-hike inflection)
def f42rb_f42_capital_return_buyback_dpsaccel_base_v104_signal(dps):
    g = dps / dps.shift(126).replace(0, np.nan) - 1.0
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps smoothed slope over a year (steady dividend-growth trajectory)
def f42rb_f42_capital_return_buyback_dpsslope_base_v105_signal(dps):
    sm = dps.rolling(63, min_periods=21).mean()
    b = _slope(sm, 252) / sm.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps rank vs 504d history (relative dividend-level percentile)
def f42rb_f42_capital_return_buyback_dpsrank_base_v106_signal(dps):
    b = _rank(dps, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps dispersion (variability of the per-share dividend over a year)
def f42rb_f42_capital_return_buyback_dpsdisp_base_v107_signal(dps):
    b = _std(dps, 252) / _mean(dps, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps stability: average absolute month-over-month dps change over a year (inverse of hike activity)
def f42rb_f42_capital_return_buyback_dpsstag_base_v108_signal(dps):
    chg = (dps / dps.shift(21).replace(0, np.nan) - 1.0).abs()
    b = -chg.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dps vs cumulative dividend cash flow consistency (per-share vs total dividend co-move)
def f42rb_f42_capital_return_buyback_dpsvsdiv_base_v109_signal(dps, ncfdiv):
    dg = dps / dps.shift(126).replace(0, np.nan) - 1.0
    cg = ncfdiv.abs() / ncfdiv.abs().shift(126).replace(0, np.nan) - 1.0
    b = dg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yearly FCF yield z-scored vs 504d (multi-year cash-generation regime, marketcap-detrended)
def f42rb_f42_capital_return_buyback_fcfyieldyr_base_v110_signal(fcf, marketcap):
    fy = (fcf / marketcap.replace(0, np.nan)).rolling(252, min_periods=84).mean()
    b = _z(fy, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-yield momentum over a half-year (cash-generation trend)
def f42rb_f42_capital_return_buyback_fcfymom_base_v111_signal(fcf, marketcap):
    fy = fcf / marketcap.replace(0, np.nan)
    b = fy - fy.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-yield rank vs 504d (relative cash-richness percentile)
def f42rb_f42_capital_return_buyback_fcfyrank_base_v112_signal(fcf, marketcap):
    fy = fcf / marketcap.replace(0, np.nan)
    b = _rank(fy, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-yield dispersion (volatility of cash-generation yield over a year)
def f42rb_f42_capital_return_buyback_fcfydisp_base_v113_signal(fcf, marketcap):
    fy = fcf / marketcap.replace(0, np.nan)
    b = _std(fy, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surplus-after-return yearly momentum (change in retained-cash yield vs a year ago)
def f42rb_f42_capital_return_buyback_surplusrank_base_v114_signal(ncfcommon, ncfdiv, fcf, marketcap):
    surplus = (fcf - (_f42_buyback(ncfcommon) + ncfdiv.abs())) / marketcap.replace(0, np.nan)
    sm = surplus.rolling(126, min_periods=42).mean()
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surplus-after-return regime distance: retained-cash yield minus its 252d median
def f42rb_f42_capital_return_buyback_surplussm_base_v115_signal(ncfcommon, ncfdiv, fcf, marketcap):
    surplus = (fcf - (_f42_buyback(ncfcommon) + ncfdiv.abs())) / marketcap.replace(0, np.nan)
    sm = surplus.rolling(63, min_periods=21).mean()
    b = sm - sm.rolling(252, min_periods=84).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# over-distribution intensity: total payout as a multiple of FCF, smoothed and tanh-compressed
def f42rb_f42_capital_return_buyback_overpayrank_base_v116_signal(ncfcommon, ncfdiv, fcf, marketcap):
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    ratio = ret / fcf.clip(lower=0).replace(0, np.nan)
    b = np.tanh(ratio.rolling(63, min_periods=21).mean() - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# over-distribution variability: dispersion of the payout-minus-cash gap over a year
def f42rb_f42_capital_return_buyback_overpaystreak_base_v117_signal(ncfcommon, ncfdiv, fcf, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    b = _std(ty - fy, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF conversion z-scored vs 504d (multi-year cash-quality regime)
def f42rb_f42_capital_return_buyback_fcfconvyr_base_v118_signal(fcf, ncfo):
    conv = (fcf / ncfo.replace(0, np.nan)).rolling(252, min_periods=84).mean()
    b = _z(conv, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF conversion dispersion (variability of cash conversion over a year)
def f42rb_f42_capital_return_buyback_fcfconvdisp_base_v119_signal(fcf, ncfo):
    conv = fcf / ncfo.replace(0, np.nan)
    b = _std(conv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback dollars co-movement with FCF (does the firm buy back when cash is strong?)
def f42rb_f42_capital_return_buyback_bbfcfcorr_base_v120_signal(ncfcommon, fcf):
    bb = _f42_buyback(ncfcommon)
    b = bb.rolling(252, min_periods=84).corr(fcf)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend dollars co-movement with FCF (income tracking cash generation)
def f42rb_f42_capital_return_buyback_divfcfcorr_base_v121_signal(ncfdiv, fcf):
    b = ncfdiv.abs().rolling(252, min_periods=84).corr(fcf)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-yield vs dividend-yield co-movement (do return channels move together or substitute?)
def f42rb_f42_capital_return_buyback_channelcorr_base_v122_signal(ncfcommon, ncfdiv, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = by.rolling(252, min_periods=84).corr(dy)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-yield to FCF-yield slope spread (distribution growing faster/slower than cash)
def f42rb_f42_capital_return_buyback_distribgrow_base_v123_signal(ncfcommon, ncfdiv, fcf, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    b = _slope(ty, 126) - _slope(fy, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback yield x FCF yield interaction (cash-rich repurchase intensity)
def f42rb_f42_capital_return_buyback_bbfcfinter_base_v124_signal(ncfcommon, fcf, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    fy = (fcf / marketcap.replace(0, np.nan)).clip(lower=0)
    b = by * fy
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield x coverage interaction over a year (sustained income quality)
def f42rb_f42_capital_return_buyback_incomequalyr_base_v125_signal(ncfdiv, fcf, marketcap):
    dy = _f42_div_yield(ncfdiv, marketcap)
    cov = _f42_div_cover(ncfdiv, fcf).clip(lower=0)
    raw = dy * np.tanh(cov)
    b = raw.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback timing skill proxy: buyback yield weighted by FCF-yield rank (buying when cash-rich)
def f42rb_f42_capital_return_buyback_bbtimerank_base_v126_signal(ncfcommon, fcf, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    fyr = _rank(fcf / marketcap.replace(0, np.nan), 504)
    b = by * fyr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-return consistency: negative dispersion of total payout dollars over a year
def f42rb_f42_capital_return_buyback_retconsist_base_v127_signal(ncfcommon, ncfdiv):
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    b = -_std(ret, 252) / _mean(ret, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout growth acceleration: change in annual total-payout growth (return-ramp inflection)
def f42rb_f42_capital_return_buyback_payoutaccel_base_v128_signal(ncfcommon, ncfdiv):
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    g = ret / ret.shift(252).replace(0, np.nan) - 1.0
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback share of FCF spent, change over a year (rising repurchase-funding intensity)
def f42rb_f42_capital_return_buyback_bbfcfmom_base_v129_signal(ncfcommon, fcf):
    r = _f42_buyback(ncfcommon) / fcf.clip(lower=0).replace(0, np.nan)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend reliance displacement: dividend share of payout vs its slow EMA (mix drift)
def f42rb_f42_capital_return_buyback_divsharesm_base_v130_signal(ncfcommon, ncfdiv):
    dv = ncfdiv.abs()
    ret = (_f42_buyback(ncfcommon) + dv).replace(0, np.nan)
    share = dv / ret
    b = share.ewm(span=42, min_periods=21).mean() - share.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-share-flow z-scored vs 504d (multi-year net-repurchase extremity)
def f42rb_f42_capital_return_buyback_netshz_base_v131_signal(ncfcommon, marketcap):
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    b = _z(nsf, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-share-flow trend: half-year slope of net repurchase yield (accelerating buyback)
def f42rb_f42_capital_return_buyback_netshslope_base_v132_signal(ncfcommon, marketcap):
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    b = _slope(nsf, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-share-flow dispersion over a year (volatility of net-repurchase intensity)
def f42rb_f42_capital_return_buyback_netshrank_base_v133_signal(ncfcommon, marketcap):
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    b = _std(nsf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance episodes: dispersion of dilution dollars vs buyback dollars (lumpy capital actions)
def f42rb_f42_capital_return_buyback_capactlumpy_base_v134_signal(ncfcommon):
    iss = ncfcommon.clip(lower=0)
    bb = (-ncfcommon).clip(lower=0)
    b = _std(iss, 252) - _std(bb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback funded beyond FCF, smoothed (persistent external-funding of repurchase)
def f42rb_f42_capital_return_buyback_extfundsm_base_v135_signal(ncfcommon, fcf):
    bb = _f42_buyback(ncfcommon)
    shortfall = np.tanh((bb - fcf.clip(lower=0)) / bb.replace(0, np.nan))
    b = shortfall.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage-weighted yield: total yield x tanh(min FCF coverage) over a year (durable return)
def f42rb_f42_capital_return_buyback_durablereturn_base_v136_signal(ncfcommon, ncfdiv, fcf, marketcap):
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    mincov = (fcf / ret).rolling(252, min_periods=84).min().clip(lower=0)
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap).rolling(126, min_periods=42).mean()
    b = ty * np.tanh(mincov)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend safety distance: coverage minus 1, signed-root compressed (cushion magnitude)
def f42rb_f42_capital_return_buyback_safetydist_base_v137_signal(ncfdiv, fcf):
    cov = _f42_div_cover(ncfdiv, fcf)
    g = cov - 1.0
    b = np.sign(g) * np.sqrt(g.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-funded total return floor: min(FCF, payout)/marketcap (cash-backed return yield)
def f42rb_f42_capital_return_buyback_backedyield_base_v138_signal(ncfcommon, ncfdiv, fcf, marketcap):
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    backed = pd.concat([ret, fcf.clip(lower=0)], axis=1).min(axis=1)
    b = backed / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unbacked payout: payout beyond FCF as a fraction of payout (financed distribution share)
def f42rb_f42_capital_return_buyback_unbacked_base_v139_signal(ncfcommon, ncfdiv, fcf):
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs())
    unb = (ret - fcf.clip(lower=0)).clip(lower=0) / ret.replace(0, np.nan)
    b = unb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-return tilt yield z-scored (net buyback minus dividend, de-trended)
def f42rb_f42_capital_return_buyback_tiltz_base_v140_signal(ncfcommon, ncfdiv, marketcap):
    tilt = (_f42_buyback(ncfcommon) - ncfdiv.abs()) / marketcap.replace(0, np.nan)
    b = _z(tilt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash safety composite: OCF coverage of total payout vs buyback funding (dual cushion)
def f42rb_f42_capital_return_buyback_safetycomp_base_v141_signal(ncfcommon, ncfdiv, ncfo):
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    ocfcov = np.tanh(ncfo.clip(lower=0) / ret - 1.0)
    bb = _f42_buyback(ncfcommon)
    bbshare = np.tanh(bb / ret - 0.5)
    b = ocfcov - bbshare
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# annual distribution coverage momentum: change in year-summed FCF/payout vs a year ago
def f42rb_f42_capital_return_buyback_annualcover_base_v142_signal(ncfcommon, ncfdiv, fcf):
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).rolling(252, min_periods=84).sum()
    cash = fcf.rolling(252, min_periods=84).sum()
    cov = cash / ret.replace(0, np.nan)
    b = cov - cov.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-yield to dividend-yield log ratio, smoothed (steady channel preference)
def f42rb_f42_capital_return_buyback_channelratio_base_v143_signal(ncfcommon, ncfdiv, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    dy = _f42_div_yield(ncfdiv, marketcap).replace(0, np.nan)
    r = np.log((by + 1e-6) / (dy + 1e-6))
    b = r.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-cash-flow growth over a year (total income expansion)
def f42rb_f42_capital_return_buyback_divgrow_base_v144_signal(ncfdiv):
    dv = ncfdiv.abs()
    b = dv / dv.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-dollar growth over a year (repurchase-program expansion)
def f42rb_f42_capital_return_buyback_bbgrow_base_v145_signal(ncfcommon):
    bb = _f42_buyback(ncfcommon)
    bb_sm = bb.rolling(63, min_periods=21).mean()
    b = bb_sm / bb_sm.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash yield change over a year (cash engine behind payouts)
def f42rb_f42_capital_return_buyback_ocfgrow_base_v146_signal(ncfo, marketcap):
    fy = ncfo / marketcap.replace(0, np.nan)
    b = fy - fy.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout-to-OCF burden cushion: 1 minus max(payout/OCF) over a year (tightest headroom)
def f42rb_f42_capital_return_buyback_ocfcushion_base_v147_signal(ncfcommon, ncfdiv, ncfo):
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    burden = ret / ncfo.clip(lower=0).replace(0, np.nan)
    b = 1.0 - burden.rolling(252, min_periods=84).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-channel return level smoothed then de-meaned (income-weighted return regime)
def f42rb_f42_capital_return_buyback_retbias_base_v148_signal(ncfcommon, ncfdiv, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    divshare = dv / (bb + dv).replace(0, np.nan)
    raw = (ty * divshare).rolling(63, min_periods=21).mean()
    b = raw - raw.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-coverage regime distance: coverage minus its 504d median, signed-root
def f42rb_f42_capital_return_buyback_covregdist_base_v149_signal(ncfdiv, fcf):
    cov = _f42_div_cover(ncfdiv, fcf)
    med = cov.rolling(504, min_periods=126).median()
    g = cov - med
    b = np.sign(g) * np.sqrt(g.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-return composite: smoothed total yield x FCF-coverage x (0.5 + buyback tilt)
def f42rb_f42_capital_return_buyback_crscore_base_v150_signal(ncfcommon, ncfdiv, fcf, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap).rolling(63, min_periods=21).mean()
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    cov = np.tanh((fcf / ret).clip(lower=0))
    bb = _f42_buyback(ncfcommon)
    tilt = bb / ret
    b = ty * cov * (0.5 + tilt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f42rb_f42_capital_return_buyback_byyieldyr_base_v076_signal,
    f42rb_f42_capital_return_buyback_byaccel2_base_v077_signal,
    f42rb_f42_capital_return_buyback_bycurv_base_v078_signal,
    f42rb_f42_capital_return_buyback_bbcumyield_base_v079_signal,
    f42rb_f42_capital_return_buyback_byskew_base_v080_signal,
    f42rb_f42_capital_return_buyback_divyieldyr_base_v081_signal,
    f42rb_f42_capital_return_buyback_dyaccel_base_v082_signal,
    f42rb_f42_capital_return_buyback_dycurv_base_v083_signal,
    f42rb_f42_capital_return_buyback_divcumyield_base_v084_signal,
    f42rb_f42_capital_return_buyback_dydisp_base_v085_signal,
    f42rb_f42_capital_return_buyback_tyyrz_base_v086_signal,
    f42rb_f42_capital_return_buyback_tyaccel_base_v087_signal,
    f42rb_f42_capital_return_buyback_tycumyield_base_v088_signal,
    f42rb_f42_capital_return_buyback_tydisp_base_v089_signal,
    f42rb_f42_capital_return_buyback_mixsm_base_v090_signal,
    f42rb_f42_capital_return_buyback_mixdisp_base_v091_signal,
    f42rb_f42_capital_return_buyback_mixrank_base_v092_signal,
    f42rb_f42_capital_return_buyback_covmin_base_v093_signal,
    f42rb_f42_capital_return_buyback_covdisp_base_v094_signal,
    f42rb_f42_capital_return_buyback_covrank_base_v095_signal,
    f42rb_f42_capital_return_buyback_covaccel_base_v096_signal,
    f42rb_f42_capital_return_buyback_retcovmin_base_v097_signal,
    f42rb_f42_capital_return_buyback_fcfpayoutsm_base_v098_signal,
    f42rb_f42_capital_return_buyback_fcfpayoutrank_base_v099_signal,
    f42rb_f42_capital_return_buyback_bbfcfsm_base_v100_signal,
    f42rb_f42_capital_return_buyback_bbocfz2_base_v101_signal,
    f42rb_f42_capital_return_buyback_divocfsm_base_v102_signal,
    f42rb_f42_capital_return_buyback_retocfrank_base_v103_signal,
    f42rb_f42_capital_return_buyback_dpsaccel_base_v104_signal,
    f42rb_f42_capital_return_buyback_dpsslope_base_v105_signal,
    f42rb_f42_capital_return_buyback_dpsrank_base_v106_signal,
    f42rb_f42_capital_return_buyback_dpsdisp_base_v107_signal,
    f42rb_f42_capital_return_buyback_dpsstag_base_v108_signal,
    f42rb_f42_capital_return_buyback_dpsvsdiv_base_v109_signal,
    f42rb_f42_capital_return_buyback_fcfyieldyr_base_v110_signal,
    f42rb_f42_capital_return_buyback_fcfymom_base_v111_signal,
    f42rb_f42_capital_return_buyback_fcfyrank_base_v112_signal,
    f42rb_f42_capital_return_buyback_fcfydisp_base_v113_signal,
    f42rb_f42_capital_return_buyback_surplusrank_base_v114_signal,
    f42rb_f42_capital_return_buyback_surplussm_base_v115_signal,
    f42rb_f42_capital_return_buyback_overpayrank_base_v116_signal,
    f42rb_f42_capital_return_buyback_overpaystreak_base_v117_signal,
    f42rb_f42_capital_return_buyback_fcfconvyr_base_v118_signal,
    f42rb_f42_capital_return_buyback_fcfconvdisp_base_v119_signal,
    f42rb_f42_capital_return_buyback_bbfcfcorr_base_v120_signal,
    f42rb_f42_capital_return_buyback_divfcfcorr_base_v121_signal,
    f42rb_f42_capital_return_buyback_channelcorr_base_v122_signal,
    f42rb_f42_capital_return_buyback_distribgrow_base_v123_signal,
    f42rb_f42_capital_return_buyback_bbfcfinter_base_v124_signal,
    f42rb_f42_capital_return_buyback_incomequalyr_base_v125_signal,
    f42rb_f42_capital_return_buyback_bbtimerank_base_v126_signal,
    f42rb_f42_capital_return_buyback_retconsist_base_v127_signal,
    f42rb_f42_capital_return_buyback_payoutaccel_base_v128_signal,
    f42rb_f42_capital_return_buyback_bbfcfmom_base_v129_signal,
    f42rb_f42_capital_return_buyback_divsharesm_base_v130_signal,
    f42rb_f42_capital_return_buyback_netshz_base_v131_signal,
    f42rb_f42_capital_return_buyback_netshslope_base_v132_signal,
    f42rb_f42_capital_return_buyback_netshrank_base_v133_signal,
    f42rb_f42_capital_return_buyback_capactlumpy_base_v134_signal,
    f42rb_f42_capital_return_buyback_extfundsm_base_v135_signal,
    f42rb_f42_capital_return_buyback_durablereturn_base_v136_signal,
    f42rb_f42_capital_return_buyback_safetydist_base_v137_signal,
    f42rb_f42_capital_return_buyback_backedyield_base_v138_signal,
    f42rb_f42_capital_return_buyback_unbacked_base_v139_signal,
    f42rb_f42_capital_return_buyback_tiltz_base_v140_signal,
    f42rb_f42_capital_return_buyback_safetycomp_base_v141_signal,
    f42rb_f42_capital_return_buyback_annualcover_base_v142_signal,
    f42rb_f42_capital_return_buyback_channelratio_base_v143_signal,
    f42rb_f42_capital_return_buyback_divgrow_base_v144_signal,
    f42rb_f42_capital_return_buyback_bbgrow_base_v145_signal,
    f42rb_f42_capital_return_buyback_ocfgrow_base_v146_signal,
    f42rb_f42_capital_return_buyback_ocfcushion_base_v147_signal,
    f42rb_f42_capital_return_buyback_retbias_base_v148_signal,
    f42rb_f42_capital_return_buyback_covregdist_base_v149_signal,
    f42rb_f42_capital_return_buyback_crscore_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_CAPITAL_RETURN_BUYBACK_REGISTRY_076_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
    g = np.random.default_rng(seed)
    n = 1500
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    s = s * (1.0 + g.normal(0.0, 0.04, n))
    if allow_neg:
        s = s - base * 0.6
    return pd.Series(s, name=None)


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
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    _bb_mag = _fund(101, base=7e7, drift=0.005, vol=0.18)
    _iss_mag = _fund(111, base=6.5e7, drift=-0.01, vol=0.30)
    ncfcommon = (_iss_mag - _bb_mag).rename("ncfcommon")
    ncfdiv = _fund(102, base=6e7, drift=0.02, vol=0.11).rename("ncfdiv")
    dps = _fund(103, base=0.4, drift=0.015, vol=0.05).rename("dps")
    fcf = _fund(104, base=1.2e8, drift=0.025, vol=0.1, allow_neg=True).rename("fcf")
    ncfo = _fund(105, base=1.6e8, drift=0.025, vol=0.09, allow_neg=True).rename("ncfo")
    marketcap = _fund(106, base=2.5e9, drift=0.02, vol=0.06).rename("marketcap")

    cols = {"ncfcommon": ncfcommon, "ncfdiv": ncfdiv, "dps": dps,
            "fcf": fcf, "ncfo": ncfo, "marketcap": marketcap}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f42_capital_return_buyback_base_076_150_claude: %d features pass" % n_features)
