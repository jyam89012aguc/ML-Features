"""Family f027 - Accumulated deficit and retained earnings (Capital Structure) | Sharadar tables: SF1 | fields: retearn, equity, assets | base 001-075"""
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
def _retained_deficit_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _retained_deficit_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _retained_deficit_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed retearn times closeadj
def rd_f027_retained_deficit_raw_21d_base_v001_signal(retearn, closeadj):
    result = _mean(retearn, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed retearn times closeadj
def rd_f027_retained_deficit_raw_63d_base_v002_signal(retearn, closeadj):
    result = _mean(retearn, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed retearn times closeadj
def rd_f027_retained_deficit_raw_126d_base_v003_signal(retearn, closeadj):
    result = _mean(retearn, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed retearn times closeadj
def rd_f027_retained_deficit_raw_252d_base_v004_signal(retearn, closeadj):
    result = _mean(retearn, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed retearn times closeadj
def rd_f027_retained_deficit_raw_504d_base_v005_signal(retearn, closeadj):
    result = _mean(retearn, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(retearn) times closeadj
def rd_f027_retained_deficit_log_21d_base_v006_signal(retearn, closeadj):
    result = _mean(_retained_deficit_log(retearn), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(retearn) times closeadj
def rd_f027_retained_deficit_log_63d_base_v007_signal(retearn, closeadj):
    result = _mean(_retained_deficit_log(retearn), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(retearn) times closeadj
def rd_f027_retained_deficit_log_126d_base_v008_signal(retearn, closeadj):
    result = _mean(_retained_deficit_log(retearn), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(retearn) times closeadj
def rd_f027_retained_deficit_log_252d_base_v009_signal(retearn, closeadj):
    result = _mean(_retained_deficit_log(retearn), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(retearn) times closeadj
def rd_f027_retained_deficit_log_504d_base_v010_signal(retearn, closeadj):
    result = _mean(_retained_deficit_log(retearn), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retearn/equity mean
def rd_f027_retained_deficit_per_equity_63d_base_v011_signal(retearn, equity):
    result = _mean(_retained_deficit_scaled(retearn, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn/equity mean
def rd_f027_retained_deficit_per_equity_252d_base_v012_signal(retearn, equity):
    result = _mean(_retained_deficit_scaled(retearn, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d retearn/equity mean
def rd_f027_retained_deficit_per_equity_504d_base_v013_signal(retearn, equity):
    result = _mean(_retained_deficit_scaled(retearn, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retearn/assets mean
def rd_f027_retained_deficit_per_assets_63d_base_v014_signal(retearn, assets):
    result = _mean(_retained_deficit_scaled(retearn, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn/assets mean
def rd_f027_retained_deficit_per_assets_252d_base_v015_signal(retearn, assets):
    result = _mean(_retained_deficit_scaled(retearn, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d retearn/assets mean
def rd_f027_retained_deficit_per_assets_504d_base_v016_signal(retearn, assets):
    result = _mean(_retained_deficit_scaled(retearn, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retearn/marketcap mean
def rd_f027_retained_deficit_per_marketcap_63d_base_v017_signal(retearn, marketcap):
    result = _mean(_retained_deficit_scaled(retearn, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn/marketcap mean
def rd_f027_retained_deficit_per_marketcap_252d_base_v018_signal(retearn, marketcap):
    result = _mean(_retained_deficit_scaled(retearn, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d retearn/marketcap mean
def rd_f027_retained_deficit_per_marketcap_504d_base_v019_signal(retearn, marketcap):
    result = _mean(_retained_deficit_scaled(retearn, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retearn/debt mean
def rd_f027_retained_deficit_per_debt_63d_base_v020_signal(retearn, debt):
    result = _mean(_retained_deficit_scaled(retearn, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn/debt mean
def rd_f027_retained_deficit_per_debt_252d_base_v021_signal(retearn, debt):
    result = _mean(_retained_deficit_scaled(retearn, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d retearn/debt mean
def rd_f027_retained_deficit_per_debt_504d_base_v022_signal(retearn, debt):
    result = _mean(_retained_deficit_scaled(retearn, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retearn/revenue mean
def rd_f027_retained_deficit_per_revenue_63d_base_v023_signal(retearn, revenue):
    result = _mean(_retained_deficit_scaled(retearn, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn/revenue mean
def rd_f027_retained_deficit_per_revenue_252d_base_v024_signal(retearn, revenue):
    result = _mean(_retained_deficit_scaled(retearn, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d retearn/revenue mean
def rd_f027_retained_deficit_per_revenue_504d_base_v025_signal(retearn, revenue):
    result = _mean(_retained_deficit_scaled(retearn, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retearn per share times closeadj
def rd_f027_retained_deficit_pershare_21d_base_v026_signal(retearn, sharesbas, closeadj):
    ps = _retained_deficit_per_share(retearn, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retearn per share times closeadj
def rd_f027_retained_deficit_pershare_63d_base_v027_signal(retearn, sharesbas, closeadj):
    ps = _retained_deficit_per_share(retearn, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d retearn per share times closeadj
def rd_f027_retained_deficit_pershare_126d_base_v028_signal(retearn, sharesbas, closeadj):
    ps = _retained_deficit_per_share(retearn, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn per share times closeadj
def rd_f027_retained_deficit_pershare_252d_base_v029_signal(retearn, sharesbas, closeadj):
    ps = _retained_deficit_per_share(retearn, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d retearn per share times closeadj
def rd_f027_retained_deficit_pershare_504d_base_v030_signal(retearn, sharesbas, closeadj):
    ps = _retained_deficit_per_share(retearn, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of retearn times closeadj
def rd_f027_retained_deficit_std_63d_base_v031_signal(retearn, closeadj):
    result = _std(retearn, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of retearn times closeadj
def rd_f027_retained_deficit_std_252d_base_v032_signal(retearn, closeadj):
    result = _std(retearn, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of retearn times closeadj
def rd_f027_retained_deficit_std_504d_base_v033_signal(retearn, closeadj):
    result = _std(retearn, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of retearn
def rd_f027_retained_deficit_z_252d_base_v034_signal(retearn):
    result = _z(retearn, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of retearn
def rd_f027_retained_deficit_z_504d_base_v035_signal(retearn):
    result = _z(retearn, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(retearn)
def rd_f027_retained_deficit_logz_252d_base_v036_signal(retearn):
    result = _z(_retained_deficit_log(retearn), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(retearn)
def rd_f027_retained_deficit_logz_504d_base_v037_signal(retearn):
    result = _z(_retained_deficit_log(retearn), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of retearn^2 times closeadj
def rd_f027_retained_deficit_sq_63d_base_v038_signal(retearn, closeadj):
    result = _mean(retearn * retearn, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of retearn^2 times closeadj
def rd_f027_retained_deficit_sq_252d_base_v039_signal(retearn, closeadj):
    result = _mean(retearn * retearn, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(retearn) times closeadj
def rd_f027_retained_deficit_sign_21d_base_v040_signal(retearn, closeadj):
    result = _mean(np.sign(retearn), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(retearn) times closeadj
def rd_f027_retained_deficit_sign_63d_base_v041_signal(retearn, closeadj):
    result = _mean(np.sign(retearn), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(retearn) times closeadj
def rd_f027_retained_deficit_sign_252d_base_v042_signal(retearn, closeadj):
    result = _mean(np.sign(retearn), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retearn/opex mean
def rd_f027_retained_deficit_per_opex_63d_base_v043_signal(retearn, opex):
    result = _mean(_retained_deficit_scaled(retearn, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn/opex mean
def rd_f027_retained_deficit_per_opex_252d_base_v044_signal(retearn, opex):
    result = _mean(_retained_deficit_scaled(retearn, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retearn/ebitda mean
def rd_f027_retained_deficit_per_ebitda_63d_base_v045_signal(retearn, ebitda):
    result = _mean(_retained_deficit_scaled(retearn, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn/ebitda mean
def rd_f027_retained_deficit_per_ebitda_252d_base_v046_signal(retearn, ebitda):
    result = _mean(_retained_deficit_scaled(retearn, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retearn/capex mean
def rd_f027_retained_deficit_per_capex_63d_base_v047_signal(retearn, capex):
    result = _mean(_retained_deficit_scaled(retearn, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn/capex mean
def rd_f027_retained_deficit_per_capex_252d_base_v048_signal(retearn, capex):
    result = _mean(_retained_deficit_scaled(retearn, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retearn/liabilities mean
def rd_f027_retained_deficit_per_liabilities_63d_base_v049_signal(retearn, liabilities):
    result = _mean(_retained_deficit_scaled(retearn, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn/liabilities mean
def rd_f027_retained_deficit_per_liabilities_252d_base_v050_signal(retearn, liabilities):
    result = _mean(_retained_deficit_scaled(retearn, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# retearn relative to 252d max times closeadj
def rd_f027_retained_deficit_relmax_252d_base_v051_signal(retearn, closeadj):
    peak = retearn.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (retearn / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# retearn relative to 504d max times closeadj
def rd_f027_retained_deficit_relmax_504d_base_v052_signal(retearn, closeadj):
    peak = retearn.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (retearn / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# retearn relative to 252d min times closeadj
def rd_f027_retained_deficit_relmin_252d_base_v053_signal(retearn, closeadj):
    trough = retearn.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (retearn / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# retearn relative to 504d min times closeadj
def rd_f027_retained_deficit_relmin_504d_base_v054_signal(retearn, closeadj):
    trough = retearn.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (retearn / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of retearn times closeadj
def rd_f027_retained_deficit_pct_21d_base_v055_signal(retearn, closeadj):
    result = _pct_change(retearn, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of retearn times closeadj
def rd_f027_retained_deficit_pct_63d_base_v056_signal(retearn, closeadj):
    result = _pct_change(retearn, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of retearn times closeadj
def rd_f027_retained_deficit_pct_252d_base_v057_signal(retearn, closeadj):
    result = _pct_change(retearn, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of retearn times closeadj
def rd_f027_retained_deficit_sum_63d_base_v058_signal(retearn, closeadj):
    result = retearn.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of retearn times closeadj
def rd_f027_retained_deficit_sum_252d_base_v059_signal(retearn, closeadj):
    result = retearn.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of retearn times closeadj
def rd_f027_retained_deficit_sum_504d_base_v060_signal(retearn, closeadj):
    result = retearn.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed retearn(63d) / smoothed equity(252d) x closeadj
def rd_f027_retained_deficit_rom_equity_252_63d_base_v061_signal(retearn, equity, closeadj):
    n = _mean(retearn, 63)
    d = _mean(equity, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed retearn(126d) / smoothed equity(504d) x closeadj
def rd_f027_retained_deficit_rom_equity_504_126d_base_v062_signal(retearn, equity, closeadj):
    n = _mean(retearn, 126)
    d = _mean(equity, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed retearn(63d) / smoothed assets(252d) x closeadj
def rd_f027_retained_deficit_rom_assets_252_63d_base_v063_signal(retearn, assets, closeadj):
    n = _mean(retearn, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed retearn(126d) / smoothed assets(504d) x closeadj
def rd_f027_retained_deficit_rom_assets_504_126d_base_v064_signal(retearn, assets, closeadj):
    n = _mean(retearn, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed retearn(63d) / smoothed marketcap(252d) x closeadj
def rd_f027_retained_deficit_rom_marketcap_252_63d_base_v065_signal(retearn, marketcap, closeadj):
    n = _mean(retearn, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed retearn(126d) / smoothed marketcap(504d) x closeadj
def rd_f027_retained_deficit_rom_marketcap_504_126d_base_v066_signal(retearn, marketcap, closeadj):
    n = _mean(retearn, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(retearn) / std(equity)
def rd_f027_retained_deficit_volratio_equity_252d_base_v067_signal(retearn, equity):
    n = _std(retearn, 252)
    d = _std(equity, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(retearn) / std(equity)
def rd_f027_retained_deficit_volratio_equity_504d_base_v068_signal(retearn, equity):
    n = _std(retearn, 504)
    d = _std(equity, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(retearn) / std(assets)
def rd_f027_retained_deficit_volratio_assets_252d_base_v069_signal(retearn, assets):
    n = _std(retearn, 252)
    d = _std(assets, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(retearn) / std(assets)
def rd_f027_retained_deficit_volratio_assets_504d_base_v070_signal(retearn, assets):
    n = _std(retearn, 504)
    d = _std(assets, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed retearn times closeadj
def rd_f027_retained_deficit_raw_5d_base_v071_signal(retearn, closeadj):
    result = _mean(retearn, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed retearn times closeadj
def rd_f027_retained_deficit_raw_1008d_base_v072_signal(retearn, closeadj):
    result = _mean(retearn, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of retearn/equity
def rd_f027_retained_deficit_log_per_equity_252d_base_v073_signal(retearn, equity):
    s = _retained_deficit_scaled(retearn, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of retearn/equity
def rd_f027_retained_deficit_log_per_equity_504d_base_v074_signal(retearn, equity):
    s = _retained_deficit_scaled(retearn, equity)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of retearn/assets
def rd_f027_retained_deficit_log_per_assets_252d_base_v075_signal(retearn, assets):
    s = _retained_deficit_scaled(retearn, assets)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
