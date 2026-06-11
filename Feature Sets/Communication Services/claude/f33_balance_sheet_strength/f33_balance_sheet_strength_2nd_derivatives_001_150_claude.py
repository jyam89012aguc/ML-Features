import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope(s, w):
    # rolling OLS slope vs time index (1st discrete derivative, per-day)
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx * idx).sum()

    def _f(a):
        return float((idx * (a - a.mean())).sum() / denom)

    return s.rolling(w, min_periods=w).apply(_f, raw=True)


def _accel(s, w):
    # rolling 2nd derivative: slope-of-slope (jerk of the level series)
    sl = _slope(s, w)
    return _slope(sl, w)


# ----- normalized derivative variants (decouple ratios sharing a common trend) -----
def _slope_z(s, w):
    # slope of the z-scored series (unit-variance-normalized 1st derivative)
    return _slope(_z(s, w), w)


def _accel_z(s, w):
    return _accel(_z(s, w), w)


def _slope_pct(s, w):
    # slope normalized by the local level magnitude (percentage 1st derivative)
    sl = _slope(s, w)
    lvl = _mean(s, w).abs()
    return sl / lvl.replace(0, np.nan)


def _accel_pct(s, w):
    ac = _accel(s, w)
    lvl = _mean(s, w).abs()
    return ac / lvl.replace(0, np.nan)


def _slope_log(s, w):
    # slope of the sign-preserving log-magnitude (multiplicative 1st derivative)
    t = np.sign(s) * np.log1p(s.abs())
    return _slope(t, w)


def _accel_log(s, w):
    t = np.sign(s) * np.log1p(s.abs())
    return _accel(t, w)


def _slope_sn(s, w):
    # signal-to-noise slope: slope divided by local dispersion
    sl = _slope(s, w)
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return sl / sd.replace(0, np.nan)


def _accel_sn(s, w):
    ac = _accel(s, w)
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return ac / sd.replace(0, np.nan)


# ===== balance-sheet ratio primitives =====
def _f33_net_cash(cashneq, debt):
    return cashneq - debt


def _f33_de(debt, equity):
    return debt / equity.replace(0, np.nan)


def _f33_da(debt, assets):
    return debt / assets.replace(0, np.nan)


def _f33_ea(equity, assets):
    return equity / assets.replace(0, np.nan)


def _f33_wca(workingcapital, assets):
    return workingcapital / assets.replace(0, np.nan)


def _f33_cash_assets(cashneq, assets):
    return cashneq / assets.replace(0, np.nan)


def _f33_liab_assets(liabilities, assets):
    return liabilities / assets.replace(0, np.nan)


# slope z-normalized 1st-derivative (window 10d) of net cash / assets
def f33bs_f33_balance_sheet_strength_netcashassets_10d_slope_v001_signal(cashneq, debt, assets):
    ratio = (_f33_net_cash(cashneq, debt) / assets.replace(0, np.nan))
    b = _slope_z(ratio, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 10d) of debt / equity
def f33bs_f33_balance_sheet_strength_de_10d_slope_v002_signal(debt, equity):
    ratio = _f33_de(debt, equity)
    b = _slope_z(ratio, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 10d) of debt / assets
def f33bs_f33_balance_sheet_strength_da_10d_slope_v003_signal(debt, assets):
    ratio = _f33_da(debt, assets)
    b = _slope_z(ratio, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 10d) of equity / assets
def f33bs_f33_balance_sheet_strength_ea_10d_slope_v004_signal(equity, assets):
    ratio = _f33_ea(equity, assets)
    b = _slope_z(ratio, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 10d) of working capital / assets
def f33bs_f33_balance_sheet_strength_wca_10d_slope_v005_signal(workingcapital, assets):
    ratio = _f33_wca(workingcapital, assets)
    b = _slope_z(ratio, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 10d) of current ratio
def f33bs_f33_balance_sheet_strength_curr_10d_slope_v006_signal(currentratio):
    ratio = currentratio
    b = _slope_z(ratio, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 10d) of liabilities / assets
def f33bs_f33_balance_sheet_strength_liabassets_10d_slope_v007_signal(liabilities, assets):
    ratio = _f33_liab_assets(liabilities, assets)
    b = _slope_z(ratio, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 10d) of cash / assets
def f33bs_f33_balance_sheet_strength_cashassets_10d_slope_v008_signal(cashneq, assets):
    ratio = _f33_cash_assets(cashneq, assets)
    b = _slope_z(ratio, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 10d) of cash / liabilities
def f33bs_f33_balance_sheet_strength_cashliab_10d_slope_v009_signal(cashneq, liabilities):
    ratio = (cashneq / liabilities.replace(0, np.nan))
    b = _slope_z(ratio, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 10d) of equity / liabilities
def f33bs_f33_balance_sheet_strength_eqliab_10d_slope_v010_signal(equity, liabilities):
    ratio = (equity / liabilities.replace(0, np.nan))
    b = _slope_z(ratio, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 10d) of debt / working capital
def f33bs_f33_balance_sheet_strength_debtwc_10d_slope_v011_signal(debt, workingcapital):
    ratio = (debt / workingcapital.replace(0, np.nan))
    b = _slope_z(ratio, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 10d) of equity/assets * current ratio
def f33bs_f33_balance_sheet_strength_capliq_10d_slope_v012_signal(equity, assets, currentratio):
    ratio = (_f33_ea(equity, assets) * currentratio)
    b = _slope_z(ratio, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 10d) of cash/assets * current ratio
def f33bs_f33_balance_sheet_strength_cashbacked_10d_slope_v013_signal(cashneq, assets, currentratio):
    ratio = (_f33_cash_assets(cashneq, assets) * currentratio)
    b = _slope_z(ratio, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 10d) of equity / cash
def f33bs_f33_balance_sheet_strength_eqcash_10d_slope_v014_signal(equity, cashneq):
    ratio = (equity / cashneq.replace(0, np.nan))
    b = _slope_z(ratio, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 10d) of (cash+wc)/assets
def f33bs_f33_balance_sheet_strength_liqbufassets_10d_slope_v015_signal(cashneq, workingcapital, assets):
    ratio = ((cashneq + workingcapital) / assets.replace(0, np.nan))
    b = _slope_z(ratio, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 25d) of net cash / assets
def f33bs_f33_balance_sheet_strength_netcashassets_25d_slope_v016_signal(cashneq, debt, assets):
    ratio = (_f33_net_cash(cashneq, debt) / assets.replace(0, np.nan))
    b = _slope_sn(ratio, 25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 25d) of debt / equity
def f33bs_f33_balance_sheet_strength_de_25d_slope_v017_signal(debt, equity):
    ratio = _f33_de(debt, equity)
    b = _slope_sn(ratio, 25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 25d) of debt / assets
def f33bs_f33_balance_sheet_strength_da_25d_slope_v018_signal(debt, assets):
    ratio = _f33_da(debt, assets)
    b = _slope_sn(ratio, 25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 25d) of equity / assets
def f33bs_f33_balance_sheet_strength_ea_25d_slope_v019_signal(equity, assets):
    ratio = _f33_ea(equity, assets)
    b = _slope_sn(ratio, 25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 25d) of working capital / assets
def f33bs_f33_balance_sheet_strength_wca_25d_slope_v020_signal(workingcapital, assets):
    ratio = _f33_wca(workingcapital, assets)
    b = _slope_sn(ratio, 25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 25d) of current ratio
def f33bs_f33_balance_sheet_strength_curr_25d_slope_v021_signal(currentratio):
    ratio = currentratio
    b = _slope_sn(ratio, 25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 25d) of liabilities / assets
def f33bs_f33_balance_sheet_strength_liabassets_25d_slope_v022_signal(liabilities, assets):
    ratio = _f33_liab_assets(liabilities, assets)
    b = _slope_sn(ratio, 25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 25d) of cash / assets
def f33bs_f33_balance_sheet_strength_cashassets_25d_slope_v023_signal(cashneq, assets):
    ratio = _f33_cash_assets(cashneq, assets)
    b = _slope_sn(ratio, 25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 25d) of cash / liabilities
def f33bs_f33_balance_sheet_strength_cashliab_25d_slope_v024_signal(cashneq, liabilities):
    ratio = (cashneq / liabilities.replace(0, np.nan))
    b = _slope_sn(ratio, 25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 25d) of equity / liabilities
def f33bs_f33_balance_sheet_strength_eqliab_25d_slope_v025_signal(equity, liabilities):
    ratio = (equity / liabilities.replace(0, np.nan))
    b = _slope_sn(ratio, 25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 25d) of debt / working capital
def f33bs_f33_balance_sheet_strength_debtwc_25d_slope_v026_signal(debt, workingcapital):
    ratio = (debt / workingcapital.replace(0, np.nan))
    b = _slope_sn(ratio, 25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 25d) of equity/assets * current ratio
def f33bs_f33_balance_sheet_strength_capliq_25d_slope_v027_signal(equity, assets, currentratio):
    ratio = (_f33_ea(equity, assets) * currentratio)
    b = _slope_sn(ratio, 25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 25d) of cash/assets * current ratio
def f33bs_f33_balance_sheet_strength_cashbacked_25d_slope_v028_signal(cashneq, assets, currentratio):
    ratio = (_f33_cash_assets(cashneq, assets) * currentratio)
    b = _slope_sn(ratio, 25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 25d) of equity / cash
def f33bs_f33_balance_sheet_strength_eqcash_25d_slope_v029_signal(equity, cashneq):
    ratio = (equity / cashneq.replace(0, np.nan))
    b = _slope_sn(ratio, 25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 25d) of (cash+wc)/assets
def f33bs_f33_balance_sheet_strength_liqbufassets_25d_slope_v030_signal(cashneq, workingcapital, assets):
    ratio = ((cashneq + workingcapital) / assets.replace(0, np.nan))
    b = _slope_sn(ratio, 25)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 42d) of net cash / assets
def f33bs_f33_balance_sheet_strength_netcashassets_42d_slope_v031_signal(cashneq, debt, assets):
    ratio = (_f33_net_cash(cashneq, debt) / assets.replace(0, np.nan))
    b = _slope_log(ratio, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 42d) of debt / equity
def f33bs_f33_balance_sheet_strength_de_42d_slope_v032_signal(debt, equity):
    ratio = _f33_de(debt, equity)
    b = _slope_log(ratio, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 42d) of debt / assets
def f33bs_f33_balance_sheet_strength_da_42d_slope_v033_signal(debt, assets):
    ratio = _f33_da(debt, assets)
    b = _slope_log(ratio, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 42d) of equity / assets
def f33bs_f33_balance_sheet_strength_ea_42d_slope_v034_signal(equity, assets):
    ratio = _f33_ea(equity, assets)
    b = _slope_log(ratio, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 42d) of working capital / assets
def f33bs_f33_balance_sheet_strength_wca_42d_slope_v035_signal(workingcapital, assets):
    ratio = _f33_wca(workingcapital, assets)
    b = _slope_log(ratio, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 42d) of current ratio
def f33bs_f33_balance_sheet_strength_curr_42d_slope_v036_signal(currentratio):
    ratio = currentratio
    b = _slope_log(ratio, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 42d) of liabilities / assets
def f33bs_f33_balance_sheet_strength_liabassets_42d_slope_v037_signal(liabilities, assets):
    ratio = _f33_liab_assets(liabilities, assets)
    b = _slope_log(ratio, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 42d) of cash / assets
def f33bs_f33_balance_sheet_strength_cashassets_42d_slope_v038_signal(cashneq, assets):
    ratio = _f33_cash_assets(cashneq, assets)
    b = _slope_log(ratio, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 42d) of cash / liabilities
def f33bs_f33_balance_sheet_strength_cashliab_42d_slope_v039_signal(cashneq, liabilities):
    ratio = (cashneq / liabilities.replace(0, np.nan))
    b = _slope_log(ratio, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 42d) of equity / liabilities
def f33bs_f33_balance_sheet_strength_eqliab_42d_slope_v040_signal(equity, liabilities):
    ratio = (equity / liabilities.replace(0, np.nan))
    b = _slope_log(ratio, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 42d) of debt / working capital
def f33bs_f33_balance_sheet_strength_debtwc_42d_slope_v041_signal(debt, workingcapital):
    ratio = (debt / workingcapital.replace(0, np.nan))
    b = _slope_log(ratio, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 42d) of equity/assets * current ratio
def f33bs_f33_balance_sheet_strength_capliq_42d_slope_v042_signal(equity, assets, currentratio):
    ratio = (_f33_ea(equity, assets) * currentratio)
    b = _slope_log(ratio, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 42d) of cash/assets * current ratio
def f33bs_f33_balance_sheet_strength_cashbacked_42d_slope_v043_signal(cashneq, assets, currentratio):
    ratio = (_f33_cash_assets(cashneq, assets) * currentratio)
    b = _slope_log(ratio, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 42d) of equity / cash
def f33bs_f33_balance_sheet_strength_eqcash_42d_slope_v044_signal(equity, cashneq):
    ratio = (equity / cashneq.replace(0, np.nan))
    b = _slope_log(ratio, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 42d) of (cash+wc)/assets
def f33bs_f33_balance_sheet_strength_liqbufassets_42d_slope_v045_signal(cashneq, workingcapital, assets):
    ratio = ((cashneq + workingcapital) / assets.replace(0, np.nan))
    b = _slope_log(ratio, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 63d) of net cash / assets
def f33bs_f33_balance_sheet_strength_netcashassets_63d_slope_v046_signal(cashneq, debt, assets):
    ratio = (_f33_net_cash(cashneq, debt) / assets.replace(0, np.nan))
    b = _slope_pct(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 63d) of debt / equity
def f33bs_f33_balance_sheet_strength_de_63d_slope_v047_signal(debt, equity):
    ratio = _f33_de(debt, equity)
    b = _slope_pct(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 63d) of debt / assets
def f33bs_f33_balance_sheet_strength_da_63d_slope_v048_signal(debt, assets):
    ratio = _f33_da(debt, assets)
    b = _slope_pct(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 63d) of equity / assets
def f33bs_f33_balance_sheet_strength_ea_63d_slope_v049_signal(equity, assets):
    ratio = _f33_ea(equity, assets)
    b = _slope_pct(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 63d) of working capital / assets
def f33bs_f33_balance_sheet_strength_wca_63d_slope_v050_signal(workingcapital, assets):
    ratio = _f33_wca(workingcapital, assets)
    b = _slope_pct(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 63d) of current ratio
def f33bs_f33_balance_sheet_strength_curr_63d_slope_v051_signal(currentratio):
    ratio = currentratio
    b = _slope_pct(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 63d) of liabilities / assets
def f33bs_f33_balance_sheet_strength_liabassets_63d_slope_v052_signal(liabilities, assets):
    ratio = _f33_liab_assets(liabilities, assets)
    b = _slope_pct(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 63d) of cash / assets
def f33bs_f33_balance_sheet_strength_cashassets_63d_slope_v053_signal(cashneq, assets):
    ratio = _f33_cash_assets(cashneq, assets)
    b = _slope_pct(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 63d) of cash / liabilities
def f33bs_f33_balance_sheet_strength_cashliab_63d_slope_v054_signal(cashneq, liabilities):
    ratio = (cashneq / liabilities.replace(0, np.nan))
    b = _slope_pct(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 63d) of equity / liabilities
def f33bs_f33_balance_sheet_strength_eqliab_63d_slope_v055_signal(equity, liabilities):
    ratio = (equity / liabilities.replace(0, np.nan))
    b = _slope_pct(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 63d) of debt / working capital
def f33bs_f33_balance_sheet_strength_debtwc_63d_slope_v056_signal(debt, workingcapital):
    ratio = (debt / workingcapital.replace(0, np.nan))
    b = _slope_pct(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 63d) of equity/assets * current ratio
def f33bs_f33_balance_sheet_strength_capliq_63d_slope_v057_signal(equity, assets, currentratio):
    ratio = (_f33_ea(equity, assets) * currentratio)
    b = _slope_pct(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 63d) of cash/assets * current ratio
def f33bs_f33_balance_sheet_strength_cashbacked_63d_slope_v058_signal(cashneq, assets, currentratio):
    ratio = (_f33_cash_assets(cashneq, assets) * currentratio)
    b = _slope_pct(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 63d) of equity / cash
def f33bs_f33_balance_sheet_strength_eqcash_63d_slope_v059_signal(equity, cashneq):
    ratio = (equity / cashneq.replace(0, np.nan))
    b = _slope_pct(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 63d) of (cash+wc)/assets
def f33bs_f33_balance_sheet_strength_liqbufassets_63d_slope_v060_signal(cashneq, workingcapital, assets):
    ratio = ((cashneq + workingcapital) / assets.replace(0, np.nan))
    b = _slope_pct(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 84d) of net cash / assets
def f33bs_f33_balance_sheet_strength_netcashassets_84d_slope_v061_signal(cashneq, debt, assets):
    ratio = (_f33_net_cash(cashneq, debt) / assets.replace(0, np.nan))
    b = _slope(ratio, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 84d) of debt / equity
def f33bs_f33_balance_sheet_strength_de_84d_slope_v062_signal(debt, equity):
    ratio = _f33_de(debt, equity)
    b = _slope(ratio, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 84d) of debt / assets
def f33bs_f33_balance_sheet_strength_da_84d_slope_v063_signal(debt, assets):
    ratio = _f33_da(debt, assets)
    b = _slope(ratio, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 84d) of equity / assets
def f33bs_f33_balance_sheet_strength_ea_84d_slope_v064_signal(equity, assets):
    ratio = _f33_ea(equity, assets)
    b = _slope(ratio, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 84d) of working capital / assets
def f33bs_f33_balance_sheet_strength_wca_84d_slope_v065_signal(workingcapital, assets):
    ratio = _f33_wca(workingcapital, assets)
    b = _slope(ratio, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 84d) of current ratio
def f33bs_f33_balance_sheet_strength_curr_84d_slope_v066_signal(currentratio):
    ratio = currentratio
    b = _slope(ratio, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 84d) of liabilities / assets
def f33bs_f33_balance_sheet_strength_liabassets_84d_slope_v067_signal(liabilities, assets):
    ratio = _f33_liab_assets(liabilities, assets)
    b = _slope(ratio, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 84d) of cash / assets
def f33bs_f33_balance_sheet_strength_cashassets_84d_slope_v068_signal(cashneq, assets):
    ratio = _f33_cash_assets(cashneq, assets)
    b = _slope(ratio, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 84d) of cash / liabilities
def f33bs_f33_balance_sheet_strength_cashliab_84d_slope_v069_signal(cashneq, liabilities):
    ratio = (cashneq / liabilities.replace(0, np.nan))
    b = _slope(ratio, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 84d) of equity / liabilities
def f33bs_f33_balance_sheet_strength_eqliab_84d_slope_v070_signal(equity, liabilities):
    ratio = (equity / liabilities.replace(0, np.nan))
    b = _slope(ratio, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 84d) of debt / working capital
def f33bs_f33_balance_sheet_strength_debtwc_84d_slope_v071_signal(debt, workingcapital):
    ratio = (debt / workingcapital.replace(0, np.nan))
    b = _slope(ratio, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 84d) of equity/assets * current ratio
def f33bs_f33_balance_sheet_strength_capliq_84d_slope_v072_signal(equity, assets, currentratio):
    ratio = (_f33_ea(equity, assets) * currentratio)
    b = _slope(ratio, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 84d) of cash/assets * current ratio
def f33bs_f33_balance_sheet_strength_cashbacked_84d_slope_v073_signal(cashneq, assets, currentratio):
    ratio = (_f33_cash_assets(cashneq, assets) * currentratio)
    b = _slope(ratio, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 84d) of equity / cash
def f33bs_f33_balance_sheet_strength_eqcash_84d_slope_v074_signal(equity, cashneq):
    ratio = (equity / cashneq.replace(0, np.nan))
    b = _slope(ratio, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 84d) of (cash+wc)/assets
def f33bs_f33_balance_sheet_strength_liqbufassets_84d_slope_v075_signal(cashneq, workingcapital, assets):
    ratio = ((cashneq + workingcapital) / assets.replace(0, np.nan))
    b = _slope(ratio, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 110d) of net cash / assets
def f33bs_f33_balance_sheet_strength_netcashassets_110d_slope_v076_signal(cashneq, debt, assets):
    ratio = (_f33_net_cash(cashneq, debt) / assets.replace(0, np.nan))
    b = _slope_z(ratio, 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 110d) of debt / equity
def f33bs_f33_balance_sheet_strength_de_110d_slope_v077_signal(debt, equity):
    ratio = _f33_de(debt, equity)
    b = _slope_z(ratio, 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 110d) of debt / assets
def f33bs_f33_balance_sheet_strength_da_110d_slope_v078_signal(debt, assets):
    ratio = _f33_da(debt, assets)
    b = _slope_z(ratio, 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 110d) of equity / assets
def f33bs_f33_balance_sheet_strength_ea_110d_slope_v079_signal(equity, assets):
    ratio = _f33_ea(equity, assets)
    b = _slope_z(ratio, 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 110d) of working capital / assets
def f33bs_f33_balance_sheet_strength_wca_110d_slope_v080_signal(workingcapital, assets):
    ratio = _f33_wca(workingcapital, assets)
    b = _slope_z(ratio, 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 110d) of current ratio
def f33bs_f33_balance_sheet_strength_curr_110d_slope_v081_signal(currentratio):
    ratio = currentratio
    b = _slope_z(ratio, 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 110d) of liabilities / assets
def f33bs_f33_balance_sheet_strength_liabassets_110d_slope_v082_signal(liabilities, assets):
    ratio = _f33_liab_assets(liabilities, assets)
    b = _slope_z(ratio, 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 110d) of cash / assets
def f33bs_f33_balance_sheet_strength_cashassets_110d_slope_v083_signal(cashneq, assets):
    ratio = _f33_cash_assets(cashneq, assets)
    b = _slope_z(ratio, 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 110d) of cash / liabilities
def f33bs_f33_balance_sheet_strength_cashliab_110d_slope_v084_signal(cashneq, liabilities):
    ratio = (cashneq / liabilities.replace(0, np.nan))
    b = _slope_z(ratio, 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 110d) of equity / liabilities
def f33bs_f33_balance_sheet_strength_eqliab_110d_slope_v085_signal(equity, liabilities):
    ratio = (equity / liabilities.replace(0, np.nan))
    b = _slope_z(ratio, 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 110d) of debt / working capital
def f33bs_f33_balance_sheet_strength_debtwc_110d_slope_v086_signal(debt, workingcapital):
    ratio = (debt / workingcapital.replace(0, np.nan))
    b = _slope_z(ratio, 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 110d) of equity/assets * current ratio
def f33bs_f33_balance_sheet_strength_capliq_110d_slope_v087_signal(equity, assets, currentratio):
    ratio = (_f33_ea(equity, assets) * currentratio)
    b = _slope_z(ratio, 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 110d) of cash/assets * current ratio
def f33bs_f33_balance_sheet_strength_cashbacked_110d_slope_v088_signal(cashneq, assets, currentratio):
    ratio = (_f33_cash_assets(cashneq, assets) * currentratio)
    b = _slope_z(ratio, 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 110d) of equity / cash
def f33bs_f33_balance_sheet_strength_eqcash_110d_slope_v089_signal(equity, cashneq):
    ratio = (equity / cashneq.replace(0, np.nan))
    b = _slope_z(ratio, 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope z-normalized 1st-derivative (window 110d) of (cash+wc)/assets
def f33bs_f33_balance_sheet_strength_liqbufassets_110d_slope_v090_signal(cashneq, workingcapital, assets):
    ratio = ((cashneq + workingcapital) / assets.replace(0, np.nan))
    b = _slope_z(ratio, 110)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 130d) of net cash / assets
def f33bs_f33_balance_sheet_strength_netcashassets_130d_slope_v091_signal(cashneq, debt, assets):
    ratio = (_f33_net_cash(cashneq, debt) / assets.replace(0, np.nan))
    b = _slope_pct(ratio, 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 130d) of debt / equity
def f33bs_f33_balance_sheet_strength_de_130d_slope_v092_signal(debt, equity):
    ratio = _f33_de(debt, equity)
    b = _slope_pct(ratio, 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 130d) of debt / assets
def f33bs_f33_balance_sheet_strength_da_130d_slope_v093_signal(debt, assets):
    ratio = _f33_da(debt, assets)
    b = _slope_pct(ratio, 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 130d) of equity / assets
def f33bs_f33_balance_sheet_strength_ea_130d_slope_v094_signal(equity, assets):
    ratio = _f33_ea(equity, assets)
    b = _slope_pct(ratio, 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 130d) of working capital / assets
def f33bs_f33_balance_sheet_strength_wca_130d_slope_v095_signal(workingcapital, assets):
    ratio = _f33_wca(workingcapital, assets)
    b = _slope_pct(ratio, 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 130d) of current ratio
def f33bs_f33_balance_sheet_strength_curr_130d_slope_v096_signal(currentratio):
    ratio = currentratio
    b = _slope_pct(ratio, 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 130d) of liabilities / assets
def f33bs_f33_balance_sheet_strength_liabassets_130d_slope_v097_signal(liabilities, assets):
    ratio = _f33_liab_assets(liabilities, assets)
    b = _slope_pct(ratio, 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 130d) of cash / assets
def f33bs_f33_balance_sheet_strength_cashassets_130d_slope_v098_signal(cashneq, assets):
    ratio = _f33_cash_assets(cashneq, assets)
    b = _slope_pct(ratio, 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 130d) of cash / liabilities
def f33bs_f33_balance_sheet_strength_cashliab_130d_slope_v099_signal(cashneq, liabilities):
    ratio = (cashneq / liabilities.replace(0, np.nan))
    b = _slope_pct(ratio, 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 130d) of equity / liabilities
def f33bs_f33_balance_sheet_strength_eqliab_130d_slope_v100_signal(equity, liabilities):
    ratio = (equity / liabilities.replace(0, np.nan))
    b = _slope_pct(ratio, 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 130d) of debt / working capital
def f33bs_f33_balance_sheet_strength_debtwc_130d_slope_v101_signal(debt, workingcapital):
    ratio = (debt / workingcapital.replace(0, np.nan))
    b = _slope_pct(ratio, 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 130d) of equity/assets * current ratio
def f33bs_f33_balance_sheet_strength_capliq_130d_slope_v102_signal(equity, assets, currentratio):
    ratio = (_f33_ea(equity, assets) * currentratio)
    b = _slope_pct(ratio, 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 130d) of cash/assets * current ratio
def f33bs_f33_balance_sheet_strength_cashbacked_130d_slope_v103_signal(cashneq, assets, currentratio):
    ratio = (_f33_cash_assets(cashneq, assets) * currentratio)
    b = _slope_pct(ratio, 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 130d) of equity / cash
def f33bs_f33_balance_sheet_strength_eqcash_130d_slope_v104_signal(equity, cashneq):
    ratio = (equity / cashneq.replace(0, np.nan))
    b = _slope_pct(ratio, 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope percentage 1st-derivative (window 130d) of (cash+wc)/assets
def f33bs_f33_balance_sheet_strength_liqbufassets_130d_slope_v105_signal(cashneq, workingcapital, assets):
    ratio = ((cashneq + workingcapital) / assets.replace(0, np.nan))
    b = _slope_pct(ratio, 130)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 168d) of net cash / assets
def f33bs_f33_balance_sheet_strength_netcashassets_168d_slope_v106_signal(cashneq, debt, assets):
    ratio = (_f33_net_cash(cashneq, debt) / assets.replace(0, np.nan))
    b = _slope_log(ratio, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 168d) of debt / equity
def f33bs_f33_balance_sheet_strength_de_168d_slope_v107_signal(debt, equity):
    ratio = _f33_de(debt, equity)
    b = _slope_log(ratio, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 168d) of debt / assets
def f33bs_f33_balance_sheet_strength_da_168d_slope_v108_signal(debt, assets):
    ratio = _f33_da(debt, assets)
    b = _slope_log(ratio, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 168d) of equity / assets
def f33bs_f33_balance_sheet_strength_ea_168d_slope_v109_signal(equity, assets):
    ratio = _f33_ea(equity, assets)
    b = _slope_log(ratio, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 168d) of working capital / assets
def f33bs_f33_balance_sheet_strength_wca_168d_slope_v110_signal(workingcapital, assets):
    ratio = _f33_wca(workingcapital, assets)
    b = _slope_log(ratio, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 168d) of current ratio
def f33bs_f33_balance_sheet_strength_curr_168d_slope_v111_signal(currentratio):
    ratio = currentratio
    b = _slope_log(ratio, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 168d) of liabilities / assets
def f33bs_f33_balance_sheet_strength_liabassets_168d_slope_v112_signal(liabilities, assets):
    ratio = _f33_liab_assets(liabilities, assets)
    b = _slope_log(ratio, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 168d) of cash / assets
def f33bs_f33_balance_sheet_strength_cashassets_168d_slope_v113_signal(cashneq, assets):
    ratio = _f33_cash_assets(cashneq, assets)
    b = _slope_log(ratio, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 168d) of cash / liabilities
def f33bs_f33_balance_sheet_strength_cashliab_168d_slope_v114_signal(cashneq, liabilities):
    ratio = (cashneq / liabilities.replace(0, np.nan))
    b = _slope_log(ratio, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 168d) of equity / liabilities
def f33bs_f33_balance_sheet_strength_eqliab_168d_slope_v115_signal(equity, liabilities):
    ratio = (equity / liabilities.replace(0, np.nan))
    b = _slope_log(ratio, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 168d) of debt / working capital
def f33bs_f33_balance_sheet_strength_debtwc_168d_slope_v116_signal(debt, workingcapital):
    ratio = (debt / workingcapital.replace(0, np.nan))
    b = _slope_log(ratio, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 168d) of equity/assets * current ratio
def f33bs_f33_balance_sheet_strength_capliq_168d_slope_v117_signal(equity, assets, currentratio):
    ratio = (_f33_ea(equity, assets) * currentratio)
    b = _slope_log(ratio, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 168d) of cash/assets * current ratio
def f33bs_f33_balance_sheet_strength_cashbacked_168d_slope_v118_signal(cashneq, assets, currentratio):
    ratio = (_f33_cash_assets(cashneq, assets) * currentratio)
    b = _slope_log(ratio, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 168d) of equity / cash
def f33bs_f33_balance_sheet_strength_eqcash_168d_slope_v119_signal(equity, cashneq):
    ratio = (equity / cashneq.replace(0, np.nan))
    b = _slope_log(ratio, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope log-magnitude 1st-derivative (window 168d) of (cash+wc)/assets
def f33bs_f33_balance_sheet_strength_liqbufassets_168d_slope_v120_signal(cashneq, workingcapital, assets):
    ratio = ((cashneq + workingcapital) / assets.replace(0, np.nan))
    b = _slope_log(ratio, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 210d) of net cash / assets
def f33bs_f33_balance_sheet_strength_netcashassets_210d_slope_v121_signal(cashneq, debt, assets):
    ratio = (_f33_net_cash(cashneq, debt) / assets.replace(0, np.nan))
    b = _slope_sn(ratio, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 210d) of debt / equity
def f33bs_f33_balance_sheet_strength_de_210d_slope_v122_signal(debt, equity):
    ratio = _f33_de(debt, equity)
    b = _slope_sn(ratio, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 210d) of debt / assets
def f33bs_f33_balance_sheet_strength_da_210d_slope_v123_signal(debt, assets):
    ratio = _f33_da(debt, assets)
    b = _slope_sn(ratio, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 210d) of equity / assets
def f33bs_f33_balance_sheet_strength_ea_210d_slope_v124_signal(equity, assets):
    ratio = _f33_ea(equity, assets)
    b = _slope_sn(ratio, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 210d) of working capital / assets
def f33bs_f33_balance_sheet_strength_wca_210d_slope_v125_signal(workingcapital, assets):
    ratio = _f33_wca(workingcapital, assets)
    b = _slope_sn(ratio, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 210d) of current ratio
def f33bs_f33_balance_sheet_strength_curr_210d_slope_v126_signal(currentratio):
    ratio = currentratio
    b = _slope_sn(ratio, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 210d) of liabilities / assets
def f33bs_f33_balance_sheet_strength_liabassets_210d_slope_v127_signal(liabilities, assets):
    ratio = _f33_liab_assets(liabilities, assets)
    b = _slope_sn(ratio, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 210d) of cash / assets
def f33bs_f33_balance_sheet_strength_cashassets_210d_slope_v128_signal(cashneq, assets):
    ratio = _f33_cash_assets(cashneq, assets)
    b = _slope_sn(ratio, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 210d) of cash / liabilities
def f33bs_f33_balance_sheet_strength_cashliab_210d_slope_v129_signal(cashneq, liabilities):
    ratio = (cashneq / liabilities.replace(0, np.nan))
    b = _slope_sn(ratio, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 210d) of equity / liabilities
def f33bs_f33_balance_sheet_strength_eqliab_210d_slope_v130_signal(equity, liabilities):
    ratio = (equity / liabilities.replace(0, np.nan))
    b = _slope_sn(ratio, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 210d) of debt / working capital
def f33bs_f33_balance_sheet_strength_debtwc_210d_slope_v131_signal(debt, workingcapital):
    ratio = (debt / workingcapital.replace(0, np.nan))
    b = _slope_sn(ratio, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 210d) of equity/assets * current ratio
def f33bs_f33_balance_sheet_strength_capliq_210d_slope_v132_signal(equity, assets, currentratio):
    ratio = (_f33_ea(equity, assets) * currentratio)
    b = _slope_sn(ratio, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 210d) of cash/assets * current ratio
def f33bs_f33_balance_sheet_strength_cashbacked_210d_slope_v133_signal(cashneq, assets, currentratio):
    ratio = (_f33_cash_assets(cashneq, assets) * currentratio)
    b = _slope_sn(ratio, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 210d) of equity / cash
def f33bs_f33_balance_sheet_strength_eqcash_210d_slope_v134_signal(equity, cashneq):
    ratio = (equity / cashneq.replace(0, np.nan))
    b = _slope_sn(ratio, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope signal-to-noise 1st-derivative (window 210d) of (cash+wc)/assets
def f33bs_f33_balance_sheet_strength_liqbufassets_210d_slope_v135_signal(cashneq, workingcapital, assets):
    ratio = ((cashneq + workingcapital) / assets.replace(0, np.nan))
    b = _slope_sn(ratio, 210)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 252d) of net cash / assets
def f33bs_f33_balance_sheet_strength_netcashassets_252d_slope_v136_signal(cashneq, debt, assets):
    ratio = (_f33_net_cash(cashneq, debt) / assets.replace(0, np.nan))
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 252d) of debt / equity
def f33bs_f33_balance_sheet_strength_de_252d_slope_v137_signal(debt, equity):
    ratio = _f33_de(debt, equity)
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 252d) of debt / assets
def f33bs_f33_balance_sheet_strength_da_252d_slope_v138_signal(debt, assets):
    ratio = _f33_da(debt, assets)
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 252d) of equity / assets
def f33bs_f33_balance_sheet_strength_ea_252d_slope_v139_signal(equity, assets):
    ratio = _f33_ea(equity, assets)
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 252d) of working capital / assets
def f33bs_f33_balance_sheet_strength_wca_252d_slope_v140_signal(workingcapital, assets):
    ratio = _f33_wca(workingcapital, assets)
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 252d) of current ratio
def f33bs_f33_balance_sheet_strength_curr_252d_slope_v141_signal(currentratio):
    ratio = currentratio
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 252d) of liabilities / assets
def f33bs_f33_balance_sheet_strength_liabassets_252d_slope_v142_signal(liabilities, assets):
    ratio = _f33_liab_assets(liabilities, assets)
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 252d) of cash / assets
def f33bs_f33_balance_sheet_strength_cashassets_252d_slope_v143_signal(cashneq, assets):
    ratio = _f33_cash_assets(cashneq, assets)
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 252d) of cash / liabilities
def f33bs_f33_balance_sheet_strength_cashliab_252d_slope_v144_signal(cashneq, liabilities):
    ratio = (cashneq / liabilities.replace(0, np.nan))
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 252d) of equity / liabilities
def f33bs_f33_balance_sheet_strength_eqliab_252d_slope_v145_signal(equity, liabilities):
    ratio = (equity / liabilities.replace(0, np.nan))
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 252d) of debt / working capital
def f33bs_f33_balance_sheet_strength_debtwc_252d_slope_v146_signal(debt, workingcapital):
    ratio = (debt / workingcapital.replace(0, np.nan))
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 252d) of equity/assets * current ratio
def f33bs_f33_balance_sheet_strength_capliq_252d_slope_v147_signal(equity, assets, currentratio):
    ratio = (_f33_ea(equity, assets) * currentratio)
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 252d) of cash/assets * current ratio
def f33bs_f33_balance_sheet_strength_cashbacked_252d_slope_v148_signal(cashneq, assets, currentratio):
    ratio = (_f33_cash_assets(cashneq, assets) * currentratio)
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 252d) of equity / cash
def f33bs_f33_balance_sheet_strength_eqcash_252d_slope_v149_signal(equity, cashneq):
    ratio = (equity / cashneq.replace(0, np.nan))
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope 1st-derivative (window 252d) of (cash+wc)/assets
def f33bs_f33_balance_sheet_strength_liqbufassets_252d_slope_v150_signal(cashneq, workingcapital, assets):
    ratio = ((cashneq + workingcapital) / assets.replace(0, np.nan))
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33bs_f33_balance_sheet_strength_netcashassets_10d_slope_v001_signal,
    f33bs_f33_balance_sheet_strength_de_10d_slope_v002_signal,
    f33bs_f33_balance_sheet_strength_da_10d_slope_v003_signal,
    f33bs_f33_balance_sheet_strength_ea_10d_slope_v004_signal,
    f33bs_f33_balance_sheet_strength_wca_10d_slope_v005_signal,
    f33bs_f33_balance_sheet_strength_curr_10d_slope_v006_signal,
    f33bs_f33_balance_sheet_strength_liabassets_10d_slope_v007_signal,
    f33bs_f33_balance_sheet_strength_cashassets_10d_slope_v008_signal,
    f33bs_f33_balance_sheet_strength_cashliab_10d_slope_v009_signal,
    f33bs_f33_balance_sheet_strength_eqliab_10d_slope_v010_signal,
    f33bs_f33_balance_sheet_strength_debtwc_10d_slope_v011_signal,
    f33bs_f33_balance_sheet_strength_capliq_10d_slope_v012_signal,
    f33bs_f33_balance_sheet_strength_cashbacked_10d_slope_v013_signal,
    f33bs_f33_balance_sheet_strength_eqcash_10d_slope_v014_signal,
    f33bs_f33_balance_sheet_strength_liqbufassets_10d_slope_v015_signal,
    f33bs_f33_balance_sheet_strength_netcashassets_25d_slope_v016_signal,
    f33bs_f33_balance_sheet_strength_de_25d_slope_v017_signal,
    f33bs_f33_balance_sheet_strength_da_25d_slope_v018_signal,
    f33bs_f33_balance_sheet_strength_ea_25d_slope_v019_signal,
    f33bs_f33_balance_sheet_strength_wca_25d_slope_v020_signal,
    f33bs_f33_balance_sheet_strength_curr_25d_slope_v021_signal,
    f33bs_f33_balance_sheet_strength_liabassets_25d_slope_v022_signal,
    f33bs_f33_balance_sheet_strength_cashassets_25d_slope_v023_signal,
    f33bs_f33_balance_sheet_strength_cashliab_25d_slope_v024_signal,
    f33bs_f33_balance_sheet_strength_eqliab_25d_slope_v025_signal,
    f33bs_f33_balance_sheet_strength_debtwc_25d_slope_v026_signal,
    f33bs_f33_balance_sheet_strength_capliq_25d_slope_v027_signal,
    f33bs_f33_balance_sheet_strength_cashbacked_25d_slope_v028_signal,
    f33bs_f33_balance_sheet_strength_eqcash_25d_slope_v029_signal,
    f33bs_f33_balance_sheet_strength_liqbufassets_25d_slope_v030_signal,
    f33bs_f33_balance_sheet_strength_netcashassets_42d_slope_v031_signal,
    f33bs_f33_balance_sheet_strength_de_42d_slope_v032_signal,
    f33bs_f33_balance_sheet_strength_da_42d_slope_v033_signal,
    f33bs_f33_balance_sheet_strength_ea_42d_slope_v034_signal,
    f33bs_f33_balance_sheet_strength_wca_42d_slope_v035_signal,
    f33bs_f33_balance_sheet_strength_curr_42d_slope_v036_signal,
    f33bs_f33_balance_sheet_strength_liabassets_42d_slope_v037_signal,
    f33bs_f33_balance_sheet_strength_cashassets_42d_slope_v038_signal,
    f33bs_f33_balance_sheet_strength_cashliab_42d_slope_v039_signal,
    f33bs_f33_balance_sheet_strength_eqliab_42d_slope_v040_signal,
    f33bs_f33_balance_sheet_strength_debtwc_42d_slope_v041_signal,
    f33bs_f33_balance_sheet_strength_capliq_42d_slope_v042_signal,
    f33bs_f33_balance_sheet_strength_cashbacked_42d_slope_v043_signal,
    f33bs_f33_balance_sheet_strength_eqcash_42d_slope_v044_signal,
    f33bs_f33_balance_sheet_strength_liqbufassets_42d_slope_v045_signal,
    f33bs_f33_balance_sheet_strength_netcashassets_63d_slope_v046_signal,
    f33bs_f33_balance_sheet_strength_de_63d_slope_v047_signal,
    f33bs_f33_balance_sheet_strength_da_63d_slope_v048_signal,
    f33bs_f33_balance_sheet_strength_ea_63d_slope_v049_signal,
    f33bs_f33_balance_sheet_strength_wca_63d_slope_v050_signal,
    f33bs_f33_balance_sheet_strength_curr_63d_slope_v051_signal,
    f33bs_f33_balance_sheet_strength_liabassets_63d_slope_v052_signal,
    f33bs_f33_balance_sheet_strength_cashassets_63d_slope_v053_signal,
    f33bs_f33_balance_sheet_strength_cashliab_63d_slope_v054_signal,
    f33bs_f33_balance_sheet_strength_eqliab_63d_slope_v055_signal,
    f33bs_f33_balance_sheet_strength_debtwc_63d_slope_v056_signal,
    f33bs_f33_balance_sheet_strength_capliq_63d_slope_v057_signal,
    f33bs_f33_balance_sheet_strength_cashbacked_63d_slope_v058_signal,
    f33bs_f33_balance_sheet_strength_eqcash_63d_slope_v059_signal,
    f33bs_f33_balance_sheet_strength_liqbufassets_63d_slope_v060_signal,
    f33bs_f33_balance_sheet_strength_netcashassets_84d_slope_v061_signal,
    f33bs_f33_balance_sheet_strength_de_84d_slope_v062_signal,
    f33bs_f33_balance_sheet_strength_da_84d_slope_v063_signal,
    f33bs_f33_balance_sheet_strength_ea_84d_slope_v064_signal,
    f33bs_f33_balance_sheet_strength_wca_84d_slope_v065_signal,
    f33bs_f33_balance_sheet_strength_curr_84d_slope_v066_signal,
    f33bs_f33_balance_sheet_strength_liabassets_84d_slope_v067_signal,
    f33bs_f33_balance_sheet_strength_cashassets_84d_slope_v068_signal,
    f33bs_f33_balance_sheet_strength_cashliab_84d_slope_v069_signal,
    f33bs_f33_balance_sheet_strength_eqliab_84d_slope_v070_signal,
    f33bs_f33_balance_sheet_strength_debtwc_84d_slope_v071_signal,
    f33bs_f33_balance_sheet_strength_capliq_84d_slope_v072_signal,
    f33bs_f33_balance_sheet_strength_cashbacked_84d_slope_v073_signal,
    f33bs_f33_balance_sheet_strength_eqcash_84d_slope_v074_signal,
    f33bs_f33_balance_sheet_strength_liqbufassets_84d_slope_v075_signal,
    f33bs_f33_balance_sheet_strength_netcashassets_110d_slope_v076_signal,
    f33bs_f33_balance_sheet_strength_de_110d_slope_v077_signal,
    f33bs_f33_balance_sheet_strength_da_110d_slope_v078_signal,
    f33bs_f33_balance_sheet_strength_ea_110d_slope_v079_signal,
    f33bs_f33_balance_sheet_strength_wca_110d_slope_v080_signal,
    f33bs_f33_balance_sheet_strength_curr_110d_slope_v081_signal,
    f33bs_f33_balance_sheet_strength_liabassets_110d_slope_v082_signal,
    f33bs_f33_balance_sheet_strength_cashassets_110d_slope_v083_signal,
    f33bs_f33_balance_sheet_strength_cashliab_110d_slope_v084_signal,
    f33bs_f33_balance_sheet_strength_eqliab_110d_slope_v085_signal,
    f33bs_f33_balance_sheet_strength_debtwc_110d_slope_v086_signal,
    f33bs_f33_balance_sheet_strength_capliq_110d_slope_v087_signal,
    f33bs_f33_balance_sheet_strength_cashbacked_110d_slope_v088_signal,
    f33bs_f33_balance_sheet_strength_eqcash_110d_slope_v089_signal,
    f33bs_f33_balance_sheet_strength_liqbufassets_110d_slope_v090_signal,
    f33bs_f33_balance_sheet_strength_netcashassets_130d_slope_v091_signal,
    f33bs_f33_balance_sheet_strength_de_130d_slope_v092_signal,
    f33bs_f33_balance_sheet_strength_da_130d_slope_v093_signal,
    f33bs_f33_balance_sheet_strength_ea_130d_slope_v094_signal,
    f33bs_f33_balance_sheet_strength_wca_130d_slope_v095_signal,
    f33bs_f33_balance_sheet_strength_curr_130d_slope_v096_signal,
    f33bs_f33_balance_sheet_strength_liabassets_130d_slope_v097_signal,
    f33bs_f33_balance_sheet_strength_cashassets_130d_slope_v098_signal,
    f33bs_f33_balance_sheet_strength_cashliab_130d_slope_v099_signal,
    f33bs_f33_balance_sheet_strength_eqliab_130d_slope_v100_signal,
    f33bs_f33_balance_sheet_strength_debtwc_130d_slope_v101_signal,
    f33bs_f33_balance_sheet_strength_capliq_130d_slope_v102_signal,
    f33bs_f33_balance_sheet_strength_cashbacked_130d_slope_v103_signal,
    f33bs_f33_balance_sheet_strength_eqcash_130d_slope_v104_signal,
    f33bs_f33_balance_sheet_strength_liqbufassets_130d_slope_v105_signal,
    f33bs_f33_balance_sheet_strength_netcashassets_168d_slope_v106_signal,
    f33bs_f33_balance_sheet_strength_de_168d_slope_v107_signal,
    f33bs_f33_balance_sheet_strength_da_168d_slope_v108_signal,
    f33bs_f33_balance_sheet_strength_ea_168d_slope_v109_signal,
    f33bs_f33_balance_sheet_strength_wca_168d_slope_v110_signal,
    f33bs_f33_balance_sheet_strength_curr_168d_slope_v111_signal,
    f33bs_f33_balance_sheet_strength_liabassets_168d_slope_v112_signal,
    f33bs_f33_balance_sheet_strength_cashassets_168d_slope_v113_signal,
    f33bs_f33_balance_sheet_strength_cashliab_168d_slope_v114_signal,
    f33bs_f33_balance_sheet_strength_eqliab_168d_slope_v115_signal,
    f33bs_f33_balance_sheet_strength_debtwc_168d_slope_v116_signal,
    f33bs_f33_balance_sheet_strength_capliq_168d_slope_v117_signal,
    f33bs_f33_balance_sheet_strength_cashbacked_168d_slope_v118_signal,
    f33bs_f33_balance_sheet_strength_eqcash_168d_slope_v119_signal,
    f33bs_f33_balance_sheet_strength_liqbufassets_168d_slope_v120_signal,
    f33bs_f33_balance_sheet_strength_netcashassets_210d_slope_v121_signal,
    f33bs_f33_balance_sheet_strength_de_210d_slope_v122_signal,
    f33bs_f33_balance_sheet_strength_da_210d_slope_v123_signal,
    f33bs_f33_balance_sheet_strength_ea_210d_slope_v124_signal,
    f33bs_f33_balance_sheet_strength_wca_210d_slope_v125_signal,
    f33bs_f33_balance_sheet_strength_curr_210d_slope_v126_signal,
    f33bs_f33_balance_sheet_strength_liabassets_210d_slope_v127_signal,
    f33bs_f33_balance_sheet_strength_cashassets_210d_slope_v128_signal,
    f33bs_f33_balance_sheet_strength_cashliab_210d_slope_v129_signal,
    f33bs_f33_balance_sheet_strength_eqliab_210d_slope_v130_signal,
    f33bs_f33_balance_sheet_strength_debtwc_210d_slope_v131_signal,
    f33bs_f33_balance_sheet_strength_capliq_210d_slope_v132_signal,
    f33bs_f33_balance_sheet_strength_cashbacked_210d_slope_v133_signal,
    f33bs_f33_balance_sheet_strength_eqcash_210d_slope_v134_signal,
    f33bs_f33_balance_sheet_strength_liqbufassets_210d_slope_v135_signal,
    f33bs_f33_balance_sheet_strength_netcashassets_252d_slope_v136_signal,
    f33bs_f33_balance_sheet_strength_de_252d_slope_v137_signal,
    f33bs_f33_balance_sheet_strength_da_252d_slope_v138_signal,
    f33bs_f33_balance_sheet_strength_ea_252d_slope_v139_signal,
    f33bs_f33_balance_sheet_strength_wca_252d_slope_v140_signal,
    f33bs_f33_balance_sheet_strength_curr_252d_slope_v141_signal,
    f33bs_f33_balance_sheet_strength_liabassets_252d_slope_v142_signal,
    f33bs_f33_balance_sheet_strength_cashassets_252d_slope_v143_signal,
    f33bs_f33_balance_sheet_strength_cashliab_252d_slope_v144_signal,
    f33bs_f33_balance_sheet_strength_eqliab_252d_slope_v145_signal,
    f33bs_f33_balance_sheet_strength_debtwc_252d_slope_v146_signal,
    f33bs_f33_balance_sheet_strength_capliq_252d_slope_v147_signal,
    f33bs_f33_balance_sheet_strength_cashbacked_252d_slope_v148_signal,
    f33bs_f33_balance_sheet_strength_eqcash_252d_slope_v149_signal,
    f33bs_f33_balance_sheet_strength_liqbufassets_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_BALANCE_SHEET_STRENGTH_REGISTRY_001_150 = REGISTRY


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

    print("OK f33_balance_sheet_strength_2nd_derivatives_001_150_claude: %d features pass" % n_features)
