"""Family f009 - Free cash flow burn (Cash Flow and Burn) | Sharadar tables: SF1 | fields: fcf, fcfps, ncfo, capex | base 001-075"""
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
def _free_cash_flow_burn_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _free_cash_flow_burn_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _free_cash_flow_burn_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed fcf times closeadj
def fcfb_f009_free_cash_flow_burn_raw_21d_base_v001_signal(fcf, closeadj):
    result = _mean(fcf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed fcf times closeadj
def fcfb_f009_free_cash_flow_burn_raw_63d_base_v002_signal(fcf, closeadj):
    result = _mean(fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed fcf times closeadj
def fcfb_f009_free_cash_flow_burn_raw_126d_base_v003_signal(fcf, closeadj):
    result = _mean(fcf, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed fcf times closeadj
def fcfb_f009_free_cash_flow_burn_raw_252d_base_v004_signal(fcf, closeadj):
    result = _mean(fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed fcf times closeadj
def fcfb_f009_free_cash_flow_burn_raw_504d_base_v005_signal(fcf, closeadj):
    result = _mean(fcf, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(fcf) times closeadj
def fcfb_f009_free_cash_flow_burn_log_21d_base_v006_signal(fcf, closeadj):
    result = _mean(_free_cash_flow_burn_log(fcf), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(fcf) times closeadj
def fcfb_f009_free_cash_flow_burn_log_63d_base_v007_signal(fcf, closeadj):
    result = _mean(_free_cash_flow_burn_log(fcf), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(fcf) times closeadj
def fcfb_f009_free_cash_flow_burn_log_126d_base_v008_signal(fcf, closeadj):
    result = _mean(_free_cash_flow_burn_log(fcf), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(fcf) times closeadj
def fcfb_f009_free_cash_flow_burn_log_252d_base_v009_signal(fcf, closeadj):
    result = _mean(_free_cash_flow_burn_log(fcf), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(fcf) times closeadj
def fcfb_f009_free_cash_flow_burn_log_504d_base_v010_signal(fcf, closeadj):
    result = _mean(_free_cash_flow_burn_log(fcf), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/fcfps mean
def fcfb_f009_free_cash_flow_burn_per_fcfps_63d_base_v011_signal(fcf, fcfps):
    result = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/fcfps mean
def fcfb_f009_free_cash_flow_burn_per_fcfps_252d_base_v012_signal(fcf, fcfps):
    result = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf/fcfps mean
def fcfb_f009_free_cash_flow_burn_per_fcfps_504d_base_v013_signal(fcf, fcfps):
    result = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/ncfo mean
def fcfb_f009_free_cash_flow_burn_per_ncfo_63d_base_v014_signal(fcf, ncfo):
    result = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/ncfo mean
def fcfb_f009_free_cash_flow_burn_per_ncfo_252d_base_v015_signal(fcf, ncfo):
    result = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf/ncfo mean
def fcfb_f009_free_cash_flow_burn_per_ncfo_504d_base_v016_signal(fcf, ncfo):
    result = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/assets mean
def fcfb_f009_free_cash_flow_burn_per_assets_63d_base_v017_signal(fcf, assets):
    result = _mean(_free_cash_flow_burn_scaled(fcf, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/assets mean
def fcfb_f009_free_cash_flow_burn_per_assets_252d_base_v018_signal(fcf, assets):
    result = _mean(_free_cash_flow_burn_scaled(fcf, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf/assets mean
def fcfb_f009_free_cash_flow_burn_per_assets_504d_base_v019_signal(fcf, assets):
    result = _mean(_free_cash_flow_burn_scaled(fcf, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/marketcap mean
def fcfb_f009_free_cash_flow_burn_per_marketcap_63d_base_v020_signal(fcf, marketcap):
    result = _mean(_free_cash_flow_burn_scaled(fcf, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/marketcap mean
def fcfb_f009_free_cash_flow_burn_per_marketcap_252d_base_v021_signal(fcf, marketcap):
    result = _mean(_free_cash_flow_burn_scaled(fcf, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf/marketcap mean
def fcfb_f009_free_cash_flow_burn_per_marketcap_504d_base_v022_signal(fcf, marketcap):
    result = _mean(_free_cash_flow_burn_scaled(fcf, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/equity mean
def fcfb_f009_free_cash_flow_burn_per_equity_63d_base_v023_signal(fcf, equity):
    result = _mean(_free_cash_flow_burn_scaled(fcf, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/equity mean
def fcfb_f009_free_cash_flow_burn_per_equity_252d_base_v024_signal(fcf, equity):
    result = _mean(_free_cash_flow_burn_scaled(fcf, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf/equity mean
def fcfb_f009_free_cash_flow_burn_per_equity_504d_base_v025_signal(fcf, equity):
    result = _mean(_free_cash_flow_burn_scaled(fcf, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fcf per share times closeadj
def fcfb_f009_free_cash_flow_burn_pershare_21d_base_v026_signal(fcf, sharesbas, closeadj):
    ps = _free_cash_flow_burn_per_share(fcf, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf per share times closeadj
def fcfb_f009_free_cash_flow_burn_pershare_63d_base_v027_signal(fcf, sharesbas, closeadj):
    ps = _free_cash_flow_burn_per_share(fcf, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fcf per share times closeadj
def fcfb_f009_free_cash_flow_burn_pershare_126d_base_v028_signal(fcf, sharesbas, closeadj):
    ps = _free_cash_flow_burn_per_share(fcf, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf per share times closeadj
def fcfb_f009_free_cash_flow_burn_pershare_252d_base_v029_signal(fcf, sharesbas, closeadj):
    ps = _free_cash_flow_burn_per_share(fcf, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fcf per share times closeadj
def fcfb_f009_free_cash_flow_burn_pershare_504d_base_v030_signal(fcf, sharesbas, closeadj):
    ps = _free_cash_flow_burn_per_share(fcf, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_std_63d_base_v031_signal(fcf, closeadj):
    result = _std(fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_std_252d_base_v032_signal(fcf, closeadj):
    result = _std(fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_std_504d_base_v033_signal(fcf, closeadj):
    result = _std(fcf, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of fcf
def fcfb_f009_free_cash_flow_burn_z_252d_base_v034_signal(fcf):
    result = _z(fcf, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of fcf
def fcfb_f009_free_cash_flow_burn_z_504d_base_v035_signal(fcf):
    result = _z(fcf, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(fcf)
def fcfb_f009_free_cash_flow_burn_logz_252d_base_v036_signal(fcf):
    result = _z(_free_cash_flow_burn_log(fcf), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(fcf)
def fcfb_f009_free_cash_flow_burn_logz_504d_base_v037_signal(fcf):
    result = _z(_free_cash_flow_burn_log(fcf), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of fcf^2 times closeadj
def fcfb_f009_free_cash_flow_burn_sq_63d_base_v038_signal(fcf, closeadj):
    result = _mean(fcf * fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of fcf^2 times closeadj
def fcfb_f009_free_cash_flow_burn_sq_252d_base_v039_signal(fcf, closeadj):
    result = _mean(fcf * fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(fcf) times closeadj
def fcfb_f009_free_cash_flow_burn_sign_21d_base_v040_signal(fcf, closeadj):
    result = _mean(np.sign(fcf), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(fcf) times closeadj
def fcfb_f009_free_cash_flow_burn_sign_63d_base_v041_signal(fcf, closeadj):
    result = _mean(np.sign(fcf), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(fcf) times closeadj
def fcfb_f009_free_cash_flow_burn_sign_252d_base_v042_signal(fcf, closeadj):
    result = _mean(np.sign(fcf), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/opex mean
def fcfb_f009_free_cash_flow_burn_per_opex_63d_base_v043_signal(fcf, opex):
    result = _mean(_free_cash_flow_burn_scaled(fcf, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/opex mean
def fcfb_f009_free_cash_flow_burn_per_opex_252d_base_v044_signal(fcf, opex):
    result = _mean(_free_cash_flow_burn_scaled(fcf, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/ebitda mean
def fcfb_f009_free_cash_flow_burn_per_ebitda_63d_base_v045_signal(fcf, ebitda):
    result = _mean(_free_cash_flow_burn_scaled(fcf, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/ebitda mean
def fcfb_f009_free_cash_flow_burn_per_ebitda_252d_base_v046_signal(fcf, ebitda):
    result = _mean(_free_cash_flow_burn_scaled(fcf, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/capex mean
def fcfb_f009_free_cash_flow_burn_per_capex_63d_base_v047_signal(fcf, capex):
    result = _mean(_free_cash_flow_burn_scaled(fcf, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/capex mean
def fcfb_f009_free_cash_flow_burn_per_capex_252d_base_v048_signal(fcf, capex):
    result = _mean(_free_cash_flow_burn_scaled(fcf, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf/liabilities mean
def fcfb_f009_free_cash_flow_burn_per_liabilities_63d_base_v049_signal(fcf, liabilities):
    result = _mean(_free_cash_flow_burn_scaled(fcf, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf/liabilities mean
def fcfb_f009_free_cash_flow_burn_per_liabilities_252d_base_v050_signal(fcf, liabilities):
    result = _mean(_free_cash_flow_burn_scaled(fcf, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf relative to 252d max times closeadj
def fcfb_f009_free_cash_flow_burn_relmax_252d_base_v051_signal(fcf, closeadj):
    peak = fcf.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (fcf / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fcf relative to 504d max times closeadj
def fcfb_f009_free_cash_flow_burn_relmax_504d_base_v052_signal(fcf, closeadj):
    peak = fcf.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (fcf / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fcf relative to 252d min times closeadj
def fcfb_f009_free_cash_flow_burn_relmin_252d_base_v053_signal(fcf, closeadj):
    trough = fcf.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (fcf / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fcf relative to 504d min times closeadj
def fcfb_f009_free_cash_flow_burn_relmin_504d_base_v054_signal(fcf, closeadj):
    trough = fcf.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (fcf / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_pct_21d_base_v055_signal(fcf, closeadj):
    result = _pct_change(fcf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_pct_63d_base_v056_signal(fcf, closeadj):
    result = _pct_change(fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_pct_252d_base_v057_signal(fcf, closeadj):
    result = _pct_change(fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_sum_63d_base_v058_signal(fcf, closeadj):
    result = fcf.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_sum_252d_base_v059_signal(fcf, closeadj):
    result = fcf.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of fcf times closeadj
def fcfb_f009_free_cash_flow_burn_sum_504d_base_v060_signal(fcf, closeadj):
    result = fcf.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed fcf(63d) / smoothed fcfps(252d) x closeadj
def fcfb_f009_free_cash_flow_burn_rom_fcfps_252_63d_base_v061_signal(fcf, fcfps, closeadj):
    n = _mean(fcf, 63)
    d = _mean(fcfps, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed fcf(126d) / smoothed fcfps(504d) x closeadj
def fcfb_f009_free_cash_flow_burn_rom_fcfps_504_126d_base_v062_signal(fcf, fcfps, closeadj):
    n = _mean(fcf, 126)
    d = _mean(fcfps, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed fcf(63d) / smoothed ncfo(252d) x closeadj
def fcfb_f009_free_cash_flow_burn_rom_ncfo_252_63d_base_v063_signal(fcf, ncfo, closeadj):
    n = _mean(fcf, 63)
    d = _mean(ncfo, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed fcf(126d) / smoothed ncfo(504d) x closeadj
def fcfb_f009_free_cash_flow_burn_rom_ncfo_504_126d_base_v064_signal(fcf, ncfo, closeadj):
    n = _mean(fcf, 126)
    d = _mean(ncfo, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed fcf(63d) / smoothed assets(252d) x closeadj
def fcfb_f009_free_cash_flow_burn_rom_assets_252_63d_base_v065_signal(fcf, assets, closeadj):
    n = _mean(fcf, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed fcf(126d) / smoothed assets(504d) x closeadj
def fcfb_f009_free_cash_flow_burn_rom_assets_504_126d_base_v066_signal(fcf, assets, closeadj):
    n = _mean(fcf, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(fcf) / std(fcfps)
def fcfb_f009_free_cash_flow_burn_volratio_fcfps_252d_base_v067_signal(fcf, fcfps):
    n = _std(fcf, 252)
    d = _std(fcfps, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(fcf) / std(fcfps)
def fcfb_f009_free_cash_flow_burn_volratio_fcfps_504d_base_v068_signal(fcf, fcfps):
    n = _std(fcf, 504)
    d = _std(fcfps, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(fcf) / std(ncfo)
def fcfb_f009_free_cash_flow_burn_volratio_ncfo_252d_base_v069_signal(fcf, ncfo):
    n = _std(fcf, 252)
    d = _std(ncfo, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(fcf) / std(ncfo)
def fcfb_f009_free_cash_flow_burn_volratio_ncfo_504d_base_v070_signal(fcf, ncfo):
    n = _std(fcf, 504)
    d = _std(ncfo, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed fcf times closeadj
def fcfb_f009_free_cash_flow_burn_raw_5d_base_v071_signal(fcf, closeadj):
    result = _mean(fcf, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed fcf times closeadj
def fcfb_f009_free_cash_flow_burn_raw_1008d_base_v072_signal(fcf, closeadj):
    result = _mean(fcf, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of fcf/fcfps
def fcfb_f009_free_cash_flow_burn_log_per_fcfps_252d_base_v073_signal(fcf, fcfps):
    s = _free_cash_flow_burn_scaled(fcf, fcfps)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of fcf/fcfps
def fcfb_f009_free_cash_flow_burn_log_per_fcfps_504d_base_v074_signal(fcf, fcfps):
    s = _free_cash_flow_burn_scaled(fcf, fcfps)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of fcf/ncfo
def fcfb_f009_free_cash_flow_burn_log_per_ncfo_252d_base_v075_signal(fcf, ncfo):
    s = _free_cash_flow_burn_scaled(fcf, ncfo)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
