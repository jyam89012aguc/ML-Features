"""Family f046 - Revenue scale (Revenue and Commercialization) | Sharadar tables: SF1 | fields: revenue, revenueusd, sps | base 001-075"""
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
def _revenue_level_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _revenue_level_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _revenue_level_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed revenue times closeadj
def rl_f046_revenue_level_raw_21d_base_v001_signal(revenue, closeadj):
    result = _mean(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed revenue times closeadj
def rl_f046_revenue_level_raw_63d_base_v002_signal(revenue, closeadj):
    result = _mean(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed revenue times closeadj
def rl_f046_revenue_level_raw_126d_base_v003_signal(revenue, closeadj):
    result = _mean(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed revenue times closeadj
def rl_f046_revenue_level_raw_252d_base_v004_signal(revenue, closeadj):
    result = _mean(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed revenue times closeadj
def rl_f046_revenue_level_raw_504d_base_v005_signal(revenue, closeadj):
    result = _mean(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(revenue) times closeadj
def rl_f046_revenue_level_log_21d_base_v006_signal(revenue, closeadj):
    result = _mean(_revenue_level_log(revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(revenue) times closeadj
def rl_f046_revenue_level_log_63d_base_v007_signal(revenue, closeadj):
    result = _mean(_revenue_level_log(revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(revenue) times closeadj
def rl_f046_revenue_level_log_126d_base_v008_signal(revenue, closeadj):
    result = _mean(_revenue_level_log(revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(revenue) times closeadj
def rl_f046_revenue_level_log_252d_base_v009_signal(revenue, closeadj):
    result = _mean(_revenue_level_log(revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(revenue) times closeadj
def rl_f046_revenue_level_log_504d_base_v010_signal(revenue, closeadj):
    result = _mean(_revenue_level_log(revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/revenueusd mean
def rl_f046_revenue_level_per_revenueusd_63d_base_v011_signal(revenue, revenueusd):
    result = _mean(_revenue_level_scaled(revenue, revenueusd), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/revenueusd mean
def rl_f046_revenue_level_per_revenueusd_252d_base_v012_signal(revenue, revenueusd):
    result = _mean(_revenue_level_scaled(revenue, revenueusd), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue/revenueusd mean
def rl_f046_revenue_level_per_revenueusd_504d_base_v013_signal(revenue, revenueusd):
    result = _mean(_revenue_level_scaled(revenue, revenueusd), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/sps mean
def rl_f046_revenue_level_per_sps_63d_base_v014_signal(revenue, sps):
    result = _mean(_revenue_level_scaled(revenue, sps), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/sps mean
def rl_f046_revenue_level_per_sps_252d_base_v015_signal(revenue, sps):
    result = _mean(_revenue_level_scaled(revenue, sps), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue/sps mean
def rl_f046_revenue_level_per_sps_504d_base_v016_signal(revenue, sps):
    result = _mean(_revenue_level_scaled(revenue, sps), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/assets mean
def rl_f046_revenue_level_per_assets_63d_base_v017_signal(revenue, assets):
    result = _mean(_revenue_level_scaled(revenue, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/assets mean
def rl_f046_revenue_level_per_assets_252d_base_v018_signal(revenue, assets):
    result = _mean(_revenue_level_scaled(revenue, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue/assets mean
def rl_f046_revenue_level_per_assets_504d_base_v019_signal(revenue, assets):
    result = _mean(_revenue_level_scaled(revenue, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/marketcap mean
def rl_f046_revenue_level_per_marketcap_63d_base_v020_signal(revenue, marketcap):
    result = _mean(_revenue_level_scaled(revenue, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/marketcap mean
def rl_f046_revenue_level_per_marketcap_252d_base_v021_signal(revenue, marketcap):
    result = _mean(_revenue_level_scaled(revenue, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue/marketcap mean
def rl_f046_revenue_level_per_marketcap_504d_base_v022_signal(revenue, marketcap):
    result = _mean(_revenue_level_scaled(revenue, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/equity mean
def rl_f046_revenue_level_per_equity_63d_base_v023_signal(revenue, equity):
    result = _mean(_revenue_level_scaled(revenue, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/equity mean
def rl_f046_revenue_level_per_equity_252d_base_v024_signal(revenue, equity):
    result = _mean(_revenue_level_scaled(revenue, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue/equity mean
def rl_f046_revenue_level_per_equity_504d_base_v025_signal(revenue, equity):
    result = _mean(_revenue_level_scaled(revenue, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue per share times closeadj
def rl_f046_revenue_level_pershare_21d_base_v026_signal(revenue, sharesbas, closeadj):
    ps = _revenue_level_per_share(revenue, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue per share times closeadj
def rl_f046_revenue_level_pershare_63d_base_v027_signal(revenue, sharesbas, closeadj):
    ps = _revenue_level_per_share(revenue, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d revenue per share times closeadj
def rl_f046_revenue_level_pershare_126d_base_v028_signal(revenue, sharesbas, closeadj):
    ps = _revenue_level_per_share(revenue, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue per share times closeadj
def rl_f046_revenue_level_pershare_252d_base_v029_signal(revenue, sharesbas, closeadj):
    ps = _revenue_level_per_share(revenue, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue per share times closeadj
def rl_f046_revenue_level_pershare_504d_base_v030_signal(revenue, sharesbas, closeadj):
    ps = _revenue_level_per_share(revenue, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of revenue times closeadj
def rl_f046_revenue_level_std_63d_base_v031_signal(revenue, closeadj):
    result = _std(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of revenue times closeadj
def rl_f046_revenue_level_std_252d_base_v032_signal(revenue, closeadj):
    result = _std(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of revenue times closeadj
def rl_f046_revenue_level_std_504d_base_v033_signal(revenue, closeadj):
    result = _std(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of revenue
def rl_f046_revenue_level_z_252d_base_v034_signal(revenue):
    result = _z(revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of revenue
def rl_f046_revenue_level_z_504d_base_v035_signal(revenue):
    result = _z(revenue, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(revenue)
def rl_f046_revenue_level_logz_252d_base_v036_signal(revenue):
    result = _z(_revenue_level_log(revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(revenue)
def rl_f046_revenue_level_logz_504d_base_v037_signal(revenue):
    result = _z(_revenue_level_log(revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of revenue^2 times closeadj
def rl_f046_revenue_level_sq_63d_base_v038_signal(revenue, closeadj):
    result = _mean(revenue * revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of revenue^2 times closeadj
def rl_f046_revenue_level_sq_252d_base_v039_signal(revenue, closeadj):
    result = _mean(revenue * revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(revenue) times closeadj
def rl_f046_revenue_level_sign_21d_base_v040_signal(revenue, closeadj):
    result = _mean(np.sign(revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(revenue) times closeadj
def rl_f046_revenue_level_sign_63d_base_v041_signal(revenue, closeadj):
    result = _mean(np.sign(revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(revenue) times closeadj
def rl_f046_revenue_level_sign_252d_base_v042_signal(revenue, closeadj):
    result = _mean(np.sign(revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/opex mean
def rl_f046_revenue_level_per_opex_63d_base_v043_signal(revenue, opex):
    result = _mean(_revenue_level_scaled(revenue, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/opex mean
def rl_f046_revenue_level_per_opex_252d_base_v044_signal(revenue, opex):
    result = _mean(_revenue_level_scaled(revenue, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/ebitda mean
def rl_f046_revenue_level_per_ebitda_63d_base_v045_signal(revenue, ebitda):
    result = _mean(_revenue_level_scaled(revenue, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/ebitda mean
def rl_f046_revenue_level_per_ebitda_252d_base_v046_signal(revenue, ebitda):
    result = _mean(_revenue_level_scaled(revenue, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/capex mean
def rl_f046_revenue_level_per_capex_63d_base_v047_signal(revenue, capex):
    result = _mean(_revenue_level_scaled(revenue, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/capex mean
def rl_f046_revenue_level_per_capex_252d_base_v048_signal(revenue, capex):
    result = _mean(_revenue_level_scaled(revenue, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue/liabilities mean
def rl_f046_revenue_level_per_liabilities_63d_base_v049_signal(revenue, liabilities):
    result = _mean(_revenue_level_scaled(revenue, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue/liabilities mean
def rl_f046_revenue_level_per_liabilities_252d_base_v050_signal(revenue, liabilities):
    result = _mean(_revenue_level_scaled(revenue, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue relative to 252d max times closeadj
def rl_f046_revenue_level_relmax_252d_base_v051_signal(revenue, closeadj):
    peak = revenue.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (revenue / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue relative to 504d max times closeadj
def rl_f046_revenue_level_relmax_504d_base_v052_signal(revenue, closeadj):
    peak = revenue.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (revenue / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue relative to 252d min times closeadj
def rl_f046_revenue_level_relmin_252d_base_v053_signal(revenue, closeadj):
    trough = revenue.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (revenue / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revenue relative to 504d min times closeadj
def rl_f046_revenue_level_relmin_504d_base_v054_signal(revenue, closeadj):
    trough = revenue.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (revenue / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of revenue times closeadj
def rl_f046_revenue_level_pct_21d_base_v055_signal(revenue, closeadj):
    result = _pct_change(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of revenue times closeadj
def rl_f046_revenue_level_pct_63d_base_v056_signal(revenue, closeadj):
    result = _pct_change(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of revenue times closeadj
def rl_f046_revenue_level_pct_252d_base_v057_signal(revenue, closeadj):
    result = _pct_change(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of revenue times closeadj
def rl_f046_revenue_level_sum_63d_base_v058_signal(revenue, closeadj):
    result = revenue.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of revenue times closeadj
def rl_f046_revenue_level_sum_252d_base_v059_signal(revenue, closeadj):
    result = revenue.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of revenue times closeadj
def rl_f046_revenue_level_sum_504d_base_v060_signal(revenue, closeadj):
    result = revenue.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue(63d) / smoothed revenueusd(252d) x closeadj
def rl_f046_revenue_level_rom_revenueusd_252_63d_base_v061_signal(revenue, revenueusd, closeadj):
    n = _mean(revenue, 63)
    d = _mean(revenueusd, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue(126d) / smoothed revenueusd(504d) x closeadj
def rl_f046_revenue_level_rom_revenueusd_504_126d_base_v062_signal(revenue, revenueusd, closeadj):
    n = _mean(revenue, 126)
    d = _mean(revenueusd, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue(63d) / smoothed sps(252d) x closeadj
def rl_f046_revenue_level_rom_sps_252_63d_base_v063_signal(revenue, sps, closeadj):
    n = _mean(revenue, 63)
    d = _mean(sps, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue(126d) / smoothed sps(504d) x closeadj
def rl_f046_revenue_level_rom_sps_504_126d_base_v064_signal(revenue, sps, closeadj):
    n = _mean(revenue, 126)
    d = _mean(sps, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue(63d) / smoothed assets(252d) x closeadj
def rl_f046_revenue_level_rom_assets_252_63d_base_v065_signal(revenue, assets, closeadj):
    n = _mean(revenue, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revenue(126d) / smoothed assets(504d) x closeadj
def rl_f046_revenue_level_rom_assets_504_126d_base_v066_signal(revenue, assets, closeadj):
    n = _mean(revenue, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(revenue) / std(revenueusd)
def rl_f046_revenue_level_volratio_revenueusd_252d_base_v067_signal(revenue, revenueusd):
    n = _std(revenue, 252)
    d = _std(revenueusd, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(revenue) / std(revenueusd)
def rl_f046_revenue_level_volratio_revenueusd_504d_base_v068_signal(revenue, revenueusd):
    n = _std(revenue, 504)
    d = _std(revenueusd, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(revenue) / std(sps)
def rl_f046_revenue_level_volratio_sps_252d_base_v069_signal(revenue, sps):
    n = _std(revenue, 252)
    d = _std(sps, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(revenue) / std(sps)
def rl_f046_revenue_level_volratio_sps_504d_base_v070_signal(revenue, sps):
    n = _std(revenue, 504)
    d = _std(sps, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed revenue times closeadj
def rl_f046_revenue_level_raw_5d_base_v071_signal(revenue, closeadj):
    result = _mean(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed revenue times closeadj
def rl_f046_revenue_level_raw_1008d_base_v072_signal(revenue, closeadj):
    result = _mean(revenue, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of revenue/revenueusd
def rl_f046_revenue_level_log_per_revenueusd_252d_base_v073_signal(revenue, revenueusd):
    s = _revenue_level_scaled(revenue, revenueusd)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of revenue/revenueusd
def rl_f046_revenue_level_log_per_revenueusd_504d_base_v074_signal(revenue, revenueusd):
    s = _revenue_level_scaled(revenue, revenueusd)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of revenue/sps
def rl_f046_revenue_level_log_per_sps_252d_base_v075_signal(revenue, sps):
    s = _revenue_level_scaled(revenue, sps)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
