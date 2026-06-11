"""Family f12 - Financing cash flow / capital raised  (B_CashFlow_Burn) | base 001-075"""
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
def _capital_raised_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _capital_raised_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _capital_raised_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed ncff times closeadj
def cap_f12_capital_raised_raw_21d_base_v001_signal(ncff, closeadj):
    result = _mean(ncff, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed ncff times closeadj
def cap_f12_capital_raised_raw_63d_base_v002_signal(ncff, closeadj):
    result = _mean(ncff, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed ncff times closeadj
def cap_f12_capital_raised_raw_126d_base_v003_signal(ncff, closeadj):
    result = _mean(ncff, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed ncff times closeadj
def cap_f12_capital_raised_raw_252d_base_v004_signal(ncff, closeadj):
    result = _mean(ncff, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed ncff times closeadj
def cap_f12_capital_raised_raw_504d_base_v005_signal(ncff, closeadj):
    result = _mean(ncff, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(ncff) times closeadj
def cap_f12_capital_raised_log_21d_base_v006_signal(ncff, closeadj):
    result = _mean(_capital_raised_log(ncff), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(ncff) times closeadj
def cap_f12_capital_raised_log_63d_base_v007_signal(ncff, closeadj):
    result = _mean(_capital_raised_log(ncff), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(ncff) times closeadj
def cap_f12_capital_raised_log_126d_base_v008_signal(ncff, closeadj):
    result = _mean(_capital_raised_log(ncff), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(ncff) times closeadj
def cap_f12_capital_raised_log_252d_base_v009_signal(ncff, closeadj):
    result = _mean(_capital_raised_log(ncff), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(ncff) times closeadj
def cap_f12_capital_raised_log_504d_base_v010_signal(ncff, closeadj):
    result = _mean(_capital_raised_log(ncff), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/assets mean
def cap_f12_capital_raised_per_assets_63d_base_v011_signal(ncff, assets):
    result = _mean(_capital_raised_scaled(ncff, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/assets mean
def cap_f12_capital_raised_per_assets_252d_base_v012_signal(ncff, assets):
    result = _mean(_capital_raised_scaled(ncff, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff/assets mean
def cap_f12_capital_raised_per_assets_504d_base_v013_signal(ncff, assets):
    result = _mean(_capital_raised_scaled(ncff, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/marketcap mean
def cap_f12_capital_raised_per_marketcap_63d_base_v014_signal(ncff, marketcap):
    result = _mean(_capital_raised_scaled(ncff, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/marketcap mean
def cap_f12_capital_raised_per_marketcap_252d_base_v015_signal(ncff, marketcap):
    result = _mean(_capital_raised_scaled(ncff, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff/marketcap mean
def cap_f12_capital_raised_per_marketcap_504d_base_v016_signal(ncff, marketcap):
    result = _mean(_capital_raised_scaled(ncff, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/equity mean
def cap_f12_capital_raised_per_equity_63d_base_v017_signal(ncff, equity):
    result = _mean(_capital_raised_scaled(ncff, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/equity mean
def cap_f12_capital_raised_per_equity_252d_base_v018_signal(ncff, equity):
    result = _mean(_capital_raised_scaled(ncff, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff/equity mean
def cap_f12_capital_raised_per_equity_504d_base_v019_signal(ncff, equity):
    result = _mean(_capital_raised_scaled(ncff, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/debt mean
def cap_f12_capital_raised_per_debt_63d_base_v020_signal(ncff, debt):
    result = _mean(_capital_raised_scaled(ncff, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/debt mean
def cap_f12_capital_raised_per_debt_252d_base_v021_signal(ncff, debt):
    result = _mean(_capital_raised_scaled(ncff, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff/debt mean
def cap_f12_capital_raised_per_debt_504d_base_v022_signal(ncff, debt):
    result = _mean(_capital_raised_scaled(ncff, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/revenue mean
def cap_f12_capital_raised_per_revenue_63d_base_v023_signal(ncff, revenue):
    result = _mean(_capital_raised_scaled(ncff, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/revenue mean
def cap_f12_capital_raised_per_revenue_252d_base_v024_signal(ncff, revenue):
    result = _mean(_capital_raised_scaled(ncff, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff/revenue mean
def cap_f12_capital_raised_per_revenue_504d_base_v025_signal(ncff, revenue):
    result = _mean(_capital_raised_scaled(ncff, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncff per share times closeadj
def cap_f12_capital_raised_pershare_21d_base_v026_signal(ncff, sharesbas, closeadj):
    ps = _capital_raised_per_share(ncff, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff per share times closeadj
def cap_f12_capital_raised_pershare_63d_base_v027_signal(ncff, sharesbas, closeadj):
    ps = _capital_raised_per_share(ncff, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ncff per share times closeadj
def cap_f12_capital_raised_pershare_126d_base_v028_signal(ncff, sharesbas, closeadj):
    ps = _capital_raised_per_share(ncff, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff per share times closeadj
def cap_f12_capital_raised_pershare_252d_base_v029_signal(ncff, sharesbas, closeadj):
    ps = _capital_raised_per_share(ncff, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff per share times closeadj
def cap_f12_capital_raised_pershare_504d_base_v030_signal(ncff, sharesbas, closeadj):
    ps = _capital_raised_per_share(ncff, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of ncff times closeadj
def cap_f12_capital_raised_std_63d_base_v031_signal(ncff, closeadj):
    result = _std(ncff, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of ncff times closeadj
def cap_f12_capital_raised_std_252d_base_v032_signal(ncff, closeadj):
    result = _std(ncff, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of ncff times closeadj
def cap_f12_capital_raised_std_504d_base_v033_signal(ncff, closeadj):
    result = _std(ncff, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of ncff
def cap_f12_capital_raised_z_252d_base_v034_signal(ncff):
    result = _z(ncff, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of ncff
def cap_f12_capital_raised_z_504d_base_v035_signal(ncff):
    result = _z(ncff, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(ncff)
def cap_f12_capital_raised_logz_252d_base_v036_signal(ncff):
    result = _z(_capital_raised_log(ncff), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(ncff)
def cap_f12_capital_raised_logz_504d_base_v037_signal(ncff):
    result = _z(_capital_raised_log(ncff), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of ncff^2 times closeadj
def cap_f12_capital_raised_sq_63d_base_v038_signal(ncff, closeadj):
    result = _mean(ncff * ncff, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of ncff^2 times closeadj
def cap_f12_capital_raised_sq_252d_base_v039_signal(ncff, closeadj):
    result = _mean(ncff * ncff, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(ncff) times closeadj
def cap_f12_capital_raised_sign_21d_base_v040_signal(ncff, closeadj):
    result = _mean(np.sign(ncff), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(ncff) times closeadj
def cap_f12_capital_raised_sign_63d_base_v041_signal(ncff, closeadj):
    result = _mean(np.sign(ncff), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(ncff) times closeadj
def cap_f12_capital_raised_sign_252d_base_v042_signal(ncff, closeadj):
    result = _mean(np.sign(ncff), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/opex mean
def cap_f12_capital_raised_per_opex_63d_base_v043_signal(ncff, opex):
    result = _mean(_capital_raised_scaled(ncff, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/opex mean
def cap_f12_capital_raised_per_opex_252d_base_v044_signal(ncff, opex):
    result = _mean(_capital_raised_scaled(ncff, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/ebitda mean
def cap_f12_capital_raised_per_ebitda_63d_base_v045_signal(ncff, ebitda):
    result = _mean(_capital_raised_scaled(ncff, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/ebitda mean
def cap_f12_capital_raised_per_ebitda_252d_base_v046_signal(ncff, ebitda):
    result = _mean(_capital_raised_scaled(ncff, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/capex mean
def cap_f12_capital_raised_per_capex_63d_base_v047_signal(ncff, capex):
    result = _mean(_capital_raised_scaled(ncff, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/capex mean
def cap_f12_capital_raised_per_capex_252d_base_v048_signal(ncff, capex):
    result = _mean(_capital_raised_scaled(ncff, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/liabilities mean
def cap_f12_capital_raised_per_liabilities_63d_base_v049_signal(ncff, liabilities):
    result = _mean(_capital_raised_scaled(ncff, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/liabilities mean
def cap_f12_capital_raised_per_liabilities_252d_base_v050_signal(ncff, liabilities):
    result = _mean(_capital_raised_scaled(ncff, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ncff relative to 252d max times closeadj
def cap_f12_capital_raised_relmax_252d_base_v051_signal(ncff, closeadj):
    peak = ncff.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (ncff / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncff relative to 504d max times closeadj
def cap_f12_capital_raised_relmax_504d_base_v052_signal(ncff, closeadj):
    peak = ncff.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (ncff / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncff relative to 252d min times closeadj
def cap_f12_capital_raised_relmin_252d_base_v053_signal(ncff, closeadj):
    trough = ncff.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (ncff / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncff relative to 504d min times closeadj
def cap_f12_capital_raised_relmin_504d_base_v054_signal(ncff, closeadj):
    trough = ncff.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (ncff / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of ncff times closeadj
def cap_f12_capital_raised_pct_21d_base_v055_signal(ncff, closeadj):
    result = _pct_change(ncff, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of ncff times closeadj
def cap_f12_capital_raised_pct_63d_base_v056_signal(ncff, closeadj):
    result = _pct_change(ncff, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of ncff times closeadj
def cap_f12_capital_raised_pct_252d_base_v057_signal(ncff, closeadj):
    result = _pct_change(ncff, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of ncff times closeadj
def cap_f12_capital_raised_sum_63d_base_v058_signal(ncff, closeadj):
    result = ncff.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of ncff times closeadj
def cap_f12_capital_raised_sum_252d_base_v059_signal(ncff, closeadj):
    result = ncff.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of ncff times closeadj
def cap_f12_capital_raised_sum_504d_base_v060_signal(ncff, closeadj):
    result = ncff.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncff(63d) / smoothed assets(252d) x closeadj
def cap_f12_capital_raised_rom_assets_252_63d_base_v061_signal(ncff, assets, closeadj):
    n = _mean(ncff, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncff(126d) / smoothed assets(504d) x closeadj
def cap_f12_capital_raised_rom_assets_504_126d_base_v062_signal(ncff, assets, closeadj):
    n = _mean(ncff, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncff(63d) / smoothed marketcap(252d) x closeadj
def cap_f12_capital_raised_rom_marketcap_252_63d_base_v063_signal(ncff, marketcap, closeadj):
    n = _mean(ncff, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncff(126d) / smoothed marketcap(504d) x closeadj
def cap_f12_capital_raised_rom_marketcap_504_126d_base_v064_signal(ncff, marketcap, closeadj):
    n = _mean(ncff, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncff(63d) / smoothed equity(252d) x closeadj
def cap_f12_capital_raised_rom_equity_252_63d_base_v065_signal(ncff, equity, closeadj):
    n = _mean(ncff, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncff(126d) / smoothed equity(504d) x closeadj
def cap_f12_capital_raised_rom_equity_504_126d_base_v066_signal(ncff, equity, closeadj):
    n = _mean(ncff, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ncff) / std(assets)
def cap_f12_capital_raised_volratio_assets_252d_base_v067_signal(ncff, assets):
    n = _std(ncff, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ncff) / std(assets)
def cap_f12_capital_raised_volratio_assets_504d_base_v068_signal(ncff, assets):
    n = _std(ncff, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ncff) / std(marketcap)
def cap_f12_capital_raised_volratio_marketcap_252d_base_v069_signal(ncff, marketcap):
    n = _std(ncff, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ncff) / std(marketcap)
def cap_f12_capital_raised_volratio_marketcap_504d_base_v070_signal(ncff, marketcap):
    n = _std(ncff, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed ncff times closeadj
def cap_f12_capital_raised_raw_5d_base_v071_signal(ncff, closeadj):
    result = _mean(ncff, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed ncff times closeadj
def cap_f12_capital_raised_raw_1008d_base_v072_signal(ncff, closeadj):
    result = _mean(ncff, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ncff/assets
def cap_f12_capital_raised_log_per_assets_252d_base_v073_signal(ncff, assets):
    s = _capital_raised_scaled(ncff, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ncff/assets
def cap_f12_capital_raised_log_per_assets_504d_base_v074_signal(ncff, assets):
    s = _capital_raised_scaled(ncff, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ncff/marketcap
def cap_f12_capital_raised_log_per_marketcap_252d_base_v075_signal(ncff, marketcap):
    s = _capital_raised_scaled(ncff, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
