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
    # days-sales-outstanding: receivables relative to per-day revenue over window
    rev_day = revenue.rolling(w, min_periods=max(1, w // 2)).mean() / 91.0
    return receivables / rev_day.replace(0, np.nan)


def _f20_dio(inventory, cor, w):
    # days-inventory-outstanding: inventory relative to per-day cost-of-revenue
    cor_day = cor.rolling(w, min_periods=max(1, w // 2)).mean() / 91.0
    return inventory / cor_day.replace(0, np.nan)


def _f20_dpo(payables, cor, w):
    # days-payables-outstanding: payables relative to per-day cost-of-revenue
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
# DSO level (252d revenue base)
def f20wc_f20_working_capital_dynamics_dso_252d_base_v001_signal(receivables, revenue):
    b = _f20_dso(receivables, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO z-scored vs own 252d history (de-trended collection-period level)
def f20wc_f20_working_capital_dynamics_dsoz_252d_base_v002_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 126)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO percentile-rank vs own 504d history
def f20wc_f20_working_capital_dynamics_dsorank_504d_base_v003_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 126)
    b = _rank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO level (252d cor base)
def f20wc_f20_working_capital_dynamics_dio_252d_base_v004_signal(inventory, cor):
    b = _f20_dio(inventory, cor, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO z-scored vs own 252d history
def f20wc_f20_working_capital_dynamics_dioz_252d_base_v005_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 126)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO percentile-rank vs own 504d history
def f20wc_f20_working_capital_dynamics_diorank_504d_base_v006_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 126)
    b = _rank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO level (252d cor base)
def f20wc_f20_working_capital_dynamics_dpo_252d_base_v007_signal(payables, cor):
    b = _f20_dpo(payables, cor, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO z-scored vs own 252d history
def f20wc_f20_working_capital_dynamics_dpoz_252d_base_v008_signal(payables, cor):
    d = _f20_dpo(payables, cor, 126)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO percentile-rank vs own 504d history
def f20wc_f20_working_capital_dynamics_dporank_504d_base_v009_signal(payables, cor):
    d = _f20_dpo(payables, cor, 126)
    b = _rank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion cycle level (252d)
def f20wc_f20_working_capital_dynamics_ccc_252d_base_v010_signal(receivables, inventory, payables, revenue, cor):
    b = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC z-scored vs own 252d history
def f20wc_f20_working_capital_dynamics_cccz_252d_base_v011_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 126)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC compression ratio: short-window cycle vs long-window cycle (level ratio)
def f20wc_f20_working_capital_dynamics_cccratio_504d_base_v012_signal(receivables, inventory, payables, revenue, cor):
    short = _f20_ccc(receivables, inventory, payables, revenue, cor, 63)
    long = _f20_ccc(receivables, inventory, payables, revenue, cor, 504)
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cycle (DSO + DIO), level
def f20wc_f20_working_capital_dynamics_opcyc_252d_base_v013_signal(receivables, inventory, revenue, cor):
    b = _f20_dso(receivables, revenue, 252) + _f20_dio(inventory, cor, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital intensity: WC / revenue (per-day revenue scaling)
def f20wc_f20_working_capital_dynamics_wcint_252d_base_v014_signal(assetsc, liabilitiesc, revenue):
    wc = _f20_wc(assetsc, liabilitiesc)
    rev = _mean(revenue, 252)
    b = wc / rev.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital intensity z-scored
def f20wc_f20_working_capital_dynamics_wcintz_252d_base_v015_signal(assetsc, liabilitiesc, revenue):
    wc = _f20_wc(assetsc, liabilitiesc)
    ratio = wc / revenue.replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables / revenue ratio level
def f20wc_f20_working_capital_dynamics_recrev_126d_base_v016_signal(receivables, revenue):
    b = _mean(_f20_recratio(receivables, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/revenue trend (slope over 252d)
def f20wc_f20_working_capital_dynamics_recrevtrend_252d_base_v017_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    b = _slope(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory / cor ratio level
def f20wc_f20_working_capital_dynamics_invcor_126d_base_v018_signal(inventory, cor):
    b = _mean(_f20_invratio(inventory, cor), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory build: inventory growth over 252d minus cor growth (build vs demand)
def f20wc_f20_working_capital_dynamics_invbuild_252d_base_v019_signal(inventory, cor):
    ig = np.log(inventory.replace(0, np.nan) / inventory.shift(252).replace(0, np.nan))
    cg = np.log(cor.replace(0, np.nan) / cor.shift(252).replace(0, np.nan))
    b = ig - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables / cor ratio level
def f20wc_f20_working_capital_dynamics_paycor_126d_base_v020_signal(payables, cor):
    b = _mean(_f20_payratio(payables, cor), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO acceleration: change-of-change of DSO (collection-period inflection)
def f20wc_f20_working_capital_dynamics_dsotrend_252d_base_v021_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    b = d.diff(63) - d.diff(63).shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO acceleration: change-of-change of DIO (inventory-build inflection)
def f20wc_f20_working_capital_dynamics_diotrend_252d_base_v022_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    b = d.diff(63) - d.diff(63).shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO acceleration: change-of-change of DPO (payment-stretch inflection)
def f20wc_f20_working_capital_dynamics_dpotrend_252d_base_v023_signal(payables, cor):
    d = _f20_dpo(payables, cor, 63)
    b = d.diff(63) - d.diff(63).shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC trend (slope over 126d of the smoothed cycle)
def f20wc_f20_working_capital_dynamics_ccctrend_252d_base_v024_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 126)
    b = _slope(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio (assetsc / liabilitiesc) level
def f20wc_f20_working_capital_dynamics_curratio_63d_base_v025_signal(assetsc, liabilitiesc):
    b = _mean(assetsc / liabilitiesc.replace(0, np.nan), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio z-scored
def f20wc_f20_working_capital_dynamics_curratioz_252d_base_v026_signal(assetsc, liabilitiesc):
    cr = assetsc / liabilitiesc.replace(0, np.nan)
    b = _z(cr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables share of current assets
def f20wc_f20_working_capital_dynamics_recshare_126d_base_v027_signal(receivables, assetsc):
    b = _mean(receivables / assetsc.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory share of current assets
def f20wc_f20_working_capital_dynamics_invshare_126d_base_v028_signal(inventory, assetsc):
    b = _mean(inventory / assetsc.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables share of current liabilities
def f20wc_f20_working_capital_dynamics_payshare_126d_base_v029_signal(payables, liabilitiesc):
    b = _mean(payables / liabilitiesc.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory drag on liquidity: gap between current and quick ratio (inventory share of coverage)
def f20wc_f20_working_capital_dynamics_quick_63d_base_v030_signal(assetsc, inventory, liabilitiesc):
    cr = assetsc / liabilitiesc.replace(0, np.nan)
    qr = (assetsc - inventory) / liabilitiesc.replace(0, np.nan)
    b = _mean((cr - qr) / cr.replace(0, np.nan), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO minus DPO (net financing days on the customer/supplier axis)
def f20wc_f20_working_capital_dynamics_dsominusdpo_252d_base_v031_signal(receivables, payables, revenue, cor):
    b = _f20_dso(receivables, revenue, 252) - _f20_dpo(payables, cor, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO minus DPO (inventory financing gap)
def f20wc_f20_working_capital_dynamics_diominusdpo_252d_base_v032_signal(inventory, payables, cor):
    b = _f20_dio(inventory, cor, 252) - _f20_dpo(payables, cor, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth minus revenue-growth (channel-stuffing proxy)
def f20wc_f20_working_capital_dynamics_recvsrev_252d_base_v033_signal(receivables, revenue):
    rg = np.log(receivables.replace(0, np.nan) / receivables.shift(252).replace(0, np.nan))
    sg = np.log(revenue.replace(0, np.nan) / revenue.shift(252).replace(0, np.nan))
    b = rg - sg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables-growth minus cor-growth (supplier-financing expansion)
def f20wc_f20_working_capital_dynamics_payvscor_252d_base_v034_signal(payables, cor):
    pg = np.log(payables.replace(0, np.nan) / payables.shift(252).replace(0, np.nan))
    cg = np.log(cor.replace(0, np.nan) / cor.shift(252).replace(0, np.nan))
    b = pg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital growth over 252d (log change of WC level)
def f20wc_f20_working_capital_dynamics_wcgrowth_252d_base_v035_signal(assetsc, liabilitiesc):
    wc = _f20_wc(assetsc, liabilitiesc)
    b = np.log(wc.replace(0, np.nan) / wc.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO dispersion (rolling std of DSO over 126d) - collection volatility
def f20wc_f20_working_capital_dynamics_dsodisp_126d_base_v036_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    b = _std(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO dispersion (rolling std over 126d)
def f20wc_f20_working_capital_dynamics_diodisp_126d_base_v037_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    b = _std(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC dispersion (rolling std over 252d)
def f20wc_f20_working_capital_dynamics_cccdisp_252d_base_v038_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 63)
    b = _std(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient-of-variation of DSO (dispersion / level)
def f20wc_f20_working_capital_dynamics_dsocv_252d_base_v039_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    b = _std(d, 252) / _mean(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC change vs one year ago (year-over-year cycle delta)
def f20wc_f20_working_capital_dynamics_cccyoy_252d_base_v040_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO change vs one year ago
def f20wc_f20_working_capital_dynamics_dsoyoy_252d_base_v041_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 252)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO change vs one year ago
def f20wc_f20_working_capital_dynamics_dioyoy_252d_base_v042_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 252)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net trade cycle scaled by revenue intensity (CCC weighted by recratio)
def f20wc_f20_working_capital_dynamics_cccwt_252d_base_v043_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    intensity = _mean(_f20_recratio(receivables, revenue), 252)
    b = c * intensity
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-to-receivables balance (stock vs claim composition)
def f20wc_f20_working_capital_dynamics_invrec_126d_base_v044_signal(inventory, receivables):
    b = _mean(inventory / receivables.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables-to-receivables balance (supplier vs customer financing)
def f20wc_f20_working_capital_dynamics_payrec_126d_base_v045_signal(payables, receivables):
    b = _mean(payables / receivables.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net operating WC composition: (rec + inv - pay) financed share of current assets, ranked
def f20wc_f20_working_capital_dynamics_nowc_252d_base_v046_signal(receivables, inventory, payables, assetsc):
    nowc = receivables + inventory - payables
    ratio = nowc / assetsc.replace(0, np.nan)
    b = _rank(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net operating WC z-scored vs history
def f20wc_f20_working_capital_dynamics_nowcz_252d_base_v047_signal(receivables, inventory, payables, revenue):
    nowc = receivables + inventory - payables
    ratio = nowc / revenue.replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO momentum: change in DSO over a quarter
def f20wc_f20_working_capital_dynamics_dsomom_63d_base_v048_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 252)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO momentum: change over a quarter
def f20wc_f20_working_capital_dynamics_diomom_63d_base_v049_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 252)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO momentum: change over a quarter
def f20wc_f20_working_capital_dynamics_dpomom_63d_base_v050_signal(payables, cor):
    d = _f20_dpo(payables, cor, 252)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital turnover trend: slope of revenue/WC over a year (efficiency trajectory)
def f20wc_f20_working_capital_dynamics_wcturn_252d_base_v051_signal(revenue, assetsc, liabilitiesc):
    wc = _f20_wc(assetsc, liabilitiesc)
    turn = revenue / wc.replace(0, np.nan)
    b = _slope(turn, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables turnover stability: coefficient-of-variation of revenue/receivables
def f20wc_f20_working_capital_dynamics_recturn_126d_base_v052_signal(revenue, receivables):
    t = revenue / receivables.replace(0, np.nan)
    b = _std(t, 126) / _mean(t, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory turnover acceleration: turnover now vs its 126d-ago level
def f20wc_f20_working_capital_dynamics_invturn_126d_base_v053_signal(cor, inventory):
    t = cor / inventory.replace(0, np.nan)
    b = t - t.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payables turnover dispersion: rolling std of cor/payables (supplier-terms volatility)
def f20wc_f20_working_capital_dynamics_payturn_126d_base_v054_signal(cor, payables):
    t = cor / payables.replace(0, np.nan)
    b = _std(t, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cycle sign x sqrt-magnitude of its half-year change (signed cycle shock)
def f20wc_f20_working_capital_dynamics_dsosignmag_252d_base_v055_signal(receivables, inventory, revenue, cor):
    op = _f20_dso(receivables, revenue, 126) + _f20_dio(inventory, cor, 126)
    chg = op - op.shift(126)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC tanh-squashed momentum (bounded cycle change)
def f20wc_f20_working_capital_dynamics_ccctanh_63d_base_v056_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 126)
    chg = c - c.shift(63)
    b = np.tanh(chg / 10.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory build relative to current-asset base (stockpiling intensity)
def f20wc_f20_working_capital_dynamics_invbuildint_252d_base_v057_signal(inventory, assetsc):
    share = inventory / assetsc.replace(0, np.nan)
    b = share - share.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO exponential-weighted level minus slow EWMA (displacement)
def f20wc_f20_working_capital_dynamics_dsodisp2_base_v058_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 63)
    b = d.ewm(span=42, min_periods=21).mean() - d.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC EWMA-smoothed level (persistent cycle)
def f20wc_f20_working_capital_dynamics_cccema_base_v059_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 126)
    b = c.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-vs-inventory intensity spread: which working-capital tie-up dominates
def f20wc_f20_working_capital_dynamics_recrevaccl_252d_base_v060_signal(receivables, inventory, revenue, cor):
    rr = _z(_f20_recratio(receivables, revenue), 252)
    ir = _z(_f20_invratio(inventory, cor), 252)
    b = rr - ir
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# defensive interval proxy: (rec + assetsc-inv) / per-day cor
def f20wc_f20_working_capital_dynamics_definterval_252d_base_v061_signal(receivables, assetsc, inventory, cor):
    liquid = receivables + (assetsc - inventory)
    cor_day = _mean(cor, 252) / 91.0
    b = liquid / cor_day.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC relative to operating cycle (financing share of the cycle)
def f20wc_f20_working_capital_dynamics_cccshare_252d_base_v062_signal(receivables, inventory, payables, revenue, cor):
    op = _f20_dso(receivables, revenue, 252) + _f20_dio(inventory, cor, 252)
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 252)
    b = c / op.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-ratio acceleration: change-of-change of assetsc/liabilitiesc (liquidity inflection)
def f20wc_f20_working_capital_dynamics_curlevdrift_252d_base_v063_signal(assetsc, liabilitiesc):
    cr = assetsc / liabilitiesc.replace(0, np.nan)
    b = cr.diff(63) - cr.diff(63).shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO regime extremity: recent level vs distant level, in std units
def f20wc_f20_working_capital_dynamics_dioextreme_252d_base_v064_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 63)
    near = _mean(d, 63)
    far = _mean(d, 504)
    b = (near - far) / _std(d, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC accrual reversal: this year's WC delta minus last year's WC delta, revenue-scaled
def f20wc_f20_working_capital_dynamics_wcaccrual_252d_base_v065_signal(assetsc, liabilitiesc, revenue):
    wc = _f20_wc(assetsc, liabilitiesc)
    dwc = wc - wc.shift(252)
    rev = _mean(revenue, 252).replace(0, np.nan)
    b = dwc / rev - (dwc.shift(252) / rev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables intensity dispersion (cross-window std of recratio)
def f20wc_f20_working_capital_dynamics_recdisp_multi_base_v066_signal(receivables, revenue):
    r = _f20_recratio(receivables, revenue)
    r1 = _mean(r, 63)
    r2 = _mean(r, 126)
    r3 = _mean(r, 252)
    b = pd.concat([r1, r2, r3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DPO sustainability: payables ratio vs its own 504d rank (stretch extremity)
def f20wc_f20_working_capital_dynamics_dpostretch_504d_base_v067_signal(payables, cor):
    p = _f20_payratio(payables, cor)
    b = _rank(p, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CCC vs working-capital intensity interaction (efficient-cycle composite)
def f20wc_f20_working_capital_dynamics_cccwcint_252d_base_v068_signal(receivables, inventory, payables, revenue, cor, assetsc, liabilitiesc):
    c = _z(_f20_ccc(receivables, inventory, payables, revenue, cor, 126), 252)
    wc = _f20_wc(assetsc, liabilitiesc)
    wint = _z(wc / revenue.replace(0, np.nan), 252)
    b = c + wint
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory turnover trend (slope of cor/inventory)
def f20wc_f20_working_capital_dynamics_invturntrend_252d_base_v069_signal(cor, inventory):
    t = cor / inventory.replace(0, np.nan)
    b = _slope(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables turnover trend (slope of revenue/receivables)
def f20wc_f20_working_capital_dynamics_recturntrend_252d_base_v070_signal(revenue, receivables):
    t = revenue / receivables.replace(0, np.nan)
    b = _slope(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC-to-current-assets ratio (working-capital cushion)
def f20wc_f20_working_capital_dynamics_wccushion_126d_base_v071_signal(assetsc, liabilitiesc):
    wc = _f20_wc(assetsc, liabilitiesc)
    b = _mean(wc / assetsc.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO local oscillation: short-window DSO deviation from its own EMA, scaled (collection noise)
def f20wc_f20_working_capital_dynamics_dsohit_252d_base_v072_signal(receivables, revenue):
    d = _f20_dso(receivables, revenue, 21)
    resid = d - d.ewm(span=63, min_periods=21).mean()
    b = resid / d.ewm(span=63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DIO local oscillation: short-window DIO deviation from its own EMA, scaled (stocking noise)
def f20wc_f20_working_capital_dynamics_diohit_252d_base_v073_signal(inventory, cor):
    d = _f20_dio(inventory, cor, 21)
    resid = d - d.ewm(span=63, min_periods=21).mean()
    b = resid / d.ewm(span=63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asymmetry of CCC: skew of cycle distribution over a year
def f20wc_f20_working_capital_dynamics_cccskew_252d_base_v074_signal(receivables, inventory, payables, revenue, cor):
    c = _f20_ccc(receivables, inventory, payables, revenue, cor, 63)
    b = c.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite turnover efficiency: z-scored receivables + inventory turnover vs payables turnover
def f20wc_f20_working_capital_dynamics_effrank_504d_base_v075_signal(receivables, inventory, payables, revenue, cor):
    rec_t = _z(revenue / receivables.replace(0, np.nan), 252)
    inv_t = _z(cor / inventory.replace(0, np.nan), 252)
    pay_t = _z(cor / payables.replace(0, np.nan), 252)
    b = rec_t + inv_t - pay_t
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20wc_f20_working_capital_dynamics_dso_252d_base_v001_signal,
    f20wc_f20_working_capital_dynamics_dsoz_252d_base_v002_signal,
    f20wc_f20_working_capital_dynamics_dsorank_504d_base_v003_signal,
    f20wc_f20_working_capital_dynamics_dio_252d_base_v004_signal,
    f20wc_f20_working_capital_dynamics_dioz_252d_base_v005_signal,
    f20wc_f20_working_capital_dynamics_diorank_504d_base_v006_signal,
    f20wc_f20_working_capital_dynamics_dpo_252d_base_v007_signal,
    f20wc_f20_working_capital_dynamics_dpoz_252d_base_v008_signal,
    f20wc_f20_working_capital_dynamics_dporank_504d_base_v009_signal,
    f20wc_f20_working_capital_dynamics_ccc_252d_base_v010_signal,
    f20wc_f20_working_capital_dynamics_cccz_252d_base_v011_signal,
    f20wc_f20_working_capital_dynamics_cccratio_504d_base_v012_signal,
    f20wc_f20_working_capital_dynamics_opcyc_252d_base_v013_signal,
    f20wc_f20_working_capital_dynamics_wcint_252d_base_v014_signal,
    f20wc_f20_working_capital_dynamics_wcintz_252d_base_v015_signal,
    f20wc_f20_working_capital_dynamics_recrev_126d_base_v016_signal,
    f20wc_f20_working_capital_dynamics_recrevtrend_252d_base_v017_signal,
    f20wc_f20_working_capital_dynamics_invcor_126d_base_v018_signal,
    f20wc_f20_working_capital_dynamics_invbuild_252d_base_v019_signal,
    f20wc_f20_working_capital_dynamics_paycor_126d_base_v020_signal,
    f20wc_f20_working_capital_dynamics_dsotrend_252d_base_v021_signal,
    f20wc_f20_working_capital_dynamics_diotrend_252d_base_v022_signal,
    f20wc_f20_working_capital_dynamics_dpotrend_252d_base_v023_signal,
    f20wc_f20_working_capital_dynamics_ccctrend_252d_base_v024_signal,
    f20wc_f20_working_capital_dynamics_curratio_63d_base_v025_signal,
    f20wc_f20_working_capital_dynamics_curratioz_252d_base_v026_signal,
    f20wc_f20_working_capital_dynamics_recshare_126d_base_v027_signal,
    f20wc_f20_working_capital_dynamics_invshare_126d_base_v028_signal,
    f20wc_f20_working_capital_dynamics_payshare_126d_base_v029_signal,
    f20wc_f20_working_capital_dynamics_quick_63d_base_v030_signal,
    f20wc_f20_working_capital_dynamics_dsominusdpo_252d_base_v031_signal,
    f20wc_f20_working_capital_dynamics_diominusdpo_252d_base_v032_signal,
    f20wc_f20_working_capital_dynamics_recvsrev_252d_base_v033_signal,
    f20wc_f20_working_capital_dynamics_payvscor_252d_base_v034_signal,
    f20wc_f20_working_capital_dynamics_wcgrowth_252d_base_v035_signal,
    f20wc_f20_working_capital_dynamics_dsodisp_126d_base_v036_signal,
    f20wc_f20_working_capital_dynamics_diodisp_126d_base_v037_signal,
    f20wc_f20_working_capital_dynamics_cccdisp_252d_base_v038_signal,
    f20wc_f20_working_capital_dynamics_dsocv_252d_base_v039_signal,
    f20wc_f20_working_capital_dynamics_cccyoy_252d_base_v040_signal,
    f20wc_f20_working_capital_dynamics_dsoyoy_252d_base_v041_signal,
    f20wc_f20_working_capital_dynamics_dioyoy_252d_base_v042_signal,
    f20wc_f20_working_capital_dynamics_cccwt_252d_base_v043_signal,
    f20wc_f20_working_capital_dynamics_invrec_126d_base_v044_signal,
    f20wc_f20_working_capital_dynamics_payrec_126d_base_v045_signal,
    f20wc_f20_working_capital_dynamics_nowc_252d_base_v046_signal,
    f20wc_f20_working_capital_dynamics_nowcz_252d_base_v047_signal,
    f20wc_f20_working_capital_dynamics_dsomom_63d_base_v048_signal,
    f20wc_f20_working_capital_dynamics_diomom_63d_base_v049_signal,
    f20wc_f20_working_capital_dynamics_dpomom_63d_base_v050_signal,
    f20wc_f20_working_capital_dynamics_wcturn_252d_base_v051_signal,
    f20wc_f20_working_capital_dynamics_recturn_126d_base_v052_signal,
    f20wc_f20_working_capital_dynamics_invturn_126d_base_v053_signal,
    f20wc_f20_working_capital_dynamics_payturn_126d_base_v054_signal,
    f20wc_f20_working_capital_dynamics_dsosignmag_252d_base_v055_signal,
    f20wc_f20_working_capital_dynamics_ccctanh_63d_base_v056_signal,
    f20wc_f20_working_capital_dynamics_invbuildint_252d_base_v057_signal,
    f20wc_f20_working_capital_dynamics_dsodisp2_base_v058_signal,
    f20wc_f20_working_capital_dynamics_cccema_base_v059_signal,
    f20wc_f20_working_capital_dynamics_recrevaccl_252d_base_v060_signal,
    f20wc_f20_working_capital_dynamics_definterval_252d_base_v061_signal,
    f20wc_f20_working_capital_dynamics_cccshare_252d_base_v062_signal,
    f20wc_f20_working_capital_dynamics_curlevdrift_252d_base_v063_signal,
    f20wc_f20_working_capital_dynamics_dioextreme_252d_base_v064_signal,
    f20wc_f20_working_capital_dynamics_wcaccrual_252d_base_v065_signal,
    f20wc_f20_working_capital_dynamics_recdisp_multi_base_v066_signal,
    f20wc_f20_working_capital_dynamics_dpostretch_504d_base_v067_signal,
    f20wc_f20_working_capital_dynamics_cccwcint_252d_base_v068_signal,
    f20wc_f20_working_capital_dynamics_invturntrend_252d_base_v069_signal,
    f20wc_f20_working_capital_dynamics_recturntrend_252d_base_v070_signal,
    f20wc_f20_working_capital_dynamics_wccushion_126d_base_v071_signal,
    f20wc_f20_working_capital_dynamics_dsohit_252d_base_v072_signal,
    f20wc_f20_working_capital_dynamics_diohit_252d_base_v073_signal,
    f20wc_f20_working_capital_dynamics_cccskew_252d_base_v074_signal,
    f20wc_f20_working_capital_dynamics_effrank_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_WORKING_CAPITAL_DYNAMICS_REGISTRY_001_075 = REGISTRY


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

    print("OK f20_working_capital_dynamics_base_001_075_claude: %d features pass" % n_features)
