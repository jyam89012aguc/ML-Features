"""Family f092 - Insider transaction net flow (Insiders and Ownership) | Sharadar tables: SF2 | fields: transactioncode, transactionshares, transactionvalue, transactionpricepershare | base 001-075"""
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
def _insider_transaction_flow_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _insider_transaction_flow_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _insider_transaction_flow_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed transactioncode times closeadj
def itf_f092_insider_transaction_flow_raw_21d_base_v001_signal(transactioncode, closeadj):
    result = _mean(transactioncode, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed transactioncode times closeadj
def itf_f092_insider_transaction_flow_raw_63d_base_v002_signal(transactioncode, closeadj):
    result = _mean(transactioncode, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed transactioncode times closeadj
def itf_f092_insider_transaction_flow_raw_126d_base_v003_signal(transactioncode, closeadj):
    result = _mean(transactioncode, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed transactioncode times closeadj
def itf_f092_insider_transaction_flow_raw_252d_base_v004_signal(transactioncode, closeadj):
    result = _mean(transactioncode, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed transactioncode times closeadj
def itf_f092_insider_transaction_flow_raw_504d_base_v005_signal(transactioncode, closeadj):
    result = _mean(transactioncode, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(transactioncode) times closeadj
def itf_f092_insider_transaction_flow_log_21d_base_v006_signal(transactioncode, closeadj):
    result = _mean(_insider_transaction_flow_log(transactioncode), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(transactioncode) times closeadj
def itf_f092_insider_transaction_flow_log_63d_base_v007_signal(transactioncode, closeadj):
    result = _mean(_insider_transaction_flow_log(transactioncode), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(transactioncode) times closeadj
def itf_f092_insider_transaction_flow_log_126d_base_v008_signal(transactioncode, closeadj):
    result = _mean(_insider_transaction_flow_log(transactioncode), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(transactioncode) times closeadj
def itf_f092_insider_transaction_flow_log_252d_base_v009_signal(transactioncode, closeadj):
    result = _mean(_insider_transaction_flow_log(transactioncode), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(transactioncode) times closeadj
def itf_f092_insider_transaction_flow_log_504d_base_v010_signal(transactioncode, closeadj):
    result = _mean(_insider_transaction_flow_log(transactioncode), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactioncode/transactionshares mean
def itf_f092_insider_transaction_flow_per_transactionshares_63d_base_v011_signal(transactioncode, transactionshares):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactioncode/transactionshares mean
def itf_f092_insider_transaction_flow_per_transactionshares_252d_base_v012_signal(transactioncode, transactionshares):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d transactioncode/transactionshares mean
def itf_f092_insider_transaction_flow_per_transactionshares_504d_base_v013_signal(transactioncode, transactionshares):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, transactionshares), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactioncode/transactionvalue mean
def itf_f092_insider_transaction_flow_per_transactionvalue_63d_base_v014_signal(transactioncode, transactionvalue):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactioncode/transactionvalue mean
def itf_f092_insider_transaction_flow_per_transactionvalue_252d_base_v015_signal(transactioncode, transactionvalue):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d transactioncode/transactionvalue mean
def itf_f092_insider_transaction_flow_per_transactionvalue_504d_base_v016_signal(transactioncode, transactionvalue):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, transactionvalue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactioncode/transactionpricepershare mean
def itf_f092_insider_transaction_flow_per_transactionprice_63d_base_v017_signal(transactioncode, transactionpricepershare):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactioncode/transactionpricepershare mean
def itf_f092_insider_transaction_flow_per_transactionprice_252d_base_v018_signal(transactioncode, transactionpricepershare):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d transactioncode/transactionpricepershare mean
def itf_f092_insider_transaction_flow_per_transactionprice_504d_base_v019_signal(transactioncode, transactionpricepershare):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, transactionpricepershare), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactioncode/assets mean
def itf_f092_insider_transaction_flow_per_assets_63d_base_v020_signal(transactioncode, assets):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactioncode/assets mean
def itf_f092_insider_transaction_flow_per_assets_252d_base_v021_signal(transactioncode, assets):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d transactioncode/assets mean
def itf_f092_insider_transaction_flow_per_assets_504d_base_v022_signal(transactioncode, assets):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactioncode/marketcap mean
def itf_f092_insider_transaction_flow_per_marketcap_63d_base_v023_signal(transactioncode, marketcap):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactioncode/marketcap mean
def itf_f092_insider_transaction_flow_per_marketcap_252d_base_v024_signal(transactioncode, marketcap):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d transactioncode/marketcap mean
def itf_f092_insider_transaction_flow_per_marketcap_504d_base_v025_signal(transactioncode, marketcap):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d transactioncode per share times closeadj
def itf_f092_insider_transaction_flow_pershare_21d_base_v026_signal(transactioncode, sharesbas, closeadj):
    ps = _insider_transaction_flow_per_share(transactioncode, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactioncode per share times closeadj
def itf_f092_insider_transaction_flow_pershare_63d_base_v027_signal(transactioncode, sharesbas, closeadj):
    ps = _insider_transaction_flow_per_share(transactioncode, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d transactioncode per share times closeadj
def itf_f092_insider_transaction_flow_pershare_126d_base_v028_signal(transactioncode, sharesbas, closeadj):
    ps = _insider_transaction_flow_per_share(transactioncode, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactioncode per share times closeadj
def itf_f092_insider_transaction_flow_pershare_252d_base_v029_signal(transactioncode, sharesbas, closeadj):
    ps = _insider_transaction_flow_per_share(transactioncode, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d transactioncode per share times closeadj
def itf_f092_insider_transaction_flow_pershare_504d_base_v030_signal(transactioncode, sharesbas, closeadj):
    ps = _insider_transaction_flow_per_share(transactioncode, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of transactioncode times closeadj
def itf_f092_insider_transaction_flow_std_63d_base_v031_signal(transactioncode, closeadj):
    result = _std(transactioncode, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of transactioncode times closeadj
def itf_f092_insider_transaction_flow_std_252d_base_v032_signal(transactioncode, closeadj):
    result = _std(transactioncode, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of transactioncode times closeadj
def itf_f092_insider_transaction_flow_std_504d_base_v033_signal(transactioncode, closeadj):
    result = _std(transactioncode, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of transactioncode
def itf_f092_insider_transaction_flow_z_252d_base_v034_signal(transactioncode):
    result = _z(transactioncode, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of transactioncode
def itf_f092_insider_transaction_flow_z_504d_base_v035_signal(transactioncode):
    result = _z(transactioncode, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(transactioncode)
def itf_f092_insider_transaction_flow_logz_252d_base_v036_signal(transactioncode):
    result = _z(_insider_transaction_flow_log(transactioncode), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(transactioncode)
def itf_f092_insider_transaction_flow_logz_504d_base_v037_signal(transactioncode):
    result = _z(_insider_transaction_flow_log(transactioncode), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of transactioncode^2 times closeadj
def itf_f092_insider_transaction_flow_sq_63d_base_v038_signal(transactioncode, closeadj):
    result = _mean(transactioncode * transactioncode, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of transactioncode^2 times closeadj
def itf_f092_insider_transaction_flow_sq_252d_base_v039_signal(transactioncode, closeadj):
    result = _mean(transactioncode * transactioncode, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(transactioncode) times closeadj
def itf_f092_insider_transaction_flow_sign_21d_base_v040_signal(transactioncode, closeadj):
    result = _mean(np.sign(transactioncode), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(transactioncode) times closeadj
def itf_f092_insider_transaction_flow_sign_63d_base_v041_signal(transactioncode, closeadj):
    result = _mean(np.sign(transactioncode), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(transactioncode) times closeadj
def itf_f092_insider_transaction_flow_sign_252d_base_v042_signal(transactioncode, closeadj):
    result = _mean(np.sign(transactioncode), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactioncode/opex mean
def itf_f092_insider_transaction_flow_per_opex_63d_base_v043_signal(transactioncode, opex):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactioncode/opex mean
def itf_f092_insider_transaction_flow_per_opex_252d_base_v044_signal(transactioncode, opex):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactioncode/ebitda mean
def itf_f092_insider_transaction_flow_per_ebitda_63d_base_v045_signal(transactioncode, ebitda):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactioncode/ebitda mean
def itf_f092_insider_transaction_flow_per_ebitda_252d_base_v046_signal(transactioncode, ebitda):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactioncode/capex mean
def itf_f092_insider_transaction_flow_per_capex_63d_base_v047_signal(transactioncode, capex):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactioncode/capex mean
def itf_f092_insider_transaction_flow_per_capex_252d_base_v048_signal(transactioncode, capex):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d transactioncode/liabilities mean
def itf_f092_insider_transaction_flow_per_liabilities_63d_base_v049_signal(transactioncode, liabilities):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d transactioncode/liabilities mean
def itf_f092_insider_transaction_flow_per_liabilities_252d_base_v050_signal(transactioncode, liabilities):
    result = _mean(_insider_transaction_flow_scaled(transactioncode, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# transactioncode relative to 252d max times closeadj
def itf_f092_insider_transaction_flow_relmax_252d_base_v051_signal(transactioncode, closeadj):
    peak = transactioncode.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (transactioncode / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# transactioncode relative to 504d max times closeadj
def itf_f092_insider_transaction_flow_relmax_504d_base_v052_signal(transactioncode, closeadj):
    peak = transactioncode.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (transactioncode / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# transactioncode relative to 252d min times closeadj
def itf_f092_insider_transaction_flow_relmin_252d_base_v053_signal(transactioncode, closeadj):
    trough = transactioncode.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (transactioncode / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# transactioncode relative to 504d min times closeadj
def itf_f092_insider_transaction_flow_relmin_504d_base_v054_signal(transactioncode, closeadj):
    trough = transactioncode.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (transactioncode / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of transactioncode times closeadj
def itf_f092_insider_transaction_flow_pct_21d_base_v055_signal(transactioncode, closeadj):
    result = _pct_change(transactioncode, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of transactioncode times closeadj
def itf_f092_insider_transaction_flow_pct_63d_base_v056_signal(transactioncode, closeadj):
    result = _pct_change(transactioncode, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of transactioncode times closeadj
def itf_f092_insider_transaction_flow_pct_252d_base_v057_signal(transactioncode, closeadj):
    result = _pct_change(transactioncode, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of transactioncode times closeadj
def itf_f092_insider_transaction_flow_sum_63d_base_v058_signal(transactioncode, closeadj):
    result = transactioncode.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of transactioncode times closeadj
def itf_f092_insider_transaction_flow_sum_252d_base_v059_signal(transactioncode, closeadj):
    result = transactioncode.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of transactioncode times closeadj
def itf_f092_insider_transaction_flow_sum_504d_base_v060_signal(transactioncode, closeadj):
    result = transactioncode.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed transactioncode(63d) / smoothed transactionshares(252d) x closeadj
def itf_f092_insider_transaction_flow_rom_transactionshares_252_63d_base_v061_signal(transactioncode, transactionshares, closeadj):
    n = _mean(transactioncode, 63)
    d = _mean(transactionshares, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed transactioncode(126d) / smoothed transactionshares(504d) x closeadj
def itf_f092_insider_transaction_flow_rom_transactionshares_504_126d_base_v062_signal(transactioncode, transactionshares, closeadj):
    n = _mean(transactioncode, 126)
    d = _mean(transactionshares, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed transactioncode(63d) / smoothed transactionvalue(252d) x closeadj
def itf_f092_insider_transaction_flow_rom_transactionvalue_252_63d_base_v063_signal(transactioncode, transactionvalue, closeadj):
    n = _mean(transactioncode, 63)
    d = _mean(transactionvalue, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed transactioncode(126d) / smoothed transactionvalue(504d) x closeadj
def itf_f092_insider_transaction_flow_rom_transactionvalue_504_126d_base_v064_signal(transactioncode, transactionvalue, closeadj):
    n = _mean(transactioncode, 126)
    d = _mean(transactionvalue, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed transactioncode(63d) / smoothed transactionpricepershare(252d) x closeadj
def itf_f092_insider_transaction_flow_rom_transactionprice_252_63d_base_v065_signal(transactioncode, transactionpricepershare, closeadj):
    n = _mean(transactioncode, 63)
    d = _mean(transactionpricepershare, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed transactioncode(126d) / smoothed transactionpricepershare(504d) x closeadj
def itf_f092_insider_transaction_flow_rom_transactionprice_504_126d_base_v066_signal(transactioncode, transactionpricepershare, closeadj):
    n = _mean(transactioncode, 126)
    d = _mean(transactionpricepershare, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(transactioncode) / std(transactionshares)
def itf_f092_insider_transaction_flow_volratio_transactionshares_252d_base_v067_signal(transactioncode, transactionshares):
    n = _std(transactioncode, 252)
    d = _std(transactionshares, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(transactioncode) / std(transactionshares)
def itf_f092_insider_transaction_flow_volratio_transactionshares_504d_base_v068_signal(transactioncode, transactionshares):
    n = _std(transactioncode, 504)
    d = _std(transactionshares, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(transactioncode) / std(transactionvalue)
def itf_f092_insider_transaction_flow_volratio_transactionvalue_252d_base_v069_signal(transactioncode, transactionvalue):
    n = _std(transactioncode, 252)
    d = _std(transactionvalue, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(transactioncode) / std(transactionvalue)
def itf_f092_insider_transaction_flow_volratio_transactionvalue_504d_base_v070_signal(transactioncode, transactionvalue):
    n = _std(transactioncode, 504)
    d = _std(transactionvalue, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed transactioncode times closeadj
def itf_f092_insider_transaction_flow_raw_5d_base_v071_signal(transactioncode, closeadj):
    result = _mean(transactioncode, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed transactioncode times closeadj
def itf_f092_insider_transaction_flow_raw_1008d_base_v072_signal(transactioncode, closeadj):
    result = _mean(transactioncode, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of transactioncode/transactionshares
def itf_f092_insider_transaction_flow_log_per_transactionshares_252d_base_v073_signal(transactioncode, transactionshares):
    s = _insider_transaction_flow_scaled(transactioncode, transactionshares)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of transactioncode/transactionshares
def itf_f092_insider_transaction_flow_log_per_transactionshares_504d_base_v074_signal(transactioncode, transactionshares):
    s = _insider_transaction_flow_scaled(transactioncode, transactionshares)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of transactioncode/transactionvalue
def itf_f092_insider_transaction_flow_log_per_transactionvalue_252d_base_v075_signal(transactioncode, transactionvalue):
    s = _insider_transaction_flow_scaled(transactioncode, transactionvalue)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
