"""Family f60 - ROIC trend  (J_Returns_Efficiency) | base 001-075"""
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
def _roic_trend_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _roic_trend_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _roic_trend_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed roic times closeadj
def rt_f60_roic_trend_raw_21d_base_v001_signal(roic, closeadj):
    result = _mean(roic, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed roic times closeadj
def rt_f60_roic_trend_raw_63d_base_v002_signal(roic, closeadj):
    result = _mean(roic, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed roic times closeadj
def rt_f60_roic_trend_raw_126d_base_v003_signal(roic, closeadj):
    result = _mean(roic, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed roic times closeadj
def rt_f60_roic_trend_raw_252d_base_v004_signal(roic, closeadj):
    result = _mean(roic, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed roic times closeadj
def rt_f60_roic_trend_raw_504d_base_v005_signal(roic, closeadj):
    result = _mean(roic, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(roic) times closeadj
def rt_f60_roic_trend_log_21d_base_v006_signal(roic, closeadj):
    result = _mean(_roic_trend_log(roic), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(roic) times closeadj
def rt_f60_roic_trend_log_63d_base_v007_signal(roic, closeadj):
    result = _mean(_roic_trend_log(roic), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(roic) times closeadj
def rt_f60_roic_trend_log_126d_base_v008_signal(roic, closeadj):
    result = _mean(_roic_trend_log(roic), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(roic) times closeadj
def rt_f60_roic_trend_log_252d_base_v009_signal(roic, closeadj):
    result = _mean(_roic_trend_log(roic), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(roic) times closeadj
def rt_f60_roic_trend_log_504d_base_v010_signal(roic, closeadj):
    result = _mean(_roic_trend_log(roic), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roic/assets mean
def rt_f60_roic_trend_per_assets_63d_base_v011_signal(roic, assets):
    result = _mean(_roic_trend_scaled(roic, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic/assets mean
def rt_f60_roic_trend_per_assets_252d_base_v012_signal(roic, assets):
    result = _mean(_roic_trend_scaled(roic, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roic/assets mean
def rt_f60_roic_trend_per_assets_504d_base_v013_signal(roic, assets):
    result = _mean(_roic_trend_scaled(roic, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roic/marketcap mean
def rt_f60_roic_trend_per_marketcap_63d_base_v014_signal(roic, marketcap):
    result = _mean(_roic_trend_scaled(roic, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic/marketcap mean
def rt_f60_roic_trend_per_marketcap_252d_base_v015_signal(roic, marketcap):
    result = _mean(_roic_trend_scaled(roic, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roic/marketcap mean
def rt_f60_roic_trend_per_marketcap_504d_base_v016_signal(roic, marketcap):
    result = _mean(_roic_trend_scaled(roic, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roic/equity mean
def rt_f60_roic_trend_per_equity_63d_base_v017_signal(roic, equity):
    result = _mean(_roic_trend_scaled(roic, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic/equity mean
def rt_f60_roic_trend_per_equity_252d_base_v018_signal(roic, equity):
    result = _mean(_roic_trend_scaled(roic, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roic/equity mean
def rt_f60_roic_trend_per_equity_504d_base_v019_signal(roic, equity):
    result = _mean(_roic_trend_scaled(roic, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roic/debt mean
def rt_f60_roic_trend_per_debt_63d_base_v020_signal(roic, debt):
    result = _mean(_roic_trend_scaled(roic, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic/debt mean
def rt_f60_roic_trend_per_debt_252d_base_v021_signal(roic, debt):
    result = _mean(_roic_trend_scaled(roic, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roic/debt mean
def rt_f60_roic_trend_per_debt_504d_base_v022_signal(roic, debt):
    result = _mean(_roic_trend_scaled(roic, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roic/revenue mean
def rt_f60_roic_trend_per_revenue_63d_base_v023_signal(roic, revenue):
    result = _mean(_roic_trend_scaled(roic, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic/revenue mean
def rt_f60_roic_trend_per_revenue_252d_base_v024_signal(roic, revenue):
    result = _mean(_roic_trend_scaled(roic, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roic/revenue mean
def rt_f60_roic_trend_per_revenue_504d_base_v025_signal(roic, revenue):
    result = _mean(_roic_trend_scaled(roic, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d roic per share times closeadj
def rt_f60_roic_trend_pershare_21d_base_v026_signal(roic, sharesbas, closeadj):
    ps = _roic_trend_per_share(roic, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roic per share times closeadj
def rt_f60_roic_trend_pershare_63d_base_v027_signal(roic, sharesbas, closeadj):
    ps = _roic_trend_per_share(roic, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d roic per share times closeadj
def rt_f60_roic_trend_pershare_126d_base_v028_signal(roic, sharesbas, closeadj):
    ps = _roic_trend_per_share(roic, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic per share times closeadj
def rt_f60_roic_trend_pershare_252d_base_v029_signal(roic, sharesbas, closeadj):
    ps = _roic_trend_per_share(roic, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d roic per share times closeadj
def rt_f60_roic_trend_pershare_504d_base_v030_signal(roic, sharesbas, closeadj):
    ps = _roic_trend_per_share(roic, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of roic times closeadj
def rt_f60_roic_trend_std_63d_base_v031_signal(roic, closeadj):
    result = _std(roic, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of roic times closeadj
def rt_f60_roic_trend_std_252d_base_v032_signal(roic, closeadj):
    result = _std(roic, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of roic times closeadj
def rt_f60_roic_trend_std_504d_base_v033_signal(roic, closeadj):
    result = _std(roic, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of roic
def rt_f60_roic_trend_z_252d_base_v034_signal(roic):
    result = _z(roic, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of roic
def rt_f60_roic_trend_z_504d_base_v035_signal(roic):
    result = _z(roic, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(roic)
def rt_f60_roic_trend_logz_252d_base_v036_signal(roic):
    result = _z(_roic_trend_log(roic), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(roic)
def rt_f60_roic_trend_logz_504d_base_v037_signal(roic):
    result = _z(_roic_trend_log(roic), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of roic^2 times closeadj
def rt_f60_roic_trend_sq_63d_base_v038_signal(roic, closeadj):
    result = _mean(roic * roic, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of roic^2 times closeadj
def rt_f60_roic_trend_sq_252d_base_v039_signal(roic, closeadj):
    result = _mean(roic * roic, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(roic) times closeadj
def rt_f60_roic_trend_sign_21d_base_v040_signal(roic, closeadj):
    result = _mean(np.sign(roic), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(roic) times closeadj
def rt_f60_roic_trend_sign_63d_base_v041_signal(roic, closeadj):
    result = _mean(np.sign(roic), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(roic) times closeadj
def rt_f60_roic_trend_sign_252d_base_v042_signal(roic, closeadj):
    result = _mean(np.sign(roic), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roic/opex mean
def rt_f60_roic_trend_per_opex_63d_base_v043_signal(roic, opex):
    result = _mean(_roic_trend_scaled(roic, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic/opex mean
def rt_f60_roic_trend_per_opex_252d_base_v044_signal(roic, opex):
    result = _mean(_roic_trend_scaled(roic, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roic/ebitda mean
def rt_f60_roic_trend_per_ebitda_63d_base_v045_signal(roic, ebitda):
    result = _mean(_roic_trend_scaled(roic, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic/ebitda mean
def rt_f60_roic_trend_per_ebitda_252d_base_v046_signal(roic, ebitda):
    result = _mean(_roic_trend_scaled(roic, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roic/capex mean
def rt_f60_roic_trend_per_capex_63d_base_v047_signal(roic, capex):
    result = _mean(_roic_trend_scaled(roic, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic/capex mean
def rt_f60_roic_trend_per_capex_252d_base_v048_signal(roic, capex):
    result = _mean(_roic_trend_scaled(roic, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roic/liabilities mean
def rt_f60_roic_trend_per_liabilities_63d_base_v049_signal(roic, liabilities):
    result = _mean(_roic_trend_scaled(roic, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roic/liabilities mean
def rt_f60_roic_trend_per_liabilities_252d_base_v050_signal(roic, liabilities):
    result = _mean(_roic_trend_scaled(roic, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# roic relative to 252d max times closeadj
def rt_f60_roic_trend_relmax_252d_base_v051_signal(roic, closeadj):
    peak = roic.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (roic / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roic relative to 504d max times closeadj
def rt_f60_roic_trend_relmax_504d_base_v052_signal(roic, closeadj):
    peak = roic.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (roic / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roic relative to 252d min times closeadj
def rt_f60_roic_trend_relmin_252d_base_v053_signal(roic, closeadj):
    trough = roic.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (roic / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# roic relative to 504d min times closeadj
def rt_f60_roic_trend_relmin_504d_base_v054_signal(roic, closeadj):
    trough = roic.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (roic / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of roic times closeadj
def rt_f60_roic_trend_pct_21d_base_v055_signal(roic, closeadj):
    result = _pct_change(roic, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of roic times closeadj
def rt_f60_roic_trend_pct_63d_base_v056_signal(roic, closeadj):
    result = _pct_change(roic, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of roic times closeadj
def rt_f60_roic_trend_pct_252d_base_v057_signal(roic, closeadj):
    result = _pct_change(roic, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of roic times closeadj
def rt_f60_roic_trend_sum_63d_base_v058_signal(roic, closeadj):
    result = roic.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of roic times closeadj
def rt_f60_roic_trend_sum_252d_base_v059_signal(roic, closeadj):
    result = roic.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of roic times closeadj
def rt_f60_roic_trend_sum_504d_base_v060_signal(roic, closeadj):
    result = roic.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roic(63d) / smoothed assets(252d) x closeadj
def rt_f60_roic_trend_rom_assets_252_63d_base_v061_signal(roic, assets, closeadj):
    n = _mean(roic, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roic(126d) / smoothed assets(504d) x closeadj
def rt_f60_roic_trend_rom_assets_504_126d_base_v062_signal(roic, assets, closeadj):
    n = _mean(roic, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roic(63d) / smoothed marketcap(252d) x closeadj
def rt_f60_roic_trend_rom_marketcap_252_63d_base_v063_signal(roic, marketcap, closeadj):
    n = _mean(roic, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roic(126d) / smoothed marketcap(504d) x closeadj
def rt_f60_roic_trend_rom_marketcap_504_126d_base_v064_signal(roic, marketcap, closeadj):
    n = _mean(roic, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roic(63d) / smoothed equity(252d) x closeadj
def rt_f60_roic_trend_rom_equity_252_63d_base_v065_signal(roic, equity, closeadj):
    n = _mean(roic, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed roic(126d) / smoothed equity(504d) x closeadj
def rt_f60_roic_trend_rom_equity_504_126d_base_v066_signal(roic, equity, closeadj):
    n = _mean(roic, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(roic) / std(assets)
def rt_f60_roic_trend_volratio_assets_252d_base_v067_signal(roic, assets):
    n = _std(roic, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(roic) / std(assets)
def rt_f60_roic_trend_volratio_assets_504d_base_v068_signal(roic, assets):
    n = _std(roic, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(roic) / std(marketcap)
def rt_f60_roic_trend_volratio_marketcap_252d_base_v069_signal(roic, marketcap):
    n = _std(roic, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(roic) / std(marketcap)
def rt_f60_roic_trend_volratio_marketcap_504d_base_v070_signal(roic, marketcap):
    n = _std(roic, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed roic times closeadj
def rt_f60_roic_trend_raw_5d_base_v071_signal(roic, closeadj):
    result = _mean(roic, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed roic times closeadj
def rt_f60_roic_trend_raw_1008d_base_v072_signal(roic, closeadj):
    result = _mean(roic, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of roic/assets
def rt_f60_roic_trend_log_per_assets_252d_base_v073_signal(roic, assets):
    s = _roic_trend_scaled(roic, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of roic/assets
def rt_f60_roic_trend_log_per_assets_504d_base_v074_signal(roic, assets):
    s = _roic_trend_scaled(roic, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of roic/marketcap
def rt_f60_roic_trend_log_per_marketcap_252d_base_v075_signal(roic, marketcap):
    s = _roic_trend_scaled(roic, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
