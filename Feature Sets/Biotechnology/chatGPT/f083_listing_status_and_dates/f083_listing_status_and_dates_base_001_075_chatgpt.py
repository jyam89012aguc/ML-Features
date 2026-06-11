"""Family f083 - Listing lifecycle and delisting context (Security Master and Universe) | Sharadar tables: TICKERS | fields: isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter | base 001-075"""
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
def _listing_status_and_dates_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _listing_status_and_dates_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _listing_status_and_dates_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed listingage times closeadj
def lsad_f083_listing_status_and_dates_raw_21d_base_v001_signal(listingage, closeadj):
    result = _mean(listingage, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed listingage times closeadj
def lsad_f083_listing_status_and_dates_raw_63d_base_v002_signal(listingage, closeadj):
    result = _mean(listingage, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed listingage times closeadj
def lsad_f083_listing_status_and_dates_raw_126d_base_v003_signal(listingage, closeadj):
    result = _mean(listingage, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed listingage times closeadj
def lsad_f083_listing_status_and_dates_raw_252d_base_v004_signal(listingage, closeadj):
    result = _mean(listingage, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed listingage times closeadj
def lsad_f083_listing_status_and_dates_raw_504d_base_v005_signal(listingage, closeadj):
    result = _mean(listingage, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(listingage) times closeadj
def lsad_f083_listing_status_and_dates_log_21d_base_v006_signal(listingage, closeadj):
    result = _mean(_listing_status_and_dates_log(listingage), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(listingage) times closeadj
def lsad_f083_listing_status_and_dates_log_63d_base_v007_signal(listingage, closeadj):
    result = _mean(_listing_status_and_dates_log(listingage), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(listingage) times closeadj
def lsad_f083_listing_status_and_dates_log_126d_base_v008_signal(listingage, closeadj):
    result = _mean(_listing_status_and_dates_log(listingage), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(listingage) times closeadj
def lsad_f083_listing_status_and_dates_log_252d_base_v009_signal(listingage, closeadj):
    result = _mean(_listing_status_and_dates_log(listingage), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(listingage) times closeadj
def lsad_f083_listing_status_and_dates_log_504d_base_v010_signal(listingage, closeadj):
    result = _mean(_listing_status_and_dates_log(listingage), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d listingage/assets mean
def lsad_f083_listing_status_and_dates_per_assets_63d_base_v011_signal(listingage, assets):
    result = _mean(_listing_status_and_dates_scaled(listingage, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d listingage/assets mean
def lsad_f083_listing_status_and_dates_per_assets_252d_base_v012_signal(listingage, assets):
    result = _mean(_listing_status_and_dates_scaled(listingage, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d listingage/assets mean
def lsad_f083_listing_status_and_dates_per_assets_504d_base_v013_signal(listingage, assets):
    result = _mean(_listing_status_and_dates_scaled(listingage, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d listingage/marketcap mean
def lsad_f083_listing_status_and_dates_per_marketcap_63d_base_v014_signal(listingage, marketcap):
    result = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d listingage/marketcap mean
def lsad_f083_listing_status_and_dates_per_marketcap_252d_base_v015_signal(listingage, marketcap):
    result = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d listingage/marketcap mean
def lsad_f083_listing_status_and_dates_per_marketcap_504d_base_v016_signal(listingage, marketcap):
    result = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d listingage/equity mean
def lsad_f083_listing_status_and_dates_per_equity_63d_base_v017_signal(listingage, equity):
    result = _mean(_listing_status_and_dates_scaled(listingage, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d listingage/equity mean
def lsad_f083_listing_status_and_dates_per_equity_252d_base_v018_signal(listingage, equity):
    result = _mean(_listing_status_and_dates_scaled(listingage, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d listingage/equity mean
def lsad_f083_listing_status_and_dates_per_equity_504d_base_v019_signal(listingage, equity):
    result = _mean(_listing_status_and_dates_scaled(listingage, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d listingage/debt mean
def lsad_f083_listing_status_and_dates_per_debt_63d_base_v020_signal(listingage, debt):
    result = _mean(_listing_status_and_dates_scaled(listingage, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d listingage/debt mean
def lsad_f083_listing_status_and_dates_per_debt_252d_base_v021_signal(listingage, debt):
    result = _mean(_listing_status_and_dates_scaled(listingage, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d listingage/debt mean
def lsad_f083_listing_status_and_dates_per_debt_504d_base_v022_signal(listingage, debt):
    result = _mean(_listing_status_and_dates_scaled(listingage, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d listingage/revenue mean
def lsad_f083_listing_status_and_dates_per_revenue_63d_base_v023_signal(listingage, revenue):
    result = _mean(_listing_status_and_dates_scaled(listingage, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d listingage/revenue mean
def lsad_f083_listing_status_and_dates_per_revenue_252d_base_v024_signal(listingage, revenue):
    result = _mean(_listing_status_and_dates_scaled(listingage, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d listingage/revenue mean
def lsad_f083_listing_status_and_dates_per_revenue_504d_base_v025_signal(listingage, revenue):
    result = _mean(_listing_status_and_dates_scaled(listingage, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d listingage per share times closeadj
def lsad_f083_listing_status_and_dates_pershare_21d_base_v026_signal(listingage, sharesbas, closeadj):
    ps = _listing_status_and_dates_per_share(listingage, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d listingage per share times closeadj
def lsad_f083_listing_status_and_dates_pershare_63d_base_v027_signal(listingage, sharesbas, closeadj):
    ps = _listing_status_and_dates_per_share(listingage, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d listingage per share times closeadj
def lsad_f083_listing_status_and_dates_pershare_126d_base_v028_signal(listingage, sharesbas, closeadj):
    ps = _listing_status_and_dates_per_share(listingage, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d listingage per share times closeadj
def lsad_f083_listing_status_and_dates_pershare_252d_base_v029_signal(listingage, sharesbas, closeadj):
    ps = _listing_status_and_dates_per_share(listingage, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d listingage per share times closeadj
def lsad_f083_listing_status_and_dates_pershare_504d_base_v030_signal(listingage, sharesbas, closeadj):
    ps = _listing_status_and_dates_per_share(listingage, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of listingage times closeadj
def lsad_f083_listing_status_and_dates_std_63d_base_v031_signal(listingage, closeadj):
    result = _std(listingage, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of listingage times closeadj
def lsad_f083_listing_status_and_dates_std_252d_base_v032_signal(listingage, closeadj):
    result = _std(listingage, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of listingage times closeadj
def lsad_f083_listing_status_and_dates_std_504d_base_v033_signal(listingage, closeadj):
    result = _std(listingage, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of listingage
def lsad_f083_listing_status_and_dates_z_252d_base_v034_signal(listingage):
    result = _z(listingage, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of listingage
def lsad_f083_listing_status_and_dates_z_504d_base_v035_signal(listingage):
    result = _z(listingage, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(listingage)
def lsad_f083_listing_status_and_dates_logz_252d_base_v036_signal(listingage):
    result = _z(_listing_status_and_dates_log(listingage), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(listingage)
def lsad_f083_listing_status_and_dates_logz_504d_base_v037_signal(listingage):
    result = _z(_listing_status_and_dates_log(listingage), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of listingage^2 times closeadj
def lsad_f083_listing_status_and_dates_sq_63d_base_v038_signal(listingage, closeadj):
    result = _mean(listingage * listingage, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of listingage^2 times closeadj
def lsad_f083_listing_status_and_dates_sq_252d_base_v039_signal(listingage, closeadj):
    result = _mean(listingage * listingage, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(listingage) times closeadj
def lsad_f083_listing_status_and_dates_sign_21d_base_v040_signal(listingage, closeadj):
    result = _mean(np.sign(listingage), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(listingage) times closeadj
def lsad_f083_listing_status_and_dates_sign_63d_base_v041_signal(listingage, closeadj):
    result = _mean(np.sign(listingage), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(listingage) times closeadj
def lsad_f083_listing_status_and_dates_sign_252d_base_v042_signal(listingage, closeadj):
    result = _mean(np.sign(listingage), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d listingage/opex mean
def lsad_f083_listing_status_and_dates_per_opex_63d_base_v043_signal(listingage, opex):
    result = _mean(_listing_status_and_dates_scaled(listingage, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d listingage/opex mean
def lsad_f083_listing_status_and_dates_per_opex_252d_base_v044_signal(listingage, opex):
    result = _mean(_listing_status_and_dates_scaled(listingage, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d listingage/ebitda mean
def lsad_f083_listing_status_and_dates_per_ebitda_63d_base_v045_signal(listingage, ebitda):
    result = _mean(_listing_status_and_dates_scaled(listingage, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d listingage/ebitda mean
def lsad_f083_listing_status_and_dates_per_ebitda_252d_base_v046_signal(listingage, ebitda):
    result = _mean(_listing_status_and_dates_scaled(listingage, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d listingage/capex mean
def lsad_f083_listing_status_and_dates_per_capex_63d_base_v047_signal(listingage, capex):
    result = _mean(_listing_status_and_dates_scaled(listingage, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d listingage/capex mean
def lsad_f083_listing_status_and_dates_per_capex_252d_base_v048_signal(listingage, capex):
    result = _mean(_listing_status_and_dates_scaled(listingage, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d listingage/liabilities mean
def lsad_f083_listing_status_and_dates_per_liabilities_63d_base_v049_signal(listingage, liabilities):
    result = _mean(_listing_status_and_dates_scaled(listingage, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d listingage/liabilities mean
def lsad_f083_listing_status_and_dates_per_liabilities_252d_base_v050_signal(listingage, liabilities):
    result = _mean(_listing_status_and_dates_scaled(listingage, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# listingage relative to 252d max times closeadj
def lsad_f083_listing_status_and_dates_relmax_252d_base_v051_signal(listingage, closeadj):
    peak = listingage.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (listingage / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# listingage relative to 504d max times closeadj
def lsad_f083_listing_status_and_dates_relmax_504d_base_v052_signal(listingage, closeadj):
    peak = listingage.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (listingage / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# listingage relative to 252d min times closeadj
def lsad_f083_listing_status_and_dates_relmin_252d_base_v053_signal(listingage, closeadj):
    trough = listingage.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (listingage / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# listingage relative to 504d min times closeadj
def lsad_f083_listing_status_and_dates_relmin_504d_base_v054_signal(listingage, closeadj):
    trough = listingage.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (listingage / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of listingage times closeadj
def lsad_f083_listing_status_and_dates_pct_21d_base_v055_signal(listingage, closeadj):
    result = _pct_change(listingage, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of listingage times closeadj
def lsad_f083_listing_status_and_dates_pct_63d_base_v056_signal(listingage, closeadj):
    result = _pct_change(listingage, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of listingage times closeadj
def lsad_f083_listing_status_and_dates_pct_252d_base_v057_signal(listingage, closeadj):
    result = _pct_change(listingage, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of listingage times closeadj
def lsad_f083_listing_status_and_dates_sum_63d_base_v058_signal(listingage, closeadj):
    result = listingage.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of listingage times closeadj
def lsad_f083_listing_status_and_dates_sum_252d_base_v059_signal(listingage, closeadj):
    result = listingage.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of listingage times closeadj
def lsad_f083_listing_status_and_dates_sum_504d_base_v060_signal(listingage, closeadj):
    result = listingage.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed listingage(63d) / smoothed assets(252d) x closeadj
def lsad_f083_listing_status_and_dates_rom_assets_252_63d_base_v061_signal(listingage, assets, closeadj):
    n = _mean(listingage, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed listingage(126d) / smoothed assets(504d) x closeadj
def lsad_f083_listing_status_and_dates_rom_assets_504_126d_base_v062_signal(listingage, assets, closeadj):
    n = _mean(listingage, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed listingage(63d) / smoothed marketcap(252d) x closeadj
def lsad_f083_listing_status_and_dates_rom_marketcap_252_63d_base_v063_signal(listingage, marketcap, closeadj):
    n = _mean(listingage, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed listingage(126d) / smoothed marketcap(504d) x closeadj
def lsad_f083_listing_status_and_dates_rom_marketcap_504_126d_base_v064_signal(listingage, marketcap, closeadj):
    n = _mean(listingage, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed listingage(63d) / smoothed equity(252d) x closeadj
def lsad_f083_listing_status_and_dates_rom_equity_252_63d_base_v065_signal(listingage, equity, closeadj):
    n = _mean(listingage, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed listingage(126d) / smoothed equity(504d) x closeadj
def lsad_f083_listing_status_and_dates_rom_equity_504_126d_base_v066_signal(listingage, equity, closeadj):
    n = _mean(listingage, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(listingage) / std(assets)
def lsad_f083_listing_status_and_dates_volratio_assets_252d_base_v067_signal(listingage, assets):
    n = _std(listingage, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(listingage) / std(assets)
def lsad_f083_listing_status_and_dates_volratio_assets_504d_base_v068_signal(listingage, assets):
    n = _std(listingage, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(listingage) / std(marketcap)
def lsad_f083_listing_status_and_dates_volratio_marketcap_252d_base_v069_signal(listingage, marketcap):
    n = _std(listingage, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(listingage) / std(marketcap)
def lsad_f083_listing_status_and_dates_volratio_marketcap_504d_base_v070_signal(listingage, marketcap):
    n = _std(listingage, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed listingage times closeadj
def lsad_f083_listing_status_and_dates_raw_5d_base_v071_signal(listingage, closeadj):
    result = _mean(listingage, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed listingage times closeadj
def lsad_f083_listing_status_and_dates_raw_1008d_base_v072_signal(listingage, closeadj):
    result = _mean(listingage, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of listingage/assets
def lsad_f083_listing_status_and_dates_log_per_assets_252d_base_v073_signal(listingage, assets):
    s = _listing_status_and_dates_scaled(listingage, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of listingage/assets
def lsad_f083_listing_status_and_dates_log_per_assets_504d_base_v074_signal(listingage, assets):
    s = _listing_status_and_dates_scaled(listingage, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of listingage/marketcap
def lsad_f083_listing_status_and_dates_log_per_marketcap_252d_base_v075_signal(listingage, marketcap):
    s = _listing_status_and_dates_scaled(listingage, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
