"""Family f62 - Invested capital  (J_Returns_Efficiency) | base 001-075"""
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
def _invested_capital_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _invested_capital_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _invested_capital_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed invcap times closeadj
def ivc_f62_invested_capital_raw_21d_base_v001_signal(invcap, closeadj):
    result = _mean(invcap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed invcap times closeadj
def ivc_f62_invested_capital_raw_63d_base_v002_signal(invcap, closeadj):
    result = _mean(invcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed invcap times closeadj
def ivc_f62_invested_capital_raw_126d_base_v003_signal(invcap, closeadj):
    result = _mean(invcap, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed invcap times closeadj
def ivc_f62_invested_capital_raw_252d_base_v004_signal(invcap, closeadj):
    result = _mean(invcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed invcap times closeadj
def ivc_f62_invested_capital_raw_504d_base_v005_signal(invcap, closeadj):
    result = _mean(invcap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(invcap) times closeadj
def ivc_f62_invested_capital_log_21d_base_v006_signal(invcap, closeadj):
    result = _mean(_invested_capital_log(invcap), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(invcap) times closeadj
def ivc_f62_invested_capital_log_63d_base_v007_signal(invcap, closeadj):
    result = _mean(_invested_capital_log(invcap), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(invcap) times closeadj
def ivc_f62_invested_capital_log_126d_base_v008_signal(invcap, closeadj):
    result = _mean(_invested_capital_log(invcap), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(invcap) times closeadj
def ivc_f62_invested_capital_log_252d_base_v009_signal(invcap, closeadj):
    result = _mean(_invested_capital_log(invcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(invcap) times closeadj
def ivc_f62_invested_capital_log_504d_base_v010_signal(invcap, closeadj):
    result = _mean(_invested_capital_log(invcap), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d invcap/assets mean
def ivc_f62_invested_capital_per_assets_63d_base_v011_signal(invcap, assets):
    result = _mean(_invested_capital_scaled(invcap, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invcap/assets mean
def ivc_f62_invested_capital_per_assets_252d_base_v012_signal(invcap, assets):
    result = _mean(_invested_capital_scaled(invcap, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d invcap/assets mean
def ivc_f62_invested_capital_per_assets_504d_base_v013_signal(invcap, assets):
    result = _mean(_invested_capital_scaled(invcap, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d invcap/marketcap mean
def ivc_f62_invested_capital_per_marketcap_63d_base_v014_signal(invcap, marketcap):
    result = _mean(_invested_capital_scaled(invcap, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invcap/marketcap mean
def ivc_f62_invested_capital_per_marketcap_252d_base_v015_signal(invcap, marketcap):
    result = _mean(_invested_capital_scaled(invcap, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d invcap/marketcap mean
def ivc_f62_invested_capital_per_marketcap_504d_base_v016_signal(invcap, marketcap):
    result = _mean(_invested_capital_scaled(invcap, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d invcap/equity mean
def ivc_f62_invested_capital_per_equity_63d_base_v017_signal(invcap, equity):
    result = _mean(_invested_capital_scaled(invcap, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invcap/equity mean
def ivc_f62_invested_capital_per_equity_252d_base_v018_signal(invcap, equity):
    result = _mean(_invested_capital_scaled(invcap, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d invcap/equity mean
def ivc_f62_invested_capital_per_equity_504d_base_v019_signal(invcap, equity):
    result = _mean(_invested_capital_scaled(invcap, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d invcap/debt mean
def ivc_f62_invested_capital_per_debt_63d_base_v020_signal(invcap, debt):
    result = _mean(_invested_capital_scaled(invcap, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invcap/debt mean
def ivc_f62_invested_capital_per_debt_252d_base_v021_signal(invcap, debt):
    result = _mean(_invested_capital_scaled(invcap, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d invcap/debt mean
def ivc_f62_invested_capital_per_debt_504d_base_v022_signal(invcap, debt):
    result = _mean(_invested_capital_scaled(invcap, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d invcap/revenue mean
def ivc_f62_invested_capital_per_revenue_63d_base_v023_signal(invcap, revenue):
    result = _mean(_invested_capital_scaled(invcap, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invcap/revenue mean
def ivc_f62_invested_capital_per_revenue_252d_base_v024_signal(invcap, revenue):
    result = _mean(_invested_capital_scaled(invcap, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d invcap/revenue mean
def ivc_f62_invested_capital_per_revenue_504d_base_v025_signal(invcap, revenue):
    result = _mean(_invested_capital_scaled(invcap, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d invcap per share times closeadj
def ivc_f62_invested_capital_pershare_21d_base_v026_signal(invcap, sharesbas, closeadj):
    ps = _invested_capital_per_share(invcap, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d invcap per share times closeadj
def ivc_f62_invested_capital_pershare_63d_base_v027_signal(invcap, sharesbas, closeadj):
    ps = _invested_capital_per_share(invcap, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d invcap per share times closeadj
def ivc_f62_invested_capital_pershare_126d_base_v028_signal(invcap, sharesbas, closeadj):
    ps = _invested_capital_per_share(invcap, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invcap per share times closeadj
def ivc_f62_invested_capital_pershare_252d_base_v029_signal(invcap, sharesbas, closeadj):
    ps = _invested_capital_per_share(invcap, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d invcap per share times closeadj
def ivc_f62_invested_capital_pershare_504d_base_v030_signal(invcap, sharesbas, closeadj):
    ps = _invested_capital_per_share(invcap, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of invcap times closeadj
def ivc_f62_invested_capital_std_63d_base_v031_signal(invcap, closeadj):
    result = _std(invcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of invcap times closeadj
def ivc_f62_invested_capital_std_252d_base_v032_signal(invcap, closeadj):
    result = _std(invcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of invcap times closeadj
def ivc_f62_invested_capital_std_504d_base_v033_signal(invcap, closeadj):
    result = _std(invcap, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of invcap
def ivc_f62_invested_capital_z_252d_base_v034_signal(invcap):
    result = _z(invcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of invcap
def ivc_f62_invested_capital_z_504d_base_v035_signal(invcap):
    result = _z(invcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(invcap)
def ivc_f62_invested_capital_logz_252d_base_v036_signal(invcap):
    result = _z(_invested_capital_log(invcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(invcap)
def ivc_f62_invested_capital_logz_504d_base_v037_signal(invcap):
    result = _z(_invested_capital_log(invcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of invcap^2 times closeadj
def ivc_f62_invested_capital_sq_63d_base_v038_signal(invcap, closeadj):
    result = _mean(invcap * invcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of invcap^2 times closeadj
def ivc_f62_invested_capital_sq_252d_base_v039_signal(invcap, closeadj):
    result = _mean(invcap * invcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(invcap) times closeadj
def ivc_f62_invested_capital_sign_21d_base_v040_signal(invcap, closeadj):
    result = _mean(np.sign(invcap), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(invcap) times closeadj
def ivc_f62_invested_capital_sign_63d_base_v041_signal(invcap, closeadj):
    result = _mean(np.sign(invcap), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(invcap) times closeadj
def ivc_f62_invested_capital_sign_252d_base_v042_signal(invcap, closeadj):
    result = _mean(np.sign(invcap), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d invcap/opex mean
def ivc_f62_invested_capital_per_opex_63d_base_v043_signal(invcap, opex):
    result = _mean(_invested_capital_scaled(invcap, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invcap/opex mean
def ivc_f62_invested_capital_per_opex_252d_base_v044_signal(invcap, opex):
    result = _mean(_invested_capital_scaled(invcap, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d invcap/ebitda mean
def ivc_f62_invested_capital_per_ebitda_63d_base_v045_signal(invcap, ebitda):
    result = _mean(_invested_capital_scaled(invcap, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invcap/ebitda mean
def ivc_f62_invested_capital_per_ebitda_252d_base_v046_signal(invcap, ebitda):
    result = _mean(_invested_capital_scaled(invcap, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d invcap/capex mean
def ivc_f62_invested_capital_per_capex_63d_base_v047_signal(invcap, capex):
    result = _mean(_invested_capital_scaled(invcap, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invcap/capex mean
def ivc_f62_invested_capital_per_capex_252d_base_v048_signal(invcap, capex):
    result = _mean(_invested_capital_scaled(invcap, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d invcap/liabilities mean
def ivc_f62_invested_capital_per_liabilities_63d_base_v049_signal(invcap, liabilities):
    result = _mean(_invested_capital_scaled(invcap, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invcap/liabilities mean
def ivc_f62_invested_capital_per_liabilities_252d_base_v050_signal(invcap, liabilities):
    result = _mean(_invested_capital_scaled(invcap, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# invcap relative to 252d max times closeadj
def ivc_f62_invested_capital_relmax_252d_base_v051_signal(invcap, closeadj):
    peak = invcap.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (invcap / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# invcap relative to 504d max times closeadj
def ivc_f62_invested_capital_relmax_504d_base_v052_signal(invcap, closeadj):
    peak = invcap.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (invcap / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# invcap relative to 252d min times closeadj
def ivc_f62_invested_capital_relmin_252d_base_v053_signal(invcap, closeadj):
    trough = invcap.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (invcap / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# invcap relative to 504d min times closeadj
def ivc_f62_invested_capital_relmin_504d_base_v054_signal(invcap, closeadj):
    trough = invcap.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (invcap / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of invcap times closeadj
def ivc_f62_invested_capital_pct_21d_base_v055_signal(invcap, closeadj):
    result = _pct_change(invcap, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of invcap times closeadj
def ivc_f62_invested_capital_pct_63d_base_v056_signal(invcap, closeadj):
    result = _pct_change(invcap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of invcap times closeadj
def ivc_f62_invested_capital_pct_252d_base_v057_signal(invcap, closeadj):
    result = _pct_change(invcap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of invcap times closeadj
def ivc_f62_invested_capital_sum_63d_base_v058_signal(invcap, closeadj):
    result = invcap.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of invcap times closeadj
def ivc_f62_invested_capital_sum_252d_base_v059_signal(invcap, closeadj):
    result = invcap.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of invcap times closeadj
def ivc_f62_invested_capital_sum_504d_base_v060_signal(invcap, closeadj):
    result = invcap.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed invcap(63d) / smoothed assets(252d) x closeadj
def ivc_f62_invested_capital_rom_assets_252_63d_base_v061_signal(invcap, assets, closeadj):
    n = _mean(invcap, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed invcap(126d) / smoothed assets(504d) x closeadj
def ivc_f62_invested_capital_rom_assets_504_126d_base_v062_signal(invcap, assets, closeadj):
    n = _mean(invcap, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed invcap(63d) / smoothed marketcap(252d) x closeadj
def ivc_f62_invested_capital_rom_marketcap_252_63d_base_v063_signal(invcap, marketcap, closeadj):
    n = _mean(invcap, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed invcap(126d) / smoothed marketcap(504d) x closeadj
def ivc_f62_invested_capital_rom_marketcap_504_126d_base_v064_signal(invcap, marketcap, closeadj):
    n = _mean(invcap, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed invcap(63d) / smoothed equity(252d) x closeadj
def ivc_f62_invested_capital_rom_equity_252_63d_base_v065_signal(invcap, equity, closeadj):
    n = _mean(invcap, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed invcap(126d) / smoothed equity(504d) x closeadj
def ivc_f62_invested_capital_rom_equity_504_126d_base_v066_signal(invcap, equity, closeadj):
    n = _mean(invcap, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(invcap) / std(assets)
def ivc_f62_invested_capital_volratio_assets_252d_base_v067_signal(invcap, assets):
    n = _std(invcap, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(invcap) / std(assets)
def ivc_f62_invested_capital_volratio_assets_504d_base_v068_signal(invcap, assets):
    n = _std(invcap, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(invcap) / std(marketcap)
def ivc_f62_invested_capital_volratio_marketcap_252d_base_v069_signal(invcap, marketcap):
    n = _std(invcap, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(invcap) / std(marketcap)
def ivc_f62_invested_capital_volratio_marketcap_504d_base_v070_signal(invcap, marketcap):
    n = _std(invcap, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed invcap times closeadj
def ivc_f62_invested_capital_raw_5d_base_v071_signal(invcap, closeadj):
    result = _mean(invcap, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed invcap times closeadj
def ivc_f62_invested_capital_raw_1008d_base_v072_signal(invcap, closeadj):
    result = _mean(invcap, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of invcap/assets
def ivc_f62_invested_capital_log_per_assets_252d_base_v073_signal(invcap, assets):
    s = _invested_capital_scaled(invcap, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of invcap/assets
def ivc_f62_invested_capital_log_per_assets_504d_base_v074_signal(invcap, assets):
    s = _invested_capital_scaled(invcap, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of invcap/marketcap
def ivc_f62_invested_capital_log_per_marketcap_252d_base_v075_signal(invcap, marketcap):
    s = _invested_capital_scaled(invcap, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
