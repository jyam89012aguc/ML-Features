"""Family f40 - Receivables level & quality  (F_BalanceSheet) | base 001-075"""
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
def _receivables_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _receivables_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _receivables_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed receivables times closeadj
def rec_f40_receivables_raw_21d_base_v001_signal(receivables, closeadj):
    result = _mean(receivables, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed receivables times closeadj
def rec_f40_receivables_raw_63d_base_v002_signal(receivables, closeadj):
    result = _mean(receivables, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed receivables times closeadj
def rec_f40_receivables_raw_126d_base_v003_signal(receivables, closeadj):
    result = _mean(receivables, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed receivables times closeadj
def rec_f40_receivables_raw_252d_base_v004_signal(receivables, closeadj):
    result = _mean(receivables, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed receivables times closeadj
def rec_f40_receivables_raw_504d_base_v005_signal(receivables, closeadj):
    result = _mean(receivables, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(receivables) times closeadj
def rec_f40_receivables_log_21d_base_v006_signal(receivables, closeadj):
    result = _mean(_receivables_log(receivables), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(receivables) times closeadj
def rec_f40_receivables_log_63d_base_v007_signal(receivables, closeadj):
    result = _mean(_receivables_log(receivables), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(receivables) times closeadj
def rec_f40_receivables_log_126d_base_v008_signal(receivables, closeadj):
    result = _mean(_receivables_log(receivables), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(receivables) times closeadj
def rec_f40_receivables_log_252d_base_v009_signal(receivables, closeadj):
    result = _mean(_receivables_log(receivables), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(receivables) times closeadj
def rec_f40_receivables_log_504d_base_v010_signal(receivables, closeadj):
    result = _mean(_receivables_log(receivables), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/assets mean
def rec_f40_receivables_per_assets_63d_base_v011_signal(receivables, assets):
    result = _mean(_receivables_scaled(receivables, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/assets mean
def rec_f40_receivables_per_assets_252d_base_v012_signal(receivables, assets):
    result = _mean(_receivables_scaled(receivables, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d receivables/assets mean
def rec_f40_receivables_per_assets_504d_base_v013_signal(receivables, assets):
    result = _mean(_receivables_scaled(receivables, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/marketcap mean
def rec_f40_receivables_per_marketcap_63d_base_v014_signal(receivables, marketcap):
    result = _mean(_receivables_scaled(receivables, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/marketcap mean
def rec_f40_receivables_per_marketcap_252d_base_v015_signal(receivables, marketcap):
    result = _mean(_receivables_scaled(receivables, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d receivables/marketcap mean
def rec_f40_receivables_per_marketcap_504d_base_v016_signal(receivables, marketcap):
    result = _mean(_receivables_scaled(receivables, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/equity mean
def rec_f40_receivables_per_equity_63d_base_v017_signal(receivables, equity):
    result = _mean(_receivables_scaled(receivables, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/equity mean
def rec_f40_receivables_per_equity_252d_base_v018_signal(receivables, equity):
    result = _mean(_receivables_scaled(receivables, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d receivables/equity mean
def rec_f40_receivables_per_equity_504d_base_v019_signal(receivables, equity):
    result = _mean(_receivables_scaled(receivables, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/debt mean
def rec_f40_receivables_per_debt_63d_base_v020_signal(receivables, debt):
    result = _mean(_receivables_scaled(receivables, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/debt mean
def rec_f40_receivables_per_debt_252d_base_v021_signal(receivables, debt):
    result = _mean(_receivables_scaled(receivables, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d receivables/debt mean
def rec_f40_receivables_per_debt_504d_base_v022_signal(receivables, debt):
    result = _mean(_receivables_scaled(receivables, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/revenue mean
def rec_f40_receivables_per_revenue_63d_base_v023_signal(receivables, revenue):
    result = _mean(_receivables_scaled(receivables, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/revenue mean
def rec_f40_receivables_per_revenue_252d_base_v024_signal(receivables, revenue):
    result = _mean(_receivables_scaled(receivables, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d receivables/revenue mean
def rec_f40_receivables_per_revenue_504d_base_v025_signal(receivables, revenue):
    result = _mean(_receivables_scaled(receivables, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d receivables per share times closeadj
def rec_f40_receivables_pershare_21d_base_v026_signal(receivables, sharesbas, closeadj):
    ps = _receivables_per_share(receivables, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables per share times closeadj
def rec_f40_receivables_pershare_63d_base_v027_signal(receivables, sharesbas, closeadj):
    ps = _receivables_per_share(receivables, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d receivables per share times closeadj
def rec_f40_receivables_pershare_126d_base_v028_signal(receivables, sharesbas, closeadj):
    ps = _receivables_per_share(receivables, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables per share times closeadj
def rec_f40_receivables_pershare_252d_base_v029_signal(receivables, sharesbas, closeadj):
    ps = _receivables_per_share(receivables, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d receivables per share times closeadj
def rec_f40_receivables_pershare_504d_base_v030_signal(receivables, sharesbas, closeadj):
    ps = _receivables_per_share(receivables, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of receivables times closeadj
def rec_f40_receivables_std_63d_base_v031_signal(receivables, closeadj):
    result = _std(receivables, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of receivables times closeadj
def rec_f40_receivables_std_252d_base_v032_signal(receivables, closeadj):
    result = _std(receivables, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of receivables times closeadj
def rec_f40_receivables_std_504d_base_v033_signal(receivables, closeadj):
    result = _std(receivables, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of receivables
def rec_f40_receivables_z_252d_base_v034_signal(receivables):
    result = _z(receivables, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of receivables
def rec_f40_receivables_z_504d_base_v035_signal(receivables):
    result = _z(receivables, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(receivables)
def rec_f40_receivables_logz_252d_base_v036_signal(receivables):
    result = _z(_receivables_log(receivables), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(receivables)
def rec_f40_receivables_logz_504d_base_v037_signal(receivables):
    result = _z(_receivables_log(receivables), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of receivables^2 times closeadj
def rec_f40_receivables_sq_63d_base_v038_signal(receivables, closeadj):
    result = _mean(receivables * receivables, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of receivables^2 times closeadj
def rec_f40_receivables_sq_252d_base_v039_signal(receivables, closeadj):
    result = _mean(receivables * receivables, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(receivables) times closeadj
def rec_f40_receivables_sign_21d_base_v040_signal(receivables, closeadj):
    result = _mean(np.sign(receivables), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(receivables) times closeadj
def rec_f40_receivables_sign_63d_base_v041_signal(receivables, closeadj):
    result = _mean(np.sign(receivables), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(receivables) times closeadj
def rec_f40_receivables_sign_252d_base_v042_signal(receivables, closeadj):
    result = _mean(np.sign(receivables), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/opex mean
def rec_f40_receivables_per_opex_63d_base_v043_signal(receivables, opex):
    result = _mean(_receivables_scaled(receivables, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/opex mean
def rec_f40_receivables_per_opex_252d_base_v044_signal(receivables, opex):
    result = _mean(_receivables_scaled(receivables, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/ebitda mean
def rec_f40_receivables_per_ebitda_63d_base_v045_signal(receivables, ebitda):
    result = _mean(_receivables_scaled(receivables, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/ebitda mean
def rec_f40_receivables_per_ebitda_252d_base_v046_signal(receivables, ebitda):
    result = _mean(_receivables_scaled(receivables, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/capex mean
def rec_f40_receivables_per_capex_63d_base_v047_signal(receivables, capex):
    result = _mean(_receivables_scaled(receivables, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/capex mean
def rec_f40_receivables_per_capex_252d_base_v048_signal(receivables, capex):
    result = _mean(_receivables_scaled(receivables, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d receivables/liabilities mean
def rec_f40_receivables_per_liabilities_63d_base_v049_signal(receivables, liabilities):
    result = _mean(_receivables_scaled(receivables, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d receivables/liabilities mean
def rec_f40_receivables_per_liabilities_252d_base_v050_signal(receivables, liabilities):
    result = _mean(_receivables_scaled(receivables, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# receivables relative to 252d max times closeadj
def rec_f40_receivables_relmax_252d_base_v051_signal(receivables, closeadj):
    peak = receivables.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (receivables / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# receivables relative to 504d max times closeadj
def rec_f40_receivables_relmax_504d_base_v052_signal(receivables, closeadj):
    peak = receivables.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (receivables / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# receivables relative to 252d min times closeadj
def rec_f40_receivables_relmin_252d_base_v053_signal(receivables, closeadj):
    trough = receivables.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (receivables / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# receivables relative to 504d min times closeadj
def rec_f40_receivables_relmin_504d_base_v054_signal(receivables, closeadj):
    trough = receivables.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (receivables / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of receivables times closeadj
def rec_f40_receivables_pct_21d_base_v055_signal(receivables, closeadj):
    result = _pct_change(receivables, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of receivables times closeadj
def rec_f40_receivables_pct_63d_base_v056_signal(receivables, closeadj):
    result = _pct_change(receivables, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of receivables times closeadj
def rec_f40_receivables_pct_252d_base_v057_signal(receivables, closeadj):
    result = _pct_change(receivables, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of receivables times closeadj
def rec_f40_receivables_sum_63d_base_v058_signal(receivables, closeadj):
    result = receivables.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of receivables times closeadj
def rec_f40_receivables_sum_252d_base_v059_signal(receivables, closeadj):
    result = receivables.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of receivables times closeadj
def rec_f40_receivables_sum_504d_base_v060_signal(receivables, closeadj):
    result = receivables.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed receivables(63d) / smoothed assets(252d) x closeadj
def rec_f40_receivables_rom_assets_252_63d_base_v061_signal(receivables, assets, closeadj):
    n = _mean(receivables, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed receivables(126d) / smoothed assets(504d) x closeadj
def rec_f40_receivables_rom_assets_504_126d_base_v062_signal(receivables, assets, closeadj):
    n = _mean(receivables, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed receivables(63d) / smoothed marketcap(252d) x closeadj
def rec_f40_receivables_rom_marketcap_252_63d_base_v063_signal(receivables, marketcap, closeadj):
    n = _mean(receivables, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed receivables(126d) / smoothed marketcap(504d) x closeadj
def rec_f40_receivables_rom_marketcap_504_126d_base_v064_signal(receivables, marketcap, closeadj):
    n = _mean(receivables, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed receivables(63d) / smoothed equity(252d) x closeadj
def rec_f40_receivables_rom_equity_252_63d_base_v065_signal(receivables, equity, closeadj):
    n = _mean(receivables, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed receivables(126d) / smoothed equity(504d) x closeadj
def rec_f40_receivables_rom_equity_504_126d_base_v066_signal(receivables, equity, closeadj):
    n = _mean(receivables, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(receivables) / std(assets)
def rec_f40_receivables_volratio_assets_252d_base_v067_signal(receivables, assets):
    n = _std(receivables, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(receivables) / std(assets)
def rec_f40_receivables_volratio_assets_504d_base_v068_signal(receivables, assets):
    n = _std(receivables, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(receivables) / std(marketcap)
def rec_f40_receivables_volratio_marketcap_252d_base_v069_signal(receivables, marketcap):
    n = _std(receivables, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(receivables) / std(marketcap)
def rec_f40_receivables_volratio_marketcap_504d_base_v070_signal(receivables, marketcap):
    n = _std(receivables, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed receivables times closeadj
def rec_f40_receivables_raw_5d_base_v071_signal(receivables, closeadj):
    result = _mean(receivables, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed receivables times closeadj
def rec_f40_receivables_raw_1008d_base_v072_signal(receivables, closeadj):
    result = _mean(receivables, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of receivables/assets
def rec_f40_receivables_log_per_assets_252d_base_v073_signal(receivables, assets):
    s = _receivables_scaled(receivables, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of receivables/assets
def rec_f40_receivables_log_per_assets_504d_base_v074_signal(receivables, assets):
    s = _receivables_scaled(receivables, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of receivables/marketcap
def rec_f40_receivables_log_per_marketcap_252d_base_v075_signal(receivables, marketcap):
    s = _receivables_scaled(receivables, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
