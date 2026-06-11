"""Family f34 - Equity issuance cadence  (E_Dilution_Shares) | base 001-075"""
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
def _issuance_cadence_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _issuance_cadence_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _issuance_cadence_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed ncfcommon times closeadj
def ica_f34_issuance_cadence_raw_21d_base_v001_signal(ncfcommon, closeadj):
    result = _mean(ncfcommon, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed ncfcommon times closeadj
def ica_f34_issuance_cadence_raw_63d_base_v002_signal(ncfcommon, closeadj):
    result = _mean(ncfcommon, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed ncfcommon times closeadj
def ica_f34_issuance_cadence_raw_126d_base_v003_signal(ncfcommon, closeadj):
    result = _mean(ncfcommon, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed ncfcommon times closeadj
def ica_f34_issuance_cadence_raw_252d_base_v004_signal(ncfcommon, closeadj):
    result = _mean(ncfcommon, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed ncfcommon times closeadj
def ica_f34_issuance_cadence_raw_504d_base_v005_signal(ncfcommon, closeadj):
    result = _mean(ncfcommon, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(ncfcommon) times closeadj
def ica_f34_issuance_cadence_log_21d_base_v006_signal(ncfcommon, closeadj):
    result = _mean(_issuance_cadence_log(ncfcommon), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(ncfcommon) times closeadj
def ica_f34_issuance_cadence_log_63d_base_v007_signal(ncfcommon, closeadj):
    result = _mean(_issuance_cadence_log(ncfcommon), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(ncfcommon) times closeadj
def ica_f34_issuance_cadence_log_126d_base_v008_signal(ncfcommon, closeadj):
    result = _mean(_issuance_cadence_log(ncfcommon), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(ncfcommon) times closeadj
def ica_f34_issuance_cadence_log_252d_base_v009_signal(ncfcommon, closeadj):
    result = _mean(_issuance_cadence_log(ncfcommon), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(ncfcommon) times closeadj
def ica_f34_issuance_cadence_log_504d_base_v010_signal(ncfcommon, closeadj):
    result = _mean(_issuance_cadence_log(ncfcommon), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfcommon/assets mean
def ica_f34_issuance_cadence_per_assets_63d_base_v011_signal(ncfcommon, assets):
    result = _mean(_issuance_cadence_scaled(ncfcommon, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfcommon/assets mean
def ica_f34_issuance_cadence_per_assets_252d_base_v012_signal(ncfcommon, assets):
    result = _mean(_issuance_cadence_scaled(ncfcommon, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfcommon/assets mean
def ica_f34_issuance_cadence_per_assets_504d_base_v013_signal(ncfcommon, assets):
    result = _mean(_issuance_cadence_scaled(ncfcommon, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfcommon/marketcap mean
def ica_f34_issuance_cadence_per_marketcap_63d_base_v014_signal(ncfcommon, marketcap):
    result = _mean(_issuance_cadence_scaled(ncfcommon, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfcommon/marketcap mean
def ica_f34_issuance_cadence_per_marketcap_252d_base_v015_signal(ncfcommon, marketcap):
    result = _mean(_issuance_cadence_scaled(ncfcommon, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfcommon/marketcap mean
def ica_f34_issuance_cadence_per_marketcap_504d_base_v016_signal(ncfcommon, marketcap):
    result = _mean(_issuance_cadence_scaled(ncfcommon, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfcommon/equity mean
def ica_f34_issuance_cadence_per_equity_63d_base_v017_signal(ncfcommon, equity):
    result = _mean(_issuance_cadence_scaled(ncfcommon, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfcommon/equity mean
def ica_f34_issuance_cadence_per_equity_252d_base_v018_signal(ncfcommon, equity):
    result = _mean(_issuance_cadence_scaled(ncfcommon, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfcommon/equity mean
def ica_f34_issuance_cadence_per_equity_504d_base_v019_signal(ncfcommon, equity):
    result = _mean(_issuance_cadence_scaled(ncfcommon, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfcommon/debt mean
def ica_f34_issuance_cadence_per_debt_63d_base_v020_signal(ncfcommon, debt):
    result = _mean(_issuance_cadence_scaled(ncfcommon, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfcommon/debt mean
def ica_f34_issuance_cadence_per_debt_252d_base_v021_signal(ncfcommon, debt):
    result = _mean(_issuance_cadence_scaled(ncfcommon, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfcommon/debt mean
def ica_f34_issuance_cadence_per_debt_504d_base_v022_signal(ncfcommon, debt):
    result = _mean(_issuance_cadence_scaled(ncfcommon, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfcommon/revenue mean
def ica_f34_issuance_cadence_per_revenue_63d_base_v023_signal(ncfcommon, revenue):
    result = _mean(_issuance_cadence_scaled(ncfcommon, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfcommon/revenue mean
def ica_f34_issuance_cadence_per_revenue_252d_base_v024_signal(ncfcommon, revenue):
    result = _mean(_issuance_cadence_scaled(ncfcommon, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfcommon/revenue mean
def ica_f34_issuance_cadence_per_revenue_504d_base_v025_signal(ncfcommon, revenue):
    result = _mean(_issuance_cadence_scaled(ncfcommon, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfcommon per share times closeadj
def ica_f34_issuance_cadence_pershare_21d_base_v026_signal(ncfcommon, sharesbas, closeadj):
    ps = _issuance_cadence_per_share(ncfcommon, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfcommon per share times closeadj
def ica_f34_issuance_cadence_pershare_63d_base_v027_signal(ncfcommon, sharesbas, closeadj):
    ps = _issuance_cadence_per_share(ncfcommon, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ncfcommon per share times closeadj
def ica_f34_issuance_cadence_pershare_126d_base_v028_signal(ncfcommon, sharesbas, closeadj):
    ps = _issuance_cadence_per_share(ncfcommon, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfcommon per share times closeadj
def ica_f34_issuance_cadence_pershare_252d_base_v029_signal(ncfcommon, sharesbas, closeadj):
    ps = _issuance_cadence_per_share(ncfcommon, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfcommon per share times closeadj
def ica_f34_issuance_cadence_pershare_504d_base_v030_signal(ncfcommon, sharesbas, closeadj):
    ps = _issuance_cadence_per_share(ncfcommon, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of ncfcommon times closeadj
def ica_f34_issuance_cadence_std_63d_base_v031_signal(ncfcommon, closeadj):
    result = _std(ncfcommon, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of ncfcommon times closeadj
def ica_f34_issuance_cadence_std_252d_base_v032_signal(ncfcommon, closeadj):
    result = _std(ncfcommon, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of ncfcommon times closeadj
def ica_f34_issuance_cadence_std_504d_base_v033_signal(ncfcommon, closeadj):
    result = _std(ncfcommon, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of ncfcommon
def ica_f34_issuance_cadence_z_252d_base_v034_signal(ncfcommon):
    result = _z(ncfcommon, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of ncfcommon
def ica_f34_issuance_cadence_z_504d_base_v035_signal(ncfcommon):
    result = _z(ncfcommon, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(ncfcommon)
def ica_f34_issuance_cadence_logz_252d_base_v036_signal(ncfcommon):
    result = _z(_issuance_cadence_log(ncfcommon), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(ncfcommon)
def ica_f34_issuance_cadence_logz_504d_base_v037_signal(ncfcommon):
    result = _z(_issuance_cadence_log(ncfcommon), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of ncfcommon^2 times closeadj
def ica_f34_issuance_cadence_sq_63d_base_v038_signal(ncfcommon, closeadj):
    result = _mean(ncfcommon * ncfcommon, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of ncfcommon^2 times closeadj
def ica_f34_issuance_cadence_sq_252d_base_v039_signal(ncfcommon, closeadj):
    result = _mean(ncfcommon * ncfcommon, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(ncfcommon) times closeadj
def ica_f34_issuance_cadence_sign_21d_base_v040_signal(ncfcommon, closeadj):
    result = _mean(np.sign(ncfcommon), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(ncfcommon) times closeadj
def ica_f34_issuance_cadence_sign_63d_base_v041_signal(ncfcommon, closeadj):
    result = _mean(np.sign(ncfcommon), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(ncfcommon) times closeadj
def ica_f34_issuance_cadence_sign_252d_base_v042_signal(ncfcommon, closeadj):
    result = _mean(np.sign(ncfcommon), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfcommon/opex mean
def ica_f34_issuance_cadence_per_opex_63d_base_v043_signal(ncfcommon, opex):
    result = _mean(_issuance_cadence_scaled(ncfcommon, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfcommon/opex mean
def ica_f34_issuance_cadence_per_opex_252d_base_v044_signal(ncfcommon, opex):
    result = _mean(_issuance_cadence_scaled(ncfcommon, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfcommon/ebitda mean
def ica_f34_issuance_cadence_per_ebitda_63d_base_v045_signal(ncfcommon, ebitda):
    result = _mean(_issuance_cadence_scaled(ncfcommon, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfcommon/ebitda mean
def ica_f34_issuance_cadence_per_ebitda_252d_base_v046_signal(ncfcommon, ebitda):
    result = _mean(_issuance_cadence_scaled(ncfcommon, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfcommon/capex mean
def ica_f34_issuance_cadence_per_capex_63d_base_v047_signal(ncfcommon, capex):
    result = _mean(_issuance_cadence_scaled(ncfcommon, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfcommon/capex mean
def ica_f34_issuance_cadence_per_capex_252d_base_v048_signal(ncfcommon, capex):
    result = _mean(_issuance_cadence_scaled(ncfcommon, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfcommon/liabilities mean
def ica_f34_issuance_cadence_per_liabilities_63d_base_v049_signal(ncfcommon, liabilities):
    result = _mean(_issuance_cadence_scaled(ncfcommon, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfcommon/liabilities mean
def ica_f34_issuance_cadence_per_liabilities_252d_base_v050_signal(ncfcommon, liabilities):
    result = _mean(_issuance_cadence_scaled(ncfcommon, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ncfcommon relative to 252d max times closeadj
def ica_f34_issuance_cadence_relmax_252d_base_v051_signal(ncfcommon, closeadj):
    peak = ncfcommon.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (ncfcommon / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfcommon relative to 504d max times closeadj
def ica_f34_issuance_cadence_relmax_504d_base_v052_signal(ncfcommon, closeadj):
    peak = ncfcommon.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (ncfcommon / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfcommon relative to 252d min times closeadj
def ica_f34_issuance_cadence_relmin_252d_base_v053_signal(ncfcommon, closeadj):
    trough = ncfcommon.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (ncfcommon / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfcommon relative to 504d min times closeadj
def ica_f34_issuance_cadence_relmin_504d_base_v054_signal(ncfcommon, closeadj):
    trough = ncfcommon.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (ncfcommon / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of ncfcommon times closeadj
def ica_f34_issuance_cadence_pct_21d_base_v055_signal(ncfcommon, closeadj):
    result = _pct_change(ncfcommon, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of ncfcommon times closeadj
def ica_f34_issuance_cadence_pct_63d_base_v056_signal(ncfcommon, closeadj):
    result = _pct_change(ncfcommon, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of ncfcommon times closeadj
def ica_f34_issuance_cadence_pct_252d_base_v057_signal(ncfcommon, closeadj):
    result = _pct_change(ncfcommon, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of ncfcommon times closeadj
def ica_f34_issuance_cadence_sum_63d_base_v058_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of ncfcommon times closeadj
def ica_f34_issuance_cadence_sum_252d_base_v059_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of ncfcommon times closeadj
def ica_f34_issuance_cadence_sum_504d_base_v060_signal(ncfcommon, closeadj):
    result = ncfcommon.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfcommon(63d) / smoothed assets(252d) x closeadj
def ica_f34_issuance_cadence_rom_assets_252_63d_base_v061_signal(ncfcommon, assets, closeadj):
    n = _mean(ncfcommon, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfcommon(126d) / smoothed assets(504d) x closeadj
def ica_f34_issuance_cadence_rom_assets_504_126d_base_v062_signal(ncfcommon, assets, closeadj):
    n = _mean(ncfcommon, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfcommon(63d) / smoothed marketcap(252d) x closeadj
def ica_f34_issuance_cadence_rom_marketcap_252_63d_base_v063_signal(ncfcommon, marketcap, closeadj):
    n = _mean(ncfcommon, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfcommon(126d) / smoothed marketcap(504d) x closeadj
def ica_f34_issuance_cadence_rom_marketcap_504_126d_base_v064_signal(ncfcommon, marketcap, closeadj):
    n = _mean(ncfcommon, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfcommon(63d) / smoothed equity(252d) x closeadj
def ica_f34_issuance_cadence_rom_equity_252_63d_base_v065_signal(ncfcommon, equity, closeadj):
    n = _mean(ncfcommon, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfcommon(126d) / smoothed equity(504d) x closeadj
def ica_f34_issuance_cadence_rom_equity_504_126d_base_v066_signal(ncfcommon, equity, closeadj):
    n = _mean(ncfcommon, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ncfcommon) / std(assets)
def ica_f34_issuance_cadence_volratio_assets_252d_base_v067_signal(ncfcommon, assets):
    n = _std(ncfcommon, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ncfcommon) / std(assets)
def ica_f34_issuance_cadence_volratio_assets_504d_base_v068_signal(ncfcommon, assets):
    n = _std(ncfcommon, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ncfcommon) / std(marketcap)
def ica_f34_issuance_cadence_volratio_marketcap_252d_base_v069_signal(ncfcommon, marketcap):
    n = _std(ncfcommon, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ncfcommon) / std(marketcap)
def ica_f34_issuance_cadence_volratio_marketcap_504d_base_v070_signal(ncfcommon, marketcap):
    n = _std(ncfcommon, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed ncfcommon times closeadj
def ica_f34_issuance_cadence_raw_5d_base_v071_signal(ncfcommon, closeadj):
    result = _mean(ncfcommon, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed ncfcommon times closeadj
def ica_f34_issuance_cadence_raw_1008d_base_v072_signal(ncfcommon, closeadj):
    result = _mean(ncfcommon, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ncfcommon/assets
def ica_f34_issuance_cadence_log_per_assets_252d_base_v073_signal(ncfcommon, assets):
    s = _issuance_cadence_scaled(ncfcommon, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ncfcommon/assets
def ica_f34_issuance_cadence_log_per_assets_504d_base_v074_signal(ncfcommon, assets):
    s = _issuance_cadence_scaled(ncfcommon, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ncfcommon/marketcap
def ica_f34_issuance_cadence_log_per_marketcap_252d_base_v075_signal(ncfcommon, marketcap):
    s = _issuance_cadence_scaled(ncfcommon, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
