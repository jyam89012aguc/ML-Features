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
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
    return s - s.shift(w)


# ===== folder domain primitives (capital return / payout) =====
def _f49_payout_sustain(ncfdiv, fcf):
    return ncfdiv.abs() / fcf.replace(0, np.nan)


def _f49_div_coverage_fcf(fcf, ncfdiv):
    return fcf / ncfdiv.abs().replace(0, np.nan)


def _f49_div_coverage_ocf(ncfo, ncfdiv):
    return ncfo / ncfdiv.abs().replace(0, np.nan)


def _f49_pref_drag(prefdivis, netinc):
    return prefdivis.abs() / netinc.abs().replace(0, np.nan)


def _f49_payout_earn(ncfdiv, netinc):
    return ncfdiv.abs() / netinc.replace(0, np.nan)


# ============================================================
# --- dividend dollar level dynamics (ncfdiv) ---
# dividends paid, log-growth over a year (absolute capital-return growth)
def f49pr_f49_capital_return_payout_divgrow_252d_base_v076_signal(ncfdiv):
    g = np.log(ncfdiv.abs().replace(0, np.nan)) - np.log(ncfdiv.abs().shift(252).replace(0, np.nan))
    result = g
    return result.replace([np.inf, -np.inf], np.nan)


# dividends paid relative to their own 2yr average (payout level vs normal)
def f49pr_f49_capital_return_payout_divnorm_504d_base_v077_signal(ncfdiv):
    avg = ncfdiv.abs().rolling(504, min_periods=126).mean()
    result = ncfdiv.abs() / avg.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# dividend dollar dispersion (volatility of the payout dollars)
def f49pr_f49_capital_return_payout_divvol_252d_base_v078_signal(ncfdiv):
    d = ncfdiv.abs()
    result = _std(d, 252) / _mean(d, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# --- divyield facets ---
# dividend yield smoothed minus its slow EMA (yield displacement)
def f49pr_f49_capital_return_payout_dydisp_252d_base_v079_signal(divyield):
    sm = divyield.ewm(span=42, min_periods=21).mean()
    result = sm - divyield.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield range position over 2yr (where yield sits in its own band)
def f49pr_f49_capital_return_payout_dyrangepos_504d_base_v080_signal(divyield):
    hi = divyield.rolling(504, min_periods=126).max()
    lo = divyield.rolling(504, min_periods=126).min()
    result = (divyield - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield acceleration (2nd-difference of smoothed yield)
def f49pr_f49_capital_return_payout_dyaccel_252d_base_v081_signal(divyield):
    sm = divyield.rolling(42, min_periods=21).mean()
    result = _slope(sm, 63) - _slope(sm.shift(63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# yield rising while price falling? yield momentum sign x magnitude
def f49pr_f49_capital_return_payout_dysignmag_252d_base_v082_signal(divyield):
    chg = _slope(divyield, 126)
    result = np.sign(chg) * (chg.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)


# --- payout ratio facets ---
# payout ratio range position over 2yr
def f49pr_f49_capital_return_payout_prrangepos_504d_base_v083_signal(payoutratio):
    hi = payoutratio.rolling(504, min_periods=126).max()
    lo = payoutratio.rolling(504, min_periods=126).min()
    result = (payoutratio - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio momentum over a half-year
def f49pr_f49_capital_return_payout_prmom_126d_base_v084_signal(payoutratio):
    result = _slope(payoutratio.rolling(21, min_periods=10).mean(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio mean-reversion vs 2yr average
def f49pr_f49_capital_return_payout_prrevert_504d_base_v085_signal(payoutratio):
    avg = payoutratio.rolling(504, min_periods=126).mean()
    result = payoutratio / avg.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio smoothed level (persistent policy stance)
def f49pr_f49_capital_return_payout_prsmooth_252d_base_v086_signal(payoutratio):
    result = payoutratio.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- dps facets ---
# dps smoothed log-growth over a half-year (dividend-raise tempo)
def f49pr_f49_capital_return_payout_dpsgrow126_base_v087_signal(dps):
    g = np.log(dps.replace(0, np.nan)) - np.log(dps.shift(126).replace(0, np.nan))
    result = g.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dps consistency: low coefficient of variation = steady raiser
def f49pr_f49_capital_return_payout_dpsconsist_504d_base_v088_signal(dps):
    result = -_std(dps, 504) / _mean(dps, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# dps vs its 5yr (1260d) anchor: long-run dividend level
def f49pr_f49_capital_return_payout_dpslonganchor_1260d_base_v089_signal(dps):
    anchor = dps.rolling(1260, min_periods=252).mean()
    result = np.log(dps.replace(0, np.nan) / anchor.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# dps z-scored vs its 252d history (short-term dividend deviation)
def f49pr_f49_capital_return_payout_dpsz_252d_base_v090_signal(dps):
    result = _z(dps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- coverage facets (fcf / ocf) ---
# FCF coverage momentum normalized by its own level (relative safety trajectory)
def f49pr_f49_capital_return_payout_covfcfmom_252d_base_v091_signal(fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv).rolling(42, min_periods=21).mean()
    result = _slope(cov, 126) / cov.shift(126).abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# OCF coverage z-scored vs its own history
def f49pr_f49_capital_return_payout_covocfz_252d_base_v092_signal(ncfo, ncfdiv):
    result = _z(_f49_div_coverage_ocf(ncfo, ncfdiv), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# coverage range position: where FCF coverage sits in its 2yr band
def f49pr_f49_capital_return_payout_covrangepos_504d_base_v093_signal(fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    hi = cov.rolling(504, min_periods=126).max()
    lo = cov.rolling(504, min_periods=126).min()
    result = (cov - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# coverage shortfall depth: how far FCF coverage sits below its 2yr median, smoothed
def f49pr_f49_capital_return_payout_covdeficit_252d_base_v094_signal(fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    med = cov.rolling(504, min_periods=126).median()
    deficit = (med - cov).clip(lower=0)
    result = deficit.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- preferred facets ---
# preferred dividends growth (rising senior claim = drag building)
def f49pr_f49_capital_return_payout_prefgrow_252d_base_v095_signal(prefdivis):
    g = np.log(prefdivis.abs().replace(0, np.nan)) - np.log(prefdivis.abs().shift(252).replace(0, np.nan))
    result = g
    return result.replace([np.inf, -np.inf], np.nan)


# preferred drag momentum (is the senior claim eating more of earnings?)
def f49pr_f49_capital_return_payout_prefdragmom_252d_base_v096_signal(prefdivis, netinc):
    drag = _f49_pref_drag(prefdivis, netinc)
    result = _slope(drag.rolling(42, min_periods=21).mean(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# preferred claim relative to FCF (cash-flow seniority drag), z-scored vs own history
def f49pr_f49_capital_return_payout_preffcf_252d_base_v097_signal(prefdivis, fcf):
    b = prefdivis.abs() / fcf.replace(0, np.nan)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-to-market-cap (capital structure seniority intensity)
def f49pr_f49_capital_return_payout_prefmc_252d_base_v098_signal(prefdivis, marketcap):
    b = prefdivis.abs() / marketcap.replace(0, np.nan)
    result = b.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- fcf / earnings per share facets ---
# fcfps level z-scored (per-share cash generation deviation)
def f49pr_f49_capital_return_payout_fcfpsz_252d_base_v099_signal(fcfps):
    result = _z(fcfps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps growth (per-share cash trajectory funding future raises)
def f49pr_f49_capital_return_payout_fcfpsgrow_252d_base_v100_signal(fcfps):
    g = (fcfps - fcfps.shift(252)) / fcfps.shift(252).abs().replace(0, np.nan)
    result = g
    return result.replace([np.inf, -np.inf], np.nan)


# eps growth vs dps level (earnings runway behind the dividend)
def f49pr_f49_capital_return_payout_epsgrowvsdps_252d_base_v101_signal(eps, dps):
    ge = (eps - eps.shift(252)) / eps.shift(252).abs().replace(0, np.nan)
    result = ge - _rank(dps, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps minus dps absolute per-share retained cash, smoothed
def f49pr_f49_capital_return_payout_retainedps_252d_base_v102_signal(fcfps, dps):
    retained = fcfps - dps
    result = retained.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite / interaction facets ---
# dividend coverage breadth: min of FCF and OCF coverage (binding constraint)
def f49pr_f49_capital_return_payout_covmin_252d_base_v103_signal(fcf, ncfo, ncfdiv):
    cfcf = _f49_div_coverage_fcf(fcf, ncfdiv)
    cocf = _f49_div_coverage_ocf(ncfo, ncfdiv)
    binding = pd.concat([cfcf, cocf], axis=1).min(axis=1)
    result = binding.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capital-return yield: total dollars returned (div+pref) over market cap, z
def f49pr_f49_capital_return_payout_cryield_z_252d_base_v104_signal(ncfdiv, prefdivis, marketcap):
    cry = (ncfdiv.abs() + prefdivis.abs()) / marketcap.replace(0, np.nan)
    result = _z(cry, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# payout sustainability dispersion across windows (policy stability proxy)
def f49pr_f49_capital_return_payout_psustdisp_504d_base_v105_signal(ncfdiv, fcf):
    ps = _f49_payout_sustain(ncfdiv, fcf)
    short = ps.rolling(63, min_periods=21).mean()
    long = ps.rolling(252, min_periods=63).mean()
    result = (short - long).rolling(126, min_periods=42).std()
    return result.replace([np.inf, -np.inf], np.nan)


# earnings payout vs cash payout ratio (accrual quality of distributions)
def f49pr_f49_capital_return_payout_accrualquality_252d_base_v106_signal(dps, eps, ncfdiv, fcf):
    epspay = dps / eps.replace(0, np.nan)
    fcfpay = _f49_payout_sustain(ncfdiv, fcf)
    result = (epspay / fcfpay.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dividend funded by operations after capex AND preferred (true free residual share)
def f49pr_f49_capital_return_payout_trueresidual_252d_base_v107_signal(fcf, prefdivis, ncfdiv):
    residual = fcf - prefdivis.abs()
    b = ncfdiv.abs() / residual.replace(0, np.nan)
    result = b.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dividend growth vs payout-ratio change (raising via growth vs via higher payout)
def f49pr_f49_capital_return_payout_raisesource_252d_base_v108_signal(dps, payoutratio):
    gd = (dps - dps.shift(252)) / dps.shift(252).abs().replace(0, np.nan)
    gpr = _slope(payoutratio, 252)
    result = gd - gpr
    return result.replace([np.inf, -np.inf], np.nan)


# yield vs payout-ratio divergence (yield up but payout flat => price-driven)
def f49pr_f49_capital_return_payout_yieldsource_252d_base_v109_signal(divyield, payoutratio):
    gy = _slope(divyield, 126)
    gpr = _slope(payoutratio, 126)
    result = np.sign(gy) * (gy.abs()) - np.sign(gpr) * (gpr.abs()) * 0.1
    return result.replace([np.inf, -np.inf], np.nan)


# net income coverage of total claims, smoothed (earnings safety of distributions)
def f49pr_f49_capital_return_payout_earnsafety_252d_base_v110_signal(netinc, ncfdiv, prefdivis):
    claims = ncfdiv.abs() + prefdivis.abs()
    cov = netinc / claims.replace(0, np.nan)
    result = cov.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield vs payout ratio ratio (implied earnings yield embedded in payout)
def f49pr_f49_capital_return_payout_impliedearnyield_252d_base_v111_signal(divyield, payoutratio):
    b = divyield / payoutratio.replace(0, np.nan)
    result = b.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio above earnings flag (paying out >100% of earnings), adaptive
def f49pr_f49_capital_return_payout_proverearn_252d_base_v112_signal(dps, eps):
    pr = dps / eps.replace(0, np.nan)
    thr = pr.rolling(504, min_periods=126).quantile(0.75)
    over = (pr > thr).astype(float)
    result = over.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dividend coverage trend acceleration (2nd diff of FCF coverage)
def f49pr_f49_capital_return_payout_covaccel_252d_base_v113_signal(fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv).rolling(42, min_periods=21).mean()
    result = _slope(cov, 63) - _slope(cov.shift(63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# capital-return payout ratio (cash dividends/netinc) range position
def f49pr_f49_capital_return_payout_payearnpos_504d_base_v114_signal(ncfdiv, netinc):
    pe = _f49_payout_earn(ncfdiv, netinc)
    hi = pe.rolling(504, min_periods=126).max()
    lo = pe.rolling(504, min_periods=126).min()
    result = (pe - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# blended per-share resource coverage: (fcfps + eps) per dps (total cushion behind dividend)
def f49pr_f49_capital_return_payout_cashreturnps_252d_base_v115_signal(fcfps, eps, dps):
    resources = fcfps + eps
    cov = resources / dps.replace(0, np.nan)
    result = cov.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield rank minus FCF-yield rank (relative-distribution positioning)
def f49pr_f49_capital_return_payout_yieldrankspr_504d_base_v116_signal(divyield, fcf, marketcap):
    fcfy = fcf / marketcap.replace(0, np.nan)
    result = _rank(divyield, 504) - _rank(fcfy, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# preferred-adjusted earnings payout (after senior claims) vs FCF
def f49pr_f49_capital_return_payout_prefadjpayout_252d_base_v117_signal(ncfdiv, prefdivis, netinc):
    avail = netinc - prefdivis.abs()
    b = ncfdiv.abs() / avail.replace(0, np.nan)
    result = b.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dividend dollar momentum scaled by marketcap (size-normalized growth)
def f49pr_f49_capital_return_payout_divmommc_252d_base_v118_signal(ncfdiv, marketcap):
    dmc = ncfdiv.abs() / marketcap.replace(0, np.nan)
    result = _slope(dmc.rolling(42, min_periods=21).mean(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# sustainability regime: fraction of 2yr payout-of-FCF stayed below 0.7 (safe), adaptive
def f49pr_f49_capital_return_payout_safetime_504d_base_v119_signal(ncfdiv, fcf):
    ps = _f49_payout_sustain(ncfdiv, fcf)
    thr = ps.rolling(504, min_periods=126).quantile(0.4)
    safe = (ps < thr).astype(float)
    result = safe.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# coverage stability rank (steadiest coverage = best quality), 2yr
def f49pr_f49_capital_return_payout_covstabrank_504d_base_v120_signal(fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    cv = _std(cov, 252) / _mean(cov, 252).abs().replace(0, np.nan)
    result = -_rank(cv, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# eps cushion over dps, ranked (earnings-backed dividend percentile)
def f49pr_f49_capital_return_payout_epscushrank_504d_base_v121_signal(eps, dps):
    cushion = eps / dps.replace(0, np.nan)
    result = _rank(cushion, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# dps trajectory vs eps trajectory cross (raise outpacing earnings = warning)
def f49pr_f49_capital_return_payout_raisewarning_252d_base_v122_signal(dps, eps):
    gd = (dps - dps.shift(126)) / dps.shift(126).abs().replace(0, np.nan)
    ge = (eps - eps.shift(126)) / eps.shift(126).abs().replace(0, np.nan)
    warn = (gd - ge).clip(lower=0)
    result = warn.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capital return intensity acceleration (ncfdiv/ncfo 2nd diff)
def f49pr_f49_capital_return_payout_crintensaccel_252d_base_v123_signal(ncfdiv, ncfo):
    intens = ncfdiv.abs() / ncfo.replace(0, np.nan)
    sm = intens.rolling(42, min_periods=21).mean()
    result = _slope(sm, 63) - _slope(sm.shift(63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# yield-trap depth: high-yield-percentile weighted by inverse coverage (thin = deep trap)
def f49pr_f49_capital_return_payout_trapdepth_252d_base_v124_signal(divyield, fcf, ncfdiv):
    yhi = (_rank(divyield, 504) + 0.5)
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    thin = 1.0 / (1.0 + cov.clip(lower=0))
    result = (yhi * thin).rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# distribution discipline: ncfdiv stability relative to FCF swings (smooth payer)
def f49pr_f49_capital_return_payout_discipline_504d_base_v125_signal(ncfdiv, fcf):
    div_cv = _std(ncfdiv.abs(), 252) / _mean(ncfdiv.abs(), 252).replace(0, np.nan)
    fcf_cv = _std(fcf, 252) / _mean(fcf.abs(), 252).replace(0, np.nan)
    result = fcf_cv - div_cv
    return result.replace([np.inf, -np.inf], np.nan)


# eps payout ratio momentum (accrual payout trend)
def f49pr_f49_capital_return_payout_epspayoutmom_252d_base_v126_signal(dps, eps):
    pr = dps / eps.replace(0, np.nan)
    result = _slope(pr.rolling(42, min_periods=21).mean(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield long-run anchor deviation (5yr)
def f49pr_f49_capital_return_payout_dylonganchor_1260d_base_v127_signal(divyield):
    anchor = divyield.rolling(1260, min_periods=252).mean()
    result = divyield / anchor.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# coverage by netinc vs coverage by fcf spread (accrual vs cash coverage gap)
def f49pr_f49_capital_return_payout_covsource_252d_base_v128_signal(netinc, fcf, ncfdiv):
    ecov = netinc / ncfdiv.abs().replace(0, np.nan)
    fcov = _f49_div_coverage_fcf(fcf, ncfdiv)
    result = (ecov - fcov).rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# total payout (div+pref) vs net income, smoothed (gross distribution payout)
def f49pr_f49_capital_return_payout_grosspayout_252d_base_v129_signal(ncfdiv, prefdivis, netinc):
    gross = (ncfdiv.abs() + prefdivis.abs()) / netinc.replace(0, np.nan)
    result = gross.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps payout ratio (dps/fcfps) range position over 2yr
def f49pr_f49_capital_return_payout_fcfpayoutpos_504d_base_v130_signal(dps, fcfps):
    pr = dps / fcfps.replace(0, np.nan)
    hi = pr.rolling(504, min_periods=126).max()
    lo = pr.rolling(504, min_periods=126).min()
    result = (pr - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield tanh-squashed momentum (bounded yield change)
def f49pr_f49_capital_return_payout_dytanh_252d_base_v131_signal(divyield):
    chg = _slope(divyield, 63)
    result = np.tanh(50.0 * chg)
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio vs FCF coverage interaction (high payout AND thin coverage = stress)
def f49pr_f49_capital_return_payout_prcovstress_252d_base_v132_signal(payoutratio, fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    stress = payoutratio.rolling(42, min_periods=21).mean() / (1.0 + cov.clip(lower=0))
    result = stress
    return result.replace([np.inf, -np.inf], np.nan)


# dps drawdown depth from 5yr peak (long-run dividend cut severity)
def f49pr_f49_capital_return_payout_dpsdd_1260d_base_v133_signal(dps):
    peak = dps.rolling(1260, min_periods=252).max()
    result = dps / peak.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# fcf yield momentum (cash-generation yield trajectory)
def f49pr_f49_capital_return_payout_fcfymom_252d_base_v134_signal(fcf, marketcap):
    fcfy = fcf / marketcap.replace(0, np.nan)
    result = _slope(fcfy.rolling(42, min_periods=21).mean(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# total-yield dispersion: std of (divyield, fcfyield) (mix concentration)
def f49pr_f49_capital_return_payout_yieldmixdisp_252d_base_v135_signal(divyield, fcf, marketcap):
    fcfy = fcf / marketcap.replace(0, np.nan)
    result = pd.concat([divyield, fcfy], axis=1).std(axis=1).rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# net income payout coverage z (earnings cover the cash dividend, deviation)
def f49pr_f49_capital_return_payout_earncovz_252d_base_v136_signal(netinc, ncfdiv):
    cov = netinc / ncfdiv.abs().replace(0, np.nan)
    result = _z(cov, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# preferred share of payout trend (rising senior intensity)
def f49pr_f49_capital_return_payout_prefsharemom_252d_base_v137_signal(prefdivis, ncfdiv):
    share = prefdivis.abs() / (prefdivis.abs() + ncfdiv.abs()).replace(0, np.nan)
    result = _slope(share.rolling(42, min_periods=21).mean(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# dividend growth streak length scaled (consecutive YoY raises), longer window
def f49pr_f49_capital_return_payout_growstreak_504d_base_v138_signal(dps):
    rising = (dps > dps.shift(126)).astype(float)
    streak = rising.groupby((rising == 0).cumsum()).cumsum()
    result = _z(streak, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf coverage minus eps payout (cash-vs-accrual safety composite)
def f49pr_f49_capital_return_payout_safetycomposite_252d_base_v139_signal(fcf, ncfdiv, dps, eps):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    epspay = dps / eps.replace(0, np.nan)
    result = (np.tanh(cov - 1.0) - np.tanh(epspay - 1.0)).rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capital-return yield acceleration (total dollars returned / mc, 2nd difference)
def f49pr_f49_capital_return_payout_cryieldmom_252d_base_v140_signal(ncfdiv, prefdivis, marketcap):
    cry = (ncfdiv.abs() + prefdivis.abs()) / marketcap.replace(0, np.nan)
    sm = cry.rolling(42, min_periods=21).mean()
    result = _slope(sm, 63) - _slope(sm.shift(63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# divyield percentile minus payout-ratio percentile (cheap-yield vs high-payout)
def f49pr_f49_capital_return_payout_yieldvspayout_504d_base_v141_signal(divyield, payoutratio):
    result = _rank(divyield, 504) - _rank(payoutratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps minus dps per-share buffer z-scored (per-share dividend safety)
def f49pr_f49_capital_return_payout_psbufferz_252d_base_v142_signal(fcfps, dps):
    buf = fcfps - dps
    result = _z(buf, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# payout sustainability tanh level (bounded payout-of-FCF stance)
def f49pr_f49_capital_return_payout_psusttanh_252d_base_v143_signal(ncfdiv, fcf):
    ps = _f49_payout_sustain(ncfdiv, fcf)
    result = np.tanh((ps - 1.0).rolling(63, min_periods=21).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-to-earnings vs dividend-to-fcf percentile divergence
def f49pr_f49_capital_return_payout_payrankspr_504d_base_v144_signal(ncfdiv, netinc, fcf):
    pe = _f49_payout_earn(ncfdiv, netinc)
    pf = _f49_payout_sustain(ncfdiv, fcf)
    result = _rank(pe, 504) - _rank(pf, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# eps stability behind the dividend (low eps vol = reliable payer)
def f49pr_f49_capital_return_payout_epsstab_504d_base_v145_signal(eps, dps):
    eps_cv = _std(eps, 252) / _mean(eps, 252).abs().replace(0, np.nan)
    payer = (dps > 0).astype(float)
    result = (-eps_cv) * payer.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# total payout dollars vs OCF (gross claim on operating cash)
def f49pr_f49_capital_return_payout_grossocfclaim_252d_base_v146_signal(ncfdiv, prefdivis, ncfo):
    claim = (ncfdiv.abs() + prefdivis.abs()) / ncfo.replace(0, np.nan)
    result = _z(claim, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# dividend coverage convexity: squared distance of coverage from 1.0 (deep safe/unsafe)
def f49pr_f49_capital_return_payout_covconvex_252d_base_v147_signal(fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    conv = np.sign(cov - 1.0) * (cov - 1.0) ** 2
    result = conv.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield vs its own 252d/504d crossover (short vs long yield regime)
def f49pr_f49_capital_return_payout_dycross_base_v148_signal(divyield):
    short = divyield.rolling(63, min_periods=21).mean()
    long = divyield.rolling(252, min_periods=63).mean()
    result = short / long.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# capital-return quality composite: coverage z + cushion z - payout-ratio z
def f49pr_f49_capital_return_payout_qualcomposite_252d_base_v149_signal(fcf, ncfdiv, fcfps, dps, payoutratio):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    cushion = fcfps - dps
    result = _z(cov, 252) + _z(cushion, 252) - _z(payoutratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# distress-payout combo: paying dividends while netinc declining, adaptive flag
def f49pr_f49_capital_return_payout_distresspayout_252d_base_v150_signal(netinc, ncfdiv):
    ni_decline = (netinc < netinc.rolling(252, min_periods=63).median()).astype(float)
    paying = (ncfdiv.abs() > ncfdiv.abs().rolling(252, min_periods=63).median()).astype(float)
    combo = ni_decline * paying
    result = combo.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f49pr_f49_capital_return_payout_divgrow_252d_base_v076_signal,
    f49pr_f49_capital_return_payout_divnorm_504d_base_v077_signal,
    f49pr_f49_capital_return_payout_divvol_252d_base_v078_signal,
    f49pr_f49_capital_return_payout_dydisp_252d_base_v079_signal,
    f49pr_f49_capital_return_payout_dyrangepos_504d_base_v080_signal,
    f49pr_f49_capital_return_payout_dyaccel_252d_base_v081_signal,
    f49pr_f49_capital_return_payout_dysignmag_252d_base_v082_signal,
    f49pr_f49_capital_return_payout_prrangepos_504d_base_v083_signal,
    f49pr_f49_capital_return_payout_prmom_126d_base_v084_signal,
    f49pr_f49_capital_return_payout_prrevert_504d_base_v085_signal,
    f49pr_f49_capital_return_payout_prsmooth_252d_base_v086_signal,
    f49pr_f49_capital_return_payout_dpsgrow126_base_v087_signal,
    f49pr_f49_capital_return_payout_dpsconsist_504d_base_v088_signal,
    f49pr_f49_capital_return_payout_dpslonganchor_1260d_base_v089_signal,
    f49pr_f49_capital_return_payout_dpsz_252d_base_v090_signal,
    f49pr_f49_capital_return_payout_covfcfmom_252d_base_v091_signal,
    f49pr_f49_capital_return_payout_covocfz_252d_base_v092_signal,
    f49pr_f49_capital_return_payout_covrangepos_504d_base_v093_signal,
    f49pr_f49_capital_return_payout_covdeficit_252d_base_v094_signal,
    f49pr_f49_capital_return_payout_prefgrow_252d_base_v095_signal,
    f49pr_f49_capital_return_payout_prefdragmom_252d_base_v096_signal,
    f49pr_f49_capital_return_payout_preffcf_252d_base_v097_signal,
    f49pr_f49_capital_return_payout_prefmc_252d_base_v098_signal,
    f49pr_f49_capital_return_payout_fcfpsz_252d_base_v099_signal,
    f49pr_f49_capital_return_payout_fcfpsgrow_252d_base_v100_signal,
    f49pr_f49_capital_return_payout_epsgrowvsdps_252d_base_v101_signal,
    f49pr_f49_capital_return_payout_retainedps_252d_base_v102_signal,
    f49pr_f49_capital_return_payout_covmin_252d_base_v103_signal,
    f49pr_f49_capital_return_payout_cryield_z_252d_base_v104_signal,
    f49pr_f49_capital_return_payout_psustdisp_504d_base_v105_signal,
    f49pr_f49_capital_return_payout_accrualquality_252d_base_v106_signal,
    f49pr_f49_capital_return_payout_trueresidual_252d_base_v107_signal,
    f49pr_f49_capital_return_payout_raisesource_252d_base_v108_signal,
    f49pr_f49_capital_return_payout_yieldsource_252d_base_v109_signal,
    f49pr_f49_capital_return_payout_earnsafety_252d_base_v110_signal,
    f49pr_f49_capital_return_payout_impliedearnyield_252d_base_v111_signal,
    f49pr_f49_capital_return_payout_proverearn_252d_base_v112_signal,
    f49pr_f49_capital_return_payout_covaccel_252d_base_v113_signal,
    f49pr_f49_capital_return_payout_payearnpos_504d_base_v114_signal,
    f49pr_f49_capital_return_payout_cashreturnps_252d_base_v115_signal,
    f49pr_f49_capital_return_payout_yieldrankspr_504d_base_v116_signal,
    f49pr_f49_capital_return_payout_prefadjpayout_252d_base_v117_signal,
    f49pr_f49_capital_return_payout_divmommc_252d_base_v118_signal,
    f49pr_f49_capital_return_payout_safetime_504d_base_v119_signal,
    f49pr_f49_capital_return_payout_covstabrank_504d_base_v120_signal,
    f49pr_f49_capital_return_payout_epscushrank_504d_base_v121_signal,
    f49pr_f49_capital_return_payout_raisewarning_252d_base_v122_signal,
    f49pr_f49_capital_return_payout_crintensaccel_252d_base_v123_signal,
    f49pr_f49_capital_return_payout_trapdepth_252d_base_v124_signal,
    f49pr_f49_capital_return_payout_discipline_504d_base_v125_signal,
    f49pr_f49_capital_return_payout_epspayoutmom_252d_base_v126_signal,
    f49pr_f49_capital_return_payout_dylonganchor_1260d_base_v127_signal,
    f49pr_f49_capital_return_payout_covsource_252d_base_v128_signal,
    f49pr_f49_capital_return_payout_grosspayout_252d_base_v129_signal,
    f49pr_f49_capital_return_payout_fcfpayoutpos_504d_base_v130_signal,
    f49pr_f49_capital_return_payout_dytanh_252d_base_v131_signal,
    f49pr_f49_capital_return_payout_prcovstress_252d_base_v132_signal,
    f49pr_f49_capital_return_payout_dpsdd_1260d_base_v133_signal,
    f49pr_f49_capital_return_payout_fcfymom_252d_base_v134_signal,
    f49pr_f49_capital_return_payout_yieldmixdisp_252d_base_v135_signal,
    f49pr_f49_capital_return_payout_earncovz_252d_base_v136_signal,
    f49pr_f49_capital_return_payout_prefsharemom_252d_base_v137_signal,
    f49pr_f49_capital_return_payout_growstreak_504d_base_v138_signal,
    f49pr_f49_capital_return_payout_safetycomposite_252d_base_v139_signal,
    f49pr_f49_capital_return_payout_cryieldmom_252d_base_v140_signal,
    f49pr_f49_capital_return_payout_yieldvspayout_504d_base_v141_signal,
    f49pr_f49_capital_return_payout_psbufferz_252d_base_v142_signal,
    f49pr_f49_capital_return_payout_psusttanh_252d_base_v143_signal,
    f49pr_f49_capital_return_payout_payrankspr_504d_base_v144_signal,
    f49pr_f49_capital_return_payout_epsstab_504d_base_v145_signal,
    f49pr_f49_capital_return_payout_grossocfclaim_252d_base_v146_signal,
    f49pr_f49_capital_return_payout_covconvex_252d_base_v147_signal,
    f49pr_f49_capital_return_payout_dycross_base_v148_signal,
    f49pr_f49_capital_return_payout_qualcomposite_252d_base_v149_signal,
    f49pr_f49_capital_return_payout_distresspayout_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_CAPITAL_RETURN_PAYOUT_REGISTRY_076_150 = REGISTRY


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

    dps = _fund(1, base=1.0, drift=0.01, vol=0.05).rename("dps")
    divyield = _fund(2, base=0.03, drift=0.0, vol=0.06).rename("divyield")
    payoutratio = _fund(3, base=0.5, drift=0.0, vol=0.07).rename("payoutratio")
    ncfdiv = _fund(4, base=5e7, drift=0.005, vol=0.07).rename("ncfdiv")
    prefdivis = _fund(5, base=5e6, drift=0.0, vol=0.07).rename("prefdivis")
    fcf = _fund(6, base=1.2e8, drift=0.0, vol=0.10, allow_neg=True).rename("fcf")
    ncfo = _fund(7, base=2e8, drift=0.0, vol=0.09, allow_neg=True).rename("ncfo")
    fcfps = _fund(8, base=2.0, drift=0.0, vol=0.10, allow_neg=True).rename("fcfps")
    eps = _fund(9, base=2.5, drift=0.0, vol=0.10, allow_neg=True).rename("eps")
    netinc = _fund(10, base=1.5e8, drift=0.0, vol=0.10, allow_neg=True).rename("netinc")
    marketcap = _fund(11, base=2e9, drift=0.0, vol=0.06).rename("marketcap")

    cols = {"dps": dps, "divyield": divyield, "payoutratio": payoutratio,
            "ncfdiv": ncfdiv, "prefdivis": prefdivis, "fcf": fcf, "ncfo": ncfo,
            "fcfps": fcfps, "eps": eps, "netinc": netinc, "marketcap": marketcap}

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

    print("OK f49_capital_return_payout_base_076_150_claude: %d features pass" % n_features)
