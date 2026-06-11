"""Family f023 - Current versus long-term debt mix (Capital Structure) | Sharadar tables: SF1 | fields: debtc, debtnc, debt | base 001-075"""
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
def _debt_maturity_mix_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _debt_maturity_mix_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _debt_maturity_mix_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed debtc times closeadj
def dmm_f023_debt_maturity_mix_raw_21d_base_v001_signal(debtc, closeadj):
    result = _mean(debtc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed debtc times closeadj
def dmm_f023_debt_maturity_mix_raw_63d_base_v002_signal(debtc, closeadj):
    result = _mean(debtc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed debtc times closeadj
def dmm_f023_debt_maturity_mix_raw_126d_base_v003_signal(debtc, closeadj):
    result = _mean(debtc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed debtc times closeadj
def dmm_f023_debt_maturity_mix_raw_252d_base_v004_signal(debtc, closeadj):
    result = _mean(debtc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed debtc times closeadj
def dmm_f023_debt_maturity_mix_raw_504d_base_v005_signal(debtc, closeadj):
    result = _mean(debtc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(debtc) times closeadj
def dmm_f023_debt_maturity_mix_log_21d_base_v006_signal(debtc, closeadj):
    result = _mean(_debt_maturity_mix_log(debtc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(debtc) times closeadj
def dmm_f023_debt_maturity_mix_log_63d_base_v007_signal(debtc, closeadj):
    result = _mean(_debt_maturity_mix_log(debtc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(debtc) times closeadj
def dmm_f023_debt_maturity_mix_log_126d_base_v008_signal(debtc, closeadj):
    result = _mean(_debt_maturity_mix_log(debtc), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(debtc) times closeadj
def dmm_f023_debt_maturity_mix_log_252d_base_v009_signal(debtc, closeadj):
    result = _mean(_debt_maturity_mix_log(debtc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(debtc) times closeadj
def dmm_f023_debt_maturity_mix_log_504d_base_v010_signal(debtc, closeadj):
    result = _mean(_debt_maturity_mix_log(debtc), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debtc/debtnc mean
def dmm_f023_debt_maturity_mix_per_debtnc_63d_base_v011_signal(debtc, debtnc):
    result = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debtc/debtnc mean
def dmm_f023_debt_maturity_mix_per_debtnc_252d_base_v012_signal(debtc, debtnc):
    result = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debtc/debtnc mean
def dmm_f023_debt_maturity_mix_per_debtnc_504d_base_v013_signal(debtc, debtnc):
    result = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debtc/debt mean
def dmm_f023_debt_maturity_mix_per_debt_63d_base_v014_signal(debtc, debt):
    result = _mean(_debt_maturity_mix_scaled(debtc, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debtc/debt mean
def dmm_f023_debt_maturity_mix_per_debt_252d_base_v015_signal(debtc, debt):
    result = _mean(_debt_maturity_mix_scaled(debtc, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debtc/debt mean
def dmm_f023_debt_maturity_mix_per_debt_504d_base_v016_signal(debtc, debt):
    result = _mean(_debt_maturity_mix_scaled(debtc, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debtc/assets mean
def dmm_f023_debt_maturity_mix_per_assets_63d_base_v017_signal(debtc, assets):
    result = _mean(_debt_maturity_mix_scaled(debtc, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debtc/assets mean
def dmm_f023_debt_maturity_mix_per_assets_252d_base_v018_signal(debtc, assets):
    result = _mean(_debt_maturity_mix_scaled(debtc, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debtc/assets mean
def dmm_f023_debt_maturity_mix_per_assets_504d_base_v019_signal(debtc, assets):
    result = _mean(_debt_maturity_mix_scaled(debtc, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debtc/marketcap mean
def dmm_f023_debt_maturity_mix_per_marketcap_63d_base_v020_signal(debtc, marketcap):
    result = _mean(_debt_maturity_mix_scaled(debtc, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debtc/marketcap mean
def dmm_f023_debt_maturity_mix_per_marketcap_252d_base_v021_signal(debtc, marketcap):
    result = _mean(_debt_maturity_mix_scaled(debtc, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debtc/marketcap mean
def dmm_f023_debt_maturity_mix_per_marketcap_504d_base_v022_signal(debtc, marketcap):
    result = _mean(_debt_maturity_mix_scaled(debtc, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debtc/equity mean
def dmm_f023_debt_maturity_mix_per_equity_63d_base_v023_signal(debtc, equity):
    result = _mean(_debt_maturity_mix_scaled(debtc, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debtc/equity mean
def dmm_f023_debt_maturity_mix_per_equity_252d_base_v024_signal(debtc, equity):
    result = _mean(_debt_maturity_mix_scaled(debtc, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debtc/equity mean
def dmm_f023_debt_maturity_mix_per_equity_504d_base_v025_signal(debtc, equity):
    result = _mean(_debt_maturity_mix_scaled(debtc, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debtc per share times closeadj
def dmm_f023_debt_maturity_mix_pershare_21d_base_v026_signal(debtc, sharesbas, closeadj):
    ps = _debt_maturity_mix_per_share(debtc, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debtc per share times closeadj
def dmm_f023_debt_maturity_mix_pershare_63d_base_v027_signal(debtc, sharesbas, closeadj):
    ps = _debt_maturity_mix_per_share(debtc, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d debtc per share times closeadj
def dmm_f023_debt_maturity_mix_pershare_126d_base_v028_signal(debtc, sharesbas, closeadj):
    ps = _debt_maturity_mix_per_share(debtc, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debtc per share times closeadj
def dmm_f023_debt_maturity_mix_pershare_252d_base_v029_signal(debtc, sharesbas, closeadj):
    ps = _debt_maturity_mix_per_share(debtc, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debtc per share times closeadj
def dmm_f023_debt_maturity_mix_pershare_504d_base_v030_signal(debtc, sharesbas, closeadj):
    ps = _debt_maturity_mix_per_share(debtc, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of debtc times closeadj
def dmm_f023_debt_maturity_mix_std_63d_base_v031_signal(debtc, closeadj):
    result = _std(debtc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of debtc times closeadj
def dmm_f023_debt_maturity_mix_std_252d_base_v032_signal(debtc, closeadj):
    result = _std(debtc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of debtc times closeadj
def dmm_f023_debt_maturity_mix_std_504d_base_v033_signal(debtc, closeadj):
    result = _std(debtc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of debtc
def dmm_f023_debt_maturity_mix_z_252d_base_v034_signal(debtc):
    result = _z(debtc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of debtc
def dmm_f023_debt_maturity_mix_z_504d_base_v035_signal(debtc):
    result = _z(debtc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(debtc)
def dmm_f023_debt_maturity_mix_logz_252d_base_v036_signal(debtc):
    result = _z(_debt_maturity_mix_log(debtc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(debtc)
def dmm_f023_debt_maturity_mix_logz_504d_base_v037_signal(debtc):
    result = _z(_debt_maturity_mix_log(debtc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of debtc^2 times closeadj
def dmm_f023_debt_maturity_mix_sq_63d_base_v038_signal(debtc, closeadj):
    result = _mean(debtc * debtc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of debtc^2 times closeadj
def dmm_f023_debt_maturity_mix_sq_252d_base_v039_signal(debtc, closeadj):
    result = _mean(debtc * debtc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(debtc) times closeadj
def dmm_f023_debt_maturity_mix_sign_21d_base_v040_signal(debtc, closeadj):
    result = _mean(np.sign(debtc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(debtc) times closeadj
def dmm_f023_debt_maturity_mix_sign_63d_base_v041_signal(debtc, closeadj):
    result = _mean(np.sign(debtc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(debtc) times closeadj
def dmm_f023_debt_maturity_mix_sign_252d_base_v042_signal(debtc, closeadj):
    result = _mean(np.sign(debtc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debtc/opex mean
def dmm_f023_debt_maturity_mix_per_opex_63d_base_v043_signal(debtc, opex):
    result = _mean(_debt_maturity_mix_scaled(debtc, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debtc/opex mean
def dmm_f023_debt_maturity_mix_per_opex_252d_base_v044_signal(debtc, opex):
    result = _mean(_debt_maturity_mix_scaled(debtc, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debtc/ebitda mean
def dmm_f023_debt_maturity_mix_per_ebitda_63d_base_v045_signal(debtc, ebitda):
    result = _mean(_debt_maturity_mix_scaled(debtc, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debtc/ebitda mean
def dmm_f023_debt_maturity_mix_per_ebitda_252d_base_v046_signal(debtc, ebitda):
    result = _mean(_debt_maturity_mix_scaled(debtc, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debtc/capex mean
def dmm_f023_debt_maturity_mix_per_capex_63d_base_v047_signal(debtc, capex):
    result = _mean(_debt_maturity_mix_scaled(debtc, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debtc/capex mean
def dmm_f023_debt_maturity_mix_per_capex_252d_base_v048_signal(debtc, capex):
    result = _mean(_debt_maturity_mix_scaled(debtc, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debtc/liabilities mean
def dmm_f023_debt_maturity_mix_per_liabilities_63d_base_v049_signal(debtc, liabilities):
    result = _mean(_debt_maturity_mix_scaled(debtc, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debtc/liabilities mean
def dmm_f023_debt_maturity_mix_per_liabilities_252d_base_v050_signal(debtc, liabilities):
    result = _mean(_debt_maturity_mix_scaled(debtc, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# debtc relative to 252d max times closeadj
def dmm_f023_debt_maturity_mix_relmax_252d_base_v051_signal(debtc, closeadj):
    peak = debtc.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (debtc / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debtc relative to 504d max times closeadj
def dmm_f023_debt_maturity_mix_relmax_504d_base_v052_signal(debtc, closeadj):
    peak = debtc.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (debtc / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debtc relative to 252d min times closeadj
def dmm_f023_debt_maturity_mix_relmin_252d_base_v053_signal(debtc, closeadj):
    trough = debtc.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (debtc / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debtc relative to 504d min times closeadj
def dmm_f023_debt_maturity_mix_relmin_504d_base_v054_signal(debtc, closeadj):
    trough = debtc.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (debtc / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of debtc times closeadj
def dmm_f023_debt_maturity_mix_pct_21d_base_v055_signal(debtc, closeadj):
    result = _pct_change(debtc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of debtc times closeadj
def dmm_f023_debt_maturity_mix_pct_63d_base_v056_signal(debtc, closeadj):
    result = _pct_change(debtc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of debtc times closeadj
def dmm_f023_debt_maturity_mix_pct_252d_base_v057_signal(debtc, closeadj):
    result = _pct_change(debtc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of debtc times closeadj
def dmm_f023_debt_maturity_mix_sum_63d_base_v058_signal(debtc, closeadj):
    result = debtc.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of debtc times closeadj
def dmm_f023_debt_maturity_mix_sum_252d_base_v059_signal(debtc, closeadj):
    result = debtc.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of debtc times closeadj
def dmm_f023_debt_maturity_mix_sum_504d_base_v060_signal(debtc, closeadj):
    result = debtc.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed debtc(63d) / smoothed debtnc(252d) x closeadj
def dmm_f023_debt_maturity_mix_rom_debtnc_252_63d_base_v061_signal(debtc, debtnc, closeadj):
    n = _mean(debtc, 63)
    d = _mean(debtnc, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed debtc(126d) / smoothed debtnc(504d) x closeadj
def dmm_f023_debt_maturity_mix_rom_debtnc_504_126d_base_v062_signal(debtc, debtnc, closeadj):
    n = _mean(debtc, 126)
    d = _mean(debtnc, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed debtc(63d) / smoothed debt(252d) x closeadj
def dmm_f023_debt_maturity_mix_rom_debt_252_63d_base_v063_signal(debtc, debt, closeadj):
    n = _mean(debtc, 63)
    d = _mean(debt, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed debtc(126d) / smoothed debt(504d) x closeadj
def dmm_f023_debt_maturity_mix_rom_debt_504_126d_base_v064_signal(debtc, debt, closeadj):
    n = _mean(debtc, 126)
    d = _mean(debt, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed debtc(63d) / smoothed assets(252d) x closeadj
def dmm_f023_debt_maturity_mix_rom_assets_252_63d_base_v065_signal(debtc, assets, closeadj):
    n = _mean(debtc, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed debtc(126d) / smoothed assets(504d) x closeadj
def dmm_f023_debt_maturity_mix_rom_assets_504_126d_base_v066_signal(debtc, assets, closeadj):
    n = _mean(debtc, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(debtc) / std(debtnc)
def dmm_f023_debt_maturity_mix_volratio_debtnc_252d_base_v067_signal(debtc, debtnc):
    n = _std(debtc, 252)
    d = _std(debtnc, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(debtc) / std(debtnc)
def dmm_f023_debt_maturity_mix_volratio_debtnc_504d_base_v068_signal(debtc, debtnc):
    n = _std(debtc, 504)
    d = _std(debtnc, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(debtc) / std(debt)
def dmm_f023_debt_maturity_mix_volratio_debt_252d_base_v069_signal(debtc, debt):
    n = _std(debtc, 252)
    d = _std(debt, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(debtc) / std(debt)
def dmm_f023_debt_maturity_mix_volratio_debt_504d_base_v070_signal(debtc, debt):
    n = _std(debtc, 504)
    d = _std(debt, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed debtc times closeadj
def dmm_f023_debt_maturity_mix_raw_5d_base_v071_signal(debtc, closeadj):
    result = _mean(debtc, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed debtc times closeadj
def dmm_f023_debt_maturity_mix_raw_1008d_base_v072_signal(debtc, closeadj):
    result = _mean(debtc, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of debtc/debtnc
def dmm_f023_debt_maturity_mix_log_per_debtnc_252d_base_v073_signal(debtc, debtnc):
    s = _debt_maturity_mix_scaled(debtc, debtnc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of debtc/debtnc
def dmm_f023_debt_maturity_mix_log_per_debtnc_504d_base_v074_signal(debtc, debtnc):
    s = _debt_maturity_mix_scaled(debtc, debtnc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of debtc/debt
def dmm_f023_debt_maturity_mix_log_per_debt_252d_base_v075_signal(debtc, debt):
    s = _debt_maturity_mix_scaled(debtc, debt)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
