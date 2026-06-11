"""Family f084 - Identifier continuity (Security Master and Universe) | Sharadar tables: TICKERS | fields: ticker, permaticker, relatedtickers, table, currency | base 001-075"""
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
def _ticker_changes_and_permaticker_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ticker_changes_and_permaticker_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ticker_changes_and_permaticker_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_raw_21d_base_v001_signal(ticker_change_count, closeadj):
    result = _mean(ticker_change_count, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_raw_63d_base_v002_signal(ticker_change_count, closeadj):
    result = _mean(ticker_change_count, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_raw_126d_base_v003_signal(ticker_change_count, closeadj):
    result = _mean(ticker_change_count, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_raw_252d_base_v004_signal(ticker_change_count, closeadj):
    result = _mean(ticker_change_count, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_raw_504d_base_v005_signal(ticker_change_count, closeadj):
    result = _mean(ticker_change_count, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(ticker_change_count) times closeadj
def tcap_f084_ticker_changes_and_permaticker_log_21d_base_v006_signal(ticker_change_count, closeadj):
    result = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(ticker_change_count) times closeadj
def tcap_f084_ticker_changes_and_permaticker_log_63d_base_v007_signal(ticker_change_count, closeadj):
    result = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(ticker_change_count) times closeadj
def tcap_f084_ticker_changes_and_permaticker_log_126d_base_v008_signal(ticker_change_count, closeadj):
    result = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(ticker_change_count) times closeadj
def tcap_f084_ticker_changes_and_permaticker_log_252d_base_v009_signal(ticker_change_count, closeadj):
    result = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(ticker_change_count) times closeadj
def tcap_f084_ticker_changes_and_permaticker_log_504d_base_v010_signal(ticker_change_count, closeadj):
    result = _mean(_ticker_changes_and_permaticker_log(ticker_change_count), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ticker_change_count/assets mean
def tcap_f084_ticker_changes_and_permaticker_per_assets_63d_base_v011_signal(ticker_change_count, assets):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ticker_change_count/assets mean
def tcap_f084_ticker_changes_and_permaticker_per_assets_252d_base_v012_signal(ticker_change_count, assets):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ticker_change_count/assets mean
def tcap_f084_ticker_changes_and_permaticker_per_assets_504d_base_v013_signal(ticker_change_count, assets):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ticker_change_count/marketcap mean
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_63d_base_v014_signal(ticker_change_count, marketcap):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ticker_change_count/marketcap mean
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_252d_base_v015_signal(ticker_change_count, marketcap):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ticker_change_count/marketcap mean
def tcap_f084_ticker_changes_and_permaticker_per_marketcap_504d_base_v016_signal(ticker_change_count, marketcap):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ticker_change_count/equity mean
def tcap_f084_ticker_changes_and_permaticker_per_equity_63d_base_v017_signal(ticker_change_count, equity):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ticker_change_count/equity mean
def tcap_f084_ticker_changes_and_permaticker_per_equity_252d_base_v018_signal(ticker_change_count, equity):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ticker_change_count/equity mean
def tcap_f084_ticker_changes_and_permaticker_per_equity_504d_base_v019_signal(ticker_change_count, equity):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ticker_change_count/debt mean
def tcap_f084_ticker_changes_and_permaticker_per_debt_63d_base_v020_signal(ticker_change_count, debt):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ticker_change_count/debt mean
def tcap_f084_ticker_changes_and_permaticker_per_debt_252d_base_v021_signal(ticker_change_count, debt):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ticker_change_count/debt mean
def tcap_f084_ticker_changes_and_permaticker_per_debt_504d_base_v022_signal(ticker_change_count, debt):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ticker_change_count/revenue mean
def tcap_f084_ticker_changes_and_permaticker_per_revenue_63d_base_v023_signal(ticker_change_count, revenue):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ticker_change_count/revenue mean
def tcap_f084_ticker_changes_and_permaticker_per_revenue_252d_base_v024_signal(ticker_change_count, revenue):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ticker_change_count/revenue mean
def tcap_f084_ticker_changes_and_permaticker_per_revenue_504d_base_v025_signal(ticker_change_count, revenue):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ticker_change_count per share times closeadj
def tcap_f084_ticker_changes_and_permaticker_pershare_21d_base_v026_signal(ticker_change_count, sharesbas, closeadj):
    ps = _ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ticker_change_count per share times closeadj
def tcap_f084_ticker_changes_and_permaticker_pershare_63d_base_v027_signal(ticker_change_count, sharesbas, closeadj):
    ps = _ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ticker_change_count per share times closeadj
def tcap_f084_ticker_changes_and_permaticker_pershare_126d_base_v028_signal(ticker_change_count, sharesbas, closeadj):
    ps = _ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ticker_change_count per share times closeadj
def tcap_f084_ticker_changes_and_permaticker_pershare_252d_base_v029_signal(ticker_change_count, sharesbas, closeadj):
    ps = _ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ticker_change_count per share times closeadj
def tcap_f084_ticker_changes_and_permaticker_pershare_504d_base_v030_signal(ticker_change_count, sharesbas, closeadj):
    ps = _ticker_changes_and_permaticker_per_share(ticker_change_count, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_std_63d_base_v031_signal(ticker_change_count, closeadj):
    result = _std(ticker_change_count, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_std_252d_base_v032_signal(ticker_change_count, closeadj):
    result = _std(ticker_change_count, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_std_504d_base_v033_signal(ticker_change_count, closeadj):
    result = _std(ticker_change_count, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_252d_base_v034_signal(ticker_change_count):
    result = _z(ticker_change_count, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of ticker_change_count
def tcap_f084_ticker_changes_and_permaticker_z_504d_base_v035_signal(ticker_change_count):
    result = _z(ticker_change_count, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(ticker_change_count)
def tcap_f084_ticker_changes_and_permaticker_logz_252d_base_v036_signal(ticker_change_count):
    result = _z(_ticker_changes_and_permaticker_log(ticker_change_count), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(ticker_change_count)
def tcap_f084_ticker_changes_and_permaticker_logz_504d_base_v037_signal(ticker_change_count):
    result = _z(_ticker_changes_and_permaticker_log(ticker_change_count), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of ticker_change_count^2 times closeadj
def tcap_f084_ticker_changes_and_permaticker_sq_63d_base_v038_signal(ticker_change_count, closeadj):
    result = _mean(ticker_change_count * ticker_change_count, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of ticker_change_count^2 times closeadj
def tcap_f084_ticker_changes_and_permaticker_sq_252d_base_v039_signal(ticker_change_count, closeadj):
    result = _mean(ticker_change_count * ticker_change_count, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(ticker_change_count) times closeadj
def tcap_f084_ticker_changes_and_permaticker_sign_21d_base_v040_signal(ticker_change_count, closeadj):
    result = _mean(np.sign(ticker_change_count), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(ticker_change_count) times closeadj
def tcap_f084_ticker_changes_and_permaticker_sign_63d_base_v041_signal(ticker_change_count, closeadj):
    result = _mean(np.sign(ticker_change_count), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(ticker_change_count) times closeadj
def tcap_f084_ticker_changes_and_permaticker_sign_252d_base_v042_signal(ticker_change_count, closeadj):
    result = _mean(np.sign(ticker_change_count), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ticker_change_count/opex mean
def tcap_f084_ticker_changes_and_permaticker_per_opex_63d_base_v043_signal(ticker_change_count, opex):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ticker_change_count/opex mean
def tcap_f084_ticker_changes_and_permaticker_per_opex_252d_base_v044_signal(ticker_change_count, opex):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ticker_change_count/ebitda mean
def tcap_f084_ticker_changes_and_permaticker_per_ebitda_63d_base_v045_signal(ticker_change_count, ebitda):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ticker_change_count/ebitda mean
def tcap_f084_ticker_changes_and_permaticker_per_ebitda_252d_base_v046_signal(ticker_change_count, ebitda):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ticker_change_count/capex mean
def tcap_f084_ticker_changes_and_permaticker_per_capex_63d_base_v047_signal(ticker_change_count, capex):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ticker_change_count/capex mean
def tcap_f084_ticker_changes_and_permaticker_per_capex_252d_base_v048_signal(ticker_change_count, capex):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ticker_change_count/liabilities mean
def tcap_f084_ticker_changes_and_permaticker_per_liabilities_63d_base_v049_signal(ticker_change_count, liabilities):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ticker_change_count/liabilities mean
def tcap_f084_ticker_changes_and_permaticker_per_liabilities_252d_base_v050_signal(ticker_change_count, liabilities):
    result = _mean(_ticker_changes_and_permaticker_scaled(ticker_change_count, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ticker_change_count relative to 252d max times closeadj
def tcap_f084_ticker_changes_and_permaticker_relmax_252d_base_v051_signal(ticker_change_count, closeadj):
    peak = ticker_change_count.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (ticker_change_count / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ticker_change_count relative to 504d max times closeadj
def tcap_f084_ticker_changes_and_permaticker_relmax_504d_base_v052_signal(ticker_change_count, closeadj):
    peak = ticker_change_count.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (ticker_change_count / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ticker_change_count relative to 252d min times closeadj
def tcap_f084_ticker_changes_and_permaticker_relmin_252d_base_v053_signal(ticker_change_count, closeadj):
    trough = ticker_change_count.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (ticker_change_count / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ticker_change_count relative to 504d min times closeadj
def tcap_f084_ticker_changes_and_permaticker_relmin_504d_base_v054_signal(ticker_change_count, closeadj):
    trough = ticker_change_count.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (ticker_change_count / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_pct_21d_base_v055_signal(ticker_change_count, closeadj):
    result = _pct_change(ticker_change_count, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_pct_63d_base_v056_signal(ticker_change_count, closeadj):
    result = _pct_change(ticker_change_count, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_pct_252d_base_v057_signal(ticker_change_count, closeadj):
    result = _pct_change(ticker_change_count, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_sum_63d_base_v058_signal(ticker_change_count, closeadj):
    result = ticker_change_count.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_sum_252d_base_v059_signal(ticker_change_count, closeadj):
    result = ticker_change_count.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_sum_504d_base_v060_signal(ticker_change_count, closeadj):
    result = ticker_change_count.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ticker_change_count(63d) / smoothed assets(252d) x closeadj
def tcap_f084_ticker_changes_and_permaticker_rom_assets_252_63d_base_v061_signal(ticker_change_count, assets, closeadj):
    n = _mean(ticker_change_count, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ticker_change_count(126d) / smoothed assets(504d) x closeadj
def tcap_f084_ticker_changes_and_permaticker_rom_assets_504_126d_base_v062_signal(ticker_change_count, assets, closeadj):
    n = _mean(ticker_change_count, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ticker_change_count(63d) / smoothed marketcap(252d) x closeadj
def tcap_f084_ticker_changes_and_permaticker_rom_marketcap_252_63d_base_v063_signal(ticker_change_count, marketcap, closeadj):
    n = _mean(ticker_change_count, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ticker_change_count(126d) / smoothed marketcap(504d) x closeadj
def tcap_f084_ticker_changes_and_permaticker_rom_marketcap_504_126d_base_v064_signal(ticker_change_count, marketcap, closeadj):
    n = _mean(ticker_change_count, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ticker_change_count(63d) / smoothed equity(252d) x closeadj
def tcap_f084_ticker_changes_and_permaticker_rom_equity_252_63d_base_v065_signal(ticker_change_count, equity, closeadj):
    n = _mean(ticker_change_count, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ticker_change_count(126d) / smoothed equity(504d) x closeadj
def tcap_f084_ticker_changes_and_permaticker_rom_equity_504_126d_base_v066_signal(ticker_change_count, equity, closeadj):
    n = _mean(ticker_change_count, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ticker_change_count) / std(assets)
def tcap_f084_ticker_changes_and_permaticker_volratio_assets_252d_base_v067_signal(ticker_change_count, assets):
    n = _std(ticker_change_count, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ticker_change_count) / std(assets)
def tcap_f084_ticker_changes_and_permaticker_volratio_assets_504d_base_v068_signal(ticker_change_count, assets):
    n = _std(ticker_change_count, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ticker_change_count) / std(marketcap)
def tcap_f084_ticker_changes_and_permaticker_volratio_marketcap_252d_base_v069_signal(ticker_change_count, marketcap):
    n = _std(ticker_change_count, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ticker_change_count) / std(marketcap)
def tcap_f084_ticker_changes_and_permaticker_volratio_marketcap_504d_base_v070_signal(ticker_change_count, marketcap):
    n = _std(ticker_change_count, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_raw_5d_base_v071_signal(ticker_change_count, closeadj):
    result = _mean(ticker_change_count, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed ticker_change_count times closeadj
def tcap_f084_ticker_changes_and_permaticker_raw_1008d_base_v072_signal(ticker_change_count, closeadj):
    result = _mean(ticker_change_count, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ticker_change_count/assets
def tcap_f084_ticker_changes_and_permaticker_log_per_assets_252d_base_v073_signal(ticker_change_count, assets):
    s = _ticker_changes_and_permaticker_scaled(ticker_change_count, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ticker_change_count/assets
def tcap_f084_ticker_changes_and_permaticker_log_per_assets_504d_base_v074_signal(ticker_change_count, assets):
    s = _ticker_changes_and_permaticker_scaled(ticker_change_count, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ticker_change_count/marketcap
def tcap_f084_ticker_changes_and_permaticker_log_per_marketcap_252d_base_v075_signal(ticker_change_count, marketcap):
    s = _ticker_changes_and_permaticker_scaled(ticker_change_count, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
