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
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


def _jerk(s, w):
    return (s - 2.0 * s.shift(w) + s.shift(2 * w)) / float(w * w)


def _rng(s, w):
    return _rmax(s, w) - _rmin(s, w)


# ===== folder domain primitives: BALANCE-SHEET LEVERAGE & LIQUIDITY STRUCTURE =====
# This file continues the f22 debt/currentratio-centric leverage & liquidity STRUCTURE
# facets. It deliberately avoids the liabilities-based ratios, cash/liabilities and
# cash/assets coverage, equity/assets, wc/assets and Altman-Z composites that the f21
# distress / going-concern family owns.
def _abs_floor(s):
    return s.abs().replace(0, np.nan)


def _debt_equity(debt, equity):
    return (debt / _abs_floor(equity)).clip(lower=-50.0, upper=50.0)


def _debt_assets(debt, assets):
    return debt / assets.replace(0, np.nan)


def _net_debt_equity(debt, cashneq, equity):
    return ((debt - cashneq) / _abs_floor(equity)).clip(lower=-50.0, upper=50.0)


def _cash_debt(cashneq, debt):
    return cashneq / debt.replace(0, np.nan)


def _debt_wc(debt, workingcapital):
    return (debt / _abs_floor(workingcapital)).clip(lower=-50.0, upper=50.0)


def _usd_prem(debtusd, debt):
    return (debtusd / debt.replace(0, np.nan)).clip(lower=-5.0, upper=10.0)


def _debt_currcover(debt, assets, currentratio):
    # leverage adjusted for short-term liquidity: debt/assets discounted by the current
    # ratio (a debt-light, liquidity-rich firm scores low). currentratio is f21-free.
    da = _debt_assets(debt, assets).clip(lower=0.0, upper=2.0)
    return da / (currentratio.clip(lower=0.05))


def _maturity_proxy(currentratio, debt, equity):
    # near-term obligation pressure: gross leverage scaled by inverse short-term liquidity
    de = _debt_equity(debt, equity).clip(lower=-10.0, upper=10.0)
    return de / currentratio.clip(lower=0.05)


def _gross_gear(debt, equity):
    cap = (debt + equity).replace(0, np.nan)
    return (debt / cap).clip(lower=-5.0, upper=5.0)


def _net_gearing(debt, cashneq, equity):
    nd = debt - cashneq
    cap = (nd + equity).replace(0, np.nan)
    return (nd / cap).clip(lower=-5.0, upper=5.0)


def _liq_buffer_debt(cashneq, workingcapital, debt):
    return ((cashneq + workingcapital) / debt.replace(0, np.nan)).clip(lower=-50.0, upper=50.0)


def _quick_ratio(currentratio, cashneq, liabilities):
    cl = (cashneq / liabilities.replace(0, np.nan)).clip(lower=0.0, upper=10.0)
    return (0.5 * currentratio + cl).clip(lower=0.0, upper=20.0)


# ============================================================
# ---- net debt / equity extended facets ----
# net debt-to-equity [z126]
def f22bs_f22_balance_sheet_survival_ndeq_z126_126d_base_v076_signal(debt, cashneq, equity):
    b = _z(_net_debt_equity(debt, cashneq, equity), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net debt-to-equity [dsp126 dispersion]
def f22bs_f22_balance_sheet_survival_ndeq_dsp126_126d_base_v077_signal(debt, cashneq, equity):
    b = _std(_net_debt_equity(debt, cashneq, equity), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net debt-to-equity [yoy252]
def f22bs_f22_balance_sheet_survival_ndeq_yoy252_252d_base_v078_signal(debt, cashneq, equity):
    r = _net_debt_equity(debt, cashneq, equity)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net debt-to-equity [rng252 travel]
def f22bs_f22_balance_sheet_survival_ndeq_rng252_252d_base_v079_signal(debt, cashneq, equity):
    b = _rng(_net_debt_equity(debt, cashneq, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net debt-to-equity [curv]
def f22bs_f22_balance_sheet_survival_ndeq_curv_63d_base_v080_signal(debt, cashneq, equity):
    r = _net_debt_equity(debt, cashneq, equity)
    b = r - 0.5 * (r.shift(63) + r.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- debt / equity extended facets ----
# gross debt-to-equity [dsp126]
def f22bs_f22_balance_sheet_survival_dbteq_dsp126_126d_base_v081_signal(debt, equity):
    b = _std(_debt_equity(debt, equity), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-equity [yoy252]
def f22bs_f22_balance_sheet_survival_dbteq_yoy252_252d_base_v082_signal(debt, equity):
    r = _debt_equity(debt, equity)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-equity [rng252 travel]
def f22bs_f22_balance_sheet_survival_dbteq_rng252_252d_base_v083_signal(debt, equity):
    b = _rng(_debt_equity(debt, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-equity displacement from slow EMA
def f22bs_f22_balance_sheet_survival_dbteq_disp_126d_base_v084_signal(debt, equity):
    r = _debt_equity(debt, equity)
    b = r - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-equity [smz63]
def f22bs_f22_balance_sheet_survival_dbteq_smz63_63d_base_v085_signal(debt, equity):
    r = _debt_equity(debt, equity)
    b = r - r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- debt / assets extended facets ----
# gross debt-to-assets [dsp126]
def f22bs_f22_balance_sheet_survival_dbtassets_dsp126_126d_base_v086_signal(debt, assets):
    b = _std(_debt_assets(debt, assets), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-assets [smz63]
def f22bs_f22_balance_sheet_survival_dbtassets_smz63_63d_base_v087_signal(debt, assets):
    r = _debt_assets(debt, assets)
    b = r - r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-assets [rng252 travel]
def f22bs_f22_balance_sheet_survival_dbtassets_rng252_252d_base_v088_signal(debt, assets):
    b = _rng(_debt_assets(debt, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-assets runup off 252d trough (re-leveraging distance)
def f22bs_f22_balance_sheet_survival_dbtassets_runup_252d_base_v089_signal(debt, assets):
    r = _debt_assets(debt, assets)
    trough = _rmin(r, 252)
    b = r - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-assets term spread (short minus long)
def f22bs_f22_balance_sheet_survival_dbtassets_term_base_v090_signal(debt, assets):
    r = _debt_assets(debt, assets)
    b = r.rolling(63, min_periods=21).mean() - r.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- cash / debt extended facets ----
# cash-to-debt [z126]
def f22bs_f22_balance_sheet_survival_cashdebt_z126_126d_base_v091_signal(cashneq, debt):
    b = _z(_cash_debt(cashneq, debt), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# cash-to-debt [chg63]
def f22bs_f22_balance_sheet_survival_cashdebt_chg63_63d_base_v092_signal(cashneq, debt):
    r = _cash_debt(cashneq, debt)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# cash-to-debt [ema63 trend]
def f22bs_f22_balance_sheet_survival_cashdebt_ema63_63d_base_v093_signal(cashneq, debt):
    r = _cash_debt(cashneq, debt)
    b = r.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# cash-to-debt drawdown off 252d peak (eroding debt coverage)
def f22bs_f22_balance_sheet_survival_cashdebt_dd252_252d_base_v094_signal(cashneq, debt):
    r = _cash_debt(cashneq, debt)
    peak = _rmax(r, 252)
    b = r - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# cash-to-debt term spread (short minus long coverage)
def f22bs_f22_balance_sheet_survival_cashdebt_term_base_v095_signal(cashneq, debt):
    r = _cash_debt(cashneq, debt)
    b = r.rolling(63, min_periods=21).mean() - r.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- debt / working capital extended facets ----
# debt-to-working-capital [z126]
def f22bs_f22_balance_sheet_survival_dbtwc_z126_126d_base_v096_signal(debt, workingcapital):
    b = _z(_debt_wc(debt, workingcapital), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-working-capital [chg63]
def f22bs_f22_balance_sheet_survival_dbtwc_chg63_63d_base_v097_signal(debt, workingcapital):
    r = _debt_wc(debt, workingcapital)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-working-capital [dsp126]
def f22bs_f22_balance_sheet_survival_dbtwc_dsp126_126d_base_v098_signal(debt, workingcapital):
    b = _std(_debt_wc(debt, workingcapital), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-working-capital [smz63]
def f22bs_f22_balance_sheet_survival_dbtwc_smz63_63d_base_v099_signal(debt, workingcapital):
    r = _debt_wc(debt, workingcapital)
    b = r - r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-working-capital [yoy252]
def f22bs_f22_balance_sheet_survival_dbtwc_yoy252_252d_base_v100_signal(debt, workingcapital):
    r = _debt_wc(debt, workingcapital)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- working capital / debt (inverse cushion-vs-debt) ----
# working-capital-to-debt [lvl]
def f22bs_f22_balance_sheet_survival_wcdebt_lvl_63d_base_v101_signal(workingcapital, debt):
    b = (workingcapital / debt.replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# working-capital-to-debt [z252]
def f22bs_f22_balance_sheet_survival_wcdebt_z252_252d_base_v102_signal(workingcapital, debt):
    r = (workingcapital / debt.replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# working-capital-to-debt [rnk252]
def f22bs_f22_balance_sheet_survival_wcdebt_rnk252_252d_base_v103_signal(workingcapital, debt):
    r = (workingcapital / debt.replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    b = _rank(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# working-capital-to-debt [chg126]
def f22bs_f22_balance_sheet_survival_wcdebt_chg126_126d_base_v104_signal(workingcapital, debt):
    r = (workingcapital / debt.replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# working-capital-to-debt [dsp126]
def f22bs_f22_balance_sheet_survival_wcdebt_dsp126_126d_base_v105_signal(workingcapital, debt):
    r = (workingcapital / debt.replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    b = _std(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- current ratio extended facets ----
# current ratio [ema63 trend]
def f22bs_f22_balance_sheet_survival_curratio_ema63_63d_base_v106_signal(currentratio):
    b = currentratio.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# current ratio [smz63 deviation-from-mean]
def f22bs_f22_balance_sheet_survival_curratio_smz63_63d_base_v107_signal(currentratio):
    b = currentratio - currentratio.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# current ratio [yoy252]
def f22bs_f22_balance_sheet_survival_curratio_yoy252_252d_base_v108_signal(currentratio):
    b = currentratio - currentratio.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# current ratio drawdown off 252d peak (liquidity erosion)
def f22bs_f22_balance_sheet_survival_curratio_dd252_252d_base_v109_signal(currentratio):
    peak = _rmax(currentratio, 252)
    b = currentratio - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# current ratio term spread (short minus long liquidity)
def f22bs_f22_balance_sheet_survival_curratio_term_base_v110_signal(currentratio):
    short = currentratio.rolling(63, min_periods=21).mean()
    long = currentratio.rolling(252, min_periods=126).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- additional debt-leverage & liquidity-structure facets ----
# debt-to-working-capital travel range (leverage-vs-cushion swing) [rng252]
def f22bs_f22_balance_sheet_survival_dbtwc_rng252_252d_base_v111_signal(debt, workingcapital):
    b = _rng(_debt_wc(debt, workingcapital), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# cash-to-debt travel range (debt-coverage swing) [rng252]
def f22bs_f22_balance_sheet_survival_cashdebt_rng252_252d_base_v112_signal(cashneq, debt):
    b = _rng(_cash_debt(cashneq, debt), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# quick-ratio proxy dispersion (conservative-liquidity volatility) [dsp126]
def f22bs_f22_balance_sheet_survival_quick_dsp126_126d_base_v113_signal(currentratio, cashneq, liabilities):
    b = _std(_quick_ratio(currentratio, cashneq, liabilities), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-capital percentile rank (structural-gearing rank) [rnk252]
def f22bs_f22_balance_sheet_survival_dbtcap_rnk252_252d_base_v114_signal(debt, equity, cashneq):
    cap = (debt + equity + cashneq).replace(0, np.nan)
    r = (debt / cap).clip(lower=-5.0, upper=5.0)
    b = _rank(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net gearing percentile rank (net-leverage rank) [rnk252]
def f22bs_f22_balance_sheet_survival_netgear_rnk252_252d_base_v115_signal(debt, cashneq, equity):
    b = _rank(_net_gearing(debt, cashneq, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# liquidity-buffer-to-debt percentile rank (liquidity-vs-debt rank) [rnk252]
def f22bs_f22_balance_sheet_survival_liqbuf_rnk252_252d_base_v116_signal(cashneq, workingcapital, debt):
    b = _rank(_liq_buffer_debt(cashneq, workingcapital, debt), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# working-capital-to-debt deviation from its 63d mean (cushion-vs-debt displacement) [smz63]
def f22bs_f22_balance_sheet_survival_wcdebt_smz63_63d_base_v117_signal(workingcapital, debt):
    r = (workingcapital / debt.replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    b = r - r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-per-quick-liquidity z-level (liquidity-adjusted leverage) [z252]
def f22bs_f22_balance_sheet_survival_dbtquick_z252_252d_base_v118_signal(debt, assets, currentratio, cashneq, liabilities):
    q = _quick_ratio(currentratio, cashneq, liabilities).clip(lower=0.05)
    da = _debt_assets(debt, assets).clip(lower=0.0, upper=2.0)
    b = _z(da / q, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- debt-stack level dynamics ----
# gross debt log-growth over a quarter (debt build/paydown rate)
def f22bs_f22_balance_sheet_survival_dbtgrow_q63_63d_base_v119_signal(debt):
    b = np.log(debt.replace(0, np.nan) / debt.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt z-level vs its own 126d scale
def f22bs_f22_balance_sheet_survival_dbtlevel_z126_126d_base_v120_signal(debt):
    b = _z(debt, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt drawdown off 252d peak (deleveraging from a debt peak)
def f22bs_f22_balance_sheet_survival_dbtdd_252d_base_v121_signal(debt):
    peak = _rmax(debt, 252)
    b = debt / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt log-growth over a half-year (medium-horizon debt build/paydown rate)
def f22bs_f22_balance_sheet_survival_dbtgrow_h126_126d_base_v122_signal(debt):
    b = np.log(debt.replace(0, np.nan) / debt.shift(126).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt drawup off its 504d trough (long-horizon re-leveraging distance)
def f22bs_f22_balance_sheet_survival_dbtrunup_504d_base_v123_signal(debt):
    trough = _rmin(debt, 504)
    b = debt / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- liquidity-adjusted leverage (debt/assets discounted by current ratio) ----
# debt-vs-liquidity cover [lvl]
def f22bs_f22_balance_sheet_survival_dbtcurr_lvl_63d_base_v124_signal(debt, assets, currentratio):
    b = _debt_currcover(debt, assets, currentratio)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-vs-liquidity cover [z252]
def f22bs_f22_balance_sheet_survival_dbtcurr_z252_252d_base_v125_signal(debt, assets, currentratio):
    b = _z(_debt_currcover(debt, assets, currentratio), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-vs-liquidity cover [rnk252]
def f22bs_f22_balance_sheet_survival_dbtcurr_rnk252_252d_base_v126_signal(debt, assets, currentratio):
    b = _rank(_debt_currcover(debt, assets, currentratio), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-vs-liquidity cover [chg126]
def f22bs_f22_balance_sheet_survival_dbtcurr_chg126_126d_base_v127_signal(debt, assets, currentratio):
    r = _debt_currcover(debt, assets, currentratio)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-vs-liquidity cover [smz63]
def f22bs_f22_balance_sheet_survival_dbtcurr_smz63_63d_base_v128_signal(debt, assets, currentratio):
    r = _debt_currcover(debt, assets, currentratio)
    b = r - r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- near-term maturity pressure (gross leverage / current ratio) ----
# maturity pressure proxy [lvl]
def f22bs_f22_balance_sheet_survival_matpress_lvl_63d_base_v129_signal(currentratio, debt, equity):
    b = _maturity_proxy(currentratio, debt, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# maturity pressure proxy [z252]
def f22bs_f22_balance_sheet_survival_matpress_z252_252d_base_v130_signal(currentratio, debt, equity):
    b = _z(_maturity_proxy(currentratio, debt, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# maturity pressure proxy [rnk252]
def f22bs_f22_balance_sheet_survival_matpress_rnk252_252d_base_v131_signal(currentratio, debt, equity):
    b = _rank(_maturity_proxy(currentratio, debt, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# maturity pressure proxy [chg126]
def f22bs_f22_balance_sheet_survival_matpress_chg126_126d_base_v132_signal(currentratio, debt, equity):
    r = _maturity_proxy(currentratio, debt, equity)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# maturity pressure proxy [dsp126]
def f22bs_f22_balance_sheet_survival_matpress_dsp126_126d_base_v133_signal(currentratio, debt, equity):
    b = _std(_maturity_proxy(currentratio, debt, equity), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- net debt / assets extended facets (debt-based net debt) ----
# net debt-to-assets [z126]
def f22bs_f22_balance_sheet_survival_ndassets_z126_126d_base_v134_signal(debt, cashneq, assets):
    r = (debt - cashneq) / assets.replace(0, np.nan)
    b = _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net debt-to-assets [yoy252]
def f22bs_f22_balance_sheet_survival_ndassets_yoy252_252d_base_v135_signal(debt, cashneq, assets):
    r = (debt - cashneq) / assets.replace(0, np.nan)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net debt-to-assets [dsp126]
def f22bs_f22_balance_sheet_survival_ndassets_dsp126_126d_base_v136_signal(debt, cashneq, assets):
    r = (debt - cashneq) / assets.replace(0, np.nan)
    b = _std(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net debt-to-assets runup off 252d trough
def f22bs_f22_balance_sheet_survival_ndassets_runup_252d_base_v137_signal(debt, cashneq, assets):
    r = (debt - cashneq) / assets.replace(0, np.nan)
    trough = _rmin(r, 252)
    b = r - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- gross-minus-net debt/equity divergence (cash buffer share) ----
# cash buffer relative to equity (gross minus net debt/equity) [lvl]
def f22bs_f22_balance_sheet_survival_cashbufeq_lvl_63d_base_v138_signal(debt, cashneq, equity):
    gross = _debt_equity(debt, equity)
    net = _net_debt_equity(debt, cashneq, equity)
    b = gross - net
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# cash-buffer-to-equity spread [z252]
def f22bs_f22_balance_sheet_survival_cashbufeq_z252_252d_base_v139_signal(debt, cashneq, equity):
    gross = _debt_equity(debt, equity)
    net = _net_debt_equity(debt, cashneq, equity)
    b = _z(gross - net, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# cash-buffer-to-equity spread [chg126]
def f22bs_f22_balance_sheet_survival_cashbufeq_chg126_126d_base_v140_signal(debt, cashneq, equity):
    gross = _debt_equity(debt, equity)
    net = _net_debt_equity(debt, cashneq, equity)
    r = gross - net
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- leverage-mix divergence: debt/equity vs debt/assets (capital-mix structure) ----
# leverage-mix divergence (debt/equity minus 5x debt/assets) [lvl]
def f22bs_f22_balance_sheet_survival_levmix_lvl_63d_base_v141_signal(debt, equity, assets):
    de = _debt_equity(debt, equity).clip(lower=-10.0, upper=10.0)
    da = _debt_assets(debt, assets)
    b = de - 5.0 * da
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# leverage-mix divergence [z252]
def f22bs_f22_balance_sheet_survival_levmix_z252_252d_base_v142_signal(debt, equity, assets):
    de = _debt_equity(debt, equity).clip(lower=-10.0, upper=10.0)
    da = _debt_assets(debt, assets)
    b = _z(de - 5.0 * da, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# leverage-mix divergence [chg126]
def f22bs_f22_balance_sheet_survival_levmix_chg126_126d_base_v143_signal(debt, equity, assets):
    de = _debt_equity(debt, equity).clip(lower=-10.0, upper=10.0)
    da = _debt_assets(debt, assets)
    r = de - 5.0 * da
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- gross gearing debt/(debt+equity) curvature/term facets (no cash) ----
# gross gearing curvature (acceleration of the gearing structure)
def f22bs_f22_balance_sheet_survival_grsgear_curv_63d_base_v144_signal(debt, equity):
    r = _gross_gear(debt, equity)
    b = r - 0.5 * (r.shift(63) + r.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross gearing term spread (short minus long)
def f22bs_f22_balance_sheet_survival_grsgear_term_base_v145_signal(debt, equity):
    r = _gross_gear(debt, equity)
    b = r.rolling(63, min_periods=21).mean() - r.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross gearing [dsp126]
def f22bs_f22_balance_sheet_survival_grsgear_dsp126_126d_base_v146_signal(debt, equity):
    b = _std(_gross_gear(debt, equity), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- liquidity-buffer (cash+wc) vs debt stack dynamics ----
# cash+wc liquidity stack relative to the debt stack [chg63]
def f22bs_f22_balance_sheet_survival_liqbuf_chg63_63d_base_v147_signal(cashneq, workingcapital, debt):
    r = ((cashneq + workingcapital) / debt.replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# cash+wc liquidity stack relative to debt [dsp126]
def f22bs_f22_balance_sheet_survival_liqbuf_dsp126_126d_base_v148_signal(cashneq, workingcapital, debt):
    r = ((cashneq + workingcapital) / debt.replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    b = _std(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# cash+wc liquidity stack relative to debt drawdown off 252d peak
def f22bs_f22_balance_sheet_survival_liqbuf_dd252_252d_base_v149_signal(cashneq, workingcapital, debt):
    r = ((cashneq + workingcapital) / debt.replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    peak = _rmax(r, 252)
    b = r - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# cash+wc liquidity stack relative to debt term spread
def f22bs_f22_balance_sheet_survival_liqbuf_term_base_v150_signal(cashneq, workingcapital, debt):
    r = ((cashneq + workingcapital) / debt.replace(0, np.nan)).clip(lower=-50.0, upper=50.0)
    b = r.rolling(63, min_periods=21).mean() - r.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22bs_f22_balance_sheet_survival_ndeq_z126_126d_base_v076_signal,
    f22bs_f22_balance_sheet_survival_ndeq_dsp126_126d_base_v077_signal,
    f22bs_f22_balance_sheet_survival_ndeq_yoy252_252d_base_v078_signal,
    f22bs_f22_balance_sheet_survival_ndeq_rng252_252d_base_v079_signal,
    f22bs_f22_balance_sheet_survival_ndeq_curv_63d_base_v080_signal,
    f22bs_f22_balance_sheet_survival_dbteq_dsp126_126d_base_v081_signal,
    f22bs_f22_balance_sheet_survival_dbteq_yoy252_252d_base_v082_signal,
    f22bs_f22_balance_sheet_survival_dbteq_rng252_252d_base_v083_signal,
    f22bs_f22_balance_sheet_survival_dbteq_disp_126d_base_v084_signal,
    f22bs_f22_balance_sheet_survival_dbteq_smz63_63d_base_v085_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_dsp126_126d_base_v086_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_smz63_63d_base_v087_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_rng252_252d_base_v088_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_runup_252d_base_v089_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_term_base_v090_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_z126_126d_base_v091_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_chg63_63d_base_v092_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_ema63_63d_base_v093_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_dd252_252d_base_v094_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_term_base_v095_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_z126_126d_base_v096_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_chg63_63d_base_v097_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_dsp126_126d_base_v098_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_smz63_63d_base_v099_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_yoy252_252d_base_v100_signal,
    f22bs_f22_balance_sheet_survival_wcdebt_lvl_63d_base_v101_signal,
    f22bs_f22_balance_sheet_survival_wcdebt_z252_252d_base_v102_signal,
    f22bs_f22_balance_sheet_survival_wcdebt_rnk252_252d_base_v103_signal,
    f22bs_f22_balance_sheet_survival_wcdebt_chg126_126d_base_v104_signal,
    f22bs_f22_balance_sheet_survival_wcdebt_dsp126_126d_base_v105_signal,
    f22bs_f22_balance_sheet_survival_curratio_ema63_63d_base_v106_signal,
    f22bs_f22_balance_sheet_survival_curratio_smz63_63d_base_v107_signal,
    f22bs_f22_balance_sheet_survival_curratio_yoy252_252d_base_v108_signal,
    f22bs_f22_balance_sheet_survival_curratio_dd252_252d_base_v109_signal,
    f22bs_f22_balance_sheet_survival_curratio_term_base_v110_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_rng252_252d_base_v111_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_rng252_252d_base_v112_signal,
    f22bs_f22_balance_sheet_survival_quick_dsp126_126d_base_v113_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_rnk252_252d_base_v114_signal,
    f22bs_f22_balance_sheet_survival_netgear_rnk252_252d_base_v115_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_rnk252_252d_base_v116_signal,
    f22bs_f22_balance_sheet_survival_wcdebt_smz63_63d_base_v117_signal,
    f22bs_f22_balance_sheet_survival_dbtquick_z252_252d_base_v118_signal,
    f22bs_f22_balance_sheet_survival_dbtgrow_q63_63d_base_v119_signal,
    f22bs_f22_balance_sheet_survival_dbtlevel_z126_126d_base_v120_signal,
    f22bs_f22_balance_sheet_survival_dbtdd_252d_base_v121_signal,
    f22bs_f22_balance_sheet_survival_dbtgrow_h126_126d_base_v122_signal,
    f22bs_f22_balance_sheet_survival_dbtrunup_504d_base_v123_signal,
    f22bs_f22_balance_sheet_survival_dbtcurr_lvl_63d_base_v124_signal,
    f22bs_f22_balance_sheet_survival_dbtcurr_z252_252d_base_v125_signal,
    f22bs_f22_balance_sheet_survival_dbtcurr_rnk252_252d_base_v126_signal,
    f22bs_f22_balance_sheet_survival_dbtcurr_chg126_126d_base_v127_signal,
    f22bs_f22_balance_sheet_survival_dbtcurr_smz63_63d_base_v128_signal,
    f22bs_f22_balance_sheet_survival_matpress_lvl_63d_base_v129_signal,
    f22bs_f22_balance_sheet_survival_matpress_z252_252d_base_v130_signal,
    f22bs_f22_balance_sheet_survival_matpress_rnk252_252d_base_v131_signal,
    f22bs_f22_balance_sheet_survival_matpress_chg126_126d_base_v132_signal,
    f22bs_f22_balance_sheet_survival_matpress_dsp126_126d_base_v133_signal,
    f22bs_f22_balance_sheet_survival_ndassets_z126_126d_base_v134_signal,
    f22bs_f22_balance_sheet_survival_ndassets_yoy252_252d_base_v135_signal,
    f22bs_f22_balance_sheet_survival_ndassets_dsp126_126d_base_v136_signal,
    f22bs_f22_balance_sheet_survival_ndassets_runup_252d_base_v137_signal,
    f22bs_f22_balance_sheet_survival_cashbufeq_lvl_63d_base_v138_signal,
    f22bs_f22_balance_sheet_survival_cashbufeq_z252_252d_base_v139_signal,
    f22bs_f22_balance_sheet_survival_cashbufeq_chg126_126d_base_v140_signal,
    f22bs_f22_balance_sheet_survival_levmix_lvl_63d_base_v141_signal,
    f22bs_f22_balance_sheet_survival_levmix_z252_252d_base_v142_signal,
    f22bs_f22_balance_sheet_survival_levmix_chg126_126d_base_v143_signal,
    f22bs_f22_balance_sheet_survival_grsgear_curv_63d_base_v144_signal,
    f22bs_f22_balance_sheet_survival_grsgear_term_base_v145_signal,
    f22bs_f22_balance_sheet_survival_grsgear_dsp126_126d_base_v146_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_chg63_63d_base_v147_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_dsp126_126d_base_v148_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_dd252_252d_base_v149_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_term_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_BALANCE_SHEET_SURVIVAL_REGISTRY_076_150 = REGISTRY


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

    debt = _fund(2201, base=8e7, drift=0.01, vol=0.14).rename("debt")
    debtusd = _fund(2202, base=8.2e7, drift=0.012, vol=0.15).rename("debtusd")
    equity = _fund(2203, base=1.5e8, drift=-0.01, vol=0.16, allow_neg=True).rename("equity")
    assets = _fund(2204, base=3.0e8, drift=0.005, vol=0.09).rename("assets")
    liabilities = _fund(2205, base=1.4e8, drift=0.008, vol=0.11).rename("liabilities")
    currentratio = (1.0 + _fund(2206, base=1.0, drift=0.0, vol=0.18).clip(lower=0.05)).rename("currentratio")
    workingcapital = _fund(2207, base=6e7, drift=0.0, vol=0.20, allow_neg=True).rename("workingcapital")
    cashneq = _fund(2208, base=5e7, drift=-0.005, vol=0.17).rename("cashneq")

    cols = {"debt": debt, "debtusd": debtusd, "equity": equity,
            "assets": assets, "liabilities": liabilities,
            "currentratio": currentratio, "workingcapital": workingcapital,
            "cashneq": cashneq}
    _FUND_SET = ("debt", "debtusd", "equity", "assets", "liabilities",
                 "currentratio", "workingcapital", "cashneq")

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in _FUND_SET for c in meta["inputs"]), name
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

    print("OK f22_balance_sheet_survival_base_076_150_claude: %d features pass" % n_features)
