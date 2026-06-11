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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _logroc(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


# ===== folder domain primitives (working-capital & receivables quality) =====
def _f52_dso(receivables, revenue):
    return receivables / revenue.replace(0, np.nan)


def _f52_dpo(payables, cor):
    return payables / cor.replace(0, np.nan)


def _f52_ccc(receivables, revenue, payables, cor):
    return receivables / revenue.replace(0, np.nan) - payables / cor.replace(0, np.nan)


def _f52_nwc_intensity(workingcapital, revenue):
    return workingcapital / revenue.replace(0, np.nan)


def _f52_cl_cover(assetsc, liabilitiesc):
    return assetsc / liabilitiesc.replace(0, np.nan)


def _f52_defcushion(deferredrev, revenue):
    return deferredrev / revenue.replace(0, np.nan)


# ============================================================
# --- DSO extended facets (longer/alternate windows & transforms) ---
# DSO level smoothed over a month (acute collection-period level)
def f52wc_f52_working_capital_receivables_dso_21d_base_v076_signal(receivables, revenue):
    b = _mean(_f52_dso(receivables, revenue), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO z-score vs its own 126d history (faster collection-stress de-trend)
def f52wc_f52_working_capital_receivables_dsoz_126d_base_v077_signal(receivables, revenue):
    b = _z(_f52_dso(receivables, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO momentum: change in DSO over a quarter (collection-period drift)
def f52wc_f52_working_capital_receivables_dsomom_63d_base_v078_signal(receivables, revenue):
    d = _f52_dso(receivables, revenue)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO distance above its 504d minimum (how far collection has stretched off best)
def f52wc_f52_working_capital_receivables_dsooffmin_base_v079_signal(receivables, revenue):
    d = _f52_dso(receivables, revenue)
    b = d / _rmin(d, 504).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO drawup: distance below its 504d maximum (slack vs worst collection regime)
def f52wc_f52_working_capital_receivables_dsooffmax_base_v080_signal(receivables, revenue):
    d = _f52_dso(receivables, revenue)
    b = d / _rmax(d, 504).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO EMA-displacement (level minus its slow EMA — persistent collection drift)
def f52wc_f52_working_capital_receivables_dsodisp_ema_base_v081_signal(receivables, revenue):
    d = _f52_dso(receivables, revenue)
    b = d - d.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DPO extended facets ---
# DPO level smoothed over a month (acute payment-stretch level)
def f52wc_f52_working_capital_receivables_dpo_21d_base_v082_signal(payables, cor):
    b = _mean(_f52_dpo(payables, cor), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO momentum over a quarter (supplier-stretch drift)
def f52wc_f52_working_capital_receivables_dpomom_63d_base_v083_signal(payables, cor):
    d = _f52_dpo(payables, cor)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO percentile-rank vs its own 252d history (payment-stretch regime extremity)
def f52wc_f52_working_capital_receivables_dporank_252d_base_v084_signal(payables, cor):
    d = _f52_dpo(payables, cor)
    b = _rank(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO dispersion: payment-stretch volatility over a year (supplier-terms instability)
def f52wc_f52_working_capital_receivables_dpodisp_base_v085_signal(payables, cor):
    d = _f52_dpo(payables, cor)
    b = _std(d, 252) / _mean(d, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO EMA-displacement (persistent payment-stretch drift)
def f52wc_f52_working_capital_receivables_dpodisp_ema_base_v086_signal(payables, cor):
    d = _f52_dpo(payables, cor)
    b = d - d.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CCC extended facets ---
# CCC level smoothed over a month (acute net-float exposure)
def f52wc_f52_working_capital_receivables_ccc_21d_base_v087_signal(receivables, revenue, payables, cor):
    b = _mean(_f52_ccc(receivables, revenue, payables, cor), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC z-score vs its own 126d history (faster de-trend)
def f52wc_f52_working_capital_receivables_cccz_126d_base_v088_signal(receivables, revenue, payables, cor):
    b = _z(_f52_ccc(receivables, revenue, payables, cor), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC EMA-displacement (persistent drift in net conversion cycle)
def f52wc_f52_working_capital_receivables_cccdisp_ema_base_v089_signal(receivables, revenue, payables, cor):
    c = _f52_ccc(receivables, revenue, payables, cor)
    b = c - c.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC distance above its 504d minimum (worsening off best conversion cycle)
def f52wc_f52_working_capital_receivables_cccoffmin_base_v090_signal(receivables, revenue, payables, cor):
    c = _f52_ccc(receivables, revenue, payables, cor)
    b = c - _rmin(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC sign-magnitude deviation from typical (net-float extremity, compressed)
def f52wc_f52_working_capital_receivables_cccsignmag_base_v091_signal(receivables, revenue, payables, cor):
    c = _f52_ccc(receivables, revenue, payables, cor)
    dev = c - c.rolling(252, min_periods=126).mean()
    b = np.sign(dev) * (dev.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- receivables-growth divergence extended facets ---
# receivables-growth-vs-revenue-growth divergence smoothed and risk-normalized
# (sustained collection-quality drift relative to its own noise)
def f52wc_f52_working_capital_receivables_recrevdivsm_base_v092_signal(receivables, revenue):
    div = _logroc(receivables, 126) - _logroc(revenue, 126)
    sm = _mean(div, 63)
    b = sm / _std(div, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth divergence regime: fraction of year receivables outgrow revenue
def f52wc_f52_working_capital_receivables_recrevdivreg_base_v093_signal(receivables, revenue):
    div = _logroc(receivables, 63) - _logroc(revenue, 63)
    flag = (div > 0).astype(float)
    b = flag.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth divergence percentile-rank vs 504d history (divergence extremity)
def f52wc_f52_working_capital_receivables_recrevdivrank_base_v094_signal(receivables, revenue):
    div = _logroc(receivables, 126) - _logroc(revenue, 126)
    b = _rank(div, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth divergence acceleration (change-over-change in collection-quality drift)
def f52wc_f52_working_capital_receivables_recrevdivaccel_base_v095_signal(receivables, revenue):
    div = _logroc(receivables, 63) - _logroc(revenue, 63)
    b = (div - div.shift(42)) - (div.shift(42) - div.shift(84))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net-working-capital intensity extended facets ---
# NWC intensity smoothed over a month
def f52wc_f52_working_capital_receivables_nwcint_21d_base_v096_signal(workingcapital, revenue):
    b = _mean(_f52_nwc_intensity(workingcapital, revenue), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# NWC intensity z-score vs 126d history
def f52wc_f52_working_capital_receivables_nwcintz_126d_base_v097_signal(workingcapital, revenue):
    b = _z(_f52_nwc_intensity(workingcapital, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# NWC intensity EMA-displacement
def f52wc_f52_working_capital_receivables_nwcintdisp_ema_base_v098_signal(workingcapital, revenue):
    w = _f52_nwc_intensity(workingcapital, revenue)
    b = w - w.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# NWC absorbed: change in working-capital over a half-year scaled by revenue
def f52wc_f52_working_capital_receivables_nwcabsorb_126d_base_v099_signal(workingcapital, revenue):
    d = workingcapital - workingcapital.shift(126)
    b = d / revenue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# NWC-intensity regime distance: how far below its 252d median NWC/revenue sits
# (lower = moving toward supplier-funded / negative-working-capital float)
def f52wc_f52_working_capital_receivables_nwcregdist_base_v100_signal(workingcapital, revenue):
    intensity = _f52_nwc_intensity(workingcapital, revenue)
    med = intensity.rolling(252, min_periods=126).median()
    sd = intensity.rolling(252, min_periods=126).std()
    b = (med - intensity) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- current-liability coverage extended facets ---
# current ratio smoothed over a month
def f52wc_f52_working_capital_receivables_clcover_21d_base_v101_signal(assetsc, liabilitiesc):
    b = _mean(_f52_cl_cover(assetsc, liabilitiesc), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio momentum over a quarter (coverage drift)
def f52wc_f52_working_capital_receivables_clcovermom_63d_base_v102_signal(assetsc, liabilitiesc):
    cr = _f52_cl_cover(assetsc, liabilitiesc)
    b = cr - cr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio dispersion (coverage instability over a year)
def f52wc_f52_working_capital_receivables_clcoverdisp_base_v103_signal(assetsc, liabilitiesc):
    cr = _f52_cl_cover(assetsc, liabilitiesc)
    b = _std(cr, 252) / _mean(cr, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio distance below its 504d max (coverage erosion off best)
def f52wc_f52_working_capital_receivables_clcoveroffmax_base_v104_signal(assetsc, liabilitiesc):
    cr = _f52_cl_cover(assetsc, liabilitiesc)
    b = cr / _rmax(cr, 504).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weak-coverage regime: fraction of year current ratio below 1.2 (thin liquidity buffer)
def f52wc_f52_working_capital_receivables_weakcovreg_base_v105_signal(assetsc, liabilitiesc):
    cr = _f52_cl_cover(assetsc, liabilitiesc)
    flag = (cr < 1.2).astype(float)
    b = flag.rolling(252, min_periods=126).mean() + (1.2 - cr).clip(lower=0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- deferred-revenue cushion extended facets ---
# deferred-rev cushion smoothed over a month
def f52wc_f52_working_capital_receivables_defcush_21d_base_v106_signal(deferredrev, revenue):
    b = _mean(_f52_defcushion(deferredrev, revenue), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev cushion momentum over a quarter (bookings-float drift)
def f52wc_f52_working_capital_receivables_defcushmom_63d_base_v107_signal(deferredrev, revenue):
    c = _f52_defcushion(deferredrev, revenue)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev cushion distance above its 504d min (cushion build off lows)
def f52wc_f52_working_capital_receivables_defcushoffmin_base_v108_signal(deferredrev, revenue):
    c = _f52_defcushion(deferredrev, revenue)
    b = c / _rmin(c, 504).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev vs payables (customer-prepay float vs supplier-financing float)
def f52wc_f52_working_capital_receivables_defvspay_base_v109_signal(deferredrev, payables):
    r = deferredrev / payables.replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev cushion covering receivables drag (prepay offsets uncollected claims)
def f52wc_f52_working_capital_receivables_defoffrec_base_v110_signal(deferredrev, receivables):
    r = (deferredrev - receivables) / (deferredrev + receivables).replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- receivables / payables composition extended facets ---
# receivables share of current assets momentum over a quarter
def f52wc_f52_working_capital_receivables_recinassetscmom_base_v111_signal(receivables, assetsc):
    r = receivables / assetsc.replace(0, np.nan)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables share of current assets percentile-rank vs 504d history
def f52wc_f52_working_capital_receivables_recinassetscrank_base_v112_signal(receivables, assetsc):
    r = receivables / assetsc.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables share of current liabilities momentum (supplier-financing drift)
def f52wc_f52_working_capital_receivables_payinliabcmom_base_v113_signal(payables, liabilitiesc):
    r = payables / liabilitiesc.replace(0, np.nan)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-to-payables momentum over a quarter (net trade-credit drift)
def f52wc_f52_working_capital_receivables_rectopaymom_base_v114_signal(receivables, payables):
    r = receivables / payables.replace(0, np.nan)
    b = _logroc(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-to-payables percentile-rank vs 504d history (float-extension regime)
def f52wc_f52_working_capital_receivables_rectopayrank_base_v115_signal(receivables, payables):
    r = receivables / payables.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net trade credit / revenue z-score (float-intensity extremity)
def f52wc_f52_working_capital_receivables_nettradez_base_v116_signal(receivables, payables, revenue):
    nt = (receivables - payables) / revenue.replace(0, np.nan)
    b = _z(nt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net trade credit / revenue percentile-rank vs 504d history
def f52wc_f52_working_capital_receivables_nettraderank_base_v117_signal(receivables, payables, revenue):
    nt = (receivables - payables) / revenue.replace(0, np.nan)
    b = _rank(nt, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- growth-divergence & cross-line facets ---
# payables growth minus cor growth over a half-year (faster stretch divergence)
def f52wc_f52_working_capital_receivables_paycordiv_126d_base_v118_signal(payables, cor):
    b = _logroc(payables, 126) - _logroc(cor, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables growth minus current-asset growth (claims concentrating within current assets)
def f52wc_f52_working_capital_receivables_recassetcdiv_base_v119_signal(receivables, assetsc):
    b = _logroc(receivables, 252) - _logroc(assetsc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev growth minus receivables growth (prepay momentum vs collection drag)
def f52wc_f52_working_capital_receivables_defrecdiv_base_v120_signal(deferredrev, receivables):
    b = _logroc(deferredrev, 252) - _logroc(receivables, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital growth minus revenue growth (NWC build outrunning sales)
def f52wc_f52_working_capital_receivables_wcrevdiv_base_v121_signal(workingcapital, revenue):
    b = _logroc(workingcapital.abs(), 252) - _logroc(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cor growth minus revenue growth (cost base outrunning sales — margin & WC stress)
def f52wc_f52_working_capital_receivables_correvdiv_base_v122_signal(cor, revenue):
    b = _logroc(cor, 252) - _logroc(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- interaction / composite red-flag facets ---
# DSO worsening AND coverage weakening: combined liquidity-collection stress
def f52wc_f52_working_capital_receivables_stresscombo_base_v123_signal(receivables, revenue, assetsc, liabilitiesc):
    dso_chg = _f52_dso(receivables, revenue)
    dso_chg = dso_chg - dso_chg.shift(63)
    cr_chg = _f52_cl_cover(assetsc, liabilitiesc)
    cr_chg = cr_chg - cr_chg.shift(63)
    b = dso_chg.clip(lower=0) * (-cr_chg).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables float vs deferred-rev float net position (who is financing whom)
def f52wc_f52_working_capital_receivables_floatnet_base_v124_signal(receivables, deferredrev, revenue):
    net = (receivables - deferredrev) / revenue.replace(0, np.nan)
    b = _mean(net, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC scaled by NWC intensity sign (long cycle worse when WC is positive-absorbing)
def f52wc_f52_working_capital_receivables_cccnwcint_base_v125_signal(receivables, revenue, payables, cor, workingcapital):
    c = _z(_f52_ccc(receivables, revenue, payables, cor), 252)
    nwc = _z(_f52_nwc_intensity(workingcapital, revenue), 252)
    b = c + 0.5 * nwc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO per unit of coverage: collection-period normalized by current-ratio buffer
def f52wc_f52_working_capital_receivables_dsopercover_base_v126_signal(receivables, revenue, assetsc, liabilitiesc):
    d = _f52_dso(receivables, revenue)
    cr = _f52_cl_cover(assetsc, liabilitiesc)
    b = _mean(d * cr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev cushion minus payables stretch (prepay benefit net of supplier reliance)
def f52wc_f52_working_capital_receivables_cushvsstretch_base_v127_signal(deferredrev, revenue, payables, cor):
    cush = _z(_f52_defcushion(deferredrev, revenue), 252)
    dpo = _z(_f52_dpo(payables, cor), 252)
    b = cush - dpo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables intensity vs revenue scaled by collection volatility (risk-adjusted DSO)
def f52wc_f52_working_capital_receivables_dsorisk_base_v128_signal(receivables, revenue):
    d = _f52_dso(receivables, revenue)
    vol = _std(d.pct_change(), 63)
    b = _z(d, 252) / (1.0 + vol)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net trade credit absorption vs cost base: change in (receivables - payables) over cor
def f52wc_f52_working_capital_receivables_nettradeabsorbcor_base_v129_signal(receivables, payables, cor):
    nt = receivables - payables
    d = nt - nt.shift(126)
    b = d / cor.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-buffer composition: working capital funded by deferred-rev share
def f52wc_f52_working_capital_receivables_wcdeffund_base_v130_signal(deferredrev, workingcapital):
    r = deferredrev / workingcapital.replace(0, np.nan)
    b = _mean(np.sign(r) * np.log1p(r.abs()), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO streak: longest recent run of rising-DSO quarters (persistent collection lengthening)
def f52wc_f52_working_capital_receivables_dsostreak_base_v131_signal(receivables, revenue):
    d = _f52_dso(receivables, revenue)
    rising = (d > d.shift(21)).astype(float)
    b = rising.rolling(126, min_periods=63).sum() / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO streak: persistent run of rising-DPO (supplier-stretch persistence)
def f52wc_f52_working_capital_receivables_dpostreak_base_v132_signal(payables, cor):
    d = _f52_dpo(payables, cor)
    rising = (d > d.shift(21)).astype(float)
    b = rising.rolling(126, min_periods=63).sum() / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC year-over-year change (net conversion-cycle shift vs same period last year)
def f52wc_f52_working_capital_receivables_cccyoy_base_v133_signal(receivables, revenue, payables, cor):
    c = _f52_ccc(receivables, revenue, payables, cor)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO year-over-year change (collection-period shift vs same period last year)
def f52wc_f52_working_capital_receivables_dsoyoy_base_v134_signal(receivables, revenue):
    d = _f52_dso(receivables, revenue)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev cushion percentile-rank vs 252d history (bookings-float regime, faster)
def f52wc_f52_working_capital_receivables_defcushrank252_base_v135_signal(deferredrev, revenue):
    c = _f52_defcushion(deferredrev, revenue)
    b = _rank(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables share of revenue vs payables share of cor spread (gross float asymmetry)
def f52wc_f52_working_capital_receivables_floatasym_base_v136_signal(receivables, revenue, payables, cor):
    rs = receivables / revenue.replace(0, np.nan)
    ps = payables / cor.replace(0, np.nan)
    b = _z(rs, 252) - _z(ps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quick-coverage trend: (current assets - receivables)/current liabilities change
def f52wc_f52_working_capital_receivables_quickcovtrend_base_v137_signal(assetsc, receivables, liabilitiesc):
    q = (assetsc - receivables) / liabilitiesc.replace(0, np.nan)
    b = q - q.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital turnover momentum (revenue/NWC drift over a quarter)
def f52wc_f52_working_capital_receivables_wcturnmom_base_v138_signal(revenue, workingcapital):
    t = revenue / workingcapital.replace(0, np.nan)
    b = _logroc(t, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-liability intensity: current liabilities / revenue (short-term obligation load)
def f52wc_f52_working_capital_receivables_liabcint_base_v139_signal(liabilitiesc, revenue):
    r = liabilitiesc / revenue.replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-asset intensity: current assets / revenue (liquid-asset load per sale)
def f52wc_f52_working_capital_receivables_assetcint_base_v140_signal(assetsc, revenue):
    r = assetsc / revenue.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev funding ratio trend: change in deferred-rev coverage of trade float
def f52wc_f52_working_capital_receivables_deffundtrend_base_v141_signal(deferredrev, receivables, payables):
    r = deferredrev / (receivables + payables).replace(0, np.nan)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC short-vs-long ratio scaled (relative acceleration of conversion cycle)
def f52wc_f52_working_capital_receivables_cccslratio_base_v142_signal(receivables, revenue, payables, cor):
    c = _f52_ccc(receivables, revenue, payables, cor)
    short = _mean(c, 21)
    long = _mean(c, 252)
    b = (short - long) / (c.rolling(252, min_periods=126).std()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables build velocity scaled by revenue (uncollected-claims accumulation rate)
def f52wc_f52_working_capital_receivables_recbuildvel_base_v143_signal(receivables, revenue):
    d = receivables - receivables.shift(63)
    b = d / revenue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables build velocity scaled by cor (supplier-financing accumulation rate)
def f52wc_f52_working_capital_receivables_paybuildvel_base_v144_signal(payables, cor):
    d = payables - payables.shift(63)
    b = d / cor.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-float regime distance: CCC distance from its own 252d median in std units
def f52wc_f52_working_capital_receivables_cccregdist_base_v145_signal(receivables, revenue, payables, cor):
    c = _f52_ccc(receivables, revenue, payables, cor)
    med = c.rolling(252, min_periods=126).median()
    sd = c.rolling(252, min_periods=126).std()
    b = (c - med) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev cushion dispersion (bookings-float instability over a year)
def f52wc_f52_working_capital_receivables_defcushdisp_base_v146_signal(deferredrev, revenue):
    c = _f52_defcushion(deferredrev, revenue)
    b = _std(c, 252) / _mean(c, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-to-revenue vs receivables-to-current-assets spread (denominator-sensitivity)
def f52wc_f52_working_capital_receivables_recdenomspr_base_v147_signal(receivables, revenue, assetsc):
    a = receivables / revenue.replace(0, np.nan)
    bb = receivables / assetsc.replace(0, np.nan)
    b = _z(a, 252) - _z(bb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite collection-quality score: rec/rev-growth-divergence regime weighted by DSO rank
def f52wc_f52_working_capital_receivables_collqual_base_v148_signal(receivables, revenue):
    div = _logroc(receivables, 126) - _logroc(revenue, 126)
    div_reg = (div > 0).astype(float).rolling(252, min_periods=126).mean()
    dso_rank = _rank(_f52_dso(receivables, revenue), 504)
    b = div_reg * (0.5 + dso_rank)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# supplier-vs-customer financing balance trend: change in (DPO - DSO) over a half-year
# (net trade-credit advantage building or eroding)
def f52wc_f52_working_capital_receivables_tradebaltrend_base_v149_signal(payables, cor, receivables, revenue):
    bal = _f52_dpo(payables, cor) - _f52_dso(receivables, revenue)
    b = bal - bal.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital quality composite: coverage-z + deferred-cushion-z - NWC-intensity-z
def f52wc_f52_working_capital_receivables_wcqual_base_v150_signal(assetsc, liabilitiesc, deferredrev, revenue, workingcapital):
    cov_z = _z(_f52_cl_cover(assetsc, liabilitiesc), 252)
    cush_z = _z(_f52_defcushion(deferredrev, revenue), 252)
    nwc_z = _z(_f52_nwc_intensity(workingcapital, revenue), 252)
    b = cov_z + cush_z - 0.5 * nwc_z
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f52wc_f52_working_capital_receivables_dso_21d_base_v076_signal,
    f52wc_f52_working_capital_receivables_dsoz_126d_base_v077_signal,
    f52wc_f52_working_capital_receivables_dsomom_63d_base_v078_signal,
    f52wc_f52_working_capital_receivables_dsooffmin_base_v079_signal,
    f52wc_f52_working_capital_receivables_dsooffmax_base_v080_signal,
    f52wc_f52_working_capital_receivables_dsodisp_ema_base_v081_signal,
    f52wc_f52_working_capital_receivables_dpo_21d_base_v082_signal,
    f52wc_f52_working_capital_receivables_dpomom_63d_base_v083_signal,
    f52wc_f52_working_capital_receivables_dporank_252d_base_v084_signal,
    f52wc_f52_working_capital_receivables_dpodisp_base_v085_signal,
    f52wc_f52_working_capital_receivables_dpodisp_ema_base_v086_signal,
    f52wc_f52_working_capital_receivables_ccc_21d_base_v087_signal,
    f52wc_f52_working_capital_receivables_cccz_126d_base_v088_signal,
    f52wc_f52_working_capital_receivables_cccdisp_ema_base_v089_signal,
    f52wc_f52_working_capital_receivables_cccoffmin_base_v090_signal,
    f52wc_f52_working_capital_receivables_cccsignmag_base_v091_signal,
    f52wc_f52_working_capital_receivables_recrevdivsm_base_v092_signal,
    f52wc_f52_working_capital_receivables_recrevdivreg_base_v093_signal,
    f52wc_f52_working_capital_receivables_recrevdivrank_base_v094_signal,
    f52wc_f52_working_capital_receivables_recrevdivaccel_base_v095_signal,
    f52wc_f52_working_capital_receivables_nwcint_21d_base_v096_signal,
    f52wc_f52_working_capital_receivables_nwcintz_126d_base_v097_signal,
    f52wc_f52_working_capital_receivables_nwcintdisp_ema_base_v098_signal,
    f52wc_f52_working_capital_receivables_nwcabsorb_126d_base_v099_signal,
    f52wc_f52_working_capital_receivables_nwcregdist_base_v100_signal,
    f52wc_f52_working_capital_receivables_clcover_21d_base_v101_signal,
    f52wc_f52_working_capital_receivables_clcovermom_63d_base_v102_signal,
    f52wc_f52_working_capital_receivables_clcoverdisp_base_v103_signal,
    f52wc_f52_working_capital_receivables_clcoveroffmax_base_v104_signal,
    f52wc_f52_working_capital_receivables_weakcovreg_base_v105_signal,
    f52wc_f52_working_capital_receivables_defcush_21d_base_v106_signal,
    f52wc_f52_working_capital_receivables_defcushmom_63d_base_v107_signal,
    f52wc_f52_working_capital_receivables_defcushoffmin_base_v108_signal,
    f52wc_f52_working_capital_receivables_defvspay_base_v109_signal,
    f52wc_f52_working_capital_receivables_defoffrec_base_v110_signal,
    f52wc_f52_working_capital_receivables_recinassetscmom_base_v111_signal,
    f52wc_f52_working_capital_receivables_recinassetscrank_base_v112_signal,
    f52wc_f52_working_capital_receivables_payinliabcmom_base_v113_signal,
    f52wc_f52_working_capital_receivables_rectopaymom_base_v114_signal,
    f52wc_f52_working_capital_receivables_rectopayrank_base_v115_signal,
    f52wc_f52_working_capital_receivables_nettradez_base_v116_signal,
    f52wc_f52_working_capital_receivables_nettraderank_base_v117_signal,
    f52wc_f52_working_capital_receivables_paycordiv_126d_base_v118_signal,
    f52wc_f52_working_capital_receivables_recassetcdiv_base_v119_signal,
    f52wc_f52_working_capital_receivables_defrecdiv_base_v120_signal,
    f52wc_f52_working_capital_receivables_wcrevdiv_base_v121_signal,
    f52wc_f52_working_capital_receivables_correvdiv_base_v122_signal,
    f52wc_f52_working_capital_receivables_stresscombo_base_v123_signal,
    f52wc_f52_working_capital_receivables_floatnet_base_v124_signal,
    f52wc_f52_working_capital_receivables_cccnwcint_base_v125_signal,
    f52wc_f52_working_capital_receivables_dsopercover_base_v126_signal,
    f52wc_f52_working_capital_receivables_cushvsstretch_base_v127_signal,
    f52wc_f52_working_capital_receivables_dsorisk_base_v128_signal,
    f52wc_f52_working_capital_receivables_nettradeabsorbcor_base_v129_signal,
    f52wc_f52_working_capital_receivables_wcdeffund_base_v130_signal,
    f52wc_f52_working_capital_receivables_dsostreak_base_v131_signal,
    f52wc_f52_working_capital_receivables_dpostreak_base_v132_signal,
    f52wc_f52_working_capital_receivables_cccyoy_base_v133_signal,
    f52wc_f52_working_capital_receivables_dsoyoy_base_v134_signal,
    f52wc_f52_working_capital_receivables_defcushrank252_base_v135_signal,
    f52wc_f52_working_capital_receivables_floatasym_base_v136_signal,
    f52wc_f52_working_capital_receivables_quickcovtrend_base_v137_signal,
    f52wc_f52_working_capital_receivables_wcturnmom_base_v138_signal,
    f52wc_f52_working_capital_receivables_liabcint_base_v139_signal,
    f52wc_f52_working_capital_receivables_assetcint_base_v140_signal,
    f52wc_f52_working_capital_receivables_deffundtrend_base_v141_signal,
    f52wc_f52_working_capital_receivables_cccslratio_base_v142_signal,
    f52wc_f52_working_capital_receivables_recbuildvel_base_v143_signal,
    f52wc_f52_working_capital_receivables_paybuildvel_base_v144_signal,
    f52wc_f52_working_capital_receivables_cccregdist_base_v145_signal,
    f52wc_f52_working_capital_receivables_defcushdisp_base_v146_signal,
    f52wc_f52_working_capital_receivables_recdenomspr_base_v147_signal,
    f52wc_f52_working_capital_receivables_collqual_base_v148_signal,
    f52wc_f52_working_capital_receivables_tradebaltrend_base_v149_signal,
    f52wc_f52_working_capital_receivables_wcqual_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F52_WORKING_CAPITAL_RECEIVABLES_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    receivables = _fund(201, base=8e7, drift=0.030, vol=0.07).rename("receivables")
    payables = _fund(202, base=5e7, drift=0.025, vol=0.08).rename("payables")
    deferredrev = _fund(203, base=4e7, drift=0.035, vol=0.09).rename("deferredrev")
    workingcapital = _fund(204, base=6e7, drift=0.015, vol=0.10, allow_neg=True).rename("workingcapital")
    liabilitiesc = _fund(205, base=1.1e8, drift=0.022, vol=0.06).rename("liabilitiesc")
    assetsc = _fund(206, base=1.7e8, drift=0.024, vol=0.05).rename("assetsc")
    revenue = _fund(207, base=3e8, drift=0.028, vol=0.06).rename("revenue")
    cor = _fund(208, base=1.8e8, drift=0.026, vol=0.07).rename("cor")

    cols = {
        "receivables": receivables, "payables": payables, "deferredrev": deferredrev,
        "workingcapital": workingcapital, "liabilitiesc": liabilitiesc, "assetsc": assetsc,
        "revenue": revenue, "cor": cor,
    }

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi",
        "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas", "shareswa",
        "shareswadil", "assets", "assetsc", "tangibles", "intangibles", "ppnenet",
        "investments", "inventory", "receivables", "payables", "equity", "retearn",
        "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
        "cashneq", "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap",
        "intexp", "taxexp", "ebt", "sps", "bvps", "tbvps", "de", "ncfdiv", "ncfinv", "dps",
        "divyield", "payoutratio", "prefdivis", "netincdis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal", "fndholders",
        "undholders", "prfholders", "dbtholders", "putholders", "putvalue", "cllholders",
        "cllvalue", "wntholders", "wntvalue", "dbtvalue", "fndvalue", "undvalue", "prfvalue",
        "fndunits", "undunits",
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (name, meta["inputs"])
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

    print("OK f52_working_capital_receivables_base_076_150_claude: %d features pass" % n_features)
