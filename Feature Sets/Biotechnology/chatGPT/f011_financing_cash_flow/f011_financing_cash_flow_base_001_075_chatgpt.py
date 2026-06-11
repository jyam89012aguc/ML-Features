"""Family f011 - Capital raised through financing (Cash Flow and Burn) | Sharadar tables: SF1 | fields: ncff, ncfcommon, ncfdebt, ncfi | base 001-075"""
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
def _financing_cash_flow_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _financing_cash_flow_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _financing_cash_flow_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed ncff times closeadj
def fcf_f011_financing_cash_flow_raw_21d_base_v001_signal(ncff, closeadj):
    result = _mean(ncff, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed ncff times closeadj
def fcf_f011_financing_cash_flow_raw_63d_base_v002_signal(ncff, closeadj):
    result = _mean(ncff, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed ncff times closeadj
def fcf_f011_financing_cash_flow_raw_126d_base_v003_signal(ncff, closeadj):
    result = _mean(ncff, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed ncff times closeadj
def fcf_f011_financing_cash_flow_raw_252d_base_v004_signal(ncff, closeadj):
    result = _mean(ncff, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed ncff times closeadj
def fcf_f011_financing_cash_flow_raw_504d_base_v005_signal(ncff, closeadj):
    result = _mean(ncff, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(ncff) times closeadj
def fcf_f011_financing_cash_flow_log_21d_base_v006_signal(ncff, closeadj):
    result = _mean(_financing_cash_flow_log(ncff), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(ncff) times closeadj
def fcf_f011_financing_cash_flow_log_63d_base_v007_signal(ncff, closeadj):
    result = _mean(_financing_cash_flow_log(ncff), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(ncff) times closeadj
def fcf_f011_financing_cash_flow_log_126d_base_v008_signal(ncff, closeadj):
    result = _mean(_financing_cash_flow_log(ncff), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(ncff) times closeadj
def fcf_f011_financing_cash_flow_log_252d_base_v009_signal(ncff, closeadj):
    result = _mean(_financing_cash_flow_log(ncff), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(ncff) times closeadj
def fcf_f011_financing_cash_flow_log_504d_base_v010_signal(ncff, closeadj):
    result = _mean(_financing_cash_flow_log(ncff), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/ncfcommon mean
def fcf_f011_financing_cash_flow_per_ncfcommon_63d_base_v011_signal(ncff, ncfcommon):
    result = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/ncfcommon mean
def fcf_f011_financing_cash_flow_per_ncfcommon_252d_base_v012_signal(ncff, ncfcommon):
    result = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff/ncfcommon mean
def fcf_f011_financing_cash_flow_per_ncfcommon_504d_base_v013_signal(ncff, ncfcommon):
    result = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/ncfdebt mean
def fcf_f011_financing_cash_flow_per_ncfdebt_63d_base_v014_signal(ncff, ncfdebt):
    result = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/ncfdebt mean
def fcf_f011_financing_cash_flow_per_ncfdebt_252d_base_v015_signal(ncff, ncfdebt):
    result = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff/ncfdebt mean
def fcf_f011_financing_cash_flow_per_ncfdebt_504d_base_v016_signal(ncff, ncfdebt):
    result = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/ncfi mean
def fcf_f011_financing_cash_flow_per_ncfi_63d_base_v017_signal(ncff, ncfi):
    result = _mean(_financing_cash_flow_scaled(ncff, ncfi), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/ncfi mean
def fcf_f011_financing_cash_flow_per_ncfi_252d_base_v018_signal(ncff, ncfi):
    result = _mean(_financing_cash_flow_scaled(ncff, ncfi), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff/ncfi mean
def fcf_f011_financing_cash_flow_per_ncfi_504d_base_v019_signal(ncff, ncfi):
    result = _mean(_financing_cash_flow_scaled(ncff, ncfi), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/assets mean
def fcf_f011_financing_cash_flow_per_assets_63d_base_v020_signal(ncff, assets):
    result = _mean(_financing_cash_flow_scaled(ncff, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/assets mean
def fcf_f011_financing_cash_flow_per_assets_252d_base_v021_signal(ncff, assets):
    result = _mean(_financing_cash_flow_scaled(ncff, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff/assets mean
def fcf_f011_financing_cash_flow_per_assets_504d_base_v022_signal(ncff, assets):
    result = _mean(_financing_cash_flow_scaled(ncff, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/marketcap mean
def fcf_f011_financing_cash_flow_per_marketcap_63d_base_v023_signal(ncff, marketcap):
    result = _mean(_financing_cash_flow_scaled(ncff, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/marketcap mean
def fcf_f011_financing_cash_flow_per_marketcap_252d_base_v024_signal(ncff, marketcap):
    result = _mean(_financing_cash_flow_scaled(ncff, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff/marketcap mean
def fcf_f011_financing_cash_flow_per_marketcap_504d_base_v025_signal(ncff, marketcap):
    result = _mean(_financing_cash_flow_scaled(ncff, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncff per share times closeadj
def fcf_f011_financing_cash_flow_pershare_21d_base_v026_signal(ncff, sharesbas, closeadj):
    ps = _financing_cash_flow_per_share(ncff, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff per share times closeadj
def fcf_f011_financing_cash_flow_pershare_63d_base_v027_signal(ncff, sharesbas, closeadj):
    ps = _financing_cash_flow_per_share(ncff, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ncff per share times closeadj
def fcf_f011_financing_cash_flow_pershare_126d_base_v028_signal(ncff, sharesbas, closeadj):
    ps = _financing_cash_flow_per_share(ncff, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff per share times closeadj
def fcf_f011_financing_cash_flow_pershare_252d_base_v029_signal(ncff, sharesbas, closeadj):
    ps = _financing_cash_flow_per_share(ncff, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff per share times closeadj
def fcf_f011_financing_cash_flow_pershare_504d_base_v030_signal(ncff, sharesbas, closeadj):
    ps = _financing_cash_flow_per_share(ncff, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of ncff times closeadj
def fcf_f011_financing_cash_flow_std_63d_base_v031_signal(ncff, closeadj):
    result = _std(ncff, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of ncff times closeadj
def fcf_f011_financing_cash_flow_std_252d_base_v032_signal(ncff, closeadj):
    result = _std(ncff, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of ncff times closeadj
def fcf_f011_financing_cash_flow_std_504d_base_v033_signal(ncff, closeadj):
    result = _std(ncff, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of ncff
def fcf_f011_financing_cash_flow_z_252d_base_v034_signal(ncff):
    result = _z(ncff, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of ncff
def fcf_f011_financing_cash_flow_z_504d_base_v035_signal(ncff):
    result = _z(ncff, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(ncff)
def fcf_f011_financing_cash_flow_logz_252d_base_v036_signal(ncff):
    result = _z(_financing_cash_flow_log(ncff), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(ncff)
def fcf_f011_financing_cash_flow_logz_504d_base_v037_signal(ncff):
    result = _z(_financing_cash_flow_log(ncff), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of ncff^2 times closeadj
def fcf_f011_financing_cash_flow_sq_63d_base_v038_signal(ncff, closeadj):
    result = _mean(ncff * ncff, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of ncff^2 times closeadj
def fcf_f011_financing_cash_flow_sq_252d_base_v039_signal(ncff, closeadj):
    result = _mean(ncff * ncff, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(ncff) times closeadj
def fcf_f011_financing_cash_flow_sign_21d_base_v040_signal(ncff, closeadj):
    result = _mean(np.sign(ncff), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(ncff) times closeadj
def fcf_f011_financing_cash_flow_sign_63d_base_v041_signal(ncff, closeadj):
    result = _mean(np.sign(ncff), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(ncff) times closeadj
def fcf_f011_financing_cash_flow_sign_252d_base_v042_signal(ncff, closeadj):
    result = _mean(np.sign(ncff), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/opex mean
def fcf_f011_financing_cash_flow_per_opex_63d_base_v043_signal(ncff, opex):
    result = _mean(_financing_cash_flow_scaled(ncff, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/opex mean
def fcf_f011_financing_cash_flow_per_opex_252d_base_v044_signal(ncff, opex):
    result = _mean(_financing_cash_flow_scaled(ncff, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/ebitda mean
def fcf_f011_financing_cash_flow_per_ebitda_63d_base_v045_signal(ncff, ebitda):
    result = _mean(_financing_cash_flow_scaled(ncff, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/ebitda mean
def fcf_f011_financing_cash_flow_per_ebitda_252d_base_v046_signal(ncff, ebitda):
    result = _mean(_financing_cash_flow_scaled(ncff, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/capex mean
def fcf_f011_financing_cash_flow_per_capex_63d_base_v047_signal(ncff, capex):
    result = _mean(_financing_cash_flow_scaled(ncff, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/capex mean
def fcf_f011_financing_cash_flow_per_capex_252d_base_v048_signal(ncff, capex):
    result = _mean(_financing_cash_flow_scaled(ncff, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/liabilities mean
def fcf_f011_financing_cash_flow_per_liabilities_63d_base_v049_signal(ncff, liabilities):
    result = _mean(_financing_cash_flow_scaled(ncff, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/liabilities mean
def fcf_f011_financing_cash_flow_per_liabilities_252d_base_v050_signal(ncff, liabilities):
    result = _mean(_financing_cash_flow_scaled(ncff, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ncff relative to 252d max times closeadj
def fcf_f011_financing_cash_flow_relmax_252d_base_v051_signal(ncff, closeadj):
    peak = ncff.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (ncff / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncff relative to 504d max times closeadj
def fcf_f011_financing_cash_flow_relmax_504d_base_v052_signal(ncff, closeadj):
    peak = ncff.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (ncff / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncff relative to 252d min times closeadj
def fcf_f011_financing_cash_flow_relmin_252d_base_v053_signal(ncff, closeadj):
    trough = ncff.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (ncff / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncff relative to 504d min times closeadj
def fcf_f011_financing_cash_flow_relmin_504d_base_v054_signal(ncff, closeadj):
    trough = ncff.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (ncff / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of ncff times closeadj
def fcf_f011_financing_cash_flow_pct_21d_base_v055_signal(ncff, closeadj):
    result = _pct_change(ncff, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of ncff times closeadj
def fcf_f011_financing_cash_flow_pct_63d_base_v056_signal(ncff, closeadj):
    result = _pct_change(ncff, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of ncff times closeadj
def fcf_f011_financing_cash_flow_pct_252d_base_v057_signal(ncff, closeadj):
    result = _pct_change(ncff, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of ncff times closeadj
def fcf_f011_financing_cash_flow_sum_63d_base_v058_signal(ncff, closeadj):
    result = ncff.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of ncff times closeadj
def fcf_f011_financing_cash_flow_sum_252d_base_v059_signal(ncff, closeadj):
    result = ncff.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of ncff times closeadj
def fcf_f011_financing_cash_flow_sum_504d_base_v060_signal(ncff, closeadj):
    result = ncff.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncff(63d) / smoothed ncfcommon(252d) x closeadj
def fcf_f011_financing_cash_flow_rom_ncfcommon_252_63d_base_v061_signal(ncff, ncfcommon, closeadj):
    n = _mean(ncff, 63)
    d = _mean(ncfcommon, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncff(126d) / smoothed ncfcommon(504d) x closeadj
def fcf_f011_financing_cash_flow_rom_ncfcommon_504_126d_base_v062_signal(ncff, ncfcommon, closeadj):
    n = _mean(ncff, 126)
    d = _mean(ncfcommon, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncff(63d) / smoothed ncfdebt(252d) x closeadj
def fcf_f011_financing_cash_flow_rom_ncfdebt_252_63d_base_v063_signal(ncff, ncfdebt, closeadj):
    n = _mean(ncff, 63)
    d = _mean(ncfdebt, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncff(126d) / smoothed ncfdebt(504d) x closeadj
def fcf_f011_financing_cash_flow_rom_ncfdebt_504_126d_base_v064_signal(ncff, ncfdebt, closeadj):
    n = _mean(ncff, 126)
    d = _mean(ncfdebt, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncff(63d) / smoothed ncfi(252d) x closeadj
def fcf_f011_financing_cash_flow_rom_ncfi_252_63d_base_v065_signal(ncff, ncfi, closeadj):
    n = _mean(ncff, 63)
    d = _mean(ncfi, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncff(126d) / smoothed ncfi(504d) x closeadj
def fcf_f011_financing_cash_flow_rom_ncfi_504_126d_base_v066_signal(ncff, ncfi, closeadj):
    n = _mean(ncff, 126)
    d = _mean(ncfi, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ncff) / std(ncfcommon)
def fcf_f011_financing_cash_flow_volratio_ncfcommon_252d_base_v067_signal(ncff, ncfcommon):
    n = _std(ncff, 252)
    d = _std(ncfcommon, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ncff) / std(ncfcommon)
def fcf_f011_financing_cash_flow_volratio_ncfcommon_504d_base_v068_signal(ncff, ncfcommon):
    n = _std(ncff, 504)
    d = _std(ncfcommon, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ncff) / std(ncfdebt)
def fcf_f011_financing_cash_flow_volratio_ncfdebt_252d_base_v069_signal(ncff, ncfdebt):
    n = _std(ncff, 252)
    d = _std(ncfdebt, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ncff) / std(ncfdebt)
def fcf_f011_financing_cash_flow_volratio_ncfdebt_504d_base_v070_signal(ncff, ncfdebt):
    n = _std(ncff, 504)
    d = _std(ncfdebt, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed ncff times closeadj
def fcf_f011_financing_cash_flow_raw_5d_base_v071_signal(ncff, closeadj):
    result = _mean(ncff, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed ncff times closeadj
def fcf_f011_financing_cash_flow_raw_1008d_base_v072_signal(ncff, closeadj):
    result = _mean(ncff, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ncff/ncfcommon
def fcf_f011_financing_cash_flow_log_per_ncfcommon_252d_base_v073_signal(ncff, ncfcommon):
    s = _financing_cash_flow_scaled(ncff, ncfcommon)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ncff/ncfcommon
def fcf_f011_financing_cash_flow_log_per_ncfcommon_504d_base_v074_signal(ncff, ncfcommon):
    s = _financing_cash_flow_scaled(ncff, ncfcommon)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ncff/ncfdebt
def fcf_f011_financing_cash_flow_log_per_ncfdebt_252d_base_v075_signal(ncff, ncfdebt):
    s = _financing_cash_flow_scaled(ncff, ncfdebt)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
