"""Family f093 - Insider role and cluster behavior (Insiders and Ownership) | Sharadar tables: SF2 | fields: ownername, officertitle, isdirector, isofficer, transactiondate | base 001-075"""
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
def _insider_role_clusters_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _insider_role_clusters_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _insider_role_clusters_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed isdirector times closeadj
def irc_f093_insider_role_clusters_raw_21d_base_v001_signal(isdirector, closeadj):
    result = _mean(isdirector, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed isdirector times closeadj
def irc_f093_insider_role_clusters_raw_63d_base_v002_signal(isdirector, closeadj):
    result = _mean(isdirector, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed isdirector times closeadj
def irc_f093_insider_role_clusters_raw_126d_base_v003_signal(isdirector, closeadj):
    result = _mean(isdirector, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed isdirector times closeadj
def irc_f093_insider_role_clusters_raw_252d_base_v004_signal(isdirector, closeadj):
    result = _mean(isdirector, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed isdirector times closeadj
def irc_f093_insider_role_clusters_raw_504d_base_v005_signal(isdirector, closeadj):
    result = _mean(isdirector, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(isdirector) times closeadj
def irc_f093_insider_role_clusters_log_21d_base_v006_signal(isdirector, closeadj):
    result = _mean(_insider_role_clusters_log(isdirector), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(isdirector) times closeadj
def irc_f093_insider_role_clusters_log_63d_base_v007_signal(isdirector, closeadj):
    result = _mean(_insider_role_clusters_log(isdirector), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(isdirector) times closeadj
def irc_f093_insider_role_clusters_log_126d_base_v008_signal(isdirector, closeadj):
    result = _mean(_insider_role_clusters_log(isdirector), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(isdirector) times closeadj
def irc_f093_insider_role_clusters_log_252d_base_v009_signal(isdirector, closeadj):
    result = _mean(_insider_role_clusters_log(isdirector), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(isdirector) times closeadj
def irc_f093_insider_role_clusters_log_504d_base_v010_signal(isdirector, closeadj):
    result = _mean(_insider_role_clusters_log(isdirector), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d isdirector/isofficer mean
def irc_f093_insider_role_clusters_per_isofficer_63d_base_v011_signal(isdirector, isofficer):
    result = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d isdirector/isofficer mean
def irc_f093_insider_role_clusters_per_isofficer_252d_base_v012_signal(isdirector, isofficer):
    result = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d isdirector/isofficer mean
def irc_f093_insider_role_clusters_per_isofficer_504d_base_v013_signal(isdirector, isofficer):
    result = _mean(_insider_role_clusters_scaled(isdirector, isofficer), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d isdirector/transactiondate mean
def irc_f093_insider_role_clusters_per_transactiondate_63d_base_v014_signal(isdirector, transactiondate):
    result = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d isdirector/transactiondate mean
def irc_f093_insider_role_clusters_per_transactiondate_252d_base_v015_signal(isdirector, transactiondate):
    result = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d isdirector/transactiondate mean
def irc_f093_insider_role_clusters_per_transactiondate_504d_base_v016_signal(isdirector, transactiondate):
    result = _mean(_insider_role_clusters_scaled(isdirector, transactiondate), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d isdirector/assets mean
def irc_f093_insider_role_clusters_per_assets_63d_base_v017_signal(isdirector, assets):
    result = _mean(_insider_role_clusters_scaled(isdirector, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d isdirector/assets mean
def irc_f093_insider_role_clusters_per_assets_252d_base_v018_signal(isdirector, assets):
    result = _mean(_insider_role_clusters_scaled(isdirector, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d isdirector/assets mean
def irc_f093_insider_role_clusters_per_assets_504d_base_v019_signal(isdirector, assets):
    result = _mean(_insider_role_clusters_scaled(isdirector, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d isdirector/marketcap mean
def irc_f093_insider_role_clusters_per_marketcap_63d_base_v020_signal(isdirector, marketcap):
    result = _mean(_insider_role_clusters_scaled(isdirector, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d isdirector/marketcap mean
def irc_f093_insider_role_clusters_per_marketcap_252d_base_v021_signal(isdirector, marketcap):
    result = _mean(_insider_role_clusters_scaled(isdirector, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d isdirector/marketcap mean
def irc_f093_insider_role_clusters_per_marketcap_504d_base_v022_signal(isdirector, marketcap):
    result = _mean(_insider_role_clusters_scaled(isdirector, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d isdirector/equity mean
def irc_f093_insider_role_clusters_per_equity_63d_base_v023_signal(isdirector, equity):
    result = _mean(_insider_role_clusters_scaled(isdirector, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d isdirector/equity mean
def irc_f093_insider_role_clusters_per_equity_252d_base_v024_signal(isdirector, equity):
    result = _mean(_insider_role_clusters_scaled(isdirector, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d isdirector/equity mean
def irc_f093_insider_role_clusters_per_equity_504d_base_v025_signal(isdirector, equity):
    result = _mean(_insider_role_clusters_scaled(isdirector, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d isdirector per share times closeadj
def irc_f093_insider_role_clusters_pershare_21d_base_v026_signal(isdirector, sharesbas, closeadj):
    ps = _insider_role_clusters_per_share(isdirector, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d isdirector per share times closeadj
def irc_f093_insider_role_clusters_pershare_63d_base_v027_signal(isdirector, sharesbas, closeadj):
    ps = _insider_role_clusters_per_share(isdirector, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d isdirector per share times closeadj
def irc_f093_insider_role_clusters_pershare_126d_base_v028_signal(isdirector, sharesbas, closeadj):
    ps = _insider_role_clusters_per_share(isdirector, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d isdirector per share times closeadj
def irc_f093_insider_role_clusters_pershare_252d_base_v029_signal(isdirector, sharesbas, closeadj):
    ps = _insider_role_clusters_per_share(isdirector, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d isdirector per share times closeadj
def irc_f093_insider_role_clusters_pershare_504d_base_v030_signal(isdirector, sharesbas, closeadj):
    ps = _insider_role_clusters_per_share(isdirector, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of isdirector times closeadj
def irc_f093_insider_role_clusters_std_63d_base_v031_signal(isdirector, closeadj):
    result = _std(isdirector, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of isdirector times closeadj
def irc_f093_insider_role_clusters_std_252d_base_v032_signal(isdirector, closeadj):
    result = _std(isdirector, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of isdirector times closeadj
def irc_f093_insider_role_clusters_std_504d_base_v033_signal(isdirector, closeadj):
    result = _std(isdirector, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of isdirector
def irc_f093_insider_role_clusters_z_252d_base_v034_signal(isdirector):
    result = _z(isdirector, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of isdirector
def irc_f093_insider_role_clusters_z_504d_base_v035_signal(isdirector):
    result = _z(isdirector, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(isdirector)
def irc_f093_insider_role_clusters_logz_252d_base_v036_signal(isdirector):
    result = _z(_insider_role_clusters_log(isdirector), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(isdirector)
def irc_f093_insider_role_clusters_logz_504d_base_v037_signal(isdirector):
    result = _z(_insider_role_clusters_log(isdirector), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of isdirector^2 times closeadj
def irc_f093_insider_role_clusters_sq_63d_base_v038_signal(isdirector, closeadj):
    result = _mean(isdirector * isdirector, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of isdirector^2 times closeadj
def irc_f093_insider_role_clusters_sq_252d_base_v039_signal(isdirector, closeadj):
    result = _mean(isdirector * isdirector, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(isdirector) times closeadj
def irc_f093_insider_role_clusters_sign_21d_base_v040_signal(isdirector, closeadj):
    result = _mean(np.sign(isdirector), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(isdirector) times closeadj
def irc_f093_insider_role_clusters_sign_63d_base_v041_signal(isdirector, closeadj):
    result = _mean(np.sign(isdirector), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(isdirector) times closeadj
def irc_f093_insider_role_clusters_sign_252d_base_v042_signal(isdirector, closeadj):
    result = _mean(np.sign(isdirector), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d isdirector/opex mean
def irc_f093_insider_role_clusters_per_opex_63d_base_v043_signal(isdirector, opex):
    result = _mean(_insider_role_clusters_scaled(isdirector, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d isdirector/opex mean
def irc_f093_insider_role_clusters_per_opex_252d_base_v044_signal(isdirector, opex):
    result = _mean(_insider_role_clusters_scaled(isdirector, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d isdirector/ebitda mean
def irc_f093_insider_role_clusters_per_ebitda_63d_base_v045_signal(isdirector, ebitda):
    result = _mean(_insider_role_clusters_scaled(isdirector, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d isdirector/ebitda mean
def irc_f093_insider_role_clusters_per_ebitda_252d_base_v046_signal(isdirector, ebitda):
    result = _mean(_insider_role_clusters_scaled(isdirector, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d isdirector/capex mean
def irc_f093_insider_role_clusters_per_capex_63d_base_v047_signal(isdirector, capex):
    result = _mean(_insider_role_clusters_scaled(isdirector, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d isdirector/capex mean
def irc_f093_insider_role_clusters_per_capex_252d_base_v048_signal(isdirector, capex):
    result = _mean(_insider_role_clusters_scaled(isdirector, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d isdirector/liabilities mean
def irc_f093_insider_role_clusters_per_liabilities_63d_base_v049_signal(isdirector, liabilities):
    result = _mean(_insider_role_clusters_scaled(isdirector, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d isdirector/liabilities mean
def irc_f093_insider_role_clusters_per_liabilities_252d_base_v050_signal(isdirector, liabilities):
    result = _mean(_insider_role_clusters_scaled(isdirector, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# isdirector relative to 252d max times closeadj
def irc_f093_insider_role_clusters_relmax_252d_base_v051_signal(isdirector, closeadj):
    peak = isdirector.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (isdirector / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# isdirector relative to 504d max times closeadj
def irc_f093_insider_role_clusters_relmax_504d_base_v052_signal(isdirector, closeadj):
    peak = isdirector.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (isdirector / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# isdirector relative to 252d min times closeadj
def irc_f093_insider_role_clusters_relmin_252d_base_v053_signal(isdirector, closeadj):
    trough = isdirector.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (isdirector / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# isdirector relative to 504d min times closeadj
def irc_f093_insider_role_clusters_relmin_504d_base_v054_signal(isdirector, closeadj):
    trough = isdirector.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (isdirector / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of isdirector times closeadj
def irc_f093_insider_role_clusters_pct_21d_base_v055_signal(isdirector, closeadj):
    result = _pct_change(isdirector, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of isdirector times closeadj
def irc_f093_insider_role_clusters_pct_63d_base_v056_signal(isdirector, closeadj):
    result = _pct_change(isdirector, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of isdirector times closeadj
def irc_f093_insider_role_clusters_pct_252d_base_v057_signal(isdirector, closeadj):
    result = _pct_change(isdirector, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of isdirector times closeadj
def irc_f093_insider_role_clusters_sum_63d_base_v058_signal(isdirector, closeadj):
    result = isdirector.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of isdirector times closeadj
def irc_f093_insider_role_clusters_sum_252d_base_v059_signal(isdirector, closeadj):
    result = isdirector.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of isdirector times closeadj
def irc_f093_insider_role_clusters_sum_504d_base_v060_signal(isdirector, closeadj):
    result = isdirector.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed isdirector(63d) / smoothed isofficer(252d) x closeadj
def irc_f093_insider_role_clusters_rom_isofficer_252_63d_base_v061_signal(isdirector, isofficer, closeadj):
    n = _mean(isdirector, 63)
    d = _mean(isofficer, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed isdirector(126d) / smoothed isofficer(504d) x closeadj
def irc_f093_insider_role_clusters_rom_isofficer_504_126d_base_v062_signal(isdirector, isofficer, closeadj):
    n = _mean(isdirector, 126)
    d = _mean(isofficer, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed isdirector(63d) / smoothed transactiondate(252d) x closeadj
def irc_f093_insider_role_clusters_rom_transactiondate_252_63d_base_v063_signal(isdirector, transactiondate, closeadj):
    n = _mean(isdirector, 63)
    d = _mean(transactiondate, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed isdirector(126d) / smoothed transactiondate(504d) x closeadj
def irc_f093_insider_role_clusters_rom_transactiondate_504_126d_base_v064_signal(isdirector, transactiondate, closeadj):
    n = _mean(isdirector, 126)
    d = _mean(transactiondate, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed isdirector(63d) / smoothed assets(252d) x closeadj
def irc_f093_insider_role_clusters_rom_assets_252_63d_base_v065_signal(isdirector, assets, closeadj):
    n = _mean(isdirector, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed isdirector(126d) / smoothed assets(504d) x closeadj
def irc_f093_insider_role_clusters_rom_assets_504_126d_base_v066_signal(isdirector, assets, closeadj):
    n = _mean(isdirector, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(isdirector) / std(isofficer)
def irc_f093_insider_role_clusters_volratio_isofficer_252d_base_v067_signal(isdirector, isofficer):
    n = _std(isdirector, 252)
    d = _std(isofficer, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(isdirector) / std(isofficer)
def irc_f093_insider_role_clusters_volratio_isofficer_504d_base_v068_signal(isdirector, isofficer):
    n = _std(isdirector, 504)
    d = _std(isofficer, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(isdirector) / std(transactiondate)
def irc_f093_insider_role_clusters_volratio_transactiondate_252d_base_v069_signal(isdirector, transactiondate):
    n = _std(isdirector, 252)
    d = _std(transactiondate, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(isdirector) / std(transactiondate)
def irc_f093_insider_role_clusters_volratio_transactiondate_504d_base_v070_signal(isdirector, transactiondate):
    n = _std(isdirector, 504)
    d = _std(transactiondate, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed isdirector times closeadj
def irc_f093_insider_role_clusters_raw_5d_base_v071_signal(isdirector, closeadj):
    result = _mean(isdirector, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed isdirector times closeadj
def irc_f093_insider_role_clusters_raw_1008d_base_v072_signal(isdirector, closeadj):
    result = _mean(isdirector, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of isdirector/isofficer
def irc_f093_insider_role_clusters_log_per_isofficer_252d_base_v073_signal(isdirector, isofficer):
    s = _insider_role_clusters_scaled(isdirector, isofficer)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of isdirector/isofficer
def irc_f093_insider_role_clusters_log_per_isofficer_504d_base_v074_signal(isdirector, isofficer):
    s = _insider_role_clusters_scaled(isdirector, isofficer)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of isdirector/transactiondate
def irc_f093_insider_role_clusters_log_per_transactiondate_252d_base_v075_signal(isdirector, transactiondate):
    s = _insider_role_clusters_scaled(isdirector, transactiondate)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
