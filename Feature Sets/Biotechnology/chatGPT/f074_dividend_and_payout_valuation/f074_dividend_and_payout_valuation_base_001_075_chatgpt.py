"""Family f074 - Dividend and payout valuation (Valuation Multiples) | Sharadar tables: SF1 | fields: dps, ncfdiv, payoutratio, value | base 001-075"""
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
def _dividend_and_payout_valuation_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _dividend_and_payout_valuation_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _dividend_and_payout_valuation_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed dps times closeadj
def dpv_f074_dividend_and_payout_valuation_raw_21d_base_v001_signal(dps, closeadj):
    result = _mean(dps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed dps times closeadj
def dpv_f074_dividend_and_payout_valuation_raw_63d_base_v002_signal(dps, closeadj):
    result = _mean(dps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed dps times closeadj
def dpv_f074_dividend_and_payout_valuation_raw_126d_base_v003_signal(dps, closeadj):
    result = _mean(dps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed dps times closeadj
def dpv_f074_dividend_and_payout_valuation_raw_252d_base_v004_signal(dps, closeadj):
    result = _mean(dps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed dps times closeadj
def dpv_f074_dividend_and_payout_valuation_raw_504d_base_v005_signal(dps, closeadj):
    result = _mean(dps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(dps) times closeadj
def dpv_f074_dividend_and_payout_valuation_log_21d_base_v006_signal(dps, closeadj):
    result = _mean(_dividend_and_payout_valuation_log(dps), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(dps) times closeadj
def dpv_f074_dividend_and_payout_valuation_log_63d_base_v007_signal(dps, closeadj):
    result = _mean(_dividend_and_payout_valuation_log(dps), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(dps) times closeadj
def dpv_f074_dividend_and_payout_valuation_log_126d_base_v008_signal(dps, closeadj):
    result = _mean(_dividend_and_payout_valuation_log(dps), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(dps) times closeadj
def dpv_f074_dividend_and_payout_valuation_log_252d_base_v009_signal(dps, closeadj):
    result = _mean(_dividend_and_payout_valuation_log(dps), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(dps) times closeadj
def dpv_f074_dividend_and_payout_valuation_log_504d_base_v010_signal(dps, closeadj):
    result = _mean(_dividend_and_payout_valuation_log(dps), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dps/ncfdiv mean
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_63d_base_v011_signal(dps, ncfdiv):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dps/ncfdiv mean
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_252d_base_v012_signal(dps, ncfdiv):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dps/ncfdiv mean
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_504d_base_v013_signal(dps, ncfdiv):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dps/payoutratio mean
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_63d_base_v014_signal(dps, payoutratio):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dps/payoutratio mean
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_252d_base_v015_signal(dps, payoutratio):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dps/payoutratio mean
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_504d_base_v016_signal(dps, payoutratio):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dps/value mean
def dpv_f074_dividend_and_payout_valuation_per_value_63d_base_v017_signal(dps, value):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, value), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dps/value mean
def dpv_f074_dividend_and_payout_valuation_per_value_252d_base_v018_signal(dps, value):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, value), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dps/value mean
def dpv_f074_dividend_and_payout_valuation_per_value_504d_base_v019_signal(dps, value):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, value), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dps/equity mean
def dpv_f074_dividend_and_payout_valuation_per_equity_63d_base_v020_signal(dps, equity):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dps/equity mean
def dpv_f074_dividend_and_payout_valuation_per_equity_252d_base_v021_signal(dps, equity):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dps/equity mean
def dpv_f074_dividend_and_payout_valuation_per_equity_504d_base_v022_signal(dps, equity):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dps/debt mean
def dpv_f074_dividend_and_payout_valuation_per_debt_63d_base_v023_signal(dps, debt):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dps/debt mean
def dpv_f074_dividend_and_payout_valuation_per_debt_252d_base_v024_signal(dps, debt):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dps/debt mean
def dpv_f074_dividend_and_payout_valuation_per_debt_504d_base_v025_signal(dps, debt):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dps per share times closeadj
def dpv_f074_dividend_and_payout_valuation_pershare_21d_base_v026_signal(dps, sharesbas, closeadj):
    ps = _dividend_and_payout_valuation_per_share(dps, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dps per share times closeadj
def dpv_f074_dividend_and_payout_valuation_pershare_63d_base_v027_signal(dps, sharesbas, closeadj):
    ps = _dividend_and_payout_valuation_per_share(dps, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d dps per share times closeadj
def dpv_f074_dividend_and_payout_valuation_pershare_126d_base_v028_signal(dps, sharesbas, closeadj):
    ps = _dividend_and_payout_valuation_per_share(dps, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dps per share times closeadj
def dpv_f074_dividend_and_payout_valuation_pershare_252d_base_v029_signal(dps, sharesbas, closeadj):
    ps = _dividend_and_payout_valuation_per_share(dps, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dps per share times closeadj
def dpv_f074_dividend_and_payout_valuation_pershare_504d_base_v030_signal(dps, sharesbas, closeadj):
    ps = _dividend_and_payout_valuation_per_share(dps, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_std_63d_base_v031_signal(dps, closeadj):
    result = _std(dps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_std_252d_base_v032_signal(dps, closeadj):
    result = _std(dps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_std_504d_base_v033_signal(dps, closeadj):
    result = _std(dps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of dps
def dpv_f074_dividend_and_payout_valuation_z_252d_base_v034_signal(dps):
    result = _z(dps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of dps
def dpv_f074_dividend_and_payout_valuation_z_504d_base_v035_signal(dps):
    result = _z(dps, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(dps)
def dpv_f074_dividend_and_payout_valuation_logz_252d_base_v036_signal(dps):
    result = _z(_dividend_and_payout_valuation_log(dps), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(dps)
def dpv_f074_dividend_and_payout_valuation_logz_504d_base_v037_signal(dps):
    result = _z(_dividend_and_payout_valuation_log(dps), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of dps^2 times closeadj
def dpv_f074_dividend_and_payout_valuation_sq_63d_base_v038_signal(dps, closeadj):
    result = _mean(dps * dps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of dps^2 times closeadj
def dpv_f074_dividend_and_payout_valuation_sq_252d_base_v039_signal(dps, closeadj):
    result = _mean(dps * dps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(dps) times closeadj
def dpv_f074_dividend_and_payout_valuation_sign_21d_base_v040_signal(dps, closeadj):
    result = _mean(np.sign(dps), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(dps) times closeadj
def dpv_f074_dividend_and_payout_valuation_sign_63d_base_v041_signal(dps, closeadj):
    result = _mean(np.sign(dps), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(dps) times closeadj
def dpv_f074_dividend_and_payout_valuation_sign_252d_base_v042_signal(dps, closeadj):
    result = _mean(np.sign(dps), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dps/opex mean
def dpv_f074_dividend_and_payout_valuation_per_opex_63d_base_v043_signal(dps, opex):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dps/opex mean
def dpv_f074_dividend_and_payout_valuation_per_opex_252d_base_v044_signal(dps, opex):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dps/ebitda mean
def dpv_f074_dividend_and_payout_valuation_per_ebitda_63d_base_v045_signal(dps, ebitda):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dps/ebitda mean
def dpv_f074_dividend_and_payout_valuation_per_ebitda_252d_base_v046_signal(dps, ebitda):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dps/capex mean
def dpv_f074_dividend_and_payout_valuation_per_capex_63d_base_v047_signal(dps, capex):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dps/capex mean
def dpv_f074_dividend_and_payout_valuation_per_capex_252d_base_v048_signal(dps, capex):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dps/liabilities mean
def dpv_f074_dividend_and_payout_valuation_per_liabilities_63d_base_v049_signal(dps, liabilities):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dps/liabilities mean
def dpv_f074_dividend_and_payout_valuation_per_liabilities_252d_base_v050_signal(dps, liabilities):
    result = _mean(_dividend_and_payout_valuation_scaled(dps, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# dps relative to 252d max times closeadj
def dpv_f074_dividend_and_payout_valuation_relmax_252d_base_v051_signal(dps, closeadj):
    peak = dps.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (dps / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dps relative to 504d max times closeadj
def dpv_f074_dividend_and_payout_valuation_relmax_504d_base_v052_signal(dps, closeadj):
    peak = dps.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (dps / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dps relative to 252d min times closeadj
def dpv_f074_dividend_and_payout_valuation_relmin_252d_base_v053_signal(dps, closeadj):
    trough = dps.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (dps / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dps relative to 504d min times closeadj
def dpv_f074_dividend_and_payout_valuation_relmin_504d_base_v054_signal(dps, closeadj):
    trough = dps.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (dps / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_pct_21d_base_v055_signal(dps, closeadj):
    result = _pct_change(dps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_pct_63d_base_v056_signal(dps, closeadj):
    result = _pct_change(dps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_pct_252d_base_v057_signal(dps, closeadj):
    result = _pct_change(dps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_sum_63d_base_v058_signal(dps, closeadj):
    result = dps.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_sum_252d_base_v059_signal(dps, closeadj):
    result = dps.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of dps times closeadj
def dpv_f074_dividend_and_payout_valuation_sum_504d_base_v060_signal(dps, closeadj):
    result = dps.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dps(63d) / smoothed ncfdiv(252d) x closeadj
def dpv_f074_dividend_and_payout_valuation_rom_ncfdiv_252_63d_base_v061_signal(dps, ncfdiv, closeadj):
    n = _mean(dps, 63)
    d = _mean(ncfdiv, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dps(126d) / smoothed ncfdiv(504d) x closeadj
def dpv_f074_dividend_and_payout_valuation_rom_ncfdiv_504_126d_base_v062_signal(dps, ncfdiv, closeadj):
    n = _mean(dps, 126)
    d = _mean(ncfdiv, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dps(63d) / smoothed payoutratio(252d) x closeadj
def dpv_f074_dividend_and_payout_valuation_rom_payoutratio_252_63d_base_v063_signal(dps, payoutratio, closeadj):
    n = _mean(dps, 63)
    d = _mean(payoutratio, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dps(126d) / smoothed payoutratio(504d) x closeadj
def dpv_f074_dividend_and_payout_valuation_rom_payoutratio_504_126d_base_v064_signal(dps, payoutratio, closeadj):
    n = _mean(dps, 126)
    d = _mean(payoutratio, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dps(63d) / smoothed value(252d) x closeadj
def dpv_f074_dividend_and_payout_valuation_rom_value_252_63d_base_v065_signal(dps, value, closeadj):
    n = _mean(dps, 63)
    d = _mean(value, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dps(126d) / smoothed value(504d) x closeadj
def dpv_f074_dividend_and_payout_valuation_rom_value_504_126d_base_v066_signal(dps, value, closeadj):
    n = _mean(dps, 126)
    d = _mean(value, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(dps) / std(ncfdiv)
def dpv_f074_dividend_and_payout_valuation_volratio_ncfdiv_252d_base_v067_signal(dps, ncfdiv):
    n = _std(dps, 252)
    d = _std(ncfdiv, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(dps) / std(ncfdiv)
def dpv_f074_dividend_and_payout_valuation_volratio_ncfdiv_504d_base_v068_signal(dps, ncfdiv):
    n = _std(dps, 504)
    d = _std(ncfdiv, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(dps) / std(payoutratio)
def dpv_f074_dividend_and_payout_valuation_volratio_payoutratio_252d_base_v069_signal(dps, payoutratio):
    n = _std(dps, 252)
    d = _std(payoutratio, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(dps) / std(payoutratio)
def dpv_f074_dividend_and_payout_valuation_volratio_payoutratio_504d_base_v070_signal(dps, payoutratio):
    n = _std(dps, 504)
    d = _std(payoutratio, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed dps times closeadj
def dpv_f074_dividend_and_payout_valuation_raw_5d_base_v071_signal(dps, closeadj):
    result = _mean(dps, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed dps times closeadj
def dpv_f074_dividend_and_payout_valuation_raw_1008d_base_v072_signal(dps, closeadj):
    result = _mean(dps, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of dps/ncfdiv
def dpv_f074_dividend_and_payout_valuation_log_per_ncfdiv_252d_base_v073_signal(dps, ncfdiv):
    s = _dividend_and_payout_valuation_scaled(dps, ncfdiv)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of dps/ncfdiv
def dpv_f074_dividend_and_payout_valuation_log_per_ncfdiv_504d_base_v074_signal(dps, ncfdiv):
    s = _dividend_and_payout_valuation_scaled(dps, ncfdiv)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of dps/payoutratio
def dpv_f074_dividend_and_payout_valuation_log_per_payoutratio_252d_base_v075_signal(dps, payoutratio):
    s = _dividend_and_payout_valuation_scaled(dps, payoutratio)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
