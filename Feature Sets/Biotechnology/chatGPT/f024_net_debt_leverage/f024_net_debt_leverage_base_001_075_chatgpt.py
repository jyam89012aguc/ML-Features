"""Family f024 - Net debt leverage (Capital Structure) | Sharadar tables: SF1 | fields: debt, cashneq, investments, ebitda, assets | base 001-075"""
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
def _net_debt_leverage_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _net_debt_leverage_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _net_debt_leverage_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed debt times closeadj
def ndl_f024_net_debt_leverage_raw_21d_base_v001_signal(debt, closeadj):
    result = _mean(debt, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed debt times closeadj
def ndl_f024_net_debt_leverage_raw_63d_base_v002_signal(debt, closeadj):
    result = _mean(debt, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed debt times closeadj
def ndl_f024_net_debt_leverage_raw_126d_base_v003_signal(debt, closeadj):
    result = _mean(debt, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed debt times closeadj
def ndl_f024_net_debt_leverage_raw_252d_base_v004_signal(debt, closeadj):
    result = _mean(debt, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed debt times closeadj
def ndl_f024_net_debt_leverage_raw_504d_base_v005_signal(debt, closeadj):
    result = _mean(debt, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(debt) times closeadj
def ndl_f024_net_debt_leverage_log_21d_base_v006_signal(debt, closeadj):
    result = _mean(_net_debt_leverage_log(debt), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(debt) times closeadj
def ndl_f024_net_debt_leverage_log_63d_base_v007_signal(debt, closeadj):
    result = _mean(_net_debt_leverage_log(debt), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(debt) times closeadj
def ndl_f024_net_debt_leverage_log_126d_base_v008_signal(debt, closeadj):
    result = _mean(_net_debt_leverage_log(debt), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(debt) times closeadj
def ndl_f024_net_debt_leverage_log_252d_base_v009_signal(debt, closeadj):
    result = _mean(_net_debt_leverage_log(debt), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(debt) times closeadj
def ndl_f024_net_debt_leverage_log_504d_base_v010_signal(debt, closeadj):
    result = _mean(_net_debt_leverage_log(debt), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt/cashneq mean
def ndl_f024_net_debt_leverage_per_cashneq_63d_base_v011_signal(debt, cashneq):
    result = _mean(_net_debt_leverage_scaled(debt, cashneq), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt/cashneq mean
def ndl_f024_net_debt_leverage_per_cashneq_252d_base_v012_signal(debt, cashneq):
    result = _mean(_net_debt_leverage_scaled(debt, cashneq), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt/cashneq mean
def ndl_f024_net_debt_leverage_per_cashneq_504d_base_v013_signal(debt, cashneq):
    result = _mean(_net_debt_leverage_scaled(debt, cashneq), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt/investments mean
def ndl_f024_net_debt_leverage_per_investments_63d_base_v014_signal(debt, investments):
    result = _mean(_net_debt_leverage_scaled(debt, investments), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt/investments mean
def ndl_f024_net_debt_leverage_per_investments_252d_base_v015_signal(debt, investments):
    result = _mean(_net_debt_leverage_scaled(debt, investments), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt/investments mean
def ndl_f024_net_debt_leverage_per_investments_504d_base_v016_signal(debt, investments):
    result = _mean(_net_debt_leverage_scaled(debt, investments), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt/assets mean
def ndl_f024_net_debt_leverage_per_assets_63d_base_v017_signal(debt, assets):
    result = _mean(_net_debt_leverage_scaled(debt, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt/assets mean
def ndl_f024_net_debt_leverage_per_assets_252d_base_v018_signal(debt, assets):
    result = _mean(_net_debt_leverage_scaled(debt, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt/assets mean
def ndl_f024_net_debt_leverage_per_assets_504d_base_v019_signal(debt, assets):
    result = _mean(_net_debt_leverage_scaled(debt, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt/marketcap mean
def ndl_f024_net_debt_leverage_per_marketcap_63d_base_v020_signal(debt, marketcap):
    result = _mean(_net_debt_leverage_scaled(debt, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt/marketcap mean
def ndl_f024_net_debt_leverage_per_marketcap_252d_base_v021_signal(debt, marketcap):
    result = _mean(_net_debt_leverage_scaled(debt, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt/marketcap mean
def ndl_f024_net_debt_leverage_per_marketcap_504d_base_v022_signal(debt, marketcap):
    result = _mean(_net_debt_leverage_scaled(debt, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt/equity mean
def ndl_f024_net_debt_leverage_per_equity_63d_base_v023_signal(debt, equity):
    result = _mean(_net_debt_leverage_scaled(debt, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt/equity mean
def ndl_f024_net_debt_leverage_per_equity_252d_base_v024_signal(debt, equity):
    result = _mean(_net_debt_leverage_scaled(debt, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt/equity mean
def ndl_f024_net_debt_leverage_per_equity_504d_base_v025_signal(debt, equity):
    result = _mean(_net_debt_leverage_scaled(debt, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt per share times closeadj
def ndl_f024_net_debt_leverage_pershare_21d_base_v026_signal(debt, sharesbas, closeadj):
    ps = _net_debt_leverage_per_share(debt, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt per share times closeadj
def ndl_f024_net_debt_leverage_pershare_63d_base_v027_signal(debt, sharesbas, closeadj):
    ps = _net_debt_leverage_per_share(debt, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d debt per share times closeadj
def ndl_f024_net_debt_leverage_pershare_126d_base_v028_signal(debt, sharesbas, closeadj):
    ps = _net_debt_leverage_per_share(debt, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt per share times closeadj
def ndl_f024_net_debt_leverage_pershare_252d_base_v029_signal(debt, sharesbas, closeadj):
    ps = _net_debt_leverage_per_share(debt, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt per share times closeadj
def ndl_f024_net_debt_leverage_pershare_504d_base_v030_signal(debt, sharesbas, closeadj):
    ps = _net_debt_leverage_per_share(debt, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of debt times closeadj
def ndl_f024_net_debt_leverage_std_63d_base_v031_signal(debt, closeadj):
    result = _std(debt, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of debt times closeadj
def ndl_f024_net_debt_leverage_std_252d_base_v032_signal(debt, closeadj):
    result = _std(debt, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of debt times closeadj
def ndl_f024_net_debt_leverage_std_504d_base_v033_signal(debt, closeadj):
    result = _std(debt, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of debt
def ndl_f024_net_debt_leverage_z_252d_base_v034_signal(debt):
    result = _z(debt, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of debt
def ndl_f024_net_debt_leverage_z_504d_base_v035_signal(debt):
    result = _z(debt, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(debt)
def ndl_f024_net_debt_leverage_logz_252d_base_v036_signal(debt):
    result = _z(_net_debt_leverage_log(debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(debt)
def ndl_f024_net_debt_leverage_logz_504d_base_v037_signal(debt):
    result = _z(_net_debt_leverage_log(debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of debt^2 times closeadj
def ndl_f024_net_debt_leverage_sq_63d_base_v038_signal(debt, closeadj):
    result = _mean(debt * debt, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of debt^2 times closeadj
def ndl_f024_net_debt_leverage_sq_252d_base_v039_signal(debt, closeadj):
    result = _mean(debt * debt, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(debt) times closeadj
def ndl_f024_net_debt_leverage_sign_21d_base_v040_signal(debt, closeadj):
    result = _mean(np.sign(debt), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(debt) times closeadj
def ndl_f024_net_debt_leverage_sign_63d_base_v041_signal(debt, closeadj):
    result = _mean(np.sign(debt), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(debt) times closeadj
def ndl_f024_net_debt_leverage_sign_252d_base_v042_signal(debt, closeadj):
    result = _mean(np.sign(debt), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt/opex mean
def ndl_f024_net_debt_leverage_per_opex_63d_base_v043_signal(debt, opex):
    result = _mean(_net_debt_leverage_scaled(debt, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt/opex mean
def ndl_f024_net_debt_leverage_per_opex_252d_base_v044_signal(debt, opex):
    result = _mean(_net_debt_leverage_scaled(debt, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt/ebitda mean
def ndl_f024_net_debt_leverage_per_ebitda_63d_base_v045_signal(debt, ebitda):
    result = _mean(_net_debt_leverage_scaled(debt, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt/ebitda mean
def ndl_f024_net_debt_leverage_per_ebitda_252d_base_v046_signal(debt, ebitda):
    result = _mean(_net_debt_leverage_scaled(debt, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt/capex mean
def ndl_f024_net_debt_leverage_per_capex_63d_base_v047_signal(debt, capex):
    result = _mean(_net_debt_leverage_scaled(debt, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt/capex mean
def ndl_f024_net_debt_leverage_per_capex_252d_base_v048_signal(debt, capex):
    result = _mean(_net_debt_leverage_scaled(debt, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt/liabilities mean
def ndl_f024_net_debt_leverage_per_liabilities_63d_base_v049_signal(debt, liabilities):
    result = _mean(_net_debt_leverage_scaled(debt, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt/liabilities mean
def ndl_f024_net_debt_leverage_per_liabilities_252d_base_v050_signal(debt, liabilities):
    result = _mean(_net_debt_leverage_scaled(debt, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# debt relative to 252d max times closeadj
def ndl_f024_net_debt_leverage_relmax_252d_base_v051_signal(debt, closeadj):
    peak = debt.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (debt / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debt relative to 504d max times closeadj
def ndl_f024_net_debt_leverage_relmax_504d_base_v052_signal(debt, closeadj):
    peak = debt.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (debt / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debt relative to 252d min times closeadj
def ndl_f024_net_debt_leverage_relmin_252d_base_v053_signal(debt, closeadj):
    trough = debt.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (debt / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# debt relative to 504d min times closeadj
def ndl_f024_net_debt_leverage_relmin_504d_base_v054_signal(debt, closeadj):
    trough = debt.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (debt / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of debt times closeadj
def ndl_f024_net_debt_leverage_pct_21d_base_v055_signal(debt, closeadj):
    result = _pct_change(debt, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of debt times closeadj
def ndl_f024_net_debt_leverage_pct_63d_base_v056_signal(debt, closeadj):
    result = _pct_change(debt, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of debt times closeadj
def ndl_f024_net_debt_leverage_pct_252d_base_v057_signal(debt, closeadj):
    result = _pct_change(debt, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of debt times closeadj
def ndl_f024_net_debt_leverage_sum_63d_base_v058_signal(debt, closeadj):
    result = debt.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of debt times closeadj
def ndl_f024_net_debt_leverage_sum_252d_base_v059_signal(debt, closeadj):
    result = debt.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of debt times closeadj
def ndl_f024_net_debt_leverage_sum_504d_base_v060_signal(debt, closeadj):
    result = debt.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed debt(63d) / smoothed cashneq(252d) x closeadj
def ndl_f024_net_debt_leverage_rom_cashneq_252_63d_base_v061_signal(debt, cashneq, closeadj):
    n = _mean(debt, 63)
    d = _mean(cashneq, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed debt(126d) / smoothed cashneq(504d) x closeadj
def ndl_f024_net_debt_leverage_rom_cashneq_504_126d_base_v062_signal(debt, cashneq, closeadj):
    n = _mean(debt, 126)
    d = _mean(cashneq, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed debt(63d) / smoothed investments(252d) x closeadj
def ndl_f024_net_debt_leverage_rom_investments_252_63d_base_v063_signal(debt, investments, closeadj):
    n = _mean(debt, 63)
    d = _mean(investments, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed debt(126d) / smoothed investments(504d) x closeadj
def ndl_f024_net_debt_leverage_rom_investments_504_126d_base_v064_signal(debt, investments, closeadj):
    n = _mean(debt, 126)
    d = _mean(investments, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed debt(63d) / smoothed assets(252d) x closeadj
def ndl_f024_net_debt_leverage_rom_assets_252_63d_base_v065_signal(debt, assets, closeadj):
    n = _mean(debt, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed debt(126d) / smoothed assets(504d) x closeadj
def ndl_f024_net_debt_leverage_rom_assets_504_126d_base_v066_signal(debt, assets, closeadj):
    n = _mean(debt, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(debt) / std(cashneq)
def ndl_f024_net_debt_leverage_volratio_cashneq_252d_base_v067_signal(debt, cashneq):
    n = _std(debt, 252)
    d = _std(cashneq, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(debt) / std(cashneq)
def ndl_f024_net_debt_leverage_volratio_cashneq_504d_base_v068_signal(debt, cashneq):
    n = _std(debt, 504)
    d = _std(cashneq, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(debt) / std(investments)
def ndl_f024_net_debt_leverage_volratio_investments_252d_base_v069_signal(debt, investments):
    n = _std(debt, 252)
    d = _std(investments, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(debt) / std(investments)
def ndl_f024_net_debt_leverage_volratio_investments_504d_base_v070_signal(debt, investments):
    n = _std(debt, 504)
    d = _std(investments, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed debt times closeadj
def ndl_f024_net_debt_leverage_raw_5d_base_v071_signal(debt, closeadj):
    result = _mean(debt, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed debt times closeadj
def ndl_f024_net_debt_leverage_raw_1008d_base_v072_signal(debt, closeadj):
    result = _mean(debt, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of debt/cashneq
def ndl_f024_net_debt_leverage_log_per_cashneq_252d_base_v073_signal(debt, cashneq):
    s = _net_debt_leverage_scaled(debt, cashneq)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of debt/cashneq
def ndl_f024_net_debt_leverage_log_per_cashneq_504d_base_v074_signal(debt, cashneq):
    s = _net_debt_leverage_scaled(debt, cashneq)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of debt/investments
def ndl_f024_net_debt_leverage_log_per_investments_252d_base_v075_signal(debt, investments):
    s = _net_debt_leverage_scaled(debt, investments)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
