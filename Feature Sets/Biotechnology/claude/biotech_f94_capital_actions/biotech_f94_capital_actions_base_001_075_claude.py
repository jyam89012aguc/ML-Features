"""Family f94 - Capital-structure actions  (Q_Actions_Events) | base 001-075"""
import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _capital_actions_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _capital_actions_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _capital_actions_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed actionvalue times closeadj
def ca_f94_capital_actions_raw_21d_base_v001_signal(actionvalue, closeadj):
    result = _mean(actionvalue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed actionvalue times closeadj
def ca_f94_capital_actions_raw_63d_base_v002_signal(actionvalue, closeadj):
    result = _mean(actionvalue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed actionvalue times closeadj
def ca_f94_capital_actions_raw_126d_base_v003_signal(actionvalue, closeadj):
    result = _mean(actionvalue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed actionvalue times closeadj
def ca_f94_capital_actions_raw_252d_base_v004_signal(actionvalue, closeadj):
    result = _mean(actionvalue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed actionvalue times closeadj
def ca_f94_capital_actions_raw_504d_base_v005_signal(actionvalue, closeadj):
    result = _mean(actionvalue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(actionvalue) times closeadj
def ca_f94_capital_actions_log_21d_base_v006_signal(actionvalue, closeadj):
    result = _mean(_capital_actions_log(actionvalue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(actionvalue) times closeadj
def ca_f94_capital_actions_log_63d_base_v007_signal(actionvalue, closeadj):
    result = _mean(_capital_actions_log(actionvalue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(actionvalue) times closeadj
def ca_f94_capital_actions_log_126d_base_v008_signal(actionvalue, closeadj):
    result = _mean(_capital_actions_log(actionvalue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(actionvalue) times closeadj
def ca_f94_capital_actions_log_252d_base_v009_signal(actionvalue, closeadj):
    result = _mean(_capital_actions_log(actionvalue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(actionvalue) times closeadj
def ca_f94_capital_actions_log_504d_base_v010_signal(actionvalue, closeadj):
    result = _mean(_capital_actions_log(actionvalue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d actionvalue/assets mean
def ca_f94_capital_actions_per_assets_63d_base_v011_signal(actionvalue, assets):
    result = _mean(_capital_actions_scaled(actionvalue, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d actionvalue/assets mean
def ca_f94_capital_actions_per_assets_252d_base_v012_signal(actionvalue, assets):
    result = _mean(_capital_actions_scaled(actionvalue, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d actionvalue/assets mean
def ca_f94_capital_actions_per_assets_504d_base_v013_signal(actionvalue, assets):
    result = _mean(_capital_actions_scaled(actionvalue, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d actionvalue/marketcap mean
def ca_f94_capital_actions_per_marketcap_63d_base_v014_signal(actionvalue, marketcap):
    result = _mean(_capital_actions_scaled(actionvalue, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d actionvalue/marketcap mean
def ca_f94_capital_actions_per_marketcap_252d_base_v015_signal(actionvalue, marketcap):
    result = _mean(_capital_actions_scaled(actionvalue, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d actionvalue/marketcap mean
def ca_f94_capital_actions_per_marketcap_504d_base_v016_signal(actionvalue, marketcap):
    result = _mean(_capital_actions_scaled(actionvalue, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d actionvalue/equity mean
def ca_f94_capital_actions_per_equity_63d_base_v017_signal(actionvalue, equity):
    result = _mean(_capital_actions_scaled(actionvalue, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d actionvalue/equity mean
def ca_f94_capital_actions_per_equity_252d_base_v018_signal(actionvalue, equity):
    result = _mean(_capital_actions_scaled(actionvalue, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d actionvalue/equity mean
def ca_f94_capital_actions_per_equity_504d_base_v019_signal(actionvalue, equity):
    result = _mean(_capital_actions_scaled(actionvalue, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d actionvalue/debt mean
def ca_f94_capital_actions_per_debt_63d_base_v020_signal(actionvalue, debt):
    result = _mean(_capital_actions_scaled(actionvalue, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d actionvalue/debt mean
def ca_f94_capital_actions_per_debt_252d_base_v021_signal(actionvalue, debt):
    result = _mean(_capital_actions_scaled(actionvalue, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d actionvalue/debt mean
def ca_f94_capital_actions_per_debt_504d_base_v022_signal(actionvalue, debt):
    result = _mean(_capital_actions_scaled(actionvalue, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d actionvalue/revenue mean
def ca_f94_capital_actions_per_revenue_63d_base_v023_signal(actionvalue, revenue):
    result = _mean(_capital_actions_scaled(actionvalue, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d actionvalue/revenue mean
def ca_f94_capital_actions_per_revenue_252d_base_v024_signal(actionvalue, revenue):
    result = _mean(_capital_actions_scaled(actionvalue, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d actionvalue/revenue mean
def ca_f94_capital_actions_per_revenue_504d_base_v025_signal(actionvalue, revenue):
    result = _mean(_capital_actions_scaled(actionvalue, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d actionvalue per share times closeadj
def ca_f94_capital_actions_pershare_21d_base_v026_signal(actionvalue, sharesbas, closeadj):
    ps = _capital_actions_per_share(actionvalue, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d actionvalue per share times closeadj
def ca_f94_capital_actions_pershare_63d_base_v027_signal(actionvalue, sharesbas, closeadj):
    ps = _capital_actions_per_share(actionvalue, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d actionvalue per share times closeadj
def ca_f94_capital_actions_pershare_126d_base_v028_signal(actionvalue, sharesbas, closeadj):
    ps = _capital_actions_per_share(actionvalue, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d actionvalue per share times closeadj
def ca_f94_capital_actions_pershare_252d_base_v029_signal(actionvalue, sharesbas, closeadj):
    ps = _capital_actions_per_share(actionvalue, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d actionvalue per share times closeadj
def ca_f94_capital_actions_pershare_504d_base_v030_signal(actionvalue, sharesbas, closeadj):
    ps = _capital_actions_per_share(actionvalue, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of actionvalue times closeadj
def ca_f94_capital_actions_std_63d_base_v031_signal(actionvalue, closeadj):
    result = _std(actionvalue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of actionvalue times closeadj
def ca_f94_capital_actions_std_252d_base_v032_signal(actionvalue, closeadj):
    result = _std(actionvalue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of actionvalue times closeadj
def ca_f94_capital_actions_std_504d_base_v033_signal(actionvalue, closeadj):
    result = _std(actionvalue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of actionvalue
def ca_f94_capital_actions_z_252d_base_v034_signal(actionvalue):
    result = _z(actionvalue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of actionvalue
def ca_f94_capital_actions_z_504d_base_v035_signal(actionvalue):
    result = _z(actionvalue, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(actionvalue)
def ca_f94_capital_actions_logz_252d_base_v036_signal(actionvalue):
    result = _z(_capital_actions_log(actionvalue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(actionvalue)
def ca_f94_capital_actions_logz_504d_base_v037_signal(actionvalue):
    result = _z(_capital_actions_log(actionvalue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of actionvalue^2 times closeadj
def ca_f94_capital_actions_sq_63d_base_v038_signal(actionvalue, closeadj):
    result = _mean(actionvalue * actionvalue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of actionvalue^2 times closeadj
def ca_f94_capital_actions_sq_252d_base_v039_signal(actionvalue, closeadj):
    result = _mean(actionvalue * actionvalue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(actionvalue) times closeadj
def ca_f94_capital_actions_sign_21d_base_v040_signal(actionvalue, closeadj):
    result = _mean(np.sign(actionvalue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(actionvalue) times closeadj
def ca_f94_capital_actions_sign_63d_base_v041_signal(actionvalue, closeadj):
    result = _mean(np.sign(actionvalue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(actionvalue) times closeadj
def ca_f94_capital_actions_sign_252d_base_v042_signal(actionvalue, closeadj):
    result = _mean(np.sign(actionvalue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d actionvalue/opex mean
def ca_f94_capital_actions_per_opex_63d_base_v043_signal(actionvalue, opex):
    result = _mean(_capital_actions_scaled(actionvalue, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d actionvalue/opex mean
def ca_f94_capital_actions_per_opex_252d_base_v044_signal(actionvalue, opex):
    result = _mean(_capital_actions_scaled(actionvalue, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d actionvalue/ebitda mean
def ca_f94_capital_actions_per_ebitda_63d_base_v045_signal(actionvalue, ebitda):
    result = _mean(_capital_actions_scaled(actionvalue, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d actionvalue/ebitda mean
def ca_f94_capital_actions_per_ebitda_252d_base_v046_signal(actionvalue, ebitda):
    result = _mean(_capital_actions_scaled(actionvalue, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d actionvalue/capex mean
def ca_f94_capital_actions_per_capex_63d_base_v047_signal(actionvalue, capex):
    result = _mean(_capital_actions_scaled(actionvalue, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d actionvalue/capex mean
def ca_f94_capital_actions_per_capex_252d_base_v048_signal(actionvalue, capex):
    result = _mean(_capital_actions_scaled(actionvalue, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d actionvalue/liabilities mean
def ca_f94_capital_actions_per_liabilities_63d_base_v049_signal(actionvalue, liabilities):
    result = _mean(_capital_actions_scaled(actionvalue, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d actionvalue/liabilities mean
def ca_f94_capital_actions_per_liabilities_252d_base_v050_signal(actionvalue, liabilities):
    result = _mean(_capital_actions_scaled(actionvalue, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# actionvalue relative to 252d max times closeadj
def ca_f94_capital_actions_relmax_252d_base_v051_signal(actionvalue, closeadj):
    peak = actionvalue.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (actionvalue / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# actionvalue relative to 504d max times closeadj
def ca_f94_capital_actions_relmax_504d_base_v052_signal(actionvalue, closeadj):
    peak = actionvalue.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (actionvalue / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# actionvalue relative to 252d min times closeadj
def ca_f94_capital_actions_relmin_252d_base_v053_signal(actionvalue, closeadj):
    trough = actionvalue.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (actionvalue / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# actionvalue relative to 504d min times closeadj
def ca_f94_capital_actions_relmin_504d_base_v054_signal(actionvalue, closeadj):
    trough = actionvalue.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (actionvalue / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of actionvalue times closeadj
def ca_f94_capital_actions_pct_21d_base_v055_signal(actionvalue, closeadj):
    result = _pct_change(actionvalue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of actionvalue times closeadj
def ca_f94_capital_actions_pct_63d_base_v056_signal(actionvalue, closeadj):
    result = _pct_change(actionvalue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of actionvalue times closeadj
def ca_f94_capital_actions_pct_252d_base_v057_signal(actionvalue, closeadj):
    result = _pct_change(actionvalue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of actionvalue times closeadj
def ca_f94_capital_actions_sum_63d_base_v058_signal(actionvalue, closeadj):
    result = actionvalue.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of actionvalue times closeadj
def ca_f94_capital_actions_sum_252d_base_v059_signal(actionvalue, closeadj):
    result = actionvalue.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of actionvalue times closeadj
def ca_f94_capital_actions_sum_504d_base_v060_signal(actionvalue, closeadj):
    result = actionvalue.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed actionvalue(63d) / smoothed assets(252d) x closeadj
def ca_f94_capital_actions_rom_assets_252_63d_base_v061_signal(actionvalue, assets, closeadj):
    n = _mean(actionvalue, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed actionvalue(126d) / smoothed assets(504d) x closeadj
def ca_f94_capital_actions_rom_assets_504_126d_base_v062_signal(actionvalue, assets, closeadj):
    n = _mean(actionvalue, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed actionvalue(63d) / smoothed marketcap(252d) x closeadj
def ca_f94_capital_actions_rom_marketcap_252_63d_base_v063_signal(actionvalue, marketcap, closeadj):
    n = _mean(actionvalue, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed actionvalue(126d) / smoothed marketcap(504d) x closeadj
def ca_f94_capital_actions_rom_marketcap_504_126d_base_v064_signal(actionvalue, marketcap, closeadj):
    n = _mean(actionvalue, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed actionvalue(63d) / smoothed equity(252d) x closeadj
def ca_f94_capital_actions_rom_equity_252_63d_base_v065_signal(actionvalue, equity, closeadj):
    n = _mean(actionvalue, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed actionvalue(126d) / smoothed equity(504d) x closeadj
def ca_f94_capital_actions_rom_equity_504_126d_base_v066_signal(actionvalue, equity, closeadj):
    n = _mean(actionvalue, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(actionvalue) / std(assets)
def ca_f94_capital_actions_volratio_assets_252d_base_v067_signal(actionvalue, assets):
    n = _std(actionvalue, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(actionvalue) / std(assets)
def ca_f94_capital_actions_volratio_assets_504d_base_v068_signal(actionvalue, assets):
    n = _std(actionvalue, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(actionvalue) / std(marketcap)
def ca_f94_capital_actions_volratio_marketcap_252d_base_v069_signal(actionvalue, marketcap):
    n = _std(actionvalue, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(actionvalue) / std(marketcap)
def ca_f94_capital_actions_volratio_marketcap_504d_base_v070_signal(actionvalue, marketcap):
    n = _std(actionvalue, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed actionvalue times closeadj
def ca_f94_capital_actions_raw_5d_base_v071_signal(actionvalue, closeadj):
    result = _mean(actionvalue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed actionvalue times closeadj
def ca_f94_capital_actions_raw_1008d_base_v072_signal(actionvalue, closeadj):
    result = _mean(actionvalue, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of actionvalue/assets
def ca_f94_capital_actions_log_per_assets_252d_base_v073_signal(actionvalue, assets):
    s = _capital_actions_scaled(actionvalue, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of actionvalue/assets
def ca_f94_capital_actions_log_per_assets_504d_base_v074_signal(actionvalue, assets):
    s = _capital_actions_scaled(actionvalue, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of actionvalue/marketcap
def ca_f94_capital_actions_log_per_marketcap_252d_base_v075_signal(actionvalue, marketcap):
    s = _capital_actions_scaled(actionvalue, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
