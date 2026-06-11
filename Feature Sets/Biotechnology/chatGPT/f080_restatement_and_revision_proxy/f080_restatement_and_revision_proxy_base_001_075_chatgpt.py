"""Family f080 - Revision and restatement proxy (Fundamental Dynamics) | Sharadar tables: SF1 | fields: datekey, lastupdated, reportperiod, dimension | base 001-075"""
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
def _restatement_and_revision_proxy_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _restatement_and_revision_proxy_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _restatement_and_revision_proxy_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_raw_21d_base_v001_signal(revisioncount, closeadj):
    result = _mean(revisioncount, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_raw_63d_base_v002_signal(revisioncount, closeadj):
    result = _mean(revisioncount, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_raw_126d_base_v003_signal(revisioncount, closeadj):
    result = _mean(revisioncount, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_raw_252d_base_v004_signal(revisioncount, closeadj):
    result = _mean(revisioncount, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_raw_504d_base_v005_signal(revisioncount, closeadj):
    result = _mean(revisioncount, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(revisioncount) times closeadj
def rarp_f080_restatement_and_revision_proxy_log_21d_base_v006_signal(revisioncount, closeadj):
    result = _mean(_restatement_and_revision_proxy_log(revisioncount), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(revisioncount) times closeadj
def rarp_f080_restatement_and_revision_proxy_log_63d_base_v007_signal(revisioncount, closeadj):
    result = _mean(_restatement_and_revision_proxy_log(revisioncount), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(revisioncount) times closeadj
def rarp_f080_restatement_and_revision_proxy_log_126d_base_v008_signal(revisioncount, closeadj):
    result = _mean(_restatement_and_revision_proxy_log(revisioncount), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(revisioncount) times closeadj
def rarp_f080_restatement_and_revision_proxy_log_252d_base_v009_signal(revisioncount, closeadj):
    result = _mean(_restatement_and_revision_proxy_log(revisioncount), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(revisioncount) times closeadj
def rarp_f080_restatement_and_revision_proxy_log_504d_base_v010_signal(revisioncount, closeadj):
    result = _mean(_restatement_and_revision_proxy_log(revisioncount), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revisioncount/datekey mean
def rarp_f080_restatement_and_revision_proxy_per_datekey_63d_base_v011_signal(revisioncount, datekey):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revisioncount/datekey mean
def rarp_f080_restatement_and_revision_proxy_per_datekey_252d_base_v012_signal(revisioncount, datekey):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revisioncount/datekey mean
def rarp_f080_restatement_and_revision_proxy_per_datekey_504d_base_v013_signal(revisioncount, datekey):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, datekey), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revisioncount/dimension mean
def rarp_f080_restatement_and_revision_proxy_per_dimension_63d_base_v014_signal(revisioncount, dimension):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revisioncount/dimension mean
def rarp_f080_restatement_and_revision_proxy_per_dimension_252d_base_v015_signal(revisioncount, dimension):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revisioncount/dimension mean
def rarp_f080_restatement_and_revision_proxy_per_dimension_504d_base_v016_signal(revisioncount, dimension):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, dimension), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revisioncount/assets mean
def rarp_f080_restatement_and_revision_proxy_per_assets_63d_base_v017_signal(revisioncount, assets):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revisioncount/assets mean
def rarp_f080_restatement_and_revision_proxy_per_assets_252d_base_v018_signal(revisioncount, assets):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revisioncount/assets mean
def rarp_f080_restatement_and_revision_proxy_per_assets_504d_base_v019_signal(revisioncount, assets):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revisioncount/marketcap mean
def rarp_f080_restatement_and_revision_proxy_per_marketcap_63d_base_v020_signal(revisioncount, marketcap):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revisioncount/marketcap mean
def rarp_f080_restatement_and_revision_proxy_per_marketcap_252d_base_v021_signal(revisioncount, marketcap):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revisioncount/marketcap mean
def rarp_f080_restatement_and_revision_proxy_per_marketcap_504d_base_v022_signal(revisioncount, marketcap):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revisioncount/equity mean
def rarp_f080_restatement_and_revision_proxy_per_equity_63d_base_v023_signal(revisioncount, equity):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revisioncount/equity mean
def rarp_f080_restatement_and_revision_proxy_per_equity_252d_base_v024_signal(revisioncount, equity):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revisioncount/equity mean
def rarp_f080_restatement_and_revision_proxy_per_equity_504d_base_v025_signal(revisioncount, equity):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revisioncount per share times closeadj
def rarp_f080_restatement_and_revision_proxy_pershare_21d_base_v026_signal(revisioncount, sharesbas, closeadj):
    ps = _restatement_and_revision_proxy_per_share(revisioncount, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revisioncount per share times closeadj
def rarp_f080_restatement_and_revision_proxy_pershare_63d_base_v027_signal(revisioncount, sharesbas, closeadj):
    ps = _restatement_and_revision_proxy_per_share(revisioncount, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d revisioncount per share times closeadj
def rarp_f080_restatement_and_revision_proxy_pershare_126d_base_v028_signal(revisioncount, sharesbas, closeadj):
    ps = _restatement_and_revision_proxy_per_share(revisioncount, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revisioncount per share times closeadj
def rarp_f080_restatement_and_revision_proxy_pershare_252d_base_v029_signal(revisioncount, sharesbas, closeadj):
    ps = _restatement_and_revision_proxy_per_share(revisioncount, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revisioncount per share times closeadj
def rarp_f080_restatement_and_revision_proxy_pershare_504d_base_v030_signal(revisioncount, sharesbas, closeadj):
    ps = _restatement_and_revision_proxy_per_share(revisioncount, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_std_63d_base_v031_signal(revisioncount, closeadj):
    result = _std(revisioncount, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_std_252d_base_v032_signal(revisioncount, closeadj):
    result = _std(revisioncount, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_std_504d_base_v033_signal(revisioncount, closeadj):
    result = _std(revisioncount, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of revisioncount
def rarp_f080_restatement_and_revision_proxy_z_252d_base_v034_signal(revisioncount):
    result = _z(revisioncount, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of revisioncount
def rarp_f080_restatement_and_revision_proxy_z_504d_base_v035_signal(revisioncount):
    result = _z(revisioncount, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(revisioncount)
def rarp_f080_restatement_and_revision_proxy_logz_252d_base_v036_signal(revisioncount):
    result = _z(_restatement_and_revision_proxy_log(revisioncount), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(revisioncount)
def rarp_f080_restatement_and_revision_proxy_logz_504d_base_v037_signal(revisioncount):
    result = _z(_restatement_and_revision_proxy_log(revisioncount), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of revisioncount^2 times closeadj
def rarp_f080_restatement_and_revision_proxy_sq_63d_base_v038_signal(revisioncount, closeadj):
    result = _mean(revisioncount * revisioncount, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of revisioncount^2 times closeadj
def rarp_f080_restatement_and_revision_proxy_sq_252d_base_v039_signal(revisioncount, closeadj):
    result = _mean(revisioncount * revisioncount, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(revisioncount) times closeadj
def rarp_f080_restatement_and_revision_proxy_sign_21d_base_v040_signal(revisioncount, closeadj):
    result = _mean(np.sign(revisioncount), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(revisioncount) times closeadj
def rarp_f080_restatement_and_revision_proxy_sign_63d_base_v041_signal(revisioncount, closeadj):
    result = _mean(np.sign(revisioncount), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(revisioncount) times closeadj
def rarp_f080_restatement_and_revision_proxy_sign_252d_base_v042_signal(revisioncount, closeadj):
    result = _mean(np.sign(revisioncount), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revisioncount/opex mean
def rarp_f080_restatement_and_revision_proxy_per_opex_63d_base_v043_signal(revisioncount, opex):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revisioncount/opex mean
def rarp_f080_restatement_and_revision_proxy_per_opex_252d_base_v044_signal(revisioncount, opex):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revisioncount/ebitda mean
def rarp_f080_restatement_and_revision_proxy_per_ebitda_63d_base_v045_signal(revisioncount, ebitda):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revisioncount/ebitda mean
def rarp_f080_restatement_and_revision_proxy_per_ebitda_252d_base_v046_signal(revisioncount, ebitda):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revisioncount/capex mean
def rarp_f080_restatement_and_revision_proxy_per_capex_63d_base_v047_signal(revisioncount, capex):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revisioncount/capex mean
def rarp_f080_restatement_and_revision_proxy_per_capex_252d_base_v048_signal(revisioncount, capex):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revisioncount/liabilities mean
def rarp_f080_restatement_and_revision_proxy_per_liabilities_63d_base_v049_signal(revisioncount, liabilities):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revisioncount/liabilities mean
def rarp_f080_restatement_and_revision_proxy_per_liabilities_252d_base_v050_signal(revisioncount, liabilities):
    result = _mean(_restatement_and_revision_proxy_scaled(revisioncount, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revisioncount relative to 252d max times closeadj
def rarp_f080_restatement_and_revision_proxy_relmax_252d_base_v051_signal(revisioncount, closeadj):
    peak = revisioncount.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (revisioncount / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revisioncount relative to 504d max times closeadj
def rarp_f080_restatement_and_revision_proxy_relmax_504d_base_v052_signal(revisioncount, closeadj):
    peak = revisioncount.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (revisioncount / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revisioncount relative to 252d min times closeadj
def rarp_f080_restatement_and_revision_proxy_relmin_252d_base_v053_signal(revisioncount, closeadj):
    trough = revisioncount.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (revisioncount / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# revisioncount relative to 504d min times closeadj
def rarp_f080_restatement_and_revision_proxy_relmin_504d_base_v054_signal(revisioncount, closeadj):
    trough = revisioncount.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (revisioncount / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_pct_21d_base_v055_signal(revisioncount, closeadj):
    result = _pct_change(revisioncount, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_pct_63d_base_v056_signal(revisioncount, closeadj):
    result = _pct_change(revisioncount, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_pct_252d_base_v057_signal(revisioncount, closeadj):
    result = _pct_change(revisioncount, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_sum_63d_base_v058_signal(revisioncount, closeadj):
    result = revisioncount.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_sum_252d_base_v059_signal(revisioncount, closeadj):
    result = revisioncount.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_sum_504d_base_v060_signal(revisioncount, closeadj):
    result = revisioncount.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revisioncount(63d) / smoothed datekey(252d) x closeadj
def rarp_f080_restatement_and_revision_proxy_rom_datekey_252_63d_base_v061_signal(revisioncount, datekey, closeadj):
    n = _mean(revisioncount, 63)
    d = _mean(datekey, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revisioncount(126d) / smoothed datekey(504d) x closeadj
def rarp_f080_restatement_and_revision_proxy_rom_datekey_504_126d_base_v062_signal(revisioncount, datekey, closeadj):
    n = _mean(revisioncount, 126)
    d = _mean(datekey, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revisioncount(63d) / smoothed dimension(252d) x closeadj
def rarp_f080_restatement_and_revision_proxy_rom_dimension_252_63d_base_v063_signal(revisioncount, dimension, closeadj):
    n = _mean(revisioncount, 63)
    d = _mean(dimension, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revisioncount(126d) / smoothed dimension(504d) x closeadj
def rarp_f080_restatement_and_revision_proxy_rom_dimension_504_126d_base_v064_signal(revisioncount, dimension, closeadj):
    n = _mean(revisioncount, 126)
    d = _mean(dimension, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revisioncount(63d) / smoothed assets(252d) x closeadj
def rarp_f080_restatement_and_revision_proxy_rom_assets_252_63d_base_v065_signal(revisioncount, assets, closeadj):
    n = _mean(revisioncount, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed revisioncount(126d) / smoothed assets(504d) x closeadj
def rarp_f080_restatement_and_revision_proxy_rom_assets_504_126d_base_v066_signal(revisioncount, assets, closeadj):
    n = _mean(revisioncount, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(revisioncount) / std(datekey)
def rarp_f080_restatement_and_revision_proxy_volratio_datekey_252d_base_v067_signal(revisioncount, datekey):
    n = _std(revisioncount, 252)
    d = _std(datekey, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(revisioncount) / std(datekey)
def rarp_f080_restatement_and_revision_proxy_volratio_datekey_504d_base_v068_signal(revisioncount, datekey):
    n = _std(revisioncount, 504)
    d = _std(datekey, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(revisioncount) / std(dimension)
def rarp_f080_restatement_and_revision_proxy_volratio_dimension_252d_base_v069_signal(revisioncount, dimension):
    n = _std(revisioncount, 252)
    d = _std(dimension, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(revisioncount) / std(dimension)
def rarp_f080_restatement_and_revision_proxy_volratio_dimension_504d_base_v070_signal(revisioncount, dimension):
    n = _std(revisioncount, 504)
    d = _std(dimension, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_raw_5d_base_v071_signal(revisioncount, closeadj):
    result = _mean(revisioncount, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed revisioncount times closeadj
def rarp_f080_restatement_and_revision_proxy_raw_1008d_base_v072_signal(revisioncount, closeadj):
    result = _mean(revisioncount, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of revisioncount/datekey
def rarp_f080_restatement_and_revision_proxy_log_per_datekey_252d_base_v073_signal(revisioncount, datekey):
    s = _restatement_and_revision_proxy_scaled(revisioncount, datekey)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of revisioncount/datekey
def rarp_f080_restatement_and_revision_proxy_log_per_datekey_504d_base_v074_signal(revisioncount, datekey):
    s = _restatement_and_revision_proxy_scaled(revisioncount, datekey)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of revisioncount/dimension
def rarp_f080_restatement_and_revision_proxy_log_per_dimension_252d_base_v075_signal(revisioncount, dimension):
    s = _restatement_and_revision_proxy_scaled(revisioncount, dimension)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
