"""Family f82 - Fundamental volatility index  (N_Fundamental_Dynamics) | base 001-075"""
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
def _fundamental_volatility_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _fundamental_volatility_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _fundamental_volatility_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed revenue times closeadj
def fv_f82_fundamental_volatility_raw_21d_base_v001_signal(revenue, closeadj):
    result = _mean(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed revenue times closeadj
def fv_f82_fundamental_volatility_raw_63d_base_v002_signal(revenue, closeadj):
    result = _mean(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed revenue times closeadj
def fv_f82_fundamental_volatility_raw_126d_base_v003_signal(revenue, closeadj):
    result = _mean(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed revenue times closeadj
def fv_f82_fundamental_volatility_raw_252d_base_v004_signal(revenue, closeadj):
    result = _mean(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed revenue times closeadj
def fv_f82_fundamental_volatility_raw_504d_base_v005_signal(revenue, closeadj):
    result = _mean(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(revenue) times closeadj
def fv_f82_fundamental_volatility_log_21d_base_v006_signal(revenue, closeadj):
    result = _mean(_fundamental_volatility_log(revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(revenue) times closeadj
def fv_f82_fundamental_volatility_log_63d_base_v007_signal(revenue, closeadj):
    result = _mean(_fundamental_volatility_log(revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(revenue) times closeadj
def fv_f82_fundamental_volatility_log_126d_base_v008_signal(revenue, closeadj):
    result = _mean(_fundamental_volatility_log(revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(revenue) times closeadj
def fv_f82_fundamental_volatility_log_252d_base_v009_signal(revenue, closeadj):
    result = _mean(_fundamental_volatility_log(revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(revenue) times closeadj
def fv_f82_fundamental_volatility_log_504d_base_v010_signal(revenue, closeadj):
    result = _mean(_fundamental_volatility_log(revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/assets mean
def fv_f82_fundamental_volatility_per_assets_63d_base_v011_signal(revenue, assets):
    result = _mean(_fundamental_volatility_scaled(revenue, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/assets mean
def fv_f82_fundamental_volatility_per_assets_252d_base_v012_signal(revenue, assets):
    result = _mean(_fundamental_volatility_scaled(revenue, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue/assets mean
def fv_f82_fundamental_volatility_per_assets_504d_base_v013_signal(revenue, assets):
    result = _mean(_fundamental_volatility_scaled(revenue, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/marketcap mean
def fv_f82_fundamental_volatility_per_marketcap_63d_base_v014_signal(revenue, marketcap):
    result = _mean(_fundamental_volatility_scaled(revenue, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/marketcap mean
def fv_f82_fundamental_volatility_per_marketcap_252d_base_v015_signal(revenue, marketcap):
    result = _mean(_fundamental_volatility_scaled(revenue, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue/marketcap mean
def fv_f82_fundamental_volatility_per_marketcap_504d_base_v016_signal(revenue, marketcap):
    result = _mean(_fundamental_volatility_scaled(revenue, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/equity mean
def fv_f82_fundamental_volatility_per_equity_63d_base_v017_signal(revenue, equity):
    result = _mean(_fundamental_volatility_scaled(revenue, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/equity mean
def fv_f82_fundamental_volatility_per_equity_252d_base_v018_signal(revenue, equity):
    result = _mean(_fundamental_volatility_scaled(revenue, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue/equity mean
def fv_f82_fundamental_volatility_per_equity_504d_base_v019_signal(revenue, equity):
    result = _mean(_fundamental_volatility_scaled(revenue, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/debt mean
def fv_f82_fundamental_volatility_per_debt_63d_base_v020_signal(revenue, debt):
    result = _mean(_fundamental_volatility_scaled(revenue, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/debt mean
def fv_f82_fundamental_volatility_per_debt_252d_base_v021_signal(revenue, debt):
    result = _mean(_fundamental_volatility_scaled(revenue, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue/debt mean
def fv_f82_fundamental_volatility_per_debt_504d_base_v022_signal(revenue, debt):
    result = _mean(_fundamental_volatility_scaled(revenue, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/revenue mean
def fv_f82_fundamental_volatility_per_revenue_63d_base_v023_signal(revenue):
    result = _mean(_fundamental_volatility_scaled(revenue, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/revenue mean
def fv_f82_fundamental_volatility_per_revenue_252d_base_v024_signal(revenue):
    result = _mean(_fundamental_volatility_scaled(revenue, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue/revenue mean
def fv_f82_fundamental_volatility_per_revenue_504d_base_v025_signal(revenue):
    result = _mean(_fundamental_volatility_scaled(revenue, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue per share times closeadj
def fv_f82_fundamental_volatility_pershare_21d_base_v026_signal(revenue, sharesbas, closeadj):
    ps = _fundamental_volatility_per_share(revenue, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue per share times closeadj
def fv_f82_fundamental_volatility_pershare_63d_base_v027_signal(revenue, sharesbas, closeadj):
    ps = _fundamental_volatility_per_share(revenue, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d revenue per share times closeadj
def fv_f82_fundamental_volatility_pershare_126d_base_v028_signal(revenue, sharesbas, closeadj):
    ps = _fundamental_volatility_per_share(revenue, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue per share times closeadj
def fv_f82_fundamental_volatility_pershare_252d_base_v029_signal(revenue, sharesbas, closeadj):
    ps = _fundamental_volatility_per_share(revenue, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue per share times closeadj
def fv_f82_fundamental_volatility_pershare_504d_base_v030_signal(revenue, sharesbas, closeadj):
    ps = _fundamental_volatility_per_share(revenue, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of revenue times closeadj
def fv_f82_fundamental_volatility_std_63d_base_v031_signal(revenue, closeadj):
    result = _std(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of revenue times closeadj
def fv_f82_fundamental_volatility_std_252d_base_v032_signal(revenue, closeadj):
    result = _std(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of revenue times closeadj
def fv_f82_fundamental_volatility_std_504d_base_v033_signal(revenue, closeadj):
    result = _std(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of revenue
def fv_f82_fundamental_volatility_z_252d_base_v034_signal(revenue):
    result = _z(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of revenue
def fv_f82_fundamental_volatility_z_504d_base_v035_signal(revenue):
    result = _z(revenue, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(revenue)
def fv_f82_fundamental_volatility_logz_252d_base_v036_signal(revenue):
    result = _z(_fundamental_volatility_log(revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(revenue)
def fv_f82_fundamental_volatility_logz_504d_base_v037_signal(revenue):
    result = _z(_fundamental_volatility_log(revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of revenue^2 times closeadj
def fv_f82_fundamental_volatility_sq_63d_base_v038_signal(revenue, closeadj):
    result = _mean(revenue * revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of revenue^2 times closeadj
def fv_f82_fundamental_volatility_sq_252d_base_v039_signal(revenue, closeadj):
    result = _mean(revenue * revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(revenue) times closeadj
def fv_f82_fundamental_volatility_sign_21d_base_v040_signal(revenue, closeadj):
    result = _mean(np.sign(revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(revenue) times closeadj
def fv_f82_fundamental_volatility_sign_63d_base_v041_signal(revenue, closeadj):
    result = _mean(np.sign(revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(revenue) times closeadj
def fv_f82_fundamental_volatility_sign_252d_base_v042_signal(revenue, closeadj):
    result = _mean(np.sign(revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/opex mean
def fv_f82_fundamental_volatility_per_opex_63d_base_v043_signal(revenue, opex):
    result = _mean(_fundamental_volatility_scaled(revenue, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/opex mean
def fv_f82_fundamental_volatility_per_opex_252d_base_v044_signal(revenue, opex):
    result = _mean(_fundamental_volatility_scaled(revenue, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/ebitda mean
def fv_f82_fundamental_volatility_per_ebitda_63d_base_v045_signal(revenue, ebitda):
    result = _mean(_fundamental_volatility_scaled(revenue, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/ebitda mean
def fv_f82_fundamental_volatility_per_ebitda_252d_base_v046_signal(revenue, ebitda):
    result = _mean(_fundamental_volatility_scaled(revenue, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/capex mean
def fv_f82_fundamental_volatility_per_capex_63d_base_v047_signal(revenue, capex):
    result = _mean(_fundamental_volatility_scaled(revenue, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/capex mean
def fv_f82_fundamental_volatility_per_capex_252d_base_v048_signal(revenue, capex):
    result = _mean(_fundamental_volatility_scaled(revenue, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/liabilities mean
def fv_f82_fundamental_volatility_per_liabilities_63d_base_v049_signal(revenue, liabilities):
    result = _mean(_fundamental_volatility_scaled(revenue, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/liabilities mean
def fv_f82_fundamental_volatility_per_liabilities_252d_base_v050_signal(revenue, liabilities):
    result = _mean(_fundamental_volatility_scaled(revenue, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue relative to 252d max times closeadj
def fv_f82_fundamental_volatility_relmax_252d_base_v051_signal(revenue, closeadj):
    peak = revenue.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (revenue / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue relative to 504d max times closeadj
def fv_f82_fundamental_volatility_relmax_504d_base_v052_signal(revenue, closeadj):
    peak = revenue.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (revenue / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue relative to 252d min times closeadj
def fv_f82_fundamental_volatility_relmin_252d_base_v053_signal(revenue, closeadj):
    trough = revenue.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (revenue / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue relative to 504d min times closeadj
def fv_f82_fundamental_volatility_relmin_504d_base_v054_signal(revenue, closeadj):
    trough = revenue.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (revenue / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of revenue times closeadj
def fv_f82_fundamental_volatility_pct_21d_base_v055_signal(revenue, closeadj):
    result = _pct_change(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of revenue times closeadj
def fv_f82_fundamental_volatility_pct_63d_base_v056_signal(revenue, closeadj):
    result = _pct_change(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of revenue times closeadj
def fv_f82_fundamental_volatility_pct_252d_base_v057_signal(revenue, closeadj):
    result = _pct_change(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of revenue times closeadj
def fv_f82_fundamental_volatility_sum_63d_base_v058_signal(revenue, closeadj):
    result = revenue.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of revenue times closeadj
def fv_f82_fundamental_volatility_sum_252d_base_v059_signal(revenue, closeadj):
    result = revenue.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of revenue times closeadj
def fv_f82_fundamental_volatility_sum_504d_base_v060_signal(revenue, closeadj):
    result = revenue.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue(63d) / smoothed assets(252d) x closeadj
def fv_f82_fundamental_volatility_rom_assets_252_63d_base_v061_signal(revenue, assets, closeadj):
    n = _mean(revenue, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue(126d) / smoothed assets(504d) x closeadj
def fv_f82_fundamental_volatility_rom_assets_504_126d_base_v062_signal(revenue, assets, closeadj):
    n = _mean(revenue, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue(63d) / smoothed marketcap(252d) x closeadj
def fv_f82_fundamental_volatility_rom_marketcap_252_63d_base_v063_signal(revenue, marketcap, closeadj):
    n = _mean(revenue, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue(126d) / smoothed marketcap(504d) x closeadj
def fv_f82_fundamental_volatility_rom_marketcap_504_126d_base_v064_signal(revenue, marketcap, closeadj):
    n = _mean(revenue, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue(63d) / smoothed equity(252d) x closeadj
def fv_f82_fundamental_volatility_rom_equity_252_63d_base_v065_signal(revenue, equity, closeadj):
    n = _mean(revenue, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue(126d) / smoothed equity(504d) x closeadj
def fv_f82_fundamental_volatility_rom_equity_504_126d_base_v066_signal(revenue, equity, closeadj):
    n = _mean(revenue, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(revenue) / std(assets)
def fv_f82_fundamental_volatility_volratio_assets_252d_base_v067_signal(revenue, assets):
    n = _std(revenue, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(revenue) / std(assets)
def fv_f82_fundamental_volatility_volratio_assets_504d_base_v068_signal(revenue, assets):
    n = _std(revenue, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(revenue) / std(marketcap)
def fv_f82_fundamental_volatility_volratio_marketcap_252d_base_v069_signal(revenue, marketcap):
    n = _std(revenue, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(revenue) / std(marketcap)
def fv_f82_fundamental_volatility_volratio_marketcap_504d_base_v070_signal(revenue, marketcap):
    n = _std(revenue, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed revenue times closeadj
def fv_f82_fundamental_volatility_raw_5d_base_v071_signal(revenue, closeadj):
    result = _mean(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed revenue times closeadj
def fv_f82_fundamental_volatility_raw_1008d_base_v072_signal(revenue, closeadj):
    result = _mean(revenue, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of revenue/assets
def fv_f82_fundamental_volatility_log_per_assets_252d_base_v073_signal(revenue, assets):
    s = _fundamental_volatility_scaled(revenue, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of revenue/assets
def fv_f82_fundamental_volatility_log_per_assets_504d_base_v074_signal(revenue, assets):
    s = _fundamental_volatility_scaled(revenue, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of revenue/marketcap
def fv_f82_fundamental_volatility_log_per_marketcap_252d_base_v075_signal(revenue, marketcap):
    s = _fundamental_volatility_scaled(revenue, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
