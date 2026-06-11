"""Family f085 - Field availability and schema coverage (Security Master and Universe) | Sharadar tables: INDICATORS | fields: table, indicator, title, description | base 001-075"""
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
def _indicator_availability_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _indicator_availability_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _indicator_availability_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed field_coverage times closeadj
def ia_f085_indicator_availability_raw_21d_base_v001_signal(field_coverage, closeadj):
    result = _mean(field_coverage, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed field_coverage times closeadj
def ia_f085_indicator_availability_raw_63d_base_v002_signal(field_coverage, closeadj):
    result = _mean(field_coverage, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed field_coverage times closeadj
def ia_f085_indicator_availability_raw_126d_base_v003_signal(field_coverage, closeadj):
    result = _mean(field_coverage, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed field_coverage times closeadj
def ia_f085_indicator_availability_raw_252d_base_v004_signal(field_coverage, closeadj):
    result = _mean(field_coverage, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed field_coverage times closeadj
def ia_f085_indicator_availability_raw_504d_base_v005_signal(field_coverage, closeadj):
    result = _mean(field_coverage, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(field_coverage) times closeadj
def ia_f085_indicator_availability_log_21d_base_v006_signal(field_coverage, closeadj):
    result = _mean(_indicator_availability_log(field_coverage), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(field_coverage) times closeadj
def ia_f085_indicator_availability_log_63d_base_v007_signal(field_coverage, closeadj):
    result = _mean(_indicator_availability_log(field_coverage), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(field_coverage) times closeadj
def ia_f085_indicator_availability_log_126d_base_v008_signal(field_coverage, closeadj):
    result = _mean(_indicator_availability_log(field_coverage), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(field_coverage) times closeadj
def ia_f085_indicator_availability_log_252d_base_v009_signal(field_coverage, closeadj):
    result = _mean(_indicator_availability_log(field_coverage), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(field_coverage) times closeadj
def ia_f085_indicator_availability_log_504d_base_v010_signal(field_coverage, closeadj):
    result = _mean(_indicator_availability_log(field_coverage), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d field_coverage/indicator mean
def ia_f085_indicator_availability_per_indicator_63d_base_v011_signal(field_coverage, indicator):
    result = _mean(_indicator_availability_scaled(field_coverage, indicator), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d field_coverage/indicator mean
def ia_f085_indicator_availability_per_indicator_252d_base_v012_signal(field_coverage, indicator):
    result = _mean(_indicator_availability_scaled(field_coverage, indicator), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d field_coverage/indicator mean
def ia_f085_indicator_availability_per_indicator_504d_base_v013_signal(field_coverage, indicator):
    result = _mean(_indicator_availability_scaled(field_coverage, indicator), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d field_coverage/assets mean
def ia_f085_indicator_availability_per_assets_63d_base_v014_signal(field_coverage, assets):
    result = _mean(_indicator_availability_scaled(field_coverage, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d field_coverage/assets mean
def ia_f085_indicator_availability_per_assets_252d_base_v015_signal(field_coverage, assets):
    result = _mean(_indicator_availability_scaled(field_coverage, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d field_coverage/assets mean
def ia_f085_indicator_availability_per_assets_504d_base_v016_signal(field_coverage, assets):
    result = _mean(_indicator_availability_scaled(field_coverage, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d field_coverage/marketcap mean
def ia_f085_indicator_availability_per_marketcap_63d_base_v017_signal(field_coverage, marketcap):
    result = _mean(_indicator_availability_scaled(field_coverage, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d field_coverage/marketcap mean
def ia_f085_indicator_availability_per_marketcap_252d_base_v018_signal(field_coverage, marketcap):
    result = _mean(_indicator_availability_scaled(field_coverage, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d field_coverage/marketcap mean
def ia_f085_indicator_availability_per_marketcap_504d_base_v019_signal(field_coverage, marketcap):
    result = _mean(_indicator_availability_scaled(field_coverage, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d field_coverage/equity mean
def ia_f085_indicator_availability_per_equity_63d_base_v020_signal(field_coverage, equity):
    result = _mean(_indicator_availability_scaled(field_coverage, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d field_coverage/equity mean
def ia_f085_indicator_availability_per_equity_252d_base_v021_signal(field_coverage, equity):
    result = _mean(_indicator_availability_scaled(field_coverage, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d field_coverage/equity mean
def ia_f085_indicator_availability_per_equity_504d_base_v022_signal(field_coverage, equity):
    result = _mean(_indicator_availability_scaled(field_coverage, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d field_coverage/debt mean
def ia_f085_indicator_availability_per_debt_63d_base_v023_signal(field_coverage, debt):
    result = _mean(_indicator_availability_scaled(field_coverage, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d field_coverage/debt mean
def ia_f085_indicator_availability_per_debt_252d_base_v024_signal(field_coverage, debt):
    result = _mean(_indicator_availability_scaled(field_coverage, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d field_coverage/debt mean
def ia_f085_indicator_availability_per_debt_504d_base_v025_signal(field_coverage, debt):
    result = _mean(_indicator_availability_scaled(field_coverage, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d field_coverage per share times closeadj
def ia_f085_indicator_availability_pershare_21d_base_v026_signal(field_coverage, sharesbas, closeadj):
    ps = _indicator_availability_per_share(field_coverage, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d field_coverage per share times closeadj
def ia_f085_indicator_availability_pershare_63d_base_v027_signal(field_coverage, sharesbas, closeadj):
    ps = _indicator_availability_per_share(field_coverage, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d field_coverage per share times closeadj
def ia_f085_indicator_availability_pershare_126d_base_v028_signal(field_coverage, sharesbas, closeadj):
    ps = _indicator_availability_per_share(field_coverage, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d field_coverage per share times closeadj
def ia_f085_indicator_availability_pershare_252d_base_v029_signal(field_coverage, sharesbas, closeadj):
    ps = _indicator_availability_per_share(field_coverage, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d field_coverage per share times closeadj
def ia_f085_indicator_availability_pershare_504d_base_v030_signal(field_coverage, sharesbas, closeadj):
    ps = _indicator_availability_per_share(field_coverage, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of field_coverage times closeadj
def ia_f085_indicator_availability_std_63d_base_v031_signal(field_coverage, closeadj):
    result = _std(field_coverage, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of field_coverage times closeadj
def ia_f085_indicator_availability_std_252d_base_v032_signal(field_coverage, closeadj):
    result = _std(field_coverage, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of field_coverage times closeadj
def ia_f085_indicator_availability_std_504d_base_v033_signal(field_coverage, closeadj):
    result = _std(field_coverage, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of field_coverage
def ia_f085_indicator_availability_z_252d_base_v034_signal(field_coverage):
    result = _z(field_coverage, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of field_coverage
def ia_f085_indicator_availability_z_504d_base_v035_signal(field_coverage):
    result = _z(field_coverage, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(field_coverage)
def ia_f085_indicator_availability_logz_252d_base_v036_signal(field_coverage):
    result = _z(_indicator_availability_log(field_coverage), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(field_coverage)
def ia_f085_indicator_availability_logz_504d_base_v037_signal(field_coverage):
    result = _z(_indicator_availability_log(field_coverage), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of field_coverage^2 times closeadj
def ia_f085_indicator_availability_sq_63d_base_v038_signal(field_coverage, closeadj):
    result = _mean(field_coverage * field_coverage, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of field_coverage^2 times closeadj
def ia_f085_indicator_availability_sq_252d_base_v039_signal(field_coverage, closeadj):
    result = _mean(field_coverage * field_coverage, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(field_coverage) times closeadj
def ia_f085_indicator_availability_sign_21d_base_v040_signal(field_coverage, closeadj):
    result = _mean(np.sign(field_coverage), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(field_coverage) times closeadj
def ia_f085_indicator_availability_sign_63d_base_v041_signal(field_coverage, closeadj):
    result = _mean(np.sign(field_coverage), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(field_coverage) times closeadj
def ia_f085_indicator_availability_sign_252d_base_v042_signal(field_coverage, closeadj):
    result = _mean(np.sign(field_coverage), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d field_coverage/opex mean
def ia_f085_indicator_availability_per_opex_63d_base_v043_signal(field_coverage, opex):
    result = _mean(_indicator_availability_scaled(field_coverage, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d field_coverage/opex mean
def ia_f085_indicator_availability_per_opex_252d_base_v044_signal(field_coverage, opex):
    result = _mean(_indicator_availability_scaled(field_coverage, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d field_coverage/ebitda mean
def ia_f085_indicator_availability_per_ebitda_63d_base_v045_signal(field_coverage, ebitda):
    result = _mean(_indicator_availability_scaled(field_coverage, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d field_coverage/ebitda mean
def ia_f085_indicator_availability_per_ebitda_252d_base_v046_signal(field_coverage, ebitda):
    result = _mean(_indicator_availability_scaled(field_coverage, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d field_coverage/capex mean
def ia_f085_indicator_availability_per_capex_63d_base_v047_signal(field_coverage, capex):
    result = _mean(_indicator_availability_scaled(field_coverage, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d field_coverage/capex mean
def ia_f085_indicator_availability_per_capex_252d_base_v048_signal(field_coverage, capex):
    result = _mean(_indicator_availability_scaled(field_coverage, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d field_coverage/liabilities mean
def ia_f085_indicator_availability_per_liabilities_63d_base_v049_signal(field_coverage, liabilities):
    result = _mean(_indicator_availability_scaled(field_coverage, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d field_coverage/liabilities mean
def ia_f085_indicator_availability_per_liabilities_252d_base_v050_signal(field_coverage, liabilities):
    result = _mean(_indicator_availability_scaled(field_coverage, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# field_coverage relative to 252d max times closeadj
def ia_f085_indicator_availability_relmax_252d_base_v051_signal(field_coverage, closeadj):
    peak = field_coverage.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (field_coverage / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# field_coverage relative to 504d max times closeadj
def ia_f085_indicator_availability_relmax_504d_base_v052_signal(field_coverage, closeadj):
    peak = field_coverage.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (field_coverage / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# field_coverage relative to 252d min times closeadj
def ia_f085_indicator_availability_relmin_252d_base_v053_signal(field_coverage, closeadj):
    trough = field_coverage.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (field_coverage / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# field_coverage relative to 504d min times closeadj
def ia_f085_indicator_availability_relmin_504d_base_v054_signal(field_coverage, closeadj):
    trough = field_coverage.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (field_coverage / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of field_coverage times closeadj
def ia_f085_indicator_availability_pct_21d_base_v055_signal(field_coverage, closeadj):
    result = _pct_change(field_coverage, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of field_coverage times closeadj
def ia_f085_indicator_availability_pct_63d_base_v056_signal(field_coverage, closeadj):
    result = _pct_change(field_coverage, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of field_coverage times closeadj
def ia_f085_indicator_availability_pct_252d_base_v057_signal(field_coverage, closeadj):
    result = _pct_change(field_coverage, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of field_coverage times closeadj
def ia_f085_indicator_availability_sum_63d_base_v058_signal(field_coverage, closeadj):
    result = field_coverage.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of field_coverage times closeadj
def ia_f085_indicator_availability_sum_252d_base_v059_signal(field_coverage, closeadj):
    result = field_coverage.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of field_coverage times closeadj
def ia_f085_indicator_availability_sum_504d_base_v060_signal(field_coverage, closeadj):
    result = field_coverage.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed field_coverage(63d) / smoothed indicator(252d) x closeadj
def ia_f085_indicator_availability_rom_indicator_252_63d_base_v061_signal(field_coverage, indicator, closeadj):
    n = _mean(field_coverage, 63)
    d = _mean(indicator, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed field_coverage(126d) / smoothed indicator(504d) x closeadj
def ia_f085_indicator_availability_rom_indicator_504_126d_base_v062_signal(field_coverage, indicator, closeadj):
    n = _mean(field_coverage, 126)
    d = _mean(indicator, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed field_coverage(63d) / smoothed assets(252d) x closeadj
def ia_f085_indicator_availability_rom_assets_252_63d_base_v063_signal(field_coverage, assets, closeadj):
    n = _mean(field_coverage, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed field_coverage(126d) / smoothed assets(504d) x closeadj
def ia_f085_indicator_availability_rom_assets_504_126d_base_v064_signal(field_coverage, assets, closeadj):
    n = _mean(field_coverage, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed field_coverage(63d) / smoothed marketcap(252d) x closeadj
def ia_f085_indicator_availability_rom_marketcap_252_63d_base_v065_signal(field_coverage, marketcap, closeadj):
    n = _mean(field_coverage, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed field_coverage(126d) / smoothed marketcap(504d) x closeadj
def ia_f085_indicator_availability_rom_marketcap_504_126d_base_v066_signal(field_coverage, marketcap, closeadj):
    n = _mean(field_coverage, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(field_coverage) / std(indicator)
def ia_f085_indicator_availability_volratio_indicator_252d_base_v067_signal(field_coverage, indicator):
    n = _std(field_coverage, 252)
    d = _std(indicator, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(field_coverage) / std(indicator)
def ia_f085_indicator_availability_volratio_indicator_504d_base_v068_signal(field_coverage, indicator):
    n = _std(field_coverage, 504)
    d = _std(indicator, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(field_coverage) / std(assets)
def ia_f085_indicator_availability_volratio_assets_252d_base_v069_signal(field_coverage, assets):
    n = _std(field_coverage, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(field_coverage) / std(assets)
def ia_f085_indicator_availability_volratio_assets_504d_base_v070_signal(field_coverage, assets):
    n = _std(field_coverage, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed field_coverage times closeadj
def ia_f085_indicator_availability_raw_5d_base_v071_signal(field_coverage, closeadj):
    result = _mean(field_coverage, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed field_coverage times closeadj
def ia_f085_indicator_availability_raw_1008d_base_v072_signal(field_coverage, closeadj):
    result = _mean(field_coverage, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of field_coverage/indicator
def ia_f085_indicator_availability_log_per_indicator_252d_base_v073_signal(field_coverage, indicator):
    s = _indicator_availability_scaled(field_coverage, indicator)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of field_coverage/indicator
def ia_f085_indicator_availability_log_per_indicator_504d_base_v074_signal(field_coverage, indicator):
    s = _indicator_availability_scaled(field_coverage, indicator)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of field_coverage/assets
def ia_f085_indicator_availability_log_per_assets_252d_base_v075_signal(field_coverage, assets):
    s = _indicator_availability_scaled(field_coverage, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
