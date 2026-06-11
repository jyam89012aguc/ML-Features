"""Family f35 - Total assets level & growth  (F_BalanceSheet) | base 001-075"""
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
def _total_assets_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _total_assets_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _total_assets_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed assets times closeadj
def ta_f35_total_assets_raw_21d_base_v001_signal(assets, closeadj):
    result = _mean(assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed assets times closeadj
def ta_f35_total_assets_raw_63d_base_v002_signal(assets, closeadj):
    result = _mean(assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed assets times closeadj
def ta_f35_total_assets_raw_126d_base_v003_signal(assets, closeadj):
    result = _mean(assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed assets times closeadj
def ta_f35_total_assets_raw_252d_base_v004_signal(assets, closeadj):
    result = _mean(assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed assets times closeadj
def ta_f35_total_assets_raw_504d_base_v005_signal(assets, closeadj):
    result = _mean(assets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(assets) times closeadj
def ta_f35_total_assets_log_21d_base_v006_signal(assets, closeadj):
    result = _mean(_total_assets_log(assets), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(assets) times closeadj
def ta_f35_total_assets_log_63d_base_v007_signal(assets, closeadj):
    result = _mean(_total_assets_log(assets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(assets) times closeadj
def ta_f35_total_assets_log_126d_base_v008_signal(assets, closeadj):
    result = _mean(_total_assets_log(assets), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(assets) times closeadj
def ta_f35_total_assets_log_252d_base_v009_signal(assets, closeadj):
    result = _mean(_total_assets_log(assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(assets) times closeadj
def ta_f35_total_assets_log_504d_base_v010_signal(assets, closeadj):
    result = _mean(_total_assets_log(assets), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assets/assets mean
def ta_f35_total_assets_per_assets_63d_base_v011_signal(assets):
    result = _mean(_total_assets_scaled(assets, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assets/assets mean
def ta_f35_total_assets_per_assets_252d_base_v012_signal(assets):
    result = _mean(_total_assets_scaled(assets, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assets/assets mean
def ta_f35_total_assets_per_assets_504d_base_v013_signal(assets):
    result = _mean(_total_assets_scaled(assets, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assets/marketcap mean
def ta_f35_total_assets_per_marketcap_63d_base_v014_signal(assets, marketcap):
    result = _mean(_total_assets_scaled(assets, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assets/marketcap mean
def ta_f35_total_assets_per_marketcap_252d_base_v015_signal(assets, marketcap):
    result = _mean(_total_assets_scaled(assets, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assets/marketcap mean
def ta_f35_total_assets_per_marketcap_504d_base_v016_signal(assets, marketcap):
    result = _mean(_total_assets_scaled(assets, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assets/equity mean
def ta_f35_total_assets_per_equity_63d_base_v017_signal(assets, equity):
    result = _mean(_total_assets_scaled(assets, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assets/equity mean
def ta_f35_total_assets_per_equity_252d_base_v018_signal(assets, equity):
    result = _mean(_total_assets_scaled(assets, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assets/equity mean
def ta_f35_total_assets_per_equity_504d_base_v019_signal(assets, equity):
    result = _mean(_total_assets_scaled(assets, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assets/debt mean
def ta_f35_total_assets_per_debt_63d_base_v020_signal(assets, debt):
    result = _mean(_total_assets_scaled(assets, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assets/debt mean
def ta_f35_total_assets_per_debt_252d_base_v021_signal(assets, debt):
    result = _mean(_total_assets_scaled(assets, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assets/debt mean
def ta_f35_total_assets_per_debt_504d_base_v022_signal(assets, debt):
    result = _mean(_total_assets_scaled(assets, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assets/revenue mean
def ta_f35_total_assets_per_revenue_63d_base_v023_signal(assets, revenue):
    result = _mean(_total_assets_scaled(assets, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assets/revenue mean
def ta_f35_total_assets_per_revenue_252d_base_v024_signal(assets, revenue):
    result = _mean(_total_assets_scaled(assets, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assets/revenue mean
def ta_f35_total_assets_per_revenue_504d_base_v025_signal(assets, revenue):
    result = _mean(_total_assets_scaled(assets, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d assets per share times closeadj
def ta_f35_total_assets_pershare_21d_base_v026_signal(assets, sharesbas, closeadj):
    ps = _total_assets_per_share(assets, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assets per share times closeadj
def ta_f35_total_assets_pershare_63d_base_v027_signal(assets, sharesbas, closeadj):
    ps = _total_assets_per_share(assets, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d assets per share times closeadj
def ta_f35_total_assets_pershare_126d_base_v028_signal(assets, sharesbas, closeadj):
    ps = _total_assets_per_share(assets, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assets per share times closeadj
def ta_f35_total_assets_pershare_252d_base_v029_signal(assets, sharesbas, closeadj):
    ps = _total_assets_per_share(assets, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assets per share times closeadj
def ta_f35_total_assets_pershare_504d_base_v030_signal(assets, sharesbas, closeadj):
    ps = _total_assets_per_share(assets, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of assets times closeadj
def ta_f35_total_assets_std_63d_base_v031_signal(assets, closeadj):
    result = _std(assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of assets times closeadj
def ta_f35_total_assets_std_252d_base_v032_signal(assets, closeadj):
    result = _std(assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of assets times closeadj
def ta_f35_total_assets_std_504d_base_v033_signal(assets, closeadj):
    result = _std(assets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of assets
def ta_f35_total_assets_z_252d_base_v034_signal(assets):
    result = _z(assets, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of assets
def ta_f35_total_assets_z_504d_base_v035_signal(assets):
    result = _z(assets, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(assets)
def ta_f35_total_assets_logz_252d_base_v036_signal(assets):
    result = _z(_total_assets_log(assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(assets)
def ta_f35_total_assets_logz_504d_base_v037_signal(assets):
    result = _z(_total_assets_log(assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of assets^2 times closeadj
def ta_f35_total_assets_sq_63d_base_v038_signal(assets, closeadj):
    result = _mean(assets * assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of assets^2 times closeadj
def ta_f35_total_assets_sq_252d_base_v039_signal(assets, closeadj):
    result = _mean(assets * assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(assets) times closeadj
def ta_f35_total_assets_sign_21d_base_v040_signal(assets, closeadj):
    result = _mean(np.sign(assets), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(assets) times closeadj
def ta_f35_total_assets_sign_63d_base_v041_signal(assets, closeadj):
    result = _mean(np.sign(assets), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(assets) times closeadj
def ta_f35_total_assets_sign_252d_base_v042_signal(assets, closeadj):
    result = _mean(np.sign(assets), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assets/opex mean
def ta_f35_total_assets_per_opex_63d_base_v043_signal(assets, opex):
    result = _mean(_total_assets_scaled(assets, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assets/opex mean
def ta_f35_total_assets_per_opex_252d_base_v044_signal(assets, opex):
    result = _mean(_total_assets_scaled(assets, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assets/ebitda mean
def ta_f35_total_assets_per_ebitda_63d_base_v045_signal(assets, ebitda):
    result = _mean(_total_assets_scaled(assets, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assets/ebitda mean
def ta_f35_total_assets_per_ebitda_252d_base_v046_signal(assets, ebitda):
    result = _mean(_total_assets_scaled(assets, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assets/capex mean
def ta_f35_total_assets_per_capex_63d_base_v047_signal(assets, capex):
    result = _mean(_total_assets_scaled(assets, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assets/capex mean
def ta_f35_total_assets_per_capex_252d_base_v048_signal(assets, capex):
    result = _mean(_total_assets_scaled(assets, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assets/liabilities mean
def ta_f35_total_assets_per_liabilities_63d_base_v049_signal(assets, liabilities):
    result = _mean(_total_assets_scaled(assets, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assets/liabilities mean
def ta_f35_total_assets_per_liabilities_252d_base_v050_signal(assets, liabilities):
    result = _mean(_total_assets_scaled(assets, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# assets relative to 252d max times closeadj
def ta_f35_total_assets_relmax_252d_base_v051_signal(assets, closeadj):
    peak = assets.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (assets / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assets relative to 504d max times closeadj
def ta_f35_total_assets_relmax_504d_base_v052_signal(assets, closeadj):
    peak = assets.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (assets / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assets relative to 252d min times closeadj
def ta_f35_total_assets_relmin_252d_base_v053_signal(assets, closeadj):
    trough = assets.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (assets / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assets relative to 504d min times closeadj
def ta_f35_total_assets_relmin_504d_base_v054_signal(assets, closeadj):
    trough = assets.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (assets / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of assets times closeadj
def ta_f35_total_assets_pct_21d_base_v055_signal(assets, closeadj):
    result = _pct_change(assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of assets times closeadj
def ta_f35_total_assets_pct_63d_base_v056_signal(assets, closeadj):
    result = _pct_change(assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of assets times closeadj
def ta_f35_total_assets_pct_252d_base_v057_signal(assets, closeadj):
    result = _pct_change(assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of assets times closeadj
def ta_f35_total_assets_sum_63d_base_v058_signal(assets, closeadj):
    result = assets.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of assets times closeadj
def ta_f35_total_assets_sum_252d_base_v059_signal(assets, closeadj):
    result = assets.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of assets times closeadj
def ta_f35_total_assets_sum_504d_base_v060_signal(assets, closeadj):
    result = assets.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assets(63d) / smoothed assets(252d) x closeadj
def ta_f35_total_assets_rom_assets_252_63d_base_v061_signal(assets, closeadj):
    n = _mean(assets, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assets(126d) / smoothed assets(504d) x closeadj
def ta_f35_total_assets_rom_assets_504_126d_base_v062_signal(assets, closeadj):
    n = _mean(assets, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assets(63d) / smoothed marketcap(252d) x closeadj
def ta_f35_total_assets_rom_marketcap_252_63d_base_v063_signal(assets, marketcap, closeadj):
    n = _mean(assets, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assets(126d) / smoothed marketcap(504d) x closeadj
def ta_f35_total_assets_rom_marketcap_504_126d_base_v064_signal(assets, marketcap, closeadj):
    n = _mean(assets, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assets(63d) / smoothed equity(252d) x closeadj
def ta_f35_total_assets_rom_equity_252_63d_base_v065_signal(assets, equity, closeadj):
    n = _mean(assets, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assets(126d) / smoothed equity(504d) x closeadj
def ta_f35_total_assets_rom_equity_504_126d_base_v066_signal(assets, equity, closeadj):
    n = _mean(assets, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(assets) / std(assets)
def ta_f35_total_assets_volratio_assets_252d_base_v067_signal(assets):
    n = _std(assets, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(assets) / std(assets)
def ta_f35_total_assets_volratio_assets_504d_base_v068_signal(assets):
    n = _std(assets, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(assets) / std(marketcap)
def ta_f35_total_assets_volratio_marketcap_252d_base_v069_signal(assets, marketcap):
    n = _std(assets, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(assets) / std(marketcap)
def ta_f35_total_assets_volratio_marketcap_504d_base_v070_signal(assets, marketcap):
    n = _std(assets, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed assets times closeadj
def ta_f35_total_assets_raw_5d_base_v071_signal(assets, closeadj):
    result = _mean(assets, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed assets times closeadj
def ta_f35_total_assets_raw_1008d_base_v072_signal(assets, closeadj):
    result = _mean(assets, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of assets/assets
def ta_f35_total_assets_log_per_assets_252d_base_v073_signal(assets):
    s = _total_assets_scaled(assets, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of assets/assets
def ta_f35_total_assets_log_per_assets_504d_base_v074_signal(assets):
    s = _total_assets_scaled(assets, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of assets/marketcap
def ta_f35_total_assets_log_per_marketcap_252d_base_v075_signal(assets, marketcap):
    s = _total_assets_scaled(assets, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
