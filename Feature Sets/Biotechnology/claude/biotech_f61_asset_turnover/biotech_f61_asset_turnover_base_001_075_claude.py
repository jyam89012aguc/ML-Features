"""Family f61 - Asset turnover  (J_Returns_Efficiency) | base 001-075"""
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
def _asset_turnover_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _asset_turnover_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _asset_turnover_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed assetturnover times closeadj
def at_f61_asset_turnover_raw_21d_base_v001_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed assetturnover times closeadj
def at_f61_asset_turnover_raw_63d_base_v002_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed assetturnover times closeadj
def at_f61_asset_turnover_raw_126d_base_v003_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed assetturnover times closeadj
def at_f61_asset_turnover_raw_252d_base_v004_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed assetturnover times closeadj
def at_f61_asset_turnover_raw_504d_base_v005_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(assetturnover) times closeadj
def at_f61_asset_turnover_log_21d_base_v006_signal(assetturnover, closeadj):
    result = _mean(_asset_turnover_log(assetturnover), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(assetturnover) times closeadj
def at_f61_asset_turnover_log_63d_base_v007_signal(assetturnover, closeadj):
    result = _mean(_asset_turnover_log(assetturnover), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(assetturnover) times closeadj
def at_f61_asset_turnover_log_126d_base_v008_signal(assetturnover, closeadj):
    result = _mean(_asset_turnover_log(assetturnover), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(assetturnover) times closeadj
def at_f61_asset_turnover_log_252d_base_v009_signal(assetturnover, closeadj):
    result = _mean(_asset_turnover_log(assetturnover), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(assetturnover) times closeadj
def at_f61_asset_turnover_log_504d_base_v010_signal(assetturnover, closeadj):
    result = _mean(_asset_turnover_log(assetturnover), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetturnover/assets mean
def at_f61_asset_turnover_per_assets_63d_base_v011_signal(assetturnover, assets):
    result = _mean(_asset_turnover_scaled(assetturnover, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetturnover/assets mean
def at_f61_asset_turnover_per_assets_252d_base_v012_signal(assetturnover, assets):
    result = _mean(_asset_turnover_scaled(assetturnover, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assetturnover/assets mean
def at_f61_asset_turnover_per_assets_504d_base_v013_signal(assetturnover, assets):
    result = _mean(_asset_turnover_scaled(assetturnover, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetturnover/marketcap mean
def at_f61_asset_turnover_per_marketcap_63d_base_v014_signal(assetturnover, marketcap):
    result = _mean(_asset_turnover_scaled(assetturnover, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetturnover/marketcap mean
def at_f61_asset_turnover_per_marketcap_252d_base_v015_signal(assetturnover, marketcap):
    result = _mean(_asset_turnover_scaled(assetturnover, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assetturnover/marketcap mean
def at_f61_asset_turnover_per_marketcap_504d_base_v016_signal(assetturnover, marketcap):
    result = _mean(_asset_turnover_scaled(assetturnover, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetturnover/equity mean
def at_f61_asset_turnover_per_equity_63d_base_v017_signal(assetturnover, equity):
    result = _mean(_asset_turnover_scaled(assetturnover, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetturnover/equity mean
def at_f61_asset_turnover_per_equity_252d_base_v018_signal(assetturnover, equity):
    result = _mean(_asset_turnover_scaled(assetturnover, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assetturnover/equity mean
def at_f61_asset_turnover_per_equity_504d_base_v019_signal(assetturnover, equity):
    result = _mean(_asset_turnover_scaled(assetturnover, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetturnover/debt mean
def at_f61_asset_turnover_per_debt_63d_base_v020_signal(assetturnover, debt):
    result = _mean(_asset_turnover_scaled(assetturnover, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetturnover/debt mean
def at_f61_asset_turnover_per_debt_252d_base_v021_signal(assetturnover, debt):
    result = _mean(_asset_turnover_scaled(assetturnover, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assetturnover/debt mean
def at_f61_asset_turnover_per_debt_504d_base_v022_signal(assetturnover, debt):
    result = _mean(_asset_turnover_scaled(assetturnover, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetturnover/revenue mean
def at_f61_asset_turnover_per_revenue_63d_base_v023_signal(assetturnover, revenue):
    result = _mean(_asset_turnover_scaled(assetturnover, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetturnover/revenue mean
def at_f61_asset_turnover_per_revenue_252d_base_v024_signal(assetturnover, revenue):
    result = _mean(_asset_turnover_scaled(assetturnover, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assetturnover/revenue mean
def at_f61_asset_turnover_per_revenue_504d_base_v025_signal(assetturnover, revenue):
    result = _mean(_asset_turnover_scaled(assetturnover, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d assetturnover per share times closeadj
def at_f61_asset_turnover_pershare_21d_base_v026_signal(assetturnover, sharesbas, closeadj):
    ps = _asset_turnover_per_share(assetturnover, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetturnover per share times closeadj
def at_f61_asset_turnover_pershare_63d_base_v027_signal(assetturnover, sharesbas, closeadj):
    ps = _asset_turnover_per_share(assetturnover, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d assetturnover per share times closeadj
def at_f61_asset_turnover_pershare_126d_base_v028_signal(assetturnover, sharesbas, closeadj):
    ps = _asset_turnover_per_share(assetturnover, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetturnover per share times closeadj
def at_f61_asset_turnover_pershare_252d_base_v029_signal(assetturnover, sharesbas, closeadj):
    ps = _asset_turnover_per_share(assetturnover, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d assetturnover per share times closeadj
def at_f61_asset_turnover_pershare_504d_base_v030_signal(assetturnover, sharesbas, closeadj):
    ps = _asset_turnover_per_share(assetturnover, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of assetturnover times closeadj
def at_f61_asset_turnover_std_63d_base_v031_signal(assetturnover, closeadj):
    result = _std(assetturnover, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of assetturnover times closeadj
def at_f61_asset_turnover_std_252d_base_v032_signal(assetturnover, closeadj):
    result = _std(assetturnover, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of assetturnover times closeadj
def at_f61_asset_turnover_std_504d_base_v033_signal(assetturnover, closeadj):
    result = _std(assetturnover, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of assetturnover
def at_f61_asset_turnover_z_252d_base_v034_signal(assetturnover):
    result = _z(assetturnover, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of assetturnover
def at_f61_asset_turnover_z_504d_base_v035_signal(assetturnover):
    result = _z(assetturnover, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(assetturnover)
def at_f61_asset_turnover_logz_252d_base_v036_signal(assetturnover):
    result = _z(_asset_turnover_log(assetturnover), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(assetturnover)
def at_f61_asset_turnover_logz_504d_base_v037_signal(assetturnover):
    result = _z(_asset_turnover_log(assetturnover), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of assetturnover^2 times closeadj
def at_f61_asset_turnover_sq_63d_base_v038_signal(assetturnover, closeadj):
    result = _mean(assetturnover * assetturnover, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of assetturnover^2 times closeadj
def at_f61_asset_turnover_sq_252d_base_v039_signal(assetturnover, closeadj):
    result = _mean(assetturnover * assetturnover, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(assetturnover) times closeadj
def at_f61_asset_turnover_sign_21d_base_v040_signal(assetturnover, closeadj):
    result = _mean(np.sign(assetturnover), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(assetturnover) times closeadj
def at_f61_asset_turnover_sign_63d_base_v041_signal(assetturnover, closeadj):
    result = _mean(np.sign(assetturnover), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(assetturnover) times closeadj
def at_f61_asset_turnover_sign_252d_base_v042_signal(assetturnover, closeadj):
    result = _mean(np.sign(assetturnover), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetturnover/opex mean
def at_f61_asset_turnover_per_opex_63d_base_v043_signal(assetturnover, opex):
    result = _mean(_asset_turnover_scaled(assetturnover, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetturnover/opex mean
def at_f61_asset_turnover_per_opex_252d_base_v044_signal(assetturnover, opex):
    result = _mean(_asset_turnover_scaled(assetturnover, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetturnover/ebitda mean
def at_f61_asset_turnover_per_ebitda_63d_base_v045_signal(assetturnover, ebitda):
    result = _mean(_asset_turnover_scaled(assetturnover, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetturnover/ebitda mean
def at_f61_asset_turnover_per_ebitda_252d_base_v046_signal(assetturnover, ebitda):
    result = _mean(_asset_turnover_scaled(assetturnover, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetturnover/capex mean
def at_f61_asset_turnover_per_capex_63d_base_v047_signal(assetturnover, capex):
    result = _mean(_asset_turnover_scaled(assetturnover, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetturnover/capex mean
def at_f61_asset_turnover_per_capex_252d_base_v048_signal(assetturnover, capex):
    result = _mean(_asset_turnover_scaled(assetturnover, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d assetturnover/liabilities mean
def at_f61_asset_turnover_per_liabilities_63d_base_v049_signal(assetturnover, liabilities):
    result = _mean(_asset_turnover_scaled(assetturnover, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d assetturnover/liabilities mean
def at_f61_asset_turnover_per_liabilities_252d_base_v050_signal(assetturnover, liabilities):
    result = _mean(_asset_turnover_scaled(assetturnover, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# assetturnover relative to 252d max times closeadj
def at_f61_asset_turnover_relmax_252d_base_v051_signal(assetturnover, closeadj):
    peak = assetturnover.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (assetturnover / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assetturnover relative to 504d max times closeadj
def at_f61_asset_turnover_relmax_504d_base_v052_signal(assetturnover, closeadj):
    peak = assetturnover.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (assetturnover / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assetturnover relative to 252d min times closeadj
def at_f61_asset_turnover_relmin_252d_base_v053_signal(assetturnover, closeadj):
    trough = assetturnover.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (assetturnover / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# assetturnover relative to 504d min times closeadj
def at_f61_asset_turnover_relmin_504d_base_v054_signal(assetturnover, closeadj):
    trough = assetturnover.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (assetturnover / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of assetturnover times closeadj
def at_f61_asset_turnover_pct_21d_base_v055_signal(assetturnover, closeadj):
    result = _pct_change(assetturnover, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of assetturnover times closeadj
def at_f61_asset_turnover_pct_63d_base_v056_signal(assetturnover, closeadj):
    result = _pct_change(assetturnover, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of assetturnover times closeadj
def at_f61_asset_turnover_pct_252d_base_v057_signal(assetturnover, closeadj):
    result = _pct_change(assetturnover, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of assetturnover times closeadj
def at_f61_asset_turnover_sum_63d_base_v058_signal(assetturnover, closeadj):
    result = assetturnover.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of assetturnover times closeadj
def at_f61_asset_turnover_sum_252d_base_v059_signal(assetturnover, closeadj):
    result = assetturnover.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of assetturnover times closeadj
def at_f61_asset_turnover_sum_504d_base_v060_signal(assetturnover, closeadj):
    result = assetturnover.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assetturnover(63d) / smoothed assets(252d) x closeadj
def at_f61_asset_turnover_rom_assets_252_63d_base_v061_signal(assetturnover, assets, closeadj):
    n = _mean(assetturnover, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assetturnover(126d) / smoothed assets(504d) x closeadj
def at_f61_asset_turnover_rom_assets_504_126d_base_v062_signal(assetturnover, assets, closeadj):
    n = _mean(assetturnover, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assetturnover(63d) / smoothed marketcap(252d) x closeadj
def at_f61_asset_turnover_rom_marketcap_252_63d_base_v063_signal(assetturnover, marketcap, closeadj):
    n = _mean(assetturnover, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assetturnover(126d) / smoothed marketcap(504d) x closeadj
def at_f61_asset_turnover_rom_marketcap_504_126d_base_v064_signal(assetturnover, marketcap, closeadj):
    n = _mean(assetturnover, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assetturnover(63d) / smoothed equity(252d) x closeadj
def at_f61_asset_turnover_rom_equity_252_63d_base_v065_signal(assetturnover, equity, closeadj):
    n = _mean(assetturnover, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed assetturnover(126d) / smoothed equity(504d) x closeadj
def at_f61_asset_turnover_rom_equity_504_126d_base_v066_signal(assetturnover, equity, closeadj):
    n = _mean(assetturnover, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(assetturnover) / std(assets)
def at_f61_asset_turnover_volratio_assets_252d_base_v067_signal(assetturnover, assets):
    n = _std(assetturnover, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(assetturnover) / std(assets)
def at_f61_asset_turnover_volratio_assets_504d_base_v068_signal(assetturnover, assets):
    n = _std(assetturnover, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(assetturnover) / std(marketcap)
def at_f61_asset_turnover_volratio_marketcap_252d_base_v069_signal(assetturnover, marketcap):
    n = _std(assetturnover, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(assetturnover) / std(marketcap)
def at_f61_asset_turnover_volratio_marketcap_504d_base_v070_signal(assetturnover, marketcap):
    n = _std(assetturnover, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed assetturnover times closeadj
def at_f61_asset_turnover_raw_5d_base_v071_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed assetturnover times closeadj
def at_f61_asset_turnover_raw_1008d_base_v072_signal(assetturnover, closeadj):
    result = _mean(assetturnover, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of assetturnover/assets
def at_f61_asset_turnover_log_per_assets_252d_base_v073_signal(assetturnover, assets):
    s = _asset_turnover_scaled(assetturnover, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of assetturnover/assets
def at_f61_asset_turnover_log_per_assets_504d_base_v074_signal(assetturnover, assets):
    s = _asset_turnover_scaled(assetturnover, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of assetturnover/marketcap
def at_f61_asset_turnover_log_per_marketcap_252d_base_v075_signal(assetturnover, marketcap):
    s = _asset_turnover_scaled(assetturnover, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
