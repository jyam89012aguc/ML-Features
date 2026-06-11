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


# ===== folder domain primitives (balance-sheet strength: levels) =====
def _f17_net_debt(debt, cashneq):
    # net debt = gross debt minus cash
    return debt - cashneq


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


def _f17_quick_ratio(workingcapital, currentratio):
    # liquidity buffer proxy combining current ratio with working-capital sign
    return currentratio + 0.0 * workingcapital


# ============================================================
# net debt / equity (level)
def f17bs_f17_balance_sheet_strength_ndte_lvl_base_v001_signal(debt, cashneq, equity):
    b = _f17_net_debt_to_equity(debt, cashneq, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt / equity smoothed over a quarter (persistent leverage level)
def f17bs_f17_balance_sheet_strength_ndte_63d_base_v002_signal(debt, cashneq, equity):
    b = _mean(_f17_net_debt_to_equity(debt, cashneq, equity), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt / equity z-scored vs its own 252d history (de-trended leverage)
def f17bs_f17_balance_sheet_strength_ndtez_252d_base_v003_signal(debt, cashneq, equity):
    b = _z(_f17_net_debt_to_equity(debt, cashneq, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross debt/equity z-scored over 126d (book-leverage extremity, mid-horizon)
def f17bs_f17_balance_sheet_strength_gdtez_126d_base_v004_signal(debt, equity):
    b = _z(_safe_div(debt, equity), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt / assets (level)
def f17bs_f17_balance_sheet_strength_dta_lvl_base_v005_signal(debt, assets):
    b = _f17_debt_to_assets(debt, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt / assets smoothed over half a year
def f17bs_f17_balance_sheet_strength_dta_126d_base_v006_signal(debt, assets):
    b = _mean(_f17_debt_to_assets(debt, assets), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt / assets percentile-ranked vs its own 252d history
def f17bs_f17_balance_sheet_strength_dtarank_252d_base_v007_signal(debt, assets):
    b = _rank(_f17_debt_to_assets(debt, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-denominated debt / assets (currency-consistent leverage)
def f17bs_f17_balance_sheet_strength_dusdta_lvl_base_v008_signal(debtusd, assets):
    b = _safe_div(debtusd, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio (level)
def f17bs_f17_balance_sheet_strength_curr_lvl_base_v009_signal(currentratio):
    b = currentratio
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio z-scored vs its own 252d history (de-trended liquidity)
def f17bs_f17_balance_sheet_strength_currz_252d_base_v010_signal(currentratio):
    b = _z(currentratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last quarter the current ratio held above 2.0 (strong-liquidity persistence)
def f17bs_f17_balance_sheet_strength_currstrong_63d_base_v011_signal(currentratio):
    strong = (currentratio >= 2.0).astype(float)
    b = strong.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quick-ratio proxy: current ratio penalized by working-capital-to-assets weakness
def f17bs_f17_balance_sheet_strength_quick_lvl_base_v012_signal(currentratio, workingcapital, assets):
    wc = _f17_wc_to_assets(workingcapital, assets)
    b = currentratio * (1.0 + wc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital / assets (level)
def f17bs_f17_balance_sheet_strength_wcta_lvl_base_v013_signal(workingcapital, assets):
    b = _f17_wc_to_assets(workingcapital, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital / assets smoothed over a quarter
def f17bs_f17_balance_sheet_strength_wcta_63d_base_v014_signal(workingcapital, assets):
    b = _mean(_f17_wc_to_assets(workingcapital, assets), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital / assets z-scored vs own 252d history
def f17bs_f17_balance_sheet_strength_wctaz_252d_base_v015_signal(workingcapital, assets):
    b = _z(_f17_wc_to_assets(workingcapital, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash / assets (level)
def f17bs_f17_balance_sheet_strength_cta_lvl_base_v016_signal(cashneq, assets):
    b = _f17_cash_to_assets(cashneq, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash / assets percentile-ranked vs own 252d history (liquidity buffer extremity)
def f17bs_f17_balance_sheet_strength_ctarank_252d_base_v017_signal(cashneq, assets):
    b = _rank(_f17_cash_to_assets(cashneq, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash / debt coverage (level)
def f17bs_f17_balance_sheet_strength_ctd_lvl_base_v018_signal(cashneq, debt):
    b = _f17_cash_to_debt(cashneq, debt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash / debt coverage smoothed over half a year
def f17bs_f17_balance_sheet_strength_ctd_126d_base_v019_signal(cashneq, debt):
    b = _mean(_f17_cash_to_debt(cashneq, debt), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity / assets (capitalization, level)
def f17bs_f17_balance_sheet_strength_eta_lvl_base_v020_signal(equity, assets):
    b = _f17_equity_to_assets(equity, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity / assets z-scored vs own 252d history (de-trended capitalization)
def f17bs_f17_balance_sheet_strength_etaz_252d_base_v021_signal(equity, assets):
    b = _z(_f17_equity_to_assets(equity, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities / assets (level)
def f17bs_f17_balance_sheet_strength_lta_lvl_base_v022_signal(liabilities, assets):
    b = _f17_liab_to_assets(liabilities, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities / equity (book gearing)
def f17bs_f17_balance_sheet_strength_lte_lvl_base_v023_signal(liabilities, equity):
    b = _safe_div(liabilities, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage z-score: gross debt / equity z-scored over 504d (long leverage extremity)
def f17bs_f17_balance_sheet_strength_levz_504d_base_v024_signal(debt, equity):
    b = _z(_safe_div(debt, equity), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity buffer balance: cash/assets minus working-capital/assets (cash-vs-wc liquidity mix)
def f17bs_f17_balance_sheet_strength_liqmix_lvl_base_v025_signal(cashneq, workingcapital, assets):
    cta = _f17_cash_to_assets(cashneq, assets)
    wcta = _f17_wc_to_assets(workingcapital, assets)
    b = _safe_div(cta - wcta, cta.abs() + wcta.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net cash position: (cash - debt) / assets (net liquidity, signed)
def f17bs_f17_balance_sheet_strength_netcashta_lvl_base_v026_signal(cashneq, debt, assets):
    b = _safe_div(cashneq - debt, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net cash position z-scored vs own 252d history
def f17bs_f17_balance_sheet_strength_netcashtaz_252d_base_v027_signal(cashneq, debt, assets):
    b = _z(_safe_div(cashneq - debt, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-assets ratio relative to debt-to-equity (structure of leverage, ranked)
def f17bs_f17_balance_sheet_strength_levstructrank_base_v028_signal(debt, equity, assets):
    ratio = _safe_div(_f17_equity_to_assets(equity, assets), _safe_div(debt, equity).abs())
    b = _rank(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity / liabilities (inverse gearing, solvency-from-equity)
def f17bs_f17_balance_sheet_strength_etl_lvl_base_v029_signal(equity, liabilities):
    b = _safe_div(equity, liabilities)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Altman-style equity-to-liabilities z-scored over 252d (solvency extremity)
def f17bs_f17_balance_sheet_strength_etlz_252d_base_v030_signal(equity, liabilities):
    b = _z(_safe_div(equity, liabilities), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash share of liabilities (how much debt-like obligation cash can cover)
def f17bs_f17_balance_sheet_strength_ctl_lvl_base_v031_signal(cashneq, liabilities):
    b = _safe_div(cashneq, liabilities)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital / current-ratio divergence: current-ratio strength not backed by wc/assets
def f17bs_f17_balance_sheet_strength_wccurrdiv_base_v032_signal(workingcapital, assets, currentratio):
    wc = _f17_wc_to_assets(workingcapital, assets)
    b = _z(currentratio, 252) - _z(wc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt funded by USD vs total debt mix (FX leverage composition)
def f17bs_f17_balance_sheet_strength_usdmix_lvl_base_v033_signal(debtusd, debt):
    b = _safe_div(debtusd, debt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage cushion: equity/assets minus debt/assets (net solvency margin)
def f17bs_f17_balance_sheet_strength_solvmargin_lvl_base_v034_signal(equity, debt, assets):
    b = _f17_equity_to_assets(equity, assets) - _f17_debt_to_assets(debt, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio relative to its own 252d max (liquidity drawdown)
def f17bs_f17_balance_sheet_strength_currdd_252d_base_v035_signal(currentratio):
    hi = _rmax(currentratio, 252)
    b = _safe_div(currentratio, hi) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt / equity dispersion over a quarter (leverage instability, inverse strength)
def f17bs_f17_balance_sheet_strength_ndtevol_63d_base_v036_signal(debt, cashneq, equity):
    nd = _f17_net_debt_to_equity(debt, cashneq, equity)
    b = _std(nd, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log net-debt / equity displacement vs its 252d mean (compressed leverage anomaly)
def f17bs_f17_balance_sheet_strength_logndtedisp_base_v037_signal(debt, cashneq, equity):
    nd = (debt - cashneq)
    lg = np.sign(nd) * np.log1p((nd / equity.replace(0, np.nan)).abs())
    b = lg - _mean(lg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash buffer quality divergence: z(cash/assets) minus z(current ratio) (cash-heavy vs ratio-heavy)
def f17bs_f17_balance_sheet_strength_cashqualdiv_base_v038_signal(cashneq, assets, currentratio):
    b = _z(_f17_cash_to_assets(cashneq, assets), 252) - _z(currentratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# solvency-liquidity agreement: z(equity/assets) plus z(current ratio) (joint-strength composite)
def f17bs_f17_balance_sheet_strength_solvliqcombo_base_v039_signal(equity, assets, currentratio):
    b = _z(_f17_equity_to_assets(equity, assets), 252) + _z(currentratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt / assets dispersion over a quarter (leverage stability, inverse strength)
def f17bs_f17_balance_sheet_strength_dtadisp_63d_base_v040_signal(debt, assets):
    b = _std(_f17_debt_to_assets(debt, assets), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity / assets dispersion over half a year (capitalization stability)
def f17bs_f17_balance_sheet_strength_etadisp_126d_base_v041_signal(equity, assets):
    b = _std(_f17_equity_to_assets(equity, assets), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities-to-assets z-scored over 504d (long obligation extremity)
def f17bs_f17_balance_sheet_strength_ltaz_504d_base_v042_signal(liabilities, assets):
    b = _z(_f17_liab_to_assets(liabilities, assets), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash / debt percentile rank over 504d (long liquidity-coverage extremity)
def f17bs_f17_balance_sheet_strength_ctdrank_504d_base_v043_signal(cashneq, debt):
    b = _rank(_f17_cash_to_debt(cashneq, debt), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital / assets relative to its 252d mean (liquidity displacement)
def f17bs_f17_balance_sheet_strength_wctadisp_252d_base_v044_signal(workingcapital, assets):
    wc = _f17_wc_to_assets(workingcapital, assets)
    b = wc - _mean(wc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt level in USD scaled by assets (net USD leverage)
def f17bs_f17_balance_sheet_strength_netusdta_lvl_base_v045_signal(debtusd, cashneq, assets):
    b = _safe_div(debtusd - cashneq, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Altman-Z liquidity term momentum: change in 1.2*wc/assets over a quarter (distress drift)
def f17bs_f17_balance_sheet_strength_altmanwc_chg_base_v046_signal(workingcapital, assets):
    t = 1.2 * _f17_wc_to_assets(workingcapital, assets)
    b = t - t.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Altman-Z solvency term percentile-ranked over 252d (equity/liab extremity)
def f17bs_f17_balance_sheet_strength_altmaneq_rank_base_v047_signal(equity, liabilities):
    b = _rank(_safe_div(equity, liabilities), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined leverage-liquidity strength score (equity/assets + cash/debt - debt/assets)
def f17bs_f17_balance_sheet_strength_strscore_lvl_base_v048_signal(equity, assets, cashneq, debt):
    b = (_f17_equity_to_assets(equity, assets)
         + 0.25 * _f17_cash_to_debt(cashneq, debt)
         - _f17_debt_to_assets(debt, assets))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio per unit of leverage: currentratio / (1 + debt/equity) (liquidity net of gearing)
def f17bs_f17_balance_sheet_strength_currpergear_base_v049_signal(currentratio, debt, equity):
    b = _safe_div(currentratio, 1.0 + _safe_div(debt, equity).abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt / equity smoothed with exponential weighting (recent-leaning leverage level)
def f17bs_f17_balance_sheet_strength_gdteema_base_v050_signal(debt, equity):
    de = _safe_div(debt, equity)
    b = de.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity / assets fast-vs-slow EMA crossover (capitalization trend displacement)
def f17bs_f17_balance_sheet_strength_etaemacross_base_v051_signal(equity, assets):
    eta = _f17_equity_to_assets(equity, assets)
    b = eta.ewm(span=21, min_periods=10).mean() - eta.ewm(span=84, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash / assets minus its slow EMA (cash-buffer displacement)
def f17bs_f17_balance_sheet_strength_ctadisp_ema_base_v052_signal(cashneq, assets):
    cta = _f17_cash_to_assets(cashneq, assets)
    b = cta - cta.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage tanh-squashed change over a quarter (bounded net-debt/equity momentum)
def f17bs_f17_balance_sheet_strength_ndtetanhchg_base_v053_signal(debt, cashneq, equity):
    nd = _f17_net_debt_to_equity(debt, cashneq, equity)
    b = np.tanh(nd) - np.tanh(nd).shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity buffer interaction: cash/debt x current ratio (coverage quality)
def f17bs_f17_balance_sheet_strength_covqual_lvl_base_v054_signal(cashneq, debt, currentratio):
    b = _f17_cash_to_debt(cashneq, debt) * currentratio
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-to-assets minus liabilities-to-assets (non-debt liability share)
def f17bs_f17_balance_sheet_strength_nondebtliab_lvl_base_v055_signal(debt, liabilities, assets):
    b = _f17_liab_to_assets(liabilities, assets) - _f17_debt_to_assets(debt, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity cushion vs leverage (equity/debt) z-scored over 252d (solvency extremity)
def f17bs_f17_balance_sheet_strength_solvratioz_base_v056_signal(equity, debt, assets):
    sr = _safe_div(_f17_equity_to_assets(equity, assets), _f17_debt_to_assets(debt, assets))
    b = _z(sr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt to equity percentile-ranked over 504d
def f17bs_f17_balance_sheet_strength_ndterank_504d_base_v057_signal(debt, cashneq, equity):
    b = _rank(_f17_net_debt_to_equity(debt, cashneq, equity), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital coverage of debt (wc / debt, liquidity-to-leverage)
def f17bs_f17_balance_sheet_strength_wctd_lvl_base_v058_signal(workingcapital, debt):
    b = _safe_div(workingcapital, debt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities / equity z-scored over 252d (gearing extremity)
def f17bs_f17_balance_sheet_strength_ltez_252d_base_v059_signal(liabilities, equity):
    b = _z(_safe_div(liabilities, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-buffer depletion duration: fraction of last year cash/assets sat >10% below its 252d peak
def f17bs_f17_balance_sheet_strength_cashdepl_252d_base_v060_signal(cashneq, assets):
    cta = _f17_cash_to_assets(cashneq, assets)
    hi = _rmax(cta, 252)
    underw = _safe_div(cta, hi) - 1.0
    deep = (underw <= -0.10).astype(float)
    b = deep.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-ratio dispersion over a quarter (liquidity volatility, inverse strength)
def f17bs_f17_balance_sheet_strength_currdisp_63d_base_v061_signal(currentratio):
    b = _std(currentratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-to-assets in USD terms z-scored over 252d (FX-consistent leverage extremity)
def f17bs_f17_balance_sheet_strength_dusdtaz_252d_base_v062_signal(debtusd, assets):
    b = _z(_safe_div(debtusd, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-assets minus its own 252d min (capitalization recovery off trough)
def f17bs_f17_balance_sheet_strength_etarecov_252d_base_v063_signal(equity, assets):
    eta = _f17_equity_to_assets(equity, assets)
    lo = _rmin(eta, 252)
    b = eta - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash/assets percentile-ranked over 504d (long net-liquidity extremity)
def f17bs_f17_balance_sheet_strength_netcashrank_base_v064_signal(cashneq, debt, assets):
    nc = _safe_div(cashneq - debt, assets)
    b = _rank(nc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compounded liquidity strength z-scored over 252d (de-trended liquidity composite)
def f17bs_f17_balance_sheet_strength_liqcompoundz_base_v065_signal(workingcapital, assets, currentratio):
    comp = (1.0 + _f17_wc_to_assets(workingcapital, assets)) * currentratio - 1.0
    b = _z(comp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-capital leverage: debt / (debt + equity)  (capital-structure debt weight)
def f17bs_f17_balance_sheet_strength_debtcap_lvl_base_v066_signal(debt, equity):
    b = _safe_div(debt, debt + equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-capital leverage smoothed over half a year
def f17bs_f17_balance_sheet_strength_debtcap_126d_base_v067_signal(debt, equity):
    b = _mean(_safe_div(debt, debt + equity), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash net of short obligations proxy: cash / liabilities ranked over 252d
def f17bs_f17_balance_sheet_strength_ctlrank_252d_base_v068_signal(cashneq, liabilities):
    b = _rank(_safe_div(cashneq, liabilities), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-minus-leverage strength gap: z(current ratio) minus z(debt/assets)
def f17bs_f17_balance_sheet_strength_liqlevgap_base_v069_signal(currentratio, debt, assets):
    b = _z(currentratio, 252) - _z(_f17_debt_to_assets(debt, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# clean-balance-sheet composite ranked over 252d: equity/assets x (1 - liabilities/assets)
def f17bs_f17_balance_sheet_strength_cleanbsrank_base_v070_signal(equity, assets, liabilities):
    comp = _f17_equity_to_assets(equity, assets) * (1.0 - _f17_liab_to_assets(liabilities, assets))
    b = _rank(comp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt / assets minus its slow EMA (net-leverage displacement)
def f17bs_f17_balance_sheet_strength_netdebtdisp_ema_base_v071_signal(debt, cashneq, assets):
    nd = _safe_div(debt - cashneq, assets)
    b = nd - nd.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities / assets fast-vs-slow EMA crossover (obligation-intensity trend displacement)
def f17bs_f17_balance_sheet_strength_ltaemacross_base_v072_signal(liabilities, assets):
    lta = _f17_liab_to_assets(liabilities, assets)
    b = lta.ewm(span=21, min_periods=10).mean() - lta.ewm(span=84, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage of debt: deviation from its 252d median, tanh-bounded (coverage anomaly)
def f17bs_f17_balance_sheet_strength_ctdanom_base_v073_signal(cashneq, debt):
    ctd = _f17_cash_to_debt(cashneq, debt)
    med = ctd.rolling(252, min_periods=126).median()
    b = np.tanh(ctd - med)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital / assets percentile rank over 504d (long liquidity-buffer extremity)
def f17bs_f17_balance_sheet_strength_wctarank_504d_base_v074_signal(workingcapital, assets):
    b = _rank(_f17_wc_to_assets(workingcapital, assets), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite distress-cushion z-scored over 252d (Altman-flavored strength extremity)
def f17bs_f17_balance_sheet_strength_distresscushz_base_v075_signal(workingcapital, assets, equity, liabilities, debt):
    comp = (1.2 * _f17_wc_to_assets(workingcapital, assets)
            + 0.6 * _safe_div(equity, liabilities)
            - _f17_debt_to_assets(debt, assets))
    b = _z(comp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17bs_f17_balance_sheet_strength_ndte_lvl_base_v001_signal,
    f17bs_f17_balance_sheet_strength_ndte_63d_base_v002_signal,
    f17bs_f17_balance_sheet_strength_ndtez_252d_base_v003_signal,
    f17bs_f17_balance_sheet_strength_gdtez_126d_base_v004_signal,
    f17bs_f17_balance_sheet_strength_dta_lvl_base_v005_signal,
    f17bs_f17_balance_sheet_strength_dta_126d_base_v006_signal,
    f17bs_f17_balance_sheet_strength_dtarank_252d_base_v007_signal,
    f17bs_f17_balance_sheet_strength_dusdta_lvl_base_v008_signal,
    f17bs_f17_balance_sheet_strength_curr_lvl_base_v009_signal,
    f17bs_f17_balance_sheet_strength_currz_252d_base_v010_signal,
    f17bs_f17_balance_sheet_strength_currstrong_63d_base_v011_signal,
    f17bs_f17_balance_sheet_strength_quick_lvl_base_v012_signal,
    f17bs_f17_balance_sheet_strength_wcta_lvl_base_v013_signal,
    f17bs_f17_balance_sheet_strength_wcta_63d_base_v014_signal,
    f17bs_f17_balance_sheet_strength_wctaz_252d_base_v015_signal,
    f17bs_f17_balance_sheet_strength_cta_lvl_base_v016_signal,
    f17bs_f17_balance_sheet_strength_ctarank_252d_base_v017_signal,
    f17bs_f17_balance_sheet_strength_ctd_lvl_base_v018_signal,
    f17bs_f17_balance_sheet_strength_ctd_126d_base_v019_signal,
    f17bs_f17_balance_sheet_strength_eta_lvl_base_v020_signal,
    f17bs_f17_balance_sheet_strength_etaz_252d_base_v021_signal,
    f17bs_f17_balance_sheet_strength_lta_lvl_base_v022_signal,
    f17bs_f17_balance_sheet_strength_lte_lvl_base_v023_signal,
    f17bs_f17_balance_sheet_strength_levz_504d_base_v024_signal,
    f17bs_f17_balance_sheet_strength_liqmix_lvl_base_v025_signal,
    f17bs_f17_balance_sheet_strength_netcashta_lvl_base_v026_signal,
    f17bs_f17_balance_sheet_strength_netcashtaz_252d_base_v027_signal,
    f17bs_f17_balance_sheet_strength_levstructrank_base_v028_signal,
    f17bs_f17_balance_sheet_strength_etl_lvl_base_v029_signal,
    f17bs_f17_balance_sheet_strength_etlz_252d_base_v030_signal,
    f17bs_f17_balance_sheet_strength_ctl_lvl_base_v031_signal,
    f17bs_f17_balance_sheet_strength_wccurrdiv_base_v032_signal,
    f17bs_f17_balance_sheet_strength_usdmix_lvl_base_v033_signal,
    f17bs_f17_balance_sheet_strength_solvmargin_lvl_base_v034_signal,
    f17bs_f17_balance_sheet_strength_currdd_252d_base_v035_signal,
    f17bs_f17_balance_sheet_strength_ndtevol_63d_base_v036_signal,
    f17bs_f17_balance_sheet_strength_logndtedisp_base_v037_signal,
    f17bs_f17_balance_sheet_strength_cashqualdiv_base_v038_signal,
    f17bs_f17_balance_sheet_strength_solvliqcombo_base_v039_signal,
    f17bs_f17_balance_sheet_strength_dtadisp_63d_base_v040_signal,
    f17bs_f17_balance_sheet_strength_etadisp_126d_base_v041_signal,
    f17bs_f17_balance_sheet_strength_ltaz_504d_base_v042_signal,
    f17bs_f17_balance_sheet_strength_ctdrank_504d_base_v043_signal,
    f17bs_f17_balance_sheet_strength_wctadisp_252d_base_v044_signal,
    f17bs_f17_balance_sheet_strength_netusdta_lvl_base_v045_signal,
    f17bs_f17_balance_sheet_strength_altmanwc_chg_base_v046_signal,
    f17bs_f17_balance_sheet_strength_altmaneq_rank_base_v047_signal,
    f17bs_f17_balance_sheet_strength_strscore_lvl_base_v048_signal,
    f17bs_f17_balance_sheet_strength_currpergear_base_v049_signal,
    f17bs_f17_balance_sheet_strength_gdteema_base_v050_signal,
    f17bs_f17_balance_sheet_strength_etaemacross_base_v051_signal,
    f17bs_f17_balance_sheet_strength_ctadisp_ema_base_v052_signal,
    f17bs_f17_balance_sheet_strength_ndtetanhchg_base_v053_signal,
    f17bs_f17_balance_sheet_strength_covqual_lvl_base_v054_signal,
    f17bs_f17_balance_sheet_strength_nondebtliab_lvl_base_v055_signal,
    f17bs_f17_balance_sheet_strength_solvratioz_base_v056_signal,
    f17bs_f17_balance_sheet_strength_ndterank_504d_base_v057_signal,
    f17bs_f17_balance_sheet_strength_wctd_lvl_base_v058_signal,
    f17bs_f17_balance_sheet_strength_ltez_252d_base_v059_signal,
    f17bs_f17_balance_sheet_strength_cashdepl_252d_base_v060_signal,
    f17bs_f17_balance_sheet_strength_currdisp_63d_base_v061_signal,
    f17bs_f17_balance_sheet_strength_dusdtaz_252d_base_v062_signal,
    f17bs_f17_balance_sheet_strength_etarecov_252d_base_v063_signal,
    f17bs_f17_balance_sheet_strength_netcashrank_base_v064_signal,
    f17bs_f17_balance_sheet_strength_liqcompoundz_base_v065_signal,
    f17bs_f17_balance_sheet_strength_debtcap_lvl_base_v066_signal,
    f17bs_f17_balance_sheet_strength_debtcap_126d_base_v067_signal,
    f17bs_f17_balance_sheet_strength_ctlrank_252d_base_v068_signal,
    f17bs_f17_balance_sheet_strength_liqlevgap_base_v069_signal,
    f17bs_f17_balance_sheet_strength_cleanbsrank_base_v070_signal,
    f17bs_f17_balance_sheet_strength_netdebtdisp_ema_base_v071_signal,
    f17bs_f17_balance_sheet_strength_ltaemacross_base_v072_signal,
    f17bs_f17_balance_sheet_strength_ctdanom_base_v073_signal,
    f17bs_f17_balance_sheet_strength_wctarank_504d_base_v074_signal,
    f17bs_f17_balance_sheet_strength_distresscushz_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_BALANCE_SHEET_STRENGTH_REGISTRY_001_075 = REGISTRY


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
    # currentratio synthesized as a small positive ~1-3 series
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

    print("OK f17_balance_sheet_strength_base_001_075_claude: %d features pass" % n_features)
