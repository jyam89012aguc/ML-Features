"""Family f09 - Free cash flow  (B_CashFlow_Burn) | base 001-075"""
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
def _free_cash_flow_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _free_cash_flow_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _free_cash_flow_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed fcf times closeadj
def fcf_f09_free_cash_flow_raw_21d_base_v001_signal(fcf, closeadj):
    result = _mean(fcf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed fcf times closeadj
def fcf_f09_free_cash_flow_raw_63d_base_v002_signal(fcf, closeadj):
    result = _mean(fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed fcf times closeadj
def fcf_f09_free_cash_flow_raw_126d_base_v003_signal(fcf, closeadj):
    result = _mean(fcf, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed fcf times closeadj
def fcf_f09_free_cash_flow_raw_252d_base_v004_signal(fcf, closeadj):
    result = _mean(fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed fcf times closeadj
def fcf_f09_free_cash_flow_raw_504d_base_v005_signal(fcf, closeadj):
    result = _mean(fcf, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(fcf) times closeadj
def fcf_f09_free_cash_flow_log_21d_base_v006_signal(fcf, closeadj):
    result = _mean(_free_cash_flow_log(fcf), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(fcf) times closeadj
def fcf_f09_free_cash_flow_log_63d_base_v007_signal(fcf, closeadj):
    result = _mean(_free_cash_flow_log(fcf), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(fcf) times closeadj
def fcf_f09_free_cash_flow_log_126d_base_v008_signal(fcf, closeadj):
    result = _mean(_free_cash_flow_log(fcf), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(fcf) times closeadj
def fcf_f09_free_cash_flow_log_252d_base_v009_signal(fcf, closeadj):
    result = _mean(_free_cash_flow_log(fcf), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(fcf) times closeadj
def fcf_f09_free_cash_flow_log_504d_base_v010_signal(fcf, closeadj):
    result = _mean(_free_cash_flow_log(fcf), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/assets mean
def fcf_f09_free_cash_flow_per_assets_63d_base_v011_signal(fcf, assets):
    result = _mean(_free_cash_flow_scaled(fcf, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/assets mean
def fcf_f09_free_cash_flow_per_assets_252d_base_v012_signal(fcf, assets):
    result = _mean(_free_cash_flow_scaled(fcf, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf/assets mean
def fcf_f09_free_cash_flow_per_assets_504d_base_v013_signal(fcf, assets):
    result = _mean(_free_cash_flow_scaled(fcf, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/marketcap mean
def fcf_f09_free_cash_flow_per_marketcap_63d_base_v014_signal(fcf, marketcap):
    result = _mean(_free_cash_flow_scaled(fcf, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/marketcap mean
def fcf_f09_free_cash_flow_per_marketcap_252d_base_v015_signal(fcf, marketcap):
    result = _mean(_free_cash_flow_scaled(fcf, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf/marketcap mean
def fcf_f09_free_cash_flow_per_marketcap_504d_base_v016_signal(fcf, marketcap):
    result = _mean(_free_cash_flow_scaled(fcf, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/equity mean
def fcf_f09_free_cash_flow_per_equity_63d_base_v017_signal(fcf, equity):
    result = _mean(_free_cash_flow_scaled(fcf, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/equity mean
def fcf_f09_free_cash_flow_per_equity_252d_base_v018_signal(fcf, equity):
    result = _mean(_free_cash_flow_scaled(fcf, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf/equity mean
def fcf_f09_free_cash_flow_per_equity_504d_base_v019_signal(fcf, equity):
    result = _mean(_free_cash_flow_scaled(fcf, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/debt mean
def fcf_f09_free_cash_flow_per_debt_63d_base_v020_signal(fcf, debt):
    result = _mean(_free_cash_flow_scaled(fcf, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/debt mean
def fcf_f09_free_cash_flow_per_debt_252d_base_v021_signal(fcf, debt):
    result = _mean(_free_cash_flow_scaled(fcf, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf/debt mean
def fcf_f09_free_cash_flow_per_debt_504d_base_v022_signal(fcf, debt):
    result = _mean(_free_cash_flow_scaled(fcf, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/revenue mean
def fcf_f09_free_cash_flow_per_revenue_63d_base_v023_signal(fcf, revenue):
    result = _mean(_free_cash_flow_scaled(fcf, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/revenue mean
def fcf_f09_free_cash_flow_per_revenue_252d_base_v024_signal(fcf, revenue):
    result = _mean(_free_cash_flow_scaled(fcf, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf/revenue mean
def fcf_f09_free_cash_flow_per_revenue_504d_base_v025_signal(fcf, revenue):
    result = _mean(_free_cash_flow_scaled(fcf, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fcf per share times closeadj
def fcf_f09_free_cash_flow_pershare_21d_base_v026_signal(fcf, sharesbas, closeadj):
    ps = _free_cash_flow_per_share(fcf, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf per share times closeadj
def fcf_f09_free_cash_flow_pershare_63d_base_v027_signal(fcf, sharesbas, closeadj):
    ps = _free_cash_flow_per_share(fcf, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fcf per share times closeadj
def fcf_f09_free_cash_flow_pershare_126d_base_v028_signal(fcf, sharesbas, closeadj):
    ps = _free_cash_flow_per_share(fcf, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf per share times closeadj
def fcf_f09_free_cash_flow_pershare_252d_base_v029_signal(fcf, sharesbas, closeadj):
    ps = _free_cash_flow_per_share(fcf, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf per share times closeadj
def fcf_f09_free_cash_flow_pershare_504d_base_v030_signal(fcf, sharesbas, closeadj):
    ps = _free_cash_flow_per_share(fcf, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of fcf times closeadj
def fcf_f09_free_cash_flow_std_63d_base_v031_signal(fcf, closeadj):
    result = _std(fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of fcf times closeadj
def fcf_f09_free_cash_flow_std_252d_base_v032_signal(fcf, closeadj):
    result = _std(fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of fcf times closeadj
def fcf_f09_free_cash_flow_std_504d_base_v033_signal(fcf, closeadj):
    result = _std(fcf, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of fcf
def fcf_f09_free_cash_flow_z_252d_base_v034_signal(fcf):
    result = _z(fcf, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of fcf
def fcf_f09_free_cash_flow_z_504d_base_v035_signal(fcf):
    result = _z(fcf, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(fcf)
def fcf_f09_free_cash_flow_logz_252d_base_v036_signal(fcf):
    result = _z(_free_cash_flow_log(fcf), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(fcf)
def fcf_f09_free_cash_flow_logz_504d_base_v037_signal(fcf):
    result = _z(_free_cash_flow_log(fcf), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of fcf^2 times closeadj
def fcf_f09_free_cash_flow_sq_63d_base_v038_signal(fcf, closeadj):
    result = _mean(fcf * fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of fcf^2 times closeadj
def fcf_f09_free_cash_flow_sq_252d_base_v039_signal(fcf, closeadj):
    result = _mean(fcf * fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(fcf) times closeadj
def fcf_f09_free_cash_flow_sign_21d_base_v040_signal(fcf, closeadj):
    result = _mean(np.sign(fcf), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(fcf) times closeadj
def fcf_f09_free_cash_flow_sign_63d_base_v041_signal(fcf, closeadj):
    result = _mean(np.sign(fcf), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(fcf) times closeadj
def fcf_f09_free_cash_flow_sign_252d_base_v042_signal(fcf, closeadj):
    result = _mean(np.sign(fcf), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/opex mean
def fcf_f09_free_cash_flow_per_opex_63d_base_v043_signal(fcf, opex):
    result = _mean(_free_cash_flow_scaled(fcf, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/opex mean
def fcf_f09_free_cash_flow_per_opex_252d_base_v044_signal(fcf, opex):
    result = _mean(_free_cash_flow_scaled(fcf, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/ebitda mean
def fcf_f09_free_cash_flow_per_ebitda_63d_base_v045_signal(fcf, ebitda):
    result = _mean(_free_cash_flow_scaled(fcf, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/ebitda mean
def fcf_f09_free_cash_flow_per_ebitda_252d_base_v046_signal(fcf, ebitda):
    result = _mean(_free_cash_flow_scaled(fcf, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/capex mean
def fcf_f09_free_cash_flow_per_capex_63d_base_v047_signal(fcf, capex):
    result = _mean(_free_cash_flow_scaled(fcf, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/capex mean
def fcf_f09_free_cash_flow_per_capex_252d_base_v048_signal(fcf, capex):
    result = _mean(_free_cash_flow_scaled(fcf, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/liabilities mean
def fcf_f09_free_cash_flow_per_liabilities_63d_base_v049_signal(fcf, liabilities):
    result = _mean(_free_cash_flow_scaled(fcf, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/liabilities mean
def fcf_f09_free_cash_flow_per_liabilities_252d_base_v050_signal(fcf, liabilities):
    result = _mean(_free_cash_flow_scaled(fcf, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf relative to 252d max times closeadj
def fcf_f09_free_cash_flow_relmax_252d_base_v051_signal(fcf, closeadj):
    peak = fcf.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (fcf / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fcf relative to 504d max times closeadj
def fcf_f09_free_cash_flow_relmax_504d_base_v052_signal(fcf, closeadj):
    peak = fcf.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (fcf / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fcf relative to 252d min times closeadj
def fcf_f09_free_cash_flow_relmin_252d_base_v053_signal(fcf, closeadj):
    trough = fcf.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (fcf / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fcf relative to 504d min times closeadj
def fcf_f09_free_cash_flow_relmin_504d_base_v054_signal(fcf, closeadj):
    trough = fcf.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (fcf / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of fcf times closeadj
def fcf_f09_free_cash_flow_pct_21d_base_v055_signal(fcf, closeadj):
    result = _pct_change(fcf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of fcf times closeadj
def fcf_f09_free_cash_flow_pct_63d_base_v056_signal(fcf, closeadj):
    result = _pct_change(fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of fcf times closeadj
def fcf_f09_free_cash_flow_pct_252d_base_v057_signal(fcf, closeadj):
    result = _pct_change(fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of fcf times closeadj
def fcf_f09_free_cash_flow_sum_63d_base_v058_signal(fcf, closeadj):
    result = fcf.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of fcf times closeadj
def fcf_f09_free_cash_flow_sum_252d_base_v059_signal(fcf, closeadj):
    result = fcf.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of fcf times closeadj
def fcf_f09_free_cash_flow_sum_504d_base_v060_signal(fcf, closeadj):
    result = fcf.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed fcf(63d) / smoothed assets(252d) x closeadj
def fcf_f09_free_cash_flow_rom_assets_252_63d_base_v061_signal(fcf, assets, closeadj):
    n = _mean(fcf, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed fcf(126d) / smoothed assets(504d) x closeadj
def fcf_f09_free_cash_flow_rom_assets_504_126d_base_v062_signal(fcf, assets, closeadj):
    n = _mean(fcf, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed fcf(63d) / smoothed marketcap(252d) x closeadj
def fcf_f09_free_cash_flow_rom_marketcap_252_63d_base_v063_signal(fcf, marketcap, closeadj):
    n = _mean(fcf, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed fcf(126d) / smoothed marketcap(504d) x closeadj
def fcf_f09_free_cash_flow_rom_marketcap_504_126d_base_v064_signal(fcf, marketcap, closeadj):
    n = _mean(fcf, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed fcf(63d) / smoothed equity(252d) x closeadj
def fcf_f09_free_cash_flow_rom_equity_252_63d_base_v065_signal(fcf, equity, closeadj):
    n = _mean(fcf, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed fcf(126d) / smoothed equity(504d) x closeadj
def fcf_f09_free_cash_flow_rom_equity_504_126d_base_v066_signal(fcf, equity, closeadj):
    n = _mean(fcf, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(fcf) / std(assets)
def fcf_f09_free_cash_flow_volratio_assets_252d_base_v067_signal(fcf, assets):
    n = _std(fcf, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(fcf) / std(assets)
def fcf_f09_free_cash_flow_volratio_assets_504d_base_v068_signal(fcf, assets):
    n = _std(fcf, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(fcf) / std(marketcap)
def fcf_f09_free_cash_flow_volratio_marketcap_252d_base_v069_signal(fcf, marketcap):
    n = _std(fcf, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(fcf) / std(marketcap)
def fcf_f09_free_cash_flow_volratio_marketcap_504d_base_v070_signal(fcf, marketcap):
    n = _std(fcf, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed fcf times closeadj
def fcf_f09_free_cash_flow_raw_5d_base_v071_signal(fcf, closeadj):
    result = _mean(fcf, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed fcf times closeadj
def fcf_f09_free_cash_flow_raw_1008d_base_v072_signal(fcf, closeadj):
    result = _mean(fcf, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of fcf/assets
def fcf_f09_free_cash_flow_log_per_assets_252d_base_v073_signal(fcf, assets):
    s = _free_cash_flow_scaled(fcf, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of fcf/assets
def fcf_f09_free_cash_flow_log_per_assets_504d_base_v074_signal(fcf, assets):
    s = _free_cash_flow_scaled(fcf, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of fcf/marketcap
def fcf_f09_free_cash_flow_log_per_marketcap_252d_base_v075_signal(fcf, marketcap):
    s = _free_cash_flow_scaled(fcf, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
