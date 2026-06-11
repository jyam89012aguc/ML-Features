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


def _slope(s, w):
    def _f(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xd = x - x.mean()
        den = (xd * xd).sum()
        if den == 0:
            return np.nan
        return float((xd * (a - a.mean())).sum() / den)

    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (working-capital dynamics) =====
def _f20_dso(receivables, revenue, w):
    rev_day = revenue.rolling(w, min_periods=max(1, w // 2)).mean() / 91.0
    return receivables / rev_day.replace(0, np.nan)


def _f20_dio(inventory, cor, w):
    cor_day = cor.rolling(w, min_periods=max(1, w // 2)).mean() / 91.0
    return inventory / cor_day.replace(0, np.nan)


def _f20_dpo(payables, cor, w):
    cor_day = cor.rolling(w, min_periods=max(1, w // 2)).mean() / 91.0
    return payables / cor_day.replace(0, np.nan)


def _f20_ccc(receivables, inventory, payables, revenue, cor, w):
    return (_f20_dso(receivables, revenue, w)
            + _f20_dio(inventory, cor, w)
            - _f20_dpo(payables, cor, w))


def _f20_wc(assetsc, liabilitiesc):
    return assetsc - liabilitiesc


def _f20_recratio(receivables, revenue):
    return receivables / revenue.replace(0, np.nan)


def _f20_invratio(inventory, cor):
    return inventory / cor.replace(0, np.nan)


def _f20_payratio(payables, cor):
    return payables / cor.replace(0, np.nan)


# ============================================================
# DSO relative-to-baseline ratio: short DSO vs its own 252d mean (collection-stress ratio)
def f20wc_f20_working_capital_dynamics_dso126_126d_base_v076_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    b = d / _mean(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO smoothed by EMA (persistent collection level)
def f20wc_f20_working_capital_dynamics_dsoema_base_v077_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    b = d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO half-year change relative to its longer-run typical level
def f20wc_f20_working_capital_dynamics_dsochg_126d_base_v078_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    b = (d - d.shift(126)) / _mean(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO smoothed by EMA (persistent inventory level)
def f20wc_f20_working_capital_dynamics_dioema_base_v079_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    b = d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO half-year change relative to its longer-run typical level
def f20wc_f20_working_capital_dynamics_diochg_126d_base_v080_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    b = (d - d.shift(126)) / _mean(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO smoothed by EMA (persistent payables level)
def f20wc_f20_working_capital_dynamics_dpoema_base_v081_signal(payables, cor):
    d = _f20_dpo(payables, cor, 63)
    b = d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO half-year change relative to its longer-run typical level
def f20wc_f20_working_capital_dynamics_dpochg_126d_base_v082_signal(payables, cor):
    d = _f20_dpo(payables, cor, 63)
    b = (d - d.shift(126)) / _mean(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC smoothed minus its slow EMA (cycle displacement)
def f20wc_f20_working_capital_dynamics_cccdisp2_base_v083_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 63)
    b = c.ewm(span=42, min_periods=21).mean() - c.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cycle change vs one year ago (cycle lengthening)
def f20wc_f20_working_capital_dynamics_opcycyoy_252d_base_v084_signal(receivables, inventory, revenue, cor):
    op = _f20_dso(receivables, revenue, 252) + _f20_dio(inventory, cor, 252)
    b = op - op.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO relative to DIO (collection vs holding balance)
def f20wc_f20_working_capital_dynamics_dsodio_252d_base_v085_signal(receivables, inventory, revenue, cor):
    dso = _f20_dso(receivables, revenue, 252)
    dio = _f20_dio(inventory, cor, 252)
    b = (dso - dio) / (dso + dio).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO coverage of operating cycle (how much of DSO+DIO suppliers finance)
def f20wc_f20_working_capital_dynamics_dpocover_252d_base_v086_signal(receivables, inventory, payables, revenue, cor):
    op = _f20_dso(receivables, revenue, 252) + _f20_dio(inventory, cor, 252)
    dpo = _f20_dpo(payables, cor, 252)
    b = dpo / op.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables / revenue z-scored at a shorter window
def f20wc_f20_working_capital_dynamics_recrevz_126d_base_v087_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    b = _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory / cor z-scored
def f20wc_f20_working_capital_dynamics_invcorz_252d_base_v088_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables / cor z-scored
def f20wc_f20_working_capital_dynamics_paycorz_252d_base_v089_signal(payables, cor):
    r = _f20_payratio(payables, cor)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables intensity slope (collection-burden trajectory)
def f20wc_f20_working_capital_dynamics_recrevslope_126d_base_v090_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    b = _slope(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory intensity slope (build trajectory)
def f20wc_f20_working_capital_dynamics_invslope_126d_base_v091_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    b = _slope(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables intensity slope (supplier-terms trajectory)
def f20wc_f20_working_capital_dynamics_payslope_126d_base_v092_signal(payables, cor):
    r = _f20_payratio(payables, cor)
    b = _slope(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital intensity rank vs 504d history
def f20wc_f20_working_capital_dynamics_wcintrank_504d_base_v093_signal(assetsc, liabilitiesc, revenue):
    wc = _f20_wc(assetsc, liabilitiesc)
    ratio = wc / revenue.replace(0, np.nan)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net trade WC (rec+inv-pay) / current assets, level
def f20wc_f20_working_capital_dynamics_nowcca_126d_base_v094_signal(receivables, inventory, payables, assetsc):
    nowc = receivables + inventory - payables
    b = _mean(nowc / assetsc.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables build vs inventory build (which current account is growing faster)
def f20wc_f20_working_capital_dynamics_recvsinv_252d_base_v095_signal(receivables, inventory):
    rg = np.log(receivables.replace(0, np.nan) / receivables.shift(252).replace(0, np.nan))
    ig = np.log(inventory.replace(0, np.nan) / inventory.shift(252).replace(0, np.nan))
    b = rg - ig
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory build vs payables build (financing of stockpiling)
def f20wc_f20_working_capital_dynamics_invvspay_252d_base_v096_signal(inventory, payables):
    ig = np.log(inventory.replace(0, np.nan) / inventory.shift(252).replace(0, np.nan))
    pg = np.log(payables.replace(0, np.nan) / payables.shift(252).replace(0, np.nan))
    b = ig - pg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-asset growth (liquidity-base expansion)
def f20wc_f20_working_capital_dynamics_cagrowth_252d_base_v097_signal(assetsc):
    b = np.log(assetsc.replace(0, np.nan) / assetsc.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-liability growth (short-term obligation expansion)
def f20wc_f20_working_capital_dynamics_clgrowth_252d_base_v098_signal(liabilitiesc):
    b = np.log(liabilitiesc.replace(0, np.nan) / liabilitiesc.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-per-net-trade-WC trajectory: slope of cash-cycle productivity
def f20wc_f20_working_capital_dynamics_revpernowc_252d_base_v099_signal(receivables, inventory, payables, revenue):
    nowc = receivables + inventory - payables
    prod = revenue / nowc.replace(0, np.nan)
    b = _slope(prod, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO dispersion / DPO dispersion (asymmetry of receivable vs payable volatility)
def f20wc_f20_working_capital_dynamics_dsodpodisp_252d_base_v100_signal(receivables, payables, revenue, cor):
    dso = _f20_dso(receivables, revenue, 63)
    dpo = _f20_dpo(payables, cor, 63)
    b = _std(dso, 252) / _std(dpo, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC quarter-over-quarter momentum
def f20wc_f20_working_capital_dynamics_cccqmom_63d_base_v101_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 126)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO short-vs-long level ratio (recent collection vs structural baseline)
def f20wc_f20_working_capital_dynamics_dsoextreme_252d_base_v102_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 21)
    b = _mean(d, 21) / _mean(d, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO extremity (recent vs distant payables, std-normalized)
def f20wc_f20_working_capital_dynamics_dpoextreme_252d_base_v103_signal(payables, cor):
    d = _f20_dpo(payables, cor, 63)
    near = _mean(d, 63)
    far = _mean(d, 504)
    b = (near - far) / _std(d, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory share of current assets, slope (stockpiling structural shift)
def f20wc_f20_working_capital_dynamics_invshareslope_252d_base_v104_signal(inventory, assetsc):
    share = inventory / assetsc.replace(0, np.nan)
    b = _slope(share, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables share of current assets, slope
def f20wc_f20_working_capital_dynamics_recshareslope_252d_base_v105_signal(receivables, assetsc):
    share = receivables / assetsc.replace(0, np.nan)
    b = _slope(share, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables share of current liabilities, slope
def f20wc_f20_working_capital_dynamics_payshareslope_252d_base_v106_signal(payables, liabilitiesc):
    share = payables / liabilitiesc.replace(0, np.nan)
    b = _slope(share, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC coefficient-of-variation (cycle instability)
def f20wc_f20_working_capital_dynamics_ccccv_252d_base_v107_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 63)
    b = _std(c, 252) / _mean(c, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net trade WC change scaled by current assets (current-account accrual)
def f20wc_f20_working_capital_dynamics_nowcaccr_252d_base_v108_signal(receivables, inventory, payables, assetsc):
    nowc = receivables + inventory - payables
    dnowc = nowc - nowc.shift(252)
    b = dnowc / _mean(assetsc, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO tanh-bounded yoy change (collection shock, squashed)
def f20wc_f20_working_capital_dynamics_dsotanh_252d_base_v109_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 252)
    chg = d - d.shift(252)
    b = np.tanh(chg / 15.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO tanh-bounded yoy change (inventory shock, squashed)
def f20wc_f20_working_capital_dynamics_diotanh_252d_base_v110_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 252)
    chg = d - d.shift(252)
    b = np.tanh(chg / 15.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC intensity acceleration: level now vs lagged mean (intensity inflection)
def f20wc_f20_working_capital_dynamics_wcintaccl_252d_base_v111_signal(assetsc, liabilitiesc, revenue):
    wc = _f20_wc(assetsc, liabilitiesc)
    ratio = wc / revenue.replace(0, np.nan)
    b = ratio - _mean(ratio.shift(63), 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO vs DIO spread change (rebalancing of receivable vs inventory tie-up)
def f20wc_f20_working_capital_dynamics_dsodiospr_252d_base_v112_signal(receivables, inventory, revenue, cor):
    dso = _f20_dso(receivables, revenue, 126)
    dio = _f20_dio(inventory, cor, 126)
    spr = dso - dio
    b = spr - spr.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing days (DSO+DIO-DPO) scaled by current-ratio cushion
def f20wc_f20_working_capital_dynamics_cccbycush_252d_base_v113_signal(receivables, inventory, payables, revenue, cor, assetsc, liabilitiesc):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    cush = assetsc / liabilitiesc.replace(0, np.nan)
    b = c * cush
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables intensity rank vs 504d history
def f20wc_f20_working_capital_dynamics_recrevrank_504d_base_v114_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory intensity rank vs 504d history
def f20wc_f20_working_capital_dynamics_invrank_504d_base_v115_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables intensity rank vs 504d history
def f20wc_f20_working_capital_dynamics_payrank_504d_base_v116_signal(payables, cor):
    r = _f20_payratio(payables, cor)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quick-ratio slope (defensive-liquidity trajectory excluding inventory)
def f20wc_f20_working_capital_dynamics_quickslope_252d_base_v117_signal(assetsc, inventory, liabilitiesc):
    q = (assetsc - inventory) / liabilitiesc.replace(0, np.nan)
    b = _slope(q, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO vs DPO net-days change (working-capital financing gap momentum)
def f20wc_f20_working_capital_dynamics_dsodpomom_126d_base_v118_signal(receivables, payables, revenue, cor):
    net = _f20_dso(receivables, revenue, 126) - _f20_dpo(payables, cor, 126)
    b = net - net.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-to-payables (trade balance) slope
def f20wc_f20_working_capital_dynamics_recpayslope_252d_base_v119_signal(receivables, payables):
    r = receivables / payables.replace(0, np.nan)
    b = _slope(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-to-payables coverage (supplier financing of stock)
def f20wc_f20_working_capital_dynamics_invpay_126d_base_v120_signal(inventory, payables):
    b = _mean(inventory / payables.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC vs its 504d median (long-horizon cycle extremity)
def f20wc_f20_working_capital_dynamics_cccmedgap_504d_base_v121_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 126)
    med = c.rolling(504, min_periods=126).median()
    b = (c - med) / _std(c, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO skew over a year (collection-distribution asymmetry)
def f20wc_f20_working_capital_dynamics_dsoskew_252d_base_v122_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    b = d.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO skew over a year (inventory-distribution asymmetry)
def f20wc_f20_working_capital_dynamics_dioskew_252d_base_v123_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    b = d.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital cushion (WC / current assets) dispersion (liquidity-buffer instability)
def f20wc_f20_working_capital_dynamics_wccushslope_252d_base_v124_signal(assetsc, liabilitiesc):
    wc = _f20_wc(assetsc, liabilitiesc)
    cush = wc / assetsc.replace(0, np.nan)
    b = _std(cush, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cycle dispersion (instability of DSO+DIO)
def f20wc_f20_working_capital_dynamics_opcycdisp_252d_base_v125_signal(receivables, inventory, revenue, cor):
    op = _f20_dso(receivables, revenue, 63) + _f20_dio(inventory, cor, 63)
    b = _std(op, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth minus current-asset-growth (capital-light scaling)
def f20wc_f20_working_capital_dynamics_revvsca_252d_base_v126_signal(revenue, assetsc):
    rg = np.log(revenue.replace(0, np.nan) / revenue.shift(252).replace(0, np.nan))
    ag = np.log(assetsc.replace(0, np.nan) / assetsc.shift(252).replace(0, np.nan))
    b = rg - ag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cor-growth minus inventory-growth (demand outrunning stock = lean)
def f20wc_f20_working_capital_dynamics_corvsinv_252d_base_v127_signal(cor, inventory):
    cg = np.log(cor.replace(0, np.nan) / cor.shift(252).replace(0, np.nan))
    ig = np.log(inventory.replace(0, np.nan) / inventory.shift(252).replace(0, np.nan))
    b = cg - ig
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO sustainability: payables ratio z-scored at short window (supplier-stretch shock)
def f20wc_f20_working_capital_dynamics_dpoz126_126d_base_v128_signal(payables, cor):
    r = _f20_payratio(payables, cor)
    b = _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net WC over current liabilities (solvency buffer on short obligations)
def f20wc_f20_working_capital_dynamics_wcoverliab_126d_base_v129_signal(assetsc, liabilitiesc):
    wc = _f20_wc(assetsc, liabilitiesc)
    b = _mean(wc / liabilitiesc.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC level scaled by current-asset turnover proxy (cash tie-up intensity)
def f20wc_f20_working_capital_dynamics_ccccaint_252d_base_v130_signal(receivables, inventory, payables, revenue, cor, assetsc):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    caint = _mean(assetsc, 252) / _mean(revenue, 252).replace(0, np.nan)
    b = c * caint
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables intensity dispersion over a year (collection volatility)
def f20wc_f20_working_capital_dynamics_recrevdisp_252d_base_v131_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    b = _std(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory intensity dispersion over a year
def f20wc_f20_working_capital_dynamics_invdisp_252d_base_v132_signal(inventory, cor):
    r = _f20_invratio(inventory, cor)
    b = _std(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO momentum scaled by its own dispersion (risk-adjusted collection drift)
def f20wc_f20_working_capital_dynamics_dsoriskadj_126d_base_v133_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    mom = d - d.shift(126)
    b = mom / _std(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO momentum scaled by its own dispersion (risk-adjusted build drift)
def f20wc_f20_working_capital_dynamics_dioriskadj_126d_base_v134_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    mom = d - d.shift(126)
    b = mom / _std(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion efficiency momentum: change in revenue-per-CCC-day over a year
def f20wc_f20_working_capital_dynamics_cccveloc_252d_base_v135_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 126)
    velo = revenue / (c.abs() + 1.0)
    b = velo - velo.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO trend vs DIO trend spread (supplier-terms vs inventory-holding divergence)
def f20wc_f20_working_capital_dynamics_dpodsotrend_252d_base_v136_signal(inventory, payables, cor):
    dio = _f20_dio(inventory, cor, 63)
    dpo = _f20_dpo(payables, cor, 63)
    b = _slope(dpo, 252) - _slope(dio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-ratio rank vs 504d history (liquidity-regime positioning)
def f20wc_f20_working_capital_dynamics_wcadequacy_126d_base_v137_signal(assetsc, liabilitiesc):
    cr = assetsc / liabilitiesc.replace(0, np.nan)
    b = _rank(cr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory build acceleration (second difference of DIO)
def f20wc_f20_working_capital_dynamics_dioaccel_252d_base_v138_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    b = d.diff(63) - d.diff(63).shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables build acceleration (second difference of DSO)
def f20wc_f20_working_capital_dynamics_dsoaccel_252d_base_v139_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    b = d.diff(63) - d.diff(63).shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trade-balance (receivables/payables) z-score (net customer-vs-supplier exposure)
def f20wc_f20_working_capital_dynamics_recpayz_252d_base_v140_signal(receivables, payables):
    r = receivables / payables.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net trade WC intensity acceleration (second difference of nowc/revenue)
def f20wc_f20_working_capital_dynamics_nowcyoy_252d_base_v141_signal(receivables, inventory, payables, revenue):
    nowc = receivables + inventory - payables
    ratio = nowc / revenue.replace(0, np.nan)
    b = ratio.diff(63) - ratio.diff(63).shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC long-run rank vs 1260d history (multi-year cycle positioning)
def f20wc_f20_working_capital_dynamics_ccclongrank_1260d_base_v142_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    b = _rank(c, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO-share-of-CCC momentum: change in collection's share of the cash cycle
def f20wc_f20_working_capital_dynamics_dsoshare_252d_base_v143_signal(receivables, inventory, payables, revenue, cor):
    dso = _f20_dso(receivables, revenue, 126)
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 126)
    share = dso / c.replace(0, np.nan)
    b = share - share.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-vs-payables financing balance: DIO relative to DPO (self-financing of stock)
def f20wc_f20_working_capital_dynamics_dioshare_252d_base_v144_signal(inventory, payables, cor):
    dio = _f20_dio(inventory, cor, 252)
    dpo = _f20_dpo(payables, cor, 252)
    b = (dio - dpo) / (dio + dpo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital intensity dispersion (intensity instability)
def f20wc_f20_working_capital_dynamics_wcintdisp_252d_base_v145_signal(assetsc, liabilitiesc, revenue):
    wc = _f20_wc(assetsc, liabilitiesc)
    ratio = wc / revenue.replace(0, np.nan)
    b = _std(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# collection-vs-payment intensity spread: receivables/revenue minus payables/cor, z-blended
def f20wc_f20_working_capital_dynamics_recrevtanh_126d_base_v146_signal(receivables, payables, revenue, cor):
    rr = _z(_f20_recratio(receivables, revenue), 252)
    pr = _z(_f20_payratio(payables, cor), 252)
    b = rr - pr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-turnover acceleration (second difference of cor/inventory)
def f20wc_f20_working_capital_dynamics_invturnz_252d_base_v147_signal(cor, inventory):
    t = cor / inventory.replace(0, np.nan)
    b = t.diff(63) - t.diff(63).shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC dispersion / CCC level (relative cycle instability over 504d)
def f20wc_f20_working_capital_dynamics_cccinstab_504d_base_v148_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 63)
    b = _std(c, 504) / _mean(c, 504).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net trade WC over current liabilities (short-term financing of trade cycle)
def f20wc_f20_working_capital_dynamics_nowcliab_126d_base_v149_signal(receivables, inventory, payables, liabilitiesc):
    nowc = receivables + inventory - payables
    b = _mean(nowc / liabilitiesc.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite WC stress: DSO momentum + DIO momentum - DPO momentum, z-blended
def f20wc_f20_working_capital_dynamics_wcstress_252d_base_v150_signal(receivables, inventory, payables, revenue, cor):
    dso = _f20_dso(receivables, revenue, 63)
    dio = _f20_dio(inventory, cor, 63)
    dpo = _f20_dpo(payables, cor, 63)
    s = _z(dso - dso.shift(126), 252) + _z(dio - dio.shift(126), 252) - _z(dpo - dpo.shift(126), 252)
    result = s
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20wc_f20_working_capital_dynamics_dso126_126d_base_v076_signal,
    f20wc_f20_working_capital_dynamics_dsoema_base_v077_signal,
    f20wc_f20_working_capital_dynamics_dsochg_126d_base_v078_signal,
    f20wc_f20_working_capital_dynamics_dioema_base_v079_signal,
    f20wc_f20_working_capital_dynamics_diochg_126d_base_v080_signal,
    f20wc_f20_working_capital_dynamics_dpoema_base_v081_signal,
    f20wc_f20_working_capital_dynamics_dpochg_126d_base_v082_signal,
    f20wc_f20_working_capital_dynamics_cccdisp2_base_v083_signal,
    f20wc_f20_working_capital_dynamics_opcycyoy_252d_base_v084_signal,
    f20wc_f20_working_capital_dynamics_dsodio_252d_base_v085_signal,
    f20wc_f20_working_capital_dynamics_dpocover_252d_base_v086_signal,
    f20wc_f20_working_capital_dynamics_recrevz_126d_base_v087_signal,
    f20wc_f20_working_capital_dynamics_invcorz_252d_base_v088_signal,
    f20wc_f20_working_capital_dynamics_paycorz_252d_base_v089_signal,
    f20wc_f20_working_capital_dynamics_recrevslope_126d_base_v090_signal,
    f20wc_f20_working_capital_dynamics_invslope_126d_base_v091_signal,
    f20wc_f20_working_capital_dynamics_payslope_126d_base_v092_signal,
    f20wc_f20_working_capital_dynamics_wcintrank_504d_base_v093_signal,
    f20wc_f20_working_capital_dynamics_nowcca_126d_base_v094_signal,
    f20wc_f20_working_capital_dynamics_recvsinv_252d_base_v095_signal,
    f20wc_f20_working_capital_dynamics_invvspay_252d_base_v096_signal,
    f20wc_f20_working_capital_dynamics_cagrowth_252d_base_v097_signal,
    f20wc_f20_working_capital_dynamics_clgrowth_252d_base_v098_signal,
    f20wc_f20_working_capital_dynamics_revpernowc_252d_base_v099_signal,
    f20wc_f20_working_capital_dynamics_dsodpodisp_252d_base_v100_signal,
    f20wc_f20_working_capital_dynamics_cccqmom_63d_base_v101_signal,
    f20wc_f20_working_capital_dynamics_dsoextreme_252d_base_v102_signal,
    f20wc_f20_working_capital_dynamics_dpoextreme_252d_base_v103_signal,
    f20wc_f20_working_capital_dynamics_invshareslope_252d_base_v104_signal,
    f20wc_f20_working_capital_dynamics_recshareslope_252d_base_v105_signal,
    f20wc_f20_working_capital_dynamics_payshareslope_252d_base_v106_signal,
    f20wc_f20_working_capital_dynamics_ccccv_252d_base_v107_signal,
    f20wc_f20_working_capital_dynamics_nowcaccr_252d_base_v108_signal,
    f20wc_f20_working_capital_dynamics_dsotanh_252d_base_v109_signal,
    f20wc_f20_working_capital_dynamics_diotanh_252d_base_v110_signal,
    f20wc_f20_working_capital_dynamics_wcintaccl_252d_base_v111_signal,
    f20wc_f20_working_capital_dynamics_dsodiospr_252d_base_v112_signal,
    f20wc_f20_working_capital_dynamics_cccbycush_252d_base_v113_signal,
    f20wc_f20_working_capital_dynamics_recrevrank_504d_base_v114_signal,
    f20wc_f20_working_capital_dynamics_invrank_504d_base_v115_signal,
    f20wc_f20_working_capital_dynamics_payrank_504d_base_v116_signal,
    f20wc_f20_working_capital_dynamics_quickslope_252d_base_v117_signal,
    f20wc_f20_working_capital_dynamics_dsodpomom_126d_base_v118_signal,
    f20wc_f20_working_capital_dynamics_recpayslope_252d_base_v119_signal,
    f20wc_f20_working_capital_dynamics_invpay_126d_base_v120_signal,
    f20wc_f20_working_capital_dynamics_cccmedgap_504d_base_v121_signal,
    f20wc_f20_working_capital_dynamics_dsoskew_252d_base_v122_signal,
    f20wc_f20_working_capital_dynamics_dioskew_252d_base_v123_signal,
    f20wc_f20_working_capital_dynamics_wccushslope_252d_base_v124_signal,
    f20wc_f20_working_capital_dynamics_opcycdisp_252d_base_v125_signal,
    f20wc_f20_working_capital_dynamics_revvsca_252d_base_v126_signal,
    f20wc_f20_working_capital_dynamics_corvsinv_252d_base_v127_signal,
    f20wc_f20_working_capital_dynamics_dpoz126_126d_base_v128_signal,
    f20wc_f20_working_capital_dynamics_wcoverliab_126d_base_v129_signal,
    f20wc_f20_working_capital_dynamics_ccccaint_252d_base_v130_signal,
    f20wc_f20_working_capital_dynamics_recrevdisp_252d_base_v131_signal,
    f20wc_f20_working_capital_dynamics_invdisp_252d_base_v132_signal,
    f20wc_f20_working_capital_dynamics_dsoriskadj_126d_base_v133_signal,
    f20wc_f20_working_capital_dynamics_dioriskadj_126d_base_v134_signal,
    f20wc_f20_working_capital_dynamics_cccveloc_252d_base_v135_signal,
    f20wc_f20_working_capital_dynamics_dpodsotrend_252d_base_v136_signal,
    f20wc_f20_working_capital_dynamics_wcadequacy_126d_base_v137_signal,
    f20wc_f20_working_capital_dynamics_dioaccel_252d_base_v138_signal,
    f20wc_f20_working_capital_dynamics_dsoaccel_252d_base_v139_signal,
    f20wc_f20_working_capital_dynamics_recpayz_252d_base_v140_signal,
    f20wc_f20_working_capital_dynamics_nowcyoy_252d_base_v141_signal,
    f20wc_f20_working_capital_dynamics_ccclongrank_1260d_base_v142_signal,
    f20wc_f20_working_capital_dynamics_dsoshare_252d_base_v143_signal,
    f20wc_f20_working_capital_dynamics_dioshare_252d_base_v144_signal,
    f20wc_f20_working_capital_dynamics_wcintdisp_252d_base_v145_signal,
    f20wc_f20_working_capital_dynamics_recrevtanh_126d_base_v146_signal,
    f20wc_f20_working_capital_dynamics_invturnz_252d_base_v147_signal,
    f20wc_f20_working_capital_dynamics_cccinstab_504d_base_v148_signal,
    f20wc_f20_working_capital_dynamics_nowcliab_126d_base_v149_signal,
    f20wc_f20_working_capital_dynamics_wcstress_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_WORKING_CAPITAL_DYNAMICS_REGISTRY_076_150 = REGISTRY


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

    receivables = _fund(101, base=2.0e8).rename("receivables")
    inventory = _fund(102, base=1.5e8).rename("inventory")
    payables = _fund(103, base=1.2e8).rename("payables")
    revenue = _fund(104, base=8.0e8).rename("revenue")
    cor = _fund(105, base=5.0e8).rename("cor")
    assetsc = _fund(106, base=6.0e8).rename("assetsc")
    liabilitiesc = _fund(107, base=3.5e8).rename("liabilitiesc")

    cols = {
        "receivables": receivables, "inventory": inventory, "payables": payables,
        "revenue": revenue, "cor": cor, "assetsc": assetsc, "liabilitiesc": liabilitiesc,
    }

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

    print("OK f20_working_capital_dynamics_base_076_150_claude: %d features pass" % n_features)
