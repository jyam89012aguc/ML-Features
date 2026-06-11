"""Family f060 - Non-cash expense composition (Earnings and Quality) | Sharadar tables: SF1 | fields: depamor, sbcomp, netinc, opex | base 001-075"""
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
def _non_cash_expense_mix_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _non_cash_expense_mix_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _non_cash_expense_mix_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed depamor times closeadj
def ncem_f060_non_cash_expense_mix_raw_21d_base_v001_signal(depamor, closeadj):
    result = _mean(depamor, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed depamor times closeadj
def ncem_f060_non_cash_expense_mix_raw_63d_base_v002_signal(depamor, closeadj):
    result = _mean(depamor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed depamor times closeadj
def ncem_f060_non_cash_expense_mix_raw_126d_base_v003_signal(depamor, closeadj):
    result = _mean(depamor, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed depamor times closeadj
def ncem_f060_non_cash_expense_mix_raw_252d_base_v004_signal(depamor, closeadj):
    result = _mean(depamor, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed depamor times closeadj
def ncem_f060_non_cash_expense_mix_raw_504d_base_v005_signal(depamor, closeadj):
    result = _mean(depamor, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(depamor) times closeadj
def ncem_f060_non_cash_expense_mix_log_21d_base_v006_signal(depamor, closeadj):
    result = _mean(_non_cash_expense_mix_log(depamor), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(depamor) times closeadj
def ncem_f060_non_cash_expense_mix_log_63d_base_v007_signal(depamor, closeadj):
    result = _mean(_non_cash_expense_mix_log(depamor), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(depamor) times closeadj
def ncem_f060_non_cash_expense_mix_log_126d_base_v008_signal(depamor, closeadj):
    result = _mean(_non_cash_expense_mix_log(depamor), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(depamor) times closeadj
def ncem_f060_non_cash_expense_mix_log_252d_base_v009_signal(depamor, closeadj):
    result = _mean(_non_cash_expense_mix_log(depamor), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(depamor) times closeadj
def ncem_f060_non_cash_expense_mix_log_504d_base_v010_signal(depamor, closeadj):
    result = _mean(_non_cash_expense_mix_log(depamor), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/sbcomp mean
def ncem_f060_non_cash_expense_mix_per_sbcomp_63d_base_v011_signal(depamor, sbcomp):
    result = _mean(_non_cash_expense_mix_scaled(depamor, sbcomp), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/sbcomp mean
def ncem_f060_non_cash_expense_mix_per_sbcomp_252d_base_v012_signal(depamor, sbcomp):
    result = _mean(_non_cash_expense_mix_scaled(depamor, sbcomp), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d depamor/sbcomp mean
def ncem_f060_non_cash_expense_mix_per_sbcomp_504d_base_v013_signal(depamor, sbcomp):
    result = _mean(_non_cash_expense_mix_scaled(depamor, sbcomp), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/netinc mean
def ncem_f060_non_cash_expense_mix_per_netinc_63d_base_v014_signal(depamor, netinc):
    result = _mean(_non_cash_expense_mix_scaled(depamor, netinc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/netinc mean
def ncem_f060_non_cash_expense_mix_per_netinc_252d_base_v015_signal(depamor, netinc):
    result = _mean(_non_cash_expense_mix_scaled(depamor, netinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d depamor/netinc mean
def ncem_f060_non_cash_expense_mix_per_netinc_504d_base_v016_signal(depamor, netinc):
    result = _mean(_non_cash_expense_mix_scaled(depamor, netinc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/assets mean
def ncem_f060_non_cash_expense_mix_per_assets_63d_base_v017_signal(depamor, assets):
    result = _mean(_non_cash_expense_mix_scaled(depamor, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/assets mean
def ncem_f060_non_cash_expense_mix_per_assets_252d_base_v018_signal(depamor, assets):
    result = _mean(_non_cash_expense_mix_scaled(depamor, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d depamor/assets mean
def ncem_f060_non_cash_expense_mix_per_assets_504d_base_v019_signal(depamor, assets):
    result = _mean(_non_cash_expense_mix_scaled(depamor, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/marketcap mean
def ncem_f060_non_cash_expense_mix_per_marketcap_63d_base_v020_signal(depamor, marketcap):
    result = _mean(_non_cash_expense_mix_scaled(depamor, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/marketcap mean
def ncem_f060_non_cash_expense_mix_per_marketcap_252d_base_v021_signal(depamor, marketcap):
    result = _mean(_non_cash_expense_mix_scaled(depamor, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d depamor/marketcap mean
def ncem_f060_non_cash_expense_mix_per_marketcap_504d_base_v022_signal(depamor, marketcap):
    result = _mean(_non_cash_expense_mix_scaled(depamor, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/equity mean
def ncem_f060_non_cash_expense_mix_per_equity_63d_base_v023_signal(depamor, equity):
    result = _mean(_non_cash_expense_mix_scaled(depamor, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/equity mean
def ncem_f060_non_cash_expense_mix_per_equity_252d_base_v024_signal(depamor, equity):
    result = _mean(_non_cash_expense_mix_scaled(depamor, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d depamor/equity mean
def ncem_f060_non_cash_expense_mix_per_equity_504d_base_v025_signal(depamor, equity):
    result = _mean(_non_cash_expense_mix_scaled(depamor, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d depamor per share times closeadj
def ncem_f060_non_cash_expense_mix_pershare_21d_base_v026_signal(depamor, sharesbas, closeadj):
    ps = _non_cash_expense_mix_per_share(depamor, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor per share times closeadj
def ncem_f060_non_cash_expense_mix_pershare_63d_base_v027_signal(depamor, sharesbas, closeadj):
    ps = _non_cash_expense_mix_per_share(depamor, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d depamor per share times closeadj
def ncem_f060_non_cash_expense_mix_pershare_126d_base_v028_signal(depamor, sharesbas, closeadj):
    ps = _non_cash_expense_mix_per_share(depamor, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor per share times closeadj
def ncem_f060_non_cash_expense_mix_pershare_252d_base_v029_signal(depamor, sharesbas, closeadj):
    ps = _non_cash_expense_mix_per_share(depamor, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d depamor per share times closeadj
def ncem_f060_non_cash_expense_mix_pershare_504d_base_v030_signal(depamor, sharesbas, closeadj):
    ps = _non_cash_expense_mix_per_share(depamor, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of depamor times closeadj
def ncem_f060_non_cash_expense_mix_std_63d_base_v031_signal(depamor, closeadj):
    result = _std(depamor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of depamor times closeadj
def ncem_f060_non_cash_expense_mix_std_252d_base_v032_signal(depamor, closeadj):
    result = _std(depamor, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of depamor times closeadj
def ncem_f060_non_cash_expense_mix_std_504d_base_v033_signal(depamor, closeadj):
    result = _std(depamor, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of depamor
def ncem_f060_non_cash_expense_mix_z_252d_base_v034_signal(depamor):
    result = _z(depamor, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of depamor
def ncem_f060_non_cash_expense_mix_z_504d_base_v035_signal(depamor):
    result = _z(depamor, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(depamor)
def ncem_f060_non_cash_expense_mix_logz_252d_base_v036_signal(depamor):
    result = _z(_non_cash_expense_mix_log(depamor), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(depamor)
def ncem_f060_non_cash_expense_mix_logz_504d_base_v037_signal(depamor):
    result = _z(_non_cash_expense_mix_log(depamor), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of depamor^2 times closeadj
def ncem_f060_non_cash_expense_mix_sq_63d_base_v038_signal(depamor, closeadj):
    result = _mean(depamor * depamor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of depamor^2 times closeadj
def ncem_f060_non_cash_expense_mix_sq_252d_base_v039_signal(depamor, closeadj):
    result = _mean(depamor * depamor, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(depamor) times closeadj
def ncem_f060_non_cash_expense_mix_sign_21d_base_v040_signal(depamor, closeadj):
    result = _mean(np.sign(depamor), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(depamor) times closeadj
def ncem_f060_non_cash_expense_mix_sign_63d_base_v041_signal(depamor, closeadj):
    result = _mean(np.sign(depamor), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(depamor) times closeadj
def ncem_f060_non_cash_expense_mix_sign_252d_base_v042_signal(depamor, closeadj):
    result = _mean(np.sign(depamor), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/opex mean
def ncem_f060_non_cash_expense_mix_per_opex_63d_base_v043_signal(depamor, opex):
    result = _mean(_non_cash_expense_mix_scaled(depamor, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/opex mean
def ncem_f060_non_cash_expense_mix_per_opex_252d_base_v044_signal(depamor, opex):
    result = _mean(_non_cash_expense_mix_scaled(depamor, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/ebitda mean
def ncem_f060_non_cash_expense_mix_per_ebitda_63d_base_v045_signal(depamor, ebitda):
    result = _mean(_non_cash_expense_mix_scaled(depamor, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/ebitda mean
def ncem_f060_non_cash_expense_mix_per_ebitda_252d_base_v046_signal(depamor, ebitda):
    result = _mean(_non_cash_expense_mix_scaled(depamor, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/capex mean
def ncem_f060_non_cash_expense_mix_per_capex_63d_base_v047_signal(depamor, capex):
    result = _mean(_non_cash_expense_mix_scaled(depamor, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/capex mean
def ncem_f060_non_cash_expense_mix_per_capex_252d_base_v048_signal(depamor, capex):
    result = _mean(_non_cash_expense_mix_scaled(depamor, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d depamor/liabilities mean
def ncem_f060_non_cash_expense_mix_per_liabilities_63d_base_v049_signal(depamor, liabilities):
    result = _mean(_non_cash_expense_mix_scaled(depamor, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d depamor/liabilities mean
def ncem_f060_non_cash_expense_mix_per_liabilities_252d_base_v050_signal(depamor, liabilities):
    result = _mean(_non_cash_expense_mix_scaled(depamor, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# depamor relative to 252d max times closeadj
def ncem_f060_non_cash_expense_mix_relmax_252d_base_v051_signal(depamor, closeadj):
    peak = depamor.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (depamor / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# depamor relative to 504d max times closeadj
def ncem_f060_non_cash_expense_mix_relmax_504d_base_v052_signal(depamor, closeadj):
    peak = depamor.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (depamor / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# depamor relative to 252d min times closeadj
def ncem_f060_non_cash_expense_mix_relmin_252d_base_v053_signal(depamor, closeadj):
    trough = depamor.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (depamor / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# depamor relative to 504d min times closeadj
def ncem_f060_non_cash_expense_mix_relmin_504d_base_v054_signal(depamor, closeadj):
    trough = depamor.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (depamor / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of depamor times closeadj
def ncem_f060_non_cash_expense_mix_pct_21d_base_v055_signal(depamor, closeadj):
    result = _pct_change(depamor, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of depamor times closeadj
def ncem_f060_non_cash_expense_mix_pct_63d_base_v056_signal(depamor, closeadj):
    result = _pct_change(depamor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of depamor times closeadj
def ncem_f060_non_cash_expense_mix_pct_252d_base_v057_signal(depamor, closeadj):
    result = _pct_change(depamor, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of depamor times closeadj
def ncem_f060_non_cash_expense_mix_sum_63d_base_v058_signal(depamor, closeadj):
    result = depamor.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of depamor times closeadj
def ncem_f060_non_cash_expense_mix_sum_252d_base_v059_signal(depamor, closeadj):
    result = depamor.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of depamor times closeadj
def ncem_f060_non_cash_expense_mix_sum_504d_base_v060_signal(depamor, closeadj):
    result = depamor.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed depamor(63d) / smoothed sbcomp(252d) x closeadj
def ncem_f060_non_cash_expense_mix_rom_sbcomp_252_63d_base_v061_signal(depamor, sbcomp, closeadj):
    n = _mean(depamor, 63)
    d = _mean(sbcomp, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed depamor(126d) / smoothed sbcomp(504d) x closeadj
def ncem_f060_non_cash_expense_mix_rom_sbcomp_504_126d_base_v062_signal(depamor, sbcomp, closeadj):
    n = _mean(depamor, 126)
    d = _mean(sbcomp, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed depamor(63d) / smoothed netinc(252d) x closeadj
def ncem_f060_non_cash_expense_mix_rom_netinc_252_63d_base_v063_signal(depamor, netinc, closeadj):
    n = _mean(depamor, 63)
    d = _mean(netinc, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed depamor(126d) / smoothed netinc(504d) x closeadj
def ncem_f060_non_cash_expense_mix_rom_netinc_504_126d_base_v064_signal(depamor, netinc, closeadj):
    n = _mean(depamor, 126)
    d = _mean(netinc, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed depamor(63d) / smoothed assets(252d) x closeadj
def ncem_f060_non_cash_expense_mix_rom_assets_252_63d_base_v065_signal(depamor, assets, closeadj):
    n = _mean(depamor, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed depamor(126d) / smoothed assets(504d) x closeadj
def ncem_f060_non_cash_expense_mix_rom_assets_504_126d_base_v066_signal(depamor, assets, closeadj):
    n = _mean(depamor, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(depamor) / std(sbcomp)
def ncem_f060_non_cash_expense_mix_volratio_sbcomp_252d_base_v067_signal(depamor, sbcomp):
    n = _std(depamor, 252)
    d = _std(sbcomp, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(depamor) / std(sbcomp)
def ncem_f060_non_cash_expense_mix_volratio_sbcomp_504d_base_v068_signal(depamor, sbcomp):
    n = _std(depamor, 504)
    d = _std(sbcomp, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(depamor) / std(netinc)
def ncem_f060_non_cash_expense_mix_volratio_netinc_252d_base_v069_signal(depamor, netinc):
    n = _std(depamor, 252)
    d = _std(netinc, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(depamor) / std(netinc)
def ncem_f060_non_cash_expense_mix_volratio_netinc_504d_base_v070_signal(depamor, netinc):
    n = _std(depamor, 504)
    d = _std(netinc, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed depamor times closeadj
def ncem_f060_non_cash_expense_mix_raw_5d_base_v071_signal(depamor, closeadj):
    result = _mean(depamor, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed depamor times closeadj
def ncem_f060_non_cash_expense_mix_raw_1008d_base_v072_signal(depamor, closeadj):
    result = _mean(depamor, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of depamor/sbcomp
def ncem_f060_non_cash_expense_mix_log_per_sbcomp_252d_base_v073_signal(depamor, sbcomp):
    s = _non_cash_expense_mix_scaled(depamor, sbcomp)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of depamor/sbcomp
def ncem_f060_non_cash_expense_mix_log_per_sbcomp_504d_base_v074_signal(depamor, sbcomp):
    s = _non_cash_expense_mix_scaled(depamor, sbcomp)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of depamor/netinc
def ncem_f060_non_cash_expense_mix_log_per_netinc_252d_base_v075_signal(depamor, netinc):
    s = _non_cash_expense_mix_scaled(depamor, netinc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
