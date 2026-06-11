"""Family f50 - Net margin  (H_Margins) | base 001-075"""
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
def _net_margin_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _net_margin_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _net_margin_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed netmargin times closeadj
def nm_f50_net_margin_raw_21d_base_v001_signal(netmargin, closeadj):
    result = _mean(netmargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed netmargin times closeadj
def nm_f50_net_margin_raw_63d_base_v002_signal(netmargin, closeadj):
    result = _mean(netmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed netmargin times closeadj
def nm_f50_net_margin_raw_126d_base_v003_signal(netmargin, closeadj):
    result = _mean(netmargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed netmargin times closeadj
def nm_f50_net_margin_raw_252d_base_v004_signal(netmargin, closeadj):
    result = _mean(netmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed netmargin times closeadj
def nm_f50_net_margin_raw_504d_base_v005_signal(netmargin, closeadj):
    result = _mean(netmargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(netmargin) times closeadj
def nm_f50_net_margin_log_21d_base_v006_signal(netmargin, closeadj):
    result = _mean(_net_margin_log(netmargin), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(netmargin) times closeadj
def nm_f50_net_margin_log_63d_base_v007_signal(netmargin, closeadj):
    result = _mean(_net_margin_log(netmargin), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(netmargin) times closeadj
def nm_f50_net_margin_log_126d_base_v008_signal(netmargin, closeadj):
    result = _mean(_net_margin_log(netmargin), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(netmargin) times closeadj
def nm_f50_net_margin_log_252d_base_v009_signal(netmargin, closeadj):
    result = _mean(_net_margin_log(netmargin), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(netmargin) times closeadj
def nm_f50_net_margin_log_504d_base_v010_signal(netmargin, closeadj):
    result = _mean(_net_margin_log(netmargin), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netmargin/assets mean
def nm_f50_net_margin_per_assets_63d_base_v011_signal(netmargin, assets):
    result = _mean(_net_margin_scaled(netmargin, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netmargin/assets mean
def nm_f50_net_margin_per_assets_252d_base_v012_signal(netmargin, assets):
    result = _mean(_net_margin_scaled(netmargin, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d netmargin/assets mean
def nm_f50_net_margin_per_assets_504d_base_v013_signal(netmargin, assets):
    result = _mean(_net_margin_scaled(netmargin, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netmargin/marketcap mean
def nm_f50_net_margin_per_marketcap_63d_base_v014_signal(netmargin, marketcap):
    result = _mean(_net_margin_scaled(netmargin, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netmargin/marketcap mean
def nm_f50_net_margin_per_marketcap_252d_base_v015_signal(netmargin, marketcap):
    result = _mean(_net_margin_scaled(netmargin, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d netmargin/marketcap mean
def nm_f50_net_margin_per_marketcap_504d_base_v016_signal(netmargin, marketcap):
    result = _mean(_net_margin_scaled(netmargin, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netmargin/equity mean
def nm_f50_net_margin_per_equity_63d_base_v017_signal(netmargin, equity):
    result = _mean(_net_margin_scaled(netmargin, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netmargin/equity mean
def nm_f50_net_margin_per_equity_252d_base_v018_signal(netmargin, equity):
    result = _mean(_net_margin_scaled(netmargin, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d netmargin/equity mean
def nm_f50_net_margin_per_equity_504d_base_v019_signal(netmargin, equity):
    result = _mean(_net_margin_scaled(netmargin, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netmargin/debt mean
def nm_f50_net_margin_per_debt_63d_base_v020_signal(netmargin, debt):
    result = _mean(_net_margin_scaled(netmargin, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netmargin/debt mean
def nm_f50_net_margin_per_debt_252d_base_v021_signal(netmargin, debt):
    result = _mean(_net_margin_scaled(netmargin, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d netmargin/debt mean
def nm_f50_net_margin_per_debt_504d_base_v022_signal(netmargin, debt):
    result = _mean(_net_margin_scaled(netmargin, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netmargin/revenue mean
def nm_f50_net_margin_per_revenue_63d_base_v023_signal(netmargin, revenue):
    result = _mean(_net_margin_scaled(netmargin, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netmargin/revenue mean
def nm_f50_net_margin_per_revenue_252d_base_v024_signal(netmargin, revenue):
    result = _mean(_net_margin_scaled(netmargin, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d netmargin/revenue mean
def nm_f50_net_margin_per_revenue_504d_base_v025_signal(netmargin, revenue):
    result = _mean(_net_margin_scaled(netmargin, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d netmargin per share times closeadj
def nm_f50_net_margin_pershare_21d_base_v026_signal(netmargin, sharesbas, closeadj):
    ps = _net_margin_per_share(netmargin, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netmargin per share times closeadj
def nm_f50_net_margin_pershare_63d_base_v027_signal(netmargin, sharesbas, closeadj):
    ps = _net_margin_per_share(netmargin, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d netmargin per share times closeadj
def nm_f50_net_margin_pershare_126d_base_v028_signal(netmargin, sharesbas, closeadj):
    ps = _net_margin_per_share(netmargin, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netmargin per share times closeadj
def nm_f50_net_margin_pershare_252d_base_v029_signal(netmargin, sharesbas, closeadj):
    ps = _net_margin_per_share(netmargin, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d netmargin per share times closeadj
def nm_f50_net_margin_pershare_504d_base_v030_signal(netmargin, sharesbas, closeadj):
    ps = _net_margin_per_share(netmargin, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of netmargin times closeadj
def nm_f50_net_margin_std_63d_base_v031_signal(netmargin, closeadj):
    result = _std(netmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of netmargin times closeadj
def nm_f50_net_margin_std_252d_base_v032_signal(netmargin, closeadj):
    result = _std(netmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of netmargin times closeadj
def nm_f50_net_margin_std_504d_base_v033_signal(netmargin, closeadj):
    result = _std(netmargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of netmargin
def nm_f50_net_margin_z_252d_base_v034_signal(netmargin):
    result = _z(netmargin, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of netmargin
def nm_f50_net_margin_z_504d_base_v035_signal(netmargin):
    result = _z(netmargin, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(netmargin)
def nm_f50_net_margin_logz_252d_base_v036_signal(netmargin):
    result = _z(_net_margin_log(netmargin), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(netmargin)
def nm_f50_net_margin_logz_504d_base_v037_signal(netmargin):
    result = _z(_net_margin_log(netmargin), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of netmargin^2 times closeadj
def nm_f50_net_margin_sq_63d_base_v038_signal(netmargin, closeadj):
    result = _mean(netmargin * netmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of netmargin^2 times closeadj
def nm_f50_net_margin_sq_252d_base_v039_signal(netmargin, closeadj):
    result = _mean(netmargin * netmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(netmargin) times closeadj
def nm_f50_net_margin_sign_21d_base_v040_signal(netmargin, closeadj):
    result = _mean(np.sign(netmargin), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(netmargin) times closeadj
def nm_f50_net_margin_sign_63d_base_v041_signal(netmargin, closeadj):
    result = _mean(np.sign(netmargin), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(netmargin) times closeadj
def nm_f50_net_margin_sign_252d_base_v042_signal(netmargin, closeadj):
    result = _mean(np.sign(netmargin), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netmargin/opex mean
def nm_f50_net_margin_per_opex_63d_base_v043_signal(netmargin, opex):
    result = _mean(_net_margin_scaled(netmargin, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netmargin/opex mean
def nm_f50_net_margin_per_opex_252d_base_v044_signal(netmargin, opex):
    result = _mean(_net_margin_scaled(netmargin, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netmargin/ebitda mean
def nm_f50_net_margin_per_ebitda_63d_base_v045_signal(netmargin, ebitda):
    result = _mean(_net_margin_scaled(netmargin, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netmargin/ebitda mean
def nm_f50_net_margin_per_ebitda_252d_base_v046_signal(netmargin, ebitda):
    result = _mean(_net_margin_scaled(netmargin, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netmargin/capex mean
def nm_f50_net_margin_per_capex_63d_base_v047_signal(netmargin, capex):
    result = _mean(_net_margin_scaled(netmargin, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netmargin/capex mean
def nm_f50_net_margin_per_capex_252d_base_v048_signal(netmargin, capex):
    result = _mean(_net_margin_scaled(netmargin, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d netmargin/liabilities mean
def nm_f50_net_margin_per_liabilities_63d_base_v049_signal(netmargin, liabilities):
    result = _mean(_net_margin_scaled(netmargin, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d netmargin/liabilities mean
def nm_f50_net_margin_per_liabilities_252d_base_v050_signal(netmargin, liabilities):
    result = _mean(_net_margin_scaled(netmargin, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# netmargin relative to 252d max times closeadj
def nm_f50_net_margin_relmax_252d_base_v051_signal(netmargin, closeadj):
    peak = netmargin.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (netmargin / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# netmargin relative to 504d max times closeadj
def nm_f50_net_margin_relmax_504d_base_v052_signal(netmargin, closeadj):
    peak = netmargin.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (netmargin / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# netmargin relative to 252d min times closeadj
def nm_f50_net_margin_relmin_252d_base_v053_signal(netmargin, closeadj):
    trough = netmargin.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (netmargin / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# netmargin relative to 504d min times closeadj
def nm_f50_net_margin_relmin_504d_base_v054_signal(netmargin, closeadj):
    trough = netmargin.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (netmargin / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of netmargin times closeadj
def nm_f50_net_margin_pct_21d_base_v055_signal(netmargin, closeadj):
    result = _pct_change(netmargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of netmargin times closeadj
def nm_f50_net_margin_pct_63d_base_v056_signal(netmargin, closeadj):
    result = _pct_change(netmargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of netmargin times closeadj
def nm_f50_net_margin_pct_252d_base_v057_signal(netmargin, closeadj):
    result = _pct_change(netmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of netmargin times closeadj
def nm_f50_net_margin_sum_63d_base_v058_signal(netmargin, closeadj):
    result = netmargin.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of netmargin times closeadj
def nm_f50_net_margin_sum_252d_base_v059_signal(netmargin, closeadj):
    result = netmargin.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of netmargin times closeadj
def nm_f50_net_margin_sum_504d_base_v060_signal(netmargin, closeadj):
    result = netmargin.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed netmargin(63d) / smoothed assets(252d) x closeadj
def nm_f50_net_margin_rom_assets_252_63d_base_v061_signal(netmargin, assets, closeadj):
    n = _mean(netmargin, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed netmargin(126d) / smoothed assets(504d) x closeadj
def nm_f50_net_margin_rom_assets_504_126d_base_v062_signal(netmargin, assets, closeadj):
    n = _mean(netmargin, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed netmargin(63d) / smoothed marketcap(252d) x closeadj
def nm_f50_net_margin_rom_marketcap_252_63d_base_v063_signal(netmargin, marketcap, closeadj):
    n = _mean(netmargin, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed netmargin(126d) / smoothed marketcap(504d) x closeadj
def nm_f50_net_margin_rom_marketcap_504_126d_base_v064_signal(netmargin, marketcap, closeadj):
    n = _mean(netmargin, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed netmargin(63d) / smoothed equity(252d) x closeadj
def nm_f50_net_margin_rom_equity_252_63d_base_v065_signal(netmargin, equity, closeadj):
    n = _mean(netmargin, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed netmargin(126d) / smoothed equity(504d) x closeadj
def nm_f50_net_margin_rom_equity_504_126d_base_v066_signal(netmargin, equity, closeadj):
    n = _mean(netmargin, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(netmargin) / std(assets)
def nm_f50_net_margin_volratio_assets_252d_base_v067_signal(netmargin, assets):
    n = _std(netmargin, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(netmargin) / std(assets)
def nm_f50_net_margin_volratio_assets_504d_base_v068_signal(netmargin, assets):
    n = _std(netmargin, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(netmargin) / std(marketcap)
def nm_f50_net_margin_volratio_marketcap_252d_base_v069_signal(netmargin, marketcap):
    n = _std(netmargin, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(netmargin) / std(marketcap)
def nm_f50_net_margin_volratio_marketcap_504d_base_v070_signal(netmargin, marketcap):
    n = _std(netmargin, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed netmargin times closeadj
def nm_f50_net_margin_raw_5d_base_v071_signal(netmargin, closeadj):
    result = _mean(netmargin, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed netmargin times closeadj
def nm_f50_net_margin_raw_1008d_base_v072_signal(netmargin, closeadj):
    result = _mean(netmargin, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of netmargin/assets
def nm_f50_net_margin_log_per_assets_252d_base_v073_signal(netmargin, assets):
    s = _net_margin_scaled(netmargin, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of netmargin/assets
def nm_f50_net_margin_log_per_assets_504d_base_v074_signal(netmargin, assets):
    s = _net_margin_scaled(netmargin, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of netmargin/marketcap
def nm_f50_net_margin_log_per_marketcap_252d_base_v075_signal(netmargin, marketcap):
    s = _net_margin_scaled(netmargin, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
