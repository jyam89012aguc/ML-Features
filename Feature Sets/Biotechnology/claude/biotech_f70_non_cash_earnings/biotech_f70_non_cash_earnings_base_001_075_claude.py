"""Family f70 - Non-cash share of earnings  (L_EarningsQuality) | base 001-075"""
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
def _non_cash_earnings_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _non_cash_earnings_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _non_cash_earnings_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed depamor times closeadj
def nce_f70_non_cash_earnings_raw_21d_base_v001_signal(depamor, closeadj):
    result = _mean(depamor, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed depamor times closeadj
def nce_f70_non_cash_earnings_raw_63d_base_v002_signal(depamor, closeadj):
    result = _mean(depamor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed depamor times closeadj
def nce_f70_non_cash_earnings_raw_126d_base_v003_signal(depamor, closeadj):
    result = _mean(depamor, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed depamor times closeadj
def nce_f70_non_cash_earnings_raw_252d_base_v004_signal(depamor, closeadj):
    result = _mean(depamor, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed depamor times closeadj
def nce_f70_non_cash_earnings_raw_504d_base_v005_signal(depamor, closeadj):
    result = _mean(depamor, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(depamor) times closeadj
def nce_f70_non_cash_earnings_log_21d_base_v006_signal(depamor, closeadj):
    result = _mean(_non_cash_earnings_log(depamor), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(depamor) times closeadj
def nce_f70_non_cash_earnings_log_63d_base_v007_signal(depamor, closeadj):
    result = _mean(_non_cash_earnings_log(depamor), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(depamor) times closeadj
def nce_f70_non_cash_earnings_log_126d_base_v008_signal(depamor, closeadj):
    result = _mean(_non_cash_earnings_log(depamor), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(depamor) times closeadj
def nce_f70_non_cash_earnings_log_252d_base_v009_signal(depamor, closeadj):
    result = _mean(_non_cash_earnings_log(depamor), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(depamor) times closeadj
def nce_f70_non_cash_earnings_log_504d_base_v010_signal(depamor, closeadj):
    result = _mean(_non_cash_earnings_log(depamor), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/assets mean
def nce_f70_non_cash_earnings_per_assets_63d_base_v011_signal(depamor, assets):
    result = _mean(_non_cash_earnings_scaled(depamor, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/assets mean
def nce_f70_non_cash_earnings_per_assets_252d_base_v012_signal(depamor, assets):
    result = _mean(_non_cash_earnings_scaled(depamor, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d depamor/assets mean
def nce_f70_non_cash_earnings_per_assets_504d_base_v013_signal(depamor, assets):
    result = _mean(_non_cash_earnings_scaled(depamor, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/marketcap mean
def nce_f70_non_cash_earnings_per_marketcap_63d_base_v014_signal(depamor, marketcap):
    result = _mean(_non_cash_earnings_scaled(depamor, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/marketcap mean
def nce_f70_non_cash_earnings_per_marketcap_252d_base_v015_signal(depamor, marketcap):
    result = _mean(_non_cash_earnings_scaled(depamor, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d depamor/marketcap mean
def nce_f70_non_cash_earnings_per_marketcap_504d_base_v016_signal(depamor, marketcap):
    result = _mean(_non_cash_earnings_scaled(depamor, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/equity mean
def nce_f70_non_cash_earnings_per_equity_63d_base_v017_signal(depamor, equity):
    result = _mean(_non_cash_earnings_scaled(depamor, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/equity mean
def nce_f70_non_cash_earnings_per_equity_252d_base_v018_signal(depamor, equity):
    result = _mean(_non_cash_earnings_scaled(depamor, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d depamor/equity mean
def nce_f70_non_cash_earnings_per_equity_504d_base_v019_signal(depamor, equity):
    result = _mean(_non_cash_earnings_scaled(depamor, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/debt mean
def nce_f70_non_cash_earnings_per_debt_63d_base_v020_signal(depamor, debt):
    result = _mean(_non_cash_earnings_scaled(depamor, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/debt mean
def nce_f70_non_cash_earnings_per_debt_252d_base_v021_signal(depamor, debt):
    result = _mean(_non_cash_earnings_scaled(depamor, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d depamor/debt mean
def nce_f70_non_cash_earnings_per_debt_504d_base_v022_signal(depamor, debt):
    result = _mean(_non_cash_earnings_scaled(depamor, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/revenue mean
def nce_f70_non_cash_earnings_per_revenue_63d_base_v023_signal(depamor, revenue):
    result = _mean(_non_cash_earnings_scaled(depamor, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/revenue mean
def nce_f70_non_cash_earnings_per_revenue_252d_base_v024_signal(depamor, revenue):
    result = _mean(_non_cash_earnings_scaled(depamor, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d depamor/revenue mean
def nce_f70_non_cash_earnings_per_revenue_504d_base_v025_signal(depamor, revenue):
    result = _mean(_non_cash_earnings_scaled(depamor, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d depamor per share times closeadj
def nce_f70_non_cash_earnings_pershare_21d_base_v026_signal(depamor, sharesbas, closeadj):
    ps = _non_cash_earnings_per_share(depamor, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor per share times closeadj
def nce_f70_non_cash_earnings_pershare_63d_base_v027_signal(depamor, sharesbas, closeadj):
    ps = _non_cash_earnings_per_share(depamor, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d depamor per share times closeadj
def nce_f70_non_cash_earnings_pershare_126d_base_v028_signal(depamor, sharesbas, closeadj):
    ps = _non_cash_earnings_per_share(depamor, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor per share times closeadj
def nce_f70_non_cash_earnings_pershare_252d_base_v029_signal(depamor, sharesbas, closeadj):
    ps = _non_cash_earnings_per_share(depamor, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d depamor per share times closeadj
def nce_f70_non_cash_earnings_pershare_504d_base_v030_signal(depamor, sharesbas, closeadj):
    ps = _non_cash_earnings_per_share(depamor, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of depamor times closeadj
def nce_f70_non_cash_earnings_std_63d_base_v031_signal(depamor, closeadj):
    result = _std(depamor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of depamor times closeadj
def nce_f70_non_cash_earnings_std_252d_base_v032_signal(depamor, closeadj):
    result = _std(depamor, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of depamor times closeadj
def nce_f70_non_cash_earnings_std_504d_base_v033_signal(depamor, closeadj):
    result = _std(depamor, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of depamor
def nce_f70_non_cash_earnings_z_252d_base_v034_signal(depamor):
    result = _z(depamor, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of depamor
def nce_f70_non_cash_earnings_z_504d_base_v035_signal(depamor):
    result = _z(depamor, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(depamor)
def nce_f70_non_cash_earnings_logz_252d_base_v036_signal(depamor):
    result = _z(_non_cash_earnings_log(depamor), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(depamor)
def nce_f70_non_cash_earnings_logz_504d_base_v037_signal(depamor):
    result = _z(_non_cash_earnings_log(depamor), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of depamor^2 times closeadj
def nce_f70_non_cash_earnings_sq_63d_base_v038_signal(depamor, closeadj):
    result = _mean(depamor * depamor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of depamor^2 times closeadj
def nce_f70_non_cash_earnings_sq_252d_base_v039_signal(depamor, closeadj):
    result = _mean(depamor * depamor, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(depamor) times closeadj
def nce_f70_non_cash_earnings_sign_21d_base_v040_signal(depamor, closeadj):
    result = _mean(np.sign(depamor), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(depamor) times closeadj
def nce_f70_non_cash_earnings_sign_63d_base_v041_signal(depamor, closeadj):
    result = _mean(np.sign(depamor), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(depamor) times closeadj
def nce_f70_non_cash_earnings_sign_252d_base_v042_signal(depamor, closeadj):
    result = _mean(np.sign(depamor), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/opex mean
def nce_f70_non_cash_earnings_per_opex_63d_base_v043_signal(depamor, opex):
    result = _mean(_non_cash_earnings_scaled(depamor, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/opex mean
def nce_f70_non_cash_earnings_per_opex_252d_base_v044_signal(depamor, opex):
    result = _mean(_non_cash_earnings_scaled(depamor, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/ebitda mean
def nce_f70_non_cash_earnings_per_ebitda_63d_base_v045_signal(depamor, ebitda):
    result = _mean(_non_cash_earnings_scaled(depamor, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/ebitda mean
def nce_f70_non_cash_earnings_per_ebitda_252d_base_v046_signal(depamor, ebitda):
    result = _mean(_non_cash_earnings_scaled(depamor, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/capex mean
def nce_f70_non_cash_earnings_per_capex_63d_base_v047_signal(depamor, capex):
    result = _mean(_non_cash_earnings_scaled(depamor, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/capex mean
def nce_f70_non_cash_earnings_per_capex_252d_base_v048_signal(depamor, capex):
    result = _mean(_non_cash_earnings_scaled(depamor, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/liabilities mean
def nce_f70_non_cash_earnings_per_liabilities_63d_base_v049_signal(depamor, liabilities):
    result = _mean(_non_cash_earnings_scaled(depamor, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/liabilities mean
def nce_f70_non_cash_earnings_per_liabilities_252d_base_v050_signal(depamor, liabilities):
    result = _mean(_non_cash_earnings_scaled(depamor, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# depamor relative to 252d max times closeadj
def nce_f70_non_cash_earnings_relmax_252d_base_v051_signal(depamor, closeadj):
    peak = depamor.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (depamor / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# depamor relative to 504d max times closeadj
def nce_f70_non_cash_earnings_relmax_504d_base_v052_signal(depamor, closeadj):
    peak = depamor.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (depamor / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# depamor relative to 252d min times closeadj
def nce_f70_non_cash_earnings_relmin_252d_base_v053_signal(depamor, closeadj):
    trough = depamor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (depamor / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# depamor relative to 504d min times closeadj
def nce_f70_non_cash_earnings_relmin_504d_base_v054_signal(depamor, closeadj):
    trough = depamor.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (depamor / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of depamor times closeadj
def nce_f70_non_cash_earnings_pct_21d_base_v055_signal(depamor, closeadj):
    result = _pct_change(depamor, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of depamor times closeadj
def nce_f70_non_cash_earnings_pct_63d_base_v056_signal(depamor, closeadj):
    result = _pct_change(depamor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of depamor times closeadj
def nce_f70_non_cash_earnings_pct_252d_base_v057_signal(depamor, closeadj):
    result = _pct_change(depamor, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of depamor times closeadj
def nce_f70_non_cash_earnings_sum_63d_base_v058_signal(depamor, closeadj):
    result = depamor.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of depamor times closeadj
def nce_f70_non_cash_earnings_sum_252d_base_v059_signal(depamor, closeadj):
    result = depamor.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of depamor times closeadj
def nce_f70_non_cash_earnings_sum_504d_base_v060_signal(depamor, closeadj):
    result = depamor.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed depamor(63d) / smoothed assets(252d) x closeadj
def nce_f70_non_cash_earnings_rom_assets_252_63d_base_v061_signal(depamor, assets, closeadj):
    n = _mean(depamor, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed depamor(126d) / smoothed assets(504d) x closeadj
def nce_f70_non_cash_earnings_rom_assets_504_126d_base_v062_signal(depamor, assets, closeadj):
    n = _mean(depamor, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed depamor(63d) / smoothed marketcap(252d) x closeadj
def nce_f70_non_cash_earnings_rom_marketcap_252_63d_base_v063_signal(depamor, marketcap, closeadj):
    n = _mean(depamor, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed depamor(126d) / smoothed marketcap(504d) x closeadj
def nce_f70_non_cash_earnings_rom_marketcap_504_126d_base_v064_signal(depamor, marketcap, closeadj):
    n = _mean(depamor, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed depamor(63d) / smoothed equity(252d) x closeadj
def nce_f70_non_cash_earnings_rom_equity_252_63d_base_v065_signal(depamor, equity, closeadj):
    n = _mean(depamor, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed depamor(126d) / smoothed equity(504d) x closeadj
def nce_f70_non_cash_earnings_rom_equity_504_126d_base_v066_signal(depamor, equity, closeadj):
    n = _mean(depamor, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(depamor) / std(assets)
def nce_f70_non_cash_earnings_volratio_assets_252d_base_v067_signal(depamor, assets):
    n = _std(depamor, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(depamor) / std(assets)
def nce_f70_non_cash_earnings_volratio_assets_504d_base_v068_signal(depamor, assets):
    n = _std(depamor, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(depamor) / std(marketcap)
def nce_f70_non_cash_earnings_volratio_marketcap_252d_base_v069_signal(depamor, marketcap):
    n = _std(depamor, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(depamor) / std(marketcap)
def nce_f70_non_cash_earnings_volratio_marketcap_504d_base_v070_signal(depamor, marketcap):
    n = _std(depamor, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed depamor times closeadj
def nce_f70_non_cash_earnings_raw_5d_base_v071_signal(depamor, closeadj):
    result = _mean(depamor, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed depamor times closeadj
def nce_f70_non_cash_earnings_raw_1008d_base_v072_signal(depamor, closeadj):
    result = _mean(depamor, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of depamor/assets
def nce_f70_non_cash_earnings_log_per_assets_252d_base_v073_signal(depamor, assets):
    s = _non_cash_earnings_scaled(depamor, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of depamor/assets
def nce_f70_non_cash_earnings_log_per_assets_504d_base_v074_signal(depamor, assets):
    s = _non_cash_earnings_scaled(depamor, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of depamor/marketcap
def nce_f70_non_cash_earnings_log_per_marketcap_252d_base_v075_signal(depamor, marketcap):
    s = _non_cash_earnings_scaled(depamor, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
