"""Family f41 - Book value & equity trajectory  (F_BalanceSheet) | base 001-075"""
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
def _equity_trajectory_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _equity_trajectory_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _equity_trajectory_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed equity times closeadj
def eqt_f41_equity_trajectory_raw_21d_base_v001_signal(equity, closeadj):
    result = _mean(equity, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed equity times closeadj
def eqt_f41_equity_trajectory_raw_63d_base_v002_signal(equity, closeadj):
    result = _mean(equity, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed equity times closeadj
def eqt_f41_equity_trajectory_raw_126d_base_v003_signal(equity, closeadj):
    result = _mean(equity, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed equity times closeadj
def eqt_f41_equity_trajectory_raw_252d_base_v004_signal(equity, closeadj):
    result = _mean(equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed equity times closeadj
def eqt_f41_equity_trajectory_raw_504d_base_v005_signal(equity, closeadj):
    result = _mean(equity, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(equity) times closeadj
def eqt_f41_equity_trajectory_log_21d_base_v006_signal(equity, closeadj):
    result = _mean(_equity_trajectory_log(equity), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(equity) times closeadj
def eqt_f41_equity_trajectory_log_63d_base_v007_signal(equity, closeadj):
    result = _mean(_equity_trajectory_log(equity), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(equity) times closeadj
def eqt_f41_equity_trajectory_log_126d_base_v008_signal(equity, closeadj):
    result = _mean(_equity_trajectory_log(equity), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(equity) times closeadj
def eqt_f41_equity_trajectory_log_252d_base_v009_signal(equity, closeadj):
    result = _mean(_equity_trajectory_log(equity), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(equity) times closeadj
def eqt_f41_equity_trajectory_log_504d_base_v010_signal(equity, closeadj):
    result = _mean(_equity_trajectory_log(equity), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d equity/assets mean
def eqt_f41_equity_trajectory_per_assets_63d_base_v011_signal(equity, assets):
    result = _mean(_equity_trajectory_scaled(equity, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity/assets mean
def eqt_f41_equity_trajectory_per_assets_252d_base_v012_signal(equity, assets):
    result = _mean(_equity_trajectory_scaled(equity, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d equity/assets mean
def eqt_f41_equity_trajectory_per_assets_504d_base_v013_signal(equity, assets):
    result = _mean(_equity_trajectory_scaled(equity, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d equity/marketcap mean
def eqt_f41_equity_trajectory_per_marketcap_63d_base_v014_signal(equity, marketcap):
    result = _mean(_equity_trajectory_scaled(equity, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity/marketcap mean
def eqt_f41_equity_trajectory_per_marketcap_252d_base_v015_signal(equity, marketcap):
    result = _mean(_equity_trajectory_scaled(equity, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d equity/marketcap mean
def eqt_f41_equity_trajectory_per_marketcap_504d_base_v016_signal(equity, marketcap):
    result = _mean(_equity_trajectory_scaled(equity, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d equity/equity mean
def eqt_f41_equity_trajectory_per_equity_63d_base_v017_signal(equity):
    result = _mean(_equity_trajectory_scaled(equity, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity/equity mean
def eqt_f41_equity_trajectory_per_equity_252d_base_v018_signal(equity):
    result = _mean(_equity_trajectory_scaled(equity, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d equity/equity mean
def eqt_f41_equity_trajectory_per_equity_504d_base_v019_signal(equity):
    result = _mean(_equity_trajectory_scaled(equity, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d equity/debt mean
def eqt_f41_equity_trajectory_per_debt_63d_base_v020_signal(equity, debt):
    result = _mean(_equity_trajectory_scaled(equity, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity/debt mean
def eqt_f41_equity_trajectory_per_debt_252d_base_v021_signal(equity, debt):
    result = _mean(_equity_trajectory_scaled(equity, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d equity/debt mean
def eqt_f41_equity_trajectory_per_debt_504d_base_v022_signal(equity, debt):
    result = _mean(_equity_trajectory_scaled(equity, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d equity/revenue mean
def eqt_f41_equity_trajectory_per_revenue_63d_base_v023_signal(equity, revenue):
    result = _mean(_equity_trajectory_scaled(equity, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity/revenue mean
def eqt_f41_equity_trajectory_per_revenue_252d_base_v024_signal(equity, revenue):
    result = _mean(_equity_trajectory_scaled(equity, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d equity/revenue mean
def eqt_f41_equity_trajectory_per_revenue_504d_base_v025_signal(equity, revenue):
    result = _mean(_equity_trajectory_scaled(equity, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d equity per share times closeadj
def eqt_f41_equity_trajectory_pershare_21d_base_v026_signal(equity, sharesbas, closeadj):
    ps = _equity_trajectory_per_share(equity, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d equity per share times closeadj
def eqt_f41_equity_trajectory_pershare_63d_base_v027_signal(equity, sharesbas, closeadj):
    ps = _equity_trajectory_per_share(equity, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d equity per share times closeadj
def eqt_f41_equity_trajectory_pershare_126d_base_v028_signal(equity, sharesbas, closeadj):
    ps = _equity_trajectory_per_share(equity, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity per share times closeadj
def eqt_f41_equity_trajectory_pershare_252d_base_v029_signal(equity, sharesbas, closeadj):
    ps = _equity_trajectory_per_share(equity, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d equity per share times closeadj
def eqt_f41_equity_trajectory_pershare_504d_base_v030_signal(equity, sharesbas, closeadj):
    ps = _equity_trajectory_per_share(equity, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of equity times closeadj
def eqt_f41_equity_trajectory_std_63d_base_v031_signal(equity, closeadj):
    result = _std(equity, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of equity times closeadj
def eqt_f41_equity_trajectory_std_252d_base_v032_signal(equity, closeadj):
    result = _std(equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of equity times closeadj
def eqt_f41_equity_trajectory_std_504d_base_v033_signal(equity, closeadj):
    result = _std(equity, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of equity
def eqt_f41_equity_trajectory_z_252d_base_v034_signal(equity):
    result = _z(equity, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of equity
def eqt_f41_equity_trajectory_z_504d_base_v035_signal(equity):
    result = _z(equity, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(equity)
def eqt_f41_equity_trajectory_logz_252d_base_v036_signal(equity):
    result = _z(_equity_trajectory_log(equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(equity)
def eqt_f41_equity_trajectory_logz_504d_base_v037_signal(equity):
    result = _z(_equity_trajectory_log(equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of equity^2 times closeadj
def eqt_f41_equity_trajectory_sq_63d_base_v038_signal(equity, closeadj):
    result = _mean(equity * equity, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of equity^2 times closeadj
def eqt_f41_equity_trajectory_sq_252d_base_v039_signal(equity, closeadj):
    result = _mean(equity * equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(equity) times closeadj
def eqt_f41_equity_trajectory_sign_21d_base_v040_signal(equity, closeadj):
    result = _mean(np.sign(equity), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(equity) times closeadj
def eqt_f41_equity_trajectory_sign_63d_base_v041_signal(equity, closeadj):
    result = _mean(np.sign(equity), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(equity) times closeadj
def eqt_f41_equity_trajectory_sign_252d_base_v042_signal(equity, closeadj):
    result = _mean(np.sign(equity), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d equity/opex mean
def eqt_f41_equity_trajectory_per_opex_63d_base_v043_signal(equity, opex):
    result = _mean(_equity_trajectory_scaled(equity, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity/opex mean
def eqt_f41_equity_trajectory_per_opex_252d_base_v044_signal(equity, opex):
    result = _mean(_equity_trajectory_scaled(equity, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d equity/ebitda mean
def eqt_f41_equity_trajectory_per_ebitda_63d_base_v045_signal(equity, ebitda):
    result = _mean(_equity_trajectory_scaled(equity, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity/ebitda mean
def eqt_f41_equity_trajectory_per_ebitda_252d_base_v046_signal(equity, ebitda):
    result = _mean(_equity_trajectory_scaled(equity, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d equity/capex mean
def eqt_f41_equity_trajectory_per_capex_63d_base_v047_signal(equity, capex):
    result = _mean(_equity_trajectory_scaled(equity, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity/capex mean
def eqt_f41_equity_trajectory_per_capex_252d_base_v048_signal(equity, capex):
    result = _mean(_equity_trajectory_scaled(equity, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d equity/liabilities mean
def eqt_f41_equity_trajectory_per_liabilities_63d_base_v049_signal(equity, liabilities):
    result = _mean(_equity_trajectory_scaled(equity, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity/liabilities mean
def eqt_f41_equity_trajectory_per_liabilities_252d_base_v050_signal(equity, liabilities):
    result = _mean(_equity_trajectory_scaled(equity, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# equity relative to 252d max times closeadj
def eqt_f41_equity_trajectory_relmax_252d_base_v051_signal(equity, closeadj):
    peak = equity.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (equity / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# equity relative to 504d max times closeadj
def eqt_f41_equity_trajectory_relmax_504d_base_v052_signal(equity, closeadj):
    peak = equity.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (equity / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# equity relative to 252d min times closeadj
def eqt_f41_equity_trajectory_relmin_252d_base_v053_signal(equity, closeadj):
    trough = equity.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (equity / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# equity relative to 504d min times closeadj
def eqt_f41_equity_trajectory_relmin_504d_base_v054_signal(equity, closeadj):
    trough = equity.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (equity / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of equity times closeadj
def eqt_f41_equity_trajectory_pct_21d_base_v055_signal(equity, closeadj):
    result = _pct_change(equity, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of equity times closeadj
def eqt_f41_equity_trajectory_pct_63d_base_v056_signal(equity, closeadj):
    result = _pct_change(equity, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of equity times closeadj
def eqt_f41_equity_trajectory_pct_252d_base_v057_signal(equity, closeadj):
    result = _pct_change(equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of equity times closeadj
def eqt_f41_equity_trajectory_sum_63d_base_v058_signal(equity, closeadj):
    result = equity.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of equity times closeadj
def eqt_f41_equity_trajectory_sum_252d_base_v059_signal(equity, closeadj):
    result = equity.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of equity times closeadj
def eqt_f41_equity_trajectory_sum_504d_base_v060_signal(equity, closeadj):
    result = equity.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed equity(63d) / smoothed assets(252d) x closeadj
def eqt_f41_equity_trajectory_rom_assets_252_63d_base_v061_signal(equity, assets, closeadj):
    n = _mean(equity, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed equity(126d) / smoothed assets(504d) x closeadj
def eqt_f41_equity_trajectory_rom_assets_504_126d_base_v062_signal(equity, assets, closeadj):
    n = _mean(equity, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed equity(63d) / smoothed marketcap(252d) x closeadj
def eqt_f41_equity_trajectory_rom_marketcap_252_63d_base_v063_signal(equity, marketcap, closeadj):
    n = _mean(equity, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed equity(126d) / smoothed marketcap(504d) x closeadj
def eqt_f41_equity_trajectory_rom_marketcap_504_126d_base_v064_signal(equity, marketcap, closeadj):
    n = _mean(equity, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed equity(63d) / smoothed equity(252d) x closeadj
def eqt_f41_equity_trajectory_rom_equity_252_63d_base_v065_signal(equity, closeadj):
    n = _mean(equity, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed equity(126d) / smoothed equity(504d) x closeadj
def eqt_f41_equity_trajectory_rom_equity_504_126d_base_v066_signal(equity, closeadj):
    n = _mean(equity, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(equity) / std(assets)
def eqt_f41_equity_trajectory_volratio_assets_252d_base_v067_signal(equity, assets):
    n = _std(equity, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(equity) / std(assets)
def eqt_f41_equity_trajectory_volratio_assets_504d_base_v068_signal(equity, assets):
    n = _std(equity, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(equity) / std(marketcap)
def eqt_f41_equity_trajectory_volratio_marketcap_252d_base_v069_signal(equity, marketcap):
    n = _std(equity, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(equity) / std(marketcap)
def eqt_f41_equity_trajectory_volratio_marketcap_504d_base_v070_signal(equity, marketcap):
    n = _std(equity, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed equity times closeadj
def eqt_f41_equity_trajectory_raw_5d_base_v071_signal(equity, closeadj):
    result = _mean(equity, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed equity times closeadj
def eqt_f41_equity_trajectory_raw_1008d_base_v072_signal(equity, closeadj):
    result = _mean(equity, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of equity/assets
def eqt_f41_equity_trajectory_log_per_assets_252d_base_v073_signal(equity, assets):
    s = _equity_trajectory_scaled(equity, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of equity/assets
def eqt_f41_equity_trajectory_log_per_assets_504d_base_v074_signal(equity, assets):
    s = _equity_trajectory_scaled(equity, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of equity/marketcap
def eqt_f41_equity_trajectory_log_per_marketcap_252d_base_v075_signal(equity, marketcap):
    s = _equity_trajectory_scaled(equity, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
