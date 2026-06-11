"""Family f71 - Tax position / NOL signal  (L_EarningsQuality) | base 001-075"""
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
def _nol_signal_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _nol_signal_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _nol_signal_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed taxexp times closeadj
def nol_f71_nol_signal_raw_21d_base_v001_signal(taxexp, closeadj):
    result = _mean(taxexp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed taxexp times closeadj
def nol_f71_nol_signal_raw_63d_base_v002_signal(taxexp, closeadj):
    result = _mean(taxexp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed taxexp times closeadj
def nol_f71_nol_signal_raw_126d_base_v003_signal(taxexp, closeadj):
    result = _mean(taxexp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed taxexp times closeadj
def nol_f71_nol_signal_raw_252d_base_v004_signal(taxexp, closeadj):
    result = _mean(taxexp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed taxexp times closeadj
def nol_f71_nol_signal_raw_504d_base_v005_signal(taxexp, closeadj):
    result = _mean(taxexp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(taxexp) times closeadj
def nol_f71_nol_signal_log_21d_base_v006_signal(taxexp, closeadj):
    result = _mean(_nol_signal_log(taxexp), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(taxexp) times closeadj
def nol_f71_nol_signal_log_63d_base_v007_signal(taxexp, closeadj):
    result = _mean(_nol_signal_log(taxexp), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(taxexp) times closeadj
def nol_f71_nol_signal_log_126d_base_v008_signal(taxexp, closeadj):
    result = _mean(_nol_signal_log(taxexp), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(taxexp) times closeadj
def nol_f71_nol_signal_log_252d_base_v009_signal(taxexp, closeadj):
    result = _mean(_nol_signal_log(taxexp), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(taxexp) times closeadj
def nol_f71_nol_signal_log_504d_base_v010_signal(taxexp, closeadj):
    result = _mean(_nol_signal_log(taxexp), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxexp/assets mean
def nol_f71_nol_signal_per_assets_63d_base_v011_signal(taxexp, assets):
    result = _mean(_nol_signal_scaled(taxexp, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxexp/assets mean
def nol_f71_nol_signal_per_assets_252d_base_v012_signal(taxexp, assets):
    result = _mean(_nol_signal_scaled(taxexp, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d taxexp/assets mean
def nol_f71_nol_signal_per_assets_504d_base_v013_signal(taxexp, assets):
    result = _mean(_nol_signal_scaled(taxexp, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxexp/marketcap mean
def nol_f71_nol_signal_per_marketcap_63d_base_v014_signal(taxexp, marketcap):
    result = _mean(_nol_signal_scaled(taxexp, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxexp/marketcap mean
def nol_f71_nol_signal_per_marketcap_252d_base_v015_signal(taxexp, marketcap):
    result = _mean(_nol_signal_scaled(taxexp, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d taxexp/marketcap mean
def nol_f71_nol_signal_per_marketcap_504d_base_v016_signal(taxexp, marketcap):
    result = _mean(_nol_signal_scaled(taxexp, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxexp/equity mean
def nol_f71_nol_signal_per_equity_63d_base_v017_signal(taxexp, equity):
    result = _mean(_nol_signal_scaled(taxexp, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxexp/equity mean
def nol_f71_nol_signal_per_equity_252d_base_v018_signal(taxexp, equity):
    result = _mean(_nol_signal_scaled(taxexp, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d taxexp/equity mean
def nol_f71_nol_signal_per_equity_504d_base_v019_signal(taxexp, equity):
    result = _mean(_nol_signal_scaled(taxexp, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxexp/debt mean
def nol_f71_nol_signal_per_debt_63d_base_v020_signal(taxexp, debt):
    result = _mean(_nol_signal_scaled(taxexp, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxexp/debt mean
def nol_f71_nol_signal_per_debt_252d_base_v021_signal(taxexp, debt):
    result = _mean(_nol_signal_scaled(taxexp, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d taxexp/debt mean
def nol_f71_nol_signal_per_debt_504d_base_v022_signal(taxexp, debt):
    result = _mean(_nol_signal_scaled(taxexp, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxexp/revenue mean
def nol_f71_nol_signal_per_revenue_63d_base_v023_signal(taxexp, revenue):
    result = _mean(_nol_signal_scaled(taxexp, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxexp/revenue mean
def nol_f71_nol_signal_per_revenue_252d_base_v024_signal(taxexp, revenue):
    result = _mean(_nol_signal_scaled(taxexp, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d taxexp/revenue mean
def nol_f71_nol_signal_per_revenue_504d_base_v025_signal(taxexp, revenue):
    result = _mean(_nol_signal_scaled(taxexp, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d taxexp per share times closeadj
def nol_f71_nol_signal_pershare_21d_base_v026_signal(taxexp, sharesbas, closeadj):
    ps = _nol_signal_per_share(taxexp, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxexp per share times closeadj
def nol_f71_nol_signal_pershare_63d_base_v027_signal(taxexp, sharesbas, closeadj):
    ps = _nol_signal_per_share(taxexp, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d taxexp per share times closeadj
def nol_f71_nol_signal_pershare_126d_base_v028_signal(taxexp, sharesbas, closeadj):
    ps = _nol_signal_per_share(taxexp, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxexp per share times closeadj
def nol_f71_nol_signal_pershare_252d_base_v029_signal(taxexp, sharesbas, closeadj):
    ps = _nol_signal_per_share(taxexp, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d taxexp per share times closeadj
def nol_f71_nol_signal_pershare_504d_base_v030_signal(taxexp, sharesbas, closeadj):
    ps = _nol_signal_per_share(taxexp, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of taxexp times closeadj
def nol_f71_nol_signal_std_63d_base_v031_signal(taxexp, closeadj):
    result = _std(taxexp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of taxexp times closeadj
def nol_f71_nol_signal_std_252d_base_v032_signal(taxexp, closeadj):
    result = _std(taxexp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of taxexp times closeadj
def nol_f71_nol_signal_std_504d_base_v033_signal(taxexp, closeadj):
    result = _std(taxexp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of taxexp
def nol_f71_nol_signal_z_252d_base_v034_signal(taxexp):
    result = _z(taxexp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of taxexp
def nol_f71_nol_signal_z_504d_base_v035_signal(taxexp):
    result = _z(taxexp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(taxexp)
def nol_f71_nol_signal_logz_252d_base_v036_signal(taxexp):
    result = _z(_nol_signal_log(taxexp), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(taxexp)
def nol_f71_nol_signal_logz_504d_base_v037_signal(taxexp):
    result = _z(_nol_signal_log(taxexp), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of taxexp^2 times closeadj
def nol_f71_nol_signal_sq_63d_base_v038_signal(taxexp, closeadj):
    result = _mean(taxexp * taxexp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of taxexp^2 times closeadj
def nol_f71_nol_signal_sq_252d_base_v039_signal(taxexp, closeadj):
    result = _mean(taxexp * taxexp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(taxexp) times closeadj
def nol_f71_nol_signal_sign_21d_base_v040_signal(taxexp, closeadj):
    result = _mean(np.sign(taxexp), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(taxexp) times closeadj
def nol_f71_nol_signal_sign_63d_base_v041_signal(taxexp, closeadj):
    result = _mean(np.sign(taxexp), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(taxexp) times closeadj
def nol_f71_nol_signal_sign_252d_base_v042_signal(taxexp, closeadj):
    result = _mean(np.sign(taxexp), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxexp/opex mean
def nol_f71_nol_signal_per_opex_63d_base_v043_signal(taxexp, opex):
    result = _mean(_nol_signal_scaled(taxexp, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxexp/opex mean
def nol_f71_nol_signal_per_opex_252d_base_v044_signal(taxexp, opex):
    result = _mean(_nol_signal_scaled(taxexp, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxexp/ebitda mean
def nol_f71_nol_signal_per_ebitda_63d_base_v045_signal(taxexp, ebitda):
    result = _mean(_nol_signal_scaled(taxexp, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxexp/ebitda mean
def nol_f71_nol_signal_per_ebitda_252d_base_v046_signal(taxexp, ebitda):
    result = _mean(_nol_signal_scaled(taxexp, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxexp/capex mean
def nol_f71_nol_signal_per_capex_63d_base_v047_signal(taxexp, capex):
    result = _mean(_nol_signal_scaled(taxexp, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxexp/capex mean
def nol_f71_nol_signal_per_capex_252d_base_v048_signal(taxexp, capex):
    result = _mean(_nol_signal_scaled(taxexp, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d taxexp/liabilities mean
def nol_f71_nol_signal_per_liabilities_63d_base_v049_signal(taxexp, liabilities):
    result = _mean(_nol_signal_scaled(taxexp, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d taxexp/liabilities mean
def nol_f71_nol_signal_per_liabilities_252d_base_v050_signal(taxexp, liabilities):
    result = _mean(_nol_signal_scaled(taxexp, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# taxexp relative to 252d max times closeadj
def nol_f71_nol_signal_relmax_252d_base_v051_signal(taxexp, closeadj):
    peak = taxexp.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (taxexp / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# taxexp relative to 504d max times closeadj
def nol_f71_nol_signal_relmax_504d_base_v052_signal(taxexp, closeadj):
    peak = taxexp.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (taxexp / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# taxexp relative to 252d min times closeadj
def nol_f71_nol_signal_relmin_252d_base_v053_signal(taxexp, closeadj):
    trough = taxexp.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (taxexp / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# taxexp relative to 504d min times closeadj
def nol_f71_nol_signal_relmin_504d_base_v054_signal(taxexp, closeadj):
    trough = taxexp.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (taxexp / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of taxexp times closeadj
def nol_f71_nol_signal_pct_21d_base_v055_signal(taxexp, closeadj):
    result = _pct_change(taxexp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of taxexp times closeadj
def nol_f71_nol_signal_pct_63d_base_v056_signal(taxexp, closeadj):
    result = _pct_change(taxexp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of taxexp times closeadj
def nol_f71_nol_signal_pct_252d_base_v057_signal(taxexp, closeadj):
    result = _pct_change(taxexp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of taxexp times closeadj
def nol_f71_nol_signal_sum_63d_base_v058_signal(taxexp, closeadj):
    result = taxexp.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of taxexp times closeadj
def nol_f71_nol_signal_sum_252d_base_v059_signal(taxexp, closeadj):
    result = taxexp.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of taxexp times closeadj
def nol_f71_nol_signal_sum_504d_base_v060_signal(taxexp, closeadj):
    result = taxexp.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed taxexp(63d) / smoothed assets(252d) x closeadj
def nol_f71_nol_signal_rom_assets_252_63d_base_v061_signal(taxexp, assets, closeadj):
    n = _mean(taxexp, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed taxexp(126d) / smoothed assets(504d) x closeadj
def nol_f71_nol_signal_rom_assets_504_126d_base_v062_signal(taxexp, assets, closeadj):
    n = _mean(taxexp, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed taxexp(63d) / smoothed marketcap(252d) x closeadj
def nol_f71_nol_signal_rom_marketcap_252_63d_base_v063_signal(taxexp, marketcap, closeadj):
    n = _mean(taxexp, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed taxexp(126d) / smoothed marketcap(504d) x closeadj
def nol_f71_nol_signal_rom_marketcap_504_126d_base_v064_signal(taxexp, marketcap, closeadj):
    n = _mean(taxexp, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed taxexp(63d) / smoothed equity(252d) x closeadj
def nol_f71_nol_signal_rom_equity_252_63d_base_v065_signal(taxexp, equity, closeadj):
    n = _mean(taxexp, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed taxexp(126d) / smoothed equity(504d) x closeadj
def nol_f71_nol_signal_rom_equity_504_126d_base_v066_signal(taxexp, equity, closeadj):
    n = _mean(taxexp, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(taxexp) / std(assets)
def nol_f71_nol_signal_volratio_assets_252d_base_v067_signal(taxexp, assets):
    n = _std(taxexp, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(taxexp) / std(assets)
def nol_f71_nol_signal_volratio_assets_504d_base_v068_signal(taxexp, assets):
    n = _std(taxexp, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(taxexp) / std(marketcap)
def nol_f71_nol_signal_volratio_marketcap_252d_base_v069_signal(taxexp, marketcap):
    n = _std(taxexp, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(taxexp) / std(marketcap)
def nol_f71_nol_signal_volratio_marketcap_504d_base_v070_signal(taxexp, marketcap):
    n = _std(taxexp, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed taxexp times closeadj
def nol_f71_nol_signal_raw_5d_base_v071_signal(taxexp, closeadj):
    result = _mean(taxexp, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed taxexp times closeadj
def nol_f71_nol_signal_raw_1008d_base_v072_signal(taxexp, closeadj):
    result = _mean(taxexp, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of taxexp/assets
def nol_f71_nol_signal_log_per_assets_252d_base_v073_signal(taxexp, assets):
    s = _nol_signal_scaled(taxexp, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of taxexp/assets
def nol_f71_nol_signal_log_per_assets_504d_base_v074_signal(taxexp, assets):
    s = _nol_signal_scaled(taxexp, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of taxexp/marketcap
def nol_f71_nol_signal_log_per_marketcap_252d_base_v075_signal(taxexp, marketcap):
    s = _nol_signal_scaled(taxexp, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
