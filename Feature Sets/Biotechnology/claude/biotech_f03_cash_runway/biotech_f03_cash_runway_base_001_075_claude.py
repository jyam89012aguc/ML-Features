"""Family f03 - Cash runway in quarters  (A_Liquidity_Runway) | base 001-075"""
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
def _cash_runway_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _cash_runway_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _cash_runway_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed cashneq times closeadj
def cr_f03_cash_runway_raw_21d_base_v001_signal(cashneq, closeadj):
    result = _mean(cashneq, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed cashneq times closeadj
def cr_f03_cash_runway_raw_63d_base_v002_signal(cashneq, closeadj):
    result = _mean(cashneq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed cashneq times closeadj
def cr_f03_cash_runway_raw_126d_base_v003_signal(cashneq, closeadj):
    result = _mean(cashneq, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed cashneq times closeadj
def cr_f03_cash_runway_raw_252d_base_v004_signal(cashneq, closeadj):
    result = _mean(cashneq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed cashneq times closeadj
def cr_f03_cash_runway_raw_504d_base_v005_signal(cashneq, closeadj):
    result = _mean(cashneq, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(cashneq) times closeadj
def cr_f03_cash_runway_log_21d_base_v006_signal(cashneq, closeadj):
    result = _mean(_cash_runway_log(cashneq), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(cashneq) times closeadj
def cr_f03_cash_runway_log_63d_base_v007_signal(cashneq, closeadj):
    result = _mean(_cash_runway_log(cashneq), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(cashneq) times closeadj
def cr_f03_cash_runway_log_126d_base_v008_signal(cashneq, closeadj):
    result = _mean(_cash_runway_log(cashneq), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(cashneq) times closeadj
def cr_f03_cash_runway_log_252d_base_v009_signal(cashneq, closeadj):
    result = _mean(_cash_runway_log(cashneq), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(cashneq) times closeadj
def cr_f03_cash_runway_log_504d_base_v010_signal(cashneq, closeadj):
    result = _mean(_cash_runway_log(cashneq), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/assets mean
def cr_f03_cash_runway_per_assets_63d_base_v011_signal(cashneq, assets):
    result = _mean(_cash_runway_scaled(cashneq, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/assets mean
def cr_f03_cash_runway_per_assets_252d_base_v012_signal(cashneq, assets):
    result = _mean(_cash_runway_scaled(cashneq, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cashneq/assets mean
def cr_f03_cash_runway_per_assets_504d_base_v013_signal(cashneq, assets):
    result = _mean(_cash_runway_scaled(cashneq, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/marketcap mean
def cr_f03_cash_runway_per_marketcap_63d_base_v014_signal(cashneq, marketcap):
    result = _mean(_cash_runway_scaled(cashneq, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/marketcap mean
def cr_f03_cash_runway_per_marketcap_252d_base_v015_signal(cashneq, marketcap):
    result = _mean(_cash_runway_scaled(cashneq, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cashneq/marketcap mean
def cr_f03_cash_runway_per_marketcap_504d_base_v016_signal(cashneq, marketcap):
    result = _mean(_cash_runway_scaled(cashneq, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/equity mean
def cr_f03_cash_runway_per_equity_63d_base_v017_signal(cashneq, equity):
    result = _mean(_cash_runway_scaled(cashneq, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/equity mean
def cr_f03_cash_runway_per_equity_252d_base_v018_signal(cashneq, equity):
    result = _mean(_cash_runway_scaled(cashneq, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cashneq/equity mean
def cr_f03_cash_runway_per_equity_504d_base_v019_signal(cashneq, equity):
    result = _mean(_cash_runway_scaled(cashneq, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/debt mean
def cr_f03_cash_runway_per_debt_63d_base_v020_signal(cashneq, debt):
    result = _mean(_cash_runway_scaled(cashneq, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/debt mean
def cr_f03_cash_runway_per_debt_252d_base_v021_signal(cashneq, debt):
    result = _mean(_cash_runway_scaled(cashneq, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cashneq/debt mean
def cr_f03_cash_runway_per_debt_504d_base_v022_signal(cashneq, debt):
    result = _mean(_cash_runway_scaled(cashneq, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/revenue mean
def cr_f03_cash_runway_per_revenue_63d_base_v023_signal(cashneq, revenue):
    result = _mean(_cash_runway_scaled(cashneq, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/revenue mean
def cr_f03_cash_runway_per_revenue_252d_base_v024_signal(cashneq, revenue):
    result = _mean(_cash_runway_scaled(cashneq, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cashneq/revenue mean
def cr_f03_cash_runway_per_revenue_504d_base_v025_signal(cashneq, revenue):
    result = _mean(_cash_runway_scaled(cashneq, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cashneq per share times closeadj
def cr_f03_cash_runway_pershare_21d_base_v026_signal(cashneq, sharesbas, closeadj):
    ps = _cash_runway_per_share(cashneq, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq per share times closeadj
def cr_f03_cash_runway_pershare_63d_base_v027_signal(cashneq, sharesbas, closeadj):
    ps = _cash_runway_per_share(cashneq, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cashneq per share times closeadj
def cr_f03_cash_runway_pershare_126d_base_v028_signal(cashneq, sharesbas, closeadj):
    ps = _cash_runway_per_share(cashneq, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq per share times closeadj
def cr_f03_cash_runway_pershare_252d_base_v029_signal(cashneq, sharesbas, closeadj):
    ps = _cash_runway_per_share(cashneq, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cashneq per share times closeadj
def cr_f03_cash_runway_pershare_504d_base_v030_signal(cashneq, sharesbas, closeadj):
    ps = _cash_runway_per_share(cashneq, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of cashneq times closeadj
def cr_f03_cash_runway_std_63d_base_v031_signal(cashneq, closeadj):
    result = _std(cashneq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of cashneq times closeadj
def cr_f03_cash_runway_std_252d_base_v032_signal(cashneq, closeadj):
    result = _std(cashneq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of cashneq times closeadj
def cr_f03_cash_runway_std_504d_base_v033_signal(cashneq, closeadj):
    result = _std(cashneq, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of cashneq
def cr_f03_cash_runway_z_252d_base_v034_signal(cashneq):
    result = _z(cashneq, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of cashneq
def cr_f03_cash_runway_z_504d_base_v035_signal(cashneq):
    result = _z(cashneq, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(cashneq)
def cr_f03_cash_runway_logz_252d_base_v036_signal(cashneq):
    result = _z(_cash_runway_log(cashneq), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(cashneq)
def cr_f03_cash_runway_logz_504d_base_v037_signal(cashneq):
    result = _z(_cash_runway_log(cashneq), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of cashneq^2 times closeadj
def cr_f03_cash_runway_sq_63d_base_v038_signal(cashneq, closeadj):
    result = _mean(cashneq * cashneq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of cashneq^2 times closeadj
def cr_f03_cash_runway_sq_252d_base_v039_signal(cashneq, closeadj):
    result = _mean(cashneq * cashneq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(cashneq) times closeadj
def cr_f03_cash_runway_sign_21d_base_v040_signal(cashneq, closeadj):
    result = _mean(np.sign(cashneq), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(cashneq) times closeadj
def cr_f03_cash_runway_sign_63d_base_v041_signal(cashneq, closeadj):
    result = _mean(np.sign(cashneq), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(cashneq) times closeadj
def cr_f03_cash_runway_sign_252d_base_v042_signal(cashneq, closeadj):
    result = _mean(np.sign(cashneq), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/opex mean
def cr_f03_cash_runway_per_opex_63d_base_v043_signal(cashneq, opex):
    result = _mean(_cash_runway_scaled(cashneq, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/opex mean
def cr_f03_cash_runway_per_opex_252d_base_v044_signal(cashneq, opex):
    result = _mean(_cash_runway_scaled(cashneq, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/ebitda mean
def cr_f03_cash_runway_per_ebitda_63d_base_v045_signal(cashneq, ebitda):
    result = _mean(_cash_runway_scaled(cashneq, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/ebitda mean
def cr_f03_cash_runway_per_ebitda_252d_base_v046_signal(cashneq, ebitda):
    result = _mean(_cash_runway_scaled(cashneq, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/capex mean
def cr_f03_cash_runway_per_capex_63d_base_v047_signal(cashneq, capex):
    result = _mean(_cash_runway_scaled(cashneq, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/capex mean
def cr_f03_cash_runway_per_capex_252d_base_v048_signal(cashneq, capex):
    result = _mean(_cash_runway_scaled(cashneq, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashneq/liabilities mean
def cr_f03_cash_runway_per_liabilities_63d_base_v049_signal(cashneq, liabilities):
    result = _mean(_cash_runway_scaled(cashneq, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashneq/liabilities mean
def cr_f03_cash_runway_per_liabilities_252d_base_v050_signal(cashneq, liabilities):
    result = _mean(_cash_runway_scaled(cashneq, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq relative to 252d max times closeadj
def cr_f03_cash_runway_relmax_252d_base_v051_signal(cashneq, closeadj):
    peak = cashneq.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (cashneq / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq relative to 504d max times closeadj
def cr_f03_cash_runway_relmax_504d_base_v052_signal(cashneq, closeadj):
    peak = cashneq.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (cashneq / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq relative to 252d min times closeadj
def cr_f03_cash_runway_relmin_252d_base_v053_signal(cashneq, closeadj):
    trough = cashneq.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (cashneq / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq relative to 504d min times closeadj
def cr_f03_cash_runway_relmin_504d_base_v054_signal(cashneq, closeadj):
    trough = cashneq.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (cashneq / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of cashneq times closeadj
def cr_f03_cash_runway_pct_21d_base_v055_signal(cashneq, closeadj):
    result = _pct_change(cashneq, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of cashneq times closeadj
def cr_f03_cash_runway_pct_63d_base_v056_signal(cashneq, closeadj):
    result = _pct_change(cashneq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of cashneq times closeadj
def cr_f03_cash_runway_pct_252d_base_v057_signal(cashneq, closeadj):
    result = _pct_change(cashneq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of cashneq times closeadj
def cr_f03_cash_runway_sum_63d_base_v058_signal(cashneq, closeadj):
    result = cashneq.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of cashneq times closeadj
def cr_f03_cash_runway_sum_252d_base_v059_signal(cashneq, closeadj):
    result = cashneq.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of cashneq times closeadj
def cr_f03_cash_runway_sum_504d_base_v060_signal(cashneq, closeadj):
    result = cashneq.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed cashneq(63d) / smoothed assets(252d) x closeadj
def cr_f03_cash_runway_rom_assets_252_63d_base_v061_signal(cashneq, assets, closeadj):
    n = _mean(cashneq, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed cashneq(126d) / smoothed assets(504d) x closeadj
def cr_f03_cash_runway_rom_assets_504_126d_base_v062_signal(cashneq, assets, closeadj):
    n = _mean(cashneq, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed cashneq(63d) / smoothed marketcap(252d) x closeadj
def cr_f03_cash_runway_rom_marketcap_252_63d_base_v063_signal(cashneq, marketcap, closeadj):
    n = _mean(cashneq, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed cashneq(126d) / smoothed marketcap(504d) x closeadj
def cr_f03_cash_runway_rom_marketcap_504_126d_base_v064_signal(cashneq, marketcap, closeadj):
    n = _mean(cashneq, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed cashneq(63d) / smoothed equity(252d) x closeadj
def cr_f03_cash_runway_rom_equity_252_63d_base_v065_signal(cashneq, equity, closeadj):
    n = _mean(cashneq, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed cashneq(126d) / smoothed equity(504d) x closeadj
def cr_f03_cash_runway_rom_equity_504_126d_base_v066_signal(cashneq, equity, closeadj):
    n = _mean(cashneq, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(cashneq) / std(assets)
def cr_f03_cash_runway_volratio_assets_252d_base_v067_signal(cashneq, assets):
    n = _std(cashneq, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(cashneq) / std(assets)
def cr_f03_cash_runway_volratio_assets_504d_base_v068_signal(cashneq, assets):
    n = _std(cashneq, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(cashneq) / std(marketcap)
def cr_f03_cash_runway_volratio_marketcap_252d_base_v069_signal(cashneq, marketcap):
    n = _std(cashneq, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(cashneq) / std(marketcap)
def cr_f03_cash_runway_volratio_marketcap_504d_base_v070_signal(cashneq, marketcap):
    n = _std(cashneq, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed cashneq times closeadj
def cr_f03_cash_runway_raw_5d_base_v071_signal(cashneq, closeadj):
    result = _mean(cashneq, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed cashneq times closeadj
def cr_f03_cash_runway_raw_1008d_base_v072_signal(cashneq, closeadj):
    result = _mean(cashneq, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of cashneq/assets
def cr_f03_cash_runway_log_per_assets_252d_base_v073_signal(cashneq, assets):
    s = _cash_runway_scaled(cashneq, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of cashneq/assets
def cr_f03_cash_runway_log_per_assets_504d_base_v074_signal(cashneq, assets):
    s = _cash_runway_scaled(cashneq, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of cashneq/marketcap
def cr_f03_cash_runway_log_per_marketcap_252d_base_v075_signal(cashneq, marketcap):
    s = _cash_runway_scaled(cashneq, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
