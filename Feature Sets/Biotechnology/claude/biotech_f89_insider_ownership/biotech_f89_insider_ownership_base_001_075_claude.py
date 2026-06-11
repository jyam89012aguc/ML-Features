"""Family f89 - Insider ownership level & change  (O_Insider_SF2) | base 001-075"""
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
def _insider_ownership_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _insider_ownership_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _insider_ownership_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_raw_21d_base_v001_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(sharesownedfollowingtransaction, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_raw_63d_base_v002_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(sharesownedfollowingtransaction, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_raw_126d_base_v003_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(sharesownedfollowingtransaction, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_raw_252d_base_v004_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(sharesownedfollowingtransaction, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_raw_504d_base_v005_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(sharesownedfollowingtransaction, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(sharesownedfollowingtransaction) times closeadj
def iow_f89_insider_ownership_log_21d_base_v006_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(_insider_ownership_log(sharesownedfollowingtransaction), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(sharesownedfollowingtransaction) times closeadj
def iow_f89_insider_ownership_log_63d_base_v007_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(_insider_ownership_log(sharesownedfollowingtransaction), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(sharesownedfollowingtransaction) times closeadj
def iow_f89_insider_ownership_log_126d_base_v008_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(_insider_ownership_log(sharesownedfollowingtransaction), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(sharesownedfollowingtransaction) times closeadj
def iow_f89_insider_ownership_log_252d_base_v009_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(_insider_ownership_log(sharesownedfollowingtransaction), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(sharesownedfollowingtransaction) times closeadj
def iow_f89_insider_ownership_log_504d_base_v010_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(_insider_ownership_log(sharesownedfollowingtransaction), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesownedfollowingtransaction/assets mean
def iow_f89_insider_ownership_per_assets_63d_base_v011_signal(sharesownedfollowingtransaction, assets):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesownedfollowingtransaction/assets mean
def iow_f89_insider_ownership_per_assets_252d_base_v012_signal(sharesownedfollowingtransaction, assets):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesownedfollowingtransaction/assets mean
def iow_f89_insider_ownership_per_assets_504d_base_v013_signal(sharesownedfollowingtransaction, assets):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesownedfollowingtransaction/marketcap mean
def iow_f89_insider_ownership_per_marketcap_63d_base_v014_signal(sharesownedfollowingtransaction, marketcap):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesownedfollowingtransaction/marketcap mean
def iow_f89_insider_ownership_per_marketcap_252d_base_v015_signal(sharesownedfollowingtransaction, marketcap):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesownedfollowingtransaction/marketcap mean
def iow_f89_insider_ownership_per_marketcap_504d_base_v016_signal(sharesownedfollowingtransaction, marketcap):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesownedfollowingtransaction/equity mean
def iow_f89_insider_ownership_per_equity_63d_base_v017_signal(sharesownedfollowingtransaction, equity):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesownedfollowingtransaction/equity mean
def iow_f89_insider_ownership_per_equity_252d_base_v018_signal(sharesownedfollowingtransaction, equity):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesownedfollowingtransaction/equity mean
def iow_f89_insider_ownership_per_equity_504d_base_v019_signal(sharesownedfollowingtransaction, equity):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesownedfollowingtransaction/debt mean
def iow_f89_insider_ownership_per_debt_63d_base_v020_signal(sharesownedfollowingtransaction, debt):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesownedfollowingtransaction/debt mean
def iow_f89_insider_ownership_per_debt_252d_base_v021_signal(sharesownedfollowingtransaction, debt):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesownedfollowingtransaction/debt mean
def iow_f89_insider_ownership_per_debt_504d_base_v022_signal(sharesownedfollowingtransaction, debt):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesownedfollowingtransaction/revenue mean
def iow_f89_insider_ownership_per_revenue_63d_base_v023_signal(sharesownedfollowingtransaction, revenue):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesownedfollowingtransaction/revenue mean
def iow_f89_insider_ownership_per_revenue_252d_base_v024_signal(sharesownedfollowingtransaction, revenue):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesownedfollowingtransaction/revenue mean
def iow_f89_insider_ownership_per_revenue_504d_base_v025_signal(sharesownedfollowingtransaction, revenue):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sharesownedfollowingtransaction per share times closeadj
def iow_f89_insider_ownership_pershare_21d_base_v026_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    ps = _insider_ownership_per_share(sharesownedfollowingtransaction, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesownedfollowingtransaction per share times closeadj
def iow_f89_insider_ownership_pershare_63d_base_v027_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    ps = _insider_ownership_per_share(sharesownedfollowingtransaction, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sharesownedfollowingtransaction per share times closeadj
def iow_f89_insider_ownership_pershare_126d_base_v028_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    ps = _insider_ownership_per_share(sharesownedfollowingtransaction, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesownedfollowingtransaction per share times closeadj
def iow_f89_insider_ownership_pershare_252d_base_v029_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    ps = _insider_ownership_per_share(sharesownedfollowingtransaction, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sharesownedfollowingtransaction per share times closeadj
def iow_f89_insider_ownership_pershare_504d_base_v030_signal(sharesownedfollowingtransaction, sharesbas, closeadj):
    ps = _insider_ownership_per_share(sharesownedfollowingtransaction, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_std_63d_base_v031_signal(sharesownedfollowingtransaction, closeadj):
    result = _std(sharesownedfollowingtransaction, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_std_252d_base_v032_signal(sharesownedfollowingtransaction, closeadj):
    result = _std(sharesownedfollowingtransaction, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_std_504d_base_v033_signal(sharesownedfollowingtransaction, closeadj):
    result = _std(sharesownedfollowingtransaction, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of sharesownedfollowingtransaction
def iow_f89_insider_ownership_z_252d_base_v034_signal(sharesownedfollowingtransaction):
    result = _z(sharesownedfollowingtransaction, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of sharesownedfollowingtransaction
def iow_f89_insider_ownership_z_504d_base_v035_signal(sharesownedfollowingtransaction):
    result = _z(sharesownedfollowingtransaction, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(sharesownedfollowingtransaction)
def iow_f89_insider_ownership_logz_252d_base_v036_signal(sharesownedfollowingtransaction):
    result = _z(_insider_ownership_log(sharesownedfollowingtransaction), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(sharesownedfollowingtransaction)
def iow_f89_insider_ownership_logz_504d_base_v037_signal(sharesownedfollowingtransaction):
    result = _z(_insider_ownership_log(sharesownedfollowingtransaction), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sharesownedfollowingtransaction^2 times closeadj
def iow_f89_insider_ownership_sq_63d_base_v038_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sharesownedfollowingtransaction^2 times closeadj
def iow_f89_insider_ownership_sq_252d_base_v039_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(sharesownedfollowingtransaction * sharesownedfollowingtransaction, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(sharesownedfollowingtransaction) times closeadj
def iow_f89_insider_ownership_sign_21d_base_v040_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(np.sign(sharesownedfollowingtransaction), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(sharesownedfollowingtransaction) times closeadj
def iow_f89_insider_ownership_sign_63d_base_v041_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(np.sign(sharesownedfollowingtransaction), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(sharesownedfollowingtransaction) times closeadj
def iow_f89_insider_ownership_sign_252d_base_v042_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(np.sign(sharesownedfollowingtransaction), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesownedfollowingtransaction/opex mean
def iow_f89_insider_ownership_per_opex_63d_base_v043_signal(sharesownedfollowingtransaction, opex):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesownedfollowingtransaction/opex mean
def iow_f89_insider_ownership_per_opex_252d_base_v044_signal(sharesownedfollowingtransaction, opex):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesownedfollowingtransaction/ebitda mean
def iow_f89_insider_ownership_per_ebitda_63d_base_v045_signal(sharesownedfollowingtransaction, ebitda):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesownedfollowingtransaction/ebitda mean
def iow_f89_insider_ownership_per_ebitda_252d_base_v046_signal(sharesownedfollowingtransaction, ebitda):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesownedfollowingtransaction/capex mean
def iow_f89_insider_ownership_per_capex_63d_base_v047_signal(sharesownedfollowingtransaction, capex):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesownedfollowingtransaction/capex mean
def iow_f89_insider_ownership_per_capex_252d_base_v048_signal(sharesownedfollowingtransaction, capex):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sharesownedfollowingtransaction/liabilities mean
def iow_f89_insider_ownership_per_liabilities_63d_base_v049_signal(sharesownedfollowingtransaction, liabilities):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sharesownedfollowingtransaction/liabilities mean
def iow_f89_insider_ownership_per_liabilities_252d_base_v050_signal(sharesownedfollowingtransaction, liabilities):
    result = _mean(_insider_ownership_scaled(sharesownedfollowingtransaction, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# sharesownedfollowingtransaction relative to 252d max times closeadj
def iow_f89_insider_ownership_relmax_252d_base_v051_signal(sharesownedfollowingtransaction, closeadj):
    peak = sharesownedfollowingtransaction.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (sharesownedfollowingtransaction / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharesownedfollowingtransaction relative to 504d max times closeadj
def iow_f89_insider_ownership_relmax_504d_base_v052_signal(sharesownedfollowingtransaction, closeadj):
    peak = sharesownedfollowingtransaction.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (sharesownedfollowingtransaction / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharesownedfollowingtransaction relative to 252d min times closeadj
def iow_f89_insider_ownership_relmin_252d_base_v053_signal(sharesownedfollowingtransaction, closeadj):
    trough = sharesownedfollowingtransaction.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (sharesownedfollowingtransaction / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sharesownedfollowingtransaction relative to 504d min times closeadj
def iow_f89_insider_ownership_relmin_504d_base_v054_signal(sharesownedfollowingtransaction, closeadj):
    trough = sharesownedfollowingtransaction.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (sharesownedfollowingtransaction / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_pct_21d_base_v055_signal(sharesownedfollowingtransaction, closeadj):
    result = _pct_change(sharesownedfollowingtransaction, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_pct_63d_base_v056_signal(sharesownedfollowingtransaction, closeadj):
    result = _pct_change(sharesownedfollowingtransaction, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_pct_252d_base_v057_signal(sharesownedfollowingtransaction, closeadj):
    result = _pct_change(sharesownedfollowingtransaction, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_sum_63d_base_v058_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_sum_252d_base_v059_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_sum_504d_base_v060_signal(sharesownedfollowingtransaction, closeadj):
    result = sharesownedfollowingtransaction.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesownedfollowingtransaction(63d) / smoothed assets(252d) x closeadj
def iow_f89_insider_ownership_rom_assets_252_63d_base_v061_signal(sharesownedfollowingtransaction, assets, closeadj):
    n = _mean(sharesownedfollowingtransaction, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesownedfollowingtransaction(126d) / smoothed assets(504d) x closeadj
def iow_f89_insider_ownership_rom_assets_504_126d_base_v062_signal(sharesownedfollowingtransaction, assets, closeadj):
    n = _mean(sharesownedfollowingtransaction, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesownedfollowingtransaction(63d) / smoothed marketcap(252d) x closeadj
def iow_f89_insider_ownership_rom_marketcap_252_63d_base_v063_signal(sharesownedfollowingtransaction, marketcap, closeadj):
    n = _mean(sharesownedfollowingtransaction, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesownedfollowingtransaction(126d) / smoothed marketcap(504d) x closeadj
def iow_f89_insider_ownership_rom_marketcap_504_126d_base_v064_signal(sharesownedfollowingtransaction, marketcap, closeadj):
    n = _mean(sharesownedfollowingtransaction, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesownedfollowingtransaction(63d) / smoothed equity(252d) x closeadj
def iow_f89_insider_ownership_rom_equity_252_63d_base_v065_signal(sharesownedfollowingtransaction, equity, closeadj):
    n = _mean(sharesownedfollowingtransaction, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sharesownedfollowingtransaction(126d) / smoothed equity(504d) x closeadj
def iow_f89_insider_ownership_rom_equity_504_126d_base_v066_signal(sharesownedfollowingtransaction, equity, closeadj):
    n = _mean(sharesownedfollowingtransaction, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sharesownedfollowingtransaction) / std(assets)
def iow_f89_insider_ownership_volratio_assets_252d_base_v067_signal(sharesownedfollowingtransaction, assets):
    n = _std(sharesownedfollowingtransaction, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sharesownedfollowingtransaction) / std(assets)
def iow_f89_insider_ownership_volratio_assets_504d_base_v068_signal(sharesownedfollowingtransaction, assets):
    n = _std(sharesownedfollowingtransaction, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sharesownedfollowingtransaction) / std(marketcap)
def iow_f89_insider_ownership_volratio_marketcap_252d_base_v069_signal(sharesownedfollowingtransaction, marketcap):
    n = _std(sharesownedfollowingtransaction, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sharesownedfollowingtransaction) / std(marketcap)
def iow_f89_insider_ownership_volratio_marketcap_504d_base_v070_signal(sharesownedfollowingtransaction, marketcap):
    n = _std(sharesownedfollowingtransaction, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_raw_5d_base_v071_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(sharesownedfollowingtransaction, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed sharesownedfollowingtransaction times closeadj
def iow_f89_insider_ownership_raw_1008d_base_v072_signal(sharesownedfollowingtransaction, closeadj):
    result = _mean(sharesownedfollowingtransaction, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sharesownedfollowingtransaction/assets
def iow_f89_insider_ownership_log_per_assets_252d_base_v073_signal(sharesownedfollowingtransaction, assets):
    s = _insider_ownership_scaled(sharesownedfollowingtransaction, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of sharesownedfollowingtransaction/assets
def iow_f89_insider_ownership_log_per_assets_504d_base_v074_signal(sharesownedfollowingtransaction, assets):
    s = _insider_ownership_scaled(sharesownedfollowingtransaction, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sharesownedfollowingtransaction/marketcap
def iow_f89_insider_ownership_log_per_marketcap_252d_base_v075_signal(sharesownedfollowingtransaction, marketcap):
    s = _insider_ownership_scaled(sharesownedfollowingtransaction, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
