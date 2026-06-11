import inspect
import numpy as np
import pandas as pd

# 2nd-derivative file (1st MATH derivative = SLOPE of a base feature).
# Each function fully expands its base quantity inline, then takes the 1st
# difference / rate-of-change over a window appropriate to the base horizon.

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _logroc(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _own_pct(totalvalue, marketcap):
    return totalvalue / marketcap.replace(0, np.nan)


def _vph(totalvalue, shrholders):
    return totalvalue / shrholders.replace(0, np.nan)


def _uph(shrunits, shrholders):
    return shrunits / shrholders.replace(0, np.nan)


def _implpx(totalvalue, shrunits):
    return totalvalue / shrunits.replace(0, np.nan)


# slope (1st deriv) of log holder count via d_a
def f44ia_f44_institutional_accumulation_holdlog_d_a_slope_v001_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log holder count via d_b
def f44ia_f44_institutional_accumulation_holdlog_d_b_slope_v002_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    b = base - base.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log holder count via d_c
def f44ia_f44_institutional_accumulation_holdlog_d_c_slope_v003_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    b = base - base.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log holder count via zdiff
def f44ia_f44_institutional_accumulation_holdlog_zdiff_slope_v004_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d = base - base.shift(21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log holder count via zdiffb
def f44ia_f44_institutional_accumulation_holdlog_zdiffb_slope_v005_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d = base - base.shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log holder count via rankdiff
def f44ia_f44_institutional_accumulation_holdlog_rankdiff_slope_v006_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d = base - base.shift(21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log holder count via norm
def f44ia_f44_institutional_accumulation_holdlog_norm_slope_v007_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d = base - base.shift(63)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = d / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log holder count via accel
def f44ia_f44_institutional_accumulation_holdlog_accel_slope_v008_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log holder count via tanh
def f44ia_f44_institutional_accumulation_holdlog_tanh_slope_v009_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    b = np.tanh(50.0 * (base - base.shift(5)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log holder count via emadisp
def f44ia_f44_institutional_accumulation_holdlog_emadisp_slope_v010_signal(shrholders):
    base = np.log(shrholders.replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst value via d_a
def f44ia_f44_institutional_accumulation_vallog_d_a_slope_v011_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst value via d_b
def f44ia_f44_institutional_accumulation_vallog_d_b_slope_v012_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    b = base - base.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst value via d_c
def f44ia_f44_institutional_accumulation_vallog_d_c_slope_v013_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    b = base - base.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst value via zdiff
def f44ia_f44_institutional_accumulation_vallog_zdiff_slope_v014_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d = base - base.shift(21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst value via zdiffb
def f44ia_f44_institutional_accumulation_vallog_zdiffb_slope_v015_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d = base - base.shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst value via rankdiff
def f44ia_f44_institutional_accumulation_vallog_rankdiff_slope_v016_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d = base - base.shift(21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst value via norm
def f44ia_f44_institutional_accumulation_vallog_norm_slope_v017_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d = base - base.shift(63)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = d / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst value via accel
def f44ia_f44_institutional_accumulation_vallog_accel_slope_v018_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst value via tanh
def f44ia_f44_institutional_accumulation_vallog_tanh_slope_v019_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    b = np.tanh(50.0 * (base - base.shift(5)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst value via emadisp
def f44ia_f44_institutional_accumulation_vallog_emadisp_slope_v020_signal(totalvalue):
    base = np.log(totalvalue.replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst units via d_a
def f44ia_f44_institutional_accumulation_unitlog_d_a_slope_v021_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst units via d_b
def f44ia_f44_institutional_accumulation_unitlog_d_b_slope_v022_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    b = base - base.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst units via d_c
def f44ia_f44_institutional_accumulation_unitlog_d_c_slope_v023_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    b = base - base.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst units via zdiff
def f44ia_f44_institutional_accumulation_unitlog_zdiff_slope_v024_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d = base - base.shift(21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst units via zdiffb
def f44ia_f44_institutional_accumulation_unitlog_zdiffb_slope_v025_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d = base - base.shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst units via rankdiff
def f44ia_f44_institutional_accumulation_unitlog_rankdiff_slope_v026_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d = base - base.shift(21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst units via norm
def f44ia_f44_institutional_accumulation_unitlog_norm_slope_v027_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d = base - base.shift(63)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = d / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst units via accel
def f44ia_f44_institutional_accumulation_unitlog_accel_slope_v028_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst units via tanh
def f44ia_f44_institutional_accumulation_unitlog_tanh_slope_v029_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    b = np.tanh(50.0 * (base - base.shift(5)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log inst units via emadisp
def f44ia_f44_institutional_accumulation_unitlog_emadisp_slope_v030_signal(shrunits):
    base = np.log(shrunits.replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst ownership pct via d_a
def f44ia_f44_institutional_accumulation_ownpct_d_a_slope_v031_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst ownership pct via d_b
def f44ia_f44_institutional_accumulation_ownpct_d_b_slope_v032_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    b = base - base.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst ownership pct via d_c
def f44ia_f44_institutional_accumulation_ownpct_d_c_slope_v033_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    b = base - base.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst ownership pct via zdiff
def f44ia_f44_institutional_accumulation_ownpct_zdiff_slope_v034_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d = base - base.shift(21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst ownership pct via zdiffb
def f44ia_f44_institutional_accumulation_ownpct_zdiffb_slope_v035_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d = base - base.shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst ownership pct via rankdiff
def f44ia_f44_institutional_accumulation_ownpct_rankdiff_slope_v036_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d = base - base.shift(21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst ownership pct via norm
def f44ia_f44_institutional_accumulation_ownpct_norm_slope_v037_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d = base - base.shift(63)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = d / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst ownership pct via accel
def f44ia_f44_institutional_accumulation_ownpct_accel_slope_v038_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst ownership pct via tanh
def f44ia_f44_institutional_accumulation_ownpct_tanh_slope_v039_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    b = np.tanh(50.0 * (base - base.shift(5)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst ownership pct via emadisp
def f44ia_f44_institutional_accumulation_ownpct_emadisp_slope_v040_signal(totalvalue, marketcap):
    base = _own_pct(totalvalue, marketcap)
    d = base - base.shift(21)
    b = d - d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log value per holder via d_a
def f44ia_f44_institutional_accumulation_vphlog_d_a_slope_v041_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log value per holder via d_b
def f44ia_f44_institutional_accumulation_vphlog_d_b_slope_v042_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    b = base - base.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log value per holder via d_c
def f44ia_f44_institutional_accumulation_vphlog_d_c_slope_v043_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    b = base - base.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log value per holder via zdiff
def f44ia_f44_institutional_accumulation_vphlog_zdiff_slope_v044_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log value per holder via zdiffb
def f44ia_f44_institutional_accumulation_vphlog_zdiffb_slope_v045_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d = base - base.shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log value per holder via rankdiff
def f44ia_f44_institutional_accumulation_vphlog_rankdiff_slope_v046_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log value per holder via norm
def f44ia_f44_institutional_accumulation_vphlog_norm_slope_v047_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d = base - base.shift(63)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = d / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log value per holder via accel
def f44ia_f44_institutional_accumulation_vphlog_accel_slope_v048_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log value per holder via tanh
def f44ia_f44_institutional_accumulation_vphlog_tanh_slope_v049_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    b = np.tanh(50.0 * (base - base.shift(5)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log value per holder via emadisp
def f44ia_f44_institutional_accumulation_vphlog_emadisp_slope_v050_signal(totalvalue, shrholders):
    base = np.log(_vph(totalvalue, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log units per holder via d_a
def f44ia_f44_institutional_accumulation_uphlog_d_a_slope_v051_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log units per holder via d_b
def f44ia_f44_institutional_accumulation_uphlog_d_b_slope_v052_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    b = base - base.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log units per holder via d_c
def f44ia_f44_institutional_accumulation_uphlog_d_c_slope_v053_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    b = base - base.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log units per holder via zdiff
def f44ia_f44_institutional_accumulation_uphlog_zdiff_slope_v054_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log units per holder via zdiffb
def f44ia_f44_institutional_accumulation_uphlog_zdiffb_slope_v055_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d = base - base.shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log units per holder via rankdiff
def f44ia_f44_institutional_accumulation_uphlog_rankdiff_slope_v056_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log units per holder via norm
def f44ia_f44_institutional_accumulation_uphlog_norm_slope_v057_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d = base - base.shift(63)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = d / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log units per holder via accel
def f44ia_f44_institutional_accumulation_uphlog_accel_slope_v058_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log units per holder via tanh
def f44ia_f44_institutional_accumulation_uphlog_tanh_slope_v059_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    b = np.tanh(50.0 * (base - base.shift(5)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log units per holder via emadisp
def f44ia_f44_institutional_accumulation_uphlog_emadisp_slope_v060_signal(shrunits, shrholders):
    base = np.log(_uph(shrunits, shrholders).replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log implied price (value/units) via d_a
def f44ia_f44_institutional_accumulation_implpxlog_d_a_slope_v061_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log implied price (value/units) via d_b
def f44ia_f44_institutional_accumulation_implpxlog_d_b_slope_v062_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    b = base - base.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log implied price (value/units) via d_c
def f44ia_f44_institutional_accumulation_implpxlog_d_c_slope_v063_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    b = base - base.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log implied price (value/units) via zdiff
def f44ia_f44_institutional_accumulation_implpxlog_zdiff_slope_v064_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d = base - base.shift(21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log implied price (value/units) via zdiffb
def f44ia_f44_institutional_accumulation_implpxlog_zdiffb_slope_v065_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d = base - base.shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log implied price (value/units) via rankdiff
def f44ia_f44_institutional_accumulation_implpxlog_rankdiff_slope_v066_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d = base - base.shift(21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log implied price (value/units) via norm
def f44ia_f44_institutional_accumulation_implpxlog_norm_slope_v067_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d = base - base.shift(63)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = d / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log implied price (value/units) via accel
def f44ia_f44_institutional_accumulation_implpxlog_accel_slope_v068_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log implied price (value/units) via tanh
def f44ia_f44_institutional_accumulation_implpxlog_tanh_slope_v069_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    b = np.tanh(50.0 * (base - base.shift(5)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log implied price (value/units) via emadisp
def f44ia_f44_institutional_accumulation_implpxlog_emadisp_slope_v070_signal(totalvalue, shrunits):
    base = np.log(_implpx(totalvalue, shrunits).replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing shrvalue via d_a
def f44ia_f44_institutional_accumulation_shrvallog_d_a_slope_v071_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing shrvalue via d_b
def f44ia_f44_institutional_accumulation_shrvallog_d_b_slope_v072_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    b = base - base.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing shrvalue via d_c
def f44ia_f44_institutional_accumulation_shrvallog_d_c_slope_v073_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    b = base - base.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing shrvalue via zdiff
def f44ia_f44_institutional_accumulation_shrvallog_zdiff_slope_v074_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d = base - base.shift(21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing shrvalue via zdiffb
def f44ia_f44_institutional_accumulation_shrvallog_zdiffb_slope_v075_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d = base - base.shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing shrvalue via rankdiff
def f44ia_f44_institutional_accumulation_shrvallog_rankdiff_slope_v076_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d = base - base.shift(21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing shrvalue via norm
def f44ia_f44_institutional_accumulation_shrvallog_norm_slope_v077_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d = base - base.shift(63)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = d / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing shrvalue via accel
def f44ia_f44_institutional_accumulation_shrvallog_accel_slope_v078_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing shrvalue via tanh
def f44ia_f44_institutional_accumulation_shrvallog_tanh_slope_v079_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    b = np.tanh(50.0 * (base - base.shift(5)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing shrvalue via emadisp
def f44ia_f44_institutional_accumulation_shrvallog_emadisp_slope_v080_signal(shrvalue):
    base = np.log(shrvalue.replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of shrvalue concentration share via d_a
def f44ia_f44_institutional_accumulation_shrvalshare_d_a_slope_v081_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of shrvalue concentration share via d_b
def f44ia_f44_institutional_accumulation_shrvalshare_d_b_slope_v082_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    b = base - base.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of shrvalue concentration share via d_c
def f44ia_f44_institutional_accumulation_shrvalshare_d_c_slope_v083_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    b = base - base.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of shrvalue concentration share via zdiff
def f44ia_f44_institutional_accumulation_shrvalshare_zdiff_slope_v084_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d = base - base.shift(21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of shrvalue concentration share via zdiffb
def f44ia_f44_institutional_accumulation_shrvalshare_zdiffb_slope_v085_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d = base - base.shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of shrvalue concentration share via rankdiff
def f44ia_f44_institutional_accumulation_shrvalshare_rankdiff_slope_v086_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d = base - base.shift(21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of shrvalue concentration share via norm
def f44ia_f44_institutional_accumulation_shrvalshare_norm_slope_v087_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d = base - base.shift(63)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = d / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of shrvalue concentration share via accel
def f44ia_f44_institutional_accumulation_shrvalshare_accel_slope_v088_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of shrvalue concentration share via tanh
def f44ia_f44_institutional_accumulation_shrvalshare_tanh_slope_v089_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    b = np.tanh(50.0 * (base - base.shift(5)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of shrvalue concentration share via emadisp
def f44ia_f44_institutional_accumulation_shrvalshare_emadisp_slope_v090_signal(shrvalue, totalvalue):
    base = shrvalue / totalvalue.replace(0, np.nan)
    d = base - base.shift(21)
    b = d - d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing value vs marketcap via d_a
def f44ia_f44_institutional_accumulation_shrvalmkt_d_a_slope_v091_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing value vs marketcap via d_b
def f44ia_f44_institutional_accumulation_shrvalmkt_d_b_slope_v092_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    b = base - base.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing value vs marketcap via d_c
def f44ia_f44_institutional_accumulation_shrvalmkt_d_c_slope_v093_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    b = base - base.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing value vs marketcap via zdiff
def f44ia_f44_institutional_accumulation_shrvalmkt_zdiff_slope_v094_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d = base - base.shift(21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing value vs marketcap via zdiffb
def f44ia_f44_institutional_accumulation_shrvalmkt_zdiffb_slope_v095_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d = base - base.shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing value vs marketcap via rankdiff
def f44ia_f44_institutional_accumulation_shrvalmkt_rankdiff_slope_v096_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d = base - base.shift(21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing value vs marketcap via norm
def f44ia_f44_institutional_accumulation_shrvalmkt_norm_slope_v097_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d = base - base.shift(63)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = d / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing value vs marketcap via accel
def f44ia_f44_institutional_accumulation_shrvalmkt_accel_slope_v098_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing value vs marketcap via tanh
def f44ia_f44_institutional_accumulation_shrvalmkt_tanh_slope_v099_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    b = np.tanh(50.0 * (base - base.shift(5)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of log per-filing value vs marketcap via emadisp
def f44ia_f44_institutional_accumulation_shrvalmkt_emadisp_slope_v100_signal(shrvalue, marketcap):
    base = np.log((shrvalue / marketcap.replace(0, np.nan)).replace(0, np.nan))
    d = base - base.shift(21)
    b = d - d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct z-score via d_a
def f44ia_f44_institutional_accumulation_ownpctz_d_a_slope_v101_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct z-score via d_b
def f44ia_f44_institutional_accumulation_ownpctz_d_b_slope_v102_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    b = base - base.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct z-score via d_c
def f44ia_f44_institutional_accumulation_ownpctz_d_c_slope_v103_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    b = base - base.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct z-score via zdiff
def f44ia_f44_institutional_accumulation_ownpctz_zdiff_slope_v104_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d = base - base.shift(21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct z-score via zdiffb
def f44ia_f44_institutional_accumulation_ownpctz_zdiffb_slope_v105_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d = base - base.shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct z-score via rankdiff
def f44ia_f44_institutional_accumulation_ownpctz_rankdiff_slope_v106_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d = base - base.shift(21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct z-score via norm
def f44ia_f44_institutional_accumulation_ownpctz_norm_slope_v107_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d = base - base.shift(63)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = d / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct z-score via accel
def f44ia_f44_institutional_accumulation_ownpctz_accel_slope_v108_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct z-score via tanh
def f44ia_f44_institutional_accumulation_ownpctz_tanh_slope_v109_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    b = np.tanh(50.0 * (base - base.shift(5)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct z-score via emadisp
def f44ia_f44_institutional_accumulation_ownpctz_emadisp_slope_v110_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _z(op, 252)
    d = base - base.shift(21)
    b = d - d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst-value 504d range position via d_a
def f44ia_f44_institutional_accumulation_valrngpos_d_a_slope_v111_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst-value 504d range position via d_b
def f44ia_f44_institutional_accumulation_valrngpos_d_b_slope_v112_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    b = base - base.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst-value 504d range position via d_c
def f44ia_f44_institutional_accumulation_valrngpos_d_c_slope_v113_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    b = base - base.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst-value 504d range position via zdiff
def f44ia_f44_institutional_accumulation_valrngpos_zdiff_slope_v114_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst-value 504d range position via zdiffb
def f44ia_f44_institutional_accumulation_valrngpos_zdiffb_slope_v115_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst-value 504d range position via rankdiff
def f44ia_f44_institutional_accumulation_valrngpos_rankdiff_slope_v116_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst-value 504d range position via norm
def f44ia_f44_institutional_accumulation_valrngpos_norm_slope_v117_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(63)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = d / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst-value 504d range position via accel
def f44ia_f44_institutional_accumulation_valrngpos_accel_slope_v118_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst-value 504d range position via tanh
def f44ia_f44_institutional_accumulation_valrngpos_tanh_slope_v119_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    b = np.tanh(50.0 * (base - base.shift(5)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of inst-value 504d range position via emadisp
def f44ia_f44_institutional_accumulation_valrngpos_emadisp_slope_v120_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    base = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    b = d - d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of holder 252d range position via d_a
def f44ia_f44_institutional_accumulation_holdrngpos_d_a_slope_v121_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of holder 252d range position via d_b
def f44ia_f44_institutional_accumulation_holdrngpos_d_b_slope_v122_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    b = base - base.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of holder 252d range position via d_c
def f44ia_f44_institutional_accumulation_holdrngpos_d_c_slope_v123_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    b = base - base.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of holder 252d range position via zdiff
def f44ia_f44_institutional_accumulation_holdrngpos_zdiff_slope_v124_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of holder 252d range position via zdiffb
def f44ia_f44_institutional_accumulation_holdrngpos_zdiffb_slope_v125_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of holder 252d range position via rankdiff
def f44ia_f44_institutional_accumulation_holdrngpos_rankdiff_slope_v126_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of holder 252d range position via norm
def f44ia_f44_institutional_accumulation_holdrngpos_norm_slope_v127_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(63)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = d / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of holder 252d range position via accel
def f44ia_f44_institutional_accumulation_holdrngpos_accel_slope_v128_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of holder 252d range position via tanh
def f44ia_f44_institutional_accumulation_holdrngpos_tanh_slope_v129_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    b = np.tanh(50.0 * (base - base.shift(5)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of holder 252d range position via emadisp
def f44ia_f44_institutional_accumulation_holdrngpos_emadisp_slope_v130_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    base = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    b = d - d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of units 504d range position via d_a
def f44ia_f44_institutional_accumulation_unitrngpos_d_a_slope_v131_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of units 504d range position via d_b
def f44ia_f44_institutional_accumulation_unitrngpos_d_b_slope_v132_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    b = base - base.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of units 504d range position via d_c
def f44ia_f44_institutional_accumulation_unitrngpos_d_c_slope_v133_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    b = base - base.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of units 504d range position via zdiff
def f44ia_f44_institutional_accumulation_unitrngpos_zdiff_slope_v134_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of units 504d range position via zdiffb
def f44ia_f44_institutional_accumulation_unitrngpos_zdiffb_slope_v135_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of units 504d range position via rankdiff
def f44ia_f44_institutional_accumulation_unitrngpos_rankdiff_slope_v136_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of units 504d range position via norm
def f44ia_f44_institutional_accumulation_unitrngpos_norm_slope_v137_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(63)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = d / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of units 504d range position via accel
def f44ia_f44_institutional_accumulation_unitrngpos_accel_slope_v138_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of units 504d range position via tanh
def f44ia_f44_institutional_accumulation_unitrngpos_tanh_slope_v139_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    b = np.tanh(50.0 * (base - base.shift(5)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of units 504d range position via emadisp
def f44ia_f44_institutional_accumulation_unitrngpos_emadisp_slope_v140_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    base = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    d = base - base.shift(21)
    b = d - d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct 504d rank via d_a
def f44ia_f44_institutional_accumulation_ownpctrank_d_a_slope_v141_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    b = base - base.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct 504d rank via d_b
def f44ia_f44_institutional_accumulation_ownpctrank_d_b_slope_v142_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    b = base - base.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct 504d rank via d_c
def f44ia_f44_institutional_accumulation_ownpctrank_d_c_slope_v143_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    b = base - base.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct 504d rank via zdiff
def f44ia_f44_institutional_accumulation_ownpctrank_zdiff_slope_v144_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d = base - base.shift(21)
    b = _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct 504d rank via zdiffb
def f44ia_f44_institutional_accumulation_ownpctrank_zdiffb_slope_v145_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d = base - base.shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct 504d rank via rankdiff
def f44ia_f44_institutional_accumulation_ownpctrank_rankdiff_slope_v146_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d = base - base.shift(21)
    b = d.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct 504d rank via norm
def f44ia_f44_institutional_accumulation_ownpctrank_norm_slope_v147_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d = base - base.shift(63)
    sd = base.diff().rolling(126, min_periods=63).std()
    b = d / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct 504d rank via accel
def f44ia_f44_institutional_accumulation_ownpctrank_accel_slope_v148_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d = base - base.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct 504d rank via tanh
def f44ia_f44_institutional_accumulation_ownpctrank_tanh_slope_v149_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    b = np.tanh(50.0 * (base - base.shift(5)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of ownership-pct 504d rank via emadisp
def f44ia_f44_institutional_accumulation_ownpctrank_emadisp_slope_v150_signal(totalvalue, marketcap):
    op = _own_pct(totalvalue, marketcap)
    base = _rank(op, 504)
    d = base - base.shift(21)
    b = d - d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44ia_f44_institutional_accumulation_holdlog_d_a_slope_v001_signal,
    f44ia_f44_institutional_accumulation_holdlog_d_b_slope_v002_signal,
    f44ia_f44_institutional_accumulation_holdlog_d_c_slope_v003_signal,
    f44ia_f44_institutional_accumulation_holdlog_zdiff_slope_v004_signal,
    f44ia_f44_institutional_accumulation_holdlog_zdiffb_slope_v005_signal,
    f44ia_f44_institutional_accumulation_holdlog_rankdiff_slope_v006_signal,
    f44ia_f44_institutional_accumulation_holdlog_norm_slope_v007_signal,
    f44ia_f44_institutional_accumulation_holdlog_accel_slope_v008_signal,
    f44ia_f44_institutional_accumulation_holdlog_tanh_slope_v009_signal,
    f44ia_f44_institutional_accumulation_holdlog_emadisp_slope_v010_signal,
    f44ia_f44_institutional_accumulation_vallog_d_a_slope_v011_signal,
    f44ia_f44_institutional_accumulation_vallog_d_b_slope_v012_signal,
    f44ia_f44_institutional_accumulation_vallog_d_c_slope_v013_signal,
    f44ia_f44_institutional_accumulation_vallog_zdiff_slope_v014_signal,
    f44ia_f44_institutional_accumulation_vallog_zdiffb_slope_v015_signal,
    f44ia_f44_institutional_accumulation_vallog_rankdiff_slope_v016_signal,
    f44ia_f44_institutional_accumulation_vallog_norm_slope_v017_signal,
    f44ia_f44_institutional_accumulation_vallog_accel_slope_v018_signal,
    f44ia_f44_institutional_accumulation_vallog_tanh_slope_v019_signal,
    f44ia_f44_institutional_accumulation_vallog_emadisp_slope_v020_signal,
    f44ia_f44_institutional_accumulation_unitlog_d_a_slope_v021_signal,
    f44ia_f44_institutional_accumulation_unitlog_d_b_slope_v022_signal,
    f44ia_f44_institutional_accumulation_unitlog_d_c_slope_v023_signal,
    f44ia_f44_institutional_accumulation_unitlog_zdiff_slope_v024_signal,
    f44ia_f44_institutional_accumulation_unitlog_zdiffb_slope_v025_signal,
    f44ia_f44_institutional_accumulation_unitlog_rankdiff_slope_v026_signal,
    f44ia_f44_institutional_accumulation_unitlog_norm_slope_v027_signal,
    f44ia_f44_institutional_accumulation_unitlog_accel_slope_v028_signal,
    f44ia_f44_institutional_accumulation_unitlog_tanh_slope_v029_signal,
    f44ia_f44_institutional_accumulation_unitlog_emadisp_slope_v030_signal,
    f44ia_f44_institutional_accumulation_ownpct_d_a_slope_v031_signal,
    f44ia_f44_institutional_accumulation_ownpct_d_b_slope_v032_signal,
    f44ia_f44_institutional_accumulation_ownpct_d_c_slope_v033_signal,
    f44ia_f44_institutional_accumulation_ownpct_zdiff_slope_v034_signal,
    f44ia_f44_institutional_accumulation_ownpct_zdiffb_slope_v035_signal,
    f44ia_f44_institutional_accumulation_ownpct_rankdiff_slope_v036_signal,
    f44ia_f44_institutional_accumulation_ownpct_norm_slope_v037_signal,
    f44ia_f44_institutional_accumulation_ownpct_accel_slope_v038_signal,
    f44ia_f44_institutional_accumulation_ownpct_tanh_slope_v039_signal,
    f44ia_f44_institutional_accumulation_ownpct_emadisp_slope_v040_signal,
    f44ia_f44_institutional_accumulation_vphlog_d_a_slope_v041_signal,
    f44ia_f44_institutional_accumulation_vphlog_d_b_slope_v042_signal,
    f44ia_f44_institutional_accumulation_vphlog_d_c_slope_v043_signal,
    f44ia_f44_institutional_accumulation_vphlog_zdiff_slope_v044_signal,
    f44ia_f44_institutional_accumulation_vphlog_zdiffb_slope_v045_signal,
    f44ia_f44_institutional_accumulation_vphlog_rankdiff_slope_v046_signal,
    f44ia_f44_institutional_accumulation_vphlog_norm_slope_v047_signal,
    f44ia_f44_institutional_accumulation_vphlog_accel_slope_v048_signal,
    f44ia_f44_institutional_accumulation_vphlog_tanh_slope_v049_signal,
    f44ia_f44_institutional_accumulation_vphlog_emadisp_slope_v050_signal,
    f44ia_f44_institutional_accumulation_uphlog_d_a_slope_v051_signal,
    f44ia_f44_institutional_accumulation_uphlog_d_b_slope_v052_signal,
    f44ia_f44_institutional_accumulation_uphlog_d_c_slope_v053_signal,
    f44ia_f44_institutional_accumulation_uphlog_zdiff_slope_v054_signal,
    f44ia_f44_institutional_accumulation_uphlog_zdiffb_slope_v055_signal,
    f44ia_f44_institutional_accumulation_uphlog_rankdiff_slope_v056_signal,
    f44ia_f44_institutional_accumulation_uphlog_norm_slope_v057_signal,
    f44ia_f44_institutional_accumulation_uphlog_accel_slope_v058_signal,
    f44ia_f44_institutional_accumulation_uphlog_tanh_slope_v059_signal,
    f44ia_f44_institutional_accumulation_uphlog_emadisp_slope_v060_signal,
    f44ia_f44_institutional_accumulation_implpxlog_d_a_slope_v061_signal,
    f44ia_f44_institutional_accumulation_implpxlog_d_b_slope_v062_signal,
    f44ia_f44_institutional_accumulation_implpxlog_d_c_slope_v063_signal,
    f44ia_f44_institutional_accumulation_implpxlog_zdiff_slope_v064_signal,
    f44ia_f44_institutional_accumulation_implpxlog_zdiffb_slope_v065_signal,
    f44ia_f44_institutional_accumulation_implpxlog_rankdiff_slope_v066_signal,
    f44ia_f44_institutional_accumulation_implpxlog_norm_slope_v067_signal,
    f44ia_f44_institutional_accumulation_implpxlog_accel_slope_v068_signal,
    f44ia_f44_institutional_accumulation_implpxlog_tanh_slope_v069_signal,
    f44ia_f44_institutional_accumulation_implpxlog_emadisp_slope_v070_signal,
    f44ia_f44_institutional_accumulation_shrvallog_d_a_slope_v071_signal,
    f44ia_f44_institutional_accumulation_shrvallog_d_b_slope_v072_signal,
    f44ia_f44_institutional_accumulation_shrvallog_d_c_slope_v073_signal,
    f44ia_f44_institutional_accumulation_shrvallog_zdiff_slope_v074_signal,
    f44ia_f44_institutional_accumulation_shrvallog_zdiffb_slope_v075_signal,
    f44ia_f44_institutional_accumulation_shrvallog_rankdiff_slope_v076_signal,
    f44ia_f44_institutional_accumulation_shrvallog_norm_slope_v077_signal,
    f44ia_f44_institutional_accumulation_shrvallog_accel_slope_v078_signal,
    f44ia_f44_institutional_accumulation_shrvallog_tanh_slope_v079_signal,
    f44ia_f44_institutional_accumulation_shrvallog_emadisp_slope_v080_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_d_a_slope_v081_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_d_b_slope_v082_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_d_c_slope_v083_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_zdiff_slope_v084_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_zdiffb_slope_v085_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_rankdiff_slope_v086_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_norm_slope_v087_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_accel_slope_v088_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_tanh_slope_v089_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_emadisp_slope_v090_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_d_a_slope_v091_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_d_b_slope_v092_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_d_c_slope_v093_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_zdiff_slope_v094_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_zdiffb_slope_v095_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_rankdiff_slope_v096_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_norm_slope_v097_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_accel_slope_v098_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_tanh_slope_v099_signal,
    f44ia_f44_institutional_accumulation_shrvalmkt_emadisp_slope_v100_signal,
    f44ia_f44_institutional_accumulation_ownpctz_d_a_slope_v101_signal,
    f44ia_f44_institutional_accumulation_ownpctz_d_b_slope_v102_signal,
    f44ia_f44_institutional_accumulation_ownpctz_d_c_slope_v103_signal,
    f44ia_f44_institutional_accumulation_ownpctz_zdiff_slope_v104_signal,
    f44ia_f44_institutional_accumulation_ownpctz_zdiffb_slope_v105_signal,
    f44ia_f44_institutional_accumulation_ownpctz_rankdiff_slope_v106_signal,
    f44ia_f44_institutional_accumulation_ownpctz_norm_slope_v107_signal,
    f44ia_f44_institutional_accumulation_ownpctz_accel_slope_v108_signal,
    f44ia_f44_institutional_accumulation_ownpctz_tanh_slope_v109_signal,
    f44ia_f44_institutional_accumulation_ownpctz_emadisp_slope_v110_signal,
    f44ia_f44_institutional_accumulation_valrngpos_d_a_slope_v111_signal,
    f44ia_f44_institutional_accumulation_valrngpos_d_b_slope_v112_signal,
    f44ia_f44_institutional_accumulation_valrngpos_d_c_slope_v113_signal,
    f44ia_f44_institutional_accumulation_valrngpos_zdiff_slope_v114_signal,
    f44ia_f44_institutional_accumulation_valrngpos_zdiffb_slope_v115_signal,
    f44ia_f44_institutional_accumulation_valrngpos_rankdiff_slope_v116_signal,
    f44ia_f44_institutional_accumulation_valrngpos_norm_slope_v117_signal,
    f44ia_f44_institutional_accumulation_valrngpos_accel_slope_v118_signal,
    f44ia_f44_institutional_accumulation_valrngpos_tanh_slope_v119_signal,
    f44ia_f44_institutional_accumulation_valrngpos_emadisp_slope_v120_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_d_a_slope_v121_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_d_b_slope_v122_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_d_c_slope_v123_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_zdiff_slope_v124_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_zdiffb_slope_v125_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_rankdiff_slope_v126_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_norm_slope_v127_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_accel_slope_v128_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_tanh_slope_v129_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_emadisp_slope_v130_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_d_a_slope_v131_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_d_b_slope_v132_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_d_c_slope_v133_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_zdiff_slope_v134_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_zdiffb_slope_v135_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_rankdiff_slope_v136_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_norm_slope_v137_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_accel_slope_v138_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_tanh_slope_v139_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_emadisp_slope_v140_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_d_a_slope_v141_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_d_b_slope_v142_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_d_c_slope_v143_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_zdiff_slope_v144_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_zdiffb_slope_v145_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_rankdiff_slope_v146_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_norm_slope_v147_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_accel_slope_v148_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_tanh_slope_v149_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_emadisp_slope_v150_signal
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_INSTITUTIONAL_ACCUMULATION_REGISTRY_DERIV = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    shrholders = _fund(301, base=120.0, drift=0.03, vol=0.06).rename("shrholders")
    shrunits = _fund(302, base=5.0e6, drift=0.04, vol=0.09).rename("shrunits")
    totalvalue = _fund(303, base=8.0e7, drift=0.05, vol=0.10).rename("totalvalue")
    shrvalue = _fund(304, base=9.0e6, drift=0.04, vol=0.11).rename("shrvalue")
    marketcap = _fund(305, base=3.0e8, drift=0.02, vol=0.08).rename("marketcap")

    cols = {
        "shrholders": shrholders,
        "shrunits": shrunits,
        "totalvalue": totalvalue,
        "shrvalue": shrvalue,
        "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f44_institutional_accumulation_2nd_derivatives_001_150_claude: %d features pass" % n_features)
