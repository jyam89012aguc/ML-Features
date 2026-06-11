"""Family f92 - Specialist-fund participation  (P_Institutional_SF3) | base 001-075"""
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
def _specialist_funds_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _specialist_funds_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _specialist_funds_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed value times closeadj
def spf_f92_specialist_funds_raw_21d_base_v001_signal(value, closeadj):
    result = _mean(value, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed value times closeadj
def spf_f92_specialist_funds_raw_63d_base_v002_signal(value, closeadj):
    result = _mean(value, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed value times closeadj
def spf_f92_specialist_funds_raw_126d_base_v003_signal(value, closeadj):
    result = _mean(value, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed value times closeadj
def spf_f92_specialist_funds_raw_252d_base_v004_signal(value, closeadj):
    result = _mean(value, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed value times closeadj
def spf_f92_specialist_funds_raw_504d_base_v005_signal(value, closeadj):
    result = _mean(value, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(value) times closeadj
def spf_f92_specialist_funds_log_21d_base_v006_signal(value, closeadj):
    result = _mean(_specialist_funds_log(value), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(value) times closeadj
def spf_f92_specialist_funds_log_63d_base_v007_signal(value, closeadj):
    result = _mean(_specialist_funds_log(value), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(value) times closeadj
def spf_f92_specialist_funds_log_126d_base_v008_signal(value, closeadj):
    result = _mean(_specialist_funds_log(value), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(value) times closeadj
def spf_f92_specialist_funds_log_252d_base_v009_signal(value, closeadj):
    result = _mean(_specialist_funds_log(value), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(value) times closeadj
def spf_f92_specialist_funds_log_504d_base_v010_signal(value, closeadj):
    result = _mean(_specialist_funds_log(value), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/assets mean
def spf_f92_specialist_funds_per_assets_63d_base_v011_signal(value, assets):
    result = _mean(_specialist_funds_scaled(value, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/assets mean
def spf_f92_specialist_funds_per_assets_252d_base_v012_signal(value, assets):
    result = _mean(_specialist_funds_scaled(value, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d value/assets mean
def spf_f92_specialist_funds_per_assets_504d_base_v013_signal(value, assets):
    result = _mean(_specialist_funds_scaled(value, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/marketcap mean
def spf_f92_specialist_funds_per_marketcap_63d_base_v014_signal(value, marketcap):
    result = _mean(_specialist_funds_scaled(value, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/marketcap mean
def spf_f92_specialist_funds_per_marketcap_252d_base_v015_signal(value, marketcap):
    result = _mean(_specialist_funds_scaled(value, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d value/marketcap mean
def spf_f92_specialist_funds_per_marketcap_504d_base_v016_signal(value, marketcap):
    result = _mean(_specialist_funds_scaled(value, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/equity mean
def spf_f92_specialist_funds_per_equity_63d_base_v017_signal(value, equity):
    result = _mean(_specialist_funds_scaled(value, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/equity mean
def spf_f92_specialist_funds_per_equity_252d_base_v018_signal(value, equity):
    result = _mean(_specialist_funds_scaled(value, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d value/equity mean
def spf_f92_specialist_funds_per_equity_504d_base_v019_signal(value, equity):
    result = _mean(_specialist_funds_scaled(value, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/debt mean
def spf_f92_specialist_funds_per_debt_63d_base_v020_signal(value, debt):
    result = _mean(_specialist_funds_scaled(value, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/debt mean
def spf_f92_specialist_funds_per_debt_252d_base_v021_signal(value, debt):
    result = _mean(_specialist_funds_scaled(value, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d value/debt mean
def spf_f92_specialist_funds_per_debt_504d_base_v022_signal(value, debt):
    result = _mean(_specialist_funds_scaled(value, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/revenue mean
def spf_f92_specialist_funds_per_revenue_63d_base_v023_signal(value, revenue):
    result = _mean(_specialist_funds_scaled(value, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/revenue mean
def spf_f92_specialist_funds_per_revenue_252d_base_v024_signal(value, revenue):
    result = _mean(_specialist_funds_scaled(value, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d value/revenue mean
def spf_f92_specialist_funds_per_revenue_504d_base_v025_signal(value, revenue):
    result = _mean(_specialist_funds_scaled(value, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d value per share times closeadj
def spf_f92_specialist_funds_pershare_21d_base_v026_signal(value, sharesbas, closeadj):
    ps = _specialist_funds_per_share(value, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value per share times closeadj
def spf_f92_specialist_funds_pershare_63d_base_v027_signal(value, sharesbas, closeadj):
    ps = _specialist_funds_per_share(value, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d value per share times closeadj
def spf_f92_specialist_funds_pershare_126d_base_v028_signal(value, sharesbas, closeadj):
    ps = _specialist_funds_per_share(value, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value per share times closeadj
def spf_f92_specialist_funds_pershare_252d_base_v029_signal(value, sharesbas, closeadj):
    ps = _specialist_funds_per_share(value, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d value per share times closeadj
def spf_f92_specialist_funds_pershare_504d_base_v030_signal(value, sharesbas, closeadj):
    ps = _specialist_funds_per_share(value, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of value times closeadj
def spf_f92_specialist_funds_std_63d_base_v031_signal(value, closeadj):
    result = _std(value, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of value times closeadj
def spf_f92_specialist_funds_std_252d_base_v032_signal(value, closeadj):
    result = _std(value, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of value times closeadj
def spf_f92_specialist_funds_std_504d_base_v033_signal(value, closeadj):
    result = _std(value, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of value
def spf_f92_specialist_funds_z_252d_base_v034_signal(value):
    result = _z(value, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of value
def spf_f92_specialist_funds_z_504d_base_v035_signal(value):
    result = _z(value, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(value)
def spf_f92_specialist_funds_logz_252d_base_v036_signal(value):
    result = _z(_specialist_funds_log(value), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(value)
def spf_f92_specialist_funds_logz_504d_base_v037_signal(value):
    result = _z(_specialist_funds_log(value), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of value^2 times closeadj
def spf_f92_specialist_funds_sq_63d_base_v038_signal(value, closeadj):
    result = _mean(value * value, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of value^2 times closeadj
def spf_f92_specialist_funds_sq_252d_base_v039_signal(value, closeadj):
    result = _mean(value * value, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(value) times closeadj
def spf_f92_specialist_funds_sign_21d_base_v040_signal(value, closeadj):
    result = _mean(np.sign(value), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(value) times closeadj
def spf_f92_specialist_funds_sign_63d_base_v041_signal(value, closeadj):
    result = _mean(np.sign(value), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(value) times closeadj
def spf_f92_specialist_funds_sign_252d_base_v042_signal(value, closeadj):
    result = _mean(np.sign(value), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/opex mean
def spf_f92_specialist_funds_per_opex_63d_base_v043_signal(value, opex):
    result = _mean(_specialist_funds_scaled(value, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/opex mean
def spf_f92_specialist_funds_per_opex_252d_base_v044_signal(value, opex):
    result = _mean(_specialist_funds_scaled(value, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/ebitda mean
def spf_f92_specialist_funds_per_ebitda_63d_base_v045_signal(value, ebitda):
    result = _mean(_specialist_funds_scaled(value, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/ebitda mean
def spf_f92_specialist_funds_per_ebitda_252d_base_v046_signal(value, ebitda):
    result = _mean(_specialist_funds_scaled(value, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/capex mean
def spf_f92_specialist_funds_per_capex_63d_base_v047_signal(value, capex):
    result = _mean(_specialist_funds_scaled(value, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/capex mean
def spf_f92_specialist_funds_per_capex_252d_base_v048_signal(value, capex):
    result = _mean(_specialist_funds_scaled(value, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d value/liabilities mean
def spf_f92_specialist_funds_per_liabilities_63d_base_v049_signal(value, liabilities):
    result = _mean(_specialist_funds_scaled(value, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d value/liabilities mean
def spf_f92_specialist_funds_per_liabilities_252d_base_v050_signal(value, liabilities):
    result = _mean(_specialist_funds_scaled(value, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# value relative to 252d max times closeadj
def spf_f92_specialist_funds_relmax_252d_base_v051_signal(value, closeadj):
    peak = value.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (value / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# value relative to 504d max times closeadj
def spf_f92_specialist_funds_relmax_504d_base_v052_signal(value, closeadj):
    peak = value.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (value / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# value relative to 252d min times closeadj
def spf_f92_specialist_funds_relmin_252d_base_v053_signal(value, closeadj):
    trough = value.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (value / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# value relative to 504d min times closeadj
def spf_f92_specialist_funds_relmin_504d_base_v054_signal(value, closeadj):
    trough = value.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (value / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of value times closeadj
def spf_f92_specialist_funds_pct_21d_base_v055_signal(value, closeadj):
    result = _pct_change(value, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of value times closeadj
def spf_f92_specialist_funds_pct_63d_base_v056_signal(value, closeadj):
    result = _pct_change(value, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of value times closeadj
def spf_f92_specialist_funds_pct_252d_base_v057_signal(value, closeadj):
    result = _pct_change(value, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of value times closeadj
def spf_f92_specialist_funds_sum_63d_base_v058_signal(value, closeadj):
    result = value.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of value times closeadj
def spf_f92_specialist_funds_sum_252d_base_v059_signal(value, closeadj):
    result = value.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of value times closeadj
def spf_f92_specialist_funds_sum_504d_base_v060_signal(value, closeadj):
    result = value.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed value(63d) / smoothed assets(252d) x closeadj
def spf_f92_specialist_funds_rom_assets_252_63d_base_v061_signal(value, assets, closeadj):
    n = _mean(value, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed value(126d) / smoothed assets(504d) x closeadj
def spf_f92_specialist_funds_rom_assets_504_126d_base_v062_signal(value, assets, closeadj):
    n = _mean(value, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed value(63d) / smoothed marketcap(252d) x closeadj
def spf_f92_specialist_funds_rom_marketcap_252_63d_base_v063_signal(value, marketcap, closeadj):
    n = _mean(value, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed value(126d) / smoothed marketcap(504d) x closeadj
def spf_f92_specialist_funds_rom_marketcap_504_126d_base_v064_signal(value, marketcap, closeadj):
    n = _mean(value, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed value(63d) / smoothed equity(252d) x closeadj
def spf_f92_specialist_funds_rom_equity_252_63d_base_v065_signal(value, equity, closeadj):
    n = _mean(value, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed value(126d) / smoothed equity(504d) x closeadj
def spf_f92_specialist_funds_rom_equity_504_126d_base_v066_signal(value, equity, closeadj):
    n = _mean(value, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(value) / std(assets)
def spf_f92_specialist_funds_volratio_assets_252d_base_v067_signal(value, assets):
    n = _std(value, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(value) / std(assets)
def spf_f92_specialist_funds_volratio_assets_504d_base_v068_signal(value, assets):
    n = _std(value, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(value) / std(marketcap)
def spf_f92_specialist_funds_volratio_marketcap_252d_base_v069_signal(value, marketcap):
    n = _std(value, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(value) / std(marketcap)
def spf_f92_specialist_funds_volratio_marketcap_504d_base_v070_signal(value, marketcap):
    n = _std(value, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed value times closeadj
def spf_f92_specialist_funds_raw_5d_base_v071_signal(value, closeadj):
    result = _mean(value, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed value times closeadj
def spf_f92_specialist_funds_raw_1008d_base_v072_signal(value, closeadj):
    result = _mean(value, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of value/assets
def spf_f92_specialist_funds_log_per_assets_252d_base_v073_signal(value, assets):
    s = _specialist_funds_scaled(value, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of value/assets
def spf_f92_specialist_funds_log_per_assets_504d_base_v074_signal(value, assets):
    s = _specialist_funds_scaled(value, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of value/marketcap
def spf_f92_specialist_funds_log_per_marketcap_252d_base_v075_signal(value, marketcap):
    s = _specialist_funds_scaled(value, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
