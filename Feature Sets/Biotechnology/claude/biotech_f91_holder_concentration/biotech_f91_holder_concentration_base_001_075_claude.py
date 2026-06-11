"""Family f91 - Holder count & concentration  (P_Institutional_SF3) | base 001-075"""
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


# 21d smoothed units times closeadj
def hc_f91_holder_concentration_raw_21d_base_v001_signal(units, closeadj):
    result = _mean(units, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed units times closeadj
def hc_f91_holder_concentration_raw_63d_base_v002_signal(units, closeadj):
    result = _mean(units, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed units times closeadj
def hc_f91_holder_concentration_raw_126d_base_v003_signal(units, closeadj):
    result = _mean(units, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed units times closeadj
def hc_f91_holder_concentration_raw_252d_base_v004_signal(units, closeadj):
    result = _mean(units, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed units times closeadj
def hc_f91_holder_concentration_raw_504d_base_v005_signal(units, closeadj):
    result = _mean(units, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(units) times closeadj
def hc_f91_holder_concentration_log_21d_base_v006_signal(units, closeadj):
    result = _mean(_holder_concentration_log(units), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(units) times closeadj
def hc_f91_holder_concentration_log_63d_base_v007_signal(units, closeadj):
    result = _mean(_holder_concentration_log(units), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(units) times closeadj
def hc_f91_holder_concentration_log_126d_base_v008_signal(units, closeadj):
    result = _mean(_holder_concentration_log(units), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(units) times closeadj
def hc_f91_holder_concentration_log_252d_base_v009_signal(units, closeadj):
    result = _mean(_holder_concentration_log(units), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(units) times closeadj
def hc_f91_holder_concentration_log_504d_base_v010_signal(units, closeadj):
    result = _mean(_holder_concentration_log(units), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d units/assets mean
def hc_f91_holder_concentration_per_assets_63d_base_v011_signal(units, assets):
    result = _mean(_holder_concentration_scaled(units, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d units/assets mean
def hc_f91_holder_concentration_per_assets_252d_base_v012_signal(units, assets):
    result = _mean(_holder_concentration_scaled(units, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d units/assets mean
def hc_f91_holder_concentration_per_assets_504d_base_v013_signal(units, assets):
    result = _mean(_holder_concentration_scaled(units, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d units/marketcap mean
def hc_f91_holder_concentration_per_marketcap_63d_base_v014_signal(units, marketcap):
    result = _mean(_holder_concentration_scaled(units, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d units/marketcap mean
def hc_f91_holder_concentration_per_marketcap_252d_base_v015_signal(units, marketcap):
    result = _mean(_holder_concentration_scaled(units, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d units/marketcap mean
def hc_f91_holder_concentration_per_marketcap_504d_base_v016_signal(units, marketcap):
    result = _mean(_holder_concentration_scaled(units, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d units/equity mean
def hc_f91_holder_concentration_per_equity_63d_base_v017_signal(units, equity):
    result = _mean(_holder_concentration_scaled(units, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d units/equity mean
def hc_f91_holder_concentration_per_equity_252d_base_v018_signal(units, equity):
    result = _mean(_holder_concentration_scaled(units, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d units/equity mean
def hc_f91_holder_concentration_per_equity_504d_base_v019_signal(units, equity):
    result = _mean(_holder_concentration_scaled(units, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d units/debt mean
def hc_f91_holder_concentration_per_debt_63d_base_v020_signal(units, debt):
    result = _mean(_holder_concentration_scaled(units, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d units/debt mean
def hc_f91_holder_concentration_per_debt_252d_base_v021_signal(units, debt):
    result = _mean(_holder_concentration_scaled(units, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d units/debt mean
def hc_f91_holder_concentration_per_debt_504d_base_v022_signal(units, debt):
    result = _mean(_holder_concentration_scaled(units, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d units/revenue mean
def hc_f91_holder_concentration_per_revenue_63d_base_v023_signal(units, revenue):
    result = _mean(_holder_concentration_scaled(units, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d units/revenue mean
def hc_f91_holder_concentration_per_revenue_252d_base_v024_signal(units, revenue):
    result = _mean(_holder_concentration_scaled(units, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d units/revenue mean
def hc_f91_holder_concentration_per_revenue_504d_base_v025_signal(units, revenue):
    result = _mean(_holder_concentration_scaled(units, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d units per share times closeadj
def hc_f91_holder_concentration_pershare_21d_base_v026_signal(units, sharesbas, closeadj):
    ps = _holder_concentration_per_share(units, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d units per share times closeadj
def hc_f91_holder_concentration_pershare_63d_base_v027_signal(units, sharesbas, closeadj):
    ps = _holder_concentration_per_share(units, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d units per share times closeadj
def hc_f91_holder_concentration_pershare_126d_base_v028_signal(units, sharesbas, closeadj):
    ps = _holder_concentration_per_share(units, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d units per share times closeadj
def hc_f91_holder_concentration_pershare_252d_base_v029_signal(units, sharesbas, closeadj):
    ps = _holder_concentration_per_share(units, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d units per share times closeadj
def hc_f91_holder_concentration_pershare_504d_base_v030_signal(units, sharesbas, closeadj):
    ps = _holder_concentration_per_share(units, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of units times closeadj
def hc_f91_holder_concentration_std_63d_base_v031_signal(units, closeadj):
    result = _std(units, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of units times closeadj
def hc_f91_holder_concentration_std_252d_base_v032_signal(units, closeadj):
    result = _std(units, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of units times closeadj
def hc_f91_holder_concentration_std_504d_base_v033_signal(units, closeadj):
    result = _std(units, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of units
def hc_f91_holder_concentration_z_252d_base_v034_signal(units):
    result = _z(units, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of units
def hc_f91_holder_concentration_z_504d_base_v035_signal(units):
    result = _z(units, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(units)
def hc_f91_holder_concentration_logz_252d_base_v036_signal(units):
    result = _z(_holder_concentration_log(units), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(units)
def hc_f91_holder_concentration_logz_504d_base_v037_signal(units):
    result = _z(_holder_concentration_log(units), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of units^2 times closeadj
def hc_f91_holder_concentration_sq_63d_base_v038_signal(units, closeadj):
    result = _mean(units * units, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of units^2 times closeadj
def hc_f91_holder_concentration_sq_252d_base_v039_signal(units, closeadj):
    result = _mean(units * units, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(units) times closeadj
def hc_f91_holder_concentration_sign_21d_base_v040_signal(units, closeadj):
    result = _mean(np.sign(units), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(units) times closeadj
def hc_f91_holder_concentration_sign_63d_base_v041_signal(units, closeadj):
    result = _mean(np.sign(units), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(units) times closeadj
def hc_f91_holder_concentration_sign_252d_base_v042_signal(units, closeadj):
    result = _mean(np.sign(units), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d units/opex mean
def hc_f91_holder_concentration_per_opex_63d_base_v043_signal(units, opex):
    result = _mean(_holder_concentration_scaled(units, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d units/opex mean
def hc_f91_holder_concentration_per_opex_252d_base_v044_signal(units, opex):
    result = _mean(_holder_concentration_scaled(units, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d units/ebitda mean
def hc_f91_holder_concentration_per_ebitda_63d_base_v045_signal(units, ebitda):
    result = _mean(_holder_concentration_scaled(units, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d units/ebitda mean
def hc_f91_holder_concentration_per_ebitda_252d_base_v046_signal(units, ebitda):
    result = _mean(_holder_concentration_scaled(units, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d units/capex mean
def hc_f91_holder_concentration_per_capex_63d_base_v047_signal(units, capex):
    result = _mean(_holder_concentration_scaled(units, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d units/capex mean
def hc_f91_holder_concentration_per_capex_252d_base_v048_signal(units, capex):
    result = _mean(_holder_concentration_scaled(units, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d units/liabilities mean
def hc_f91_holder_concentration_per_liabilities_63d_base_v049_signal(units, liabilities):
    result = _mean(_holder_concentration_scaled(units, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d units/liabilities mean
def hc_f91_holder_concentration_per_liabilities_252d_base_v050_signal(units, liabilities):
    result = _mean(_holder_concentration_scaled(units, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# units relative to 252d max times closeadj
def hc_f91_holder_concentration_relmax_252d_base_v051_signal(units, closeadj):
    peak = units.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (units / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# units relative to 504d max times closeadj
def hc_f91_holder_concentration_relmax_504d_base_v052_signal(units, closeadj):
    peak = units.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (units / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# units relative to 252d min times closeadj
def hc_f91_holder_concentration_relmin_252d_base_v053_signal(units, closeadj):
    trough = units.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (units / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# units relative to 504d min times closeadj
def hc_f91_holder_concentration_relmin_504d_base_v054_signal(units, closeadj):
    trough = units.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (units / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of units times closeadj
def hc_f91_holder_concentration_pct_21d_base_v055_signal(units, closeadj):
    result = _pct_change(units, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of units times closeadj
def hc_f91_holder_concentration_pct_63d_base_v056_signal(units, closeadj):
    result = _pct_change(units, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of units times closeadj
def hc_f91_holder_concentration_pct_252d_base_v057_signal(units, closeadj):
    result = _pct_change(units, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of units times closeadj
def hc_f91_holder_concentration_sum_63d_base_v058_signal(units, closeadj):
    result = units.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of units times closeadj
def hc_f91_holder_concentration_sum_252d_base_v059_signal(units, closeadj):
    result = units.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of units times closeadj
def hc_f91_holder_concentration_sum_504d_base_v060_signal(units, closeadj):
    result = units.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed units(63d) / smoothed assets(252d) x closeadj
def hc_f91_holder_concentration_rom_assets_252_63d_base_v061_signal(units, assets, closeadj):
    n = _mean(units, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed units(126d) / smoothed assets(504d) x closeadj
def hc_f91_holder_concentration_rom_assets_504_126d_base_v062_signal(units, assets, closeadj):
    n = _mean(units, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed units(63d) / smoothed marketcap(252d) x closeadj
def hc_f91_holder_concentration_rom_marketcap_252_63d_base_v063_signal(units, marketcap, closeadj):
    n = _mean(units, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed units(126d) / smoothed marketcap(504d) x closeadj
def hc_f91_holder_concentration_rom_marketcap_504_126d_base_v064_signal(units, marketcap, closeadj):
    n = _mean(units, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed units(63d) / smoothed equity(252d) x closeadj
def hc_f91_holder_concentration_rom_equity_252_63d_base_v065_signal(units, equity, closeadj):
    n = _mean(units, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed units(126d) / smoothed equity(504d) x closeadj
def hc_f91_holder_concentration_rom_equity_504_126d_base_v066_signal(units, equity, closeadj):
    n = _mean(units, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(units) / std(assets)
def hc_f91_holder_concentration_volratio_assets_252d_base_v067_signal(units, assets):
    n = _std(units, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(units) / std(assets)
def hc_f91_holder_concentration_volratio_assets_504d_base_v068_signal(units, assets):
    n = _std(units, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(units) / std(marketcap)
def hc_f91_holder_concentration_volratio_marketcap_252d_base_v069_signal(units, marketcap):
    n = _std(units, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(units) / std(marketcap)
def hc_f91_holder_concentration_volratio_marketcap_504d_base_v070_signal(units, marketcap):
    n = _std(units, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed units times closeadj
def hc_f91_holder_concentration_raw_5d_base_v071_signal(units, closeadj):
    result = _mean(units, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed units times closeadj
def hc_f91_holder_concentration_raw_1008d_base_v072_signal(units, closeadj):
    result = _mean(units, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of units/assets
def hc_f91_holder_concentration_log_per_assets_252d_base_v073_signal(units, assets):
    s = _holder_concentration_scaled(units, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of units/assets
def hc_f91_holder_concentration_log_per_assets_504d_base_v074_signal(units, assets):
    s = _holder_concentration_scaled(units, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of units/marketcap
def hc_f91_holder_concentration_log_per_marketcap_252d_base_v075_signal(units, marketcap):
    s = _holder_concentration_scaled(units, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
