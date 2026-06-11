"""Family f013 - Capex and manufacturing buildout (Cash Flow and Burn) | Sharadar tables: SF1 | fields: capex, ppnenet, assets, revenue | base 001-075"""
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
def _capex_and_manufacturing_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _capex_and_manufacturing_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _capex_and_manufacturing_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed capex times closeadj
def cam_f013_capex_and_manufacturing_raw_21d_base_v001_signal(capex, closeadj):
    result = _mean(capex, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed capex times closeadj
def cam_f013_capex_and_manufacturing_raw_63d_base_v002_signal(capex, closeadj):
    result = _mean(capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed capex times closeadj
def cam_f013_capex_and_manufacturing_raw_126d_base_v003_signal(capex, closeadj):
    result = _mean(capex, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed capex times closeadj
def cam_f013_capex_and_manufacturing_raw_252d_base_v004_signal(capex, closeadj):
    result = _mean(capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed capex times closeadj
def cam_f013_capex_and_manufacturing_raw_504d_base_v005_signal(capex, closeadj):
    result = _mean(capex, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(capex) times closeadj
def cam_f013_capex_and_manufacturing_log_21d_base_v006_signal(capex, closeadj):
    result = _mean(_capex_and_manufacturing_log(capex), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(capex) times closeadj
def cam_f013_capex_and_manufacturing_log_63d_base_v007_signal(capex, closeadj):
    result = _mean(_capex_and_manufacturing_log(capex), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(capex) times closeadj
def cam_f013_capex_and_manufacturing_log_126d_base_v008_signal(capex, closeadj):
    result = _mean(_capex_and_manufacturing_log(capex), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(capex) times closeadj
def cam_f013_capex_and_manufacturing_log_252d_base_v009_signal(capex, closeadj):
    result = _mean(_capex_and_manufacturing_log(capex), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(capex) times closeadj
def cam_f013_capex_and_manufacturing_log_504d_base_v010_signal(capex, closeadj):
    result = _mean(_capex_and_manufacturing_log(capex), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/ppnenet mean
def cam_f013_capex_and_manufacturing_per_ppnenet_63d_base_v011_signal(capex, ppnenet):
    result = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/ppnenet mean
def cam_f013_capex_and_manufacturing_per_ppnenet_252d_base_v012_signal(capex, ppnenet):
    result = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/ppnenet mean
def cam_f013_capex_and_manufacturing_per_ppnenet_504d_base_v013_signal(capex, ppnenet):
    result = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/assets mean
def cam_f013_capex_and_manufacturing_per_assets_63d_base_v014_signal(capex, assets):
    result = _mean(_capex_and_manufacturing_scaled(capex, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/assets mean
def cam_f013_capex_and_manufacturing_per_assets_252d_base_v015_signal(capex, assets):
    result = _mean(_capex_and_manufacturing_scaled(capex, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/assets mean
def cam_f013_capex_and_manufacturing_per_assets_504d_base_v016_signal(capex, assets):
    result = _mean(_capex_and_manufacturing_scaled(capex, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/revenue mean
def cam_f013_capex_and_manufacturing_per_revenue_63d_base_v017_signal(capex, revenue):
    result = _mean(_capex_and_manufacturing_scaled(capex, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/revenue mean
def cam_f013_capex_and_manufacturing_per_revenue_252d_base_v018_signal(capex, revenue):
    result = _mean(_capex_and_manufacturing_scaled(capex, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/revenue mean
def cam_f013_capex_and_manufacturing_per_revenue_504d_base_v019_signal(capex, revenue):
    result = _mean(_capex_and_manufacturing_scaled(capex, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/marketcap mean
def cam_f013_capex_and_manufacturing_per_marketcap_63d_base_v020_signal(capex, marketcap):
    result = _mean(_capex_and_manufacturing_scaled(capex, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/marketcap mean
def cam_f013_capex_and_manufacturing_per_marketcap_252d_base_v021_signal(capex, marketcap):
    result = _mean(_capex_and_manufacturing_scaled(capex, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/marketcap mean
def cam_f013_capex_and_manufacturing_per_marketcap_504d_base_v022_signal(capex, marketcap):
    result = _mean(_capex_and_manufacturing_scaled(capex, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/equity mean
def cam_f013_capex_and_manufacturing_per_equity_63d_base_v023_signal(capex, equity):
    result = _mean(_capex_and_manufacturing_scaled(capex, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/equity mean
def cam_f013_capex_and_manufacturing_per_equity_252d_base_v024_signal(capex, equity):
    result = _mean(_capex_and_manufacturing_scaled(capex, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/equity mean
def cam_f013_capex_and_manufacturing_per_equity_504d_base_v025_signal(capex, equity):
    result = _mean(_capex_and_manufacturing_scaled(capex, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex per share times closeadj
def cam_f013_capex_and_manufacturing_pershare_21d_base_v026_signal(capex, sharesbas, closeadj):
    ps = _capex_and_manufacturing_per_share(capex, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex per share times closeadj
def cam_f013_capex_and_manufacturing_pershare_63d_base_v027_signal(capex, sharesbas, closeadj):
    ps = _capex_and_manufacturing_per_share(capex, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d capex per share times closeadj
def cam_f013_capex_and_manufacturing_pershare_126d_base_v028_signal(capex, sharesbas, closeadj):
    ps = _capex_and_manufacturing_per_share(capex, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex per share times closeadj
def cam_f013_capex_and_manufacturing_pershare_252d_base_v029_signal(capex, sharesbas, closeadj):
    ps = _capex_and_manufacturing_per_share(capex, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex per share times closeadj
def cam_f013_capex_and_manufacturing_pershare_504d_base_v030_signal(capex, sharesbas, closeadj):
    ps = _capex_and_manufacturing_per_share(capex, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of capex times closeadj
def cam_f013_capex_and_manufacturing_std_63d_base_v031_signal(capex, closeadj):
    result = _std(capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of capex times closeadj
def cam_f013_capex_and_manufacturing_std_252d_base_v032_signal(capex, closeadj):
    result = _std(capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of capex times closeadj
def cam_f013_capex_and_manufacturing_std_504d_base_v033_signal(capex, closeadj):
    result = _std(capex, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of capex
def cam_f013_capex_and_manufacturing_z_252d_base_v034_signal(capex):
    result = _z(capex, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of capex
def cam_f013_capex_and_manufacturing_z_504d_base_v035_signal(capex):
    result = _z(capex, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(capex)
def cam_f013_capex_and_manufacturing_logz_252d_base_v036_signal(capex):
    result = _z(_capex_and_manufacturing_log(capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(capex)
def cam_f013_capex_and_manufacturing_logz_504d_base_v037_signal(capex):
    result = _z(_capex_and_manufacturing_log(capex), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of capex^2 times closeadj
def cam_f013_capex_and_manufacturing_sq_63d_base_v038_signal(capex, closeadj):
    result = _mean(capex * capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of capex^2 times closeadj
def cam_f013_capex_and_manufacturing_sq_252d_base_v039_signal(capex, closeadj):
    result = _mean(capex * capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(capex) times closeadj
def cam_f013_capex_and_manufacturing_sign_21d_base_v040_signal(capex, closeadj):
    result = _mean(np.sign(capex), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(capex) times closeadj
def cam_f013_capex_and_manufacturing_sign_63d_base_v041_signal(capex, closeadj):
    result = _mean(np.sign(capex), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(capex) times closeadj
def cam_f013_capex_and_manufacturing_sign_252d_base_v042_signal(capex, closeadj):
    result = _mean(np.sign(capex), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/opex mean
def cam_f013_capex_and_manufacturing_per_opex_63d_base_v043_signal(capex, opex):
    result = _mean(_capex_and_manufacturing_scaled(capex, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/opex mean
def cam_f013_capex_and_manufacturing_per_opex_252d_base_v044_signal(capex, opex):
    result = _mean(_capex_and_manufacturing_scaled(capex, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/ebitda mean
def cam_f013_capex_and_manufacturing_per_ebitda_63d_base_v045_signal(capex, ebitda):
    result = _mean(_capex_and_manufacturing_scaled(capex, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/ebitda mean
def cam_f013_capex_and_manufacturing_per_ebitda_252d_base_v046_signal(capex, ebitda):
    result = _mean(_capex_and_manufacturing_scaled(capex, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/capex mean
def cam_f013_capex_and_manufacturing_per_capex_63d_base_v047_signal(capex):
    result = _mean(_capex_and_manufacturing_scaled(capex, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/capex mean
def cam_f013_capex_and_manufacturing_per_capex_252d_base_v048_signal(capex):
    result = _mean(_capex_and_manufacturing_scaled(capex, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/liabilities mean
def cam_f013_capex_and_manufacturing_per_liabilities_63d_base_v049_signal(capex, liabilities):
    result = _mean(_capex_and_manufacturing_scaled(capex, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/liabilities mean
def cam_f013_capex_and_manufacturing_per_liabilities_252d_base_v050_signal(capex, liabilities):
    result = _mean(_capex_and_manufacturing_scaled(capex, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex relative to 252d max times closeadj
def cam_f013_capex_and_manufacturing_relmax_252d_base_v051_signal(capex, closeadj):
    peak = capex.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (capex / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex relative to 504d max times closeadj
def cam_f013_capex_and_manufacturing_relmax_504d_base_v052_signal(capex, closeadj):
    peak = capex.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (capex / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex relative to 252d min times closeadj
def cam_f013_capex_and_manufacturing_relmin_252d_base_v053_signal(capex, closeadj):
    trough = capex.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (capex / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex relative to 504d min times closeadj
def cam_f013_capex_and_manufacturing_relmin_504d_base_v054_signal(capex, closeadj):
    trough = capex.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (capex / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of capex times closeadj
def cam_f013_capex_and_manufacturing_pct_21d_base_v055_signal(capex, closeadj):
    result = _pct_change(capex, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of capex times closeadj
def cam_f013_capex_and_manufacturing_pct_63d_base_v056_signal(capex, closeadj):
    result = _pct_change(capex, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of capex times closeadj
def cam_f013_capex_and_manufacturing_pct_252d_base_v057_signal(capex, closeadj):
    result = _pct_change(capex, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of capex times closeadj
def cam_f013_capex_and_manufacturing_sum_63d_base_v058_signal(capex, closeadj):
    result = capex.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of capex times closeadj
def cam_f013_capex_and_manufacturing_sum_252d_base_v059_signal(capex, closeadj):
    result = capex.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of capex times closeadj
def cam_f013_capex_and_manufacturing_sum_504d_base_v060_signal(capex, closeadj):
    result = capex.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed capex(63d) / smoothed ppnenet(252d) x closeadj
def cam_f013_capex_and_manufacturing_rom_ppnenet_252_63d_base_v061_signal(capex, ppnenet, closeadj):
    n = _mean(capex, 63)
    d = _mean(ppnenet, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed capex(126d) / smoothed ppnenet(504d) x closeadj
def cam_f013_capex_and_manufacturing_rom_ppnenet_504_126d_base_v062_signal(capex, ppnenet, closeadj):
    n = _mean(capex, 126)
    d = _mean(ppnenet, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed capex(63d) / smoothed assets(252d) x closeadj
def cam_f013_capex_and_manufacturing_rom_assets_252_63d_base_v063_signal(capex, assets, closeadj):
    n = _mean(capex, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed capex(126d) / smoothed assets(504d) x closeadj
def cam_f013_capex_and_manufacturing_rom_assets_504_126d_base_v064_signal(capex, assets, closeadj):
    n = _mean(capex, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed capex(63d) / smoothed revenue(252d) x closeadj
def cam_f013_capex_and_manufacturing_rom_revenue_252_63d_base_v065_signal(capex, revenue, closeadj):
    n = _mean(capex, 63)
    d = _mean(revenue, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed capex(126d) / smoothed revenue(504d) x closeadj
def cam_f013_capex_and_manufacturing_rom_revenue_504_126d_base_v066_signal(capex, revenue, closeadj):
    n = _mean(capex, 126)
    d = _mean(revenue, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(capex) / std(ppnenet)
def cam_f013_capex_and_manufacturing_volratio_ppnenet_252d_base_v067_signal(capex, ppnenet):
    n = _std(capex, 252)
    d = _std(ppnenet, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(capex) / std(ppnenet)
def cam_f013_capex_and_manufacturing_volratio_ppnenet_504d_base_v068_signal(capex, ppnenet):
    n = _std(capex, 504)
    d = _std(ppnenet, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(capex) / std(assets)
def cam_f013_capex_and_manufacturing_volratio_assets_252d_base_v069_signal(capex, assets):
    n = _std(capex, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(capex) / std(assets)
def cam_f013_capex_and_manufacturing_volratio_assets_504d_base_v070_signal(capex, assets):
    n = _std(capex, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed capex times closeadj
def cam_f013_capex_and_manufacturing_raw_5d_base_v071_signal(capex, closeadj):
    result = _mean(capex, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed capex times closeadj
def cam_f013_capex_and_manufacturing_raw_1008d_base_v072_signal(capex, closeadj):
    result = _mean(capex, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of capex/ppnenet
def cam_f013_capex_and_manufacturing_log_per_ppnenet_252d_base_v073_signal(capex, ppnenet):
    s = _capex_and_manufacturing_scaled(capex, ppnenet)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of capex/ppnenet
def cam_f013_capex_and_manufacturing_log_per_ppnenet_504d_base_v074_signal(capex, ppnenet):
    s = _capex_and_manufacturing_scaled(capex, ppnenet)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of capex/assets
def cam_f013_capex_and_manufacturing_log_per_assets_252d_base_v075_signal(capex, assets):
    s = _capex_and_manufacturing_scaled(capex, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
