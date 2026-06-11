"""Family f28 - Shares outstanding level  (E_Dilution_Shares) | base 001-075"""
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
def _shares_outstanding_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _shares_outstanding_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _shares_outstanding_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed sharesbas times closeadj
def so_f28_shares_outstanding_raw_21d_base_v001_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed sharesbas times closeadj
def so_f28_shares_outstanding_raw_63d_base_v002_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed sharesbas times closeadj
def so_f28_shares_outstanding_raw_126d_base_v003_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed sharesbas times closeadj
def so_f28_shares_outstanding_raw_252d_base_v004_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed sharesbas times closeadj
def so_f28_shares_outstanding_raw_504d_base_v005_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(sharesbas) times closeadj
def so_f28_shares_outstanding_log_21d_base_v006_signal(sharesbas, closeadj):
    result = _mean(_shares_outstanding_log(sharesbas), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(sharesbas) times closeadj
def so_f28_shares_outstanding_log_63d_base_v007_signal(sharesbas, closeadj):
    result = _mean(_shares_outstanding_log(sharesbas), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(sharesbas) times closeadj
def so_f28_shares_outstanding_log_126d_base_v008_signal(sharesbas, closeadj):
    result = _mean(_shares_outstanding_log(sharesbas), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(sharesbas) times closeadj
def so_f28_shares_outstanding_log_252d_base_v009_signal(sharesbas, closeadj):
    result = _mean(_shares_outstanding_log(sharesbas), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(sharesbas) times closeadj
def so_f28_shares_outstanding_log_504d_base_v010_signal(sharesbas, closeadj):
    result = _mean(_shares_outstanding_log(sharesbas), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/assets mean
def so_f28_shares_outstanding_per_assets_63d_base_v011_signal(sharesbas, assets):
    result = _mean(_shares_outstanding_scaled(sharesbas, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/assets mean
def so_f28_shares_outstanding_per_assets_252d_base_v012_signal(sharesbas, assets):
    result = _mean(_shares_outstanding_scaled(sharesbas, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesbas/assets mean
def so_f28_shares_outstanding_per_assets_504d_base_v013_signal(sharesbas, assets):
    result = _mean(_shares_outstanding_scaled(sharesbas, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/marketcap mean
def so_f28_shares_outstanding_per_marketcap_63d_base_v014_signal(sharesbas, marketcap):
    result = _mean(_shares_outstanding_scaled(sharesbas, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/marketcap mean
def so_f28_shares_outstanding_per_marketcap_252d_base_v015_signal(sharesbas, marketcap):
    result = _mean(_shares_outstanding_scaled(sharesbas, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesbas/marketcap mean
def so_f28_shares_outstanding_per_marketcap_504d_base_v016_signal(sharesbas, marketcap):
    result = _mean(_shares_outstanding_scaled(sharesbas, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/equity mean
def so_f28_shares_outstanding_per_equity_63d_base_v017_signal(sharesbas, equity):
    result = _mean(_shares_outstanding_scaled(sharesbas, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/equity mean
def so_f28_shares_outstanding_per_equity_252d_base_v018_signal(sharesbas, equity):
    result = _mean(_shares_outstanding_scaled(sharesbas, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesbas/equity mean
def so_f28_shares_outstanding_per_equity_504d_base_v019_signal(sharesbas, equity):
    result = _mean(_shares_outstanding_scaled(sharesbas, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/debt mean
def so_f28_shares_outstanding_per_debt_63d_base_v020_signal(sharesbas, debt):
    result = _mean(_shares_outstanding_scaled(sharesbas, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/debt mean
def so_f28_shares_outstanding_per_debt_252d_base_v021_signal(sharesbas, debt):
    result = _mean(_shares_outstanding_scaled(sharesbas, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesbas/debt mean
def so_f28_shares_outstanding_per_debt_504d_base_v022_signal(sharesbas, debt):
    result = _mean(_shares_outstanding_scaled(sharesbas, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/revenue mean
def so_f28_shares_outstanding_per_revenue_63d_base_v023_signal(sharesbas, revenue):
    result = _mean(_shares_outstanding_scaled(sharesbas, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/revenue mean
def so_f28_shares_outstanding_per_revenue_252d_base_v024_signal(sharesbas, revenue):
    result = _mean(_shares_outstanding_scaled(sharesbas, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesbas/revenue mean
def so_f28_shares_outstanding_per_revenue_504d_base_v025_signal(sharesbas, revenue):
    result = _mean(_shares_outstanding_scaled(sharesbas, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sharesbas per share times closeadj
def so_f28_shares_outstanding_pershare_21d_base_v026_signal(sharesbas, closeadj):
    ps = _shares_outstanding_per_share(sharesbas, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas per share times closeadj
def so_f28_shares_outstanding_pershare_63d_base_v027_signal(sharesbas, closeadj):
    ps = _shares_outstanding_per_share(sharesbas, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sharesbas per share times closeadj
def so_f28_shares_outstanding_pershare_126d_base_v028_signal(sharesbas, closeadj):
    ps = _shares_outstanding_per_share(sharesbas, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas per share times closeadj
def so_f28_shares_outstanding_pershare_252d_base_v029_signal(sharesbas, closeadj):
    ps = _shares_outstanding_per_share(sharesbas, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesbas per share times closeadj
def so_f28_shares_outstanding_pershare_504d_base_v030_signal(sharesbas, closeadj):
    ps = _shares_outstanding_per_share(sharesbas, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of sharesbas times closeadj
def so_f28_shares_outstanding_std_63d_base_v031_signal(sharesbas, closeadj):
    result = _std(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of sharesbas times closeadj
def so_f28_shares_outstanding_std_252d_base_v032_signal(sharesbas, closeadj):
    result = _std(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of sharesbas times closeadj
def so_f28_shares_outstanding_std_504d_base_v033_signal(sharesbas, closeadj):
    result = _std(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of sharesbas
def so_f28_shares_outstanding_z_252d_base_v034_signal(sharesbas):
    result = _z(sharesbas, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of sharesbas
def so_f28_shares_outstanding_z_504d_base_v035_signal(sharesbas):
    result = _z(sharesbas, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(sharesbas)
def so_f28_shares_outstanding_logz_252d_base_v036_signal(sharesbas):
    result = _z(_shares_outstanding_log(sharesbas), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(sharesbas)
def so_f28_shares_outstanding_logz_504d_base_v037_signal(sharesbas):
    result = _z(_shares_outstanding_log(sharesbas), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sharesbas^2 times closeadj
def so_f28_shares_outstanding_sq_63d_base_v038_signal(sharesbas, closeadj):
    result = _mean(sharesbas * sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sharesbas^2 times closeadj
def so_f28_shares_outstanding_sq_252d_base_v039_signal(sharesbas, closeadj):
    result = _mean(sharesbas * sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(sharesbas) times closeadj
def so_f28_shares_outstanding_sign_21d_base_v040_signal(sharesbas, closeadj):
    result = _mean(np.sign(sharesbas), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(sharesbas) times closeadj
def so_f28_shares_outstanding_sign_63d_base_v041_signal(sharesbas, closeadj):
    result = _mean(np.sign(sharesbas), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(sharesbas) times closeadj
def so_f28_shares_outstanding_sign_252d_base_v042_signal(sharesbas, closeadj):
    result = _mean(np.sign(sharesbas), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/opex mean
def so_f28_shares_outstanding_per_opex_63d_base_v043_signal(sharesbas, opex):
    result = _mean(_shares_outstanding_scaled(sharesbas, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/opex mean
def so_f28_shares_outstanding_per_opex_252d_base_v044_signal(sharesbas, opex):
    result = _mean(_shares_outstanding_scaled(sharesbas, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/ebitda mean
def so_f28_shares_outstanding_per_ebitda_63d_base_v045_signal(sharesbas, ebitda):
    result = _mean(_shares_outstanding_scaled(sharesbas, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/ebitda mean
def so_f28_shares_outstanding_per_ebitda_252d_base_v046_signal(sharesbas, ebitda):
    result = _mean(_shares_outstanding_scaled(sharesbas, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/capex mean
def so_f28_shares_outstanding_per_capex_63d_base_v047_signal(sharesbas, capex):
    result = _mean(_shares_outstanding_scaled(sharesbas, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/capex mean
def so_f28_shares_outstanding_per_capex_252d_base_v048_signal(sharesbas, capex):
    result = _mean(_shares_outstanding_scaled(sharesbas, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesbas/liabilities mean
def so_f28_shares_outstanding_per_liabilities_63d_base_v049_signal(sharesbas, liabilities):
    result = _mean(_shares_outstanding_scaled(sharesbas, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesbas/liabilities mean
def so_f28_shares_outstanding_per_liabilities_252d_base_v050_signal(sharesbas, liabilities):
    result = _mean(_shares_outstanding_scaled(sharesbas, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# sharesbas relative to 252d max times closeadj
def so_f28_shares_outstanding_relmax_252d_base_v051_signal(sharesbas, closeadj):
    peak = sharesbas.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (sharesbas / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharesbas relative to 504d max times closeadj
def so_f28_shares_outstanding_relmax_504d_base_v052_signal(sharesbas, closeadj):
    peak = sharesbas.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (sharesbas / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharesbas relative to 252d min times closeadj
def so_f28_shares_outstanding_relmin_252d_base_v053_signal(sharesbas, closeadj):
    trough = sharesbas.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (sharesbas / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharesbas relative to 504d min times closeadj
def so_f28_shares_outstanding_relmin_504d_base_v054_signal(sharesbas, closeadj):
    trough = sharesbas.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (sharesbas / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of sharesbas times closeadj
def so_f28_shares_outstanding_pct_21d_base_v055_signal(sharesbas, closeadj):
    result = _pct_change(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of sharesbas times closeadj
def so_f28_shares_outstanding_pct_63d_base_v056_signal(sharesbas, closeadj):
    result = _pct_change(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of sharesbas times closeadj
def so_f28_shares_outstanding_pct_252d_base_v057_signal(sharesbas, closeadj):
    result = _pct_change(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of sharesbas times closeadj
def so_f28_shares_outstanding_sum_63d_base_v058_signal(sharesbas, closeadj):
    result = sharesbas.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of sharesbas times closeadj
def so_f28_shares_outstanding_sum_252d_base_v059_signal(sharesbas, closeadj):
    result = sharesbas.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of sharesbas times closeadj
def so_f28_shares_outstanding_sum_504d_base_v060_signal(sharesbas, closeadj):
    result = sharesbas.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesbas(63d) / smoothed assets(252d) x closeadj
def so_f28_shares_outstanding_rom_assets_252_63d_base_v061_signal(sharesbas, assets, closeadj):
    n = _mean(sharesbas, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesbas(126d) / smoothed assets(504d) x closeadj
def so_f28_shares_outstanding_rom_assets_504_126d_base_v062_signal(sharesbas, assets, closeadj):
    n = _mean(sharesbas, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesbas(63d) / smoothed marketcap(252d) x closeadj
def so_f28_shares_outstanding_rom_marketcap_252_63d_base_v063_signal(sharesbas, marketcap, closeadj):
    n = _mean(sharesbas, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesbas(126d) / smoothed marketcap(504d) x closeadj
def so_f28_shares_outstanding_rom_marketcap_504_126d_base_v064_signal(sharesbas, marketcap, closeadj):
    n = _mean(sharesbas, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesbas(63d) / smoothed equity(252d) x closeadj
def so_f28_shares_outstanding_rom_equity_252_63d_base_v065_signal(sharesbas, equity, closeadj):
    n = _mean(sharesbas, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesbas(126d) / smoothed equity(504d) x closeadj
def so_f28_shares_outstanding_rom_equity_504_126d_base_v066_signal(sharesbas, equity, closeadj):
    n = _mean(sharesbas, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sharesbas) / std(assets)
def so_f28_shares_outstanding_volratio_assets_252d_base_v067_signal(sharesbas, assets):
    n = _std(sharesbas, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sharesbas) / std(assets)
def so_f28_shares_outstanding_volratio_assets_504d_base_v068_signal(sharesbas, assets):
    n = _std(sharesbas, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sharesbas) / std(marketcap)
def so_f28_shares_outstanding_volratio_marketcap_252d_base_v069_signal(sharesbas, marketcap):
    n = _std(sharesbas, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sharesbas) / std(marketcap)
def so_f28_shares_outstanding_volratio_marketcap_504d_base_v070_signal(sharesbas, marketcap):
    n = _std(sharesbas, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed sharesbas times closeadj
def so_f28_shares_outstanding_raw_5d_base_v071_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed sharesbas times closeadj
def so_f28_shares_outstanding_raw_1008d_base_v072_signal(sharesbas, closeadj):
    result = _mean(sharesbas, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sharesbas/assets
def so_f28_shares_outstanding_log_per_assets_252d_base_v073_signal(sharesbas, assets):
    s = _shares_outstanding_scaled(sharesbas, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of sharesbas/assets
def so_f28_shares_outstanding_log_per_assets_504d_base_v074_signal(sharesbas, assets):
    s = _shares_outstanding_scaled(sharesbas, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sharesbas/marketcap
def so_f28_shares_outstanding_log_per_marketcap_252d_base_v075_signal(sharesbas, marketcap):
    s = _shares_outstanding_scaled(sharesbas, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
