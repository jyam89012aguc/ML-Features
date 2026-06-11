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


# ===== folder domain primitives (balance-sheet strength) =====
def _f33_net_cash(cashneq, debt):
    # net cash = cash minus debt (many comm-services growth names are net-cash)
    return cashneq - debt


def _f33_de(debt, equity):
    # debt / equity (equity can be negative for accumulated-deficit names)
    return debt / equity.replace(0, np.nan)


def _f33_da(debt, assets):
    return debt / assets.replace(0, np.nan)


def _f33_ea(equity, assets):
    return equity / assets.replace(0, np.nan)


def _f33_wca(workingcapital, assets):
    return workingcapital / assets.replace(0, np.nan)


def _f33_quick(workingcapital, liabilities, assets):
    # liquidity buffer proxy scaled by assets
    return (workingcapital + liabilities) / assets.replace(0, np.nan)


def _f33_cash_assets(cashneq, assets):
    return cashneq / assets.replace(0, np.nan)


def _f33_liab_assets(liabilities, assets):
    return liabilities / assets.replace(0, np.nan)


# ============================================================
# net-cash / assets level (cash cushion strength)
def f33bs_f33_balance_sheet_strength_netcashassets_63d_base_v001_signal(cashneq, debt, assets):
    nc = _f33_net_cash(cashneq, debt)
    b = _mean(nc / assets.replace(0, np.nan), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash / equity level (net liquidity relative to book)
def f33bs_f33_balance_sheet_strength_netcashequity_63d_base_v002_signal(cashneq, debt, equity):
    nc = _f33_net_cash(cashneq, debt)
    b = _mean(nc / equity.replace(0, np.nan), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt / equity level (leverage)
def f33bs_f33_balance_sheet_strength_de_63d_base_v003_signal(debt, equity):
    b = _mean(_f33_de(debt, equity), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt / assets level
def f33bs_f33_balance_sheet_strength_da_63d_base_v004_signal(debt, assets):
    b = _mean(_f33_da(debt, assets), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity / assets level (capitalization)
def f33bs_f33_balance_sheet_strength_ea_63d_base_v005_signal(equity, assets):
    b = _mean(_f33_ea(equity, assets), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital / assets level
def f33bs_f33_balance_sheet_strength_wca_63d_base_v006_signal(workingcapital, assets):
    b = _mean(_f33_wca(workingcapital, assets), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio level (smoothed)
def f33bs_f33_balance_sheet_strength_curr_63d_base_v007_signal(currentratio):
    b = _mean(currentratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities / assets level (gearing)
def f33bs_f33_balance_sheet_strength_liabassets_63d_base_v008_signal(liabilities, assets):
    b = _mean(_f33_liab_assets(liabilities, assets), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash / assets level (dry powder)
def f33bs_f33_balance_sheet_strength_cashassets_63d_base_v009_signal(cashneq, assets):
    b = _mean(_f33_cash_assets(cashneq, assets), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash / liabilities coverage (solvency buffer)
def f33bs_f33_balance_sheet_strength_cashliab_63d_base_v010_signal(cashneq, liabilities):
    b = _mean(cashneq / liabilities.replace(0, np.nan), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash / assets z-scored vs 252d history (de-trended strength)
def f33bs_f33_balance_sheet_strength_netcashassetsz_252d_base_v011_signal(cashneq, debt, assets):
    nc = _f33_net_cash(cashneq, debt) / assets.replace(0, np.nan)
    b = _z(nc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/equity z-scored vs 252d history
def f33bs_f33_balance_sheet_strength_dez_252d_base_v012_signal(debt, equity):
    b = _z(_f33_de(debt, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets z-scored vs 252d history
def f33bs_f33_balance_sheet_strength_daz_252d_base_v013_signal(debt, assets):
    b = _z(_f33_da(debt, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets z-scored vs 252d history
def f33bs_f33_balance_sheet_strength_eaz_252d_base_v014_signal(equity, assets):
    b = _z(_f33_ea(equity, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/assets z-scored vs 252d history
def f33bs_f33_balance_sheet_strength_wcaz_252d_base_v015_signal(workingcapital, assets):
    b = _z(_f33_wca(workingcapital, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio z-scored vs 252d history
def f33bs_f33_balance_sheet_strength_currz_252d_base_v016_signal(currentratio):
    b = _z(currentratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/assets z-scored vs 252d history
def f33bs_f33_balance_sheet_strength_liabassetsz_252d_base_v017_signal(liabilities, assets):
    b = _z(_f33_liab_assets(liabilities, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash/assets z-scored vs 252d history
def f33bs_f33_balance_sheet_strength_cashassetsz_252d_base_v018_signal(cashneq, assets):
    b = _z(_f33_cash_assets(cashneq, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/equity percentile-rank vs 252d history
def f33bs_f33_balance_sheet_strength_derank_252d_base_v019_signal(debt, equity):
    b = _rank(_f33_de(debt, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets percentile-rank vs 252d history
def f33bs_f33_balance_sheet_strength_earank_252d_base_v020_signal(equity, assets):
    b = _rank(_f33_ea(equity, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash/assets percentile-rank vs 252d history
def f33bs_f33_balance_sheet_strength_netcashrank_252d_base_v021_signal(cashneq, debt, assets):
    nc = _f33_net_cash(cashneq, debt) / assets.replace(0, np.nan)
    b = _rank(nc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio percentile-rank vs 252d history
def f33bs_f33_balance_sheet_strength_currrank_252d_base_v022_signal(currentratio):
    b = _rank(currentratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/assets short-vs-long mean spread (liquidity drift, distinct from z/rank)
def f33bs_f33_balance_sheet_strength_wcarank_252d_base_v023_signal(workingcapital, assets):
    wca = _f33_wca(workingcapital, assets)
    b = _mean(wca, 21) - _mean(wca, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets acceleration: sign x magnitude of its quarterly change (gearing impulse)
def f33bs_f33_balance_sheet_strength_darank_252d_base_v024_signal(debt, assets):
    da = _f33_da(debt, assets)
    chg = da - da.shift(63)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in net-cash/assets over a quarter (cushion build/erode)
def f33bs_f33_balance_sheet_strength_netcashchg_63d_base_v025_signal(cashneq, debt, assets):
    nc = _f33_net_cash(cashneq, debt) / assets.replace(0, np.nan)
    b = nc - nc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in debt/equity over a quarter (leverage build)
def f33bs_f33_balance_sheet_strength_dechg_63d_base_v026_signal(debt, equity):
    de = _f33_de(debt, equity)
    b = de - de.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in equity/assets over a quarter (capitalization shift)
def f33bs_f33_balance_sheet_strength_eachg_63d_base_v027_signal(equity, assets):
    ea = _f33_ea(equity, assets)
    b = ea - ea.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in current ratio over a quarter (liquidity trend)
def f33bs_f33_balance_sheet_strength_currchg_63d_base_v028_signal(currentratio):
    b = currentratio - currentratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in working-capital/assets over a quarter
def f33bs_f33_balance_sheet_strength_wcachg_63d_base_v029_signal(workingcapital, assets):
    wca = _f33_wca(workingcapital, assets)
    b = wca - wca.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in debt/assets (deleveraging vs releveraging)
def f33bs_f33_balance_sheet_strength_dayoy_252d_base_v030_signal(debt, assets):
    da = _f33_da(debt, assets)
    b = da - da.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in cash/assets
def f33bs_f33_balance_sheet_strength_cashyoy_252d_base_v031_signal(cashneq, assets):
    ca = _f33_cash_assets(cashneq, assets)
    b = ca - ca.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in equity/assets
def f33bs_f33_balance_sheet_strength_eayoy_252d_base_v032_signal(equity, assets):
    ea = _f33_ea(equity, assets)
    b = ea - ea.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log growth of equity (book-value compounding/erosion)
def f33bs_f33_balance_sheet_strength_equitygrow_252d_base_v033_signal(equity):
    e = equity.where(equity > 0)
    b = np.log(e / e.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log growth of cash (liquidity accumulation)
def f33bs_f33_balance_sheet_strength_cashgrow_252d_base_v034_signal(cashneq):
    c = cashneq.where(cashneq > 0)
    b = np.log(c / c.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log growth of debt (debt build, content/M&A leverage)
def f33bs_f33_balance_sheet_strength_debtgrow_252d_base_v035_signal(debt):
    d = debt.where(debt > 0)
    b = np.log(d / d.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log growth of assets (balance-sheet scaling)
def f33bs_f33_balance_sheet_strength_assetgrow_252d_base_v036_signal(assets):
    a = assets.where(assets > 0)
    b = np.log(a / a.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth minus equity growth (leverage outpacing the equity cushion)
def f33bs_f33_balance_sheet_strength_debtvsasset_252d_base_v037_signal(debt, equity):
    d = debt.where(debt > 0)
    e = equity.where(equity > 0)
    b = np.log(d / d.shift(252)) - np.log(e / e.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash growth minus debt growth (net-cash trajectory)
def f33bs_f33_balance_sheet_strength_cashvsdebt_252d_base_v038_signal(cashneq, debt):
    c = cashneq.where(cashneq > 0)
    d = debt.where(debt > 0)
    b = np.log(c / c.shift(252)) - np.log(d / d.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity growth minus liability growth (capital-structure improvement)
def f33bs_f33_balance_sheet_strength_eqvsliab_252d_base_v039_signal(equity, liabilities):
    e = equity.where(equity > 0)
    l = liabilities.where(liabilities > 0)
    b = np.log(e / e.shift(252)) - np.log(l / l.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash strength regime: fraction of half-year net-cash exceeds its own 252d median
def f33bs_f33_balance_sheet_strength_netcashregime_126d_base_v040_signal(cashneq, debt):
    nc = _f33_net_cash(cashneq, debt)
    thr = nc.rolling(252, min_periods=126).median()
    flag = (nc > thr).astype(float)
    b = flag.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year with current ratio above its own 252d median (liquid-regime persistence)
def f33bs_f33_balance_sheet_strength_currhealthy_252d_base_v041_signal(currentratio):
    thr = currentratio.rolling(252, min_periods=126).median()
    flag = (currentratio > thr).astype(float)
    b = flag.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year working capital sits above its own 252d median (build persistence)
def f33bs_f33_balance_sheet_strength_wcpos_252d_base_v042_signal(workingcapital):
    thr = workingcapital.rolling(252, min_periods=126).median()
    flag = (workingcapital > thr).astype(float)
    b = flag.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year equity sits below its own 252d median (deficit-drift persistence)
def f33bs_f33_balance_sheet_strength_negequity_252d_base_v043_signal(equity):
    thr = equity.rolling(252, min_periods=126).median()
    flag = (equity < thr).astype(float)
    b = flag.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of current ratio from a hurdle of 1.0, scaled by typical dispersion
def f33bs_f33_balance_sheet_strength_currhurdle_126d_base_v044_signal(currentratio):
    dist = currentratio - 1.0
    sd = _std(currentratio, 126)
    b = dist / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of debt/assets from a 0.4 hurdle (over-levered regime distance)
def f33bs_f33_balance_sheet_strength_dahurdle_126d_base_v045_signal(debt, assets):
    da = _f33_da(debt, assets)
    sd = _std(da, 126)
    b = (0.4 - da) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity buffer = (cash + working capital) / liabilities
def f33bs_f33_balance_sheet_strength_liqbuffer_63d_base_v046_signal(cashneq, workingcapital, liabilities):
    buf = (cashneq + workingcapital) / liabilities.replace(0, np.nan)
    b = _mean(buf, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quick-ratio proxy: (working capital + liabilities) / assets level
def f33bs_f33_balance_sheet_strength_quick_63d_base_v047_signal(workingcapital, liabilities, assets):
    b = _mean(_f33_quick(workingcapital, liabilities, assets), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# solvency score: equity/assets minus debt/assets (net capitalization)
def f33bs_f33_balance_sheet_strength_solvency_63d_base_v048_signal(equity, debt, assets):
    sc = (equity - debt) / assets.replace(0, np.nan)
    b = _mean(sc, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash plus working capital, normalized by assets (total liquidity strength)
def f33bs_f33_balance_sheet_strength_totliq_63d_base_v049_signal(cashneq, debt, workingcapital, assets):
    tl = (cashneq - debt + workingcapital) / assets.replace(0, np.nan)
    b = _mean(tl, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interaction: equity/assets times current ratio (capitalized liquidity)
def f33bs_f33_balance_sheet_strength_capliq_63d_base_v050_signal(equity, assets, currentratio):
    inter = _f33_ea(equity, assets) * currentratio
    b = _mean(inter, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interaction: net-cash/assets times current ratio (cash-backed liquidity)
def f33bs_f33_balance_sheet_strength_cashbacked_63d_base_v051_signal(cashneq, debt, assets, currentratio):
    nc = _f33_net_cash(cashneq, debt) / assets.replace(0, np.nan)
    b = _mean(nc * currentratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x magnitude of net cash relative to assets (compressed strength)
def f33bs_f33_balance_sheet_strength_netcashsm_63d_base_v052_signal(cashneq, debt, assets):
    nc = _f33_net_cash(cashneq, debt) / assets.replace(0, np.nan)
    b = np.sign(nc) * (nc.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of debt/assets over a quarter (leverage instability)
def f33bs_f33_balance_sheet_strength_dadisp_63d_base_v053_signal(debt, assets):
    da = _f33_da(debt, assets)
    b = _std(da, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of current ratio over a quarter (liquidity instability)
def f33bs_f33_balance_sheet_strength_currdisp_63d_base_v054_signal(currentratio):
    b = _std(currentratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of equity/assets over half a year
def f33bs_f33_balance_sheet_strength_eadisp_126d_base_v055_signal(equity, assets):
    ea = _f33_ea(equity, assets)
    b = _std(ea, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/equity ratio of short window mean to long window mean (leverage drift)
def f33bs_f33_balance_sheet_strength_dedrift_base_v056_signal(debt, equity):
    de = _f33_de(debt, equity)
    b = _mean(de, 21) - _mean(de, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash/assets short vs long mean spread (liquidity drift)
def f33bs_f33_balance_sheet_strength_cashdrift_base_v057_signal(cashneq, assets):
    ca = _f33_cash_assets(cashneq, assets)
    b = _mean(ca, 21) - _mean(ca, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets minus its slow EMA (capitalization displacement)
def f33bs_f33_balance_sheet_strength_eadisplace_base_v058_signal(equity, assets):
    ea = _f33_ea(equity, assets)
    b = ea - ea.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio oscillator: deviation from its own slow EMA (liquidity displacement)
def f33bs_f33_balance_sheet_strength_currema_base_v059_signal(currentratio):
    b = currentratio - currentratio.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash/assets minus its slow EMA (cushion displacement)
def f33bs_f33_balance_sheet_strength_netcashdisplace_base_v060_signal(cashneq, debt, assets):
    nc = _f33_net_cash(cashneq, debt) / assets.replace(0, np.nan)
    b = nc - nc.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets distance to its own 252d max (peak-leverage proximity)
def f33bs_f33_balance_sheet_strength_dapeak_252d_base_v061_signal(debt, assets):
    da = _f33_da(debt, assets)
    mx = _rmax(da, 252)
    b = da / mx.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash/assets distance above its own 252d min (liquidity recovery off trough)
def f33bs_f33_balance_sheet_strength_cashtrough_252d_base_v062_signal(cashneq, assets):
    ca = _f33_cash_assets(cashneq, assets)
    mn = _rmin(ca, 252)
    b = ca / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets position within its own 252d range (capitalization range position)
def f33bs_f33_balance_sheet_strength_eapos_252d_base_v063_signal(equity, assets):
    ea = _f33_ea(equity, assets)
    hi = _rmax(ea, 252)
    lo = _rmin(ea, 252)
    b = (ea - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio position within its own 252d range
def f33bs_f33_balance_sheet_strength_currpos_252d_base_v064_signal(currentratio):
    hi = _rmax(currentratio, 252)
    lo = _rmin(currentratio, 252)
    b = (currentratio - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed debt/equity deviation from its 252d median (bounded leverage regime distance)
def f33bs_f33_balance_sheet_strength_detanh_63d_base_v065_signal(debt, equity):
    de = _f33_de(debt, equity)
    med = de.rolling(252, min_periods=126).median()
    b = np.tanh(de - med)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital / liabilities coverage, z-scored vs 252d history (short-term solvency drift)
def f33bs_f33_balance_sheet_strength_wcliab_63d_base_v066_signal(workingcapital, liabilities):
    ratio = workingcapital / liabilities.replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt per unit of working capital (leverage vs liquidity)
def f33bs_f33_balance_sheet_strength_debtwc_63d_base_v067_signal(debt, workingcapital):
    ratio = debt / workingcapital.replace(0, np.nan)
    b = _mean(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-leverage momentum: change in net-debt/equity over a quarter (releveraging speed)
def f33bs_f33_balance_sheet_strength_netde_63d_base_v068_signal(debt, cashneq, equity):
    nd = (debt - cashneq) / equity.replace(0, np.nan)
    b = nd - nd.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-gearing instability: dispersion of net-debt/assets over half a year (leverage volatility)
def f33bs_f33_balance_sheet_strength_netda_63d_base_v069_signal(debt, cashneq, assets):
    nd = (debt - cashneq) / assets.replace(0, np.nan)
    b = _std(nd, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liability coverage by equity (equity/liabilities)
def f33bs_f33_balance_sheet_strength_eqliab_63d_base_v070_signal(equity, liabilities):
    b = _mean(equity / liabilities.replace(0, np.nan), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash/equity z-scored vs 252d history
def f33bs_f33_balance_sheet_strength_netcasheqz_252d_base_v071_signal(cashneq, debt, equity):
    nc = _f33_net_cash(cashneq, debt) / equity.replace(0, np.nan)
    b = _z(nc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-multiplier (assets/equity) dispersion over half a year (leverage-amplification instability)
def f33bs_f33_balance_sheet_strength_liabeq_63d_base_v072_signal(assets, equity):
    em = assets / equity.replace(0, np.nan)
    b = _std(em, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite strength: rank(equity/assets) + rank(currentratio) - rank(debt/assets)
def f33bs_f33_balance_sheet_strength_composite_252d_base_v073_signal(equity, assets, currentratio, debt):
    r1 = _rank(_f33_ea(equity, assets), 252)
    r2 = _rank(currentratio, 252)
    r3 = _rank(_f33_da(debt, assets), 252)
    b = r1 + r2 - r3
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity buffer trend: change in (cash+wc)/assets over a quarter
def f33bs_f33_balance_sheet_strength_liqtrend_63d_base_v074_signal(cashneq, workingcapital, assets):
    buf = (cashneq + workingcapital) / assets.replace(0, np.nan)
    b = buf - buf.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage acceleration sign x magnitude: net-debt/assets change vs prior change
def f33bs_f33_balance_sheet_strength_netdaaccel_63d_base_v075_signal(debt, cashneq, assets):
    nd = (debt - cashneq) / assets.replace(0, np.nan)
    chg = nd - nd.shift(63)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33bs_f33_balance_sheet_strength_netcashassets_63d_base_v001_signal,
    f33bs_f33_balance_sheet_strength_netcashequity_63d_base_v002_signal,
    f33bs_f33_balance_sheet_strength_de_63d_base_v003_signal,
    f33bs_f33_balance_sheet_strength_da_63d_base_v004_signal,
    f33bs_f33_balance_sheet_strength_ea_63d_base_v005_signal,
    f33bs_f33_balance_sheet_strength_wca_63d_base_v006_signal,
    f33bs_f33_balance_sheet_strength_curr_63d_base_v007_signal,
    f33bs_f33_balance_sheet_strength_liabassets_63d_base_v008_signal,
    f33bs_f33_balance_sheet_strength_cashassets_63d_base_v009_signal,
    f33bs_f33_balance_sheet_strength_cashliab_63d_base_v010_signal,
    f33bs_f33_balance_sheet_strength_netcashassetsz_252d_base_v011_signal,
    f33bs_f33_balance_sheet_strength_dez_252d_base_v012_signal,
    f33bs_f33_balance_sheet_strength_daz_252d_base_v013_signal,
    f33bs_f33_balance_sheet_strength_eaz_252d_base_v014_signal,
    f33bs_f33_balance_sheet_strength_wcaz_252d_base_v015_signal,
    f33bs_f33_balance_sheet_strength_currz_252d_base_v016_signal,
    f33bs_f33_balance_sheet_strength_liabassetsz_252d_base_v017_signal,
    f33bs_f33_balance_sheet_strength_cashassetsz_252d_base_v018_signal,
    f33bs_f33_balance_sheet_strength_derank_252d_base_v019_signal,
    f33bs_f33_balance_sheet_strength_earank_252d_base_v020_signal,
    f33bs_f33_balance_sheet_strength_netcashrank_252d_base_v021_signal,
    f33bs_f33_balance_sheet_strength_currrank_252d_base_v022_signal,
    f33bs_f33_balance_sheet_strength_wcarank_252d_base_v023_signal,
    f33bs_f33_balance_sheet_strength_darank_252d_base_v024_signal,
    f33bs_f33_balance_sheet_strength_netcashchg_63d_base_v025_signal,
    f33bs_f33_balance_sheet_strength_dechg_63d_base_v026_signal,
    f33bs_f33_balance_sheet_strength_eachg_63d_base_v027_signal,
    f33bs_f33_balance_sheet_strength_currchg_63d_base_v028_signal,
    f33bs_f33_balance_sheet_strength_wcachg_63d_base_v029_signal,
    f33bs_f33_balance_sheet_strength_dayoy_252d_base_v030_signal,
    f33bs_f33_balance_sheet_strength_cashyoy_252d_base_v031_signal,
    f33bs_f33_balance_sheet_strength_eayoy_252d_base_v032_signal,
    f33bs_f33_balance_sheet_strength_equitygrow_252d_base_v033_signal,
    f33bs_f33_balance_sheet_strength_cashgrow_252d_base_v034_signal,
    f33bs_f33_balance_sheet_strength_debtgrow_252d_base_v035_signal,
    f33bs_f33_balance_sheet_strength_assetgrow_252d_base_v036_signal,
    f33bs_f33_balance_sheet_strength_debtvsasset_252d_base_v037_signal,
    f33bs_f33_balance_sheet_strength_cashvsdebt_252d_base_v038_signal,
    f33bs_f33_balance_sheet_strength_eqvsliab_252d_base_v039_signal,
    f33bs_f33_balance_sheet_strength_netcashregime_126d_base_v040_signal,
    f33bs_f33_balance_sheet_strength_currhealthy_252d_base_v041_signal,
    f33bs_f33_balance_sheet_strength_wcpos_252d_base_v042_signal,
    f33bs_f33_balance_sheet_strength_negequity_252d_base_v043_signal,
    f33bs_f33_balance_sheet_strength_currhurdle_126d_base_v044_signal,
    f33bs_f33_balance_sheet_strength_dahurdle_126d_base_v045_signal,
    f33bs_f33_balance_sheet_strength_liqbuffer_63d_base_v046_signal,
    f33bs_f33_balance_sheet_strength_quick_63d_base_v047_signal,
    f33bs_f33_balance_sheet_strength_solvency_63d_base_v048_signal,
    f33bs_f33_balance_sheet_strength_totliq_63d_base_v049_signal,
    f33bs_f33_balance_sheet_strength_capliq_63d_base_v050_signal,
    f33bs_f33_balance_sheet_strength_cashbacked_63d_base_v051_signal,
    f33bs_f33_balance_sheet_strength_netcashsm_63d_base_v052_signal,
    f33bs_f33_balance_sheet_strength_dadisp_63d_base_v053_signal,
    f33bs_f33_balance_sheet_strength_currdisp_63d_base_v054_signal,
    f33bs_f33_balance_sheet_strength_eadisp_126d_base_v055_signal,
    f33bs_f33_balance_sheet_strength_dedrift_base_v056_signal,
    f33bs_f33_balance_sheet_strength_cashdrift_base_v057_signal,
    f33bs_f33_balance_sheet_strength_eadisplace_base_v058_signal,
    f33bs_f33_balance_sheet_strength_currema_base_v059_signal,
    f33bs_f33_balance_sheet_strength_netcashdisplace_base_v060_signal,
    f33bs_f33_balance_sheet_strength_dapeak_252d_base_v061_signal,
    f33bs_f33_balance_sheet_strength_cashtrough_252d_base_v062_signal,
    f33bs_f33_balance_sheet_strength_eapos_252d_base_v063_signal,
    f33bs_f33_balance_sheet_strength_currpos_252d_base_v064_signal,
    f33bs_f33_balance_sheet_strength_detanh_63d_base_v065_signal,
    f33bs_f33_balance_sheet_strength_wcliab_63d_base_v066_signal,
    f33bs_f33_balance_sheet_strength_debtwc_63d_base_v067_signal,
    f33bs_f33_balance_sheet_strength_netde_63d_base_v068_signal,
    f33bs_f33_balance_sheet_strength_netda_63d_base_v069_signal,
    f33bs_f33_balance_sheet_strength_eqliab_63d_base_v070_signal,
    f33bs_f33_balance_sheet_strength_netcasheqz_252d_base_v071_signal,
    f33bs_f33_balance_sheet_strength_liabeq_63d_base_v072_signal,
    f33bs_f33_balance_sheet_strength_composite_252d_base_v073_signal,
    f33bs_f33_balance_sheet_strength_liqtrend_63d_base_v074_signal,
    f33bs_f33_balance_sheet_strength_netdaaccel_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_BALANCE_SHEET_STRENGTH_REGISTRY_001_075 = REGISTRY


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

    debt = _fund(101, base=6e7, drift=0.02, vol=0.06).rename("debt")
    equity = _fund(102, base=1.2e8, drift=0.015, vol=0.08, allow_neg=True).rename("equity")
    assets = _fund(103, base=3e8, drift=0.02, vol=0.05).rename("assets")
    liabilities = _fund(104, base=1.4e8, drift=0.02, vol=0.06).rename("liabilities")
    workingcapital = _fund(105, base=5e7, drift=0.01, vol=0.09, allow_neg=True).rename("workingcapital")
    cashneq = _fund(106, base=8e7, drift=0.025, vol=0.08).rename("cashneq")
    currentratio = (1.0 + _fund(107, base=1.0, drift=0.005, vol=0.05) * 0.0).rename("currentratio")
    # build a small-positive current ratio ~1-3 directly
    g = np.random.default_rng(108)
    cr_steps = np.repeat(g.normal(0.0, 0.06, n // 63 + 1), 63)[:n]
    currentratio = pd.Series(1.8 * np.exp(np.cumsum(cr_steps / 63)), name="currentratio")

    cols = {
        "debt": debt, "equity": equity, "assets": assets, "liabilities": liabilities,
        "workingcapital": workingcapital, "cashneq": cashneq, "currentratio": currentratio,
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
        "intexp", "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
        "payoutratio", "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal", "fndholders",
        "undholders", "prfholders", "dbtholders", "putholders", "putvalue", "cllholders",
        "cllvalue", "wntholders", "wntvalue", "dbtvalue",
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

    print("OK f33_balance_sheet_strength_base_001_075_claude: %d features pass" % n_features)
