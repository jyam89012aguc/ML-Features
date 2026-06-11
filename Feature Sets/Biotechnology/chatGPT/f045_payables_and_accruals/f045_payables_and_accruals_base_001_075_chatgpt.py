"""Family f045 - Payables and accrued liabilities (Balance Sheet Composition) | Sharadar tables: SF1 | fields: payables, liabilitiesc, opex | base 001-075"""
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
def _payables_and_accruals_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _payables_and_accruals_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _payables_and_accruals_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed payables times closeadj
def paa_f045_payables_and_accruals_raw_21d_base_v001_signal(payables, closeadj):
    result = _mean(payables, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed payables times closeadj
def paa_f045_payables_and_accruals_raw_63d_base_v002_signal(payables, closeadj):
    result = _mean(payables, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed payables times closeadj
def paa_f045_payables_and_accruals_raw_126d_base_v003_signal(payables, closeadj):
    result = _mean(payables, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed payables times closeadj
def paa_f045_payables_and_accruals_raw_252d_base_v004_signal(payables, closeadj):
    result = _mean(payables, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed payables times closeadj
def paa_f045_payables_and_accruals_raw_504d_base_v005_signal(payables, closeadj):
    result = _mean(payables, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(payables) times closeadj
def paa_f045_payables_and_accruals_log_21d_base_v006_signal(payables, closeadj):
    result = _mean(_payables_and_accruals_log(payables), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(payables) times closeadj
def paa_f045_payables_and_accruals_log_63d_base_v007_signal(payables, closeadj):
    result = _mean(_payables_and_accruals_log(payables), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(payables) times closeadj
def paa_f045_payables_and_accruals_log_126d_base_v008_signal(payables, closeadj):
    result = _mean(_payables_and_accruals_log(payables), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(payables) times closeadj
def paa_f045_payables_and_accruals_log_252d_base_v009_signal(payables, closeadj):
    result = _mean(_payables_and_accruals_log(payables), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(payables) times closeadj
def paa_f045_payables_and_accruals_log_504d_base_v010_signal(payables, closeadj):
    result = _mean(_payables_and_accruals_log(payables), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d payables/liabilitiesc mean
def paa_f045_payables_and_accruals_per_liabilitiesc_63d_base_v011_signal(payables, liabilitiesc):
    result = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d payables/liabilitiesc mean
def paa_f045_payables_and_accruals_per_liabilitiesc_252d_base_v012_signal(payables, liabilitiesc):
    result = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d payables/liabilitiesc mean
def paa_f045_payables_and_accruals_per_liabilitiesc_504d_base_v013_signal(payables, liabilitiesc):
    result = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d payables/assets mean
def paa_f045_payables_and_accruals_per_assets_63d_base_v014_signal(payables, assets):
    result = _mean(_payables_and_accruals_scaled(payables, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d payables/assets mean
def paa_f045_payables_and_accruals_per_assets_252d_base_v015_signal(payables, assets):
    result = _mean(_payables_and_accruals_scaled(payables, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d payables/assets mean
def paa_f045_payables_and_accruals_per_assets_504d_base_v016_signal(payables, assets):
    result = _mean(_payables_and_accruals_scaled(payables, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d payables/marketcap mean
def paa_f045_payables_and_accruals_per_marketcap_63d_base_v017_signal(payables, marketcap):
    result = _mean(_payables_and_accruals_scaled(payables, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d payables/marketcap mean
def paa_f045_payables_and_accruals_per_marketcap_252d_base_v018_signal(payables, marketcap):
    result = _mean(_payables_and_accruals_scaled(payables, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d payables/marketcap mean
def paa_f045_payables_and_accruals_per_marketcap_504d_base_v019_signal(payables, marketcap):
    result = _mean(_payables_and_accruals_scaled(payables, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d payables/equity mean
def paa_f045_payables_and_accruals_per_equity_63d_base_v020_signal(payables, equity):
    result = _mean(_payables_and_accruals_scaled(payables, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d payables/equity mean
def paa_f045_payables_and_accruals_per_equity_252d_base_v021_signal(payables, equity):
    result = _mean(_payables_and_accruals_scaled(payables, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d payables/equity mean
def paa_f045_payables_and_accruals_per_equity_504d_base_v022_signal(payables, equity):
    result = _mean(_payables_and_accruals_scaled(payables, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d payables/debt mean
def paa_f045_payables_and_accruals_per_debt_63d_base_v023_signal(payables, debt):
    result = _mean(_payables_and_accruals_scaled(payables, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d payables/debt mean
def paa_f045_payables_and_accruals_per_debt_252d_base_v024_signal(payables, debt):
    result = _mean(_payables_and_accruals_scaled(payables, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d payables/debt mean
def paa_f045_payables_and_accruals_per_debt_504d_base_v025_signal(payables, debt):
    result = _mean(_payables_and_accruals_scaled(payables, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d payables per share times closeadj
def paa_f045_payables_and_accruals_pershare_21d_base_v026_signal(payables, sharesbas, closeadj):
    ps = _payables_and_accruals_per_share(payables, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d payables per share times closeadj
def paa_f045_payables_and_accruals_pershare_63d_base_v027_signal(payables, sharesbas, closeadj):
    ps = _payables_and_accruals_per_share(payables, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d payables per share times closeadj
def paa_f045_payables_and_accruals_pershare_126d_base_v028_signal(payables, sharesbas, closeadj):
    ps = _payables_and_accruals_per_share(payables, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d payables per share times closeadj
def paa_f045_payables_and_accruals_pershare_252d_base_v029_signal(payables, sharesbas, closeadj):
    ps = _payables_and_accruals_per_share(payables, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d payables per share times closeadj
def paa_f045_payables_and_accruals_pershare_504d_base_v030_signal(payables, sharesbas, closeadj):
    ps = _payables_and_accruals_per_share(payables, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of payables times closeadj
def paa_f045_payables_and_accruals_std_63d_base_v031_signal(payables, closeadj):
    result = _std(payables, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of payables times closeadj
def paa_f045_payables_and_accruals_std_252d_base_v032_signal(payables, closeadj):
    result = _std(payables, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of payables times closeadj
def paa_f045_payables_and_accruals_std_504d_base_v033_signal(payables, closeadj):
    result = _std(payables, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of payables
def paa_f045_payables_and_accruals_z_252d_base_v034_signal(payables):
    result = _z(payables, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of payables
def paa_f045_payables_and_accruals_z_504d_base_v035_signal(payables):
    result = _z(payables, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(payables)
def paa_f045_payables_and_accruals_logz_252d_base_v036_signal(payables):
    result = _z(_payables_and_accruals_log(payables), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(payables)
def paa_f045_payables_and_accruals_logz_504d_base_v037_signal(payables):
    result = _z(_payables_and_accruals_log(payables), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of payables^2 times closeadj
def paa_f045_payables_and_accruals_sq_63d_base_v038_signal(payables, closeadj):
    result = _mean(payables * payables, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of payables^2 times closeadj
def paa_f045_payables_and_accruals_sq_252d_base_v039_signal(payables, closeadj):
    result = _mean(payables * payables, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(payables) times closeadj
def paa_f045_payables_and_accruals_sign_21d_base_v040_signal(payables, closeadj):
    result = _mean(np.sign(payables), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(payables) times closeadj
def paa_f045_payables_and_accruals_sign_63d_base_v041_signal(payables, closeadj):
    result = _mean(np.sign(payables), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(payables) times closeadj
def paa_f045_payables_and_accruals_sign_252d_base_v042_signal(payables, closeadj):
    result = _mean(np.sign(payables), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d payables/opex mean
def paa_f045_payables_and_accruals_per_opex_63d_base_v043_signal(payables, opex):
    result = _mean(_payables_and_accruals_scaled(payables, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d payables/opex mean
def paa_f045_payables_and_accruals_per_opex_252d_base_v044_signal(payables, opex):
    result = _mean(_payables_and_accruals_scaled(payables, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d payables/ebitda mean
def paa_f045_payables_and_accruals_per_ebitda_63d_base_v045_signal(payables, ebitda):
    result = _mean(_payables_and_accruals_scaled(payables, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d payables/ebitda mean
def paa_f045_payables_and_accruals_per_ebitda_252d_base_v046_signal(payables, ebitda):
    result = _mean(_payables_and_accruals_scaled(payables, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d payables/capex mean
def paa_f045_payables_and_accruals_per_capex_63d_base_v047_signal(payables, capex):
    result = _mean(_payables_and_accruals_scaled(payables, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d payables/capex mean
def paa_f045_payables_and_accruals_per_capex_252d_base_v048_signal(payables, capex):
    result = _mean(_payables_and_accruals_scaled(payables, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d payables/liabilities mean
def paa_f045_payables_and_accruals_per_liabilities_63d_base_v049_signal(payables, liabilities):
    result = _mean(_payables_and_accruals_scaled(payables, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d payables/liabilities mean
def paa_f045_payables_and_accruals_per_liabilities_252d_base_v050_signal(payables, liabilities):
    result = _mean(_payables_and_accruals_scaled(payables, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# payables relative to 252d max times closeadj
def paa_f045_payables_and_accruals_relmax_252d_base_v051_signal(payables, closeadj):
    peak = payables.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (payables / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# payables relative to 504d max times closeadj
def paa_f045_payables_and_accruals_relmax_504d_base_v052_signal(payables, closeadj):
    peak = payables.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (payables / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# payables relative to 252d min times closeadj
def paa_f045_payables_and_accruals_relmin_252d_base_v053_signal(payables, closeadj):
    trough = payables.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (payables / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# payables relative to 504d min times closeadj
def paa_f045_payables_and_accruals_relmin_504d_base_v054_signal(payables, closeadj):
    trough = payables.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (payables / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of payables times closeadj
def paa_f045_payables_and_accruals_pct_21d_base_v055_signal(payables, closeadj):
    result = _pct_change(payables, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of payables times closeadj
def paa_f045_payables_and_accruals_pct_63d_base_v056_signal(payables, closeadj):
    result = _pct_change(payables, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of payables times closeadj
def paa_f045_payables_and_accruals_pct_252d_base_v057_signal(payables, closeadj):
    result = _pct_change(payables, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of payables times closeadj
def paa_f045_payables_and_accruals_sum_63d_base_v058_signal(payables, closeadj):
    result = payables.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of payables times closeadj
def paa_f045_payables_and_accruals_sum_252d_base_v059_signal(payables, closeadj):
    result = payables.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of payables times closeadj
def paa_f045_payables_and_accruals_sum_504d_base_v060_signal(payables, closeadj):
    result = payables.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed payables(63d) / smoothed liabilitiesc(252d) x closeadj
def paa_f045_payables_and_accruals_rom_liabilitiesc_252_63d_base_v061_signal(payables, liabilitiesc, closeadj):
    n = _mean(payables, 63)
    d = _mean(liabilitiesc, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed payables(126d) / smoothed liabilitiesc(504d) x closeadj
def paa_f045_payables_and_accruals_rom_liabilitiesc_504_126d_base_v062_signal(payables, liabilitiesc, closeadj):
    n = _mean(payables, 126)
    d = _mean(liabilitiesc, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed payables(63d) / smoothed assets(252d) x closeadj
def paa_f045_payables_and_accruals_rom_assets_252_63d_base_v063_signal(payables, assets, closeadj):
    n = _mean(payables, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed payables(126d) / smoothed assets(504d) x closeadj
def paa_f045_payables_and_accruals_rom_assets_504_126d_base_v064_signal(payables, assets, closeadj):
    n = _mean(payables, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed payables(63d) / smoothed marketcap(252d) x closeadj
def paa_f045_payables_and_accruals_rom_marketcap_252_63d_base_v065_signal(payables, marketcap, closeadj):
    n = _mean(payables, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed payables(126d) / smoothed marketcap(504d) x closeadj
def paa_f045_payables_and_accruals_rom_marketcap_504_126d_base_v066_signal(payables, marketcap, closeadj):
    n = _mean(payables, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(payables) / std(liabilitiesc)
def paa_f045_payables_and_accruals_volratio_liabilitiesc_252d_base_v067_signal(payables, liabilitiesc):
    n = _std(payables, 252)
    d = _std(liabilitiesc, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(payables) / std(liabilitiesc)
def paa_f045_payables_and_accruals_volratio_liabilitiesc_504d_base_v068_signal(payables, liabilitiesc):
    n = _std(payables, 504)
    d = _std(liabilitiesc, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(payables) / std(assets)
def paa_f045_payables_and_accruals_volratio_assets_252d_base_v069_signal(payables, assets):
    n = _std(payables, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(payables) / std(assets)
def paa_f045_payables_and_accruals_volratio_assets_504d_base_v070_signal(payables, assets):
    n = _std(payables, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed payables times closeadj
def paa_f045_payables_and_accruals_raw_5d_base_v071_signal(payables, closeadj):
    result = _mean(payables, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed payables times closeadj
def paa_f045_payables_and_accruals_raw_1008d_base_v072_signal(payables, closeadj):
    result = _mean(payables, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of payables/liabilitiesc
def paa_f045_payables_and_accruals_log_per_liabilitiesc_252d_base_v073_signal(payables, liabilitiesc):
    s = _payables_and_accruals_scaled(payables, liabilitiesc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of payables/liabilitiesc
def paa_f045_payables_and_accruals_log_per_liabilitiesc_504d_base_v074_signal(payables, liabilitiesc):
    s = _payables_and_accruals_scaled(payables, liabilitiesc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of payables/assets
def paa_f045_payables_and_accruals_log_per_assets_252d_base_v075_signal(payables, assets):
    s = _payables_and_accruals_scaled(payables, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
