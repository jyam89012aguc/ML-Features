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
# DSO proxy: receivables / revenue (days-sales-outstanding, revenue is a flow proxy)
def _f52_dso(receivables, revenue):
    return receivables / revenue.replace(0, np.nan)


# DPO proxy: payables / cost-of-revenue (days-payable-outstanding)
def _f52_dpo(payables, cor):
    return payables / cor.replace(0, np.nan)


# DIO-light not available (no inventory in domain); cash-conversion = DSO - DPO
def _f52_ccc(receivables, revenue, payables, cor):
    return receivables / revenue.replace(0, np.nan) - payables / cor.replace(0, np.nan)


# net-working-capital intensity: workingcapital / revenue
def _f52_nwc_intensity(workingcapital, revenue):
    return workingcapital / revenue.replace(0, np.nan)


# current-liability coverage: current assets / current liabilities
def _f52_cl_cover(assetsc, liabilitiesc):
    return assetsc / liabilitiesc.replace(0, np.nan)


# deferred-revenue cushion: deferredrev / revenue (bookings float vs revenue)
def _f52_defcushion(deferredrev, revenue):
    return deferredrev / revenue.replace(0, np.nan)


# receivables intensity vs current assets (composition of liquid claims)
def _f52_rec_in_assetsc(receivables, assetsc):
    return receivables / assetsc.replace(0, np.nan)


# payables share of current liabilities (supplier-financing reliance)
def _f52_pay_in_liabc(payables, liabilitiesc):
    return payables / liabilitiesc.replace(0, np.nan)


# ============================================================
# --- DSO level family (receivables/revenue) ---
# DSO level smoothed over a quarter (collection-period level)
def f52wc_f52_working_capital_receivables_dso_63d_base_v001_signal(receivables, revenue):
    b = _mean(_f52_dso(receivables, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO z-score vs its own 252d history (de-trended collection stress)
def f52wc_f52_working_capital_receivables_dsoz_252d_base_v002_signal(receivables, revenue):
    b = _z(_f52_dso(receivables, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO percentile-rank vs its own 504d history (regime extremity)
def f52wc_f52_working_capital_receivables_dsorank_504d_base_v003_signal(receivables, revenue):
    b = _rank(_f52_dso(receivables, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO trend: log-change of DSO over a half-year (lengthening collection cycle)
def f52wc_f52_working_capital_receivables_dsotrend_126d_base_v004_signal(receivables, revenue):
    b = _logroc(_f52_dso(receivables, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO short-vs-long ratio (63d DSO mean vs 252d DSO mean — acute deterioration)
def f52wc_f52_working_capital_receivables_dsoslr_base_v005_signal(receivables, revenue):
    d = _f52_dso(receivables, revenue)
    b = _mean(d, 63) / _mean(d, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO dispersion: rolling std of DSO over a year (collection-period instability)
def f52wc_f52_working_capital_receivables_dsodisp_252d_base_v006_signal(receivables, revenue):
    d = _f52_dso(receivables, revenue)
    b = _std(d, 252) / _mean(d, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- receivables-growth-vs-revenue-growth divergence (collection-quality red flag) ---
# receivables YoY growth minus revenue YoY growth (adtech float red flag)
def f52wc_f52_working_capital_receivables_recrevdiv_252d_base_v007_signal(receivables, revenue):
    b = _logroc(receivables, 252) - _logroc(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth-vs-revenue-growth divergence, dispersion-normalized over a year
# (collection-quality red flag scaled by how noisy the divergence usually is)
def f52wc_f52_working_capital_receivables_recrevdivsn_126d_base_v008_signal(receivables, revenue):
    div = _logroc(receivables, 63) - _logroc(revenue, 63)
    b = div / _std(div, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divergence ratio: receivables-growth / revenue-growth (>1 = receivables outrunning sales)
def f52wc_f52_working_capital_receivables_recrevratio_252d_base_v009_signal(receivables, revenue):
    rg = _roc(receivables, 252)
    sg = _roc(revenue, 252)
    b = (rg - sg) / (sg.abs() + 0.05)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-scored receivables/revenue-growth divergence vs its own history
def f52wc_f52_working_capital_receivables_recrevdivz_base_v010_signal(receivables, revenue):
    div = _logroc(receivables, 126) - _logroc(revenue, 126)
    b = _z(div, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# --- DPO level family (payables/cor) ---
# DPO level smoothed over a quarter (payment-stretch level)
def f52wc_f52_working_capital_receivables_dpo_63d_base_v011_signal(payables, cor):
    b = _mean(_f52_dpo(payables, cor), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO z-score vs its own 252d history (stretch extremity)
def f52wc_f52_working_capital_receivables_dpoz_252d_base_v012_signal(payables, cor):
    b = _z(_f52_dpo(payables, cor), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO percentile-rank vs its own 504d history
def f52wc_f52_working_capital_receivables_dporank_504d_base_v013_signal(payables, cor):
    b = _rank(_f52_dpo(payables, cor), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables-stretch trend: log-change of DPO over a half-year (stretching suppliers)
def f52wc_f52_working_capital_receivables_dpotrend_126d_base_v014_signal(payables, cor):
    b = _logroc(_f52_dpo(payables, cor), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO short-vs-long ratio (acute payment stretch)
def f52wc_f52_working_capital_receivables_dposlr_base_v015_signal(payables, cor):
    d = _f52_dpo(payables, cor)
    b = _mean(d, 63) / _mean(d, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables growth minus cor growth (stretching beyond purchasing growth)
def f52wc_f52_working_capital_receivables_paycordiv_252d_base_v016_signal(payables, cor):
    b = _logroc(payables, 252) - _logroc(cor, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cash-conversion cycle (DSO - DPO) ---
# CCC level smoothed over a quarter (net float exposure)
def f52wc_f52_working_capital_receivables_ccc_63d_base_v017_signal(receivables, revenue, payables, cor):
    b = _mean(_f52_ccc(receivables, revenue, payables, cor), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC z-score vs its own 252d history
def f52wc_f52_working_capital_receivables_cccz_252d_base_v018_signal(receivables, revenue, payables, cor):
    b = _z(_f52_ccc(receivables, revenue, payables, cor), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC trend over a half-year (worsening conversion cycle)
def f52wc_f52_working_capital_receivables_ccctrend_126d_base_v019_signal(receivables, revenue, payables, cor):
    c = _f52_ccc(receivables, revenue, payables, cor)
    b = c - c.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC percentile-rank vs its own 504d history (regime extremity)
def f52wc_f52_working_capital_receivables_cccrank_504d_base_v020_signal(receivables, revenue, payables, cor):
    b = _rank(_f52_ccc(receivables, revenue, payables, cor), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC short-vs-long change (acute shift in net working-capital cycle)
def f52wc_f52_working_capital_receivables_cccslr_base_v021_signal(receivables, revenue, payables, cor):
    c = _f52_ccc(receivables, revenue, payables, cor)
    b = _mean(c, 42) - _mean(c, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO/DPO ratio short-vs-long spread (acute shift in collection-vs-payment balance)
def f52wc_f52_working_capital_receivables_dsodporatioslr_base_v022_signal(receivables, revenue, payables, cor):
    d = _f52_dso(receivables, revenue) / _f52_dpo(payables, cor).replace(0, np.nan)
    b = _mean(d, 42) / _mean(d, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO/DPO ratio dispersion: instability of the collection-vs-payment balance over a year
def f52wc_f52_working_capital_receivables_dsodporatiodisp_base_v023_signal(receivables, revenue, payables, cor):
    d = _f52_dso(receivables, revenue) / _f52_dpo(payables, cor).replace(0, np.nan)
    b = _std(d, 252) / _mean(d, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net-working-capital intensity / revenue ---
# NWC intensity level smoothed (working-capital absorbed per dollar of sales)
def f52wc_f52_working_capital_receivables_nwcint_63d_base_v024_signal(workingcapital, revenue):
    b = _mean(_f52_nwc_intensity(workingcapital, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# NWC intensity z-score vs its own 252d history
def f52wc_f52_working_capital_receivables_nwcintz_252d_base_v025_signal(workingcapital, revenue):
    b = _z(_f52_nwc_intensity(workingcapital, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# NWC intensity trend (building/releasing working capital relative to sales)
def f52wc_f52_working_capital_receivables_nwcinttrend_126d_base_v026_signal(workingcapital, revenue):
    w = _f52_nwc_intensity(workingcapital, revenue)
    b = w - w.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# NWC intensity percentile-rank vs 504d history
def f52wc_f52_working_capital_receivables_nwcintrank_504d_base_v027_signal(workingcapital, revenue):
    b = _rank(_f52_nwc_intensity(workingcapital, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign of working capital weighted by magnitude/revenue (negative-NWC float regime)
def f52wc_f52_working_capital_receivables_nwcsign_base_v028_signal(workingcapital, revenue):
    w = _f52_nwc_intensity(workingcapital, revenue)
    b = np.sign(w) * (w.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- current-liability coverage (assetsc / liabilitiesc) ---
# current ratio level smoothed (liquidity buffer)
def f52wc_f52_working_capital_receivables_clcover_63d_base_v029_signal(assetsc, liabilitiesc):
    b = _mean(_f52_cl_cover(assetsc, liabilitiesc), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio z-score vs its own 252d history (liquidity-stress de-trend)
def f52wc_f52_working_capital_receivables_clcoverz_252d_base_v030_signal(assetsc, liabilitiesc):
    b = _z(_f52_cl_cover(assetsc, liabilitiesc), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio trend (deteriorating short-term coverage)
def f52wc_f52_working_capital_receivables_clcovertrend_126d_base_v031_signal(assetsc, liabilitiesc):
    b = _logroc(_f52_cl_cover(assetsc, liabilitiesc), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio percentile-rank vs 504d history
def f52wc_f52_working_capital_receivables_clcoverrank_504d_base_v032_signal(assetsc, liabilitiesc):
    b = _rank(_f52_cl_cover(assetsc, liabilitiesc), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quick-coverage proxy: (current assets minus receivables) / current liabilities
def f52wc_f52_working_capital_receivables_quickcover_63d_base_v033_signal(assetsc, receivables, liabilitiesc):
    q = (assetsc - receivables) / liabilitiesc.replace(0, np.nan)
    b = _mean(q, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of current ratio below the 1.0 solvency threshold (coverage shortfall)
def f52wc_f52_working_capital_receivables_clshortfall_base_v034_signal(assetsc, liabilitiesc):
    cr = _f52_cl_cover(assetsc, liabilitiesc)
    b = (1.0 - cr).clip(lower=0).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- deferred-revenue cushion (deferredrev / revenue) ---
# deferred-rev cushion level smoothed (bookings float vs revenue)
def f52wc_f52_working_capital_receivables_defcush_63d_base_v035_signal(deferredrev, revenue):
    b = _mean(_f52_defcushion(deferredrev, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev cushion z-score vs 252d history
def f52wc_f52_working_capital_receivables_defcushz_252d_base_v036_signal(deferredrev, revenue):
    b = _z(_f52_defcushion(deferredrev, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev vs receivables (customer-prepay float vs customer-owed float)
def f52wc_f52_working_capital_receivables_defvsrec_63d_base_v037_signal(deferredrev, receivables):
    r = deferredrev / receivables.replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev cushion offsetting current liabilities (prepay funding of obligations)
def f52wc_f52_working_capital_receivables_deflcover_63d_base_v038_signal(deferredrev, liabilitiesc):
    r = deferredrev / liabilitiesc.replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- receivables composition / float intensity ---
# receivables as share of current assets, level (claims composition)
def f52wc_f52_working_capital_receivables_recinassetsc_63d_base_v039_signal(receivables, assetsc):
    b = _mean(_f52_rec_in_assetsc(receivables, assetsc), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables share of current assets z-score (concentration in uncollected claims)
def f52wc_f52_working_capital_receivables_recinassetscz_base_v040_signal(receivables, assetsc):
    b = _z(_f52_rec_in_assetsc(receivables, assetsc), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables share trend (rising claim concentration — collection-quality risk)
def f52wc_f52_working_capital_receivables_recinassetsctrend_base_v041_signal(receivables, assetsc):
    r = _f52_rec_in_assetsc(receivables, assetsc)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables share of current liabilities, level (supplier-financing reliance)
def f52wc_f52_working_capital_receivables_payinliabc_63d_base_v042_signal(payables, liabilitiesc):
    b = _mean(_f52_pay_in_liabc(payables, liabilitiesc), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables share of current liabilities z-score
def f52wc_f52_working_capital_receivables_payinliabcz_base_v043_signal(payables, liabilitiesc):
    b = _z(_f52_pay_in_liabc(payables, liabilitiesc), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-to-payables balance (net trade-credit position — adtech agency float)
def f52wc_f52_working_capital_receivables_rectopay_63d_base_v044_signal(receivables, payables):
    r = receivables / payables.replace(0, np.nan)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-to-payables z-score (net float-extension extremity)
def f52wc_f52_working_capital_receivables_rectopayz_base_v045_signal(receivables, payables):
    r = receivables / payables.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net trade credit / revenue: (receivables - payables) / revenue (float intensity)
def f52wc_f52_working_capital_receivables_nettradeint_63d_base_v046_signal(receivables, payables, revenue):
    nt = (receivables - payables) / revenue.replace(0, np.nan)
    b = _mean(nt, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net trade credit / revenue trend (float build-up vs sales)
def f52wc_f52_working_capital_receivables_nettradetrend_base_v047_signal(receivables, payables, revenue):
    nt = (receivables - payables) / revenue.replace(0, np.nan)
    b = nt - nt.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- receivables-turnover facets (structurally distinct from DSO level) ---
# receivables-turnover acceleration: change in collection efficiency, change-over-change
def f52wc_f52_working_capital_receivables_recturnaccel_base_v048_signal(revenue, receivables):
    t = revenue / receivables.replace(0, np.nan)
    b = (t - t.shift(42)) - (t.shift(42) - t.shift(84))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables-turnover dispersion: supplier-payment-efficiency volatility over a year
def f52wc_f52_working_capital_receivables_payturndisp_base_v049_signal(cor, payables):
    t = cor / payables.replace(0, np.nan)
    b = _std(t, 252) / _mean(t, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables-turnover gap vs receivables-turnover (supplier vs customer cash-cycle balance)
def f52wc_f52_working_capital_receivables_turngap_base_v050_signal(cor, payables, revenue, receivables):
    pt = cor / payables.replace(0, np.nan)
    rt = revenue / receivables.replace(0, np.nan)
    b = _z(pt, 252) - _z(rt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital turnover: revenue / working-capital (sales generated per NWC dollar)
def f52wc_f52_working_capital_receivables_wcturn_63d_base_v051_signal(revenue, workingcapital):
    t = revenue / workingcapital.replace(0, np.nan)
    b = _mean(t, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital turnover regime: fraction of year revenue/NWC sits above its 252d median
def f52wc_f52_working_capital_receivables_wcturnreg_base_v052_signal(revenue, workingcapital):
    t = revenue / workingcapital.replace(0, np.nan)
    med = t.rolling(252, min_periods=126).median()
    above = (t > med).astype(float)
    b = above.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- interaction / combined red-flag features ---
# DSO rising while turnover falling: red-flag interaction (collection deterioration)
def f52wc_f52_working_capital_receivables_dsoredflag_base_v053_signal(receivables, revenue):
    d = _f52_dso(receivables, revenue)
    dso_chg = d - d.shift(63)
    rec_g = _roc(receivables, 63)
    b = dso_chg * rec_g.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# float quality: deferred-rev cushion minus DSO (prepay float net of collection drag)
def f52wc_f52_working_capital_receivables_floatquality_base_v054_signal(deferredrev, revenue, receivables):
    b = _mean(_f52_defcushion(deferredrev, revenue) - _f52_dso(receivables, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC tanh-squashed momentum (bounded change in conversion cycle)
def f52wc_f52_working_capital_receivables_ccctanh_base_v055_signal(receivables, revenue, payables, cor):
    c = _f52_ccc(receivables, revenue, payables, cor)
    b = np.tanh(3.0 * (c - c.shift(63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO acceleration regime: count of quarters DSO above its 252d median (stress persistence)
def f52wc_f52_working_capital_receivables_dsostress_base_v056_signal(receivables, revenue):
    d = _f52_dso(receivables, revenue)
    med = d.rolling(252, min_periods=126).median()
    above = (d > med).astype(float)
    b = above.rolling(126, min_periods=63).mean() + 0.5 * _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables-stretch regime persistence (fraction of year DPO above 252d median)
def f52wc_f52_working_capital_receivables_dpostretchreg_base_v057_signal(payables, cor):
    d = _f52_dpo(payables, cor)
    med = d.rolling(252, min_periods=126).median()
    above = (d > med).astype(float)
    b = above.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital absorption: change in NWC scaled by revenue (cash tied up in WC)
def f52wc_f52_working_capital_receivables_wcabsorb_base_v058_signal(workingcapital, revenue):
    dnwc = workingcapital - workingcapital.shift(63)
    b = dnwc / revenue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables build relative to deferred-rev build (collection drag vs prepay benefit)
def f52wc_f52_working_capital_receivables_recvsdefbuild_base_v059_signal(receivables, deferredrev):
    b = _logroc(receivables, 126) - _logroc(deferredrev, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-headroom build vs revenue growth: is the WC buffer growing faster than sales?
def f52wc_f52_working_capital_receivables_liqheadgrow_base_v060_signal(assetsc, liabilitiesc, revenue):
    h = (assetsc - liabilitiesc)
    b = _logroc(h, 252) - _logroc(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO vs current-ratio interaction (collection stress amid weak coverage)
def f52wc_f52_working_capital_receivables_dsoclint_base_v061_signal(receivables, revenue, assetsc, liabilitiesc):
    dso_z = _z(_f52_dso(receivables, revenue), 252)
    cl_z = _z(_f52_cl_cover(assetsc, liabilitiesc), 252)
    b = dso_z - cl_z
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-working-capital composition trend: change in (receivables - payables)/current-assets
# (shifting balance between customer-owed and supplier-owed claims)
def f52wc_f52_working_capital_receivables_nwccomptrend_base_v062_signal(receivables, payables, assetsc):
    r = (receivables - payables) / assetsc.replace(0, np.nan)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev cushion percentile-rank vs 504d history (bookings-float regime)
def f52wc_f52_working_capital_receivables_defcushrank_base_v063_signal(deferredrev, revenue):
    b = _rank(_f52_defcushion(deferredrev, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables / revenue acceleration over a quarter (collection-period inflection)
def f52wc_f52_working_capital_receivables_dsoaccel_base_v064_signal(receivables, revenue):
    d = _f52_dso(receivables, revenue)
    b = (d - d.shift(63)) - (d.shift(63) - d.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables / cor acceleration over a quarter (stretch inflection)
def f52wc_f52_working_capital_receivables_dpoaccel_base_v065_signal(payables, cor):
    d = _f52_dpo(payables, cor)
    b = (d - d.shift(63)) - (d.shift(63) - d.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trade-credit float vs current liabilities, z-scored (net funding-gap extremity)
def f52wc_f52_working_capital_receivables_floatgapz_base_v066_signal(receivables, payables, liabilitiesc):
    g = (receivables - payables) / liabilitiesc.replace(0, np.nan)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO sign-magnitude deviation from 252d typical (collection extremity, compressed)
def f52wc_f52_working_capital_receivables_dsosignmag_base_v067_signal(receivables, revenue):
    d = _f52_dso(receivables, revenue)
    dev = d - d.rolling(252, min_periods=126).mean()
    b = np.sign(dev) * (dev.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth minus current-liability growth (sales outpacing short-term obligations)
def f52wc_f52_working_capital_receivables_revliabcgrow_base_v068_signal(revenue, liabilitiesc):
    b = _logroc(revenue, 252) - _logroc(liabilitiesc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-asset-quality regime: fraction of year non-receivable share sits above 252d median
def f52wc_f52_working_capital_receivables_caqualityreg_base_v069_signal(assetsc, receivables):
    q = (assetsc - receivables) / assetsc.replace(0, np.nan)
    med = q.rolling(252, min_periods=126).median()
    above = (q > med).astype(float)
    b = above.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC dispersion (instability of net conversion cycle over a year)
def f52wc_f52_working_capital_receivables_cccdisp_base_v070_signal(receivables, revenue, payables, cor):
    c = _f52_ccc(receivables, revenue, payables, cor)
    b = _std(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-float exposure vs coverage interaction: CCC z-score scaled down when coverage is strong
# (red flag = long conversion cycle AND weak current-ratio buffer)
def f52wc_f52_working_capital_receivables_floatcover_base_v071_signal(receivables, revenue, payables, cor, assetsc, liabilitiesc):
    ccc_z = _z(_f52_ccc(receivables, revenue, payables, cor), 252)
    cl_z = _z(_f52_cl_cover(assetsc, liabilitiesc), 252)
    b = ccc_z * (1.0 - np.tanh(cl_z))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev cushion acceleration (change-over-change in bookings-float intensity)
def f52wc_f52_working_capital_receivables_defcushaccel_base_v072_signal(deferredrev, revenue):
    c = _f52_defcushion(deferredrev, revenue)
    b = (c - c.shift(63)) - (c.shift(63) - c.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital intensity acceleration (change-over-change in NWC absorbed per sale)
def f52wc_f52_working_capital_receivables_nwcintaccel_base_v073_signal(workingcapital, revenue):
    w = _f52_nwc_intensity(workingcapital, revenue)
    b = (w - w.shift(42)) - (w.shift(42) - w.shift(84))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion-cycle vs deferred-rev cushion interaction (net float net of prepay funding)
def f52wc_f52_working_capital_receivables_cccdefint_base_v074_signal(receivables, revenue, payables, cor, deferredrev):
    ccc_z = _z(_f52_ccc(receivables, revenue, payables, cor), 252)
    cush_z = _z(_f52_defcushion(deferredrev, revenue), 252)
    b = ccc_z * np.sign(cush_z) - cush_z
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite float-risk score: DSO-z plus rec/rev divergence minus deferred cushion-z
def f52wc_f52_working_capital_receivables_floatrisk_base_v075_signal(receivables, revenue, deferredrev):
    dso_z = _z(_f52_dso(receivables, revenue), 252)
    div = _z(_logroc(receivables, 126) - _logroc(revenue, 126), 252)
    cush_z = _z(_f52_defcushion(deferredrev, revenue), 252)
    b = dso_z + div - cush_z
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f52wc_f52_working_capital_receivables_dso_63d_base_v001_signal,
    f52wc_f52_working_capital_receivables_dsoz_252d_base_v002_signal,
    f52wc_f52_working_capital_receivables_dsorank_504d_base_v003_signal,
    f52wc_f52_working_capital_receivables_dsotrend_126d_base_v004_signal,
    f52wc_f52_working_capital_receivables_dsoslr_base_v005_signal,
    f52wc_f52_working_capital_receivables_dsodisp_252d_base_v006_signal,
    f52wc_f52_working_capital_receivables_recrevdiv_252d_base_v007_signal,
    f52wc_f52_working_capital_receivables_recrevdivsn_126d_base_v008_signal,
    f52wc_f52_working_capital_receivables_recrevratio_252d_base_v009_signal,
    f52wc_f52_working_capital_receivables_recrevdivz_base_v010_signal,
    f52wc_f52_working_capital_receivables_dpo_63d_base_v011_signal,
    f52wc_f52_working_capital_receivables_dpoz_252d_base_v012_signal,
    f52wc_f52_working_capital_receivables_dporank_504d_base_v013_signal,
    f52wc_f52_working_capital_receivables_dpotrend_126d_base_v014_signal,
    f52wc_f52_working_capital_receivables_dposlr_base_v015_signal,
    f52wc_f52_working_capital_receivables_paycordiv_252d_base_v016_signal,
    f52wc_f52_working_capital_receivables_ccc_63d_base_v017_signal,
    f52wc_f52_working_capital_receivables_cccz_252d_base_v018_signal,
    f52wc_f52_working_capital_receivables_ccctrend_126d_base_v019_signal,
    f52wc_f52_working_capital_receivables_cccrank_504d_base_v020_signal,
    f52wc_f52_working_capital_receivables_cccslr_base_v021_signal,
    f52wc_f52_working_capital_receivables_dsodporatioslr_base_v022_signal,
    f52wc_f52_working_capital_receivables_dsodporatiodisp_base_v023_signal,
    f52wc_f52_working_capital_receivables_nwcint_63d_base_v024_signal,
    f52wc_f52_working_capital_receivables_nwcintz_252d_base_v025_signal,
    f52wc_f52_working_capital_receivables_nwcinttrend_126d_base_v026_signal,
    f52wc_f52_working_capital_receivables_nwcintrank_504d_base_v027_signal,
    f52wc_f52_working_capital_receivables_nwcsign_base_v028_signal,
    f52wc_f52_working_capital_receivables_clcover_63d_base_v029_signal,
    f52wc_f52_working_capital_receivables_clcoverz_252d_base_v030_signal,
    f52wc_f52_working_capital_receivables_clcovertrend_126d_base_v031_signal,
    f52wc_f52_working_capital_receivables_clcoverrank_504d_base_v032_signal,
    f52wc_f52_working_capital_receivables_quickcover_63d_base_v033_signal,
    f52wc_f52_working_capital_receivables_clshortfall_base_v034_signal,
    f52wc_f52_working_capital_receivables_defcush_63d_base_v035_signal,
    f52wc_f52_working_capital_receivables_defcushz_252d_base_v036_signal,
    f52wc_f52_working_capital_receivables_defvsrec_63d_base_v037_signal,
    f52wc_f52_working_capital_receivables_deflcover_63d_base_v038_signal,
    f52wc_f52_working_capital_receivables_recinassetsc_63d_base_v039_signal,
    f52wc_f52_working_capital_receivables_recinassetscz_base_v040_signal,
    f52wc_f52_working_capital_receivables_recinassetsctrend_base_v041_signal,
    f52wc_f52_working_capital_receivables_payinliabc_63d_base_v042_signal,
    f52wc_f52_working_capital_receivables_payinliabcz_base_v043_signal,
    f52wc_f52_working_capital_receivables_rectopay_63d_base_v044_signal,
    f52wc_f52_working_capital_receivables_rectopayz_base_v045_signal,
    f52wc_f52_working_capital_receivables_nettradeint_63d_base_v046_signal,
    f52wc_f52_working_capital_receivables_nettradetrend_base_v047_signal,
    f52wc_f52_working_capital_receivables_recturnaccel_base_v048_signal,
    f52wc_f52_working_capital_receivables_payturndisp_base_v049_signal,
    f52wc_f52_working_capital_receivables_turngap_base_v050_signal,
    f52wc_f52_working_capital_receivables_wcturn_63d_base_v051_signal,
    f52wc_f52_working_capital_receivables_wcturnreg_base_v052_signal,
    f52wc_f52_working_capital_receivables_dsoredflag_base_v053_signal,
    f52wc_f52_working_capital_receivables_floatquality_base_v054_signal,
    f52wc_f52_working_capital_receivables_ccctanh_base_v055_signal,
    f52wc_f52_working_capital_receivables_dsostress_base_v056_signal,
    f52wc_f52_working_capital_receivables_dpostretchreg_base_v057_signal,
    f52wc_f52_working_capital_receivables_wcabsorb_base_v058_signal,
    f52wc_f52_working_capital_receivables_recvsdefbuild_base_v059_signal,
    f52wc_f52_working_capital_receivables_liqheadgrow_base_v060_signal,
    f52wc_f52_working_capital_receivables_dsoclint_base_v061_signal,
    f52wc_f52_working_capital_receivables_nwccomptrend_base_v062_signal,
    f52wc_f52_working_capital_receivables_defcushrank_base_v063_signal,
    f52wc_f52_working_capital_receivables_dsoaccel_base_v064_signal,
    f52wc_f52_working_capital_receivables_dpoaccel_base_v065_signal,
    f52wc_f52_working_capital_receivables_floatgapz_base_v066_signal,
    f52wc_f52_working_capital_receivables_dsosignmag_base_v067_signal,
    f52wc_f52_working_capital_receivables_revliabcgrow_base_v068_signal,
    f52wc_f52_working_capital_receivables_caqualityreg_base_v069_signal,
    f52wc_f52_working_capital_receivables_cccdisp_base_v070_signal,
    f52wc_f52_working_capital_receivables_floatcover_base_v071_signal,
    f52wc_f52_working_capital_receivables_defcushaccel_base_v072_signal,
    f52wc_f52_working_capital_receivables_nwcintaccel_base_v073_signal,
    f52wc_f52_working_capital_receivables_cccdefint_base_v074_signal,
    f52wc_f52_working_capital_receivables_floatrisk_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F52_WORKING_CAPITAL_RECEIVABLES_REGISTRY_001_075 = REGISTRY


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

    print("OK f52_working_capital_receivables_base_001_075_claude: %d features pass" % n_features)
