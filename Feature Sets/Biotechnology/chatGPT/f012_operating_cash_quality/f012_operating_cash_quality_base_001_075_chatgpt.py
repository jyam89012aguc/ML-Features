"""Family f012 - Operating cash quality versus income (Cash Flow and Burn) | Sharadar tables: SF1 | fields: ncfo, netinc, depamor, sbcomp | base 001-075"""
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
def _operating_cash_quality_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _operating_cash_quality_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _operating_cash_quality_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed ncfo times closeadj
def ocq_f012_operating_cash_quality_raw_21d_base_v001_signal(ncfo, closeadj):
    result = _mean(ncfo, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed ncfo times closeadj
def ocq_f012_operating_cash_quality_raw_63d_base_v002_signal(ncfo, closeadj):
    result = _mean(ncfo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed ncfo times closeadj
def ocq_f012_operating_cash_quality_raw_126d_base_v003_signal(ncfo, closeadj):
    result = _mean(ncfo, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed ncfo times closeadj
def ocq_f012_operating_cash_quality_raw_252d_base_v004_signal(ncfo, closeadj):
    result = _mean(ncfo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed ncfo times closeadj
def ocq_f012_operating_cash_quality_raw_504d_base_v005_signal(ncfo, closeadj):
    result = _mean(ncfo, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(ncfo) times closeadj
def ocq_f012_operating_cash_quality_log_21d_base_v006_signal(ncfo, closeadj):
    result = _mean(_operating_cash_quality_log(ncfo), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(ncfo) times closeadj
def ocq_f012_operating_cash_quality_log_63d_base_v007_signal(ncfo, closeadj):
    result = _mean(_operating_cash_quality_log(ncfo), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(ncfo) times closeadj
def ocq_f012_operating_cash_quality_log_126d_base_v008_signal(ncfo, closeadj):
    result = _mean(_operating_cash_quality_log(ncfo), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(ncfo) times closeadj
def ocq_f012_operating_cash_quality_log_252d_base_v009_signal(ncfo, closeadj):
    result = _mean(_operating_cash_quality_log(ncfo), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(ncfo) times closeadj
def ocq_f012_operating_cash_quality_log_504d_base_v010_signal(ncfo, closeadj):
    result = _mean(_operating_cash_quality_log(ncfo), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/netinc mean
def ocq_f012_operating_cash_quality_per_netinc_63d_base_v011_signal(ncfo, netinc):
    result = _mean(_operating_cash_quality_scaled(ncfo, netinc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/netinc mean
def ocq_f012_operating_cash_quality_per_netinc_252d_base_v012_signal(ncfo, netinc):
    result = _mean(_operating_cash_quality_scaled(ncfo, netinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo/netinc mean
def ocq_f012_operating_cash_quality_per_netinc_504d_base_v013_signal(ncfo, netinc):
    result = _mean(_operating_cash_quality_scaled(ncfo, netinc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/depamor mean
def ocq_f012_operating_cash_quality_per_depamor_63d_base_v014_signal(ncfo, depamor):
    result = _mean(_operating_cash_quality_scaled(ncfo, depamor), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/depamor mean
def ocq_f012_operating_cash_quality_per_depamor_252d_base_v015_signal(ncfo, depamor):
    result = _mean(_operating_cash_quality_scaled(ncfo, depamor), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo/depamor mean
def ocq_f012_operating_cash_quality_per_depamor_504d_base_v016_signal(ncfo, depamor):
    result = _mean(_operating_cash_quality_scaled(ncfo, depamor), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/sbcomp mean
def ocq_f012_operating_cash_quality_per_sbcomp_63d_base_v017_signal(ncfo, sbcomp):
    result = _mean(_operating_cash_quality_scaled(ncfo, sbcomp), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/sbcomp mean
def ocq_f012_operating_cash_quality_per_sbcomp_252d_base_v018_signal(ncfo, sbcomp):
    result = _mean(_operating_cash_quality_scaled(ncfo, sbcomp), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo/sbcomp mean
def ocq_f012_operating_cash_quality_per_sbcomp_504d_base_v019_signal(ncfo, sbcomp):
    result = _mean(_operating_cash_quality_scaled(ncfo, sbcomp), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/assets mean
def ocq_f012_operating_cash_quality_per_assets_63d_base_v020_signal(ncfo, assets):
    result = _mean(_operating_cash_quality_scaled(ncfo, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/assets mean
def ocq_f012_operating_cash_quality_per_assets_252d_base_v021_signal(ncfo, assets):
    result = _mean(_operating_cash_quality_scaled(ncfo, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo/assets mean
def ocq_f012_operating_cash_quality_per_assets_504d_base_v022_signal(ncfo, assets):
    result = _mean(_operating_cash_quality_scaled(ncfo, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/marketcap mean
def ocq_f012_operating_cash_quality_per_marketcap_63d_base_v023_signal(ncfo, marketcap):
    result = _mean(_operating_cash_quality_scaled(ncfo, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/marketcap mean
def ocq_f012_operating_cash_quality_per_marketcap_252d_base_v024_signal(ncfo, marketcap):
    result = _mean(_operating_cash_quality_scaled(ncfo, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo/marketcap mean
def ocq_f012_operating_cash_quality_per_marketcap_504d_base_v025_signal(ncfo, marketcap):
    result = _mean(_operating_cash_quality_scaled(ncfo, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo per share times closeadj
def ocq_f012_operating_cash_quality_pershare_21d_base_v026_signal(ncfo, sharesbas, closeadj):
    ps = _operating_cash_quality_per_share(ncfo, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo per share times closeadj
def ocq_f012_operating_cash_quality_pershare_63d_base_v027_signal(ncfo, sharesbas, closeadj):
    ps = _operating_cash_quality_per_share(ncfo, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ncfo per share times closeadj
def ocq_f012_operating_cash_quality_pershare_126d_base_v028_signal(ncfo, sharesbas, closeadj):
    ps = _operating_cash_quality_per_share(ncfo, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo per share times closeadj
def ocq_f012_operating_cash_quality_pershare_252d_base_v029_signal(ncfo, sharesbas, closeadj):
    ps = _operating_cash_quality_per_share(ncfo, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo per share times closeadj
def ocq_f012_operating_cash_quality_pershare_504d_base_v030_signal(ncfo, sharesbas, closeadj):
    ps = _operating_cash_quality_per_share(ncfo, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of ncfo times closeadj
def ocq_f012_operating_cash_quality_std_63d_base_v031_signal(ncfo, closeadj):
    result = _std(ncfo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of ncfo times closeadj
def ocq_f012_operating_cash_quality_std_252d_base_v032_signal(ncfo, closeadj):
    result = _std(ncfo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of ncfo times closeadj
def ocq_f012_operating_cash_quality_std_504d_base_v033_signal(ncfo, closeadj):
    result = _std(ncfo, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of ncfo
def ocq_f012_operating_cash_quality_z_252d_base_v034_signal(ncfo):
    result = _z(ncfo, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of ncfo
def ocq_f012_operating_cash_quality_z_504d_base_v035_signal(ncfo):
    result = _z(ncfo, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(ncfo)
def ocq_f012_operating_cash_quality_logz_252d_base_v036_signal(ncfo):
    result = _z(_operating_cash_quality_log(ncfo), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(ncfo)
def ocq_f012_operating_cash_quality_logz_504d_base_v037_signal(ncfo):
    result = _z(_operating_cash_quality_log(ncfo), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of ncfo^2 times closeadj
def ocq_f012_operating_cash_quality_sq_63d_base_v038_signal(ncfo, closeadj):
    result = _mean(ncfo * ncfo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of ncfo^2 times closeadj
def ocq_f012_operating_cash_quality_sq_252d_base_v039_signal(ncfo, closeadj):
    result = _mean(ncfo * ncfo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(ncfo) times closeadj
def ocq_f012_operating_cash_quality_sign_21d_base_v040_signal(ncfo, closeadj):
    result = _mean(np.sign(ncfo), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(ncfo) times closeadj
def ocq_f012_operating_cash_quality_sign_63d_base_v041_signal(ncfo, closeadj):
    result = _mean(np.sign(ncfo), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(ncfo) times closeadj
def ocq_f012_operating_cash_quality_sign_252d_base_v042_signal(ncfo, closeadj):
    result = _mean(np.sign(ncfo), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/opex mean
def ocq_f012_operating_cash_quality_per_opex_63d_base_v043_signal(ncfo, opex):
    result = _mean(_operating_cash_quality_scaled(ncfo, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/opex mean
def ocq_f012_operating_cash_quality_per_opex_252d_base_v044_signal(ncfo, opex):
    result = _mean(_operating_cash_quality_scaled(ncfo, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/ebitda mean
def ocq_f012_operating_cash_quality_per_ebitda_63d_base_v045_signal(ncfo, ebitda):
    result = _mean(_operating_cash_quality_scaled(ncfo, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/ebitda mean
def ocq_f012_operating_cash_quality_per_ebitda_252d_base_v046_signal(ncfo, ebitda):
    result = _mean(_operating_cash_quality_scaled(ncfo, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/capex mean
def ocq_f012_operating_cash_quality_per_capex_63d_base_v047_signal(ncfo, capex):
    result = _mean(_operating_cash_quality_scaled(ncfo, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/capex mean
def ocq_f012_operating_cash_quality_per_capex_252d_base_v048_signal(ncfo, capex):
    result = _mean(_operating_cash_quality_scaled(ncfo, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo/liabilities mean
def ocq_f012_operating_cash_quality_per_liabilities_63d_base_v049_signal(ncfo, liabilities):
    result = _mean(_operating_cash_quality_scaled(ncfo, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo/liabilities mean
def ocq_f012_operating_cash_quality_per_liabilities_252d_base_v050_signal(ncfo, liabilities):
    result = _mean(_operating_cash_quality_scaled(ncfo, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo relative to 252d max times closeadj
def ocq_f012_operating_cash_quality_relmax_252d_base_v051_signal(ncfo, closeadj):
    peak = ncfo.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (ncfo / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo relative to 504d max times closeadj
def ocq_f012_operating_cash_quality_relmax_504d_base_v052_signal(ncfo, closeadj):
    peak = ncfo.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (ncfo / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo relative to 252d min times closeadj
def ocq_f012_operating_cash_quality_relmin_252d_base_v053_signal(ncfo, closeadj):
    trough = ncfo.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (ncfo / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo relative to 504d min times closeadj
def ocq_f012_operating_cash_quality_relmin_504d_base_v054_signal(ncfo, closeadj):
    trough = ncfo.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (ncfo / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of ncfo times closeadj
def ocq_f012_operating_cash_quality_pct_21d_base_v055_signal(ncfo, closeadj):
    result = _pct_change(ncfo, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of ncfo times closeadj
def ocq_f012_operating_cash_quality_pct_63d_base_v056_signal(ncfo, closeadj):
    result = _pct_change(ncfo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of ncfo times closeadj
def ocq_f012_operating_cash_quality_pct_252d_base_v057_signal(ncfo, closeadj):
    result = _pct_change(ncfo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of ncfo times closeadj
def ocq_f012_operating_cash_quality_sum_63d_base_v058_signal(ncfo, closeadj):
    result = ncfo.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of ncfo times closeadj
def ocq_f012_operating_cash_quality_sum_252d_base_v059_signal(ncfo, closeadj):
    result = ncfo.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of ncfo times closeadj
def ocq_f012_operating_cash_quality_sum_504d_base_v060_signal(ncfo, closeadj):
    result = ncfo.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfo(63d) / smoothed netinc(252d) x closeadj
def ocq_f012_operating_cash_quality_rom_netinc_252_63d_base_v061_signal(ncfo, netinc, closeadj):
    n = _mean(ncfo, 63)
    d = _mean(netinc, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfo(126d) / smoothed netinc(504d) x closeadj
def ocq_f012_operating_cash_quality_rom_netinc_504_126d_base_v062_signal(ncfo, netinc, closeadj):
    n = _mean(ncfo, 126)
    d = _mean(netinc, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfo(63d) / smoothed depamor(252d) x closeadj
def ocq_f012_operating_cash_quality_rom_depamor_252_63d_base_v063_signal(ncfo, depamor, closeadj):
    n = _mean(ncfo, 63)
    d = _mean(depamor, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfo(126d) / smoothed depamor(504d) x closeadj
def ocq_f012_operating_cash_quality_rom_depamor_504_126d_base_v064_signal(ncfo, depamor, closeadj):
    n = _mean(ncfo, 126)
    d = _mean(depamor, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfo(63d) / smoothed sbcomp(252d) x closeadj
def ocq_f012_operating_cash_quality_rom_sbcomp_252_63d_base_v065_signal(ncfo, sbcomp, closeadj):
    n = _mean(ncfo, 63)
    d = _mean(sbcomp, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed ncfo(126d) / smoothed sbcomp(504d) x closeadj
def ocq_f012_operating_cash_quality_rom_sbcomp_504_126d_base_v066_signal(ncfo, sbcomp, closeadj):
    n = _mean(ncfo, 126)
    d = _mean(sbcomp, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ncfo) / std(netinc)
def ocq_f012_operating_cash_quality_volratio_netinc_252d_base_v067_signal(ncfo, netinc):
    n = _std(ncfo, 252)
    d = _std(netinc, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ncfo) / std(netinc)
def ocq_f012_operating_cash_quality_volratio_netinc_504d_base_v068_signal(ncfo, netinc):
    n = _std(ncfo, 504)
    d = _std(netinc, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(ncfo) / std(depamor)
def ocq_f012_operating_cash_quality_volratio_depamor_252d_base_v069_signal(ncfo, depamor):
    n = _std(ncfo, 252)
    d = _std(depamor, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(ncfo) / std(depamor)
def ocq_f012_operating_cash_quality_volratio_depamor_504d_base_v070_signal(ncfo, depamor):
    n = _std(ncfo, 504)
    d = _std(depamor, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed ncfo times closeadj
def ocq_f012_operating_cash_quality_raw_5d_base_v071_signal(ncfo, closeadj):
    result = _mean(ncfo, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed ncfo times closeadj
def ocq_f012_operating_cash_quality_raw_1008d_base_v072_signal(ncfo, closeadj):
    result = _mean(ncfo, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ncfo/netinc
def ocq_f012_operating_cash_quality_log_per_netinc_252d_base_v073_signal(ncfo, netinc):
    s = _operating_cash_quality_scaled(ncfo, netinc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of ncfo/netinc
def ocq_f012_operating_cash_quality_log_per_netinc_504d_base_v074_signal(ncfo, netinc):
    s = _operating_cash_quality_scaled(ncfo, netinc)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of ncfo/depamor
def ocq_f012_operating_cash_quality_log_per_depamor_252d_base_v075_signal(ncfo, depamor):
    s = _operating_cash_quality_scaled(ncfo, depamor)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
