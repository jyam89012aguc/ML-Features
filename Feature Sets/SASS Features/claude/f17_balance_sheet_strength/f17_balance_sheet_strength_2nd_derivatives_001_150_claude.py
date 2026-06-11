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


def _slope(s, w):
    # 1st math derivative: per-period change over a w-day window
    return (s - s.shift(w)) / float(w)


# ===== balance-sheet level primitives (slopes are taken OF these) =====
def _f17_ndte(debt, cashneq, equity):
    return _safe_div(debt - cashneq, equity)


def _f17_dta(debt, assets):
    return _safe_div(debt, assets)


def _f17_eta(equity, assets):
    return _safe_div(equity, assets)


def _f17_lta(liabilities, assets):
    return _safe_div(liabilities, assets)


def _f17_cta(cashneq, assets):
    return _safe_div(cashneq, assets)


def _f17_wcta(workingcapital, assets):
    return _safe_div(workingcapital, assets)


def _f17_ctd(cashneq, debt):
    return _safe_div(cashneq, debt)


def _f17_etl(equity, liabilities):
    return _safe_div(equity, liabilities)


def _f17_debtcap(debt, equity):
    return _safe_div(debt, debt + equity)


# ============================================================
# slope of net debt / equity over a quarter
def f17bs_f17_balance_sheet_strength_ndte_63d_slope_v001_signal(debt, cashneq, equity):
    base = _f17_ndte(debt, cashneq, equity)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net debt / equity over half a year
def f17bs_f17_balance_sheet_strength_ndte_126d_slope_v002_signal(debt, cashneq, equity):
    base = _f17_ndte(debt, cashneq, equity)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of gross-debt/equity standardized by its own 252d volatility, over a quarter
def f17bs_f17_balance_sheet_strength_gdte_63d_slope_v003_signal(debt, equity):
    base = _safe_div(debt, equity)
    sd = _std(base, 252)
    b = _slope(base, 63) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debt / assets over a quarter
def f17bs_f17_balance_sheet_strength_dta_63d_slope_v004_signal(debt, assets):
    base = _f17_dta(debt, assets)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debt / assets over half a year
def f17bs_f17_balance_sheet_strength_dta_126d_slope_v005_signal(debt, assets):
    base = _f17_dta(debt, assets)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity / assets over a quarter
def f17bs_f17_balance_sheet_strength_eta_63d_slope_v006_signal(equity, assets):
    base = _f17_eta(equity, assets)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity / assets over half a year
def f17bs_f17_balance_sheet_strength_eta_126d_slope_v007_signal(equity, assets):
    base = _f17_eta(equity, assets)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of liabilities / assets over a quarter
def f17bs_f17_balance_sheet_strength_lta_63d_slope_v008_signal(liabilities, assets):
    base = _f17_lta(liabilities, assets)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash / assets over a month
def f17bs_f17_balance_sheet_strength_cta_21d_slope_v009_signal(cashneq, assets):
    base = _f17_cta(cashneq, assets)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash / assets over a quarter
def f17bs_f17_balance_sheet_strength_cta_63d_slope_v010_signal(cashneq, assets):
    base = _f17_cta(cashneq, assets)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of working-capital / assets over a quarter
def f17bs_f17_balance_sheet_strength_wcta_63d_slope_v011_signal(workingcapital, assets):
    base = _f17_wcta(workingcapital, assets)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of working-capital / assets over a month
def f17bs_f17_balance_sheet_strength_wcta_21d_slope_v012_signal(workingcapital, assets):
    base = _f17_wcta(workingcapital, assets)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of current ratio over a month
def f17bs_f17_balance_sheet_strength_curr_21d_slope_v013_signal(currentratio):
    b = _slope(currentratio, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of current ratio over a quarter
def f17bs_f17_balance_sheet_strength_curr_63d_slope_v014_signal(currentratio):
    b = _slope(currentratio, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash / debt coverage over a quarter
def f17bs_f17_balance_sheet_strength_ctd_63d_slope_v015_signal(cashneq, debt):
    base = _f17_ctd(cashneq, debt)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity / liabilities over a quarter
def f17bs_f17_balance_sheet_strength_etl_63d_slope_v016_signal(equity, liabilities):
    base = _f17_etl(equity, liabilities)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity / debt over a quarter
def f17bs_f17_balance_sheet_strength_etd_63d_slope_v017_signal(equity, debt):
    base = _safe_div(equity, debt)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net cash / assets over a quarter
def f17bs_f17_balance_sheet_strength_netcashta_63d_slope_v018_signal(cashneq, debt, assets):
    base = _safe_div(cashneq - debt, assets)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debtcap (debt/(debt+equity)) over a quarter
def f17bs_f17_balance_sheet_strength_debtcap_63d_slope_v019_signal(debt, equity):
    base = _f17_debtcap(debt, equity)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of assets / equity (leverage multiplier) over a quarter
def f17bs_f17_balance_sheet_strength_ate_63d_slope_v020_signal(assets, equity):
    base = _safe_div(assets, equity)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net debt / assets over half a year
def f17bs_f17_balance_sheet_strength_ndta_126d_slope_v021_signal(debt, cashneq, assets):
    base = _safe_div(debt - cashneq, assets)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash / liabilities over a quarter
def f17bs_f17_balance_sheet_strength_ctl_63d_slope_v022_signal(cashneq, liabilities):
    base = _safe_div(cashneq, liabilities)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of working-capital / liabilities over a quarter
def f17bs_f17_balance_sheet_strength_wctl_63d_slope_v023_signal(workingcapital, liabilities):
    base = _safe_div(workingcapital, liabilities)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debt / liabilities over a quarter
def f17bs_f17_balance_sheet_strength_dtl_63d_slope_v024_signal(debt, liabilities):
    base = _safe_div(debt, liabilities)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of USD debt / assets over a quarter
def f17bs_f17_balance_sheet_strength_dusdta_63d_slope_v025_signal(debtusd, assets):
    base = _safe_div(debtusd, assets)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of USD net debt / equity standardized by its 252d volatility, over a month
def f17bs_f17_balance_sheet_strength_ndusde_63d_slope_v026_signal(debtusd, cashneq, equity):
    base = _safe_div(debtusd - cashneq, equity)
    sd = _std(base, 252)
    b = _slope(base, 21) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of working-capital-to-assets x current-ratio composite standardized by 252d vol, over a month
def f17bs_f17_balance_sheet_strength_wcqual_63d_slope_v027_signal(workingcapital, assets, currentratio):
    base = _f17_wcta(workingcapital, assets) * currentratio
    sd = _std(base, 252)
    b = _slope(base, 21) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash / equity over a quarter
def f17bs_f17_balance_sheet_strength_cte_63d_slope_v028_signal(cashneq, equity):
    base = _safe_div(cashneq, equity)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of working-capital / equity over a quarter
def f17bs_f17_balance_sheet_strength_wcte_63d_slope_v029_signal(workingcapital, equity):
    base = _safe_div(workingcapital, equity)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of liabilities / equity (gearing) over a quarter
def f17bs_f17_balance_sheet_strength_lte_63d_slope_v030_signal(liabilities, equity):
    base = _safe_div(liabilities, equity)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of z-scored net-debt/equity over a month (de-trended leverage drift)
def f17bs_f17_balance_sheet_strength_ndtez_21d_slope_v031_signal(debt, cashneq, equity):
    base = _z(_f17_ndte(debt, cashneq, equity), 252)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of z-scored equity/assets over a month
def f17bs_f17_balance_sheet_strength_etaz_21d_slope_v032_signal(equity, assets):
    base = _z(_f17_eta(equity, assets), 252)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of z-scored debt/assets over a month
def f17bs_f17_balance_sheet_strength_dtaz_21d_slope_v033_signal(debt, assets):
    base = _z(_f17_dta(debt, assets), 252)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of z-scored current ratio over a month
def f17bs_f17_balance_sheet_strength_currz_21d_slope_v034_signal(currentratio):
    base = _z(currentratio, 252)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash / assets x current ratio composite over a quarter
def f17bs_f17_balance_sheet_strength_cashqual_63d_slope_v035_signal(cashneq, assets, currentratio):
    base = _f17_cta(cashneq, assets) * currentratio
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity/assets x current ratio composite standardized by 252d vol, over a quarter
def f17bs_f17_balance_sheet_strength_capliq_63d_slope_v036_signal(equity, assets, currentratio):
    base = _f17_eta(equity, assets) * currentratio
    sd = _std(base, 252)
    b = _slope(base, 63) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net-cash balance (cash-debt)/(cash+debt) standardized by 252d vol, over a quarter
def f17bs_f17_balance_sheet_strength_netcashbal_63d_slope_v037_signal(cashneq, debt):
    base = _safe_div(cashneq - debt, cashneq + debt)
    sd = _std(base, 252)
    b = _slope(base, 63) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of strength score (eta - dta + 0.25 cta) over a quarter
def f17bs_f17_balance_sheet_strength_strscore_63d_slope_v038_signal(equity, assets, debt, cashneq):
    base = _f17_eta(equity, assets) - _f17_dta(debt, assets) + 0.25 * _f17_cta(cashneq, assets)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of distress cushion (1.2 wc/a + 0.6 e/l - d/a) standardized by 252d vol, over a quarter
def f17bs_f17_balance_sheet_strength_distress_63d_slope_v039_signal(workingcapital, assets, equity, liabilities, debt):
    base = (1.2 * _f17_wcta(workingcapital, assets)
            + 0.6 * _f17_etl(equity, liabilities)
            - _f17_dta(debt, assets))
    sd = _std(base, 252)
    b = _slope(base, 63) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity/assets minus liabilities/assets over a quarter
def f17bs_f17_balance_sheet_strength_etanetlta_63d_slope_v040_signal(equity, liabilities, assets):
    base = _f17_eta(equity, assets) - _f17_lta(liabilities, assets)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net debt / equity over a month (short-horizon leverage drift)
def f17bs_f17_balance_sheet_strength_ndte_21d_slope_v041_signal(debt, cashneq, equity):
    base = _f17_ndte(debt, cashneq, equity)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debt / assets over a month
def f17bs_f17_balance_sheet_strength_dta_21d_slope_v042_signal(debt, assets):
    base = _f17_dta(debt, assets)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity / assets over a month
def f17bs_f17_balance_sheet_strength_eta_21d_slope_v043_signal(equity, assets):
    base = _f17_eta(equity, assets)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash / debt over a month
def f17bs_f17_balance_sheet_strength_ctd_21d_slope_v044_signal(cashneq, debt):
    base = _f17_ctd(cashneq, debt)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity / liabilities over a month
def f17bs_f17_balance_sheet_strength_etl_21d_slope_v045_signal(equity, liabilities):
    base = _f17_etl(equity, liabilities)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of working-capital / assets over half a year
def f17bs_f17_balance_sheet_strength_wcta_126d_slope_v046_signal(workingcapital, assets):
    base = _f17_wcta(workingcapital, assets)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash / assets over half a year
def f17bs_f17_balance_sheet_strength_cta_126d_slope_v047_signal(cashneq, assets):
    base = _f17_cta(cashneq, assets)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of liabilities / assets over half a year
def f17bs_f17_balance_sheet_strength_lta_126d_slope_v048_signal(liabilities, assets):
    base = _f17_lta(liabilities, assets)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of current ratio over half a year
def f17bs_f17_balance_sheet_strength_curr_126d_slope_v049_signal(currentratio):
    b = _slope(currentratio, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debtcap over half a year
def f17bs_f17_balance_sheet_strength_debtcap_126d_slope_v050_signal(debt, equity):
    base = _f17_debtcap(debt, equity)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash / debt over half a year
def f17bs_f17_balance_sheet_strength_ctd_126d_slope_v051_signal(cashneq, debt):
    base = _f17_ctd(cashneq, debt)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity / debt standardized by 252d vol, over a month
def f17bs_f17_balance_sheet_strength_etd_126d_slope_v052_signal(equity, debt):
    base = _safe_div(equity, debt)
    sd = _std(base, 252)
    b = _slope(base, 21) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net-cash/equity standardized by its 252d volatility, over half a year
def f17bs_f17_balance_sheet_strength_netcashte_63d_slope_v053_signal(cashneq, debt, equity):
    base = _safe_div(cashneq - debt, equity)
    sd = _std(base, 252)
    b = _slope(base, 126) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of (cash+wc)/debt liquidity coverage over a quarter
def f17bs_f17_balance_sheet_strength_liqtod_63d_slope_v054_signal(cashneq, workingcapital, debt):
    base = _safe_div(cashneq + workingcapital, debt)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debt / (cash+equity) over a quarter
def f17bs_f17_balance_sheet_strength_dtoce_63d_slope_v055_signal(debt, cashneq, equity):
    base = _safe_div(debt, cashneq + equity)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of log(equity/liabilities) over a quarter
def f17bs_f17_balance_sheet_strength_logetl_63d_slope_v056_signal(equity, liabilities):
    base = np.log(_f17_etl(equity, liabilities))
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of log(assets/liabilities) standardized by 252d vol, over half a year
def f17bs_f17_balance_sheet_strength_logatl_63d_slope_v057_signal(assets, liabilities):
    base = np.log(_safe_div(assets, liabilities))
    sd = _std(base, 252)
    b = _slope(base, 126) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash / liabilities over half a year
def f17bs_f17_balance_sheet_strength_ctl_126d_slope_v058_signal(cashneq, liabilities):
    base = _safe_div(cashneq, liabilities)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of USD debt / equity standardized by its 252d volatility, over a year
def f17bs_f17_balance_sheet_strength_dusde_63d_slope_v059_signal(debtusd, equity):
    base = _safe_div(debtusd, equity)
    sd = _std(base, 252)
    b = _slope(base, 252) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debt-to-equity z-score over a quarter (de-trended leverage drift)
def f17bs_f17_balance_sheet_strength_gdtez_63d_slope_v060_signal(debt, equity):
    base = _z(_safe_div(debt, equity), 252)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of liabilities/assets z-score over a quarter
def f17bs_f17_balance_sheet_strength_ltaz_63d_slope_v061_signal(liabilities, assets):
    base = _z(_f17_lta(liabilities, assets), 252)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash/assets z-score over a quarter
def f17bs_f17_balance_sheet_strength_ctaz_63d_slope_v062_signal(cashneq, assets):
    base = _z(_f17_cta(cashneq, assets), 252)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of working-capital/assets z-score over a quarter
def f17bs_f17_balance_sheet_strength_wctaz_63d_slope_v063_signal(workingcapital, assets):
    base = _z(_f17_wcta(workingcapital, assets), 252)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of EMA-smoothed equity/assets over a quarter (smoothed capitalization trend)
def f17bs_f17_balance_sheet_strength_etaema_63d_slope_v064_signal(equity, assets):
    base = _f17_eta(equity, assets).ewm(span=42, min_periods=21).mean()
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of EMA-smoothed debt/assets over a quarter
def f17bs_f17_balance_sheet_strength_dtaema_63d_slope_v065_signal(debt, assets):
    base = _f17_dta(debt, assets).ewm(span=42, min_periods=21).mean()
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of EMA-smoothed current ratio over a quarter
def f17bs_f17_balance_sheet_strength_currema_63d_slope_v066_signal(currentratio):
    base = currentratio.ewm(span=42, min_periods=21).mean()
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net debt / equity over a year (long deleveraging trend)
def f17bs_f17_balance_sheet_strength_ndte_252d_slope_v067_signal(debt, cashneq, equity):
    base = _f17_ndte(debt, cashneq, equity)
    b = _slope(base, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity / assets over a year
def f17bs_f17_balance_sheet_strength_eta_252d_slope_v068_signal(equity, assets):
    base = _f17_eta(equity, assets)
    b = _slope(base, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debt / assets over a year
def f17bs_f17_balance_sheet_strength_dta_252d_slope_v069_signal(debt, assets):
    base = _f17_dta(debt, assets)
    b = _slope(base, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash / debt over a year
def f17bs_f17_balance_sheet_strength_ctd_252d_slope_v070_signal(cashneq, debt):
    base = _f17_ctd(cashneq, debt)
    b = _slope(base, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of current ratio over a year
def f17bs_f17_balance_sheet_strength_curr_252d_slope_v071_signal(currentratio):
    b = _slope(currentratio, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of assets / equity over half a year
def f17bs_f17_balance_sheet_strength_ate_126d_slope_v072_signal(assets, equity):
    base = _safe_div(assets, equity)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of liabilities / equity over half a year
def f17bs_f17_balance_sheet_strength_lte_126d_slope_v073_signal(liabilities, equity):
    base = _safe_div(liabilities, equity)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net-debt/assets over a month
def f17bs_f17_balance_sheet_strength_ndta_21d_slope_v074_signal(debt, cashneq, assets):
    base = _safe_div(debt - cashneq, assets)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash + wc liquidity-to-assets standardized by 252d vol, over a quarter
def f17bs_f17_balance_sheet_strength_liqta_63d_slope_v075_signal(cashneq, workingcapital, assets):
    base = _f17_cta(cashneq, assets) + _f17_wcta(workingcapital, assets)
    sd = _std(base, 252)
    b = _slope(base, 63) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity/debt z-score over a quarter
def f17bs_f17_balance_sheet_strength_etdz_63d_slope_v076_signal(equity, debt):
    base = _z(_safe_div(equity, debt), 252)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net-cash/assets z-score over a quarter
def f17bs_f17_balance_sheet_strength_netcashtaz_63d_slope_v077_signal(cashneq, debt, assets):
    base = _z(_safe_div(cashneq - debt, assets), 252)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debt / liabilities over half a year
def f17bs_f17_balance_sheet_strength_dtl_126d_slope_v078_signal(debt, liabilities):
    base = _safe_div(debt, liabilities)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of working-capital / debt standardized by 252d vol, over a quarter
def f17bs_f17_balance_sheet_strength_wctd_63d_slope_v079_signal(workingcapital, debt):
    base = _safe_div(workingcapital, debt)
    sd = _std(base, 252)
    b = _slope(base, 63) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of USD debt mix (debtusd/debt) over a quarter
def f17bs_f17_balance_sheet_strength_usdmix_63d_slope_v080_signal(debtusd, debt):
    base = _safe_div(debtusd, debt)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of solvency margin (eta - dta) standardized by 252d vol, over a month
def f17bs_f17_balance_sheet_strength_solvmargin_63d_slope_v081_signal(equity, debt, assets):
    base = _f17_eta(equity, assets) - _f17_dta(debt, assets)
    sd = _std(base, 252)
    b = _slope(base, 21) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of clean-balance-sheet composite eta*(1-dta) standardized by 252d vol, over a quarter
def f17bs_f17_balance_sheet_strength_cleanbs_63d_slope_v082_signal(equity, assets, debt):
    base = _f17_eta(equity, assets) * (1.0 - _f17_dta(debt, assets))
    sd = _std(base, 252)
    b = _slope(base, 63) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of current ratio x equity/liabilities over a quarter
def f17bs_f17_balance_sheet_strength_shortlong_63d_slope_v083_signal(currentratio, equity, liabilities):
    base = currentratio * _f17_etl(equity, liabilities)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash/debt x current ratio coverage quality over a quarter
def f17bs_f17_balance_sheet_strength_covqual_63d_slope_v084_signal(cashneq, debt, currentratio):
    base = _f17_ctd(cashneq, debt) * currentratio
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net debt / equity over two years (multi-year deleveraging)
def f17bs_f17_balance_sheet_strength_ndte_504d_slope_v085_signal(debt, cashneq, equity):
    base = _f17_ndte(debt, cashneq, equity)
    b = _slope(base, 504)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity / assets over two years
def f17bs_f17_balance_sheet_strength_eta_504d_slope_v086_signal(equity, assets):
    base = _f17_eta(equity, assets)
    b = _slope(base, 504)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debt / assets over two years
def f17bs_f17_balance_sheet_strength_dta_504d_slope_v087_signal(debt, assets):
    base = _f17_dta(debt, assets)
    b = _slope(base, 504)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash / assets over two years
def f17bs_f17_balance_sheet_strength_cta_504d_slope_v088_signal(cashneq, assets):
    base = _f17_cta(cashneq, assets)
    b = _slope(base, 504)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of liabilities / assets over two years
def f17bs_f17_balance_sheet_strength_lta_504d_slope_v089_signal(liabilities, assets):
    base = _f17_lta(liabilities, assets)
    b = _slope(base, 504)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of working-capital / assets over a year
def f17bs_f17_balance_sheet_strength_wcta_252d_slope_v090_signal(workingcapital, assets):
    base = _f17_wcta(workingcapital, assets)
    b = _slope(base, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash / equity over half a year
def f17bs_f17_balance_sheet_strength_cte_126d_slope_v091_signal(cashneq, equity):
    base = _safe_div(cashneq, equity)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of working-capital / equity over half a year
def f17bs_f17_balance_sheet_strength_wcte_126d_slope_v092_signal(workingcapital, equity):
    base = _safe_div(workingcapital, equity)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debtcap over a month
def f17bs_f17_balance_sheet_strength_debtcap_21d_slope_v093_signal(debt, equity):
    base = _f17_debtcap(debt, equity)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity / liabilities over half a year
def f17bs_f17_balance_sheet_strength_etl_126d_slope_v094_signal(equity, liabilities):
    base = _f17_etl(equity, liabilities)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net-cash balance standardized by 252d vol, over half a year
def f17bs_f17_balance_sheet_strength_netcashbal_126d_slope_v095_signal(cashneq, debt):
    base = _safe_div(cashneq - debt, cashneq + debt)
    sd = _std(base, 252)
    b = _slope(base, 126) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of USD net debt / assets over a quarter
def f17bs_f17_balance_sheet_strength_netusdta_63d_slope_v096_signal(debtusd, cashneq, assets):
    base = _safe_div(debtusd - cashneq, assets)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity/assets minus debt/assets over half a year
def f17bs_f17_balance_sheet_strength_solvmargin_126d_slope_v097_signal(equity, debt, assets):
    base = _f17_eta(equity, assets) - _f17_dta(debt, assets)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of liquidity-vs-leverage gap z(curr) - z(d/a) over a quarter
def f17bs_f17_balance_sheet_strength_liqlevgap_63d_slope_v098_signal(currentratio, debt, assets):
    base = _z(currentratio, 252) - _z(_f17_dta(debt, assets), 252)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash/assets x current ratio runway over half a year
def f17bs_f17_balance_sheet_strength_runway_126d_slope_v099_signal(cashneq, assets, currentratio):
    base = _f17_cta(cashneq, assets) * currentratio
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of tanh-bounded net-debt/equity over a quarter
def f17bs_f17_balance_sheet_strength_ndtetanh_63d_slope_v100_signal(debt, cashneq, equity):
    base = np.tanh(_f17_ndte(debt, cashneq, equity))
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of log net-debt/equity (signed) over a quarter
def f17bs_f17_balance_sheet_strength_logndte_63d_slope_v101_signal(debt, cashneq, equity):
    nd = (debt - cashneq)
    base = np.sign(nd) * np.log1p((nd / equity.replace(0, np.nan)).abs())
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity/debt over a month
def f17bs_f17_balance_sheet_strength_etd_21d_slope_v102_signal(equity, debt):
    base = _safe_div(equity, debt)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash/liabilities over a month
def f17bs_f17_balance_sheet_strength_ctl_21d_slope_v103_signal(cashneq, liabilities):
    base = _safe_div(cashneq, liabilities)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of working-capital/liabilities over a month
def f17bs_f17_balance_sheet_strength_wctl_21d_slope_v104_signal(workingcapital, liabilities):
    base = _safe_div(workingcapital, liabilities)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debt/liabilities over a month
def f17bs_f17_balance_sheet_strength_dtl_21d_slope_v105_signal(debt, liabilities):
    base = _safe_div(debt, liabilities)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of liabilities/assets over a month
def f17bs_f17_balance_sheet_strength_lta_21d_slope_v106_signal(liabilities, assets):
    base = _f17_lta(liabilities, assets)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net-cash/(cash+debt) balance over a quarter (bounded net-liquidity drift)
def f17bs_f17_balance_sheet_strength_netcashbal2_63d_slope_v107_signal(cashneq, debt, equity):
    base = _safe_div(cashneq - debt, (cashneq + debt) + equity.abs())
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of (cash+wc)/liabilities standardized by 252d vol, over half a year
def f17bs_f17_balance_sheet_strength_liqcovl_63d_slope_v108_signal(cashneq, workingcapital, liabilities):
    base = _safe_div(cashneq + workingcapital, liabilities)
    sd = _std(base, 252)
    b = _slope(base, 126) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debt/(cash+equity) over half a year
def f17bs_f17_balance_sheet_strength_dtoce_126d_slope_v109_signal(debt, cashneq, equity):
    base = _safe_div(debt, cashneq + equity)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of blend z-score score over a quarter
def f17bs_f17_balance_sheet_strength_blendz_63d_slope_v110_signal(equity, debt, cashneq, assets):
    base = (_z(_f17_eta(equity, assets), 252)
            - _z(_f17_dta(debt, assets), 252)
            + _z(_f17_cta(cashneq, assets), 252))
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debtusd/liabilities over a quarter
def f17bs_f17_balance_sheet_strength_dusdtl_63d_slope_v111_signal(debtusd, liabilities):
    base = _safe_div(debtusd, liabilities)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of USD net debt / equity standardized by 252d vol, over half a year
def f17bs_f17_balance_sheet_strength_ndusde_126d_slope_v112_signal(debtusd, cashneq, equity):
    base = _safe_div(debtusd - cashneq, equity)
    sd = _std(base, 252)
    b = _slope(base, 126) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net liquidity score (curr*cta - dta) standardized by 252d vol, over a quarter
def f17bs_f17_balance_sheet_strength_netliq_63d_slope_v113_signal(currentratio, cashneq, assets, debt):
    base = currentratio * _f17_cta(cashneq, assets) - _f17_dta(debt, assets)
    sd = _std(base, 252)
    b = _slope(base, 63) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of harmonic liquidity (curr & cta) standardized by 252d vol, over a quarter
def f17bs_f17_balance_sheet_strength_liqdual_63d_slope_v114_signal(currentratio, cashneq, assets):
    cta = _f17_cta(cashneq, assets)
    base = _safe_div(2.0 * currentratio * cta, currentratio + cta)
    sd = _std(base, 252)
    b = _slope(base, 63) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity/assets x cash/debt over a quarter
def f17bs_f17_balance_sheet_strength_capcov_63d_slope_v115_signal(equity, assets, cashneq, debt):
    base = _f17_eta(equity, assets) * _f17_ctd(cashneq, debt)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net debt / liabilities over a quarter (net-leverage vs total obligations)
def f17bs_f17_balance_sheet_strength_ndtl_63d_slope_v116_signal(debt, cashneq, liabilities):
    base = _safe_div(debt - cashneq, liabilities)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash/equity over a month
def f17bs_f17_balance_sheet_strength_cte_21d_slope_v117_signal(cashneq, equity):
    base = _safe_div(cashneq, equity)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of working-capital/equity over a month
def f17bs_f17_balance_sheet_strength_wcte_21d_slope_v118_signal(workingcapital, equity):
    base = _safe_div(workingcapital, equity)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of assets/equity over a month
def f17bs_f17_balance_sheet_strength_ate_21d_slope_v119_signal(assets, equity):
    base = _safe_div(assets, equity)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of liabilities/equity standardized by 252d vol, over a month
def f17bs_f17_balance_sheet_strength_lte_21d_slope_v120_signal(liabilities, equity):
    base = _safe_div(liabilities, equity)
    sd = _std(base, 252)
    b = _slope(base, 21) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of solvency-liquidity combo z(eta)+z(curr) over a quarter
def f17bs_f17_balance_sheet_strength_solvliq_63d_slope_v121_signal(equity, assets, currentratio):
    base = _z(_f17_eta(equity, assets), 252) + _z(currentratio, 252)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash-vs-curr divergence z(cta)-z(curr) over a quarter
def f17bs_f17_balance_sheet_strength_cashqualdiv_63d_slope_v122_signal(cashneq, assets, currentratio):
    base = _z(_f17_cta(cashneq, assets), 252) - _z(currentratio, 252)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of joint coverage cash/debt x equity/liab over a quarter
def f17bs_f17_balance_sheet_strength_jointcov_63d_slope_v123_signal(cashneq, debt, equity, liabilities):
    base = _f17_ctd(cashneq, debt) * _f17_etl(equity, liabilities)
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of fragility (dta*(1-cov)*1/curr) standardized by 252d vol, over half a year
def f17bs_f17_balance_sheet_strength_fragility_63d_slope_v124_signal(debt, assets, cashneq, currentratio):
    cov = _f17_ctd(cashneq, debt).clip(upper=1.0)
    inv = _safe_div(pd.Series(1.0, index=currentratio.index), currentratio)
    base = _f17_dta(debt, assets) * (1.0 - cov) * inv
    sd = _std(base, 252)
    b = _slope(base, 126) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of buffer tilt cta/(cta+|wcta|) over a quarter
def f17bs_f17_balance_sheet_strength_buftilt_63d_slope_v125_signal(cashneq, workingcapital, assets):
    cta = _f17_cta(cashneq, assets)
    wcta = _f17_wcta(workingcapital, assets)
    base = _safe_div(cta, cta + wcta.abs())
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debt/assets minus cash/liabilities over half a year (leverage-vs-cash-coverage drift)
def f17bs_f17_balance_sheet_strength_levcovgap_126d_slope_v126_signal(debt, assets, cashneq, liabilities):
    base = _f17_dta(debt, assets) - _safe_div(cashneq, liabilities)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity/liabilities over a year
def f17bs_f17_balance_sheet_strength_etl_252d_slope_v127_signal(equity, liabilities):
    base = _f17_etl(equity, liabilities)
    b = _slope(base, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash/liabilities over a year
def f17bs_f17_balance_sheet_strength_ctl_252d_slope_v128_signal(cashneq, liabilities):
    base = _safe_div(cashneq, liabilities)
    b = _slope(base, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debtcap over a year
def f17bs_f17_balance_sheet_strength_debtcap_252d_slope_v129_signal(debt, equity):
    base = _f17_debtcap(debt, equity)
    b = _slope(base, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of working-capital/assets over two years
def f17bs_f17_balance_sheet_strength_wcta_504d_slope_v130_signal(workingcapital, assets):
    base = _f17_wcta(workingcapital, assets)
    b = _slope(base, 504)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash/debt over two years
def f17bs_f17_balance_sheet_strength_ctd_504d_slope_v131_signal(cashneq, debt):
    base = _f17_ctd(cashneq, debt)
    b = _slope(base, 504)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of current ratio over two years
def f17bs_f17_balance_sheet_strength_curr_504d_slope_v132_signal(currentratio):
    b = _slope(currentratio, 504)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of liabilities/equity over a year
def f17bs_f17_balance_sheet_strength_lte_252d_slope_v133_signal(liabilities, equity):
    base = _safe_div(liabilities, equity)
    b = _slope(base, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity/debt standardized by 252d vol, over half a year
def f17bs_f17_balance_sheet_strength_etd_252d_slope_v134_signal(equity, debt):
    base = _safe_div(equity, debt)
    sd = _std(base, 252)
    b = _slope(base, 126) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net-cash/assets over a year
def f17bs_f17_balance_sheet_strength_netcashta_252d_slope_v135_signal(cashneq, debt, assets):
    base = _safe_div(cashneq - debt, assets)
    b = _slope(base, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of leverage-per-liquidity (dta/curr) standardized by 252d vol, over a quarter
def f17bs_f17_balance_sheet_strength_levperliq_63d_slope_v136_signal(debt, assets, currentratio):
    base = _safe_div(_f17_dta(debt, assets), currentratio)
    sd = _std(base, 252)
    b = _slope(base, 63) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of USD debt / assets over half a year
def f17bs_f17_balance_sheet_strength_dusdta_126d_slope_v137_signal(debtusd, assets):
    base = _safe_div(debtusd, assets)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of EMA-smoothed debt/equity over a year (smoothed long leverage trend)
def f17bs_f17_balance_sheet_strength_gdte_252d_slope_v138_signal(debt, equity):
    base = _safe_div(debt, equity).ewm(span=84, min_periods=42).mean()
    b = _slope(base, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of EMA-smoothed liabilities/assets over a quarter
def f17bs_f17_balance_sheet_strength_ltaema_63d_slope_v139_signal(liabilities, assets):
    base = _f17_lta(liabilities, assets).ewm(span=42, min_periods=21).mean()
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of EMA-smoothed cash/debt over a quarter
def f17bs_f17_balance_sheet_strength_ctdema_63d_slope_v140_signal(cashneq, debt):
    base = _f17_ctd(cashneq, debt).ewm(span=42, min_periods=21).mean()
    b = _slope(base, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net debt / assets over two years
def f17bs_f17_balance_sheet_strength_ndta_504d_slope_v141_signal(debt, cashneq, assets):
    base = _safe_div(debt - cashneq, assets)
    b = _slope(base, 504)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of equity/assets minus liabilities/assets over a year
def f17bs_f17_balance_sheet_strength_etanetlta_252d_slope_v142_signal(equity, liabilities, assets):
    base = _f17_eta(equity, assets) - _f17_lta(liabilities, assets)
    b = _slope(base, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash + wc liquidity buffer standardized by 252d vol, over a year
def f17bs_f17_balance_sheet_strength_liqta_126d_slope_v143_signal(cashneq, workingcapital, assets):
    base = _f17_cta(cashneq, assets) + _f17_wcta(workingcapital, assets)
    sd = _std(base, 252)
    b = _slope(base, 252) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of cash/debt coverage quality x curr standardized by 252d vol, over half a year
def f17bs_f17_balance_sheet_strength_covqual_126d_slope_v144_signal(cashneq, debt, currentratio):
    base = _f17_ctd(cashneq, debt) * currentratio
    sd = _std(base, 252)
    b = _slope(base, 126) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of debt / (cash + equity) over a month
def f17bs_f17_balance_sheet_strength_dtoce_21d_slope_v145_signal(debt, cashneq, equity):
    base = _safe_div(debt, cashneq + equity)
    b = _slope(base, 21)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of log(equity/liabilities) over half a year
def f17bs_f17_balance_sheet_strength_logetl_126d_slope_v146_signal(equity, liabilities):
    base = np.log(_f17_etl(equity, liabilities))
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of strength score standardized by 252d vol, over a year
def f17bs_f17_balance_sheet_strength_strscore_126d_slope_v147_signal(equity, assets, debt, cashneq):
    base = _f17_eta(equity, assets) - _f17_dta(debt, assets) + 0.25 * _f17_cta(cashneq, assets)
    sd = _std(base, 252)
    b = _slope(base, 252) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of distress cushion over half a year
def f17bs_f17_balance_sheet_strength_distress_126d_slope_v148_signal(workingcapital, assets, equity, liabilities, debt):
    base = (1.2 * _f17_wcta(workingcapital, assets)
            + 0.6 * _f17_etl(equity, liabilities)
            - _f17_dta(debt, assets))
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of net-cash balance standardized by 252d vol, over a month
def f17bs_f17_balance_sheet_strength_netcashbal_21d_slope_v149_signal(cashneq, debt):
    base = _safe_div(cashneq - debt, cashneq + debt)
    sd = _std(base, 252)
    b = _slope(base, 21) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# slope of liquidity-vs-leverage gap over half a year
def f17bs_f17_balance_sheet_strength_liqlevgap_126d_slope_v150_signal(currentratio, debt, assets):
    base = _z(currentratio, 252) - _z(_f17_dta(debt, assets), 252)
    b = _slope(base, 126)
    return b.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17bs_f17_balance_sheet_strength_ndte_63d_slope_v001_signal,
    f17bs_f17_balance_sheet_strength_ndte_126d_slope_v002_signal,
    f17bs_f17_balance_sheet_strength_gdte_63d_slope_v003_signal,
    f17bs_f17_balance_sheet_strength_dta_63d_slope_v004_signal,
    f17bs_f17_balance_sheet_strength_dta_126d_slope_v005_signal,
    f17bs_f17_balance_sheet_strength_eta_63d_slope_v006_signal,
    f17bs_f17_balance_sheet_strength_eta_126d_slope_v007_signal,
    f17bs_f17_balance_sheet_strength_lta_63d_slope_v008_signal,
    f17bs_f17_balance_sheet_strength_cta_21d_slope_v009_signal,
    f17bs_f17_balance_sheet_strength_cta_63d_slope_v010_signal,
    f17bs_f17_balance_sheet_strength_wcta_63d_slope_v011_signal,
    f17bs_f17_balance_sheet_strength_wcta_21d_slope_v012_signal,
    f17bs_f17_balance_sheet_strength_curr_21d_slope_v013_signal,
    f17bs_f17_balance_sheet_strength_curr_63d_slope_v014_signal,
    f17bs_f17_balance_sheet_strength_ctd_63d_slope_v015_signal,
    f17bs_f17_balance_sheet_strength_etl_63d_slope_v016_signal,
    f17bs_f17_balance_sheet_strength_etd_63d_slope_v017_signal,
    f17bs_f17_balance_sheet_strength_netcashta_63d_slope_v018_signal,
    f17bs_f17_balance_sheet_strength_debtcap_63d_slope_v019_signal,
    f17bs_f17_balance_sheet_strength_ate_63d_slope_v020_signal,
    f17bs_f17_balance_sheet_strength_ndta_126d_slope_v021_signal,
    f17bs_f17_balance_sheet_strength_ctl_63d_slope_v022_signal,
    f17bs_f17_balance_sheet_strength_wctl_63d_slope_v023_signal,
    f17bs_f17_balance_sheet_strength_dtl_63d_slope_v024_signal,
    f17bs_f17_balance_sheet_strength_dusdta_63d_slope_v025_signal,
    f17bs_f17_balance_sheet_strength_ndusde_63d_slope_v026_signal,
    f17bs_f17_balance_sheet_strength_wcqual_63d_slope_v027_signal,
    f17bs_f17_balance_sheet_strength_cte_63d_slope_v028_signal,
    f17bs_f17_balance_sheet_strength_wcte_63d_slope_v029_signal,
    f17bs_f17_balance_sheet_strength_lte_63d_slope_v030_signal,
    f17bs_f17_balance_sheet_strength_ndtez_21d_slope_v031_signal,
    f17bs_f17_balance_sheet_strength_etaz_21d_slope_v032_signal,
    f17bs_f17_balance_sheet_strength_dtaz_21d_slope_v033_signal,
    f17bs_f17_balance_sheet_strength_currz_21d_slope_v034_signal,
    f17bs_f17_balance_sheet_strength_cashqual_63d_slope_v035_signal,
    f17bs_f17_balance_sheet_strength_capliq_63d_slope_v036_signal,
    f17bs_f17_balance_sheet_strength_netcashbal_63d_slope_v037_signal,
    f17bs_f17_balance_sheet_strength_strscore_63d_slope_v038_signal,
    f17bs_f17_balance_sheet_strength_distress_63d_slope_v039_signal,
    f17bs_f17_balance_sheet_strength_etanetlta_63d_slope_v040_signal,
    f17bs_f17_balance_sheet_strength_ndte_21d_slope_v041_signal,
    f17bs_f17_balance_sheet_strength_dta_21d_slope_v042_signal,
    f17bs_f17_balance_sheet_strength_eta_21d_slope_v043_signal,
    f17bs_f17_balance_sheet_strength_ctd_21d_slope_v044_signal,
    f17bs_f17_balance_sheet_strength_etl_21d_slope_v045_signal,
    f17bs_f17_balance_sheet_strength_wcta_126d_slope_v046_signal,
    f17bs_f17_balance_sheet_strength_cta_126d_slope_v047_signal,
    f17bs_f17_balance_sheet_strength_lta_126d_slope_v048_signal,
    f17bs_f17_balance_sheet_strength_curr_126d_slope_v049_signal,
    f17bs_f17_balance_sheet_strength_debtcap_126d_slope_v050_signal,
    f17bs_f17_balance_sheet_strength_ctd_126d_slope_v051_signal,
    f17bs_f17_balance_sheet_strength_etd_126d_slope_v052_signal,
    f17bs_f17_balance_sheet_strength_netcashte_63d_slope_v053_signal,
    f17bs_f17_balance_sheet_strength_liqtod_63d_slope_v054_signal,
    f17bs_f17_balance_sheet_strength_dtoce_63d_slope_v055_signal,
    f17bs_f17_balance_sheet_strength_logetl_63d_slope_v056_signal,
    f17bs_f17_balance_sheet_strength_logatl_63d_slope_v057_signal,
    f17bs_f17_balance_sheet_strength_ctl_126d_slope_v058_signal,
    f17bs_f17_balance_sheet_strength_dusde_63d_slope_v059_signal,
    f17bs_f17_balance_sheet_strength_gdtez_63d_slope_v060_signal,
    f17bs_f17_balance_sheet_strength_ltaz_63d_slope_v061_signal,
    f17bs_f17_balance_sheet_strength_ctaz_63d_slope_v062_signal,
    f17bs_f17_balance_sheet_strength_wctaz_63d_slope_v063_signal,
    f17bs_f17_balance_sheet_strength_etaema_63d_slope_v064_signal,
    f17bs_f17_balance_sheet_strength_dtaema_63d_slope_v065_signal,
    f17bs_f17_balance_sheet_strength_currema_63d_slope_v066_signal,
    f17bs_f17_balance_sheet_strength_ndte_252d_slope_v067_signal,
    f17bs_f17_balance_sheet_strength_eta_252d_slope_v068_signal,
    f17bs_f17_balance_sheet_strength_dta_252d_slope_v069_signal,
    f17bs_f17_balance_sheet_strength_ctd_252d_slope_v070_signal,
    f17bs_f17_balance_sheet_strength_curr_252d_slope_v071_signal,
    f17bs_f17_balance_sheet_strength_ate_126d_slope_v072_signal,
    f17bs_f17_balance_sheet_strength_lte_126d_slope_v073_signal,
    f17bs_f17_balance_sheet_strength_ndta_21d_slope_v074_signal,
    f17bs_f17_balance_sheet_strength_liqta_63d_slope_v075_signal,
    f17bs_f17_balance_sheet_strength_etdz_63d_slope_v076_signal,
    f17bs_f17_balance_sheet_strength_netcashtaz_63d_slope_v077_signal,
    f17bs_f17_balance_sheet_strength_dtl_126d_slope_v078_signal,
    f17bs_f17_balance_sheet_strength_wctd_63d_slope_v079_signal,
    f17bs_f17_balance_sheet_strength_usdmix_63d_slope_v080_signal,
    f17bs_f17_balance_sheet_strength_solvmargin_63d_slope_v081_signal,
    f17bs_f17_balance_sheet_strength_cleanbs_63d_slope_v082_signal,
    f17bs_f17_balance_sheet_strength_shortlong_63d_slope_v083_signal,
    f17bs_f17_balance_sheet_strength_covqual_63d_slope_v084_signal,
    f17bs_f17_balance_sheet_strength_ndte_504d_slope_v085_signal,
    f17bs_f17_balance_sheet_strength_eta_504d_slope_v086_signal,
    f17bs_f17_balance_sheet_strength_dta_504d_slope_v087_signal,
    f17bs_f17_balance_sheet_strength_cta_504d_slope_v088_signal,
    f17bs_f17_balance_sheet_strength_lta_504d_slope_v089_signal,
    f17bs_f17_balance_sheet_strength_wcta_252d_slope_v090_signal,
    f17bs_f17_balance_sheet_strength_cte_126d_slope_v091_signal,
    f17bs_f17_balance_sheet_strength_wcte_126d_slope_v092_signal,
    f17bs_f17_balance_sheet_strength_debtcap_21d_slope_v093_signal,
    f17bs_f17_balance_sheet_strength_etl_126d_slope_v094_signal,
    f17bs_f17_balance_sheet_strength_netcashbal_126d_slope_v095_signal,
    f17bs_f17_balance_sheet_strength_netusdta_63d_slope_v096_signal,
    f17bs_f17_balance_sheet_strength_solvmargin_126d_slope_v097_signal,
    f17bs_f17_balance_sheet_strength_liqlevgap_63d_slope_v098_signal,
    f17bs_f17_balance_sheet_strength_runway_126d_slope_v099_signal,
    f17bs_f17_balance_sheet_strength_ndtetanh_63d_slope_v100_signal,
    f17bs_f17_balance_sheet_strength_logndte_63d_slope_v101_signal,
    f17bs_f17_balance_sheet_strength_etd_21d_slope_v102_signal,
    f17bs_f17_balance_sheet_strength_ctl_21d_slope_v103_signal,
    f17bs_f17_balance_sheet_strength_wctl_21d_slope_v104_signal,
    f17bs_f17_balance_sheet_strength_dtl_21d_slope_v105_signal,
    f17bs_f17_balance_sheet_strength_lta_21d_slope_v106_signal,
    f17bs_f17_balance_sheet_strength_netcashbal2_63d_slope_v107_signal,
    f17bs_f17_balance_sheet_strength_liqcovl_63d_slope_v108_signal,
    f17bs_f17_balance_sheet_strength_dtoce_126d_slope_v109_signal,
    f17bs_f17_balance_sheet_strength_blendz_63d_slope_v110_signal,
    f17bs_f17_balance_sheet_strength_dusdtl_63d_slope_v111_signal,
    f17bs_f17_balance_sheet_strength_ndusde_126d_slope_v112_signal,
    f17bs_f17_balance_sheet_strength_netliq_63d_slope_v113_signal,
    f17bs_f17_balance_sheet_strength_liqdual_63d_slope_v114_signal,
    f17bs_f17_balance_sheet_strength_capcov_63d_slope_v115_signal,
    f17bs_f17_balance_sheet_strength_ndtl_63d_slope_v116_signal,
    f17bs_f17_balance_sheet_strength_cte_21d_slope_v117_signal,
    f17bs_f17_balance_sheet_strength_wcte_21d_slope_v118_signal,
    f17bs_f17_balance_sheet_strength_ate_21d_slope_v119_signal,
    f17bs_f17_balance_sheet_strength_lte_21d_slope_v120_signal,
    f17bs_f17_balance_sheet_strength_solvliq_63d_slope_v121_signal,
    f17bs_f17_balance_sheet_strength_cashqualdiv_63d_slope_v122_signal,
    f17bs_f17_balance_sheet_strength_jointcov_63d_slope_v123_signal,
    f17bs_f17_balance_sheet_strength_fragility_63d_slope_v124_signal,
    f17bs_f17_balance_sheet_strength_buftilt_63d_slope_v125_signal,
    f17bs_f17_balance_sheet_strength_levcovgap_126d_slope_v126_signal,
    f17bs_f17_balance_sheet_strength_etl_252d_slope_v127_signal,
    f17bs_f17_balance_sheet_strength_ctl_252d_slope_v128_signal,
    f17bs_f17_balance_sheet_strength_debtcap_252d_slope_v129_signal,
    f17bs_f17_balance_sheet_strength_wcta_504d_slope_v130_signal,
    f17bs_f17_balance_sheet_strength_ctd_504d_slope_v131_signal,
    f17bs_f17_balance_sheet_strength_curr_504d_slope_v132_signal,
    f17bs_f17_balance_sheet_strength_lte_252d_slope_v133_signal,
    f17bs_f17_balance_sheet_strength_etd_252d_slope_v134_signal,
    f17bs_f17_balance_sheet_strength_netcashta_252d_slope_v135_signal,
    f17bs_f17_balance_sheet_strength_levperliq_63d_slope_v136_signal,
    f17bs_f17_balance_sheet_strength_dusdta_126d_slope_v137_signal,
    f17bs_f17_balance_sheet_strength_gdte_252d_slope_v138_signal,
    f17bs_f17_balance_sheet_strength_ltaema_63d_slope_v139_signal,
    f17bs_f17_balance_sheet_strength_ctdema_63d_slope_v140_signal,
    f17bs_f17_balance_sheet_strength_ndta_504d_slope_v141_signal,
    f17bs_f17_balance_sheet_strength_etanetlta_252d_slope_v142_signal,
    f17bs_f17_balance_sheet_strength_liqta_126d_slope_v143_signal,
    f17bs_f17_balance_sheet_strength_covqual_126d_slope_v144_signal,
    f17bs_f17_balance_sheet_strength_dtoce_21d_slope_v145_signal,
    f17bs_f17_balance_sheet_strength_logetl_126d_slope_v146_signal,
    f17bs_f17_balance_sheet_strength_strscore_126d_slope_v147_signal,
    f17bs_f17_balance_sheet_strength_distress_126d_slope_v148_signal,
    f17bs_f17_balance_sheet_strength_netcashbal_21d_slope_v149_signal,
    f17bs_f17_balance_sheet_strength_liqlevgap_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_BALANCE_SHEET_STRENGTH_REGISTRY_SLOPE_001_150 = REGISTRY


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

    assert n_features == 150, n_features
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

    print("OK f17_balance_sheet_strength_2nd_derivatives_001_150_claude: %d features pass" % n_features)
