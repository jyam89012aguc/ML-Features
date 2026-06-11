"""Family f24 - Interest expense & coverage  (D_Capital_Debt) | base 001-075"""
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
def _interest_coverage_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _interest_coverage_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _interest_coverage_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed intexp times closeadj
def ic_f24_interest_coverage_raw_21d_base_v001_signal(intexp, closeadj):
    result = _mean(intexp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed intexp times closeadj
def ic_f24_interest_coverage_raw_63d_base_v002_signal(intexp, closeadj):
    result = _mean(intexp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed intexp times closeadj
def ic_f24_interest_coverage_raw_126d_base_v003_signal(intexp, closeadj):
    result = _mean(intexp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed intexp times closeadj
def ic_f24_interest_coverage_raw_252d_base_v004_signal(intexp, closeadj):
    result = _mean(intexp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed intexp times closeadj
def ic_f24_interest_coverage_raw_504d_base_v005_signal(intexp, closeadj):
    result = _mean(intexp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(intexp) times closeadj
def ic_f24_interest_coverage_log_21d_base_v006_signal(intexp, closeadj):
    result = _mean(_interest_coverage_log(intexp), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(intexp) times closeadj
def ic_f24_interest_coverage_log_63d_base_v007_signal(intexp, closeadj):
    result = _mean(_interest_coverage_log(intexp), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(intexp) times closeadj
def ic_f24_interest_coverage_log_126d_base_v008_signal(intexp, closeadj):
    result = _mean(_interest_coverage_log(intexp), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(intexp) times closeadj
def ic_f24_interest_coverage_log_252d_base_v009_signal(intexp, closeadj):
    result = _mean(_interest_coverage_log(intexp), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(intexp) times closeadj
def ic_f24_interest_coverage_log_504d_base_v010_signal(intexp, closeadj):
    result = _mean(_interest_coverage_log(intexp), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intexp/assets mean
def ic_f24_interest_coverage_per_assets_63d_base_v011_signal(intexp, assets):
    result = _mean(_interest_coverage_scaled(intexp, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp/assets mean
def ic_f24_interest_coverage_per_assets_252d_base_v012_signal(intexp, assets):
    result = _mean(_interest_coverage_scaled(intexp, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intexp/assets mean
def ic_f24_interest_coverage_per_assets_504d_base_v013_signal(intexp, assets):
    result = _mean(_interest_coverage_scaled(intexp, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intexp/marketcap mean
def ic_f24_interest_coverage_per_marketcap_63d_base_v014_signal(intexp, marketcap):
    result = _mean(_interest_coverage_scaled(intexp, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp/marketcap mean
def ic_f24_interest_coverage_per_marketcap_252d_base_v015_signal(intexp, marketcap):
    result = _mean(_interest_coverage_scaled(intexp, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intexp/marketcap mean
def ic_f24_interest_coverage_per_marketcap_504d_base_v016_signal(intexp, marketcap):
    result = _mean(_interest_coverage_scaled(intexp, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intexp/equity mean
def ic_f24_interest_coverage_per_equity_63d_base_v017_signal(intexp, equity):
    result = _mean(_interest_coverage_scaled(intexp, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp/equity mean
def ic_f24_interest_coverage_per_equity_252d_base_v018_signal(intexp, equity):
    result = _mean(_interest_coverage_scaled(intexp, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intexp/equity mean
def ic_f24_interest_coverage_per_equity_504d_base_v019_signal(intexp, equity):
    result = _mean(_interest_coverage_scaled(intexp, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intexp/debt mean
def ic_f24_interest_coverage_per_debt_63d_base_v020_signal(intexp, debt):
    result = _mean(_interest_coverage_scaled(intexp, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp/debt mean
def ic_f24_interest_coverage_per_debt_252d_base_v021_signal(intexp, debt):
    result = _mean(_interest_coverage_scaled(intexp, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intexp/debt mean
def ic_f24_interest_coverage_per_debt_504d_base_v022_signal(intexp, debt):
    result = _mean(_interest_coverage_scaled(intexp, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intexp/revenue mean
def ic_f24_interest_coverage_per_revenue_63d_base_v023_signal(intexp, revenue):
    result = _mean(_interest_coverage_scaled(intexp, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp/revenue mean
def ic_f24_interest_coverage_per_revenue_252d_base_v024_signal(intexp, revenue):
    result = _mean(_interest_coverage_scaled(intexp, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intexp/revenue mean
def ic_f24_interest_coverage_per_revenue_504d_base_v025_signal(intexp, revenue):
    result = _mean(_interest_coverage_scaled(intexp, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intexp per share times closeadj
def ic_f24_interest_coverage_pershare_21d_base_v026_signal(intexp, sharesbas, closeadj):
    ps = _interest_coverage_per_share(intexp, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intexp per share times closeadj
def ic_f24_interest_coverage_pershare_63d_base_v027_signal(intexp, sharesbas, closeadj):
    ps = _interest_coverage_per_share(intexp, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d intexp per share times closeadj
def ic_f24_interest_coverage_pershare_126d_base_v028_signal(intexp, sharesbas, closeadj):
    ps = _interest_coverage_per_share(intexp, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp per share times closeadj
def ic_f24_interest_coverage_pershare_252d_base_v029_signal(intexp, sharesbas, closeadj):
    ps = _interest_coverage_per_share(intexp, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intexp per share times closeadj
def ic_f24_interest_coverage_pershare_504d_base_v030_signal(intexp, sharesbas, closeadj):
    ps = _interest_coverage_per_share(intexp, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of intexp times closeadj
def ic_f24_interest_coverage_std_63d_base_v031_signal(intexp, closeadj):
    result = _std(intexp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of intexp times closeadj
def ic_f24_interest_coverage_std_252d_base_v032_signal(intexp, closeadj):
    result = _std(intexp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of intexp times closeadj
def ic_f24_interest_coverage_std_504d_base_v033_signal(intexp, closeadj):
    result = _std(intexp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of intexp
def ic_f24_interest_coverage_z_252d_base_v034_signal(intexp):
    result = _z(intexp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of intexp
def ic_f24_interest_coverage_z_504d_base_v035_signal(intexp):
    result = _z(intexp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(intexp)
def ic_f24_interest_coverage_logz_252d_base_v036_signal(intexp):
    result = _z(_interest_coverage_log(intexp), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(intexp)
def ic_f24_interest_coverage_logz_504d_base_v037_signal(intexp):
    result = _z(_interest_coverage_log(intexp), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of intexp^2 times closeadj
def ic_f24_interest_coverage_sq_63d_base_v038_signal(intexp, closeadj):
    result = _mean(intexp * intexp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of intexp^2 times closeadj
def ic_f24_interest_coverage_sq_252d_base_v039_signal(intexp, closeadj):
    result = _mean(intexp * intexp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(intexp) times closeadj
def ic_f24_interest_coverage_sign_21d_base_v040_signal(intexp, closeadj):
    result = _mean(np.sign(intexp), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(intexp) times closeadj
def ic_f24_interest_coverage_sign_63d_base_v041_signal(intexp, closeadj):
    result = _mean(np.sign(intexp), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(intexp) times closeadj
def ic_f24_interest_coverage_sign_252d_base_v042_signal(intexp, closeadj):
    result = _mean(np.sign(intexp), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intexp/opex mean
def ic_f24_interest_coverage_per_opex_63d_base_v043_signal(intexp, opex):
    result = _mean(_interest_coverage_scaled(intexp, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp/opex mean
def ic_f24_interest_coverage_per_opex_252d_base_v044_signal(intexp, opex):
    result = _mean(_interest_coverage_scaled(intexp, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intexp/ebitda mean
def ic_f24_interest_coverage_per_ebitda_63d_base_v045_signal(intexp, ebitda):
    result = _mean(_interest_coverage_scaled(intexp, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp/ebitda mean
def ic_f24_interest_coverage_per_ebitda_252d_base_v046_signal(intexp, ebitda):
    result = _mean(_interest_coverage_scaled(intexp, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intexp/capex mean
def ic_f24_interest_coverage_per_capex_63d_base_v047_signal(intexp, capex):
    result = _mean(_interest_coverage_scaled(intexp, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp/capex mean
def ic_f24_interest_coverage_per_capex_252d_base_v048_signal(intexp, capex):
    result = _mean(_interest_coverage_scaled(intexp, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intexp/liabilities mean
def ic_f24_interest_coverage_per_liabilities_63d_base_v049_signal(intexp, liabilities):
    result = _mean(_interest_coverage_scaled(intexp, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intexp/liabilities mean
def ic_f24_interest_coverage_per_liabilities_252d_base_v050_signal(intexp, liabilities):
    result = _mean(_interest_coverage_scaled(intexp, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# intexp relative to 252d max times closeadj
def ic_f24_interest_coverage_relmax_252d_base_v051_signal(intexp, closeadj):
    peak = intexp.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (intexp / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# intexp relative to 504d max times closeadj
def ic_f24_interest_coverage_relmax_504d_base_v052_signal(intexp, closeadj):
    peak = intexp.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (intexp / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# intexp relative to 252d min times closeadj
def ic_f24_interest_coverage_relmin_252d_base_v053_signal(intexp, closeadj):
    trough = intexp.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (intexp / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# intexp relative to 504d min times closeadj
def ic_f24_interest_coverage_relmin_504d_base_v054_signal(intexp, closeadj):
    trough = intexp.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (intexp / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of intexp times closeadj
def ic_f24_interest_coverage_pct_21d_base_v055_signal(intexp, closeadj):
    result = _pct_change(intexp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of intexp times closeadj
def ic_f24_interest_coverage_pct_63d_base_v056_signal(intexp, closeadj):
    result = _pct_change(intexp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of intexp times closeadj
def ic_f24_interest_coverage_pct_252d_base_v057_signal(intexp, closeadj):
    result = _pct_change(intexp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of intexp times closeadj
def ic_f24_interest_coverage_sum_63d_base_v058_signal(intexp, closeadj):
    result = intexp.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of intexp times closeadj
def ic_f24_interest_coverage_sum_252d_base_v059_signal(intexp, closeadj):
    result = intexp.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of intexp times closeadj
def ic_f24_interest_coverage_sum_504d_base_v060_signal(intexp, closeadj):
    result = intexp.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed intexp(63d) / smoothed assets(252d) x closeadj
def ic_f24_interest_coverage_rom_assets_252_63d_base_v061_signal(intexp, assets, closeadj):
    n = _mean(intexp, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed intexp(126d) / smoothed assets(504d) x closeadj
def ic_f24_interest_coverage_rom_assets_504_126d_base_v062_signal(intexp, assets, closeadj):
    n = _mean(intexp, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed intexp(63d) / smoothed marketcap(252d) x closeadj
def ic_f24_interest_coverage_rom_marketcap_252_63d_base_v063_signal(intexp, marketcap, closeadj):
    n = _mean(intexp, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed intexp(126d) / smoothed marketcap(504d) x closeadj
def ic_f24_interest_coverage_rom_marketcap_504_126d_base_v064_signal(intexp, marketcap, closeadj):
    n = _mean(intexp, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed intexp(63d) / smoothed equity(252d) x closeadj
def ic_f24_interest_coverage_rom_equity_252_63d_base_v065_signal(intexp, equity, closeadj):
    n = _mean(intexp, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed intexp(126d) / smoothed equity(504d) x closeadj
def ic_f24_interest_coverage_rom_equity_504_126d_base_v066_signal(intexp, equity, closeadj):
    n = _mean(intexp, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(intexp) / std(assets)
def ic_f24_interest_coverage_volratio_assets_252d_base_v067_signal(intexp, assets):
    n = _std(intexp, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(intexp) / std(assets)
def ic_f24_interest_coverage_volratio_assets_504d_base_v068_signal(intexp, assets):
    n = _std(intexp, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(intexp) / std(marketcap)
def ic_f24_interest_coverage_volratio_marketcap_252d_base_v069_signal(intexp, marketcap):
    n = _std(intexp, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(intexp) / std(marketcap)
def ic_f24_interest_coverage_volratio_marketcap_504d_base_v070_signal(intexp, marketcap):
    n = _std(intexp, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed intexp times closeadj
def ic_f24_interest_coverage_raw_5d_base_v071_signal(intexp, closeadj):
    result = _mean(intexp, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed intexp times closeadj
def ic_f24_interest_coverage_raw_1008d_base_v072_signal(intexp, closeadj):
    result = _mean(intexp, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of intexp/assets
def ic_f24_interest_coverage_log_per_assets_252d_base_v073_signal(intexp, assets):
    s = _interest_coverage_scaled(intexp, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of intexp/assets
def ic_f24_interest_coverage_log_per_assets_504d_base_v074_signal(intexp, assets):
    s = _interest_coverage_scaled(intexp, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of intexp/marketcap
def ic_f24_interest_coverage_log_per_marketcap_252d_base_v075_signal(intexp, marketcap):
    s = _interest_coverage_scaled(intexp, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
