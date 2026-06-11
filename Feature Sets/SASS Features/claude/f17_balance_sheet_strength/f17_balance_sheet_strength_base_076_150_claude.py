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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _med(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).median()


# ===== folder domain primitives (balance-sheet strength: levels) =====
def _f17_net_debt_to_equity(debt, cashneq, equity):
    return _safe_div(debt - cashneq, equity)


def _f17_debt_to_assets(debt, assets):
    return _safe_div(debt, assets)


def _f17_equity_to_assets(equity, assets):
    return _safe_div(equity, assets)


def _f17_liab_to_assets(liabilities, assets):
    return _safe_div(liabilities, assets)


def _f17_cash_to_assets(cashneq, assets):
    return _safe_div(cashneq, assets)


def _f17_wc_to_assets(workingcapital, assets):
    return _safe_div(workingcapital, assets)


def _f17_cash_to_debt(cashneq, debt):
    return _safe_div(cashneq, debt)


def _f17_debtcap(debt, equity):
    return _safe_div(debt, debt + equity)


# ============================================================
# net debt / assets (level)
def f17bs_f17_balance_sheet_strength_ndta_lvl_base_v076_signal(debt, cashneq, assets):
    b = _safe_div(debt - cashneq, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt / assets smoothed over a quarter
def f17bs_f17_balance_sheet_strength_ndta_63d_base_v077_signal(debt, cashneq, assets):
    b = _mean(_safe_div(debt - cashneq, assets), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt / assets percentile-ranked over 252d
def f17bs_f17_balance_sheet_strength_ndtarank_252d_base_v078_signal(debt, cashneq, assets):
    b = _rank(_safe_div(debt - cashneq, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity / debt (inverse leverage, equity coverage of debt)
def f17bs_f17_balance_sheet_strength_etd_lvl_base_v079_signal(equity, debt):
    b = _safe_div(equity, debt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity / debt z-scored over 252d (equity-cushion extremity)
def f17bs_f17_balance_sheet_strength_etdz_252d_base_v080_signal(equity, debt):
    b = _z(_safe_div(equity, debt), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt / liabilities (debt share of total obligations)
def f17bs_f17_balance_sheet_strength_dtl_lvl_base_v081_signal(debt, liabilities):
    b = _safe_div(debt, liabilities)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt / liabilities smoothed over half a year
def f17bs_f17_balance_sheet_strength_dtl_126d_base_v082_signal(debt, liabilities):
    b = _mean(_safe_div(debt, liabilities), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash + working-capital coverage of debt ((cash+wc)/debt liquidity-vs-debt)
def f17bs_f17_balance_sheet_strength_liqtod_lvl_base_v083_signal(cashneq, workingcapital, debt):
    b = _safe_div(cashneq + workingcapital, debt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio relative to its 252d median (liquidity displacement)
def f17bs_f17_balance_sheet_strength_currdisp_252d_base_v084_signal(currentratio):
    b = currentratio - _med(currentratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio percentile-ranked over 504d (long liquidity extremity)
def f17bs_f17_balance_sheet_strength_currrank_504d_base_v085_signal(currentratio):
    b = _rank(currentratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio harmonic with cash/assets (liquidity from two sources)
def f17bs_f17_balance_sheet_strength_liqdual_lvl_base_v086_signal(currentratio, cashneq, assets):
    cta = _f17_cash_to_assets(cashneq, assets)
    b = _safe_div(2.0 * currentratio * cta, currentratio + cta)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital / liabilities z-scored over 252d (wc-coverage extremity)
def f17bs_f17_balance_sheet_strength_wctlz_252d_base_v087_signal(workingcapital, liabilities):
    b = _z(_safe_div(workingcapital, liabilities), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital / equity (wc as share of book value)
def f17bs_f17_balance_sheet_strength_wcte_lvl_base_v088_signal(workingcapital, equity):
    b = _safe_div(workingcapital, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash / equity (cash backing of book value)
def f17bs_f17_balance_sheet_strength_cte_lvl_base_v089_signal(cashneq, equity):
    b = _safe_div(cashneq, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash / equity percentile-ranked over 252d
def f17bs_f17_balance_sheet_strength_cterank_252d_base_v090_signal(cashneq, equity):
    b = _rank(_safe_div(cashneq, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage spread: debtcap minus liabilities/assets (debt-vs-total-liab structure)
def f17bs_f17_balance_sheet_strength_capliabspr_base_v091_signal(debt, equity, liabilities, assets):
    b = _f17_debtcap(debt, equity) - _f17_liab_to_assets(liabilities, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets relative to its 252d min (leverage build off trough)
def f17bs_f17_balance_sheet_strength_dtabuild_252d_base_v092_signal(debt, assets):
    dta = _f17_debt_to_assets(debt, assets)
    b = dta - _rmin(dta, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets relative to its 252d max (capitalization drawdown)
def f17bs_f17_balance_sheet_strength_etadd_252d_base_v093_signal(equity, assets):
    eta = _f17_equity_to_assets(equity, assets)
    b = _safe_div(eta, _rmax(eta, 252)) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/assets relative to its 252d max (obligation peak proximity)
def f17bs_f17_balance_sheet_strength_ltapeak_252d_base_v094_signal(liabilities, assets):
    lta = _f17_liab_to_assets(liabilities, assets)
    b = _safe_div(lta, _rmax(lta, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity buffer hit-rate: fraction of quarter cash/assets above its 252d median
def f17bs_f17_balance_sheet_strength_ctahit_63d_base_v095_signal(cashneq, assets):
    cta = _f17_cash_to_assets(cashneq, assets)
    above = (cta > _med(cta, 252)).astype(float)
    b = above.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage hit-rate: fraction of quarter debt/assets above its 252d median (creeping leverage)
def f17bs_f17_balance_sheet_strength_dtahit_63d_base_v096_signal(debt, assets):
    dta = _f17_debt_to_assets(debt, assets)
    above = (dta > _med(dta, 252)).astype(float)
    b = above.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash balance: (cash - debt) / (cash + debt) (signed liquidity-vs-leverage position)
def f17bs_f17_balance_sheet_strength_netcashbal_base_v097_signal(cashneq, debt):
    b = _safe_div(cashneq - debt, cashneq + debt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets minus liabilities/assets (book-strength net of obligations)
def f17bs_f17_balance_sheet_strength_etanetlta_base_v098_signal(equity, liabilities, assets):
    b = _f17_equity_to_assets(equity, assets) - _f17_liab_to_assets(liabilities, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-coverage product: cash/debt x equity/liabilities (joint coverage strength)
def f17bs_f17_balance_sheet_strength_jointcov_lvl_base_v099_signal(cashneq, debt, equity, liabilities):
    b = _f17_cash_to_debt(cashneq, debt) * _safe_div(equity, liabilities)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtcap displacement from its 252d median, tanh-bounded (capital-structure anomaly)
def f17bs_f17_balance_sheet_strength_debtcapanom_base_v100_signal(debt, equity):
    dc = _f17_debtcap(debt, equity)
    b = np.tanh(4.0 * (dc - _med(dc, 252)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD net debt / equity (FX-consistent net leverage)
def f17bs_f17_balance_sheet_strength_ndusde_lvl_base_v101_signal(debtusd, cashneq, equity):
    b = _safe_div(debtusd - cashneq, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD debt / equity z-scored over 252d
def f17bs_f17_balance_sheet_strength_dusdez_252d_base_v102_signal(debtusd, equity):
    b = _z(_safe_div(debtusd, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-vs-reported debt gap scaled by assets (FX-translation leverage drift)
def f17bs_f17_balance_sheet_strength_fxdebtgap_base_v103_signal(debtusd, debt, assets):
    b = _safe_div(debtusd - debt, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-ratio momentum-free strength weighted by net-cash (liquidity x solvency gate)
def f17bs_f17_balance_sheet_strength_currnetcash_base_v104_signal(currentratio, cashneq, debt):
    gate = np.tanh(_f17_cash_to_debt(cashneq, debt) - 1.0)
    b = (currentratio - 1.0) * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash/assets dispersion over half a year (cash-buffer volatility)
def f17bs_f17_balance_sheet_strength_ctadisp_126d_base_v105_signal(cashneq, assets):
    b = _std(_f17_cash_to_assets(cashneq, assets), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/assets dispersion over a quarter (liquidity-buffer volatility)
def f17bs_f17_balance_sheet_strength_wctadisp_63d_base_v106_signal(workingcapital, assets):
    b = _std(_f17_wc_to_assets(workingcapital, assets), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/equity dispersion over half a year (gearing instability)
def f17bs_f17_balance_sheet_strength_ltedisp_126d_base_v107_signal(liabilities, equity):
    b = _std(_safe_div(liabilities, equity), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital debt-coverage sign x magnitude: sqrt-scaled (wc/debt - 1)
def f17bs_f17_balance_sheet_strength_wccovsignmag_base_v108_signal(workingcapital, debt):
    x = _safe_div(workingcapital, debt) - 1.0
    b = np.sign(x) * x.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-assets tanh-bounded deviation from 0.5 (capitalization extremity)
def f17bs_f17_balance_sheet_strength_etatanh_base_v109_signal(equity, assets):
    eta = _f17_equity_to_assets(equity, assets)
    b = np.tanh(3.0 * (eta - 0.5))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended strength score z: z(equity/assets) - z(debt/assets) + z(cash/assets)
def f17bs_f17_balance_sheet_strength_blendz_base_v110_signal(equity, debt, cashneq, assets):
    b = (_z(_f17_equity_to_assets(equity, assets), 252)
         - _z(_f17_debt_to_assets(debt, assets), 252)
         + _z(_f17_cash_to_assets(cashneq, assets), 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-ratio x cash/assets minus debt/assets (net liquidity-vs-leverage score)
def f17bs_f17_balance_sheet_strength_netliqscore_base_v111_signal(currentratio, cashneq, assets, debt):
    b = currentratio * _f17_cash_to_assets(cashneq, assets) - _f17_debt_to_assets(debt, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log equity/liabilities (compressed solvency scale)
def f17bs_f17_balance_sheet_strength_logetl_base_v112_signal(equity, liabilities):
    b = np.log(_safe_div(equity, liabilities))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log assets/liabilities (coverage of obligations by assets, compressed)
def f17bs_f17_balance_sheet_strength_logatl_base_v113_signal(assets, liabilities):
    b = np.log(_safe_div(assets, liabilities))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtcap change over a quarter (capital-structure shift toward debt)
def f17bs_f17_balance_sheet_strength_capshift_63d_base_v114_signal(debt, equity):
    dc = _f17_debtcap(debt, equity)
    b = dc - dc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt/assets change over half a year (deleveraging vs releveraging)
def f17bs_f17_balance_sheet_strength_ndtachg_126d_base_v115_signal(debt, cashneq, assets):
    nd = _safe_div(debt - cashneq, assets)
    b = nd - nd.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash/assets change over a quarter (cash accumulation/depletion rate as level diff)
def f17bs_f17_balance_sheet_strength_ctachg_63d_base_v116_signal(cashneq, assets):
    cta = _f17_cash_to_assets(cashneq, assets)
    b = cta - cta.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets x current ratio z-scored (joint capitalization-liquidity composite)
def f17bs_f17_balance_sheet_strength_capliqz_base_v117_signal(equity, assets, currentratio):
    comp = _f17_equity_to_assets(equity, assets) * currentratio
    b = _z(comp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between strongest and weakest liquidity buffer (buffer disagreement)
def f17bs_f17_balance_sheet_strength_bufspread_base_v118_signal(cashneq, workingcapital, assets, currentratio):
    cta = _f17_cash_to_assets(cashneq, assets)
    wcta = _f17_wc_to_assets(workingcapital, assets)
    cr = (currentratio - 1.0) / 2.0
    stacked = pd.concat([cta, wcta, cr], axis=1)
    b = stacked.max(axis=1) - stacked.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of strength ratios (balance-sheet metric disagreement)
def f17bs_f17_balance_sheet_strength_metricdisp_base_v119_signal(equity, debt, cashneq, assets):
    eta = _f17_equity_to_assets(equity, assets)
    dta = _f17_debt_to_assets(debt, assets)
    cta = _f17_cash_to_assets(cashneq, assets)
    b = pd.concat([eta, dta, cta], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net cash / market-proxy (cash net of debt scaled by equity, signed coverage)
def f17bs_f17_balance_sheet_strength_netcashte_base_v120_signal(cashneq, debt, equity):
    b = _safe_div(cashneq - debt, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage tightening streak: consecutive quarters of rising debt/assets (count proxy)
def f17bs_f17_balance_sheet_strength_levstreak_base_v121_signal(debt, assets):
    dta = _f17_debt_to_assets(debt, assets)
    up = (dta > dta.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-build streak: fraction of year cash/assets rose month-over-month
def f17bs_f17_balance_sheet_strength_cashbuild_base_v122_signal(cashneq, assets):
    cta = _f17_cash_to_assets(cashneq, assets)
    up = (cta > cta.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets EMA-smoothed minus its 252d mean (capitalization regime displacement)
def f17bs_f17_balance_sheet_strength_etaregime_base_v123_signal(equity, assets):
    eta = _f17_equity_to_assets(equity, assets)
    sm = eta.ewm(span=42, min_periods=21).mean()
    b = sm - _mean(eta, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets EMA-smoothed minus its 252d mean (leverage regime displacement)
def f17bs_f17_balance_sheet_strength_dtaregime_base_v124_signal(debt, assets):
    dta = _f17_debt_to_assets(debt, assets)
    sm = dta.ewm(span=42, min_periods=21).mean()
    b = sm - _mean(dta, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity buffer asymmetry: cash/assets vs working-capital/assets ratio (composition tilt)
def f17bs_f17_balance_sheet_strength_buftilt_base_v125_signal(cashneq, workingcapital, assets):
    cta = _f17_cash_to_assets(cashneq, assets)
    wcta = _f17_wc_to_assets(workingcapital, assets)
    b = _safe_div(cta, cta + wcta.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# solvency-cushion momentum: change in (assets-liabilities)/assets over a quarter
def f17bs_f17_balance_sheet_strength_solvcushchg_base_v126_signal(assets, liabilities):
    cush = _safe_div(assets - liabilities, assets)
    b = cush - cush.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt / (cash + equity) (leverage vs liquid+book capital)
def f17bs_f17_balance_sheet_strength_dtoce_base_v127_signal(debt, cashneq, equity):
    b = _safe_div(debt, cashneq + equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity coverage rank of (cash+wc) vs liabilities over 252d
def f17bs_f17_balance_sheet_strength_liqcovrank_base_v128_signal(cashneq, workingcapital, liabilities):
    b = _rank(_safe_div(cashneq + workingcapital, liabilities), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-ratio x equity/liabilities (combined short+long solvency)
def f17bs_f17_balance_sheet_strength_shortlong_base_v129_signal(currentratio, equity, liabilities):
    b = currentratio * _safe_div(equity, liabilities)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt/equity recovery off its 504d trough (deleveraging-from-peak-leverage gap)
def f17bs_f17_balance_sheet_strength_ndtetrough_base_v130_signal(debt, cashneq, equity):
    nd = _f17_net_debt_to_equity(debt, cashneq, equity)
    b = _rmax(nd, 504) - nd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash/liabilities (cash coverage of all obligations)
def f17bs_f17_balance_sheet_strength_ctl_lvl_base_v131_signal(cashneq, liabilities):
    b = _safe_div(cashneq, liabilities)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash/liabilities smoothed over a quarter
def f17bs_f17_balance_sheet_strength_ctl_63d_base_v132_signal(cashneq, liabilities):
    b = _mean(_safe_div(cashneq, liabilities), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/assets tanh deviation from 0 (bounded liquidity sign-strength)
def f17bs_f17_balance_sheet_strength_wctatanh_base_v133_signal(workingcapital, assets):
    wcta = _f17_wc_to_assets(workingcapital, assets)
    b = np.tanh(5.0 * wcta)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-to-liquidity ratio: (debt/assets) / current ratio (stress per unit liquidity)
def f17bs_f17_balance_sheet_strength_levperliq_base_v134_signal(debt, assets, currentratio):
    b = _safe_div(_f17_debt_to_assets(debt, assets), currentratio)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/debt minus its 252d mean (equity-cushion displacement)
def f17bs_f17_balance_sheet_strength_etddisp_base_v135_signal(equity, debt):
    etd = _safe_div(equity, debt)
    b = etd - _mean(etd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Altman working-capital term ranked over 504d (long distress-buffer extremity)
def f17bs_f17_balance_sheet_strength_altwcrank_base_v136_signal(workingcapital, assets):
    b = _rank(1.2 * _f17_wc_to_assets(workingcapital, assets), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-to-debt minus current-ratio-cushion (coverage-source divergence)
def f17bs_f17_balance_sheet_strength_covsrcdiv_base_v137_signal(cashneq, debt, currentratio):
    b = _z(_f17_cash_to_debt(cashneq, debt), 252) - _z(currentratio - 1.0, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt/equity above 1.0 flag persistence (highly-levered regime duration)
def f17bs_f17_balance_sheet_strength_highlevpers_base_v138_signal(debt, cashneq, equity):
    nd = _f17_net_debt_to_equity(debt, cashneq, equity)
    hi = (nd > 1.0).astype(float)
    b = hi.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# assets/equity (financial leverage multiplier)
def f17bs_f17_balance_sheet_strength_ate_lvl_base_v139_signal(assets, equity):
    b = _safe_div(assets, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# assets/equity z-scored over 252d (leverage-multiplier extremity)
def f17bs_f17_balance_sheet_strength_atez_252d_base_v140_signal(assets, equity):
    b = _z(_safe_div(assets, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtusd/liabilities (USD debt share of obligations)
def f17bs_f17_balance_sheet_strength_dusdtl_base_v141_signal(debtusd, liabilities):
    b = _safe_div(debtusd, liabilities)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage breadth: count of {high d/a, low curr, neg wc} stress signals
def f17bs_f17_balance_sheet_strength_stresscount_base_v142_signal(debt, assets, currentratio, workingcapital):
    dta = _f17_debt_to_assets(debt, assets)
    s1 = (dta > _med(dta, 252)).astype(float)
    s2 = (currentratio < 1.5).astype(float)
    s3 = (workingcapital < 0).astype(float)
    b = (s1 + s2 + s3).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets x cash/debt (capitalization x coverage strength composite)
def f17bs_f17_balance_sheet_strength_capcov_base_v143_signal(equity, assets, cashneq, debt):
    b = _f17_equity_to_assets(equity, assets) * _f17_cash_to_debt(cashneq, debt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt/assets z minus net-debt/equity z (leverage-base divergence)
def f17bs_f17_balance_sheet_strength_levbasediv_base_v144_signal(debt, cashneq, assets, equity):
    nda = _z(_safe_div(debt - cashneq, assets), 252)
    nde = _z(_f17_net_debt_to_equity(debt, cashneq, equity), 252)
    b = nda - nde
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/equity gearing percentile-ranked over 504d (long gearing extremity)
def f17bs_f17_balance_sheet_strength_lterank_504d_base_v145_signal(liabilities, equity):
    b = _rank(_safe_div(liabilities, equity), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/assets recovery off 252d trough (liquidity rebuild)
def f17bs_f17_balance_sheet_strength_wctarecov_base_v146_signal(workingcapital, assets):
    wcta = _f17_wc_to_assets(workingcapital, assets)
    b = wcta - _rmin(wcta, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-runway proxy: cash/assets x current ratio z-scored (liquidity-runway extremity)
def f17bs_f17_balance_sheet_strength_runwayz_base_v147_signal(cashneq, assets, currentratio):
    comp = _f17_cash_to_assets(cashneq, assets) * currentratio
    b = _z(comp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt covered by working capital: 1 - working-capital/debt clipped (liquidity-uncovered leverage)
def f17bs_f17_balance_sheet_strength_wcuncov_base_v148_signal(debt, workingcapital, assets):
    cov = _safe_div(workingcapital, debt).clip(lower=0.0, upper=2.0)
    b = _f17_debt_to_assets(debt, assets) * (2.0 - cov)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite balance-sheet strength score ranked over 504d
def f17bs_f17_balance_sheet_strength_strrank_504d_base_v149_signal(equity, assets, debt, cashneq, currentratio):
    comp = (_f17_equity_to_assets(equity, assets)
            - _f17_debt_to_assets(debt, assets)
            + 0.25 * _f17_cash_to_assets(cashneq, assets)
            + 0.1 * (currentratio - 1.0))
    b = _rank(comp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fragility index: debt/assets x (1 - cash/debt clipped) x 1/current-ratio (multiplicative stress)
def f17bs_f17_balance_sheet_strength_fragility_base_v150_signal(debt, assets, cashneq, currentratio):
    cov = _f17_cash_to_debt(cashneq, debt).clip(upper=1.0)
    b = _f17_debt_to_assets(debt, assets) * (1.0 - cov) * _safe_div(pd.Series(1.0, index=currentratio.index), currentratio)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17bs_f17_balance_sheet_strength_ndta_lvl_base_v076_signal,
    f17bs_f17_balance_sheet_strength_ndta_63d_base_v077_signal,
    f17bs_f17_balance_sheet_strength_ndtarank_252d_base_v078_signal,
    f17bs_f17_balance_sheet_strength_etd_lvl_base_v079_signal,
    f17bs_f17_balance_sheet_strength_etdz_252d_base_v080_signal,
    f17bs_f17_balance_sheet_strength_dtl_lvl_base_v081_signal,
    f17bs_f17_balance_sheet_strength_dtl_126d_base_v082_signal,
    f17bs_f17_balance_sheet_strength_liqtod_lvl_base_v083_signal,
    f17bs_f17_balance_sheet_strength_currdisp_252d_base_v084_signal,
    f17bs_f17_balance_sheet_strength_currrank_504d_base_v085_signal,
    f17bs_f17_balance_sheet_strength_liqdual_lvl_base_v086_signal,
    f17bs_f17_balance_sheet_strength_wctlz_252d_base_v087_signal,
    f17bs_f17_balance_sheet_strength_wcte_lvl_base_v088_signal,
    f17bs_f17_balance_sheet_strength_cte_lvl_base_v089_signal,
    f17bs_f17_balance_sheet_strength_cterank_252d_base_v090_signal,
    f17bs_f17_balance_sheet_strength_capliabspr_base_v091_signal,
    f17bs_f17_balance_sheet_strength_dtabuild_252d_base_v092_signal,
    f17bs_f17_balance_sheet_strength_etadd_252d_base_v093_signal,
    f17bs_f17_balance_sheet_strength_ltapeak_252d_base_v094_signal,
    f17bs_f17_balance_sheet_strength_ctahit_63d_base_v095_signal,
    f17bs_f17_balance_sheet_strength_dtahit_63d_base_v096_signal,
    f17bs_f17_balance_sheet_strength_netcashbal_base_v097_signal,
    f17bs_f17_balance_sheet_strength_etanetlta_base_v098_signal,
    f17bs_f17_balance_sheet_strength_jointcov_lvl_base_v099_signal,
    f17bs_f17_balance_sheet_strength_debtcapanom_base_v100_signal,
    f17bs_f17_balance_sheet_strength_ndusde_lvl_base_v101_signal,
    f17bs_f17_balance_sheet_strength_dusdez_252d_base_v102_signal,
    f17bs_f17_balance_sheet_strength_fxdebtgap_base_v103_signal,
    f17bs_f17_balance_sheet_strength_currnetcash_base_v104_signal,
    f17bs_f17_balance_sheet_strength_ctadisp_126d_base_v105_signal,
    f17bs_f17_balance_sheet_strength_wctadisp_63d_base_v106_signal,
    f17bs_f17_balance_sheet_strength_ltedisp_126d_base_v107_signal,
    f17bs_f17_balance_sheet_strength_wccovsignmag_base_v108_signal,
    f17bs_f17_balance_sheet_strength_etatanh_base_v109_signal,
    f17bs_f17_balance_sheet_strength_blendz_base_v110_signal,
    f17bs_f17_balance_sheet_strength_netliqscore_base_v111_signal,
    f17bs_f17_balance_sheet_strength_logetl_base_v112_signal,
    f17bs_f17_balance_sheet_strength_logatl_base_v113_signal,
    f17bs_f17_balance_sheet_strength_capshift_63d_base_v114_signal,
    f17bs_f17_balance_sheet_strength_ndtachg_126d_base_v115_signal,
    f17bs_f17_balance_sheet_strength_ctachg_63d_base_v116_signal,
    f17bs_f17_balance_sheet_strength_capliqz_base_v117_signal,
    f17bs_f17_balance_sheet_strength_bufspread_base_v118_signal,
    f17bs_f17_balance_sheet_strength_metricdisp_base_v119_signal,
    f17bs_f17_balance_sheet_strength_netcashte_base_v120_signal,
    f17bs_f17_balance_sheet_strength_levstreak_base_v121_signal,
    f17bs_f17_balance_sheet_strength_cashbuild_base_v122_signal,
    f17bs_f17_balance_sheet_strength_etaregime_base_v123_signal,
    f17bs_f17_balance_sheet_strength_dtaregime_base_v124_signal,
    f17bs_f17_balance_sheet_strength_buftilt_base_v125_signal,
    f17bs_f17_balance_sheet_strength_solvcushchg_base_v126_signal,
    f17bs_f17_balance_sheet_strength_dtoce_base_v127_signal,
    f17bs_f17_balance_sheet_strength_liqcovrank_base_v128_signal,
    f17bs_f17_balance_sheet_strength_shortlong_base_v129_signal,
    f17bs_f17_balance_sheet_strength_ndtetrough_base_v130_signal,
    f17bs_f17_balance_sheet_strength_ctl_lvl_base_v131_signal,
    f17bs_f17_balance_sheet_strength_ctl_63d_base_v132_signal,
    f17bs_f17_balance_sheet_strength_wctatanh_base_v133_signal,
    f17bs_f17_balance_sheet_strength_levperliq_base_v134_signal,
    f17bs_f17_balance_sheet_strength_etddisp_base_v135_signal,
    f17bs_f17_balance_sheet_strength_altwcrank_base_v136_signal,
    f17bs_f17_balance_sheet_strength_covsrcdiv_base_v137_signal,
    f17bs_f17_balance_sheet_strength_highlevpers_base_v138_signal,
    f17bs_f17_balance_sheet_strength_ate_lvl_base_v139_signal,
    f17bs_f17_balance_sheet_strength_atez_252d_base_v140_signal,
    f17bs_f17_balance_sheet_strength_dusdtl_base_v141_signal,
    f17bs_f17_balance_sheet_strength_stresscount_base_v142_signal,
    f17bs_f17_balance_sheet_strength_capcov_base_v143_signal,
    f17bs_f17_balance_sheet_strength_levbasediv_base_v144_signal,
    f17bs_f17_balance_sheet_strength_lterank_504d_base_v145_signal,
    f17bs_f17_balance_sheet_strength_wctarecov_base_v146_signal,
    f17bs_f17_balance_sheet_strength_runwayz_base_v147_signal,
    f17bs_f17_balance_sheet_strength_wcuncov_base_v148_signal,
    f17bs_f17_balance_sheet_strength_strrank_504d_base_v149_signal,
    f17bs_f17_balance_sheet_strength_fragility_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_BALANCE_SHEET_STRENGTH_REGISTRY_076_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=1500):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    debt = _fund(1, base=4e8, drift=0.010, vol=0.22).rename("debt")
    debtusd = (_fund(2, base=4e8, drift=0.012, vol=0.20) * 1.02).rename("debtusd")
    equity = _fund(3, base=6e8, drift=0.020, vol=0.26, allow_neg=True).rename("equity")
    assets = _fund(4, base=1.5e9, drift=0.015, vol=0.18).rename("assets")
    liabilities = _fund(5, base=8e8, drift=0.008, vol=0.20).rename("liabilities")
    workingcapital = _fund(6, base=2e8, drift=0.005, vol=0.30, allow_neg=True).rename("workingcapital")
    cashneq = _fund(7, base=3e8, drift=0.025, vol=0.32).rename("cashneq")
    currentratio = (1.0 + 1.2 * (_fund(8, base=1.0, drift=0.0, vol=0.35) ** 0.5)).rename("currentratio")

    cols = {
        "debt": debt, "debtusd": debtusd, "equity": equity, "assets": assets,
        "liabilities": liabilities, "workingcapital": workingcapital,
        "cashneq": cashneq, "currentratio": currentratio,
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

    print("OK f17_balance_sheet_strength_base_076_150_claude: %d features pass" % n_features)
