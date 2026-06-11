"""Family f008 - Operating cash burn (Cash Flow and Burn) | Sharadar tables: SF1 | fields: ncfo, cashneq, assets | base 001-075"""
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
def _cash_burn_rate_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _cash_burn_rate_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _cash_burn_rate_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed ncfo times closeadj
def cbr_f008_cash_burn_rate_raw_21d_base_v001_signal(ncfo, closeadj):
    result = _mean(ncfo, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed ncfo times closeadj
def cbr_f008_cash_burn_rate_raw_63d_base_v002_signal(ncfo, closeadj):
    result = _mean(ncfo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed ncfo times closeadj
def cbr_f008_cash_burn_rate_raw_126d_base_v003_signal(ncfo, closeadj):
    result = _mean(ncfo, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed ncfo times closeadj
def cbr_f008_cash_burn_rate_raw_252d_base_v004_signal(ncfo, closeadj):
    result = _mean(ncfo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed ncfo times closeadj
def cbr_f008_cash_burn_rate_raw_504d_base_v005_signal(ncfo, closeadj):
    result = _mean(ncfo, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(ncfo) times closeadj
def cbr_f008_cash_burn_rate_log_21d_base_v006_signal(ncfo, closeadj):
    result = _mean(_cash_burn_rate_log(ncfo), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(ncfo) times closeadj
def cbr_f008_cash_burn_rate_log_63d_base_v007_signal(ncfo, closeadj):
    result = _mean(_cash_burn_rate_log(ncfo), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(ncfo) times closeadj
def cbr_f008_cash_burn_rate_log_126d_base_v008_signal(ncfo, closeadj):
    result = _mean(_cash_burn_rate_log(ncfo), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(ncfo) times closeadj
def cbr_f008_cash_burn_rate_log_252d_base_v009_signal(ncfo, closeadj):
    result = _mean(_cash_burn_rate_log(ncfo), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(ncfo) times closeadj
def cbr_f008_cash_burn_rate_log_504d_base_v010_signal(ncfo, closeadj):
    result = _mean(_cash_burn_rate_log(ncfo), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/cashneq mean
def cbr_f008_cash_burn_rate_per_cashneq_63d_base_v011_signal(ncfo, cashneq):
    result = _mean(_cash_burn_rate_scaled(ncfo, cashneq), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/cashneq mean
def cbr_f008_cash_burn_rate_per_cashneq_252d_base_v012_signal(ncfo, cashneq):
    result = _mean(_cash_burn_rate_scaled(ncfo, cashneq), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo/cashneq mean
def cbr_f008_cash_burn_rate_per_cashneq_504d_base_v013_signal(ncfo, cashneq):
    result = _mean(_cash_burn_rate_scaled(ncfo, cashneq), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/assets mean
def cbr_f008_cash_burn_rate_per_assets_63d_base_v014_signal(ncfo, assets):
    result = _mean(_cash_burn_rate_scaled(ncfo, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/assets mean
def cbr_f008_cash_burn_rate_per_assets_252d_base_v015_signal(ncfo, assets):
    result = _mean(_cash_burn_rate_scaled(ncfo, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo/assets mean
def cbr_f008_cash_burn_rate_per_assets_504d_base_v016_signal(ncfo, assets):
    result = _mean(_cash_burn_rate_scaled(ncfo, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/marketcap mean
def cbr_f008_cash_burn_rate_per_marketcap_63d_base_v017_signal(ncfo, marketcap):
    result = _mean(_cash_burn_rate_scaled(ncfo, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/marketcap mean
def cbr_f008_cash_burn_rate_per_marketcap_252d_base_v018_signal(ncfo, marketcap):
    result = _mean(_cash_burn_rate_scaled(ncfo, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo/marketcap mean
def cbr_f008_cash_burn_rate_per_marketcap_504d_base_v019_signal(ncfo, marketcap):
    result = _mean(_cash_burn_rate_scaled(ncfo, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/equity mean
def cbr_f008_cash_burn_rate_per_equity_63d_base_v020_signal(ncfo, equity):
    result = _mean(_cash_burn_rate_scaled(ncfo, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/equity mean
def cbr_f008_cash_burn_rate_per_equity_252d_base_v021_signal(ncfo, equity):
    result = _mean(_cash_burn_rate_scaled(ncfo, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo/equity mean
def cbr_f008_cash_burn_rate_per_equity_504d_base_v022_signal(ncfo, equity):
    result = _mean(_cash_burn_rate_scaled(ncfo, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/debt mean
def cbr_f008_cash_burn_rate_per_debt_63d_base_v023_signal(ncfo, debt):
    result = _mean(_cash_burn_rate_scaled(ncfo, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/debt mean
def cbr_f008_cash_burn_rate_per_debt_252d_base_v024_signal(ncfo, debt):
    result = _mean(_cash_burn_rate_scaled(ncfo, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo/debt mean
def cbr_f008_cash_burn_rate_per_debt_504d_base_v025_signal(ncfo, debt):
    result = _mean(_cash_burn_rate_scaled(ncfo, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo per share times closeadj
def cbr_f008_cash_burn_rate_pershare_21d_base_v026_signal(ncfo, sharesbas, closeadj):
    ps = _cash_burn_rate_per_share(ncfo, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo per share times closeadj
def cbr_f008_cash_burn_rate_pershare_63d_base_v027_signal(ncfo, sharesbas, closeadj):
    ps = _cash_burn_rate_per_share(ncfo, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ncfo per share times closeadj
def cbr_f008_cash_burn_rate_pershare_126d_base_v028_signal(ncfo, sharesbas, closeadj):
    ps = _cash_burn_rate_per_share(ncfo, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo per share times closeadj
def cbr_f008_cash_burn_rate_pershare_252d_base_v029_signal(ncfo, sharesbas, closeadj):
    ps = _cash_burn_rate_per_share(ncfo, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo per share times closeadj
def cbr_f008_cash_burn_rate_pershare_504d_base_v030_signal(ncfo, sharesbas, closeadj):
    ps = _cash_burn_rate_per_share(ncfo, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of ncfo times closeadj
def cbr_f008_cash_burn_rate_std_63d_base_v031_signal(ncfo, closeadj):
    result = _std(ncfo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of ncfo times closeadj
def cbr_f008_cash_burn_rate_std_252d_base_v032_signal(ncfo, closeadj):
    result = _std(ncfo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of ncfo times closeadj
def cbr_f008_cash_burn_rate_std_504d_base_v033_signal(ncfo, closeadj):
    result = _std(ncfo, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of ncfo
def cbr_f008_cash_burn_rate_z_252d_base_v034_signal(ncfo):
    result = _z(ncfo, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of ncfo
def cbr_f008_cash_burn_rate_z_504d_base_v035_signal(ncfo):
    result = _z(ncfo, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(ncfo)
def cbr_f008_cash_burn_rate_logz_252d_base_v036_signal(ncfo):
    result = _z(_cash_burn_rate_log(ncfo), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(ncfo)
def cbr_f008_cash_burn_rate_logz_504d_base_v037_signal(ncfo):
    result = _z(_cash_burn_rate_log(ncfo), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of ncfo^2 times closeadj
def cbr_f008_cash_burn_rate_sq_63d_base_v038_signal(ncfo, closeadj):
    result = _mean(ncfo * ncfo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of ncfo^2 times closeadj
def cbr_f008_cash_burn_rate_sq_252d_base_v039_signal(ncfo, closeadj):
    result = _mean(ncfo * ncfo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(ncfo) times closeadj
def cbr_f008_cash_burn_rate_sign_21d_base_v040_signal(ncfo, closeadj):
    result = _mean(np.sign(ncfo), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(ncfo) times closeadj
def cbr_f008_cash_burn_rate_sign_63d_base_v041_signal(ncfo, closeadj):
    result = _mean(np.sign(ncfo), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(ncfo) times closeadj
def cbr_f008_cash_burn_rate_sign_252d_base_v042_signal(ncfo, closeadj):
    result = _mean(np.sign(ncfo), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/opex mean
def cbr_f008_cash_burn_rate_per_opex_63d_base_v043_signal(ncfo, opex):
    result = _mean(_cash_burn_rate_scaled(ncfo, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/opex mean
def cbr_f008_cash_burn_rate_per_opex_252d_base_v044_signal(ncfo, opex):
    result = _mean(_cash_burn_rate_scaled(ncfo, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/ebitda mean
def cbr_f008_cash_burn_rate_per_ebitda_63d_base_v045_signal(ncfo, ebitda):
    result = _mean(_cash_burn_rate_scaled(ncfo, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/ebitda mean
def cbr_f008_cash_burn_rate_per_ebitda_252d_base_v046_signal(ncfo, ebitda):
    result = _mean(_cash_burn_rate_scaled(ncfo, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/capex mean
def cbr_f008_cash_burn_rate_per_capex_63d_base_v047_signal(ncfo, capex):
    result = _mean(_cash_burn_rate_scaled(ncfo, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/capex mean
def cbr_f008_cash_burn_rate_per_capex_252d_base_v048_signal(ncfo, capex):
    result = _mean(_cash_burn_rate_scaled(ncfo, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/liabilities mean
def cbr_f008_cash_burn_rate_per_liabilities_63d_base_v049_signal(ncfo, liabilities):
    result = _mean(_cash_burn_rate_scaled(ncfo, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/liabilities mean
def cbr_f008_cash_burn_rate_per_liabilities_252d_base_v050_signal(ncfo, liabilities):
    result = _mean(_cash_burn_rate_scaled(ncfo, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo relative to 252d max times closeadj
def cbr_f008_cash_burn_rate_relmax_252d_base_v051_signal(ncfo, closeadj):
    peak = ncfo.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (ncfo / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo relative to 504d max times closeadj
def cbr_f008_cash_burn_rate_relmax_504d_base_v052_signal(ncfo, closeadj):
    peak = ncfo.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (ncfo / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo relative to 252d min times closeadj
def cbr_f008_cash_burn_rate_relmin_252d_base_v053_signal(ncfo, closeadj):
    trough = ncfo.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (ncfo / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo relative to 504d min times closeadj
def cbr_f008_cash_burn_rate_relmin_504d_base_v054_signal(ncfo, closeadj):
    trough = ncfo.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (ncfo / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of ncfo times closeadj
def cbr_f008_cash_burn_rate_pct_21d_base_v055_signal(ncfo, closeadj):
    result = _pct_change(ncfo, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of ncfo times closeadj
def cbr_f008_cash_burn_rate_pct_63d_base_v056_signal(ncfo, closeadj):
    result = _pct_change(ncfo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of ncfo times closeadj
def cbr_f008_cash_burn_rate_pct_252d_base_v057_signal(ncfo, closeadj):
    result = _pct_change(ncfo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of ncfo times closeadj
def cbr_f008_cash_burn_rate_sum_63d_base_v058_signal(ncfo, closeadj):
    result = ncfo.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of ncfo times closeadj
def cbr_f008_cash_burn_rate_sum_252d_base_v059_signal(ncfo, closeadj):
    result = ncfo.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of ncfo times closeadj
def cbr_f008_cash_burn_rate_sum_504d_base_v060_signal(ncfo, closeadj):
    result = ncfo.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfo(63d) / smoothed cashneq(252d) x closeadj
def cbr_f008_cash_burn_rate_rom_cashneq_252_63d_base_v061_signal(ncfo, cashneq, closeadj):
    n = _mean(ncfo, 63)
    d = _mean(cashneq, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfo(126d) / smoothed cashneq(504d) x closeadj
def cbr_f008_cash_burn_rate_rom_cashneq_504_126d_base_v062_signal(ncfo, cashneq, closeadj):
    n = _mean(ncfo, 126)
    d = _mean(cashneq, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfo(63d) / smoothed assets(252d) x closeadj
def cbr_f008_cash_burn_rate_rom_assets_252_63d_base_v063_signal(ncfo, assets, closeadj):
    n = _mean(ncfo, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfo(126d) / smoothed assets(504d) x closeadj
def cbr_f008_cash_burn_rate_rom_assets_504_126d_base_v064_signal(ncfo, assets, closeadj):
    n = _mean(ncfo, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfo(63d) / smoothed marketcap(252d) x closeadj
def cbr_f008_cash_burn_rate_rom_marketcap_252_63d_base_v065_signal(ncfo, marketcap, closeadj):
    n = _mean(ncfo, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfo(126d) / smoothed marketcap(504d) x closeadj
def cbr_f008_cash_burn_rate_rom_marketcap_504_126d_base_v066_signal(ncfo, marketcap, closeadj):
    n = _mean(ncfo, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ncfo) / std(cashneq)
def cbr_f008_cash_burn_rate_volratio_cashneq_252d_base_v067_signal(ncfo, cashneq):
    n = _std(ncfo, 252)
    d = _std(cashneq, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ncfo) / std(cashneq)
def cbr_f008_cash_burn_rate_volratio_cashneq_504d_base_v068_signal(ncfo, cashneq):
    n = _std(ncfo, 504)
    d = _std(cashneq, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ncfo) / std(assets)
def cbr_f008_cash_burn_rate_volratio_assets_252d_base_v069_signal(ncfo, assets):
    n = _std(ncfo, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ncfo) / std(assets)
def cbr_f008_cash_burn_rate_volratio_assets_504d_base_v070_signal(ncfo, assets):
    n = _std(ncfo, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed ncfo times closeadj
def cbr_f008_cash_burn_rate_raw_5d_base_v071_signal(ncfo, closeadj):
    result = _mean(ncfo, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed ncfo times closeadj
def cbr_f008_cash_burn_rate_raw_1008d_base_v072_signal(ncfo, closeadj):
    result = _mean(ncfo, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ncfo/cashneq
def cbr_f008_cash_burn_rate_log_per_cashneq_252d_base_v073_signal(ncfo, cashneq):
    s = _cash_burn_rate_scaled(ncfo, cashneq)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ncfo/cashneq
def cbr_f008_cash_burn_rate_log_per_cashneq_504d_base_v074_signal(ncfo, cashneq):
    s = _cash_burn_rate_scaled(ncfo, cashneq)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ncfo/assets
def cbr_f008_cash_burn_rate_log_per_assets_252d_base_v075_signal(ncfo, assets):
    s = _cash_burn_rate_scaled(ncfo, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
