"""Family f079 - Financial statement timeliness (Fundamental Dynamics) | Sharadar tables: SF1 | fields: calendardate, reportperiod, datekey, lastupdated | base 001-075"""
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
def _reporting_recency_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _reporting_recency_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _reporting_recency_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 21d smoothed filingage times closeadj
def rr_f079_reporting_recency_raw_21d_base_v001_signal(filingage, closeadj):
    result = _mean(filingage, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed filingage times closeadj
def rr_f079_reporting_recency_raw_63d_base_v002_signal(filingage, closeadj):
    result = _mean(filingage, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed filingage times closeadj
def rr_f079_reporting_recency_raw_126d_base_v003_signal(filingage, closeadj):
    result = _mean(filingage, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed filingage times closeadj
def rr_f079_reporting_recency_raw_252d_base_v004_signal(filingage, closeadj):
    result = _mean(filingage, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed filingage times closeadj
def rr_f079_reporting_recency_raw_504d_base_v005_signal(filingage, closeadj):
    result = _mean(filingage, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed log(filingage) times closeadj
def rr_f079_reporting_recency_log_21d_base_v006_signal(filingage, closeadj):
    result = _mean(_reporting_recency_log(filingage), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed log(filingage) times closeadj
def rr_f079_reporting_recency_log_63d_base_v007_signal(filingage, closeadj):
    result = _mean(_reporting_recency_log(filingage), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed log(filingage) times closeadj
def rr_f079_reporting_recency_log_126d_base_v008_signal(filingage, closeadj):
    result = _mean(_reporting_recency_log(filingage), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed log(filingage) times closeadj
def rr_f079_reporting_recency_log_252d_base_v009_signal(filingage, closeadj):
    result = _mean(_reporting_recency_log(filingage), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed log(filingage) times closeadj
def rr_f079_reporting_recency_log_504d_base_v010_signal(filingage, closeadj):
    result = _mean(_reporting_recency_log(filingage), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d filingage/calendardate mean
def rr_f079_reporting_recency_per_calendardate_63d_base_v011_signal(filingage, calendardate):
    result = _mean(_reporting_recency_scaled(filingage, calendardate), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d filingage/calendardate mean
def rr_f079_reporting_recency_per_calendardate_252d_base_v012_signal(filingage, calendardate):
    result = _mean(_reporting_recency_scaled(filingage, calendardate), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d filingage/calendardate mean
def rr_f079_reporting_recency_per_calendardate_504d_base_v013_signal(filingage, calendardate):
    result = _mean(_reporting_recency_scaled(filingage, calendardate), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d filingage/datekey mean
def rr_f079_reporting_recency_per_datekey_63d_base_v014_signal(filingage, datekey):
    result = _mean(_reporting_recency_scaled(filingage, datekey), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d filingage/datekey mean
def rr_f079_reporting_recency_per_datekey_252d_base_v015_signal(filingage, datekey):
    result = _mean(_reporting_recency_scaled(filingage, datekey), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d filingage/datekey mean
def rr_f079_reporting_recency_per_datekey_504d_base_v016_signal(filingage, datekey):
    result = _mean(_reporting_recency_scaled(filingage, datekey), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d filingage/assets mean
def rr_f079_reporting_recency_per_assets_63d_base_v017_signal(filingage, assets):
    result = _mean(_reporting_recency_scaled(filingage, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d filingage/assets mean
def rr_f079_reporting_recency_per_assets_252d_base_v018_signal(filingage, assets):
    result = _mean(_reporting_recency_scaled(filingage, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d filingage/assets mean
def rr_f079_reporting_recency_per_assets_504d_base_v019_signal(filingage, assets):
    result = _mean(_reporting_recency_scaled(filingage, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d filingage/marketcap mean
def rr_f079_reporting_recency_per_marketcap_63d_base_v020_signal(filingage, marketcap):
    result = _mean(_reporting_recency_scaled(filingage, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d filingage/marketcap mean
def rr_f079_reporting_recency_per_marketcap_252d_base_v021_signal(filingage, marketcap):
    result = _mean(_reporting_recency_scaled(filingage, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d filingage/marketcap mean
def rr_f079_reporting_recency_per_marketcap_504d_base_v022_signal(filingage, marketcap):
    result = _mean(_reporting_recency_scaled(filingage, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d filingage/equity mean
def rr_f079_reporting_recency_per_equity_63d_base_v023_signal(filingage, equity):
    result = _mean(_reporting_recency_scaled(filingage, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d filingage/equity mean
def rr_f079_reporting_recency_per_equity_252d_base_v024_signal(filingage, equity):
    result = _mean(_reporting_recency_scaled(filingage, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d filingage/equity mean
def rr_f079_reporting_recency_per_equity_504d_base_v025_signal(filingage, equity):
    result = _mean(_reporting_recency_scaled(filingage, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d filingage per share times closeadj
def rr_f079_reporting_recency_pershare_21d_base_v026_signal(filingage, sharesbas, closeadj):
    ps = _reporting_recency_per_share(filingage, sharesbas)
    result = _mean(ps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d filingage per share times closeadj
def rr_f079_reporting_recency_pershare_63d_base_v027_signal(filingage, sharesbas, closeadj):
    ps = _reporting_recency_per_share(filingage, sharesbas)
    result = _mean(ps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d filingage per share times closeadj
def rr_f079_reporting_recency_pershare_126d_base_v028_signal(filingage, sharesbas, closeadj):
    ps = _reporting_recency_per_share(filingage, sharesbas)
    result = _mean(ps, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d filingage per share times closeadj
def rr_f079_reporting_recency_pershare_252d_base_v029_signal(filingage, sharesbas, closeadj):
    ps = _reporting_recency_per_share(filingage, sharesbas)
    result = _mean(ps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d filingage per share times closeadj
def rr_f079_reporting_recency_pershare_504d_base_v030_signal(filingage, sharesbas, closeadj):
    ps = _reporting_recency_per_share(filingage, sharesbas)
    result = _mean(ps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of filingage times closeadj
def rr_f079_reporting_recency_std_63d_base_v031_signal(filingage, closeadj):
    result = _std(filingage, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling std of filingage times closeadj
def rr_f079_reporting_recency_std_252d_base_v032_signal(filingage, closeadj):
    result = _std(filingage, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling std of filingage times closeadj
def rr_f079_reporting_recency_std_504d_base_v033_signal(filingage, closeadj):
    result = _std(filingage, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of filingage
def rr_f079_reporting_recency_z_252d_base_v034_signal(filingage):
    result = _z(filingage, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of filingage
def rr_f079_reporting_recency_z_504d_base_v035_signal(filingage):
    result = _z(filingage, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of log(filingage)
def rr_f079_reporting_recency_logz_252d_base_v036_signal(filingage):
    result = _z(_reporting_recency_log(filingage), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of log(filingage)
def rr_f079_reporting_recency_logz_504d_base_v037_signal(filingage):
    result = _z(_reporting_recency_log(filingage), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of filingage^2 times closeadj
def rr_f079_reporting_recency_sq_63d_base_v038_signal(filingage, closeadj):
    result = _mean(filingage * filingage, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of filingage^2 times closeadj
def rr_f079_reporting_recency_sq_252d_base_v039_signal(filingage, closeadj):
    result = _mean(filingage * filingage, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of sign(filingage) times closeadj
def rr_f079_reporting_recency_sign_21d_base_v040_signal(filingage, closeadj):
    result = _mean(np.sign(filingage), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of sign(filingage) times closeadj
def rr_f079_reporting_recency_sign_63d_base_v041_signal(filingage, closeadj):
    result = _mean(np.sign(filingage), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of sign(filingage) times closeadj
def rr_f079_reporting_recency_sign_252d_base_v042_signal(filingage, closeadj):
    result = _mean(np.sign(filingage), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d filingage/opex mean
def rr_f079_reporting_recency_per_opex_63d_base_v043_signal(filingage, opex):
    result = _mean(_reporting_recency_scaled(filingage, opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d filingage/opex mean
def rr_f079_reporting_recency_per_opex_252d_base_v044_signal(filingage, opex):
    result = _mean(_reporting_recency_scaled(filingage, opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d filingage/ebitda mean
def rr_f079_reporting_recency_per_ebitda_63d_base_v045_signal(filingage, ebitda):
    result = _mean(_reporting_recency_scaled(filingage, ebitda), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d filingage/ebitda mean
def rr_f079_reporting_recency_per_ebitda_252d_base_v046_signal(filingage, ebitda):
    result = _mean(_reporting_recency_scaled(filingage, ebitda), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d filingage/capex mean
def rr_f079_reporting_recency_per_capex_63d_base_v047_signal(filingage, capex):
    result = _mean(_reporting_recency_scaled(filingage, capex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d filingage/capex mean
def rr_f079_reporting_recency_per_capex_252d_base_v048_signal(filingage, capex):
    result = _mean(_reporting_recency_scaled(filingage, capex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d filingage/liabilities mean
def rr_f079_reporting_recency_per_liabilities_63d_base_v049_signal(filingage, liabilities):
    result = _mean(_reporting_recency_scaled(filingage, liabilities), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d filingage/liabilities mean
def rr_f079_reporting_recency_per_liabilities_252d_base_v050_signal(filingage, liabilities):
    result = _mean(_reporting_recency_scaled(filingage, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# filingage relative to 252d max times closeadj
def rr_f079_reporting_recency_relmax_252d_base_v051_signal(filingage, closeadj):
    peak = filingage.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (filingage / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# filingage relative to 504d max times closeadj
def rr_f079_reporting_recency_relmax_504d_base_v052_signal(filingage, closeadj):
    peak = filingage.rolling(504, min_periods=63).max().replace(0, np.nan)
    result = (filingage / peak.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# filingage relative to 252d min times closeadj
def rr_f079_reporting_recency_relmin_252d_base_v053_signal(filingage, closeadj):
    trough = filingage.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (filingage / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# filingage relative to 504d min times closeadj
def rr_f079_reporting_recency_relmin_504d_base_v054_signal(filingage, closeadj):
    trough = filingage.rolling(504, min_periods=63).min().replace(0, np.nan)
    result = (filingage / trough.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pct-change of filingage times closeadj
def rr_f079_reporting_recency_pct_21d_base_v055_signal(filingage, closeadj):
    result = _pct_change(filingage, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pct-change of filingage times closeadj
def rr_f079_reporting_recency_pct_63d_base_v056_signal(filingage, closeadj):
    result = _pct_change(filingage, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pct-change of filingage times closeadj
def rr_f079_reporting_recency_pct_252d_base_v057_signal(filingage, closeadj):
    result = _pct_change(filingage, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of filingage times closeadj
def rr_f079_reporting_recency_sum_63d_base_v058_signal(filingage, closeadj):
    result = filingage.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling sum of filingage times closeadj
def rr_f079_reporting_recency_sum_252d_base_v059_signal(filingage, closeadj):
    result = filingage.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling sum of filingage times closeadj
def rr_f079_reporting_recency_sum_504d_base_v060_signal(filingage, closeadj):
    result = filingage.rolling(504, min_periods=max(1, 504//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed filingage(63d) / smoothed calendardate(252d) x closeadj
def rr_f079_reporting_recency_rom_calendardate_252_63d_base_v061_signal(filingage, calendardate, closeadj):
    n = _mean(filingage, 63)
    d = _mean(calendardate, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed filingage(126d) / smoothed calendardate(504d) x closeadj
def rr_f079_reporting_recency_rom_calendardate_504_126d_base_v062_signal(filingage, calendardate, closeadj):
    n = _mean(filingage, 126)
    d = _mean(calendardate, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed filingage(63d) / smoothed datekey(252d) x closeadj
def rr_f079_reporting_recency_rom_datekey_252_63d_base_v063_signal(filingage, datekey, closeadj):
    n = _mean(filingage, 63)
    d = _mean(datekey, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed filingage(126d) / smoothed datekey(504d) x closeadj
def rr_f079_reporting_recency_rom_datekey_504_126d_base_v064_signal(filingage, datekey, closeadj):
    n = _mean(filingage, 126)
    d = _mean(datekey, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed filingage(63d) / smoothed assets(252d) x closeadj
def rr_f079_reporting_recency_rom_assets_252_63d_base_v065_signal(filingage, assets, closeadj):
    n = _mean(filingage, 63)
    d = _mean(assets, 252).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed filingage(126d) / smoothed assets(504d) x closeadj
def rr_f079_reporting_recency_rom_assets_504_126d_base_v066_signal(filingage, assets, closeadj):
    n = _mean(filingage, 126)
    d = _mean(assets, 504).replace(0, np.nan)
    result = (n / d.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(filingage) / std(calendardate)
def rr_f079_reporting_recency_volratio_calendardate_252d_base_v067_signal(filingage, calendardate):
    n = _std(filingage, 252)
    d = _std(calendardate, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(filingage) / std(calendardate)
def rr_f079_reporting_recency_volratio_calendardate_504d_base_v068_signal(filingage, calendardate):
    n = _std(filingage, 504)
    d = _std(calendardate, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std(filingage) / std(datekey)
def rr_f079_reporting_recency_volratio_datekey_252d_base_v069_signal(filingage, datekey):
    n = _std(filingage, 252)
    d = _std(datekey, 252).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std(filingage) / std(datekey)
def rr_f079_reporting_recency_volratio_datekey_504d_base_v070_signal(filingage, datekey):
    n = _std(filingage, 504)
    d = _std(datekey, 504).replace(0, np.nan)
    result = n / d
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed filingage times closeadj
def rr_f079_reporting_recency_raw_5d_base_v071_signal(filingage, closeadj):
    result = _mean(filingage, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 1008d smoothed filingage times closeadj
def rr_f079_reporting_recency_raw_1008d_base_v072_signal(filingage, closeadj):
    result = _mean(filingage, 1008) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of filingage/calendardate
def rr_f079_reporting_recency_log_per_calendardate_252d_base_v073_signal(filingage, calendardate):
    s = _reporting_recency_scaled(filingage, calendardate)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log of filingage/calendardate
def rr_f079_reporting_recency_log_per_calendardate_504d_base_v074_signal(filingage, calendardate):
    s = _reporting_recency_scaled(filingage, calendardate)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of filingage/datekey
def rr_f079_reporting_recency_log_per_datekey_252d_base_v075_signal(filingage, datekey):
    s = _reporting_recency_scaled(filingage, datekey)
    result = _mean(np.log(s.abs().replace(0, np.nan)), 252)
    return result.replace([np.inf, -np.inf], np.nan)
