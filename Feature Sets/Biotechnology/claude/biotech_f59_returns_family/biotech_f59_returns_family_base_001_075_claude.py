"""Family f59 - ROA / ROE / ROIC  (J_Returns_Efficiency) | base 001-075"""
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
def _returns_family_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _returns_family_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _returns_family_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed roa times closeadj
def rf_f59_returns_family_raw_21d_base_v001_signal(roa, closeadj):
    result = _mean(roa, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed roa times closeadj
def rf_f59_returns_family_raw_63d_base_v002_signal(roa, closeadj):
    result = _mean(roa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed roa times closeadj
def rf_f59_returns_family_raw_126d_base_v003_signal(roa, closeadj):
    result = _mean(roa, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed roa times closeadj
def rf_f59_returns_family_raw_252d_base_v004_signal(roa, closeadj):
    result = _mean(roa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed roa times closeadj
def rf_f59_returns_family_raw_504d_base_v005_signal(roa, closeadj):
    result = _mean(roa, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(roa) times closeadj
def rf_f59_returns_family_log_21d_base_v006_signal(roa, closeadj):
    result = _mean(_returns_family_log(roa), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(roa) times closeadj
def rf_f59_returns_family_log_63d_base_v007_signal(roa, closeadj):
    result = _mean(_returns_family_log(roa), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(roa) times closeadj
def rf_f59_returns_family_log_126d_base_v008_signal(roa, closeadj):
    result = _mean(_returns_family_log(roa), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(roa) times closeadj
def rf_f59_returns_family_log_252d_base_v009_signal(roa, closeadj):
    result = _mean(_returns_family_log(roa), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(roa) times closeadj
def rf_f59_returns_family_log_504d_base_v010_signal(roa, closeadj):
    result = _mean(_returns_family_log(roa), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roa/assets mean
def rf_f59_returns_family_per_assets_63d_base_v011_signal(roa, assets):
    result = _mean(_returns_family_scaled(roa, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roa/assets mean
def rf_f59_returns_family_per_assets_252d_base_v012_signal(roa, assets):
    result = _mean(_returns_family_scaled(roa, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roa/assets mean
def rf_f59_returns_family_per_assets_504d_base_v013_signal(roa, assets):
    result = _mean(_returns_family_scaled(roa, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roa/marketcap mean
def rf_f59_returns_family_per_marketcap_63d_base_v014_signal(roa, marketcap):
    result = _mean(_returns_family_scaled(roa, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roa/marketcap mean
def rf_f59_returns_family_per_marketcap_252d_base_v015_signal(roa, marketcap):
    result = _mean(_returns_family_scaled(roa, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roa/marketcap mean
def rf_f59_returns_family_per_marketcap_504d_base_v016_signal(roa, marketcap):
    result = _mean(_returns_family_scaled(roa, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roa/equity mean
def rf_f59_returns_family_per_equity_63d_base_v017_signal(roa, equity):
    result = _mean(_returns_family_scaled(roa, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roa/equity mean
def rf_f59_returns_family_per_equity_252d_base_v018_signal(roa, equity):
    result = _mean(_returns_family_scaled(roa, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roa/equity mean
def rf_f59_returns_family_per_equity_504d_base_v019_signal(roa, equity):
    result = _mean(_returns_family_scaled(roa, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roa/debt mean
def rf_f59_returns_family_per_debt_63d_base_v020_signal(roa, debt):
    result = _mean(_returns_family_scaled(roa, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roa/debt mean
def rf_f59_returns_family_per_debt_252d_base_v021_signal(roa, debt):
    result = _mean(_returns_family_scaled(roa, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roa/debt mean
def rf_f59_returns_family_per_debt_504d_base_v022_signal(roa, debt):
    result = _mean(_returns_family_scaled(roa, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roa/revenue mean
def rf_f59_returns_family_per_revenue_63d_base_v023_signal(roa, revenue):
    result = _mean(_returns_family_scaled(roa, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roa/revenue mean
def rf_f59_returns_family_per_revenue_252d_base_v024_signal(roa, revenue):
    result = _mean(_returns_family_scaled(roa, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roa/revenue mean
def rf_f59_returns_family_per_revenue_504d_base_v025_signal(roa, revenue):
    result = _mean(_returns_family_scaled(roa, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d roa per share times closeadj
def rf_f59_returns_family_pershare_21d_base_v026_signal(roa, sharesbas, closeadj):
    ps = _returns_family_per_share(roa, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roa per share times closeadj
def rf_f59_returns_family_pershare_63d_base_v027_signal(roa, sharesbas, closeadj):
    ps = _returns_family_per_share(roa, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d roa per share times closeadj
def rf_f59_returns_family_pershare_126d_base_v028_signal(roa, sharesbas, closeadj):
    ps = _returns_family_per_share(roa, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roa per share times closeadj
def rf_f59_returns_family_pershare_252d_base_v029_signal(roa, sharesbas, closeadj):
    ps = _returns_family_per_share(roa, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roa per share times closeadj
def rf_f59_returns_family_pershare_504d_base_v030_signal(roa, sharesbas, closeadj):
    ps = _returns_family_per_share(roa, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of roa times closeadj
def rf_f59_returns_family_std_63d_base_v031_signal(roa, closeadj):
    result = _std(roa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of roa times closeadj
def rf_f59_returns_family_std_252d_base_v032_signal(roa, closeadj):
    result = _std(roa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of roa times closeadj
def rf_f59_returns_family_std_504d_base_v033_signal(roa, closeadj):
    result = _std(roa, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of roa
def rf_f59_returns_family_z_252d_base_v034_signal(roa):
    result = _z(roa, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of roa
def rf_f59_returns_family_z_504d_base_v035_signal(roa):
    result = _z(roa, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(roa)
def rf_f59_returns_family_logz_252d_base_v036_signal(roa):
    result = _z(_returns_family_log(roa), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(roa)
def rf_f59_returns_family_logz_504d_base_v037_signal(roa):
    result = _z(_returns_family_log(roa), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of roa^2 times closeadj
def rf_f59_returns_family_sq_63d_base_v038_signal(roa, closeadj):
    result = _mean(roa * roa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of roa^2 times closeadj
def rf_f59_returns_family_sq_252d_base_v039_signal(roa, closeadj):
    result = _mean(roa * roa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(roa) times closeadj
def rf_f59_returns_family_sign_21d_base_v040_signal(roa, closeadj):
    result = _mean(np.sign(roa), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(roa) times closeadj
def rf_f59_returns_family_sign_63d_base_v041_signal(roa, closeadj):
    result = _mean(np.sign(roa), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(roa) times closeadj
def rf_f59_returns_family_sign_252d_base_v042_signal(roa, closeadj):
    result = _mean(np.sign(roa), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roa/opex mean
def rf_f59_returns_family_per_opex_63d_base_v043_signal(roa, opex):
    result = _mean(_returns_family_scaled(roa, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roa/opex mean
def rf_f59_returns_family_per_opex_252d_base_v044_signal(roa, opex):
    result = _mean(_returns_family_scaled(roa, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roa/ebitda mean
def rf_f59_returns_family_per_ebitda_63d_base_v045_signal(roa, ebitda):
    result = _mean(_returns_family_scaled(roa, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roa/ebitda mean
def rf_f59_returns_family_per_ebitda_252d_base_v046_signal(roa, ebitda):
    result = _mean(_returns_family_scaled(roa, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roa/capex mean
def rf_f59_returns_family_per_capex_63d_base_v047_signal(roa, capex):
    result = _mean(_returns_family_scaled(roa, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roa/capex mean
def rf_f59_returns_family_per_capex_252d_base_v048_signal(roa, capex):
    result = _mean(_returns_family_scaled(roa, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roa/liabilities mean
def rf_f59_returns_family_per_liabilities_63d_base_v049_signal(roa, liabilities):
    result = _mean(_returns_family_scaled(roa, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roa/liabilities mean
def rf_f59_returns_family_per_liabilities_252d_base_v050_signal(roa, liabilities):
    result = _mean(_returns_family_scaled(roa, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# roa relative to 252d max times closeadj
def rf_f59_returns_family_relmax_252d_base_v051_signal(roa, closeadj):
    peak = roa.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (roa / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roa relative to 504d max times closeadj
def rf_f59_returns_family_relmax_504d_base_v052_signal(roa, closeadj):
    peak = roa.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (roa / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roa relative to 252d min times closeadj
def rf_f59_returns_family_relmin_252d_base_v053_signal(roa, closeadj):
    trough = roa.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (roa / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roa relative to 504d min times closeadj
def rf_f59_returns_family_relmin_504d_base_v054_signal(roa, closeadj):
    trough = roa.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (roa / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of roa times closeadj
def rf_f59_returns_family_pct_21d_base_v055_signal(roa, closeadj):
    result = _pct_change(roa, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of roa times closeadj
def rf_f59_returns_family_pct_63d_base_v056_signal(roa, closeadj):
    result = _pct_change(roa, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of roa times closeadj
def rf_f59_returns_family_pct_252d_base_v057_signal(roa, closeadj):
    result = _pct_change(roa, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of roa times closeadj
def rf_f59_returns_family_sum_63d_base_v058_signal(roa, closeadj):
    result = roa.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of roa times closeadj
def rf_f59_returns_family_sum_252d_base_v059_signal(roa, closeadj):
    result = roa.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of roa times closeadj
def rf_f59_returns_family_sum_504d_base_v060_signal(roa, closeadj):
    result = roa.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roa(63d) / smoothed assets(252d) x closeadj
def rf_f59_returns_family_rom_assets_252_63d_base_v061_signal(roa, assets, closeadj):
    n = _mean(roa, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roa(126d) / smoothed assets(504d) x closeadj
def rf_f59_returns_family_rom_assets_504_126d_base_v062_signal(roa, assets, closeadj):
    n = _mean(roa, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roa(63d) / smoothed marketcap(252d) x closeadj
def rf_f59_returns_family_rom_marketcap_252_63d_base_v063_signal(roa, marketcap, closeadj):
    n = _mean(roa, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roa(126d) / smoothed marketcap(504d) x closeadj
def rf_f59_returns_family_rom_marketcap_504_126d_base_v064_signal(roa, marketcap, closeadj):
    n = _mean(roa, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roa(63d) / smoothed equity(252d) x closeadj
def rf_f59_returns_family_rom_equity_252_63d_base_v065_signal(roa, equity, closeadj):
    n = _mean(roa, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roa(126d) / smoothed equity(504d) x closeadj
def rf_f59_returns_family_rom_equity_504_126d_base_v066_signal(roa, equity, closeadj):
    n = _mean(roa, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(roa) / std(assets)
def rf_f59_returns_family_volratio_assets_252d_base_v067_signal(roa, assets):
    n = _std(roa, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(roa) / std(assets)
def rf_f59_returns_family_volratio_assets_504d_base_v068_signal(roa, assets):
    n = _std(roa, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(roa) / std(marketcap)
def rf_f59_returns_family_volratio_marketcap_252d_base_v069_signal(roa, marketcap):
    n = _std(roa, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(roa) / std(marketcap)
def rf_f59_returns_family_volratio_marketcap_504d_base_v070_signal(roa, marketcap):
    n = _std(roa, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed roa times closeadj
def rf_f59_returns_family_raw_5d_base_v071_signal(roa, closeadj):
    result = _mean(roa, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed roa times closeadj
def rf_f59_returns_family_raw_1008d_base_v072_signal(roa, closeadj):
    result = _mean(roa, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of roa/assets
def rf_f59_returns_family_log_per_assets_252d_base_v073_signal(roa, assets):
    s = _returns_family_scaled(roa, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of roa/assets
def rf_f59_returns_family_log_per_assets_504d_base_v074_signal(roa, assets):
    s = _returns_family_scaled(roa, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of roa/marketcap
def rf_f59_returns_family_log_per_marketcap_252d_base_v075_signal(roa, marketcap):
    s = _returns_family_scaled(roa, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
