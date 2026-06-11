"""Family f67 - Working-capital change as cash drag  (K_WorkingCapital) | base 001-075"""
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
def _working_capital_change_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _working_capital_change_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _working_capital_change_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed workingcapital times closeadj
def wcc_f67_working_capital_change_raw_21d_base_v001_signal(workingcapital, closeadj):
    result = _mean(workingcapital, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed workingcapital times closeadj
def wcc_f67_working_capital_change_raw_63d_base_v002_signal(workingcapital, closeadj):
    result = _mean(workingcapital, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed workingcapital times closeadj
def wcc_f67_working_capital_change_raw_126d_base_v003_signal(workingcapital, closeadj):
    result = _mean(workingcapital, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed workingcapital times closeadj
def wcc_f67_working_capital_change_raw_252d_base_v004_signal(workingcapital, closeadj):
    result = _mean(workingcapital, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed workingcapital times closeadj
def wcc_f67_working_capital_change_raw_504d_base_v005_signal(workingcapital, closeadj):
    result = _mean(workingcapital, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(workingcapital) times closeadj
def wcc_f67_working_capital_change_log_21d_base_v006_signal(workingcapital, closeadj):
    result = _mean(_working_capital_change_log(workingcapital), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(workingcapital) times closeadj
def wcc_f67_working_capital_change_log_63d_base_v007_signal(workingcapital, closeadj):
    result = _mean(_working_capital_change_log(workingcapital), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(workingcapital) times closeadj
def wcc_f67_working_capital_change_log_126d_base_v008_signal(workingcapital, closeadj):
    result = _mean(_working_capital_change_log(workingcapital), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(workingcapital) times closeadj
def wcc_f67_working_capital_change_log_252d_base_v009_signal(workingcapital, closeadj):
    result = _mean(_working_capital_change_log(workingcapital), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(workingcapital) times closeadj
def wcc_f67_working_capital_change_log_504d_base_v010_signal(workingcapital, closeadj):
    result = _mean(_working_capital_change_log(workingcapital), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d workingcapital/assets mean
def wcc_f67_working_capital_change_per_assets_63d_base_v011_signal(workingcapital, assets):
    result = _mean(_working_capital_change_scaled(workingcapital, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d workingcapital/assets mean
def wcc_f67_working_capital_change_per_assets_252d_base_v012_signal(workingcapital, assets):
    result = _mean(_working_capital_change_scaled(workingcapital, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d workingcapital/assets mean
def wcc_f67_working_capital_change_per_assets_504d_base_v013_signal(workingcapital, assets):
    result = _mean(_working_capital_change_scaled(workingcapital, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d workingcapital/marketcap mean
def wcc_f67_working_capital_change_per_marketcap_63d_base_v014_signal(workingcapital, marketcap):
    result = _mean(_working_capital_change_scaled(workingcapital, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d workingcapital/marketcap mean
def wcc_f67_working_capital_change_per_marketcap_252d_base_v015_signal(workingcapital, marketcap):
    result = _mean(_working_capital_change_scaled(workingcapital, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d workingcapital/marketcap mean
def wcc_f67_working_capital_change_per_marketcap_504d_base_v016_signal(workingcapital, marketcap):
    result = _mean(_working_capital_change_scaled(workingcapital, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d workingcapital/equity mean
def wcc_f67_working_capital_change_per_equity_63d_base_v017_signal(workingcapital, equity):
    result = _mean(_working_capital_change_scaled(workingcapital, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d workingcapital/equity mean
def wcc_f67_working_capital_change_per_equity_252d_base_v018_signal(workingcapital, equity):
    result = _mean(_working_capital_change_scaled(workingcapital, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d workingcapital/equity mean
def wcc_f67_working_capital_change_per_equity_504d_base_v019_signal(workingcapital, equity):
    result = _mean(_working_capital_change_scaled(workingcapital, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d workingcapital/debt mean
def wcc_f67_working_capital_change_per_debt_63d_base_v020_signal(workingcapital, debt):
    result = _mean(_working_capital_change_scaled(workingcapital, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d workingcapital/debt mean
def wcc_f67_working_capital_change_per_debt_252d_base_v021_signal(workingcapital, debt):
    result = _mean(_working_capital_change_scaled(workingcapital, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d workingcapital/debt mean
def wcc_f67_working_capital_change_per_debt_504d_base_v022_signal(workingcapital, debt):
    result = _mean(_working_capital_change_scaled(workingcapital, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d workingcapital/revenue mean
def wcc_f67_working_capital_change_per_revenue_63d_base_v023_signal(workingcapital, revenue):
    result = _mean(_working_capital_change_scaled(workingcapital, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d workingcapital/revenue mean
def wcc_f67_working_capital_change_per_revenue_252d_base_v024_signal(workingcapital, revenue):
    result = _mean(_working_capital_change_scaled(workingcapital, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d workingcapital/revenue mean
def wcc_f67_working_capital_change_per_revenue_504d_base_v025_signal(workingcapital, revenue):
    result = _mean(_working_capital_change_scaled(workingcapital, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d workingcapital per share times closeadj
def wcc_f67_working_capital_change_pershare_21d_base_v026_signal(workingcapital, sharesbas, closeadj):
    ps = _working_capital_change_per_share(workingcapital, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d workingcapital per share times closeadj
def wcc_f67_working_capital_change_pershare_63d_base_v027_signal(workingcapital, sharesbas, closeadj):
    ps = _working_capital_change_per_share(workingcapital, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d workingcapital per share times closeadj
def wcc_f67_working_capital_change_pershare_126d_base_v028_signal(workingcapital, sharesbas, closeadj):
    ps = _working_capital_change_per_share(workingcapital, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d workingcapital per share times closeadj
def wcc_f67_working_capital_change_pershare_252d_base_v029_signal(workingcapital, sharesbas, closeadj):
    ps = _working_capital_change_per_share(workingcapital, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d workingcapital per share times closeadj
def wcc_f67_working_capital_change_pershare_504d_base_v030_signal(workingcapital, sharesbas, closeadj):
    ps = _working_capital_change_per_share(workingcapital, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of workingcapital times closeadj
def wcc_f67_working_capital_change_std_63d_base_v031_signal(workingcapital, closeadj):
    result = _std(workingcapital, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of workingcapital times closeadj
def wcc_f67_working_capital_change_std_252d_base_v032_signal(workingcapital, closeadj):
    result = _std(workingcapital, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of workingcapital times closeadj
def wcc_f67_working_capital_change_std_504d_base_v033_signal(workingcapital, closeadj):
    result = _std(workingcapital, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of workingcapital
def wcc_f67_working_capital_change_z_252d_base_v034_signal(workingcapital):
    result = _z(workingcapital, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of workingcapital
def wcc_f67_working_capital_change_z_504d_base_v035_signal(workingcapital):
    result = _z(workingcapital, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(workingcapital)
def wcc_f67_working_capital_change_logz_252d_base_v036_signal(workingcapital):
    result = _z(_working_capital_change_log(workingcapital), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(workingcapital)
def wcc_f67_working_capital_change_logz_504d_base_v037_signal(workingcapital):
    result = _z(_working_capital_change_log(workingcapital), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of workingcapital^2 times closeadj
def wcc_f67_working_capital_change_sq_63d_base_v038_signal(workingcapital, closeadj):
    result = _mean(workingcapital * workingcapital, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of workingcapital^2 times closeadj
def wcc_f67_working_capital_change_sq_252d_base_v039_signal(workingcapital, closeadj):
    result = _mean(workingcapital * workingcapital, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(workingcapital) times closeadj
def wcc_f67_working_capital_change_sign_21d_base_v040_signal(workingcapital, closeadj):
    result = _mean(np.sign(workingcapital), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(workingcapital) times closeadj
def wcc_f67_working_capital_change_sign_63d_base_v041_signal(workingcapital, closeadj):
    result = _mean(np.sign(workingcapital), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(workingcapital) times closeadj
def wcc_f67_working_capital_change_sign_252d_base_v042_signal(workingcapital, closeadj):
    result = _mean(np.sign(workingcapital), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d workingcapital/opex mean
def wcc_f67_working_capital_change_per_opex_63d_base_v043_signal(workingcapital, opex):
    result = _mean(_working_capital_change_scaled(workingcapital, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d workingcapital/opex mean
def wcc_f67_working_capital_change_per_opex_252d_base_v044_signal(workingcapital, opex):
    result = _mean(_working_capital_change_scaled(workingcapital, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d workingcapital/ebitda mean
def wcc_f67_working_capital_change_per_ebitda_63d_base_v045_signal(workingcapital, ebitda):
    result = _mean(_working_capital_change_scaled(workingcapital, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d workingcapital/ebitda mean
def wcc_f67_working_capital_change_per_ebitda_252d_base_v046_signal(workingcapital, ebitda):
    result = _mean(_working_capital_change_scaled(workingcapital, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d workingcapital/capex mean
def wcc_f67_working_capital_change_per_capex_63d_base_v047_signal(workingcapital, capex):
    result = _mean(_working_capital_change_scaled(workingcapital, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d workingcapital/capex mean
def wcc_f67_working_capital_change_per_capex_252d_base_v048_signal(workingcapital, capex):
    result = _mean(_working_capital_change_scaled(workingcapital, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d workingcapital/liabilities mean
def wcc_f67_working_capital_change_per_liabilities_63d_base_v049_signal(workingcapital, liabilities):
    result = _mean(_working_capital_change_scaled(workingcapital, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d workingcapital/liabilities mean
def wcc_f67_working_capital_change_per_liabilities_252d_base_v050_signal(workingcapital, liabilities):
    result = _mean(_working_capital_change_scaled(workingcapital, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# workingcapital relative to 252d max times closeadj
def wcc_f67_working_capital_change_relmax_252d_base_v051_signal(workingcapital, closeadj):
    peak = workingcapital.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (workingcapital / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# workingcapital relative to 504d max times closeadj
def wcc_f67_working_capital_change_relmax_504d_base_v052_signal(workingcapital, closeadj):
    peak = workingcapital.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (workingcapital / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# workingcapital relative to 252d min times closeadj
def wcc_f67_working_capital_change_relmin_252d_base_v053_signal(workingcapital, closeadj):
    trough = workingcapital.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (workingcapital / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# workingcapital relative to 504d min times closeadj
def wcc_f67_working_capital_change_relmin_504d_base_v054_signal(workingcapital, closeadj):
    trough = workingcapital.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (workingcapital / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of workingcapital times closeadj
def wcc_f67_working_capital_change_pct_21d_base_v055_signal(workingcapital, closeadj):
    result = _pct_change(workingcapital, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of workingcapital times closeadj
def wcc_f67_working_capital_change_pct_63d_base_v056_signal(workingcapital, closeadj):
    result = _pct_change(workingcapital, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of workingcapital times closeadj
def wcc_f67_working_capital_change_pct_252d_base_v057_signal(workingcapital, closeadj):
    result = _pct_change(workingcapital, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of workingcapital times closeadj
def wcc_f67_working_capital_change_sum_63d_base_v058_signal(workingcapital, closeadj):
    result = workingcapital.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of workingcapital times closeadj
def wcc_f67_working_capital_change_sum_252d_base_v059_signal(workingcapital, closeadj):
    result = workingcapital.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of workingcapital times closeadj
def wcc_f67_working_capital_change_sum_504d_base_v060_signal(workingcapital, closeadj):
    result = workingcapital.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed workingcapital(63d) / smoothed assets(252d) x closeadj
def wcc_f67_working_capital_change_rom_assets_252_63d_base_v061_signal(workingcapital, assets, closeadj):
    n = _mean(workingcapital, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed workingcapital(126d) / smoothed assets(504d) x closeadj
def wcc_f67_working_capital_change_rom_assets_504_126d_base_v062_signal(workingcapital, assets, closeadj):
    n = _mean(workingcapital, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed workingcapital(63d) / smoothed marketcap(252d) x closeadj
def wcc_f67_working_capital_change_rom_marketcap_252_63d_base_v063_signal(workingcapital, marketcap, closeadj):
    n = _mean(workingcapital, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed workingcapital(126d) / smoothed marketcap(504d) x closeadj
def wcc_f67_working_capital_change_rom_marketcap_504_126d_base_v064_signal(workingcapital, marketcap, closeadj):
    n = _mean(workingcapital, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed workingcapital(63d) / smoothed equity(252d) x closeadj
def wcc_f67_working_capital_change_rom_equity_252_63d_base_v065_signal(workingcapital, equity, closeadj):
    n = _mean(workingcapital, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed workingcapital(126d) / smoothed equity(504d) x closeadj
def wcc_f67_working_capital_change_rom_equity_504_126d_base_v066_signal(workingcapital, equity, closeadj):
    n = _mean(workingcapital, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(workingcapital) / std(assets)
def wcc_f67_working_capital_change_volratio_assets_252d_base_v067_signal(workingcapital, assets):
    n = _std(workingcapital, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(workingcapital) / std(assets)
def wcc_f67_working_capital_change_volratio_assets_504d_base_v068_signal(workingcapital, assets):
    n = _std(workingcapital, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(workingcapital) / std(marketcap)
def wcc_f67_working_capital_change_volratio_marketcap_252d_base_v069_signal(workingcapital, marketcap):
    n = _std(workingcapital, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(workingcapital) / std(marketcap)
def wcc_f67_working_capital_change_volratio_marketcap_504d_base_v070_signal(workingcapital, marketcap):
    n = _std(workingcapital, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed workingcapital times closeadj
def wcc_f67_working_capital_change_raw_5d_base_v071_signal(workingcapital, closeadj):
    result = _mean(workingcapital, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed workingcapital times closeadj
def wcc_f67_working_capital_change_raw_1008d_base_v072_signal(workingcapital, closeadj):
    result = _mean(workingcapital, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of workingcapital/assets
def wcc_f67_working_capital_change_log_per_assets_252d_base_v073_signal(workingcapital, assets):
    s = _working_capital_change_scaled(workingcapital, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of workingcapital/assets
def wcc_f67_working_capital_change_log_per_assets_504d_base_v074_signal(workingcapital, assets):
    s = _working_capital_change_scaled(workingcapital, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of workingcapital/marketcap
def wcc_f67_working_capital_change_log_per_marketcap_252d_base_v075_signal(workingcapital, marketcap):
    s = _working_capital_change_scaled(workingcapital, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
