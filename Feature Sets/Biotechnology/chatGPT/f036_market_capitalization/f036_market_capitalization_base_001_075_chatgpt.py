"""Family f036 - Market capitalization scale (Dilution and Share Count) | Sharadar tables: DAILY,SF1 | fields: marketcap, sharesbas, close | base 001-075"""
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
def _market_capitalization_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _market_capitalization_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _market_capitalization_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed marketcap times closeadj
def mc_f036_market_capitalization_raw_21d_base_v001_signal(marketcap, closeadj):
    result = _mean(marketcap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed marketcap times closeadj
def mc_f036_market_capitalization_raw_63d_base_v002_signal(marketcap, closeadj):
    result = _mean(marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed marketcap times closeadj
def mc_f036_market_capitalization_raw_126d_base_v003_signal(marketcap, closeadj):
    result = _mean(marketcap, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed marketcap times closeadj
def mc_f036_market_capitalization_raw_252d_base_v004_signal(marketcap, closeadj):
    result = _mean(marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed marketcap times closeadj
def mc_f036_market_capitalization_raw_504d_base_v005_signal(marketcap, closeadj):
    result = _mean(marketcap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(marketcap) times closeadj
def mc_f036_market_capitalization_log_21d_base_v006_signal(marketcap, closeadj):
    result = _mean(_market_capitalization_log(marketcap), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(marketcap) times closeadj
def mc_f036_market_capitalization_log_63d_base_v007_signal(marketcap, closeadj):
    result = _mean(_market_capitalization_log(marketcap), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(marketcap) times closeadj
def mc_f036_market_capitalization_log_126d_base_v008_signal(marketcap, closeadj):
    result = _mean(_market_capitalization_log(marketcap), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(marketcap) times closeadj
def mc_f036_market_capitalization_log_252d_base_v009_signal(marketcap, closeadj):
    result = _mean(_market_capitalization_log(marketcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(marketcap) times closeadj
def mc_f036_market_capitalization_log_504d_base_v010_signal(marketcap, closeadj):
    result = _mean(_market_capitalization_log(marketcap), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/sharesbas mean
def mc_f036_market_capitalization_per_sharesbas_63d_base_v011_signal(marketcap, sharesbas):
    result = _mean(_market_capitalization_scaled(marketcap, sharesbas), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/sharesbas mean
def mc_f036_market_capitalization_per_sharesbas_252d_base_v012_signal(marketcap, sharesbas):
    result = _mean(_market_capitalization_scaled(marketcap, sharesbas), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap/sharesbas mean
def mc_f036_market_capitalization_per_sharesbas_504d_base_v013_signal(marketcap, sharesbas):
    result = _mean(_market_capitalization_scaled(marketcap, sharesbas), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/close mean
def mc_f036_market_capitalization_per_close_63d_base_v014_signal(marketcap, close):
    result = _mean(_market_capitalization_scaled(marketcap, close), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/close mean
def mc_f036_market_capitalization_per_close_252d_base_v015_signal(marketcap, close):
    result = _mean(_market_capitalization_scaled(marketcap, close), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap/close mean
def mc_f036_market_capitalization_per_close_504d_base_v016_signal(marketcap, close):
    result = _mean(_market_capitalization_scaled(marketcap, close), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/assets mean
def mc_f036_market_capitalization_per_assets_63d_base_v017_signal(marketcap, assets):
    result = _mean(_market_capitalization_scaled(marketcap, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/assets mean
def mc_f036_market_capitalization_per_assets_252d_base_v018_signal(marketcap, assets):
    result = _mean(_market_capitalization_scaled(marketcap, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap/assets mean
def mc_f036_market_capitalization_per_assets_504d_base_v019_signal(marketcap, assets):
    result = _mean(_market_capitalization_scaled(marketcap, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/equity mean
def mc_f036_market_capitalization_per_equity_63d_base_v020_signal(marketcap, equity):
    result = _mean(_market_capitalization_scaled(marketcap, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/equity mean
def mc_f036_market_capitalization_per_equity_252d_base_v021_signal(marketcap, equity):
    result = _mean(_market_capitalization_scaled(marketcap, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap/equity mean
def mc_f036_market_capitalization_per_equity_504d_base_v022_signal(marketcap, equity):
    result = _mean(_market_capitalization_scaled(marketcap, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/debt mean
def mc_f036_market_capitalization_per_debt_63d_base_v023_signal(marketcap, debt):
    result = _mean(_market_capitalization_scaled(marketcap, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/debt mean
def mc_f036_market_capitalization_per_debt_252d_base_v024_signal(marketcap, debt):
    result = _mean(_market_capitalization_scaled(marketcap, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap/debt mean
def mc_f036_market_capitalization_per_debt_504d_base_v025_signal(marketcap, debt):
    result = _mean(_market_capitalization_scaled(marketcap, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap per share times closeadj
def mc_f036_market_capitalization_pershare_21d_base_v026_signal(marketcap, sharesbas, closeadj):
    ps = _market_capitalization_per_share(marketcap, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap per share times closeadj
def mc_f036_market_capitalization_pershare_63d_base_v027_signal(marketcap, sharesbas, closeadj):
    ps = _market_capitalization_per_share(marketcap, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d marketcap per share times closeadj
def mc_f036_market_capitalization_pershare_126d_base_v028_signal(marketcap, sharesbas, closeadj):
    ps = _market_capitalization_per_share(marketcap, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap per share times closeadj
def mc_f036_market_capitalization_pershare_252d_base_v029_signal(marketcap, sharesbas, closeadj):
    ps = _market_capitalization_per_share(marketcap, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap per share times closeadj
def mc_f036_market_capitalization_pershare_504d_base_v030_signal(marketcap, sharesbas, closeadj):
    ps = _market_capitalization_per_share(marketcap, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of marketcap times closeadj
def mc_f036_market_capitalization_std_63d_base_v031_signal(marketcap, closeadj):
    result = _std(marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of marketcap times closeadj
def mc_f036_market_capitalization_std_252d_base_v032_signal(marketcap, closeadj):
    result = _std(marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of marketcap times closeadj
def mc_f036_market_capitalization_std_504d_base_v033_signal(marketcap, closeadj):
    result = _std(marketcap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of marketcap
def mc_f036_market_capitalization_z_252d_base_v034_signal(marketcap):
    result = _z(marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of marketcap
def mc_f036_market_capitalization_z_504d_base_v035_signal(marketcap):
    result = _z(marketcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(marketcap)
def mc_f036_market_capitalization_logz_252d_base_v036_signal(marketcap):
    result = _z(_market_capitalization_log(marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(marketcap)
def mc_f036_market_capitalization_logz_504d_base_v037_signal(marketcap):
    result = _z(_market_capitalization_log(marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of marketcap^2 times closeadj
def mc_f036_market_capitalization_sq_63d_base_v038_signal(marketcap, closeadj):
    result = _mean(marketcap * marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of marketcap^2 times closeadj
def mc_f036_market_capitalization_sq_252d_base_v039_signal(marketcap, closeadj):
    result = _mean(marketcap * marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(marketcap) times closeadj
def mc_f036_market_capitalization_sign_21d_base_v040_signal(marketcap, closeadj):
    result = _mean(np.sign(marketcap), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(marketcap) times closeadj
def mc_f036_market_capitalization_sign_63d_base_v041_signal(marketcap, closeadj):
    result = _mean(np.sign(marketcap), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(marketcap) times closeadj
def mc_f036_market_capitalization_sign_252d_base_v042_signal(marketcap, closeadj):
    result = _mean(np.sign(marketcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/opex mean
def mc_f036_market_capitalization_per_opex_63d_base_v043_signal(marketcap, opex):
    result = _mean(_market_capitalization_scaled(marketcap, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/opex mean
def mc_f036_market_capitalization_per_opex_252d_base_v044_signal(marketcap, opex):
    result = _mean(_market_capitalization_scaled(marketcap, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/ebitda mean
def mc_f036_market_capitalization_per_ebitda_63d_base_v045_signal(marketcap, ebitda):
    result = _mean(_market_capitalization_scaled(marketcap, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/ebitda mean
def mc_f036_market_capitalization_per_ebitda_252d_base_v046_signal(marketcap, ebitda):
    result = _mean(_market_capitalization_scaled(marketcap, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/capex mean
def mc_f036_market_capitalization_per_capex_63d_base_v047_signal(marketcap, capex):
    result = _mean(_market_capitalization_scaled(marketcap, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/capex mean
def mc_f036_market_capitalization_per_capex_252d_base_v048_signal(marketcap, capex):
    result = _mean(_market_capitalization_scaled(marketcap, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/liabilities mean
def mc_f036_market_capitalization_per_liabilities_63d_base_v049_signal(marketcap, liabilities):
    result = _mean(_market_capitalization_scaled(marketcap, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/liabilities mean
def mc_f036_market_capitalization_per_liabilities_252d_base_v050_signal(marketcap, liabilities):
    result = _mean(_market_capitalization_scaled(marketcap, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap relative to 252d max times closeadj
def mc_f036_market_capitalization_relmax_252d_base_v051_signal(marketcap, closeadj):
    peak = marketcap.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (marketcap / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap relative to 504d max times closeadj
def mc_f036_market_capitalization_relmax_504d_base_v052_signal(marketcap, closeadj):
    peak = marketcap.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (marketcap / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap relative to 252d min times closeadj
def mc_f036_market_capitalization_relmin_252d_base_v053_signal(marketcap, closeadj):
    trough = marketcap.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (marketcap / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap relative to 504d min times closeadj
def mc_f036_market_capitalization_relmin_504d_base_v054_signal(marketcap, closeadj):
    trough = marketcap.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (marketcap / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of marketcap times closeadj
def mc_f036_market_capitalization_pct_21d_base_v055_signal(marketcap, closeadj):
    result = _pct_change(marketcap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of marketcap times closeadj
def mc_f036_market_capitalization_pct_63d_base_v056_signal(marketcap, closeadj):
    result = _pct_change(marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of marketcap times closeadj
def mc_f036_market_capitalization_pct_252d_base_v057_signal(marketcap, closeadj):
    result = _pct_change(marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of marketcap times closeadj
def mc_f036_market_capitalization_sum_63d_base_v058_signal(marketcap, closeadj):
    result = marketcap.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of marketcap times closeadj
def mc_f036_market_capitalization_sum_252d_base_v059_signal(marketcap, closeadj):
    result = marketcap.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of marketcap times closeadj
def mc_f036_market_capitalization_sum_504d_base_v060_signal(marketcap, closeadj):
    result = marketcap.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(63d) / smoothed sharesbas(252d) x closeadj
def mc_f036_market_capitalization_rom_sharesbas_252_63d_base_v061_signal(marketcap, sharesbas, closeadj):
    n = _mean(marketcap, 63)
    d = _mean(sharesbas, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(126d) / smoothed sharesbas(504d) x closeadj
def mc_f036_market_capitalization_rom_sharesbas_504_126d_base_v062_signal(marketcap, sharesbas, closeadj):
    n = _mean(marketcap, 126)
    d = _mean(sharesbas, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(63d) / smoothed close(252d) x closeadj
def mc_f036_market_capitalization_rom_close_252_63d_base_v063_signal(marketcap, close, closeadj):
    n = _mean(marketcap, 63)
    d = _mean(close, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(126d) / smoothed close(504d) x closeadj
def mc_f036_market_capitalization_rom_close_504_126d_base_v064_signal(marketcap, close, closeadj):
    n = _mean(marketcap, 126)
    d = _mean(close, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(63d) / smoothed assets(252d) x closeadj
def mc_f036_market_capitalization_rom_assets_252_63d_base_v065_signal(marketcap, assets, closeadj):
    n = _mean(marketcap, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(126d) / smoothed assets(504d) x closeadj
def mc_f036_market_capitalization_rom_assets_504_126d_base_v066_signal(marketcap, assets, closeadj):
    n = _mean(marketcap, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(marketcap) / std(sharesbas)
def mc_f036_market_capitalization_volratio_sharesbas_252d_base_v067_signal(marketcap, sharesbas):
    n = _std(marketcap, 252)
    d = _std(sharesbas, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(marketcap) / std(sharesbas)
def mc_f036_market_capitalization_volratio_sharesbas_504d_base_v068_signal(marketcap, sharesbas):
    n = _std(marketcap, 504)
    d = _std(sharesbas, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(marketcap) / std(close)
def mc_f036_market_capitalization_volratio_close_252d_base_v069_signal(marketcap, close):
    n = _std(marketcap, 252)
    d = _std(close, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(marketcap) / std(close)
def mc_f036_market_capitalization_volratio_close_504d_base_v070_signal(marketcap, close):
    n = _std(marketcap, 504)
    d = _std(close, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed marketcap times closeadj
def mc_f036_market_capitalization_raw_5d_base_v071_signal(marketcap, closeadj):
    result = _mean(marketcap, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed marketcap times closeadj
def mc_f036_market_capitalization_raw_1008d_base_v072_signal(marketcap, closeadj):
    result = _mean(marketcap, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of marketcap/sharesbas
def mc_f036_market_capitalization_log_per_sharesbas_252d_base_v073_signal(marketcap, sharesbas):
    s = _market_capitalization_scaled(marketcap, sharesbas)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of marketcap/sharesbas
def mc_f036_market_capitalization_log_per_sharesbas_504d_base_v074_signal(marketcap, sharesbas):
    s = _market_capitalization_scaled(marketcap, sharesbas)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of marketcap/close
def mc_f036_market_capitalization_log_per_close_252d_base_v075_signal(marketcap, close):
    s = _market_capitalization_scaled(marketcap, close)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
