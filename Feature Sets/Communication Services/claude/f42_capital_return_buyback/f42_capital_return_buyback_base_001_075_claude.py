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
    # buyback dollars = negative ncfcommon (cash paid to repurchase shares)
    return (-ncfcommon).clip(lower=0)


def _f42_issuance(ncfcommon):
    # dilution dollars = positive ncfcommon (cash raised issuing shares)
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
# buyback intensity: gross buyback dollars vs marketcap (shareholder yield from repurchase)
def f42rb_f42_capital_return_buyback_byyield_base_v001_signal(ncfcommon, marketcap):
    b = _f42_buyback_yield(ncfcommon, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback yield smoothed over a quarter (persistent repurchase regime)
def f42rb_f42_capital_return_buyback_byyieldsm_base_v002_signal(ncfcommon, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = by.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback yield z-scored vs its own 252d history (de-trended intensity)
def f42rb_f42_capital_return_buyback_byyieldz_base_v003_signal(ncfcommon, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = _z(by, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback yield percentile-ranked vs its own 504d history
def f42rb_f42_capital_return_buyback_byyieldrank_base_v004_signal(ncfcommon, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = _rank(by, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net share-count cash flow yield, change vs one year ago (net-repurchase momentum)
def f42rb_f42_capital_return_buyback_netshflow_base_v005_signal(ncfcommon, marketcap):
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    b = nsf - nsf.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution drag: gross issuance dollars vs marketcap (negative shareholder yield)
def f42rb_f42_capital_return_buyback_issyield_base_v006_signal(ncfcommon, marketcap):
    b = _f42_issuance(ncfcommon) / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-vs-issuance net regime: net repurchase relative to gross share-flow over a quarter
def f42rb_f42_capital_return_buyback_buybackbias_base_v007_signal(ncfcommon):
    net = (-ncfcommon).rolling(63, min_periods=21).sum()
    gross = ncfcommon.abs().rolling(63, min_periods=21).sum()
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield from dividend cash flow vs marketcap
def f42rb_f42_capital_return_buyback_divyield_base_v008_signal(ncfdiv, marketcap):
    b = _f42_div_yield(ncfdiv, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield z-scored vs its own 252d history (de-trended payout level)
def f42rb_f42_capital_return_buyback_divyieldz_base_v009_signal(ncfdiv, marketcap):
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = _z(dy, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield percentile-ranked vs its 504d history
def f42rb_f42_capital_return_buyback_divyieldrank_base_v010_signal(ncfdiv, marketcap):
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = _rank(dy, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total shareholder yield: buyback + dividend, vs marketcap
def f42rb_f42_capital_return_buyback_totyield_base_v011_signal(ncfcommon, ncfdiv, marketcap):
    b = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total shareholder yield smoothed over a half-year (persistent return)
def f42rb_f42_capital_return_buyback_totyieldsm_base_v012_signal(ncfcommon, ncfdiv, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = ty.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total shareholder yield z-scored vs its 252d history
def f42rb_f42_capital_return_buyback_totyieldz_base_v013_signal(ncfcommon, ncfdiv, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = _z(ty, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return mix: buyback share of total shareholder return (repurchase vs dividend tilt)
def f42rb_f42_capital_return_buyback_returnmix_base_v014_signal(ncfcommon, ncfdiv):
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    b = (bb - dv) / (bb + dv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend coverage by free cash flow (sustainability of the dividend)
def f42rb_f42_capital_return_buyback_divcover_base_v015_signal(ncfdiv, fcf):
    b = _f42_div_cover(ncfdiv, fcf)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend coverage smoothed over a year (durable coverage)
def f42rb_f42_capital_return_buyback_divcoversm_base_v016_signal(ncfdiv, fcf):
    cov = _f42_div_cover(ncfdiv, fcf)
    b = cov.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend coverage z-scored vs its own 252d history (coverage de-trend)
def f42rb_f42_capital_return_buyback_divcoverz_base_v017_signal(ncfdiv, fcf):
    cov = _f42_div_cover(ncfdiv, fcf)
    b = _z(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio of dividends out of free cash flow (FCF payout intensity)
def f42rb_f42_capital_return_buyback_divpayout_base_v018_signal(ncfdiv, fcf):
    b = ncfdiv.abs() / fcf.clip(lower=0).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-return payout: (buyback + dividend) out of free cash flow (FCF-funded return)
def f42rb_f42_capital_return_buyback_fcfpayout_base_v019_signal(ncfcommon, ncfdiv, fcf):
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    b = ret / fcf.clip(lower=0).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-funded coverage of total shareholder return (how many times FCF covers payout)
def f42rb_f42_capital_return_buyback_retcover_base_v020_signal(ncfcommon, ncfdiv, fcf):
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    b = fcf / ret
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback funded by free cash flow (repurchase out of FCF)
def f42rb_f42_capital_return_buyback_bbfcf_base_v021_signal(ncfcommon, fcf):
    b = _f42_buyback(ncfcommon) / fcf.clip(lower=0).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback funded by operating cash flow (repurchase out of ncfo)
def f42rb_f42_capital_return_buyback_bbocf_base_v022_signal(ncfcommon, ncfo):
    b = _f42_buyback(ncfcommon) / ncfo.clip(lower=0).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend out of operating cash flow (OCF dividend payout)
def f42rb_f42_capital_return_buyback_divocf_base_v023_signal(ncfdiv, ncfo):
    b = ncfdiv.abs() / ncfo.clip(lower=0).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash coverage of total capital return (how many times OCF covers payout)
def f42rb_f42_capital_return_buyback_retocf_base_v024_signal(ncfcommon, ncfdiv, ncfo):
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    cov = ncfo.clip(lower=0) / ret
    b = cov - cov.rolling(252, min_periods=84).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend per share displacement: fast EMA vs slow EMA of dps (hike-cycle phase)
def f42rb_f42_capital_return_buyback_dpslevel_base_v025_signal(dps):
    fast = dps.ewm(span=42, min_periods=21).mean()
    slow = dps.ewm(span=189, min_periods=63).mean()
    b = fast / slow.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend per share growth over a year (dividend hike momentum)
def f42rb_f42_capital_return_buyback_dpsgrow_base_v026_signal(dps):
    b = dps / dps.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend per share z-scored vs its 252d history (de-trended dps)
def f42rb_f42_capital_return_buyback_dpsz_base_v027_signal(dps):
    b = _z(dps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-hike streak: fraction of last year dps was rising (dividend growth persistence)
def f42rb_f42_capital_return_buyback_dpshikefreq_base_v028_signal(dps):
    up = (dps > dps.shift(21)).astype(float)
    b = up.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend cut detector: depth of dps below its trailing 252d peak
def f42rb_f42_capital_return_buyback_dpscut_base_v029_signal(dps):
    peak = dps.rolling(252, min_periods=84).max()
    b = dps / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-reliance trend: half-year slope of dividend's share of total shareholder yield
def f42rb_f42_capital_return_buyback_divreliance_base_v030_signal(ncfdiv, ncfcommon, marketcap):
    dy = _f42_div_yield(ncfdiv, marketcap)
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap).replace(0, np.nan)
    share = dy / ty
    b = _slope(share, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback acceleration: change in buyback yield over a quarter (ramping repurchase)
def f42rb_f42_capital_return_buyback_byaccel_base_v031_signal(ncfcommon, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = by - by.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-yield momentum over a half-year (capital-return ramp)
def f42rb_f42_capital_return_buyback_tymom_base_v032_signal(ncfcommon, ncfdiv, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = ty - ty.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-yield momentum over a year (rising income)
def f42rb_f42_capital_return_buyback_dymom_base_v033_signal(ncfdiv, marketcap):
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = dy - dy.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash-flow yield (FCF vs marketcap) — the resource funding capital return
def f42rb_f42_capital_return_buyback_fcfyield_base_v034_signal(fcf, marketcap):
    b = fcf / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF yield z-scored vs its own 252d history (de-trended cash generation)
def f42rb_f42_capital_return_buyback_fcfyieldz_base_v035_signal(fcf, marketcap):
    fy = fcf / marketcap.replace(0, np.nan)
    b = _z(fy, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surplus FCF after total return, change vs one year ago (retained-cash momentum)
def f42rb_f42_capital_return_buyback_surplus_base_v036_signal(ncfcommon, ncfdiv, fcf, marketcap):
    surplus = (fcf - (_f42_buyback(ncfcommon) + ncfdiv.abs())) / marketcap.replace(0, np.nan)
    b = surplus - surplus.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF conversion: free cash flow as a share of operating cash flow, z-scored (cash-quality regime)
def f42rb_f42_capital_return_buyback_fcfconv_base_v037_signal(fcf, ncfo):
    conv = fcf / ncfo.replace(0, np.nan)
    b = _z(conv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# over-distribution stress, de-meaned vs its own 252d norm (payout-vs-cash regime distance)
def f42rb_f42_capital_return_buyback_overpay_base_v038_signal(ncfcommon, ncfdiv, fcf, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    gap = ty - fy
    b = gap - gap.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustainable-return depth: FCF-minus-payout margin, z-scored vs its 252d norm (cushion regime)
def f42rb_f42_capital_return_buyback_sustdepth_base_v039_signal(ncfcommon, ncfdiv, fcf):
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs())
    margin = (fcf - ret) / ret.replace(0, np.nan)
    b = _z(margin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year with positive net buyback (repurchase persistence)
def f42rb_f42_capital_return_buyback_bbpersist_base_v040_signal(ncfcommon):
    isbb = (-ncfcommon > 0).astype(float)
    b = isbb.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year dividend-coverage sat in the upper half of its 504d range (comfort regime)
def f42rb_f42_capital_return_buyback_covregime_base_v041_signal(ncfdiv, fcf):
    cov = _f42_div_cover(ncfdiv, fcf)
    med = cov.rolling(504, min_periods=126).median()
    ok = (cov > med).astype(float)
    b = ok.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funded return regime: smoothed FCF-minus-payout margin relative to payout (continuous)
def f42rb_f42_capital_return_buyback_selffund_base_v042_signal(ncfcommon, ncfdiv, fcf):
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs())
    margin = np.tanh((fcf - ret) / ret.replace(0, np.nan))
    b = margin.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-buyback dollars minus dividend dollars, scaled by marketcap (return-tilt yield)
def f42rb_f42_capital_return_buyback_tiltyield_base_v043_signal(ncfcommon, ncfdiv, marketcap):
    b = (_f42_buyback(ncfcommon) - ncfdiv.abs()) / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-yield dispersion (volatility of repurchase intensity over a year)
def f42rb_f42_capital_return_buyback_bydisp_base_v044_signal(ncfcommon, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = _std(by, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-yield stability: mean-over-std (signal-to-noise) of dividend yield over a year
def f42rb_f42_capital_return_buyback_dystable_base_v045_signal(ncfdiv, marketcap):
    dy = _f42_div_yield(ncfdiv, marketcap)
    m = _mean(dy, 252)
    sd = _std(dy, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-yield smoothness: negative coefficient of variation (steady = high)
def f42rb_f42_capital_return_buyback_tysmooth_base_v046_signal(ncfcommon, ncfdiv, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = -_std(ty, 126) / _mean(ty, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback intensity vs operating cash generation, z-scored (repurchase aggression)
def f42rb_f42_capital_return_buyback_bbocfz_base_v047_signal(ncfcommon, ncfo):
    r = _f42_buyback(ncfcommon) / ncfo.clip(lower=0).replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend hike funded by FCF growth (sustainable hike vs cash trajectory)
def f42rb_f42_capital_return_buyback_hikefund_base_v048_signal(dps, fcf):
    dg = dps / dps.shift(252).replace(0, np.nan) - 1.0
    fg = fcf / fcf.shift(252).replace(0, np.nan) - 1.0
    b = dg - fg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-to-FCF spend ratio, z-scored vs its 252d norm (repurchase aggression regime)
def f42rb_f42_capital_return_buyback_byfcfratio_base_v049_signal(ncfcommon, fcf, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    fy = (fcf / marketcap.replace(0, np.nan)).replace(0, np.nan)
    b = _z(by / fy, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-mix extremity: buyback-vs-dividend tilt z-scored vs its 252d norm (composition regime)
def f42rb_f42_capital_return_buyback_mixmom_base_v050_signal(ncfcommon, ncfdiv):
    bb = _f42_buyback(ncfcommon)
    dv = ncfdiv.abs()
    mix = (bb - dv) / (bb + dv).replace(0, np.nan)
    b = _z(mix, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-yield rank vs cross-time 504d history (relative capital-return percentile)
def f42rb_f42_capital_return_buyback_tyrank_base_v051_signal(ncfcommon, ncfdiv, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = _rank(ty, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative buyback-to-dividend composition over a trailing year (annual repurchase tilt)
def f42rb_f42_capital_return_buyback_bbperdiv_base_v052_signal(ncfcommon, ncfdiv):
    bb_sum = _f42_buyback(ncfcommon).rolling(252, min_periods=84).sum()
    dv_sum = ncfdiv.abs().rolling(252, min_periods=84).sum()
    b = np.log((bb_sum + 1.0) / (dv_sum + 1.0).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback headroom (retained yield after dividend), percentile-ranked vs 504d history
def f42rb_f42_capital_return_buyback_bbheadroom_base_v053_signal(fcf, ncfdiv, marketcap):
    fy = fcf / marketcap.replace(0, np.nan)
    dy = _f42_div_yield(ncfdiv, marketcap)
    b = _rank(fy - dy, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-return cash burden: payout dollars vs operating cash flow, z-scored
def f42rb_f42_capital_return_buyback_burdenz_base_v054_signal(ncfcommon, ncfdiv, ncfo):
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    r = ret / ncfo.clip(lower=0).replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend coverage trend: slope of FCF/dividend over a half-year (improving cover)
def f42rb_f42_capital_return_buyback_covtrend_base_v055_signal(ncfdiv, fcf):
    cov = _f42_div_cover(ncfdiv, fcf)
    b = _slope(cov, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-yield trend: slope of repurchase intensity over a half-year
def f42rb_f42_capital_return_buyback_bytrend_base_v056_signal(ncfcommon, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    b = _slope(by, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-yield to FCF-yield gap, ranked (over/under-distribution percentile)
def f42rb_f42_capital_return_buyback_distribrank_base_v057_signal(ncfcommon, ncfdiv, fcf, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    b = _rank(ty - fy, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield x coverage: income quality (high yield only if covered)
def f42rb_f42_capital_return_buyback_incomequal_base_v058_signal(ncfdiv, fcf, marketcap):
    dy = _f42_div_yield(ncfdiv, marketcap)
    cov = _f42_div_cover(ncfdiv, fcf).clip(lower=0)
    b = dy * np.tanh(cov)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback yield x self-funding: repurchase quality (intensity gated by FCF funding)
def f42rb_f42_capital_return_buyback_bbqual_base_v059_signal(ncfcommon, fcf, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    fund = (fcf / _f42_buyback(ncfcommon).replace(0, np.nan)).clip(0, 3)
    b = by * fund
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total shareholder yield x sustainability (FCF-covered) composite return score
def f42rb_f42_capital_return_buyback_retscore_base_v060_signal(ncfcommon, ncfdiv, fcf, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    cov = (fcf / ret).clip(lower=0)
    b = ty * np.tanh(cov)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance burstiness: dispersion of issuance dollars over a year (lumpy dilution events)
def f42rb_f42_capital_return_buyback_dilregime_base_v061_signal(ncfcommon):
    iss = ncfcommon.clip(lower=0)
    disp = _std(iss, 252) / (_mean(iss, 252).replace(0, np.nan))
    b = disp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payer identity: dps growth co-movement with dividend cash-flow (organic income payer vs episodic)
def f42rb_f42_capital_return_buyback_payeridentity_base_v062_signal(dps, ncfdiv, marketcap):
    dg = (dps / dps.shift(63).replace(0, np.nan) - 1.0)
    dvy = _f42_div_yield(ncfdiv, marketcap)
    b = dg.rolling(252, min_periods=84).corr(dvy)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-return intensity vs its multi-year norm (buyback+div yield z over 504d)
def f42rb_f42_capital_return_buyback_intensz_base_v063_signal(ncfcommon, ncfdiv, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = _z(ty, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-funding shortfall: buyback dollars beyond FCF as a fraction of buyback (debt-funded share)
def f42rb_f42_capital_return_buyback_bbstress_base_v064_signal(ncfcommon, fcf, marketcap):
    bb = _f42_buyback(ncfcommon)
    shortfall = (bb - fcf.clip(lower=0)) / bb.replace(0, np.nan)
    b = np.tanh(shortfall)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# income-growth vs repurchase-intensity ratio (does the firm grow dividends or buy back?)
def f42rb_f42_capital_return_buyback_incomevsbb_base_v065_signal(dps, ncfcommon, marketcap):
    dg = (dps / dps.shift(126).replace(0, np.nan) - 1.0).clip(lower=0)
    by = _f42_buyback_yield(ncfcommon, marketcap).rolling(63, min_periods=21).mean()
    b = np.tanh(dg) - np.tanh(80.0 * by)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash payout ratio of dividend, z-scored (OCF dividend strain)
def f42rb_f42_capital_return_buyback_divocfz_base_v066_signal(ncfdiv, ncfo):
    r = ncfdiv.abs() / ncfo.clip(lower=0).replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash retained after all capital return, smoothed then z-scored (war-chest accumulation)
def f42rb_f42_capital_return_buyback_warchest_base_v067_signal(ncfcommon, ncfdiv, fcf, marketcap):
    surplus = (fcf - (_f42_buyback(ncfcommon) + ncfdiv.abs())) / marketcap.replace(0, np.nan)
    sm = surplus.rolling(63, min_periods=21).mean()
    b = _z(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total payout dollars growth over a year (capital-return expansion)
def f42rb_f42_capital_return_buyback_payoutgrow_base_v068_signal(ncfcommon, ncfdiv):
    ret = _f42_buyback(ncfcommon) + ncfdiv.abs()
    b = ret / ret.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback timing value: repurchase intensity weighted by FCF yield (buying with cash strength)
def f42rb_f42_capital_return_buyback_bbtiming_base_v069_signal(ncfcommon, fcf, marketcap):
    by = _f42_buyback_yield(ncfcommon, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    b = by * np.sign(fy) * np.sqrt(fy.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend coverage minus its 252d norm (coverage improvement vs own history)
def f42rb_f42_capital_return_buyback_covimprove_base_v070_signal(ncfdiv, fcf):
    cov = _f42_div_cover(ncfdiv, fcf)
    b = cov - cov.rolling(252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-cash-flow net yield: fast minus slow EMA (steady net repurchase displacement)
def f42rb_f42_capital_return_buyback_netshdisp_base_v071_signal(ncfcommon, marketcap):
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    b = nsf.ewm(span=63, min_periods=21).mean() - nsf.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-return cyclicality: how total-yield co-moves with FCF yield (pro-cyclical payout)
def f42rb_f42_capital_return_buyback_cyclicality_base_v072_signal(ncfcommon, ncfdiv, fcf, marketcap):
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    fy = fcf / marketcap.replace(0, np.nan)
    b = ty.rolling(252, min_periods=84).corr(fy)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend cash-flow growth funded by operating cash (income trajectory vs OCF trajectory)
def f42rb_f42_capital_return_buyback_dyfcfshare_base_v073_signal(ncfdiv, ncfo):
    dg = ncfdiv.abs() / ncfdiv.abs().shift(252).replace(0, np.nan) - 1.0
    og = ncfo / ncfo.shift(252).replace(0, np.nan) - 1.0
    b = dg - og
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback consistency: signed-magnitude of net repurchase compressed (steady-buyer score)
def f42rb_f42_capital_return_buyback_bbsignmag_base_v074_signal(ncfcommon, marketcap):
    nsf = -ncfcommon / marketcap.replace(0, np.nan)
    typ = nsf.rolling(252, min_periods=84).mean()
    b = np.sign(nsf) * np.sqrt(nsf.abs()) - np.sign(typ) * np.sqrt(typ.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-shareholder-return durability: min coverage over last year scaled by yield
def f42rb_f42_capital_return_buyback_durability_base_v075_signal(ncfcommon, ncfdiv, fcf, marketcap):
    ret = (_f42_buyback(ncfcommon) + ncfdiv.abs()).replace(0, np.nan)
    cov = (fcf / ret)
    mincov = cov.rolling(252, min_periods=84).min().clip(lower=0)
    ty = _f42_total_yield(ncfcommon, ncfdiv, marketcap)
    b = ty * np.tanh(mincov)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f42rb_f42_capital_return_buyback_byyield_base_v001_signal,
    f42rb_f42_capital_return_buyback_byyieldsm_base_v002_signal,
    f42rb_f42_capital_return_buyback_byyieldz_base_v003_signal,
    f42rb_f42_capital_return_buyback_byyieldrank_base_v004_signal,
    f42rb_f42_capital_return_buyback_netshflow_base_v005_signal,
    f42rb_f42_capital_return_buyback_issyield_base_v006_signal,
    f42rb_f42_capital_return_buyback_buybackbias_base_v007_signal,
    f42rb_f42_capital_return_buyback_divyield_base_v008_signal,
    f42rb_f42_capital_return_buyback_divyieldz_base_v009_signal,
    f42rb_f42_capital_return_buyback_divyieldrank_base_v010_signal,
    f42rb_f42_capital_return_buyback_totyield_base_v011_signal,
    f42rb_f42_capital_return_buyback_totyieldsm_base_v012_signal,
    f42rb_f42_capital_return_buyback_totyieldz_base_v013_signal,
    f42rb_f42_capital_return_buyback_returnmix_base_v014_signal,
    f42rb_f42_capital_return_buyback_divcover_base_v015_signal,
    f42rb_f42_capital_return_buyback_divcoversm_base_v016_signal,
    f42rb_f42_capital_return_buyback_divcoverz_base_v017_signal,
    f42rb_f42_capital_return_buyback_divpayout_base_v018_signal,
    f42rb_f42_capital_return_buyback_fcfpayout_base_v019_signal,
    f42rb_f42_capital_return_buyback_retcover_base_v020_signal,
    f42rb_f42_capital_return_buyback_bbfcf_base_v021_signal,
    f42rb_f42_capital_return_buyback_bbocf_base_v022_signal,
    f42rb_f42_capital_return_buyback_divocf_base_v023_signal,
    f42rb_f42_capital_return_buyback_retocf_base_v024_signal,
    f42rb_f42_capital_return_buyback_dpslevel_base_v025_signal,
    f42rb_f42_capital_return_buyback_dpsgrow_base_v026_signal,
    f42rb_f42_capital_return_buyback_dpsz_base_v027_signal,
    f42rb_f42_capital_return_buyback_dpshikefreq_base_v028_signal,
    f42rb_f42_capital_return_buyback_dpscut_base_v029_signal,
    f42rb_f42_capital_return_buyback_divreliance_base_v030_signal,
    f42rb_f42_capital_return_buyback_byaccel_base_v031_signal,
    f42rb_f42_capital_return_buyback_tymom_base_v032_signal,
    f42rb_f42_capital_return_buyback_dymom_base_v033_signal,
    f42rb_f42_capital_return_buyback_fcfyield_base_v034_signal,
    f42rb_f42_capital_return_buyback_fcfyieldz_base_v035_signal,
    f42rb_f42_capital_return_buyback_surplus_base_v036_signal,
    f42rb_f42_capital_return_buyback_fcfconv_base_v037_signal,
    f42rb_f42_capital_return_buyback_overpay_base_v038_signal,
    f42rb_f42_capital_return_buyback_sustdepth_base_v039_signal,
    f42rb_f42_capital_return_buyback_bbpersist_base_v040_signal,
    f42rb_f42_capital_return_buyback_covregime_base_v041_signal,
    f42rb_f42_capital_return_buyback_selffund_base_v042_signal,
    f42rb_f42_capital_return_buyback_tiltyield_base_v043_signal,
    f42rb_f42_capital_return_buyback_bydisp_base_v044_signal,
    f42rb_f42_capital_return_buyback_dystable_base_v045_signal,
    f42rb_f42_capital_return_buyback_tysmooth_base_v046_signal,
    f42rb_f42_capital_return_buyback_bbocfz_base_v047_signal,
    f42rb_f42_capital_return_buyback_hikefund_base_v048_signal,
    f42rb_f42_capital_return_buyback_byfcfratio_base_v049_signal,
    f42rb_f42_capital_return_buyback_mixmom_base_v050_signal,
    f42rb_f42_capital_return_buyback_tyrank_base_v051_signal,
    f42rb_f42_capital_return_buyback_bbperdiv_base_v052_signal,
    f42rb_f42_capital_return_buyback_bbheadroom_base_v053_signal,
    f42rb_f42_capital_return_buyback_burdenz_base_v054_signal,
    f42rb_f42_capital_return_buyback_covtrend_base_v055_signal,
    f42rb_f42_capital_return_buyback_bytrend_base_v056_signal,
    f42rb_f42_capital_return_buyback_distribrank_base_v057_signal,
    f42rb_f42_capital_return_buyback_incomequal_base_v058_signal,
    f42rb_f42_capital_return_buyback_bbqual_base_v059_signal,
    f42rb_f42_capital_return_buyback_retscore_base_v060_signal,
    f42rb_f42_capital_return_buyback_dilregime_base_v061_signal,
    f42rb_f42_capital_return_buyback_payeridentity_base_v062_signal,
    f42rb_f42_capital_return_buyback_intensz_base_v063_signal,
    f42rb_f42_capital_return_buyback_bbstress_base_v064_signal,
    f42rb_f42_capital_return_buyback_incomevsbb_base_v065_signal,
    f42rb_f42_capital_return_buyback_divocfz_base_v066_signal,
    f42rb_f42_capital_return_buyback_warchest_base_v067_signal,
    f42rb_f42_capital_return_buyback_payoutgrow_base_v068_signal,
    f42rb_f42_capital_return_buyback_bbtiming_base_v069_signal,
    f42rb_f42_capital_return_buyback_covimprove_base_v070_signal,
    f42rb_f42_capital_return_buyback_netshdisp_base_v071_signal,
    f42rb_f42_capital_return_buyback_cyclicality_base_v072_signal,
    f42rb_f42_capital_return_buyback_dyfcfshare_base_v073_signal,
    f42rb_f42_capital_return_buyback_bbsignmag_base_v074_signal,
    f42rb_f42_capital_return_buyback_durability_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_CAPITAL_RETURN_BUYBACK_REGISTRY_001_075 = REGISTRY


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

    # ncfcommon: net common-stock cash flow. Buyback-heavy media -> usually NEGATIVE
    # (cash paid to repurchase), with occasional positive issuance blocks. Build as a
    # signed series crossing zero: repurchase magnitude (negated) plus episodic issuance.
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

    print("OK f42_capital_return_buyback_base_001_075_claude: %d features pass" % n_features)
