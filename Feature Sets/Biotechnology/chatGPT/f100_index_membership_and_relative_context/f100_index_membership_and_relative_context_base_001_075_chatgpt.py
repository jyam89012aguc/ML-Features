"""Family f100 - Index membership and cross-sectional context (Corporate Actions and Events) | Sharadar tables: SP500,TICKERS,SF1,DAILY | fields: date, action, ticker, sector, industry, marketcap | base 001-075"""
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
def _index_membership_and_relative_context_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _index_membership_and_relative_context_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _index_membership_and_relative_context_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed marketcap times closeadj
def imar_f100_index_membership_and_relative_context_raw_21d_base_v001_signal(marketcap, closeadj):
    result = _mean(marketcap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed marketcap times closeadj
def imar_f100_index_membership_and_relative_context_raw_63d_base_v002_signal(marketcap, closeadj):
    result = _mean(marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed marketcap times closeadj
def imar_f100_index_membership_and_relative_context_raw_126d_base_v003_signal(marketcap, closeadj):
    result = _mean(marketcap, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed marketcap times closeadj
def imar_f100_index_membership_and_relative_context_raw_252d_base_v004_signal(marketcap, closeadj):
    result = _mean(marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed marketcap times closeadj
def imar_f100_index_membership_and_relative_context_raw_504d_base_v005_signal(marketcap, closeadj):
    result = _mean(marketcap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(marketcap) times closeadj
def imar_f100_index_membership_and_relative_context_log_21d_base_v006_signal(marketcap, closeadj):
    result = _mean(_index_membership_and_relative_context_log(marketcap), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(marketcap) times closeadj
def imar_f100_index_membership_and_relative_context_log_63d_base_v007_signal(marketcap, closeadj):
    result = _mean(_index_membership_and_relative_context_log(marketcap), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(marketcap) times closeadj
def imar_f100_index_membership_and_relative_context_log_126d_base_v008_signal(marketcap, closeadj):
    result = _mean(_index_membership_and_relative_context_log(marketcap), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(marketcap) times closeadj
def imar_f100_index_membership_and_relative_context_log_252d_base_v009_signal(marketcap, closeadj):
    result = _mean(_index_membership_and_relative_context_log(marketcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(marketcap) times closeadj
def imar_f100_index_membership_and_relative_context_log_504d_base_v010_signal(marketcap, closeadj):
    result = _mean(_index_membership_and_relative_context_log(marketcap), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/assets mean
def imar_f100_index_membership_and_relative_context_per_assets_63d_base_v011_signal(marketcap, assets):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/assets mean
def imar_f100_index_membership_and_relative_context_per_assets_252d_base_v012_signal(marketcap, assets):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap/assets mean
def imar_f100_index_membership_and_relative_context_per_assets_504d_base_v013_signal(marketcap, assets):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/equity mean
def imar_f100_index_membership_and_relative_context_per_equity_63d_base_v014_signal(marketcap, equity):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/equity mean
def imar_f100_index_membership_and_relative_context_per_equity_252d_base_v015_signal(marketcap, equity):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap/equity mean
def imar_f100_index_membership_and_relative_context_per_equity_504d_base_v016_signal(marketcap, equity):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/debt mean
def imar_f100_index_membership_and_relative_context_per_debt_63d_base_v017_signal(marketcap, debt):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/debt mean
def imar_f100_index_membership_and_relative_context_per_debt_252d_base_v018_signal(marketcap, debt):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap/debt mean
def imar_f100_index_membership_and_relative_context_per_debt_504d_base_v019_signal(marketcap, debt):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/revenue mean
def imar_f100_index_membership_and_relative_context_per_revenue_63d_base_v020_signal(marketcap, revenue):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/revenue mean
def imar_f100_index_membership_and_relative_context_per_revenue_252d_base_v021_signal(marketcap, revenue):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap/revenue mean
def imar_f100_index_membership_and_relative_context_per_revenue_504d_base_v022_signal(marketcap, revenue):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/cashneq mean
def imar_f100_index_membership_and_relative_context_per_cashneq_63d_base_v023_signal(marketcap, cashneq):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, cashneq), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/cashneq mean
def imar_f100_index_membership_and_relative_context_per_cashneq_252d_base_v024_signal(marketcap, cashneq):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, cashneq), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap/cashneq mean
def imar_f100_index_membership_and_relative_context_per_cashneq_504d_base_v025_signal(marketcap, cashneq):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, cashneq), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap per share times closeadj
def imar_f100_index_membership_and_relative_context_pershare_21d_base_v026_signal(marketcap, sharesbas, closeadj):
    ps = _index_membership_and_relative_context_per_share(marketcap, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap per share times closeadj
def imar_f100_index_membership_and_relative_context_pershare_63d_base_v027_signal(marketcap, sharesbas, closeadj):
    ps = _index_membership_and_relative_context_per_share(marketcap, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d marketcap per share times closeadj
def imar_f100_index_membership_and_relative_context_pershare_126d_base_v028_signal(marketcap, sharesbas, closeadj):
    ps = _index_membership_and_relative_context_per_share(marketcap, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap per share times closeadj
def imar_f100_index_membership_and_relative_context_pershare_252d_base_v029_signal(marketcap, sharesbas, closeadj):
    ps = _index_membership_and_relative_context_per_share(marketcap, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap per share times closeadj
def imar_f100_index_membership_and_relative_context_pershare_504d_base_v030_signal(marketcap, sharesbas, closeadj):
    ps = _index_membership_and_relative_context_per_share(marketcap, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of marketcap times closeadj
def imar_f100_index_membership_and_relative_context_std_63d_base_v031_signal(marketcap, closeadj):
    result = _std(marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of marketcap times closeadj
def imar_f100_index_membership_and_relative_context_std_252d_base_v032_signal(marketcap, closeadj):
    result = _std(marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of marketcap times closeadj
def imar_f100_index_membership_and_relative_context_std_504d_base_v033_signal(marketcap, closeadj):
    result = _std(marketcap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of marketcap
def imar_f100_index_membership_and_relative_context_z_252d_base_v034_signal(marketcap):
    result = _z(marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of marketcap
def imar_f100_index_membership_and_relative_context_z_504d_base_v035_signal(marketcap):
    result = _z(marketcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(marketcap)
def imar_f100_index_membership_and_relative_context_logz_252d_base_v036_signal(marketcap):
    result = _z(_index_membership_and_relative_context_log(marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(marketcap)
def imar_f100_index_membership_and_relative_context_logz_504d_base_v037_signal(marketcap):
    result = _z(_index_membership_and_relative_context_log(marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of marketcap^2 times closeadj
def imar_f100_index_membership_and_relative_context_sq_63d_base_v038_signal(marketcap, closeadj):
    result = _mean(marketcap * marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of marketcap^2 times closeadj
def imar_f100_index_membership_and_relative_context_sq_252d_base_v039_signal(marketcap, closeadj):
    result = _mean(marketcap * marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(marketcap) times closeadj
def imar_f100_index_membership_and_relative_context_sign_21d_base_v040_signal(marketcap, closeadj):
    result = _mean(np.sign(marketcap), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(marketcap) times closeadj
def imar_f100_index_membership_and_relative_context_sign_63d_base_v041_signal(marketcap, closeadj):
    result = _mean(np.sign(marketcap), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(marketcap) times closeadj
def imar_f100_index_membership_and_relative_context_sign_252d_base_v042_signal(marketcap, closeadj):
    result = _mean(np.sign(marketcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/opex mean
def imar_f100_index_membership_and_relative_context_per_opex_63d_base_v043_signal(marketcap, opex):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/opex mean
def imar_f100_index_membership_and_relative_context_per_opex_252d_base_v044_signal(marketcap, opex):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/ebitda mean
def imar_f100_index_membership_and_relative_context_per_ebitda_63d_base_v045_signal(marketcap, ebitda):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/ebitda mean
def imar_f100_index_membership_and_relative_context_per_ebitda_252d_base_v046_signal(marketcap, ebitda):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/capex mean
def imar_f100_index_membership_and_relative_context_per_capex_63d_base_v047_signal(marketcap, capex):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/capex mean
def imar_f100_index_membership_and_relative_context_per_capex_252d_base_v048_signal(marketcap, capex):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap/liabilities mean
def imar_f100_index_membership_and_relative_context_per_liabilities_63d_base_v049_signal(marketcap, liabilities):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap/liabilities mean
def imar_f100_index_membership_and_relative_context_per_liabilities_252d_base_v050_signal(marketcap, liabilities):
    result = _mean(_index_membership_and_relative_context_scaled(marketcap, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap relative to 252d max times closeadj
def imar_f100_index_membership_and_relative_context_relmax_252d_base_v051_signal(marketcap, closeadj):
    peak = marketcap.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (marketcap / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap relative to 504d max times closeadj
def imar_f100_index_membership_and_relative_context_relmax_504d_base_v052_signal(marketcap, closeadj):
    peak = marketcap.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (marketcap / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap relative to 252d min times closeadj
def imar_f100_index_membership_and_relative_context_relmin_252d_base_v053_signal(marketcap, closeadj):
    trough = marketcap.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (marketcap / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap relative to 504d min times closeadj
def imar_f100_index_membership_and_relative_context_relmin_504d_base_v054_signal(marketcap, closeadj):
    trough = marketcap.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (marketcap / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of marketcap times closeadj
def imar_f100_index_membership_and_relative_context_pct_21d_base_v055_signal(marketcap, closeadj):
    result = _pct_change(marketcap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of marketcap times closeadj
def imar_f100_index_membership_and_relative_context_pct_63d_base_v056_signal(marketcap, closeadj):
    result = _pct_change(marketcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of marketcap times closeadj
def imar_f100_index_membership_and_relative_context_pct_252d_base_v057_signal(marketcap, closeadj):
    result = _pct_change(marketcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of marketcap times closeadj
def imar_f100_index_membership_and_relative_context_sum_63d_base_v058_signal(marketcap, closeadj):
    result = marketcap.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of marketcap times closeadj
def imar_f100_index_membership_and_relative_context_sum_252d_base_v059_signal(marketcap, closeadj):
    result = marketcap.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of marketcap times closeadj
def imar_f100_index_membership_and_relative_context_sum_504d_base_v060_signal(marketcap, closeadj):
    result = marketcap.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(63d) / smoothed assets(252d) x closeadj
def imar_f100_index_membership_and_relative_context_rom_assets_252_63d_base_v061_signal(marketcap, assets, closeadj):
    n = _mean(marketcap, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(126d) / smoothed assets(504d) x closeadj
def imar_f100_index_membership_and_relative_context_rom_assets_504_126d_base_v062_signal(marketcap, assets, closeadj):
    n = _mean(marketcap, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(63d) / smoothed equity(252d) x closeadj
def imar_f100_index_membership_and_relative_context_rom_equity_252_63d_base_v063_signal(marketcap, equity, closeadj):
    n = _mean(marketcap, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(126d) / smoothed equity(504d) x closeadj
def imar_f100_index_membership_and_relative_context_rom_equity_504_126d_base_v064_signal(marketcap, equity, closeadj):
    n = _mean(marketcap, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(63d) / smoothed debt(252d) x closeadj
def imar_f100_index_membership_and_relative_context_rom_debt_252_63d_base_v065_signal(marketcap, debt, closeadj):
    n = _mean(marketcap, 63)
    d = _mean(debt, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed marketcap(126d) / smoothed debt(504d) x closeadj
def imar_f100_index_membership_and_relative_context_rom_debt_504_126d_base_v066_signal(marketcap, debt, closeadj):
    n = _mean(marketcap, 126)
    d = _mean(debt, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(marketcap) / std(assets)
def imar_f100_index_membership_and_relative_context_volratio_assets_252d_base_v067_signal(marketcap, assets):
    n = _std(marketcap, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(marketcap) / std(assets)
def imar_f100_index_membership_and_relative_context_volratio_assets_504d_base_v068_signal(marketcap, assets):
    n = _std(marketcap, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(marketcap) / std(equity)
def imar_f100_index_membership_and_relative_context_volratio_equity_252d_base_v069_signal(marketcap, equity):
    n = _std(marketcap, 252)
    d = _std(equity, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(marketcap) / std(equity)
def imar_f100_index_membership_and_relative_context_volratio_equity_504d_base_v070_signal(marketcap, equity):
    n = _std(marketcap, 504)
    d = _std(equity, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed marketcap times closeadj
def imar_f100_index_membership_and_relative_context_raw_5d_base_v071_signal(marketcap, closeadj):
    result = _mean(marketcap, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed marketcap times closeadj
def imar_f100_index_membership_and_relative_context_raw_1008d_base_v072_signal(marketcap, closeadj):
    result = _mean(marketcap, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of marketcap/assets
def imar_f100_index_membership_and_relative_context_log_per_assets_252d_base_v073_signal(marketcap, assets):
    s = _index_membership_and_relative_context_scaled(marketcap, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of marketcap/assets
def imar_f100_index_membership_and_relative_context_log_per_assets_504d_base_v074_signal(marketcap, assets):
    s = _index_membership_and_relative_context_scaled(marketcap, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of marketcap/equity
def imar_f100_index_membership_and_relative_context_log_per_equity_252d_base_v075_signal(marketcap, equity):
    s = _index_membership_and_relative_context_scaled(marketcap, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
