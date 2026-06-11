"""Family f096 - Holder concentration and turnover (Insiders and Ownership) | Sharadar tables: SF3,SF3A,SF3B | fields: investorname, value, units, calendardate | base 001-075"""
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
def _holder_concentration_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _holder_concentration_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _holder_concentration_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed value times closeadj
def hc_f096_holder_concentration_raw_21d_base_v001_signal(value, closeadj):
    result = _mean(value, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed value times closeadj
def hc_f096_holder_concentration_raw_63d_base_v002_signal(value, closeadj):
    result = _mean(value, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed value times closeadj
def hc_f096_holder_concentration_raw_126d_base_v003_signal(value, closeadj):
    result = _mean(value, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed value times closeadj
def hc_f096_holder_concentration_raw_252d_base_v004_signal(value, closeadj):
    result = _mean(value, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed value times closeadj
def hc_f096_holder_concentration_raw_504d_base_v005_signal(value, closeadj):
    result = _mean(value, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(value) times closeadj
def hc_f096_holder_concentration_log_21d_base_v006_signal(value, closeadj):
    result = _mean(_holder_concentration_log(value), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(value) times closeadj
def hc_f096_holder_concentration_log_63d_base_v007_signal(value, closeadj):
    result = _mean(_holder_concentration_log(value), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(value) times closeadj
def hc_f096_holder_concentration_log_126d_base_v008_signal(value, closeadj):
    result = _mean(_holder_concentration_log(value), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(value) times closeadj
def hc_f096_holder_concentration_log_252d_base_v009_signal(value, closeadj):
    result = _mean(_holder_concentration_log(value), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(value) times closeadj
def hc_f096_holder_concentration_log_504d_base_v010_signal(value, closeadj):
    result = _mean(_holder_concentration_log(value), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/units mean
def hc_f096_holder_concentration_per_units_63d_base_v011_signal(value, units):
    result = _mean(_holder_concentration_scaled(value, units), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/units mean
def hc_f096_holder_concentration_per_units_252d_base_v012_signal(value, units):
    result = _mean(_holder_concentration_scaled(value, units), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d value/units mean
def hc_f096_holder_concentration_per_units_504d_base_v013_signal(value, units):
    result = _mean(_holder_concentration_scaled(value, units), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/calendardate mean
def hc_f096_holder_concentration_per_calendardate_63d_base_v014_signal(value, calendardate):
    result = _mean(_holder_concentration_scaled(value, calendardate), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/calendardate mean
def hc_f096_holder_concentration_per_calendardate_252d_base_v015_signal(value, calendardate):
    result = _mean(_holder_concentration_scaled(value, calendardate), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d value/calendardate mean
def hc_f096_holder_concentration_per_calendardate_504d_base_v016_signal(value, calendardate):
    result = _mean(_holder_concentration_scaled(value, calendardate), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/assets mean
def hc_f096_holder_concentration_per_assets_63d_base_v017_signal(value, assets):
    result = _mean(_holder_concentration_scaled(value, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/assets mean
def hc_f096_holder_concentration_per_assets_252d_base_v018_signal(value, assets):
    result = _mean(_holder_concentration_scaled(value, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d value/assets mean
def hc_f096_holder_concentration_per_assets_504d_base_v019_signal(value, assets):
    result = _mean(_holder_concentration_scaled(value, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/marketcap mean
def hc_f096_holder_concentration_per_marketcap_63d_base_v020_signal(value, marketcap):
    result = _mean(_holder_concentration_scaled(value, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/marketcap mean
def hc_f096_holder_concentration_per_marketcap_252d_base_v021_signal(value, marketcap):
    result = _mean(_holder_concentration_scaled(value, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d value/marketcap mean
def hc_f096_holder_concentration_per_marketcap_504d_base_v022_signal(value, marketcap):
    result = _mean(_holder_concentration_scaled(value, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/equity mean
def hc_f096_holder_concentration_per_equity_63d_base_v023_signal(value, equity):
    result = _mean(_holder_concentration_scaled(value, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/equity mean
def hc_f096_holder_concentration_per_equity_252d_base_v024_signal(value, equity):
    result = _mean(_holder_concentration_scaled(value, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d value/equity mean
def hc_f096_holder_concentration_per_equity_504d_base_v025_signal(value, equity):
    result = _mean(_holder_concentration_scaled(value, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d value per share times closeadj
def hc_f096_holder_concentration_pershare_21d_base_v026_signal(value, sharesbas, closeadj):
    ps = _holder_concentration_per_share(value, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value per share times closeadj
def hc_f096_holder_concentration_pershare_63d_base_v027_signal(value, sharesbas, closeadj):
    ps = _holder_concentration_per_share(value, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d value per share times closeadj
def hc_f096_holder_concentration_pershare_126d_base_v028_signal(value, sharesbas, closeadj):
    ps = _holder_concentration_per_share(value, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value per share times closeadj
def hc_f096_holder_concentration_pershare_252d_base_v029_signal(value, sharesbas, closeadj):
    ps = _holder_concentration_per_share(value, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d value per share times closeadj
def hc_f096_holder_concentration_pershare_504d_base_v030_signal(value, sharesbas, closeadj):
    ps = _holder_concentration_per_share(value, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of value times closeadj
def hc_f096_holder_concentration_std_63d_base_v031_signal(value, closeadj):
    result = _std(value, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of value times closeadj
def hc_f096_holder_concentration_std_252d_base_v032_signal(value, closeadj):
    result = _std(value, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of value times closeadj
def hc_f096_holder_concentration_std_504d_base_v033_signal(value, closeadj):
    result = _std(value, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of value
def hc_f096_holder_concentration_z_252d_base_v034_signal(value):
    result = _z(value, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of value
def hc_f096_holder_concentration_z_504d_base_v035_signal(value):
    result = _z(value, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(value)
def hc_f096_holder_concentration_logz_252d_base_v036_signal(value):
    result = _z(_holder_concentration_log(value), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(value)
def hc_f096_holder_concentration_logz_504d_base_v037_signal(value):
    result = _z(_holder_concentration_log(value), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of value^2 times closeadj
def hc_f096_holder_concentration_sq_63d_base_v038_signal(value, closeadj):
    result = _mean(value * value, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of value^2 times closeadj
def hc_f096_holder_concentration_sq_252d_base_v039_signal(value, closeadj):
    result = _mean(value * value, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(value) times closeadj
def hc_f096_holder_concentration_sign_21d_base_v040_signal(value, closeadj):
    result = _mean(np.sign(value), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(value) times closeadj
def hc_f096_holder_concentration_sign_63d_base_v041_signal(value, closeadj):
    result = _mean(np.sign(value), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(value) times closeadj
def hc_f096_holder_concentration_sign_252d_base_v042_signal(value, closeadj):
    result = _mean(np.sign(value), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/opex mean
def hc_f096_holder_concentration_per_opex_63d_base_v043_signal(value, opex):
    result = _mean(_holder_concentration_scaled(value, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/opex mean
def hc_f096_holder_concentration_per_opex_252d_base_v044_signal(value, opex):
    result = _mean(_holder_concentration_scaled(value, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/ebitda mean
def hc_f096_holder_concentration_per_ebitda_63d_base_v045_signal(value, ebitda):
    result = _mean(_holder_concentration_scaled(value, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/ebitda mean
def hc_f096_holder_concentration_per_ebitda_252d_base_v046_signal(value, ebitda):
    result = _mean(_holder_concentration_scaled(value, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/capex mean
def hc_f096_holder_concentration_per_capex_63d_base_v047_signal(value, capex):
    result = _mean(_holder_concentration_scaled(value, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/capex mean
def hc_f096_holder_concentration_per_capex_252d_base_v048_signal(value, capex):
    result = _mean(_holder_concentration_scaled(value, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/liabilities mean
def hc_f096_holder_concentration_per_liabilities_63d_base_v049_signal(value, liabilities):
    result = _mean(_holder_concentration_scaled(value, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/liabilities mean
def hc_f096_holder_concentration_per_liabilities_252d_base_v050_signal(value, liabilities):
    result = _mean(_holder_concentration_scaled(value, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# value relative to 252d max times closeadj
def hc_f096_holder_concentration_relmax_252d_base_v051_signal(value, closeadj):
    peak = value.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (value / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# value relative to 504d max times closeadj
def hc_f096_holder_concentration_relmax_504d_base_v052_signal(value, closeadj):
    peak = value.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (value / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# value relative to 252d min times closeadj
def hc_f096_holder_concentration_relmin_252d_base_v053_signal(value, closeadj):
    trough = value.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (value / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# value relative to 504d min times closeadj
def hc_f096_holder_concentration_relmin_504d_base_v054_signal(value, closeadj):
    trough = value.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (value / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of value times closeadj
def hc_f096_holder_concentration_pct_21d_base_v055_signal(value, closeadj):
    result = _pct_change(value, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of value times closeadj
def hc_f096_holder_concentration_pct_63d_base_v056_signal(value, closeadj):
    result = _pct_change(value, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of value times closeadj
def hc_f096_holder_concentration_pct_252d_base_v057_signal(value, closeadj):
    result = _pct_change(value, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of value times closeadj
def hc_f096_holder_concentration_sum_63d_base_v058_signal(value, closeadj):
    result = value.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of value times closeadj
def hc_f096_holder_concentration_sum_252d_base_v059_signal(value, closeadj):
    result = value.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of value times closeadj
def hc_f096_holder_concentration_sum_504d_base_v060_signal(value, closeadj):
    result = value.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed value(63d) / smoothed units(252d) x closeadj
def hc_f096_holder_concentration_rom_units_252_63d_base_v061_signal(value, units, closeadj):
    n = _mean(value, 63)
    d = _mean(units, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed value(126d) / smoothed units(504d) x closeadj
def hc_f096_holder_concentration_rom_units_504_126d_base_v062_signal(value, units, closeadj):
    n = _mean(value, 126)
    d = _mean(units, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed value(63d) / smoothed calendardate(252d) x closeadj
def hc_f096_holder_concentration_rom_calendardate_252_63d_base_v063_signal(value, calendardate, closeadj):
    n = _mean(value, 63)
    d = _mean(calendardate, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed value(126d) / smoothed calendardate(504d) x closeadj
def hc_f096_holder_concentration_rom_calendardate_504_126d_base_v064_signal(value, calendardate, closeadj):
    n = _mean(value, 126)
    d = _mean(calendardate, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed value(63d) / smoothed assets(252d) x closeadj
def hc_f096_holder_concentration_rom_assets_252_63d_base_v065_signal(value, assets, closeadj):
    n = _mean(value, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed value(126d) / smoothed assets(504d) x closeadj
def hc_f096_holder_concentration_rom_assets_504_126d_base_v066_signal(value, assets, closeadj):
    n = _mean(value, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(value) / std(units)
def hc_f096_holder_concentration_volratio_units_252d_base_v067_signal(value, units):
    n = _std(value, 252)
    d = _std(units, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(value) / std(units)
def hc_f096_holder_concentration_volratio_units_504d_base_v068_signal(value, units):
    n = _std(value, 504)
    d = _std(units, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(value) / std(calendardate)
def hc_f096_holder_concentration_volratio_calendardate_252d_base_v069_signal(value, calendardate):
    n = _std(value, 252)
    d = _std(calendardate, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(value) / std(calendardate)
def hc_f096_holder_concentration_volratio_calendardate_504d_base_v070_signal(value, calendardate):
    n = _std(value, 504)
    d = _std(calendardate, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed value times closeadj
def hc_f096_holder_concentration_raw_5d_base_v071_signal(value, closeadj):
    result = _mean(value, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed value times closeadj
def hc_f096_holder_concentration_raw_1008d_base_v072_signal(value, closeadj):
    result = _mean(value, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of value/units
def hc_f096_holder_concentration_log_per_units_252d_base_v073_signal(value, units):
    s = _holder_concentration_scaled(value, units)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of value/units
def hc_f096_holder_concentration_log_per_units_504d_base_v074_signal(value, units):
    s = _holder_concentration_scaled(value, units)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of value/calendardate
def hc_f096_holder_concentration_log_per_calendardate_252d_base_v075_signal(value, calendardate):
    s = _holder_concentration_scaled(value, calendardate)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
