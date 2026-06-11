"""Family f87 - Transaction intensity  (O_Insider_SF2) | base 001-075"""
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
def _insider_intensity_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _insider_intensity_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _insider_intensity_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed transactionvalue times closeadj
def ini_f87_insider_intensity_raw_21d_base_v001_signal(transactionvalue, closeadj):
    result = _mean(transactionvalue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed transactionvalue times closeadj
def ini_f87_insider_intensity_raw_63d_base_v002_signal(transactionvalue, closeadj):
    result = _mean(transactionvalue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed transactionvalue times closeadj
def ini_f87_insider_intensity_raw_126d_base_v003_signal(transactionvalue, closeadj):
    result = _mean(transactionvalue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed transactionvalue times closeadj
def ini_f87_insider_intensity_raw_252d_base_v004_signal(transactionvalue, closeadj):
    result = _mean(transactionvalue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed transactionvalue times closeadj
def ini_f87_insider_intensity_raw_504d_base_v005_signal(transactionvalue, closeadj):
    result = _mean(transactionvalue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(transactionvalue) times closeadj
def ini_f87_insider_intensity_log_21d_base_v006_signal(transactionvalue, closeadj):
    result = _mean(_insider_intensity_log(transactionvalue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(transactionvalue) times closeadj
def ini_f87_insider_intensity_log_63d_base_v007_signal(transactionvalue, closeadj):
    result = _mean(_insider_intensity_log(transactionvalue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(transactionvalue) times closeadj
def ini_f87_insider_intensity_log_126d_base_v008_signal(transactionvalue, closeadj):
    result = _mean(_insider_intensity_log(transactionvalue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(transactionvalue) times closeadj
def ini_f87_insider_intensity_log_252d_base_v009_signal(transactionvalue, closeadj):
    result = _mean(_insider_intensity_log(transactionvalue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(transactionvalue) times closeadj
def ini_f87_insider_intensity_log_504d_base_v010_signal(transactionvalue, closeadj):
    result = _mean(_insider_intensity_log(transactionvalue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactionvalue/assets mean
def ini_f87_insider_intensity_per_assets_63d_base_v011_signal(transactionvalue, assets):
    result = _mean(_insider_intensity_scaled(transactionvalue, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactionvalue/assets mean
def ini_f87_insider_intensity_per_assets_252d_base_v012_signal(transactionvalue, assets):
    result = _mean(_insider_intensity_scaled(transactionvalue, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d transactionvalue/assets mean
def ini_f87_insider_intensity_per_assets_504d_base_v013_signal(transactionvalue, assets):
    result = _mean(_insider_intensity_scaled(transactionvalue, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactionvalue/marketcap mean
def ini_f87_insider_intensity_per_marketcap_63d_base_v014_signal(transactionvalue, marketcap):
    result = _mean(_insider_intensity_scaled(transactionvalue, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactionvalue/marketcap mean
def ini_f87_insider_intensity_per_marketcap_252d_base_v015_signal(transactionvalue, marketcap):
    result = _mean(_insider_intensity_scaled(transactionvalue, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d transactionvalue/marketcap mean
def ini_f87_insider_intensity_per_marketcap_504d_base_v016_signal(transactionvalue, marketcap):
    result = _mean(_insider_intensity_scaled(transactionvalue, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactionvalue/equity mean
def ini_f87_insider_intensity_per_equity_63d_base_v017_signal(transactionvalue, equity):
    result = _mean(_insider_intensity_scaled(transactionvalue, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactionvalue/equity mean
def ini_f87_insider_intensity_per_equity_252d_base_v018_signal(transactionvalue, equity):
    result = _mean(_insider_intensity_scaled(transactionvalue, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d transactionvalue/equity mean
def ini_f87_insider_intensity_per_equity_504d_base_v019_signal(transactionvalue, equity):
    result = _mean(_insider_intensity_scaled(transactionvalue, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactionvalue/debt mean
def ini_f87_insider_intensity_per_debt_63d_base_v020_signal(transactionvalue, debt):
    result = _mean(_insider_intensity_scaled(transactionvalue, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactionvalue/debt mean
def ini_f87_insider_intensity_per_debt_252d_base_v021_signal(transactionvalue, debt):
    result = _mean(_insider_intensity_scaled(transactionvalue, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d transactionvalue/debt mean
def ini_f87_insider_intensity_per_debt_504d_base_v022_signal(transactionvalue, debt):
    result = _mean(_insider_intensity_scaled(transactionvalue, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactionvalue/revenue mean
def ini_f87_insider_intensity_per_revenue_63d_base_v023_signal(transactionvalue, revenue):
    result = _mean(_insider_intensity_scaled(transactionvalue, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactionvalue/revenue mean
def ini_f87_insider_intensity_per_revenue_252d_base_v024_signal(transactionvalue, revenue):
    result = _mean(_insider_intensity_scaled(transactionvalue, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d transactionvalue/revenue mean
def ini_f87_insider_intensity_per_revenue_504d_base_v025_signal(transactionvalue, revenue):
    result = _mean(_insider_intensity_scaled(transactionvalue, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d transactionvalue per share times closeadj
def ini_f87_insider_intensity_pershare_21d_base_v026_signal(transactionvalue, sharesbas, closeadj):
    ps = _insider_intensity_per_share(transactionvalue, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactionvalue per share times closeadj
def ini_f87_insider_intensity_pershare_63d_base_v027_signal(transactionvalue, sharesbas, closeadj):
    ps = _insider_intensity_per_share(transactionvalue, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d transactionvalue per share times closeadj
def ini_f87_insider_intensity_pershare_126d_base_v028_signal(transactionvalue, sharesbas, closeadj):
    ps = _insider_intensity_per_share(transactionvalue, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactionvalue per share times closeadj
def ini_f87_insider_intensity_pershare_252d_base_v029_signal(transactionvalue, sharesbas, closeadj):
    ps = _insider_intensity_per_share(transactionvalue, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d transactionvalue per share times closeadj
def ini_f87_insider_intensity_pershare_504d_base_v030_signal(transactionvalue, sharesbas, closeadj):
    ps = _insider_intensity_per_share(transactionvalue, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of transactionvalue times closeadj
def ini_f87_insider_intensity_std_63d_base_v031_signal(transactionvalue, closeadj):
    result = _std(transactionvalue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of transactionvalue times closeadj
def ini_f87_insider_intensity_std_252d_base_v032_signal(transactionvalue, closeadj):
    result = _std(transactionvalue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of transactionvalue times closeadj
def ini_f87_insider_intensity_std_504d_base_v033_signal(transactionvalue, closeadj):
    result = _std(transactionvalue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of transactionvalue
def ini_f87_insider_intensity_z_252d_base_v034_signal(transactionvalue):
    result = _z(transactionvalue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of transactionvalue
def ini_f87_insider_intensity_z_504d_base_v035_signal(transactionvalue):
    result = _z(transactionvalue, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(transactionvalue)
def ini_f87_insider_intensity_logz_252d_base_v036_signal(transactionvalue):
    result = _z(_insider_intensity_log(transactionvalue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(transactionvalue)
def ini_f87_insider_intensity_logz_504d_base_v037_signal(transactionvalue):
    result = _z(_insider_intensity_log(transactionvalue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of transactionvalue^2 times closeadj
def ini_f87_insider_intensity_sq_63d_base_v038_signal(transactionvalue, closeadj):
    result = _mean(transactionvalue * transactionvalue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of transactionvalue^2 times closeadj
def ini_f87_insider_intensity_sq_252d_base_v039_signal(transactionvalue, closeadj):
    result = _mean(transactionvalue * transactionvalue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(transactionvalue) times closeadj
def ini_f87_insider_intensity_sign_21d_base_v040_signal(transactionvalue, closeadj):
    result = _mean(np.sign(transactionvalue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(transactionvalue) times closeadj
def ini_f87_insider_intensity_sign_63d_base_v041_signal(transactionvalue, closeadj):
    result = _mean(np.sign(transactionvalue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(transactionvalue) times closeadj
def ini_f87_insider_intensity_sign_252d_base_v042_signal(transactionvalue, closeadj):
    result = _mean(np.sign(transactionvalue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactionvalue/opex mean
def ini_f87_insider_intensity_per_opex_63d_base_v043_signal(transactionvalue, opex):
    result = _mean(_insider_intensity_scaled(transactionvalue, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactionvalue/opex mean
def ini_f87_insider_intensity_per_opex_252d_base_v044_signal(transactionvalue, opex):
    result = _mean(_insider_intensity_scaled(transactionvalue, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactionvalue/ebitda mean
def ini_f87_insider_intensity_per_ebitda_63d_base_v045_signal(transactionvalue, ebitda):
    result = _mean(_insider_intensity_scaled(transactionvalue, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactionvalue/ebitda mean
def ini_f87_insider_intensity_per_ebitda_252d_base_v046_signal(transactionvalue, ebitda):
    result = _mean(_insider_intensity_scaled(transactionvalue, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactionvalue/capex mean
def ini_f87_insider_intensity_per_capex_63d_base_v047_signal(transactionvalue, capex):
    result = _mean(_insider_intensity_scaled(transactionvalue, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactionvalue/capex mean
def ini_f87_insider_intensity_per_capex_252d_base_v048_signal(transactionvalue, capex):
    result = _mean(_insider_intensity_scaled(transactionvalue, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactionvalue/liabilities mean
def ini_f87_insider_intensity_per_liabilities_63d_base_v049_signal(transactionvalue, liabilities):
    result = _mean(_insider_intensity_scaled(transactionvalue, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactionvalue/liabilities mean
def ini_f87_insider_intensity_per_liabilities_252d_base_v050_signal(transactionvalue, liabilities):
    result = _mean(_insider_intensity_scaled(transactionvalue, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# transactionvalue relative to 252d max times closeadj
def ini_f87_insider_intensity_relmax_252d_base_v051_signal(transactionvalue, closeadj):
    peak = transactionvalue.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (transactionvalue / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# transactionvalue relative to 504d max times closeadj
def ini_f87_insider_intensity_relmax_504d_base_v052_signal(transactionvalue, closeadj):
    peak = transactionvalue.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (transactionvalue / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# transactionvalue relative to 252d min times closeadj
def ini_f87_insider_intensity_relmin_252d_base_v053_signal(transactionvalue, closeadj):
    trough = transactionvalue.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (transactionvalue / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# transactionvalue relative to 504d min times closeadj
def ini_f87_insider_intensity_relmin_504d_base_v054_signal(transactionvalue, closeadj):
    trough = transactionvalue.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (transactionvalue / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of transactionvalue times closeadj
def ini_f87_insider_intensity_pct_21d_base_v055_signal(transactionvalue, closeadj):
    result = _pct_change(transactionvalue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of transactionvalue times closeadj
def ini_f87_insider_intensity_pct_63d_base_v056_signal(transactionvalue, closeadj):
    result = _pct_change(transactionvalue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of transactionvalue times closeadj
def ini_f87_insider_intensity_pct_252d_base_v057_signal(transactionvalue, closeadj):
    result = _pct_change(transactionvalue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of transactionvalue times closeadj
def ini_f87_insider_intensity_sum_63d_base_v058_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of transactionvalue times closeadj
def ini_f87_insider_intensity_sum_252d_base_v059_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of transactionvalue times closeadj
def ini_f87_insider_intensity_sum_504d_base_v060_signal(transactionvalue, closeadj):
    result = transactionvalue.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed transactionvalue(63d) / smoothed assets(252d) x closeadj
def ini_f87_insider_intensity_rom_assets_252_63d_base_v061_signal(transactionvalue, assets, closeadj):
    n = _mean(transactionvalue, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed transactionvalue(126d) / smoothed assets(504d) x closeadj
def ini_f87_insider_intensity_rom_assets_504_126d_base_v062_signal(transactionvalue, assets, closeadj):
    n = _mean(transactionvalue, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed transactionvalue(63d) / smoothed marketcap(252d) x closeadj
def ini_f87_insider_intensity_rom_marketcap_252_63d_base_v063_signal(transactionvalue, marketcap, closeadj):
    n = _mean(transactionvalue, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed transactionvalue(126d) / smoothed marketcap(504d) x closeadj
def ini_f87_insider_intensity_rom_marketcap_504_126d_base_v064_signal(transactionvalue, marketcap, closeadj):
    n = _mean(transactionvalue, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed transactionvalue(63d) / smoothed equity(252d) x closeadj
def ini_f87_insider_intensity_rom_equity_252_63d_base_v065_signal(transactionvalue, equity, closeadj):
    n = _mean(transactionvalue, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed transactionvalue(126d) / smoothed equity(504d) x closeadj
def ini_f87_insider_intensity_rom_equity_504_126d_base_v066_signal(transactionvalue, equity, closeadj):
    n = _mean(transactionvalue, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(transactionvalue) / std(assets)
def ini_f87_insider_intensity_volratio_assets_252d_base_v067_signal(transactionvalue, assets):
    n = _std(transactionvalue, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(transactionvalue) / std(assets)
def ini_f87_insider_intensity_volratio_assets_504d_base_v068_signal(transactionvalue, assets):
    n = _std(transactionvalue, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(transactionvalue) / std(marketcap)
def ini_f87_insider_intensity_volratio_marketcap_252d_base_v069_signal(transactionvalue, marketcap):
    n = _std(transactionvalue, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(transactionvalue) / std(marketcap)
def ini_f87_insider_intensity_volratio_marketcap_504d_base_v070_signal(transactionvalue, marketcap):
    n = _std(transactionvalue, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed transactionvalue times closeadj
def ini_f87_insider_intensity_raw_5d_base_v071_signal(transactionvalue, closeadj):
    result = _mean(transactionvalue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed transactionvalue times closeadj
def ini_f87_insider_intensity_raw_1008d_base_v072_signal(transactionvalue, closeadj):
    result = _mean(transactionvalue, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of transactionvalue/assets
def ini_f87_insider_intensity_log_per_assets_252d_base_v073_signal(transactionvalue, assets):
    s = _insider_intensity_scaled(transactionvalue, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of transactionvalue/assets
def ini_f87_insider_intensity_log_per_assets_504d_base_v074_signal(transactionvalue, assets):
    s = _insider_intensity_scaled(transactionvalue, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of transactionvalue/marketcap
def ini_f87_insider_intensity_log_per_marketcap_252d_base_v075_signal(transactionvalue, marketcap):
    s = _insider_intensity_scaled(transactionvalue, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
