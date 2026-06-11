"""Family f028 - Deferred revenue and partner funding (Capital Structure) | Sharadar tables: SF1 | fields: deferredrev, revenue, liabilities | base 001-075"""
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
def _deferred_revenue_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _deferred_revenue_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _deferred_revenue_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed deferredrev times closeadj
def dr_f028_deferred_revenue_raw_21d_base_v001_signal(deferredrev, closeadj):
    result = _mean(deferredrev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed deferredrev times closeadj
def dr_f028_deferred_revenue_raw_63d_base_v002_signal(deferredrev, closeadj):
    result = _mean(deferredrev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed deferredrev times closeadj
def dr_f028_deferred_revenue_raw_126d_base_v003_signal(deferredrev, closeadj):
    result = _mean(deferredrev, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed deferredrev times closeadj
def dr_f028_deferred_revenue_raw_252d_base_v004_signal(deferredrev, closeadj):
    result = _mean(deferredrev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed deferredrev times closeadj
def dr_f028_deferred_revenue_raw_504d_base_v005_signal(deferredrev, closeadj):
    result = _mean(deferredrev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(deferredrev) times closeadj
def dr_f028_deferred_revenue_log_21d_base_v006_signal(deferredrev, closeadj):
    result = _mean(_deferred_revenue_log(deferredrev), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(deferredrev) times closeadj
def dr_f028_deferred_revenue_log_63d_base_v007_signal(deferredrev, closeadj):
    result = _mean(_deferred_revenue_log(deferredrev), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(deferredrev) times closeadj
def dr_f028_deferred_revenue_log_126d_base_v008_signal(deferredrev, closeadj):
    result = _mean(_deferred_revenue_log(deferredrev), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(deferredrev) times closeadj
def dr_f028_deferred_revenue_log_252d_base_v009_signal(deferredrev, closeadj):
    result = _mean(_deferred_revenue_log(deferredrev), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(deferredrev) times closeadj
def dr_f028_deferred_revenue_log_504d_base_v010_signal(deferredrev, closeadj):
    result = _mean(_deferred_revenue_log(deferredrev), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deferredrev/revenue mean
def dr_f028_deferred_revenue_per_revenue_63d_base_v011_signal(deferredrev, revenue):
    result = _mean(_deferred_revenue_scaled(deferredrev, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deferredrev/revenue mean
def dr_f028_deferred_revenue_per_revenue_252d_base_v012_signal(deferredrev, revenue):
    result = _mean(_deferred_revenue_scaled(deferredrev, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d deferredrev/revenue mean
def dr_f028_deferred_revenue_per_revenue_504d_base_v013_signal(deferredrev, revenue):
    result = _mean(_deferred_revenue_scaled(deferredrev, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deferredrev/assets mean
def dr_f028_deferred_revenue_per_assets_63d_base_v014_signal(deferredrev, assets):
    result = _mean(_deferred_revenue_scaled(deferredrev, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deferredrev/assets mean
def dr_f028_deferred_revenue_per_assets_252d_base_v015_signal(deferredrev, assets):
    result = _mean(_deferred_revenue_scaled(deferredrev, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d deferredrev/assets mean
def dr_f028_deferred_revenue_per_assets_504d_base_v016_signal(deferredrev, assets):
    result = _mean(_deferred_revenue_scaled(deferredrev, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deferredrev/marketcap mean
def dr_f028_deferred_revenue_per_marketcap_63d_base_v017_signal(deferredrev, marketcap):
    result = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deferredrev/marketcap mean
def dr_f028_deferred_revenue_per_marketcap_252d_base_v018_signal(deferredrev, marketcap):
    result = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d deferredrev/marketcap mean
def dr_f028_deferred_revenue_per_marketcap_504d_base_v019_signal(deferredrev, marketcap):
    result = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deferredrev/equity mean
def dr_f028_deferred_revenue_per_equity_63d_base_v020_signal(deferredrev, equity):
    result = _mean(_deferred_revenue_scaled(deferredrev, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deferredrev/equity mean
def dr_f028_deferred_revenue_per_equity_252d_base_v021_signal(deferredrev, equity):
    result = _mean(_deferred_revenue_scaled(deferredrev, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d deferredrev/equity mean
def dr_f028_deferred_revenue_per_equity_504d_base_v022_signal(deferredrev, equity):
    result = _mean(_deferred_revenue_scaled(deferredrev, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deferredrev/debt mean
def dr_f028_deferred_revenue_per_debt_63d_base_v023_signal(deferredrev, debt):
    result = _mean(_deferred_revenue_scaled(deferredrev, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deferredrev/debt mean
def dr_f028_deferred_revenue_per_debt_252d_base_v024_signal(deferredrev, debt):
    result = _mean(_deferred_revenue_scaled(deferredrev, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d deferredrev/debt mean
def dr_f028_deferred_revenue_per_debt_504d_base_v025_signal(deferredrev, debt):
    result = _mean(_deferred_revenue_scaled(deferredrev, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d deferredrev per share times closeadj
def dr_f028_deferred_revenue_pershare_21d_base_v026_signal(deferredrev, sharesbas, closeadj):
    ps = _deferred_revenue_per_share(deferredrev, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deferredrev per share times closeadj
def dr_f028_deferred_revenue_pershare_63d_base_v027_signal(deferredrev, sharesbas, closeadj):
    ps = _deferred_revenue_per_share(deferredrev, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d deferredrev per share times closeadj
def dr_f028_deferred_revenue_pershare_126d_base_v028_signal(deferredrev, sharesbas, closeadj):
    ps = _deferred_revenue_per_share(deferredrev, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deferredrev per share times closeadj
def dr_f028_deferred_revenue_pershare_252d_base_v029_signal(deferredrev, sharesbas, closeadj):
    ps = _deferred_revenue_per_share(deferredrev, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d deferredrev per share times closeadj
def dr_f028_deferred_revenue_pershare_504d_base_v030_signal(deferredrev, sharesbas, closeadj):
    ps = _deferred_revenue_per_share(deferredrev, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of deferredrev times closeadj
def dr_f028_deferred_revenue_std_63d_base_v031_signal(deferredrev, closeadj):
    result = _std(deferredrev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of deferredrev times closeadj
def dr_f028_deferred_revenue_std_252d_base_v032_signal(deferredrev, closeadj):
    result = _std(deferredrev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of deferredrev times closeadj
def dr_f028_deferred_revenue_std_504d_base_v033_signal(deferredrev, closeadj):
    result = _std(deferredrev, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of deferredrev
def dr_f028_deferred_revenue_z_252d_base_v034_signal(deferredrev):
    result = _z(deferredrev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of deferredrev
def dr_f028_deferred_revenue_z_504d_base_v035_signal(deferredrev):
    result = _z(deferredrev, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(deferredrev)
def dr_f028_deferred_revenue_logz_252d_base_v036_signal(deferredrev):
    result = _z(_deferred_revenue_log(deferredrev), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(deferredrev)
def dr_f028_deferred_revenue_logz_504d_base_v037_signal(deferredrev):
    result = _z(_deferred_revenue_log(deferredrev), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of deferredrev^2 times closeadj
def dr_f028_deferred_revenue_sq_63d_base_v038_signal(deferredrev, closeadj):
    result = _mean(deferredrev * deferredrev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of deferredrev^2 times closeadj
def dr_f028_deferred_revenue_sq_252d_base_v039_signal(deferredrev, closeadj):
    result = _mean(deferredrev * deferredrev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(deferredrev) times closeadj
def dr_f028_deferred_revenue_sign_21d_base_v040_signal(deferredrev, closeadj):
    result = _mean(np.sign(deferredrev), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(deferredrev) times closeadj
def dr_f028_deferred_revenue_sign_63d_base_v041_signal(deferredrev, closeadj):
    result = _mean(np.sign(deferredrev), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(deferredrev) times closeadj
def dr_f028_deferred_revenue_sign_252d_base_v042_signal(deferredrev, closeadj):
    result = _mean(np.sign(deferredrev), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deferredrev/opex mean
def dr_f028_deferred_revenue_per_opex_63d_base_v043_signal(deferredrev, opex):
    result = _mean(_deferred_revenue_scaled(deferredrev, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deferredrev/opex mean
def dr_f028_deferred_revenue_per_opex_252d_base_v044_signal(deferredrev, opex):
    result = _mean(_deferred_revenue_scaled(deferredrev, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deferredrev/ebitda mean
def dr_f028_deferred_revenue_per_ebitda_63d_base_v045_signal(deferredrev, ebitda):
    result = _mean(_deferred_revenue_scaled(deferredrev, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deferredrev/ebitda mean
def dr_f028_deferred_revenue_per_ebitda_252d_base_v046_signal(deferredrev, ebitda):
    result = _mean(_deferred_revenue_scaled(deferredrev, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deferredrev/capex mean
def dr_f028_deferred_revenue_per_capex_63d_base_v047_signal(deferredrev, capex):
    result = _mean(_deferred_revenue_scaled(deferredrev, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deferredrev/capex mean
def dr_f028_deferred_revenue_per_capex_252d_base_v048_signal(deferredrev, capex):
    result = _mean(_deferred_revenue_scaled(deferredrev, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deferredrev/liabilities mean
def dr_f028_deferred_revenue_per_liabilities_63d_base_v049_signal(deferredrev, liabilities):
    result = _mean(_deferred_revenue_scaled(deferredrev, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deferredrev/liabilities mean
def dr_f028_deferred_revenue_per_liabilities_252d_base_v050_signal(deferredrev, liabilities):
    result = _mean(_deferred_revenue_scaled(deferredrev, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# deferredrev relative to 252d max times closeadj
def dr_f028_deferred_revenue_relmax_252d_base_v051_signal(deferredrev, closeadj):
    peak = deferredrev.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (deferredrev / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deferredrev relative to 504d max times closeadj
def dr_f028_deferred_revenue_relmax_504d_base_v052_signal(deferredrev, closeadj):
    peak = deferredrev.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (deferredrev / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deferredrev relative to 252d min times closeadj
def dr_f028_deferred_revenue_relmin_252d_base_v053_signal(deferredrev, closeadj):
    trough = deferredrev.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (deferredrev / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# deferredrev relative to 504d min times closeadj
def dr_f028_deferred_revenue_relmin_504d_base_v054_signal(deferredrev, closeadj):
    trough = deferredrev.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (deferredrev / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of deferredrev times closeadj
def dr_f028_deferred_revenue_pct_21d_base_v055_signal(deferredrev, closeadj):
    result = _pct_change(deferredrev, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of deferredrev times closeadj
def dr_f028_deferred_revenue_pct_63d_base_v056_signal(deferredrev, closeadj):
    result = _pct_change(deferredrev, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of deferredrev times closeadj
def dr_f028_deferred_revenue_pct_252d_base_v057_signal(deferredrev, closeadj):
    result = _pct_change(deferredrev, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of deferredrev times closeadj
def dr_f028_deferred_revenue_sum_63d_base_v058_signal(deferredrev, closeadj):
    result = deferredrev.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of deferredrev times closeadj
def dr_f028_deferred_revenue_sum_252d_base_v059_signal(deferredrev, closeadj):
    result = deferredrev.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of deferredrev times closeadj
def dr_f028_deferred_revenue_sum_504d_base_v060_signal(deferredrev, closeadj):
    result = deferredrev.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed deferredrev(63d) / smoothed revenue(252d) x closeadj
def dr_f028_deferred_revenue_rom_revenue_252_63d_base_v061_signal(deferredrev, revenue, closeadj):
    n = _mean(deferredrev, 63)
    d = _mean(revenue, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed deferredrev(126d) / smoothed revenue(504d) x closeadj
def dr_f028_deferred_revenue_rom_revenue_504_126d_base_v062_signal(deferredrev, revenue, closeadj):
    n = _mean(deferredrev, 126)
    d = _mean(revenue, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed deferredrev(63d) / smoothed assets(252d) x closeadj
def dr_f028_deferred_revenue_rom_assets_252_63d_base_v063_signal(deferredrev, assets, closeadj):
    n = _mean(deferredrev, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed deferredrev(126d) / smoothed assets(504d) x closeadj
def dr_f028_deferred_revenue_rom_assets_504_126d_base_v064_signal(deferredrev, assets, closeadj):
    n = _mean(deferredrev, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed deferredrev(63d) / smoothed marketcap(252d) x closeadj
def dr_f028_deferred_revenue_rom_marketcap_252_63d_base_v065_signal(deferredrev, marketcap, closeadj):
    n = _mean(deferredrev, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed deferredrev(126d) / smoothed marketcap(504d) x closeadj
def dr_f028_deferred_revenue_rom_marketcap_504_126d_base_v066_signal(deferredrev, marketcap, closeadj):
    n = _mean(deferredrev, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(deferredrev) / std(revenue)
def dr_f028_deferred_revenue_volratio_revenue_252d_base_v067_signal(deferredrev, revenue):
    n = _std(deferredrev, 252)
    d = _std(revenue, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(deferredrev) / std(revenue)
def dr_f028_deferred_revenue_volratio_revenue_504d_base_v068_signal(deferredrev, revenue):
    n = _std(deferredrev, 504)
    d = _std(revenue, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(deferredrev) / std(assets)
def dr_f028_deferred_revenue_volratio_assets_252d_base_v069_signal(deferredrev, assets):
    n = _std(deferredrev, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(deferredrev) / std(assets)
def dr_f028_deferred_revenue_volratio_assets_504d_base_v070_signal(deferredrev, assets):
    n = _std(deferredrev, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed deferredrev times closeadj
def dr_f028_deferred_revenue_raw_5d_base_v071_signal(deferredrev, closeadj):
    result = _mean(deferredrev, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed deferredrev times closeadj
def dr_f028_deferred_revenue_raw_1008d_base_v072_signal(deferredrev, closeadj):
    result = _mean(deferredrev, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of deferredrev/revenue
def dr_f028_deferred_revenue_log_per_revenue_252d_base_v073_signal(deferredrev, revenue):
    s = _deferred_revenue_scaled(deferredrev, revenue)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of deferredrev/revenue
def dr_f028_deferred_revenue_log_per_revenue_504d_base_v074_signal(deferredrev, revenue):
    s = _deferred_revenue_scaled(deferredrev, revenue)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of deferredrev/assets
def dr_f028_deferred_revenue_log_per_assets_252d_base_v075_signal(deferredrev, assets):
    s = _deferred_revenue_scaled(deferredrev, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
