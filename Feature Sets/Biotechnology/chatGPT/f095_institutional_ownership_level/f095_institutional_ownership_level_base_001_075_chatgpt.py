"""Family f095 - Institutional ownership level (Insiders and Ownership) | Sharadar tables: SF3 | fields: calendardate, investorname, value, units, price | base 001-075"""
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
def _institutional_ownership_level_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _institutional_ownership_level_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _institutional_ownership_level_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed calendardate times closeadj
def iol_f095_institutional_ownership_level_raw_21d_base_v001_signal(calendardate, closeadj):
    result = _mean(calendardate, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed calendardate times closeadj
def iol_f095_institutional_ownership_level_raw_63d_base_v002_signal(calendardate, closeadj):
    result = _mean(calendardate, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed calendardate times closeadj
def iol_f095_institutional_ownership_level_raw_126d_base_v003_signal(calendardate, closeadj):
    result = _mean(calendardate, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed calendardate times closeadj
def iol_f095_institutional_ownership_level_raw_252d_base_v004_signal(calendardate, closeadj):
    result = _mean(calendardate, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed calendardate times closeadj
def iol_f095_institutional_ownership_level_raw_504d_base_v005_signal(calendardate, closeadj):
    result = _mean(calendardate, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(calendardate) times closeadj
def iol_f095_institutional_ownership_level_log_21d_base_v006_signal(calendardate, closeadj):
    result = _mean(_institutional_ownership_level_log(calendardate), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(calendardate) times closeadj
def iol_f095_institutional_ownership_level_log_63d_base_v007_signal(calendardate, closeadj):
    result = _mean(_institutional_ownership_level_log(calendardate), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(calendardate) times closeadj
def iol_f095_institutional_ownership_level_log_126d_base_v008_signal(calendardate, closeadj):
    result = _mean(_institutional_ownership_level_log(calendardate), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(calendardate) times closeadj
def iol_f095_institutional_ownership_level_log_252d_base_v009_signal(calendardate, closeadj):
    result = _mean(_institutional_ownership_level_log(calendardate), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(calendardate) times closeadj
def iol_f095_institutional_ownership_level_log_504d_base_v010_signal(calendardate, closeadj):
    result = _mean(_institutional_ownership_level_log(calendardate), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d calendardate/value mean
def iol_f095_institutional_ownership_level_per_value_63d_base_v011_signal(calendardate, value):
    result = _mean(_institutional_ownership_level_scaled(calendardate, value), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d calendardate/value mean
def iol_f095_institutional_ownership_level_per_value_252d_base_v012_signal(calendardate, value):
    result = _mean(_institutional_ownership_level_scaled(calendardate, value), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d calendardate/value mean
def iol_f095_institutional_ownership_level_per_value_504d_base_v013_signal(calendardate, value):
    result = _mean(_institutional_ownership_level_scaled(calendardate, value), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d calendardate/units mean
def iol_f095_institutional_ownership_level_per_units_63d_base_v014_signal(calendardate, units):
    result = _mean(_institutional_ownership_level_scaled(calendardate, units), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d calendardate/units mean
def iol_f095_institutional_ownership_level_per_units_252d_base_v015_signal(calendardate, units):
    result = _mean(_institutional_ownership_level_scaled(calendardate, units), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d calendardate/units mean
def iol_f095_institutional_ownership_level_per_units_504d_base_v016_signal(calendardate, units):
    result = _mean(_institutional_ownership_level_scaled(calendardate, units), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d calendardate/price mean
def iol_f095_institutional_ownership_level_per_price_63d_base_v017_signal(calendardate, price):
    result = _mean(_institutional_ownership_level_scaled(calendardate, price), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d calendardate/price mean
def iol_f095_institutional_ownership_level_per_price_252d_base_v018_signal(calendardate, price):
    result = _mean(_institutional_ownership_level_scaled(calendardate, price), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d calendardate/price mean
def iol_f095_institutional_ownership_level_per_price_504d_base_v019_signal(calendardate, price):
    result = _mean(_institutional_ownership_level_scaled(calendardate, price), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d calendardate/assets mean
def iol_f095_institutional_ownership_level_per_assets_63d_base_v020_signal(calendardate, assets):
    result = _mean(_institutional_ownership_level_scaled(calendardate, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d calendardate/assets mean
def iol_f095_institutional_ownership_level_per_assets_252d_base_v021_signal(calendardate, assets):
    result = _mean(_institutional_ownership_level_scaled(calendardate, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d calendardate/assets mean
def iol_f095_institutional_ownership_level_per_assets_504d_base_v022_signal(calendardate, assets):
    result = _mean(_institutional_ownership_level_scaled(calendardate, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d calendardate/marketcap mean
def iol_f095_institutional_ownership_level_per_marketcap_63d_base_v023_signal(calendardate, marketcap):
    result = _mean(_institutional_ownership_level_scaled(calendardate, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d calendardate/marketcap mean
def iol_f095_institutional_ownership_level_per_marketcap_252d_base_v024_signal(calendardate, marketcap):
    result = _mean(_institutional_ownership_level_scaled(calendardate, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d calendardate/marketcap mean
def iol_f095_institutional_ownership_level_per_marketcap_504d_base_v025_signal(calendardate, marketcap):
    result = _mean(_institutional_ownership_level_scaled(calendardate, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d calendardate per share times closeadj
def iol_f095_institutional_ownership_level_pershare_21d_base_v026_signal(calendardate, sharesbas, closeadj):
    ps = _institutional_ownership_level_per_share(calendardate, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d calendardate per share times closeadj
def iol_f095_institutional_ownership_level_pershare_63d_base_v027_signal(calendardate, sharesbas, closeadj):
    ps = _institutional_ownership_level_per_share(calendardate, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d calendardate per share times closeadj
def iol_f095_institutional_ownership_level_pershare_126d_base_v028_signal(calendardate, sharesbas, closeadj):
    ps = _institutional_ownership_level_per_share(calendardate, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d calendardate per share times closeadj
def iol_f095_institutional_ownership_level_pershare_252d_base_v029_signal(calendardate, sharesbas, closeadj):
    ps = _institutional_ownership_level_per_share(calendardate, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d calendardate per share times closeadj
def iol_f095_institutional_ownership_level_pershare_504d_base_v030_signal(calendardate, sharesbas, closeadj):
    ps = _institutional_ownership_level_per_share(calendardate, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of calendardate times closeadj
def iol_f095_institutional_ownership_level_std_63d_base_v031_signal(calendardate, closeadj):
    result = _std(calendardate, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of calendardate times closeadj
def iol_f095_institutional_ownership_level_std_252d_base_v032_signal(calendardate, closeadj):
    result = _std(calendardate, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of calendardate times closeadj
def iol_f095_institutional_ownership_level_std_504d_base_v033_signal(calendardate, closeadj):
    result = _std(calendardate, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of calendardate
def iol_f095_institutional_ownership_level_z_252d_base_v034_signal(calendardate):
    result = _z(calendardate, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of calendardate
def iol_f095_institutional_ownership_level_z_504d_base_v035_signal(calendardate):
    result = _z(calendardate, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(calendardate)
def iol_f095_institutional_ownership_level_logz_252d_base_v036_signal(calendardate):
    result = _z(_institutional_ownership_level_log(calendardate), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(calendardate)
def iol_f095_institutional_ownership_level_logz_504d_base_v037_signal(calendardate):
    result = _z(_institutional_ownership_level_log(calendardate), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of calendardate^2 times closeadj
def iol_f095_institutional_ownership_level_sq_63d_base_v038_signal(calendardate, closeadj):
    result = _mean(calendardate * calendardate, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of calendardate^2 times closeadj
def iol_f095_institutional_ownership_level_sq_252d_base_v039_signal(calendardate, closeadj):
    result = _mean(calendardate * calendardate, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(calendardate) times closeadj
def iol_f095_institutional_ownership_level_sign_21d_base_v040_signal(calendardate, closeadj):
    result = _mean(np.sign(calendardate), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(calendardate) times closeadj
def iol_f095_institutional_ownership_level_sign_63d_base_v041_signal(calendardate, closeadj):
    result = _mean(np.sign(calendardate), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(calendardate) times closeadj
def iol_f095_institutional_ownership_level_sign_252d_base_v042_signal(calendardate, closeadj):
    result = _mean(np.sign(calendardate), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d calendardate/opex mean
def iol_f095_institutional_ownership_level_per_opex_63d_base_v043_signal(calendardate, opex):
    result = _mean(_institutional_ownership_level_scaled(calendardate, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d calendardate/opex mean
def iol_f095_institutional_ownership_level_per_opex_252d_base_v044_signal(calendardate, opex):
    result = _mean(_institutional_ownership_level_scaled(calendardate, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d calendardate/ebitda mean
def iol_f095_institutional_ownership_level_per_ebitda_63d_base_v045_signal(calendardate, ebitda):
    result = _mean(_institutional_ownership_level_scaled(calendardate, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d calendardate/ebitda mean
def iol_f095_institutional_ownership_level_per_ebitda_252d_base_v046_signal(calendardate, ebitda):
    result = _mean(_institutional_ownership_level_scaled(calendardate, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d calendardate/capex mean
def iol_f095_institutional_ownership_level_per_capex_63d_base_v047_signal(calendardate, capex):
    result = _mean(_institutional_ownership_level_scaled(calendardate, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d calendardate/capex mean
def iol_f095_institutional_ownership_level_per_capex_252d_base_v048_signal(calendardate, capex):
    result = _mean(_institutional_ownership_level_scaled(calendardate, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d calendardate/liabilities mean
def iol_f095_institutional_ownership_level_per_liabilities_63d_base_v049_signal(calendardate, liabilities):
    result = _mean(_institutional_ownership_level_scaled(calendardate, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d calendardate/liabilities mean
def iol_f095_institutional_ownership_level_per_liabilities_252d_base_v050_signal(calendardate, liabilities):
    result = _mean(_institutional_ownership_level_scaled(calendardate, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# calendardate relative to 252d max times closeadj
def iol_f095_institutional_ownership_level_relmax_252d_base_v051_signal(calendardate, closeadj):
    peak = calendardate.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (calendardate / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# calendardate relative to 504d max times closeadj
def iol_f095_institutional_ownership_level_relmax_504d_base_v052_signal(calendardate, closeadj):
    peak = calendardate.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (calendardate / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# calendardate relative to 252d min times closeadj
def iol_f095_institutional_ownership_level_relmin_252d_base_v053_signal(calendardate, closeadj):
    trough = calendardate.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (calendardate / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# calendardate relative to 504d min times closeadj
def iol_f095_institutional_ownership_level_relmin_504d_base_v054_signal(calendardate, closeadj):
    trough = calendardate.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (calendardate / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of calendardate times closeadj
def iol_f095_institutional_ownership_level_pct_21d_base_v055_signal(calendardate, closeadj):
    result = _pct_change(calendardate, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of calendardate times closeadj
def iol_f095_institutional_ownership_level_pct_63d_base_v056_signal(calendardate, closeadj):
    result = _pct_change(calendardate, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of calendardate times closeadj
def iol_f095_institutional_ownership_level_pct_252d_base_v057_signal(calendardate, closeadj):
    result = _pct_change(calendardate, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of calendardate times closeadj
def iol_f095_institutional_ownership_level_sum_63d_base_v058_signal(calendardate, closeadj):
    result = calendardate.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of calendardate times closeadj
def iol_f095_institutional_ownership_level_sum_252d_base_v059_signal(calendardate, closeadj):
    result = calendardate.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of calendardate times closeadj
def iol_f095_institutional_ownership_level_sum_504d_base_v060_signal(calendardate, closeadj):
    result = calendardate.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed calendardate(63d) / smoothed value(252d) x closeadj
def iol_f095_institutional_ownership_level_rom_value_252_63d_base_v061_signal(calendardate, value, closeadj):
    n = _mean(calendardate, 63)
    d = _mean(value, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed calendardate(126d) / smoothed value(504d) x closeadj
def iol_f095_institutional_ownership_level_rom_value_504_126d_base_v062_signal(calendardate, value, closeadj):
    n = _mean(calendardate, 126)
    d = _mean(value, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed calendardate(63d) / smoothed units(252d) x closeadj
def iol_f095_institutional_ownership_level_rom_units_252_63d_base_v063_signal(calendardate, units, closeadj):
    n = _mean(calendardate, 63)
    d = _mean(units, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed calendardate(126d) / smoothed units(504d) x closeadj
def iol_f095_institutional_ownership_level_rom_units_504_126d_base_v064_signal(calendardate, units, closeadj):
    n = _mean(calendardate, 126)
    d = _mean(units, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed calendardate(63d) / smoothed price(252d) x closeadj
def iol_f095_institutional_ownership_level_rom_price_252_63d_base_v065_signal(calendardate, price, closeadj):
    n = _mean(calendardate, 63)
    d = _mean(price, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed calendardate(126d) / smoothed price(504d) x closeadj
def iol_f095_institutional_ownership_level_rom_price_504_126d_base_v066_signal(calendardate, price, closeadj):
    n = _mean(calendardate, 126)
    d = _mean(price, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(calendardate) / std(value)
def iol_f095_institutional_ownership_level_volratio_value_252d_base_v067_signal(calendardate, value):
    n = _std(calendardate, 252)
    d = _std(value, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(calendardate) / std(value)
def iol_f095_institutional_ownership_level_volratio_value_504d_base_v068_signal(calendardate, value):
    n = _std(calendardate, 504)
    d = _std(value, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(calendardate) / std(units)
def iol_f095_institutional_ownership_level_volratio_units_252d_base_v069_signal(calendardate, units):
    n = _std(calendardate, 252)
    d = _std(units, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(calendardate) / std(units)
def iol_f095_institutional_ownership_level_volratio_units_504d_base_v070_signal(calendardate, units):
    n = _std(calendardate, 504)
    d = _std(units, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed calendardate times closeadj
def iol_f095_institutional_ownership_level_raw_5d_base_v071_signal(calendardate, closeadj):
    result = _mean(calendardate, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed calendardate times closeadj
def iol_f095_institutional_ownership_level_raw_1008d_base_v072_signal(calendardate, closeadj):
    result = _mean(calendardate, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of calendardate/value
def iol_f095_institutional_ownership_level_log_per_value_252d_base_v073_signal(calendardate, value):
    s = _institutional_ownership_level_scaled(calendardate, value)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of calendardate/value
def iol_f095_institutional_ownership_level_log_per_value_504d_base_v074_signal(calendardate, value):
    s = _institutional_ownership_level_scaled(calendardate, value)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of calendardate/units
def iol_f095_institutional_ownership_level_log_per_units_252d_base_v075_signal(calendardate, units):
    s = _institutional_ownership_level_scaled(calendardate, units)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
