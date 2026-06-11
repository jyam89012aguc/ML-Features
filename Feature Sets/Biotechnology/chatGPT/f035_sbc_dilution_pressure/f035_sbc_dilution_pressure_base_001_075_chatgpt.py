"""Family f035 - SBC dilution pressure (Dilution and Share Count) | Sharadar tables: SF1 | fields: sbcomp, sharesbas, marketcap | base 001-075"""
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
def _sbc_dilution_pressure_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _sbc_dilution_pressure_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _sbc_dilution_pressure_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_raw_21d_base_v001_signal(sbcomp, closeadj):
    result = _mean(sbcomp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_raw_63d_base_v002_signal(sbcomp, closeadj):
    result = _mean(sbcomp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_raw_126d_base_v003_signal(sbcomp, closeadj):
    result = _mean(sbcomp, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_raw_252d_base_v004_signal(sbcomp, closeadj):
    result = _mean(sbcomp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_raw_504d_base_v005_signal(sbcomp, closeadj):
    result = _mean(sbcomp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(sbcomp) times closeadj
def sdp_f035_sbc_dilution_pressure_log_21d_base_v006_signal(sbcomp, closeadj):
    result = _mean(_sbc_dilution_pressure_log(sbcomp), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(sbcomp) times closeadj
def sdp_f035_sbc_dilution_pressure_log_63d_base_v007_signal(sbcomp, closeadj):
    result = _mean(_sbc_dilution_pressure_log(sbcomp), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(sbcomp) times closeadj
def sdp_f035_sbc_dilution_pressure_log_126d_base_v008_signal(sbcomp, closeadj):
    result = _mean(_sbc_dilution_pressure_log(sbcomp), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(sbcomp) times closeadj
def sdp_f035_sbc_dilution_pressure_log_252d_base_v009_signal(sbcomp, closeadj):
    result = _mean(_sbc_dilution_pressure_log(sbcomp), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(sbcomp) times closeadj
def sdp_f035_sbc_dilution_pressure_log_504d_base_v010_signal(sbcomp, closeadj):
    result = _mean(_sbc_dilution_pressure_log(sbcomp), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sbcomp/sharesbas mean
def sdp_f035_sbc_dilution_pressure_per_sharesbas_63d_base_v011_signal(sbcomp, sharesbas):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, sharesbas), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sbcomp/sharesbas mean
def sdp_f035_sbc_dilution_pressure_per_sharesbas_252d_base_v012_signal(sbcomp, sharesbas):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, sharesbas), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sbcomp/sharesbas mean
def sdp_f035_sbc_dilution_pressure_per_sharesbas_504d_base_v013_signal(sbcomp, sharesbas):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, sharesbas), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sbcomp/marketcap mean
def sdp_f035_sbc_dilution_pressure_per_marketcap_63d_base_v014_signal(sbcomp, marketcap):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sbcomp/marketcap mean
def sdp_f035_sbc_dilution_pressure_per_marketcap_252d_base_v015_signal(sbcomp, marketcap):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sbcomp/marketcap mean
def sdp_f035_sbc_dilution_pressure_per_marketcap_504d_base_v016_signal(sbcomp, marketcap):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sbcomp/assets mean
def sdp_f035_sbc_dilution_pressure_per_assets_63d_base_v017_signal(sbcomp, assets):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sbcomp/assets mean
def sdp_f035_sbc_dilution_pressure_per_assets_252d_base_v018_signal(sbcomp, assets):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sbcomp/assets mean
def sdp_f035_sbc_dilution_pressure_per_assets_504d_base_v019_signal(sbcomp, assets):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sbcomp/equity mean
def sdp_f035_sbc_dilution_pressure_per_equity_63d_base_v020_signal(sbcomp, equity):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sbcomp/equity mean
def sdp_f035_sbc_dilution_pressure_per_equity_252d_base_v021_signal(sbcomp, equity):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sbcomp/equity mean
def sdp_f035_sbc_dilution_pressure_per_equity_504d_base_v022_signal(sbcomp, equity):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sbcomp/debt mean
def sdp_f035_sbc_dilution_pressure_per_debt_63d_base_v023_signal(sbcomp, debt):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, debt), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sbcomp/debt mean
def sdp_f035_sbc_dilution_pressure_per_debt_252d_base_v024_signal(sbcomp, debt):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, debt), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sbcomp/debt mean
def sdp_f035_sbc_dilution_pressure_per_debt_504d_base_v025_signal(sbcomp, debt):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, debt), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sbcomp per share times closeadj
def sdp_f035_sbc_dilution_pressure_pershare_21d_base_v026_signal(sbcomp, sharesbas, closeadj):
    ps = _sbc_dilution_pressure_per_share(sbcomp, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sbcomp per share times closeadj
def sdp_f035_sbc_dilution_pressure_pershare_63d_base_v027_signal(sbcomp, sharesbas, closeadj):
    ps = _sbc_dilution_pressure_per_share(sbcomp, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d sbcomp per share times closeadj
def sdp_f035_sbc_dilution_pressure_pershare_126d_base_v028_signal(sbcomp, sharesbas, closeadj):
    ps = _sbc_dilution_pressure_per_share(sbcomp, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sbcomp per share times closeadj
def sdp_f035_sbc_dilution_pressure_pershare_252d_base_v029_signal(sbcomp, sharesbas, closeadj):
    ps = _sbc_dilution_pressure_per_share(sbcomp, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sbcomp per share times closeadj
def sdp_f035_sbc_dilution_pressure_pershare_504d_base_v030_signal(sbcomp, sharesbas, closeadj):
    ps = _sbc_dilution_pressure_per_share(sbcomp, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_std_63d_base_v031_signal(sbcomp, closeadj):
    result = _std(sbcomp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_std_252d_base_v032_signal(sbcomp, closeadj):
    result = _std(sbcomp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_std_504d_base_v033_signal(sbcomp, closeadj):
    result = _std(sbcomp, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of sbcomp
def sdp_f035_sbc_dilution_pressure_z_252d_base_v034_signal(sbcomp):
    result = _z(sbcomp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of sbcomp
def sdp_f035_sbc_dilution_pressure_z_504d_base_v035_signal(sbcomp):
    result = _z(sbcomp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(sbcomp)
def sdp_f035_sbc_dilution_pressure_logz_252d_base_v036_signal(sbcomp):
    result = _z(_sbc_dilution_pressure_log(sbcomp), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(sbcomp)
def sdp_f035_sbc_dilution_pressure_logz_504d_base_v037_signal(sbcomp):
    result = _z(_sbc_dilution_pressure_log(sbcomp), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sbcomp^2 times closeadj
def sdp_f035_sbc_dilution_pressure_sq_63d_base_v038_signal(sbcomp, closeadj):
    result = _mean(sbcomp * sbcomp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sbcomp^2 times closeadj
def sdp_f035_sbc_dilution_pressure_sq_252d_base_v039_signal(sbcomp, closeadj):
    result = _mean(sbcomp * sbcomp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(sbcomp) times closeadj
def sdp_f035_sbc_dilution_pressure_sign_21d_base_v040_signal(sbcomp, closeadj):
    result = _mean(np.sign(sbcomp), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(sbcomp) times closeadj
def sdp_f035_sbc_dilution_pressure_sign_63d_base_v041_signal(sbcomp, closeadj):
    result = _mean(np.sign(sbcomp), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(sbcomp) times closeadj
def sdp_f035_sbc_dilution_pressure_sign_252d_base_v042_signal(sbcomp, closeadj):
    result = _mean(np.sign(sbcomp), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sbcomp/opex mean
def sdp_f035_sbc_dilution_pressure_per_opex_63d_base_v043_signal(sbcomp, opex):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sbcomp/opex mean
def sdp_f035_sbc_dilution_pressure_per_opex_252d_base_v044_signal(sbcomp, opex):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sbcomp/ebitda mean
def sdp_f035_sbc_dilution_pressure_per_ebitda_63d_base_v045_signal(sbcomp, ebitda):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sbcomp/ebitda mean
def sdp_f035_sbc_dilution_pressure_per_ebitda_252d_base_v046_signal(sbcomp, ebitda):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sbcomp/capex mean
def sdp_f035_sbc_dilution_pressure_per_capex_63d_base_v047_signal(sbcomp, capex):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sbcomp/capex mean
def sdp_f035_sbc_dilution_pressure_per_capex_252d_base_v048_signal(sbcomp, capex):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sbcomp/liabilities mean
def sdp_f035_sbc_dilution_pressure_per_liabilities_63d_base_v049_signal(sbcomp, liabilities):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sbcomp/liabilities mean
def sdp_f035_sbc_dilution_pressure_per_liabilities_252d_base_v050_signal(sbcomp, liabilities):
    result = _mean(_sbc_dilution_pressure_scaled(sbcomp, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# sbcomp relative to 252d max times closeadj
def sdp_f035_sbc_dilution_pressure_relmax_252d_base_v051_signal(sbcomp, closeadj):
    peak = sbcomp.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (sbcomp / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sbcomp relative to 504d max times closeadj
def sdp_f035_sbc_dilution_pressure_relmax_504d_base_v052_signal(sbcomp, closeadj):
    peak = sbcomp.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (sbcomp / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sbcomp relative to 252d min times closeadj
def sdp_f035_sbc_dilution_pressure_relmin_252d_base_v053_signal(sbcomp, closeadj):
    trough = sbcomp.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (sbcomp / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sbcomp relative to 504d min times closeadj
def sdp_f035_sbc_dilution_pressure_relmin_504d_base_v054_signal(sbcomp, closeadj):
    trough = sbcomp.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (sbcomp / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_pct_21d_base_v055_signal(sbcomp, closeadj):
    result = _pct_change(sbcomp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_pct_63d_base_v056_signal(sbcomp, closeadj):
    result = _pct_change(sbcomp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_pct_252d_base_v057_signal(sbcomp, closeadj):
    result = _pct_change(sbcomp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_sum_63d_base_v058_signal(sbcomp, closeadj):
    result = sbcomp.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_sum_252d_base_v059_signal(sbcomp, closeadj):
    result = sbcomp.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_sum_504d_base_v060_signal(sbcomp, closeadj):
    result = sbcomp.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sbcomp(63d) / smoothed sharesbas(252d) x closeadj
def sdp_f035_sbc_dilution_pressure_rom_sharesbas_252_63d_base_v061_signal(sbcomp, sharesbas, closeadj):
    n = _mean(sbcomp, 63)
    d = _mean(sharesbas, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sbcomp(126d) / smoothed sharesbas(504d) x closeadj
def sdp_f035_sbc_dilution_pressure_rom_sharesbas_504_126d_base_v062_signal(sbcomp, sharesbas, closeadj):
    n = _mean(sbcomp, 126)
    d = _mean(sharesbas, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sbcomp(63d) / smoothed marketcap(252d) x closeadj
def sdp_f035_sbc_dilution_pressure_rom_marketcap_252_63d_base_v063_signal(sbcomp, marketcap, closeadj):
    n = _mean(sbcomp, 63)
    d = _mean(marketcap, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sbcomp(126d) / smoothed marketcap(504d) x closeadj
def sdp_f035_sbc_dilution_pressure_rom_marketcap_504_126d_base_v064_signal(sbcomp, marketcap, closeadj):
    n = _mean(sbcomp, 126)
    d = _mean(marketcap, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sbcomp(63d) / smoothed assets(252d) x closeadj
def sdp_f035_sbc_dilution_pressure_rom_assets_252_63d_base_v065_signal(sbcomp, assets, closeadj):
    n = _mean(sbcomp, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed sbcomp(126d) / smoothed assets(504d) x closeadj
def sdp_f035_sbc_dilution_pressure_rom_assets_504_126d_base_v066_signal(sbcomp, assets, closeadj):
    n = _mean(sbcomp, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sbcomp) / std(sharesbas)
def sdp_f035_sbc_dilution_pressure_volratio_sharesbas_252d_base_v067_signal(sbcomp, sharesbas):
    n = _std(sbcomp, 252)
    d = _std(sharesbas, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sbcomp) / std(sharesbas)
def sdp_f035_sbc_dilution_pressure_volratio_sharesbas_504d_base_v068_signal(sbcomp, sharesbas):
    n = _std(sbcomp, 504)
    d = _std(sharesbas, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(sbcomp) / std(marketcap)
def sdp_f035_sbc_dilution_pressure_volratio_marketcap_252d_base_v069_signal(sbcomp, marketcap):
    n = _std(sbcomp, 252)
    d = _std(marketcap, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(sbcomp) / std(marketcap)
def sdp_f035_sbc_dilution_pressure_volratio_marketcap_504d_base_v070_signal(sbcomp, marketcap):
    n = _std(sbcomp, 504)
    d = _std(marketcap, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_raw_5d_base_v071_signal(sbcomp, closeadj):
    result = _mean(sbcomp, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed sbcomp times closeadj
def sdp_f035_sbc_dilution_pressure_raw_1008d_base_v072_signal(sbcomp, closeadj):
    result = _mean(sbcomp, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sbcomp/sharesbas
def sdp_f035_sbc_dilution_pressure_log_per_sharesbas_252d_base_v073_signal(sbcomp, sharesbas):
    s = _sbc_dilution_pressure_scaled(sbcomp, sharesbas)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of sbcomp/sharesbas
def sdp_f035_sbc_dilution_pressure_log_per_sharesbas_504d_base_v074_signal(sbcomp, sharesbas):
    s = _sbc_dilution_pressure_scaled(sbcomp, sharesbas)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of sbcomp/marketcap
def sdp_f035_sbc_dilution_pressure_log_per_marketcap_252d_base_v075_signal(sbcomp, marketcap):
    s = _sbc_dilution_pressure_scaled(sbcomp, marketcap)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
