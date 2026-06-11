"""Family f45 - Revenue per share  (G_Revenue_Growth) | base 001-075"""
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
def _revenue_per_share_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _revenue_per_share_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _revenue_per_share_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed sps times closeadj
def rvp_f45_revenue_per_share_raw_21d_base_v001_signal(sps, closeadj):
    result = _mean(sps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed sps times closeadj
def rvp_f45_revenue_per_share_raw_63d_base_v002_signal(sps, closeadj):
    result = _mean(sps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed sps times closeadj
def rvp_f45_revenue_per_share_raw_126d_base_v003_signal(sps, closeadj):
    result = _mean(sps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed sps times closeadj
def rvp_f45_revenue_per_share_raw_252d_base_v004_signal(sps, closeadj):
    result = _mean(sps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed sps times closeadj
def rvp_f45_revenue_per_share_raw_504d_base_v005_signal(sps, closeadj):
    result = _mean(sps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(sps) times closeadj
def rvp_f45_revenue_per_share_log_21d_base_v006_signal(sps, closeadj):
    result = _mean(_revenue_per_share_log(sps), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(sps) times closeadj
def rvp_f45_revenue_per_share_log_63d_base_v007_signal(sps, closeadj):
    result = _mean(_revenue_per_share_log(sps), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(sps) times closeadj
def rvp_f45_revenue_per_share_log_126d_base_v008_signal(sps, closeadj):
    result = _mean(_revenue_per_share_log(sps), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(sps) times closeadj
def rvp_f45_revenue_per_share_log_252d_base_v009_signal(sps, closeadj):
    result = _mean(_revenue_per_share_log(sps), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(sps) times closeadj
def rvp_f45_revenue_per_share_log_504d_base_v010_signal(sps, closeadj):
    result = _mean(_revenue_per_share_log(sps), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sps/assets mean
def rvp_f45_revenue_per_share_per_assets_63d_base_v011_signal(sps, assets):
    result = _mean(_revenue_per_share_scaled(sps, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sps/assets mean
def rvp_f45_revenue_per_share_per_assets_252d_base_v012_signal(sps, assets):
    result = _mean(_revenue_per_share_scaled(sps, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sps/assets mean
def rvp_f45_revenue_per_share_per_assets_504d_base_v013_signal(sps, assets):
    result = _mean(_revenue_per_share_scaled(sps, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sps/marketcap mean
def rvp_f45_revenue_per_share_per_marketcap_63d_base_v014_signal(sps, marketcap):
    result = _mean(_revenue_per_share_scaled(sps, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sps/marketcap mean
def rvp_f45_revenue_per_share_per_marketcap_252d_base_v015_signal(sps, marketcap):
    result = _mean(_revenue_per_share_scaled(sps, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sps/marketcap mean
def rvp_f45_revenue_per_share_per_marketcap_504d_base_v016_signal(sps, marketcap):
    result = _mean(_revenue_per_share_scaled(sps, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sps/equity mean
def rvp_f45_revenue_per_share_per_equity_63d_base_v017_signal(sps, equity):
    result = _mean(_revenue_per_share_scaled(sps, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sps/equity mean
def rvp_f45_revenue_per_share_per_equity_252d_base_v018_signal(sps, equity):
    result = _mean(_revenue_per_share_scaled(sps, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sps/equity mean
def rvp_f45_revenue_per_share_per_equity_504d_base_v019_signal(sps, equity):
    result = _mean(_revenue_per_share_scaled(sps, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sps/debt mean
def rvp_f45_revenue_per_share_per_debt_63d_base_v020_signal(sps, debt):
    result = _mean(_revenue_per_share_scaled(sps, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sps/debt mean
def rvp_f45_revenue_per_share_per_debt_252d_base_v021_signal(sps, debt):
    result = _mean(_revenue_per_share_scaled(sps, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sps/debt mean
def rvp_f45_revenue_per_share_per_debt_504d_base_v022_signal(sps, debt):
    result = _mean(_revenue_per_share_scaled(sps, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sps/revenue mean
def rvp_f45_revenue_per_share_per_revenue_63d_base_v023_signal(sps, revenue):
    result = _mean(_revenue_per_share_scaled(sps, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sps/revenue mean
def rvp_f45_revenue_per_share_per_revenue_252d_base_v024_signal(sps, revenue):
    result = _mean(_revenue_per_share_scaled(sps, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sps/revenue mean
def rvp_f45_revenue_per_share_per_revenue_504d_base_v025_signal(sps, revenue):
    result = _mean(_revenue_per_share_scaled(sps, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sps per share times closeadj
def rvp_f45_revenue_per_share_pershare_21d_base_v026_signal(sps, sharesbas, closeadj):
    ps = _revenue_per_share_per_share(sps, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sps per share times closeadj
def rvp_f45_revenue_per_share_pershare_63d_base_v027_signal(sps, sharesbas, closeadj):
    ps = _revenue_per_share_per_share(sps, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sps per share times closeadj
def rvp_f45_revenue_per_share_pershare_126d_base_v028_signal(sps, sharesbas, closeadj):
    ps = _revenue_per_share_per_share(sps, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sps per share times closeadj
def rvp_f45_revenue_per_share_pershare_252d_base_v029_signal(sps, sharesbas, closeadj):
    ps = _revenue_per_share_per_share(sps, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sps per share times closeadj
def rvp_f45_revenue_per_share_pershare_504d_base_v030_signal(sps, sharesbas, closeadj):
    ps = _revenue_per_share_per_share(sps, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of sps times closeadj
def rvp_f45_revenue_per_share_std_63d_base_v031_signal(sps, closeadj):
    result = _std(sps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of sps times closeadj
def rvp_f45_revenue_per_share_std_252d_base_v032_signal(sps, closeadj):
    result = _std(sps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of sps times closeadj
def rvp_f45_revenue_per_share_std_504d_base_v033_signal(sps, closeadj):
    result = _std(sps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of sps
def rvp_f45_revenue_per_share_z_252d_base_v034_signal(sps):
    result = _z(sps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of sps
def rvp_f45_revenue_per_share_z_504d_base_v035_signal(sps):
    result = _z(sps, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(sps)
def rvp_f45_revenue_per_share_logz_252d_base_v036_signal(sps):
    result = _z(_revenue_per_share_log(sps), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(sps)
def rvp_f45_revenue_per_share_logz_504d_base_v037_signal(sps):
    result = _z(_revenue_per_share_log(sps), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sps^2 times closeadj
def rvp_f45_revenue_per_share_sq_63d_base_v038_signal(sps, closeadj):
    result = _mean(sps * sps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sps^2 times closeadj
def rvp_f45_revenue_per_share_sq_252d_base_v039_signal(sps, closeadj):
    result = _mean(sps * sps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(sps) times closeadj
def rvp_f45_revenue_per_share_sign_21d_base_v040_signal(sps, closeadj):
    result = _mean(np.sign(sps), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(sps) times closeadj
def rvp_f45_revenue_per_share_sign_63d_base_v041_signal(sps, closeadj):
    result = _mean(np.sign(sps), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(sps) times closeadj
def rvp_f45_revenue_per_share_sign_252d_base_v042_signal(sps, closeadj):
    result = _mean(np.sign(sps), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sps/opex mean
def rvp_f45_revenue_per_share_per_opex_63d_base_v043_signal(sps, opex):
    result = _mean(_revenue_per_share_scaled(sps, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sps/opex mean
def rvp_f45_revenue_per_share_per_opex_252d_base_v044_signal(sps, opex):
    result = _mean(_revenue_per_share_scaled(sps, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sps/ebitda mean
def rvp_f45_revenue_per_share_per_ebitda_63d_base_v045_signal(sps, ebitda):
    result = _mean(_revenue_per_share_scaled(sps, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sps/ebitda mean
def rvp_f45_revenue_per_share_per_ebitda_252d_base_v046_signal(sps, ebitda):
    result = _mean(_revenue_per_share_scaled(sps, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sps/capex mean
def rvp_f45_revenue_per_share_per_capex_63d_base_v047_signal(sps, capex):
    result = _mean(_revenue_per_share_scaled(sps, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sps/capex mean
def rvp_f45_revenue_per_share_per_capex_252d_base_v048_signal(sps, capex):
    result = _mean(_revenue_per_share_scaled(sps, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sps/liabilities mean
def rvp_f45_revenue_per_share_per_liabilities_63d_base_v049_signal(sps, liabilities):
    result = _mean(_revenue_per_share_scaled(sps, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sps/liabilities mean
def rvp_f45_revenue_per_share_per_liabilities_252d_base_v050_signal(sps, liabilities):
    result = _mean(_revenue_per_share_scaled(sps, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# sps relative to 252d max times closeadj
def rvp_f45_revenue_per_share_relmax_252d_base_v051_signal(sps, closeadj):
    peak = sps.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (sps / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sps relative to 504d max times closeadj
def rvp_f45_revenue_per_share_relmax_504d_base_v052_signal(sps, closeadj):
    peak = sps.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (sps / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sps relative to 252d min times closeadj
def rvp_f45_revenue_per_share_relmin_252d_base_v053_signal(sps, closeadj):
    trough = sps.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (sps / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sps relative to 504d min times closeadj
def rvp_f45_revenue_per_share_relmin_504d_base_v054_signal(sps, closeadj):
    trough = sps.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (sps / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of sps times closeadj
def rvp_f45_revenue_per_share_pct_21d_base_v055_signal(sps, closeadj):
    result = _pct_change(sps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of sps times closeadj
def rvp_f45_revenue_per_share_pct_63d_base_v056_signal(sps, closeadj):
    result = _pct_change(sps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of sps times closeadj
def rvp_f45_revenue_per_share_pct_252d_base_v057_signal(sps, closeadj):
    result = _pct_change(sps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of sps times closeadj
def rvp_f45_revenue_per_share_sum_63d_base_v058_signal(sps, closeadj):
    result = sps.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of sps times closeadj
def rvp_f45_revenue_per_share_sum_252d_base_v059_signal(sps, closeadj):
    result = sps.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of sps times closeadj
def rvp_f45_revenue_per_share_sum_504d_base_v060_signal(sps, closeadj):
    result = sps.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sps(63d) / smoothed assets(252d) x closeadj
def rvp_f45_revenue_per_share_rom_assets_252_63d_base_v061_signal(sps, assets, closeadj):
    n = _mean(sps, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sps(126d) / smoothed assets(504d) x closeadj
def rvp_f45_revenue_per_share_rom_assets_504_126d_base_v062_signal(sps, assets, closeadj):
    n = _mean(sps, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sps(63d) / smoothed marketcap(252d) x closeadj
def rvp_f45_revenue_per_share_rom_marketcap_252_63d_base_v063_signal(sps, marketcap, closeadj):
    n = _mean(sps, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sps(126d) / smoothed marketcap(504d) x closeadj
def rvp_f45_revenue_per_share_rom_marketcap_504_126d_base_v064_signal(sps, marketcap, closeadj):
    n = _mean(sps, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sps(63d) / smoothed equity(252d) x closeadj
def rvp_f45_revenue_per_share_rom_equity_252_63d_base_v065_signal(sps, equity, closeadj):
    n = _mean(sps, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sps(126d) / smoothed equity(504d) x closeadj
def rvp_f45_revenue_per_share_rom_equity_504_126d_base_v066_signal(sps, equity, closeadj):
    n = _mean(sps, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sps) / std(assets)
def rvp_f45_revenue_per_share_volratio_assets_252d_base_v067_signal(sps, assets):
    n = _std(sps, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sps) / std(assets)
def rvp_f45_revenue_per_share_volratio_assets_504d_base_v068_signal(sps, assets):
    n = _std(sps, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sps) / std(marketcap)
def rvp_f45_revenue_per_share_volratio_marketcap_252d_base_v069_signal(sps, marketcap):
    n = _std(sps, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sps) / std(marketcap)
def rvp_f45_revenue_per_share_volratio_marketcap_504d_base_v070_signal(sps, marketcap):
    n = _std(sps, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed sps times closeadj
def rvp_f45_revenue_per_share_raw_5d_base_v071_signal(sps, closeadj):
    result = _mean(sps, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed sps times closeadj
def rvp_f45_revenue_per_share_raw_1008d_base_v072_signal(sps, closeadj):
    result = _mean(sps, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sps/assets
def rvp_f45_revenue_per_share_log_per_assets_252d_base_v073_signal(sps, assets):
    s = _revenue_per_share_scaled(sps, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of sps/assets
def rvp_f45_revenue_per_share_log_per_assets_504d_base_v074_signal(sps, assets):
    s = _revenue_per_share_scaled(sps, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sps/marketcap
def rvp_f45_revenue_per_share_log_per_marketcap_252d_base_v075_signal(sps, marketcap):
    s = _revenue_per_share_scaled(sps, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
