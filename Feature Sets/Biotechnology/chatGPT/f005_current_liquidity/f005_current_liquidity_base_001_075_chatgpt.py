"""Family f005 - Current liquidity coverage (Liquidity and Runway) | Sharadar tables: SF1 | fields: currentratio, assetsc, liabilitiesc, cashneq | base 001-075"""
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
def _current_liquidity_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _current_liquidity_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _current_liquidity_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed currentratio times closeadj
def cl_f005_current_liquidity_raw_21d_base_v001_signal(currentratio, closeadj):
    result = _mean(currentratio, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed currentratio times closeadj
def cl_f005_current_liquidity_raw_63d_base_v002_signal(currentratio, closeadj):
    result = _mean(currentratio, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed currentratio times closeadj
def cl_f005_current_liquidity_raw_126d_base_v003_signal(currentratio, closeadj):
    result = _mean(currentratio, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed currentratio times closeadj
def cl_f005_current_liquidity_raw_252d_base_v004_signal(currentratio, closeadj):
    result = _mean(currentratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed currentratio times closeadj
def cl_f005_current_liquidity_raw_504d_base_v005_signal(currentratio, closeadj):
    result = _mean(currentratio, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(currentratio) times closeadj
def cl_f005_current_liquidity_log_21d_base_v006_signal(currentratio, closeadj):
    result = _mean(_current_liquidity_log(currentratio), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(currentratio) times closeadj
def cl_f005_current_liquidity_log_63d_base_v007_signal(currentratio, closeadj):
    result = _mean(_current_liquidity_log(currentratio), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(currentratio) times closeadj
def cl_f005_current_liquidity_log_126d_base_v008_signal(currentratio, closeadj):
    result = _mean(_current_liquidity_log(currentratio), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(currentratio) times closeadj
def cl_f005_current_liquidity_log_252d_base_v009_signal(currentratio, closeadj):
    result = _mean(_current_liquidity_log(currentratio), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(currentratio) times closeadj
def cl_f005_current_liquidity_log_504d_base_v010_signal(currentratio, closeadj):
    result = _mean(_current_liquidity_log(currentratio), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d currentratio/assetsc mean
def cl_f005_current_liquidity_per_assetsc_63d_base_v011_signal(currentratio, assetsc):
    result = _mean(_current_liquidity_scaled(currentratio, assetsc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d currentratio/assetsc mean
def cl_f005_current_liquidity_per_assetsc_252d_base_v012_signal(currentratio, assetsc):
    result = _mean(_current_liquidity_scaled(currentratio, assetsc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d currentratio/assetsc mean
def cl_f005_current_liquidity_per_assetsc_504d_base_v013_signal(currentratio, assetsc):
    result = _mean(_current_liquidity_scaled(currentratio, assetsc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d currentratio/liabilitiesc mean
def cl_f005_current_liquidity_per_liabilitiesc_63d_base_v014_signal(currentratio, liabilitiesc):
    result = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d currentratio/liabilitiesc mean
def cl_f005_current_liquidity_per_liabilitiesc_252d_base_v015_signal(currentratio, liabilitiesc):
    result = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d currentratio/liabilitiesc mean
def cl_f005_current_liquidity_per_liabilitiesc_504d_base_v016_signal(currentratio, liabilitiesc):
    result = _mean(_current_liquidity_scaled(currentratio, liabilitiesc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d currentratio/cashneq mean
def cl_f005_current_liquidity_per_cashneq_63d_base_v017_signal(currentratio, cashneq):
    result = _mean(_current_liquidity_scaled(currentratio, cashneq), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d currentratio/cashneq mean
def cl_f005_current_liquidity_per_cashneq_252d_base_v018_signal(currentratio, cashneq):
    result = _mean(_current_liquidity_scaled(currentratio, cashneq), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d currentratio/cashneq mean
def cl_f005_current_liquidity_per_cashneq_504d_base_v019_signal(currentratio, cashneq):
    result = _mean(_current_liquidity_scaled(currentratio, cashneq), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d currentratio/assets mean
def cl_f005_current_liquidity_per_assets_63d_base_v020_signal(currentratio, assets):
    result = _mean(_current_liquidity_scaled(currentratio, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d currentratio/assets mean
def cl_f005_current_liquidity_per_assets_252d_base_v021_signal(currentratio, assets):
    result = _mean(_current_liquidity_scaled(currentratio, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d currentratio/assets mean
def cl_f005_current_liquidity_per_assets_504d_base_v022_signal(currentratio, assets):
    result = _mean(_current_liquidity_scaled(currentratio, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d currentratio/marketcap mean
def cl_f005_current_liquidity_per_marketcap_63d_base_v023_signal(currentratio, marketcap):
    result = _mean(_current_liquidity_scaled(currentratio, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d currentratio/marketcap mean
def cl_f005_current_liquidity_per_marketcap_252d_base_v024_signal(currentratio, marketcap):
    result = _mean(_current_liquidity_scaled(currentratio, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d currentratio/marketcap mean
def cl_f005_current_liquidity_per_marketcap_504d_base_v025_signal(currentratio, marketcap):
    result = _mean(_current_liquidity_scaled(currentratio, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d currentratio per share times closeadj
def cl_f005_current_liquidity_pershare_21d_base_v026_signal(currentratio, sharesbas, closeadj):
    ps = _current_liquidity_per_share(currentratio, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d currentratio per share times closeadj
def cl_f005_current_liquidity_pershare_63d_base_v027_signal(currentratio, sharesbas, closeadj):
    ps = _current_liquidity_per_share(currentratio, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d currentratio per share times closeadj
def cl_f005_current_liquidity_pershare_126d_base_v028_signal(currentratio, sharesbas, closeadj):
    ps = _current_liquidity_per_share(currentratio, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d currentratio per share times closeadj
def cl_f005_current_liquidity_pershare_252d_base_v029_signal(currentratio, sharesbas, closeadj):
    ps = _current_liquidity_per_share(currentratio, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d currentratio per share times closeadj
def cl_f005_current_liquidity_pershare_504d_base_v030_signal(currentratio, sharesbas, closeadj):
    ps = _current_liquidity_per_share(currentratio, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of currentratio times closeadj
def cl_f005_current_liquidity_std_63d_base_v031_signal(currentratio, closeadj):
    result = _std(currentratio, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of currentratio times closeadj
def cl_f005_current_liquidity_std_252d_base_v032_signal(currentratio, closeadj):
    result = _std(currentratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of currentratio times closeadj
def cl_f005_current_liquidity_std_504d_base_v033_signal(currentratio, closeadj):
    result = _std(currentratio, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of currentratio
def cl_f005_current_liquidity_z_252d_base_v034_signal(currentratio):
    result = _z(currentratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of currentratio
def cl_f005_current_liquidity_z_504d_base_v035_signal(currentratio):
    result = _z(currentratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(currentratio)
def cl_f005_current_liquidity_logz_252d_base_v036_signal(currentratio):
    result = _z(_current_liquidity_log(currentratio), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(currentratio)
def cl_f005_current_liquidity_logz_504d_base_v037_signal(currentratio):
    result = _z(_current_liquidity_log(currentratio), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of currentratio^2 times closeadj
def cl_f005_current_liquidity_sq_63d_base_v038_signal(currentratio, closeadj):
    result = _mean(currentratio * currentratio, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of currentratio^2 times closeadj
def cl_f005_current_liquidity_sq_252d_base_v039_signal(currentratio, closeadj):
    result = _mean(currentratio * currentratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(currentratio) times closeadj
def cl_f005_current_liquidity_sign_21d_base_v040_signal(currentratio, closeadj):
    result = _mean(np.sign(currentratio), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(currentratio) times closeadj
def cl_f005_current_liquidity_sign_63d_base_v041_signal(currentratio, closeadj):
    result = _mean(np.sign(currentratio), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(currentratio) times closeadj
def cl_f005_current_liquidity_sign_252d_base_v042_signal(currentratio, closeadj):
    result = _mean(np.sign(currentratio), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d currentratio/opex mean
def cl_f005_current_liquidity_per_opex_63d_base_v043_signal(currentratio, opex):
    result = _mean(_current_liquidity_scaled(currentratio, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d currentratio/opex mean
def cl_f005_current_liquidity_per_opex_252d_base_v044_signal(currentratio, opex):
    result = _mean(_current_liquidity_scaled(currentratio, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d currentratio/ebitda mean
def cl_f005_current_liquidity_per_ebitda_63d_base_v045_signal(currentratio, ebitda):
    result = _mean(_current_liquidity_scaled(currentratio, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d currentratio/ebitda mean
def cl_f005_current_liquidity_per_ebitda_252d_base_v046_signal(currentratio, ebitda):
    result = _mean(_current_liquidity_scaled(currentratio, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d currentratio/capex mean
def cl_f005_current_liquidity_per_capex_63d_base_v047_signal(currentratio, capex):
    result = _mean(_current_liquidity_scaled(currentratio, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d currentratio/capex mean
def cl_f005_current_liquidity_per_capex_252d_base_v048_signal(currentratio, capex):
    result = _mean(_current_liquidity_scaled(currentratio, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d currentratio/liabilities mean
def cl_f005_current_liquidity_per_liabilities_63d_base_v049_signal(currentratio, liabilities):
    result = _mean(_current_liquidity_scaled(currentratio, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d currentratio/liabilities mean
def cl_f005_current_liquidity_per_liabilities_252d_base_v050_signal(currentratio, liabilities):
    result = _mean(_current_liquidity_scaled(currentratio, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# currentratio relative to 252d max times closeadj
def cl_f005_current_liquidity_relmax_252d_base_v051_signal(currentratio, closeadj):
    peak = currentratio.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (currentratio / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# currentratio relative to 504d max times closeadj
def cl_f005_current_liquidity_relmax_504d_base_v052_signal(currentratio, closeadj):
    peak = currentratio.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (currentratio / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# currentratio relative to 252d min times closeadj
def cl_f005_current_liquidity_relmin_252d_base_v053_signal(currentratio, closeadj):
    trough = currentratio.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (currentratio / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# currentratio relative to 504d min times closeadj
def cl_f005_current_liquidity_relmin_504d_base_v054_signal(currentratio, closeadj):
    trough = currentratio.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (currentratio / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of currentratio times closeadj
def cl_f005_current_liquidity_pct_21d_base_v055_signal(currentratio, closeadj):
    result = _pct_change(currentratio, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of currentratio times closeadj
def cl_f005_current_liquidity_pct_63d_base_v056_signal(currentratio, closeadj):
    result = _pct_change(currentratio, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of currentratio times closeadj
def cl_f005_current_liquidity_pct_252d_base_v057_signal(currentratio, closeadj):
    result = _pct_change(currentratio, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of currentratio times closeadj
def cl_f005_current_liquidity_sum_63d_base_v058_signal(currentratio, closeadj):
    result = currentratio.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of currentratio times closeadj
def cl_f005_current_liquidity_sum_252d_base_v059_signal(currentratio, closeadj):
    result = currentratio.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of currentratio times closeadj
def cl_f005_current_liquidity_sum_504d_base_v060_signal(currentratio, closeadj):
    result = currentratio.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed currentratio(63d) / smoothed assetsc(252d) x closeadj
def cl_f005_current_liquidity_rom_assetsc_252_63d_base_v061_signal(currentratio, assetsc, closeadj):
    n = _mean(currentratio, 63)
    d = _mean(assetsc, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed currentratio(126d) / smoothed assetsc(504d) x closeadj
def cl_f005_current_liquidity_rom_assetsc_504_126d_base_v062_signal(currentratio, assetsc, closeadj):
    n = _mean(currentratio, 126)
    d = _mean(assetsc, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed currentratio(63d) / smoothed liabilitiesc(252d) x closeadj
def cl_f005_current_liquidity_rom_liabilitiesc_252_63d_base_v063_signal(currentratio, liabilitiesc, closeadj):
    n = _mean(currentratio, 63)
    d = _mean(liabilitiesc, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed currentratio(126d) / smoothed liabilitiesc(504d) x closeadj
def cl_f005_current_liquidity_rom_liabilitiesc_504_126d_base_v064_signal(currentratio, liabilitiesc, closeadj):
    n = _mean(currentratio, 126)
    d = _mean(liabilitiesc, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed currentratio(63d) / smoothed cashneq(252d) x closeadj
def cl_f005_current_liquidity_rom_cashneq_252_63d_base_v065_signal(currentratio, cashneq, closeadj):
    n = _mean(currentratio, 63)
    d = _mean(cashneq, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed currentratio(126d) / smoothed cashneq(504d) x closeadj
def cl_f005_current_liquidity_rom_cashneq_504_126d_base_v066_signal(currentratio, cashneq, closeadj):
    n = _mean(currentratio, 126)
    d = _mean(cashneq, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(currentratio) / std(assetsc)
def cl_f005_current_liquidity_volratio_assetsc_252d_base_v067_signal(currentratio, assetsc):
    n = _std(currentratio, 252)
    d = _std(assetsc, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(currentratio) / std(assetsc)
def cl_f005_current_liquidity_volratio_assetsc_504d_base_v068_signal(currentratio, assetsc):
    n = _std(currentratio, 504)
    d = _std(assetsc, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(currentratio) / std(liabilitiesc)
def cl_f005_current_liquidity_volratio_liabilitiesc_252d_base_v069_signal(currentratio, liabilitiesc):
    n = _std(currentratio, 252)
    d = _std(liabilitiesc, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(currentratio) / std(liabilitiesc)
def cl_f005_current_liquidity_volratio_liabilitiesc_504d_base_v070_signal(currentratio, liabilitiesc):
    n = _std(currentratio, 504)
    d = _std(liabilitiesc, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed currentratio times closeadj
def cl_f005_current_liquidity_raw_5d_base_v071_signal(currentratio, closeadj):
    result = _mean(currentratio, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed currentratio times closeadj
def cl_f005_current_liquidity_raw_1008d_base_v072_signal(currentratio, closeadj):
    result = _mean(currentratio, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of currentratio/assetsc
def cl_f005_current_liquidity_log_per_assetsc_252d_base_v073_signal(currentratio, assetsc):
    s = _current_liquidity_scaled(currentratio, assetsc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of currentratio/assetsc
def cl_f005_current_liquidity_log_per_assetsc_504d_base_v074_signal(currentratio, assetsc):
    s = _current_liquidity_scaled(currentratio, assetsc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of currentratio/liabilitiesc
def cl_f005_current_liquidity_log_per_liabilitiesc_252d_base_v075_signal(currentratio, liabilitiesc):
    s = _current_liquidity_scaled(currentratio, liabilitiesc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
