"""Family f58 - Comprehensive vs net income gap  (I_Earnings_EPS) | base 001-075"""
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
def _compinc_gap_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _compinc_gap_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _compinc_gap_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed consolinc times closeadj
def cig_f58_compinc_gap_raw_21d_base_v001_signal(consolinc, closeadj):
    result = _mean(consolinc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed consolinc times closeadj
def cig_f58_compinc_gap_raw_63d_base_v002_signal(consolinc, closeadj):
    result = _mean(consolinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed consolinc times closeadj
def cig_f58_compinc_gap_raw_126d_base_v003_signal(consolinc, closeadj):
    result = _mean(consolinc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed consolinc times closeadj
def cig_f58_compinc_gap_raw_252d_base_v004_signal(consolinc, closeadj):
    result = _mean(consolinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed consolinc times closeadj
def cig_f58_compinc_gap_raw_504d_base_v005_signal(consolinc, closeadj):
    result = _mean(consolinc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(consolinc) times closeadj
def cig_f58_compinc_gap_log_21d_base_v006_signal(consolinc, closeadj):
    result = _mean(_compinc_gap_log(consolinc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(consolinc) times closeadj
def cig_f58_compinc_gap_log_63d_base_v007_signal(consolinc, closeadj):
    result = _mean(_compinc_gap_log(consolinc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(consolinc) times closeadj
def cig_f58_compinc_gap_log_126d_base_v008_signal(consolinc, closeadj):
    result = _mean(_compinc_gap_log(consolinc), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(consolinc) times closeadj
def cig_f58_compinc_gap_log_252d_base_v009_signal(consolinc, closeadj):
    result = _mean(_compinc_gap_log(consolinc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(consolinc) times closeadj
def cig_f58_compinc_gap_log_504d_base_v010_signal(consolinc, closeadj):
    result = _mean(_compinc_gap_log(consolinc), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d consolinc/assets mean
def cig_f58_compinc_gap_per_assets_63d_base_v011_signal(consolinc, assets):
    result = _mean(_compinc_gap_scaled(consolinc, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d consolinc/assets mean
def cig_f58_compinc_gap_per_assets_252d_base_v012_signal(consolinc, assets):
    result = _mean(_compinc_gap_scaled(consolinc, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d consolinc/assets mean
def cig_f58_compinc_gap_per_assets_504d_base_v013_signal(consolinc, assets):
    result = _mean(_compinc_gap_scaled(consolinc, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d consolinc/marketcap mean
def cig_f58_compinc_gap_per_marketcap_63d_base_v014_signal(consolinc, marketcap):
    result = _mean(_compinc_gap_scaled(consolinc, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d consolinc/marketcap mean
def cig_f58_compinc_gap_per_marketcap_252d_base_v015_signal(consolinc, marketcap):
    result = _mean(_compinc_gap_scaled(consolinc, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d consolinc/marketcap mean
def cig_f58_compinc_gap_per_marketcap_504d_base_v016_signal(consolinc, marketcap):
    result = _mean(_compinc_gap_scaled(consolinc, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d consolinc/equity mean
def cig_f58_compinc_gap_per_equity_63d_base_v017_signal(consolinc, equity):
    result = _mean(_compinc_gap_scaled(consolinc, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d consolinc/equity mean
def cig_f58_compinc_gap_per_equity_252d_base_v018_signal(consolinc, equity):
    result = _mean(_compinc_gap_scaled(consolinc, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d consolinc/equity mean
def cig_f58_compinc_gap_per_equity_504d_base_v019_signal(consolinc, equity):
    result = _mean(_compinc_gap_scaled(consolinc, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d consolinc/debt mean
def cig_f58_compinc_gap_per_debt_63d_base_v020_signal(consolinc, debt):
    result = _mean(_compinc_gap_scaled(consolinc, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d consolinc/debt mean
def cig_f58_compinc_gap_per_debt_252d_base_v021_signal(consolinc, debt):
    result = _mean(_compinc_gap_scaled(consolinc, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d consolinc/debt mean
def cig_f58_compinc_gap_per_debt_504d_base_v022_signal(consolinc, debt):
    result = _mean(_compinc_gap_scaled(consolinc, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d consolinc/revenue mean
def cig_f58_compinc_gap_per_revenue_63d_base_v023_signal(consolinc, revenue):
    result = _mean(_compinc_gap_scaled(consolinc, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d consolinc/revenue mean
def cig_f58_compinc_gap_per_revenue_252d_base_v024_signal(consolinc, revenue):
    result = _mean(_compinc_gap_scaled(consolinc, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d consolinc/revenue mean
def cig_f58_compinc_gap_per_revenue_504d_base_v025_signal(consolinc, revenue):
    result = _mean(_compinc_gap_scaled(consolinc, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d consolinc per share times closeadj
def cig_f58_compinc_gap_pershare_21d_base_v026_signal(consolinc, sharesbas, closeadj):
    ps = _compinc_gap_per_share(consolinc, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d consolinc per share times closeadj
def cig_f58_compinc_gap_pershare_63d_base_v027_signal(consolinc, sharesbas, closeadj):
    ps = _compinc_gap_per_share(consolinc, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d consolinc per share times closeadj
def cig_f58_compinc_gap_pershare_126d_base_v028_signal(consolinc, sharesbas, closeadj):
    ps = _compinc_gap_per_share(consolinc, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d consolinc per share times closeadj
def cig_f58_compinc_gap_pershare_252d_base_v029_signal(consolinc, sharesbas, closeadj):
    ps = _compinc_gap_per_share(consolinc, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d consolinc per share times closeadj
def cig_f58_compinc_gap_pershare_504d_base_v030_signal(consolinc, sharesbas, closeadj):
    ps = _compinc_gap_per_share(consolinc, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of consolinc times closeadj
def cig_f58_compinc_gap_std_63d_base_v031_signal(consolinc, closeadj):
    result = _std(consolinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of consolinc times closeadj
def cig_f58_compinc_gap_std_252d_base_v032_signal(consolinc, closeadj):
    result = _std(consolinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of consolinc times closeadj
def cig_f58_compinc_gap_std_504d_base_v033_signal(consolinc, closeadj):
    result = _std(consolinc, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of consolinc
def cig_f58_compinc_gap_z_252d_base_v034_signal(consolinc):
    result = _z(consolinc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of consolinc
def cig_f58_compinc_gap_z_504d_base_v035_signal(consolinc):
    result = _z(consolinc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(consolinc)
def cig_f58_compinc_gap_logz_252d_base_v036_signal(consolinc):
    result = _z(_compinc_gap_log(consolinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(consolinc)
def cig_f58_compinc_gap_logz_504d_base_v037_signal(consolinc):
    result = _z(_compinc_gap_log(consolinc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of consolinc^2 times closeadj
def cig_f58_compinc_gap_sq_63d_base_v038_signal(consolinc, closeadj):
    result = _mean(consolinc * consolinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of consolinc^2 times closeadj
def cig_f58_compinc_gap_sq_252d_base_v039_signal(consolinc, closeadj):
    result = _mean(consolinc * consolinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(consolinc) times closeadj
def cig_f58_compinc_gap_sign_21d_base_v040_signal(consolinc, closeadj):
    result = _mean(np.sign(consolinc), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(consolinc) times closeadj
def cig_f58_compinc_gap_sign_63d_base_v041_signal(consolinc, closeadj):
    result = _mean(np.sign(consolinc), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(consolinc) times closeadj
def cig_f58_compinc_gap_sign_252d_base_v042_signal(consolinc, closeadj):
    result = _mean(np.sign(consolinc), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d consolinc/opex mean
def cig_f58_compinc_gap_per_opex_63d_base_v043_signal(consolinc, opex):
    result = _mean(_compinc_gap_scaled(consolinc, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d consolinc/opex mean
def cig_f58_compinc_gap_per_opex_252d_base_v044_signal(consolinc, opex):
    result = _mean(_compinc_gap_scaled(consolinc, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d consolinc/ebitda mean
def cig_f58_compinc_gap_per_ebitda_63d_base_v045_signal(consolinc, ebitda):
    result = _mean(_compinc_gap_scaled(consolinc, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d consolinc/ebitda mean
def cig_f58_compinc_gap_per_ebitda_252d_base_v046_signal(consolinc, ebitda):
    result = _mean(_compinc_gap_scaled(consolinc, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d consolinc/capex mean
def cig_f58_compinc_gap_per_capex_63d_base_v047_signal(consolinc, capex):
    result = _mean(_compinc_gap_scaled(consolinc, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d consolinc/capex mean
def cig_f58_compinc_gap_per_capex_252d_base_v048_signal(consolinc, capex):
    result = _mean(_compinc_gap_scaled(consolinc, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d consolinc/liabilities mean
def cig_f58_compinc_gap_per_liabilities_63d_base_v049_signal(consolinc, liabilities):
    result = _mean(_compinc_gap_scaled(consolinc, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d consolinc/liabilities mean
def cig_f58_compinc_gap_per_liabilities_252d_base_v050_signal(consolinc, liabilities):
    result = _mean(_compinc_gap_scaled(consolinc, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# consolinc relative to 252d max times closeadj
def cig_f58_compinc_gap_relmax_252d_base_v051_signal(consolinc, closeadj):
    peak = consolinc.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (consolinc / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# consolinc relative to 504d max times closeadj
def cig_f58_compinc_gap_relmax_504d_base_v052_signal(consolinc, closeadj):
    peak = consolinc.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (consolinc / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# consolinc relative to 252d min times closeadj
def cig_f58_compinc_gap_relmin_252d_base_v053_signal(consolinc, closeadj):
    trough = consolinc.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (consolinc / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# consolinc relative to 504d min times closeadj
def cig_f58_compinc_gap_relmin_504d_base_v054_signal(consolinc, closeadj):
    trough = consolinc.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (consolinc / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of consolinc times closeadj
def cig_f58_compinc_gap_pct_21d_base_v055_signal(consolinc, closeadj):
    result = _pct_change(consolinc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of consolinc times closeadj
def cig_f58_compinc_gap_pct_63d_base_v056_signal(consolinc, closeadj):
    result = _pct_change(consolinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of consolinc times closeadj
def cig_f58_compinc_gap_pct_252d_base_v057_signal(consolinc, closeadj):
    result = _pct_change(consolinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of consolinc times closeadj
def cig_f58_compinc_gap_sum_63d_base_v058_signal(consolinc, closeadj):
    result = consolinc.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of consolinc times closeadj
def cig_f58_compinc_gap_sum_252d_base_v059_signal(consolinc, closeadj):
    result = consolinc.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of consolinc times closeadj
def cig_f58_compinc_gap_sum_504d_base_v060_signal(consolinc, closeadj):
    result = consolinc.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed consolinc(63d) / smoothed assets(252d) x closeadj
def cig_f58_compinc_gap_rom_assets_252_63d_base_v061_signal(consolinc, assets, closeadj):
    n = _mean(consolinc, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed consolinc(126d) / smoothed assets(504d) x closeadj
def cig_f58_compinc_gap_rom_assets_504_126d_base_v062_signal(consolinc, assets, closeadj):
    n = _mean(consolinc, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed consolinc(63d) / smoothed marketcap(252d) x closeadj
def cig_f58_compinc_gap_rom_marketcap_252_63d_base_v063_signal(consolinc, marketcap, closeadj):
    n = _mean(consolinc, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed consolinc(126d) / smoothed marketcap(504d) x closeadj
def cig_f58_compinc_gap_rom_marketcap_504_126d_base_v064_signal(consolinc, marketcap, closeadj):
    n = _mean(consolinc, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed consolinc(63d) / smoothed equity(252d) x closeadj
def cig_f58_compinc_gap_rom_equity_252_63d_base_v065_signal(consolinc, equity, closeadj):
    n = _mean(consolinc, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed consolinc(126d) / smoothed equity(504d) x closeadj
def cig_f58_compinc_gap_rom_equity_504_126d_base_v066_signal(consolinc, equity, closeadj):
    n = _mean(consolinc, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(consolinc) / std(assets)
def cig_f58_compinc_gap_volratio_assets_252d_base_v067_signal(consolinc, assets):
    n = _std(consolinc, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(consolinc) / std(assets)
def cig_f58_compinc_gap_volratio_assets_504d_base_v068_signal(consolinc, assets):
    n = _std(consolinc, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(consolinc) / std(marketcap)
def cig_f58_compinc_gap_volratio_marketcap_252d_base_v069_signal(consolinc, marketcap):
    n = _std(consolinc, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(consolinc) / std(marketcap)
def cig_f58_compinc_gap_volratio_marketcap_504d_base_v070_signal(consolinc, marketcap):
    n = _std(consolinc, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed consolinc times closeadj
def cig_f58_compinc_gap_raw_5d_base_v071_signal(consolinc, closeadj):
    result = _mean(consolinc, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed consolinc times closeadj
def cig_f58_compinc_gap_raw_1008d_base_v072_signal(consolinc, closeadj):
    result = _mean(consolinc, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of consolinc/assets
def cig_f58_compinc_gap_log_per_assets_252d_base_v073_signal(consolinc, assets):
    s = _compinc_gap_scaled(consolinc, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of consolinc/assets
def cig_f58_compinc_gap_log_per_assets_504d_base_v074_signal(consolinc, assets):
    s = _compinc_gap_scaled(consolinc, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of consolinc/marketcap
def cig_f58_compinc_gap_log_per_marketcap_252d_base_v075_signal(consolinc, marketcap):
    s = _compinc_gap_scaled(consolinc, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
