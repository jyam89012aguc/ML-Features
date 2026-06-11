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
    # rolling min-max travel (dispersion of a structure ratio)
    return _rmax(s, w) - _rmin(s, w)


# ===== folder domain primitives: BALANCE-SHEET LEVERAGE & LIQUIDITY STRUCTURE =====
# f22 leans on the interest-bearing `debt`/`debtusd` columns and `currentratio`
# (which the f21 distress family does NOT use) so its leverage/liquidity STRUCTURE
# ratios stay structurally distinct from f21's liabilities-based Altman-Z distress
# composites and its cash/assets-z & cash/liabilities-z going-concern flags.
def _abs_floor(s):
    # signed equity can flip through zero; |equity| as a denominator keeps the ratio finite
    return s.abs().replace(0, np.nan)


def _debt_equity(debt, equity):
    # gross financial leverage: interest-bearing debt against book equity cushion
    return (debt / _abs_floor(equity)).clip(lower=-50.0, upper=50.0)


def _debt_assets(debt, assets):
    return debt / assets.replace(0, np.nan)


def _debt_capital(debt, equity, cashneq):
    # debt-to-total-capitalization = debt / (debt + equity + cash); bounded structural
    # gearing on the full capital base. Including cash in the denominator de-couples this
    # from the gross debt/equity facet (which has no cash term).
    cap = (debt + equity + cashneq).replace(0, np.nan)
    return (debt / cap).clip(lower=-5.0, upper=5.0)


def _net_debt_equity(debt, cashneq, equity):
    # net financial gearing: debt net of liquid cash, per unit of book equity
    return ((debt - cashneq) / _abs_floor(equity)).clip(lower=-50.0, upper=50.0)


def _net_gearing(debt, cashneq, equity):
    # net debt / (net debt + equity): bounded net-leverage structure
    nd = debt - cashneq
    cap = (nd + equity).replace(0, np.nan)
    return (nd / cap).clip(lower=-5.0, upper=5.0)


def _cash_debt(cashneq, debt):
    # cash coverage of interest-bearing debt (NOT cash/liabilities, which f21 owns)
    return cashneq / debt.replace(0, np.nan)


def _debt_wc(debt, workingcapital):
    # leverage relative to the working-capital cushion
    return (debt / _abs_floor(workingcapital)).clip(lower=-50.0, upper=50.0)


def _quick_ratio(currentratio, cashneq, liabilities):
    # conservative liquidity facet derived from the reported current ratio, hair-cut
    # toward cash so it is NOT the cash/liabilities coverage f21 owns
    cl = (cashneq / liabilities.replace(0, np.nan)).clip(lower=0.0, upper=10.0)
    return (0.5 * currentratio + cl).clip(lower=0.0, upper=20.0)


def _liq_buffer_debt(cashneq, workingcapital, debt):
    # liquidity buffer (cash + working capital) measured against the debt stack
    return ((cashneq + workingcapital) / debt.replace(0, np.nan)).clip(lower=-50.0, upper=50.0)


def _usd_prem(debtusd, debt):
    # USD-denominated share of the debt stack (FX / cross-listing structure)
    return (debtusd / debt.replace(0, np.nan)).clip(lower=-5.0, upper=10.0)


# ============================================================
# ---- debt / equity (gross financial leverage) ----
# gross debt-to-equity [lvl]
def f22bs_f22_balance_sheet_survival_dbteq_lvl_63d_base_v001_signal(debt, equity):
    b = _debt_equity(debt, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-equity [z252]
def f22bs_f22_balance_sheet_survival_dbteq_z252_252d_base_v002_signal(debt, equity):
    b = _z(_debt_equity(debt, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-equity [z126]
def f22bs_f22_balance_sheet_survival_dbteq_z126_126d_base_v003_signal(debt, equity):
    b = _z(_debt_equity(debt, equity), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-equity [rnk252]
def f22bs_f22_balance_sheet_survival_dbteq_rnk252_252d_base_v004_signal(debt, equity):
    b = _rank(_debt_equity(debt, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-equity [chg126]
def f22bs_f22_balance_sheet_survival_dbteq_chg126_126d_base_v005_signal(debt, equity):
    r = _debt_equity(debt, equity)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-equity [chg63]
def f22bs_f22_balance_sheet_survival_dbteq_chg63_63d_base_v006_signal(debt, equity):
    r = _debt_equity(debt, equity)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- debt / assets (asset-based leverage) ----
# gross debt-to-assets [lvl]
def f22bs_f22_balance_sheet_survival_dbtassets_lvl_63d_base_v007_signal(debt, assets):
    b = _debt_assets(debt, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-assets [z252]
def f22bs_f22_balance_sheet_survival_dbtassets_z252_252d_base_v008_signal(debt, assets):
    b = _z(_debt_assets(debt, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-assets [z126]
def f22bs_f22_balance_sheet_survival_dbtassets_z126_126d_base_v009_signal(debt, assets):
    b = _z(_debt_assets(debt, assets), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-assets [rnk252]
def f22bs_f22_balance_sheet_survival_dbtassets_rnk252_252d_base_v010_signal(debt, assets):
    b = _rank(_debt_assets(debt, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-assets [chg126]
def f22bs_f22_balance_sheet_survival_dbtassets_chg126_126d_base_v011_signal(debt, assets):
    r = _debt_assets(debt, assets)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt-to-assets [yoy252]
def f22bs_f22_balance_sheet_survival_dbtassets_yoy252_252d_base_v012_signal(debt, assets):
    r = _debt_assets(debt, assets)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- debt-to-capital (bounded structural gearing) ----
# debt-to-capital [lvl]
def f22bs_f22_balance_sheet_survival_dbtcap_lvl_63d_base_v013_signal(debt, equity, cashneq):
    b = _debt_capital(debt, equity, cashneq)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-capital dispersion (gearing volatility through the cycle) [dsp126]
def f22bs_f22_balance_sheet_survival_dbtcap_dsp126_126d_base_v014_signal(debt, equity, cashneq):
    b = _std(_debt_capital(debt, equity, cashneq), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-capital travel range (gearing min-max swing) [rng252]
def f22bs_f22_balance_sheet_survival_dbtcap_rng252_252d_base_v015_signal(debt, equity, cashneq):
    b = _rng(_debt_capital(debt, equity, cashneq), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-capital displacement from slow EMA (gearing regime displacement)
def f22bs_f22_balance_sheet_survival_dbtcap_disp_126d_base_v016_signal(debt, equity, cashneq):
    r = _debt_capital(debt, equity, cashneq)
    b = r - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-capital term spread (short minus long gearing)
def f22bs_f22_balance_sheet_survival_dbtcap_term_base_v017_signal(debt, equity, cashneq):
    r = _debt_capital(debt, equity, cashneq)
    b = r.rolling(63, min_periods=21).mean() - r.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-capital curvature (acceleration of the gearing structure)
def f22bs_f22_balance_sheet_survival_dbtcap_curv_63d_base_v018_signal(debt, equity, cashneq):
    r = _debt_capital(debt, equity, cashneq)
    b = r - 0.5 * (r.shift(63) + r.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- net debt / equity (net financial gearing) ----
# net debt-to-equity [lvl]
def f22bs_f22_balance_sheet_survival_ndeq_lvl_63d_base_v019_signal(debt, cashneq, equity):
    b = _net_debt_equity(debt, cashneq, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net debt-to-equity [z252]
def f22bs_f22_balance_sheet_survival_ndeq_z252_252d_base_v020_signal(debt, cashneq, equity):
    b = _z(_net_debt_equity(debt, cashneq, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net debt-to-equity [rnk252]
def f22bs_f22_balance_sheet_survival_ndeq_rnk252_252d_base_v021_signal(debt, cashneq, equity):
    b = _rank(_net_debt_equity(debt, cashneq, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net debt-to-equity [chg126]
def f22bs_f22_balance_sheet_survival_ndeq_chg126_126d_base_v022_signal(debt, cashneq, equity):
    r = _net_debt_equity(debt, cashneq, equity)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net debt-to-equity [chg63]
def f22bs_f22_balance_sheet_survival_ndeq_chg63_63d_base_v023_signal(debt, cashneq, equity):
    r = _net_debt_equity(debt, cashneq, equity)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- net gearing nd/(nd+eq) (bounded) ----
# net gearing [lvl]
def f22bs_f22_balance_sheet_survival_netgear_lvl_63d_base_v024_signal(debt, cashneq, equity):
    b = _net_gearing(debt, cashneq, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net gearing [z252]
def f22bs_f22_balance_sheet_survival_netgear_z252_252d_base_v025_signal(debt, cashneq, equity):
    b = _z(_net_gearing(debt, cashneq, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net gearing [z126]
def f22bs_f22_balance_sheet_survival_netgear_z126_126d_base_v026_signal(debt, cashneq, equity):
    b = _z(_net_gearing(debt, cashneq, equity), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net gearing [chg126]
def f22bs_f22_balance_sheet_survival_netgear_chg126_126d_base_v027_signal(debt, cashneq, equity):
    r = _net_gearing(debt, cashneq, equity)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net gearing [smz63 deviation-from-mean]
def f22bs_f22_balance_sheet_survival_netgear_smz63_63d_base_v028_signal(debt, cashneq, equity):
    r = _net_gearing(debt, cashneq, equity)
    b = r - r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- net debt / assets (debt-based, NOT liabilities-based like f21) ----
# net debt-to-assets [lvl]
def f22bs_f22_balance_sheet_survival_ndassets_lvl_63d_base_v029_signal(debt, cashneq, assets):
    b = (debt - cashneq) / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net debt-to-assets [z252]
def f22bs_f22_balance_sheet_survival_ndassets_z252_252d_base_v030_signal(debt, cashneq, assets):
    r = (debt - cashneq) / assets.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net debt-to-assets [smz63 deviation-from-mean]
def f22bs_f22_balance_sheet_survival_ndassets_smz63_63d_base_v031_signal(debt, cashneq, assets):
    r = (debt - cashneq) / assets.replace(0, np.nan)
    b = r - r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net debt-to-assets [chg126]
def f22bs_f22_balance_sheet_survival_ndassets_chg126_126d_base_v032_signal(debt, cashneq, assets):
    r = (debt - cashneq) / assets.replace(0, np.nan)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net debt-to-assets [chg63]
def f22bs_f22_balance_sheet_survival_ndassets_chg63_63d_base_v033_signal(debt, cashneq, assets):
    r = (debt - cashneq) / assets.replace(0, np.nan)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- current ratio (reported short-term solvency; f21 does NOT use currentratio) ----
# current ratio [lvl]
def f22bs_f22_balance_sheet_survival_curratio_lvl_63d_base_v034_signal(currentratio):
    b = currentratio
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# current ratio [z252]
def f22bs_f22_balance_sheet_survival_curratio_z252_252d_base_v035_signal(currentratio):
    b = _z(currentratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# current ratio [z126]
def f22bs_f22_balance_sheet_survival_curratio_z126_126d_base_v036_signal(currentratio):
    b = _z(currentratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# current ratio [rnk252]
def f22bs_f22_balance_sheet_survival_curratio_rnk252_252d_base_v037_signal(currentratio):
    b = _rank(currentratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# current ratio [chg126]
def f22bs_f22_balance_sheet_survival_curratio_chg126_126d_base_v038_signal(currentratio):
    b = currentratio - currentratio.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# current ratio [chg63]
def f22bs_f22_balance_sheet_survival_curratio_chg63_63d_base_v039_signal(currentratio):
    b = currentratio - currentratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# current ratio [dsp126 dispersion]
def f22bs_f22_balance_sheet_survival_curratio_dsp126_126d_base_v040_signal(currentratio):
    b = _std(currentratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# current ratio shortfall vs its own 252d median (liquidity-tightening band)
def f22bs_f22_balance_sheet_survival_curratio_shortfall_63d_base_v041_signal(currentratio):
    med = currentratio.rolling(252, min_periods=126).median()
    b = (med - currentratio).clip(lower=0.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- quick-ratio proxy (cash-haircut liquidity, distinct from f21 cash/liab) ----
# quick-ratio proxy [lvl]
def f22bs_f22_balance_sheet_survival_quick_lvl_63d_base_v042_signal(currentratio, cashneq, liabilities):
    b = _quick_ratio(currentratio, cashneq, liabilities)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# quick-ratio proxy [z252]
def f22bs_f22_balance_sheet_survival_quick_z252_252d_base_v043_signal(currentratio, cashneq, liabilities):
    b = _z(_quick_ratio(currentratio, cashneq, liabilities), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# quick-ratio proxy [rnk252]
def f22bs_f22_balance_sheet_survival_quick_rnk252_252d_base_v044_signal(currentratio, cashneq, liabilities):
    b = _rank(_quick_ratio(currentratio, cashneq, liabilities), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# quick-ratio proxy [chg126]
def f22bs_f22_balance_sheet_survival_quick_chg126_126d_base_v045_signal(currentratio, cashneq, liabilities):
    r = _quick_ratio(currentratio, cashneq, liabilities)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-stack per unit of quick liquidity (leverage scaled by conservative liquidity)
def f22bs_f22_balance_sheet_survival_dbtquick_63d_base_v046_signal(debt, assets, currentratio, cashneq, liabilities):
    q = _quick_ratio(currentratio, cashneq, liabilities).clip(lower=0.05)
    da = _debt_assets(debt, assets).clip(lower=0.0, upper=2.0)
    b = da / q
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- cash / debt (debt coverage; denominator is interest-bearing debt) ----
# cash-to-debt [lvl]
def f22bs_f22_balance_sheet_survival_cashdebt_lvl_63d_base_v047_signal(cashneq, debt):
    b = _cash_debt(cashneq, debt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# cash-to-debt [z252]
def f22bs_f22_balance_sheet_survival_cashdebt_z252_252d_base_v048_signal(cashneq, debt):
    b = _z(_cash_debt(cashneq, debt), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# cash-to-debt [dsp126 dispersion]
def f22bs_f22_balance_sheet_survival_cashdebt_dsp126_126d_base_v049_signal(cashneq, debt):
    b = _std(_cash_debt(cashneq, debt), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# cash-to-debt [chg126]
def f22bs_f22_balance_sheet_survival_cashdebt_chg126_126d_base_v050_signal(cashneq, debt):
    r = _cash_debt(cashneq, debt)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# cash-to-debt [yoy252]
def f22bs_f22_balance_sheet_survival_cashdebt_yoy252_252d_base_v051_signal(cashneq, debt):
    r = _cash_debt(cashneq, debt)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- debt / working capital ----
# debt-to-working-capital [lvl]
def f22bs_f22_balance_sheet_survival_dbtwc_lvl_63d_base_v052_signal(debt, workingcapital):
    b = _debt_wc(debt, workingcapital)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-working-capital [z252]
def f22bs_f22_balance_sheet_survival_dbtwc_z252_252d_base_v053_signal(debt, workingcapital):
    b = _z(_debt_wc(debt, workingcapital), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-working-capital [rnk252]
def f22bs_f22_balance_sheet_survival_dbtwc_rnk252_252d_base_v054_signal(debt, workingcapital):
    b = _rank(_debt_wc(debt, workingcapital), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-working-capital [chg126]
def f22bs_f22_balance_sheet_survival_dbtwc_chg126_126d_base_v055_signal(debt, workingcapital):
    r = _debt_wc(debt, workingcapital)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- liquidity buffer (cash+wc) / debt ----
# liquidity-buffer-to-debt [lvl]
def f22bs_f22_balance_sheet_survival_liqbuf_lvl_63d_base_v056_signal(cashneq, workingcapital, debt):
    b = _liq_buffer_debt(cashneq, workingcapital, debt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# liquidity-buffer-to-debt [z252]
def f22bs_f22_balance_sheet_survival_liqbuf_z252_252d_base_v057_signal(cashneq, workingcapital, debt):
    b = _z(_liq_buffer_debt(cashneq, workingcapital, debt), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# liquidity-buffer-to-debt [yoy252]
def f22bs_f22_balance_sheet_survival_liqbuf_yoy252_252d_base_v058_signal(cashneq, workingcapital, debt):
    r = _liq_buffer_debt(cashneq, workingcapital, debt)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# liquidity-buffer-to-debt [chg126]
def f22bs_f22_balance_sheet_survival_liqbuf_chg126_126d_base_v059_signal(cashneq, workingcapital, debt):
    r = _liq_buffer_debt(cashneq, workingcapital, debt)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# liquidity-buffer-to-debt [smz63]
def f22bs_f22_balance_sheet_survival_liqbuf_smz63_63d_base_v060_signal(cashneq, workingcapital, debt):
    r = _liq_buffer_debt(cashneq, workingcapital, debt)
    b = r - r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- debtusd / assets (USD-reported leverage; one facet — on real miners debtusd≈debt) ----
# usd-debt-to-assets [lvl]
def f22bs_f22_balance_sheet_survival_dbtusdassets_lvl_63d_base_v061_signal(debtusd, assets):
    b = debtusd / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- additional leverage/liquidity facets (debt-centric) ----
# debt-to-equity curvature (acceleration of gross leverage) [curv]
def f22bs_f22_balance_sheet_survival_dbteq_curv_63d_base_v062_signal(debt, equity):
    r = _debt_equity(debt, equity)
    b = r - 0.5 * (r.shift(63) + r.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-assets curvature (acceleration of asset leverage) [curv]
def f22bs_f22_balance_sheet_survival_dbtassets_curv_63d_base_v063_signal(debt, assets):
    r = _debt_assets(debt, assets)
    b = r - 0.5 * (r.shift(63) + r.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net gearing dispersion (net-leverage structure volatility) [dsp126]
def f22bs_f22_balance_sheet_survival_netgear_dsp126_126d_base_v064_signal(debt, cashneq, equity):
    b = _std(_net_gearing(debt, cashneq, equity), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# cash-to-debt dispersion (debt-coverage volatility) [dsp63]
def f22bs_f22_balance_sheet_survival_cashdebt_dsp63_63d_base_v065_signal(cashneq, debt):
    b = _std(_cash_debt(cashneq, debt), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-capital deviation from its own 63d mean (gearing displacement) [smz63]
def f22bs_f22_balance_sheet_survival_dbtcap_smz63_63d_base_v066_signal(debt, equity, cashneq):
    r = _debt_capital(debt, equity, cashneq)
    b = r - r.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# liquidity-buffer-to-debt dispersion (liquidity-vs-debt volatility) [dsp63]
def f22bs_f22_balance_sheet_survival_liqbuf_dsp63_63d_base_v067_signal(cashneq, workingcapital, debt):
    b = _std(_liq_buffer_debt(cashneq, workingcapital, debt), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- debt level dynamics (debt stack trajectory, normalized to its own history) ----
# gross debt z-level (stack growth vs own scale) [z252]
def f22bs_f22_balance_sheet_survival_dbtlevel_z252_252d_base_v068_signal(debt):
    b = _z(debt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt log-growth over a year (debt build/paydown rate)
def f22bs_f22_balance_sheet_survival_dbtgrow_yoy252_252d_base_v069_signal(debt):
    b = np.log(debt.replace(0, np.nan) / debt.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gross debt drawup off its 252d trough (re-leveraging distance)
def f22bs_f22_balance_sheet_survival_dbtrunup_252d_base_v070_signal(debt):
    trough = _rmin(debt, 252)
    b = debt / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- current-ratio buffer vs the debt stack (liquidity-vs-leverage interaction) ----
# current-ratio scaled by debt-light structure: currentratio x (1 - debt/assets)
def f22bs_f22_balance_sheet_survival_dbtcap_z126_126d_base_v071_signal(debt, equity, cashneq):
    b = _z(_debt_capital(debt, equity, cashneq), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-capital change over a half-year (gearing build/paydown) [chg126]
def f22bs_f22_balance_sheet_survival_dbtcap_chg126_126d_base_v072_signal(debt, equity, cashneq):
    r = _debt_capital(debt, equity, cashneq)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# debt-to-capital change over a quarter (gearing momentum) [chg63]
def f22bs_f22_balance_sheet_survival_dbtcap_chg63_63d_base_v073_signal(debt, equity, cashneq):
    r = _debt_capital(debt, equity, cashneq)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ---- equity term-structure of leverage (short vs long debt-to-equity) ----
# debt-to-equity short-minus-long term spread (leverage regime shift)
def f22bs_f22_balance_sheet_survival_dbteqterm_base_v074_signal(debt, equity):
    r = _debt_equity(debt, equity)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# net-debt-to-equity short-minus-long term spread
def f22bs_f22_balance_sheet_survival_ndeqterm_base_v075_signal(debt, cashneq, equity):
    r = _net_debt_equity(debt, cashneq, equity)
    short = r.rolling(63, min_periods=21).mean()
    long = r.rolling(252, min_periods=126).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22bs_f22_balance_sheet_survival_dbteq_lvl_63d_base_v001_signal,
    f22bs_f22_balance_sheet_survival_dbteq_z252_252d_base_v002_signal,
    f22bs_f22_balance_sheet_survival_dbteq_z126_126d_base_v003_signal,
    f22bs_f22_balance_sheet_survival_dbteq_rnk252_252d_base_v004_signal,
    f22bs_f22_balance_sheet_survival_dbteq_chg126_126d_base_v005_signal,
    f22bs_f22_balance_sheet_survival_dbteq_chg63_63d_base_v006_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_lvl_63d_base_v007_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_z252_252d_base_v008_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_z126_126d_base_v009_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_rnk252_252d_base_v010_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_chg126_126d_base_v011_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_yoy252_252d_base_v012_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_lvl_63d_base_v013_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_dsp126_126d_base_v014_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_rng252_252d_base_v015_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_disp_126d_base_v016_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_term_base_v017_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_curv_63d_base_v018_signal,
    f22bs_f22_balance_sheet_survival_ndeq_lvl_63d_base_v019_signal,
    f22bs_f22_balance_sheet_survival_ndeq_z252_252d_base_v020_signal,
    f22bs_f22_balance_sheet_survival_ndeq_rnk252_252d_base_v021_signal,
    f22bs_f22_balance_sheet_survival_ndeq_chg126_126d_base_v022_signal,
    f22bs_f22_balance_sheet_survival_ndeq_chg63_63d_base_v023_signal,
    f22bs_f22_balance_sheet_survival_netgear_lvl_63d_base_v024_signal,
    f22bs_f22_balance_sheet_survival_netgear_z252_252d_base_v025_signal,
    f22bs_f22_balance_sheet_survival_netgear_z126_126d_base_v026_signal,
    f22bs_f22_balance_sheet_survival_netgear_chg126_126d_base_v027_signal,
    f22bs_f22_balance_sheet_survival_netgear_smz63_63d_base_v028_signal,
    f22bs_f22_balance_sheet_survival_ndassets_lvl_63d_base_v029_signal,
    f22bs_f22_balance_sheet_survival_ndassets_z252_252d_base_v030_signal,
    f22bs_f22_balance_sheet_survival_ndassets_smz63_63d_base_v031_signal,
    f22bs_f22_balance_sheet_survival_ndassets_chg126_126d_base_v032_signal,
    f22bs_f22_balance_sheet_survival_ndassets_chg63_63d_base_v033_signal,
    f22bs_f22_balance_sheet_survival_curratio_lvl_63d_base_v034_signal,
    f22bs_f22_balance_sheet_survival_curratio_z252_252d_base_v035_signal,
    f22bs_f22_balance_sheet_survival_curratio_z126_126d_base_v036_signal,
    f22bs_f22_balance_sheet_survival_curratio_rnk252_252d_base_v037_signal,
    f22bs_f22_balance_sheet_survival_curratio_chg126_126d_base_v038_signal,
    f22bs_f22_balance_sheet_survival_curratio_chg63_63d_base_v039_signal,
    f22bs_f22_balance_sheet_survival_curratio_dsp126_126d_base_v040_signal,
    f22bs_f22_balance_sheet_survival_curratio_shortfall_63d_base_v041_signal,
    f22bs_f22_balance_sheet_survival_quick_lvl_63d_base_v042_signal,
    f22bs_f22_balance_sheet_survival_quick_z252_252d_base_v043_signal,
    f22bs_f22_balance_sheet_survival_quick_rnk252_252d_base_v044_signal,
    f22bs_f22_balance_sheet_survival_quick_chg126_126d_base_v045_signal,
    f22bs_f22_balance_sheet_survival_dbtquick_63d_base_v046_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_lvl_63d_base_v047_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_z252_252d_base_v048_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_dsp126_126d_base_v049_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_chg126_126d_base_v050_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_yoy252_252d_base_v051_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_lvl_63d_base_v052_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_z252_252d_base_v053_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_rnk252_252d_base_v054_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_chg126_126d_base_v055_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_lvl_63d_base_v056_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_z252_252d_base_v057_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_yoy252_252d_base_v058_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_chg126_126d_base_v059_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_smz63_63d_base_v060_signal,
    f22bs_f22_balance_sheet_survival_dbtusdassets_lvl_63d_base_v061_signal,
    f22bs_f22_balance_sheet_survival_dbteq_curv_63d_base_v062_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_curv_63d_base_v063_signal,
    f22bs_f22_balance_sheet_survival_netgear_dsp126_126d_base_v064_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_dsp63_63d_base_v065_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_smz63_63d_base_v066_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_dsp63_63d_base_v067_signal,
    f22bs_f22_balance_sheet_survival_dbtlevel_z252_252d_base_v068_signal,
    f22bs_f22_balance_sheet_survival_dbtgrow_yoy252_252d_base_v069_signal,
    f22bs_f22_balance_sheet_survival_dbtrunup_252d_base_v070_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_z126_126d_base_v071_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_chg126_126d_base_v072_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_chg63_63d_base_v073_signal,
    f22bs_f22_balance_sheet_survival_dbteqterm_base_v074_signal,
    f22bs_f22_balance_sheet_survival_ndeqterm_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_BALANCE_SHEET_SURVIVAL_REGISTRY_001_075 = REGISTRY


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

    print("OK f22_balance_sheet_survival_base_001_075_claude: %d features pass" % n_features)
