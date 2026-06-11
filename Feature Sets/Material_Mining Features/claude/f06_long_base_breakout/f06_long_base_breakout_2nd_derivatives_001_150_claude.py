import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _base_range(close, w):
    hi = _rmax(close, w)
    lo = _rmin(close, w)
    mid = (hi + lo) / 2.0
    return (hi - lo) / mid.replace(0, np.nan)


def _tightness(close, w):
    return _std(close, w) / _mean(close, w).replace(0, np.nan)


def _ceiling_dist(close, w):
    ceil = close.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    return close / ceil.replace(0, np.nan) - 1.0


def _floor_dist(close, w):
    floor = close.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    return close / floor.replace(0, np.nan) - 1.0


def _breakout(close, w):
    ceil = close.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    return (close / ceil.replace(0, np.nan) - 1.0).clip(lower=0.0)


def _basepos(close, w):
    hi = _rmax(close, w)
    lo = _rmin(close, w)
    return (close - lo) / (hi - lo).replace(0, np.nan)


def _bandwidth(close, w):
    m = _mean(close, w)
    sd = _std(close, w)
    return (4.0 * sd) / m.replace(0, np.nan)


def f06lb_f06_long_base_breakout_baserange_252d_slope_v001_signal(closeadj):
    bx = _base_range(closeadj, 252)
    result = (bx - bx.shift(10)) / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_baserange_252d_slope_v002_signal(closeadj):
    bx = _base_range(closeadj, 252)
    sm = bx.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_baserange_252d_slope_v003_signal(closeadj):
    bx = _base_range(closeadj, 252)
    d = (bx - bx.shift(63)) / float(63)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_tight_252d_slope_v004_signal(closeadj):
    bx = _tightness(closeadj, 252)
    result = (bx - bx.shift(11)) / float(11)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_tight_252d_slope_v005_signal(closeadj):
    bx = _tightness(closeadj, 252)
    sm = bx.ewm(span=23, min_periods=max(2, 23 // 2)).mean()
    result = (sm - sm.shift(23)) / float(23)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_tight_252d_slope_v006_signal(closeadj):
    bx = _tightness(closeadj, 252)
    d = (bx - bx.shift(66)) / float(66)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_tightlong_504d_slope_v007_signal(closeadj):
    bx = _tightness(closeadj, 504)
    result = (bx - bx.shift(23)) / float(23)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_tightlong_504d_slope_v008_signal(closeadj):
    bx = _tightness(closeadj, 504)
    sm = bx.ewm(span=67, min_periods=max(2, 67 // 2)).mean()
    result = (sm - sm.shift(67)) / float(67)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_tightlong_504d_slope_v009_signal(closeadj):
    bx = _tightness(closeadj, 504)
    d = (bx - bx.shift(132)) / float(132)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_ceildist_252d_slope_v010_signal(closeadj):
    bx = _ceiling_dist(closeadj, 252)
    result = (bx - bx.shift(13)) / float(13)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_ceildist_252d_slope_v011_signal(closeadj):
    bx = _ceiling_dist(closeadj, 252)
    sm = bx.ewm(span=27, min_periods=max(2, 27 // 2)).mean()
    result = (sm - sm.shift(27)) / float(27)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_ceildist_252d_slope_v012_signal(closeadj):
    bx = _ceiling_dist(closeadj, 252)
    d = (bx - bx.shift(72)) / float(72)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_failrate_504d_slope_v013_signal(high, closeadj):
    ceil = closeadj.shift(1).rolling(504, min_periods=252).max()
    poke = (high > ceil).astype(float)
    held = ((high > ceil) & (closeadj > ceil)).astype(float)
    pk = poke.rolling(252, min_periods=126).sum()
    hd = held.rolling(252, min_periods=126).sum()
    bx = (pk - hd) / pk.replace(0, np.nan)
    result = (bx - bx.shift(25)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_failrate_504d_slope_v014_signal(high, closeadj):
    ceil = closeadj.shift(1).rolling(504, min_periods=252).max()
    poke = (high > ceil).astype(float)
    held = ((high > ceil) & (closeadj > ceil)).astype(float)
    pk = poke.rolling(252, min_periods=126).sum()
    hd = held.rolling(252, min_periods=126).sum()
    bx = (pk - hd) / pk.replace(0, np.nan)
    sm = bx.ewm(span=71, min_periods=max(2, 71 // 2)).mean()
    result = (sm - sm.shift(71)) / float(71)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_failrate_504d_slope_v015_signal(high, closeadj):
    ceil = closeadj.shift(1).rolling(504, min_periods=252).max()
    poke = (high > ceil).astype(float)
    held = ((high > ceil) & (closeadj > ceil)).astype(float)
    pk = poke.rolling(252, min_periods=126).sum()
    hd = held.rolling(252, min_periods=126).sum()
    bx = (pk - hd) / pk.replace(0, np.nan)
    d = (bx - bx.shift(138)) / float(138)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_floordist_252d_slope_v016_signal(closeadj):
    bx = _floor_dist(closeadj, 252)
    result = (bx - bx.shift(10)) / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_floordist_252d_slope_v017_signal(closeadj):
    bx = _floor_dist(closeadj, 252)
    sm = bx.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_floordist_252d_slope_v018_signal(closeadj):
    bx = _floor_dist(closeadj, 252)
    d = (bx - bx.shift(63)) / float(63)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_breakout_252d_slope_v019_signal(closeadj):
    bx = _breakout(closeadj, 252)
    result = (bx - bx.shift(11)) / float(11)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_breakout_252d_slope_v020_signal(closeadj):
    bx = _breakout(closeadj, 252)
    sm = bx.ewm(span=23, min_periods=max(2, 23 // 2)).mean()
    result = (sm - sm.shift(23)) / float(23)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_breakout_252d_slope_v021_signal(closeadj):
    bx = _breakout(closeadj, 252)
    d = (bx - bx.shift(66)) / float(66)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_basepos_252d_slope_v022_signal(closeadj):
    bx = _basepos(closeadj, 252)
    result = (bx - bx.shift(12)) / float(12)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_basepos_252d_slope_v023_signal(closeadj):
    bx = _basepos(closeadj, 252)
    sm = bx.ewm(span=25, min_periods=max(2, 25 // 2)).mean()
    result = (sm - sm.shift(25)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_basepos_252d_slope_v024_signal(closeadj):
    bx = _basepos(closeadj, 252)
    d = (bx - bx.shift(69)) / float(69)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_baseposdisp_504d_slope_v025_signal(closeadj):
    pos = _basepos(closeadj, 504)
    bx = pos - pos.ewm(span=63, min_periods=21).mean()
    result = (bx - bx.shift(24)) / float(24)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_baseposdisp_504d_slope_v026_signal(closeadj):
    pos = _basepos(closeadj, 504)
    bx = pos - pos.ewm(span=63, min_periods=21).mean()
    sm = bx.ewm(span=69, min_periods=max(2, 69 // 2)).mean()
    result = (sm - sm.shift(69)) / float(69)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_baseposdisp_504d_slope_v027_signal(closeadj):
    pos = _basepos(closeadj, 504)
    bx = pos - pos.ewm(span=63, min_periods=21).mean()
    d = (bx - bx.shift(135)) / float(135)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_channelmid_504d_slope_v028_signal(closeadj):
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    mid = (hi + lo) / 2.0
    bx = (mid - mid.shift(126)) / closeadj.replace(0, np.nan)
    result = (bx - bx.shift(25)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_channelmid_504d_slope_v029_signal(closeadj):
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    mid = (hi + lo) / 2.0
    bx = (mid - mid.shift(126)) / closeadj.replace(0, np.nan)
    sm = bx.ewm(span=71, min_periods=max(2, 71 // 2)).mean()
    result = (sm - sm.shift(71)) / float(71)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_channelmid_504d_slope_v030_signal(closeadj):
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    mid = (hi + lo) / 2.0
    bx = (mid - mid.shift(126)) / closeadj.replace(0, np.nan)
    d = (bx - bx.shift(138)) / float(138)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_amplitude_252d_slope_v031_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    bx = (hi - lo) / closeadj.replace(0, np.nan)
    result = (bx - bx.shift(10)) / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_amplitude_252d_slope_v032_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    bx = (hi - lo) / closeadj.replace(0, np.nan)
    sm = bx.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_amplitude_252d_slope_v033_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    bx = (hi - lo) / closeadj.replace(0, np.nan)
    d = (bx - bx.shift(63)) / float(63)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_midpoint_252d_slope_v034_signal(closeadj):
    bx = ((_rmax(closeadj, 252) + _rmin(closeadj, 252)) / 2.0) / closeadj.replace(0, np.nan)
    result = (bx - bx.shift(11)) / float(11)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_midpoint_252d_slope_v035_signal(closeadj):
    bx = ((_rmax(closeadj, 252) + _rmin(closeadj, 252)) / 2.0) / closeadj.replace(0, np.nan)
    sm = bx.ewm(span=23, min_periods=max(2, 23 // 2)).mean()
    result = (sm - sm.shift(23)) / float(23)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_midpoint_252d_slope_v036_signal(closeadj):
    bx = ((_rmax(closeadj, 252) + _rmin(closeadj, 252)) / 2.0) / closeadj.replace(0, np.nan)
    d = (bx - bx.shift(66)) / float(66)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_contract_252d_slope_v037_signal(closeadj):
    bx = _base_range(closeadj, 252) / _base_range(closeadj, 504).replace(0, np.nan)
    result = (bx - bx.shift(12)) / float(12)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_contract_252d_slope_v038_signal(closeadj):
    bx = _base_range(closeadj, 252) / _base_range(closeadj, 504).replace(0, np.nan)
    sm = bx.ewm(span=25, min_periods=max(2, 25 // 2)).mean()
    result = (sm - sm.shift(25)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_contract_252d_slope_v039_signal(closeadj):
    bx = _base_range(closeadj, 252) / _base_range(closeadj, 504).replace(0, np.nan)
    d = (bx - bx.shift(69)) / float(69)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_quietcoil_252d_slope_v040_signal(closeadj):
    br = _base_range(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    bx = br * vol
    result = (bx - bx.shift(13)) / float(13)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_quietcoil_252d_slope_v041_signal(closeadj):
    br = _base_range(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    bx = br * vol
    sm = bx.ewm(span=27, min_periods=max(2, 27 // 2)).mean()
    result = (sm - sm.shift(27)) / float(27)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_quietcoil_252d_slope_v042_signal(closeadj):
    br = _base_range(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    bx = br * vol
    d = (bx - bx.shift(72)) / float(72)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_coil_252d_slope_v043_signal(closeadj):
    bx = _basepos(closeadj, 252) / _base_range(closeadj, 252).replace(0, np.nan)
    result = (bx - bx.shift(14)) / float(14)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_coil_252d_slope_v044_signal(closeadj):
    bx = _basepos(closeadj, 252) / _base_range(closeadj, 252).replace(0, np.nan)
    sm = bx.ewm(span=29, min_periods=max(2, 29 // 2)).mean()
    result = (sm - sm.shift(29)) / float(29)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_coil_252d_slope_v045_signal(closeadj):
    bx = _basepos(closeadj, 252) / _base_range(closeadj, 252).replace(0, np.nan)
    d = (bx - bx.shift(75)) / float(75)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_baselift_1260d_slope_v046_signal(closeadj):
    bx = np.log(closeadj.replace(0, np.nan) / _rmin(closeadj, 1260).replace(0, np.nan))
    result = (bx - bx.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_baselift_1260d_slope_v047_signal(closeadj):
    bx = np.log(closeadj.replace(0, np.nan) / _rmin(closeadj, 1260).replace(0, np.nan))
    sm = bx.ewm(span=63, min_periods=max(2, 63 // 2)).mean()
    result = (sm - sm.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_baselift_1260d_slope_v048_signal(closeadj):
    bx = np.log(closeadj.replace(0, np.nan) / _rmin(closeadj, 1260).replace(0, np.nan))
    d = (bx - bx.shift(126)) / float(126)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_upperhug_504d_slope_v049_signal(closeadj):
    pos = _basepos(closeadj, 504)
    bx = (pos >= 0.75).astype(float).rolling(252, min_periods=126).mean()
    result = (bx - bx.shift(22)) / float(22)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_upperhug_504d_slope_v050_signal(closeadj):
    pos = _basepos(closeadj, 504)
    bx = (pos >= 0.75).astype(float).rolling(252, min_periods=126).mean()
    sm = bx.ewm(span=65, min_periods=max(2, 65 // 2)).mean()
    result = (sm - sm.shift(65)) / float(65)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_upperhug_504d_slope_v051_signal(closeadj):
    pos = _basepos(closeadj, 504)
    bx = (pos >= 0.75).astype(float).rolling(252, min_periods=126).mean()
    d = (bx - bx.shift(129)) / float(129)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_ceilslope_252d_slope_v052_signal(closeadj):
    ceil = _rmax(closeadj, 252)
    bx = np.log(ceil.replace(0, np.nan) / ceil.shift(63).replace(0, np.nan))
    result = (bx - bx.shift(12)) / float(12)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_ceilslope_252d_slope_v053_signal(closeadj):
    ceil = _rmax(closeadj, 252)
    bx = np.log(ceil.replace(0, np.nan) / ceil.shift(63).replace(0, np.nan))
    sm = bx.ewm(span=25, min_periods=max(2, 25 // 2)).mean()
    result = (sm - sm.shift(25)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_ceilslope_252d_slope_v054_signal(closeadj):
    ceil = _rmax(closeadj, 252)
    bx = np.log(ceil.replace(0, np.nan) / ceil.shift(63).replace(0, np.nan))
    d = (bx - bx.shift(69)) / float(69)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_floorslope_252d_slope_v055_signal(closeadj):
    fl = _rmin(closeadj, 252)
    bx = np.log(fl.replace(0, np.nan) / fl.shift(63).replace(0, np.nan))
    result = (bx - bx.shift(13)) / float(13)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_floorslope_252d_slope_v056_signal(closeadj):
    fl = _rmin(closeadj, 252)
    bx = np.log(fl.replace(0, np.nan) / fl.shift(63).replace(0, np.nan))
    sm = bx.ewm(span=27, min_periods=max(2, 27 // 2)).mean()
    result = (sm - sm.shift(27)) / float(27)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_floorslope_252d_slope_v057_signal(closeadj):
    fl = _rmin(closeadj, 252)
    bx = np.log(fl.replace(0, np.nan) / fl.shift(63).replace(0, np.nan))
    d = (bx - bx.shift(72)) / float(72)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_microcoil_252d_slope_v058_signal(closeadj):
    bx = _std(closeadj.pct_change(), 21) / _std(closeadj.pct_change(), 252).replace(0, np.nan)
    result = (bx - bx.shift(14)) / float(14)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_microcoil_252d_slope_v059_signal(closeadj):
    bx = _std(closeadj.pct_change(), 21) / _std(closeadj.pct_change(), 252).replace(0, np.nan)
    sm = bx.ewm(span=29, min_periods=max(2, 29 // 2)).mean()
    result = (sm - sm.shift(29)) / float(29)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_microcoil_252d_slope_v060_signal(closeadj):
    bx = _std(closeadj.pct_change(), 21) / _std(closeadj.pct_change(), 252).replace(0, np.nan)
    d = (bx - bx.shift(75)) / float(75)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_pinch_252d_slope_v061_signal(closeadj):
    bx = (_rmax(closeadj, 21) - _rmin(closeadj, 21)) / (_rmax(closeadj, 252) - _rmin(closeadj, 252)).replace(0, np.nan)
    result = (bx - bx.shift(10)) / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_pinch_252d_slope_v062_signal(closeadj):
    bx = (_rmax(closeadj, 21) - _rmin(closeadj, 21)) / (_rmax(closeadj, 252) - _rmin(closeadj, 252)).replace(0, np.nan)
    sm = bx.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_pinch_252d_slope_v063_signal(closeadj):
    bx = (_rmax(closeadj, 21) - _rmin(closeadj, 21)) / (_rmax(closeadj, 252) - _rmin(closeadj, 252)).replace(0, np.nan)
    d = (bx - bx.shift(63)) / float(63)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_flatness_504d_slope_v064_signal(closeadj):
    drift = np.log(_mean(closeadj, 42).replace(0, np.nan) / _mean(closeadj, 504).replace(0, np.nan))
    bx = 1.0 / (1.0 + 10.0 * drift.abs())
    result = (bx - bx.shift(22)) / float(22)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_flatness_504d_slope_v065_signal(closeadj):
    drift = np.log(_mean(closeadj, 42).replace(0, np.nan) / _mean(closeadj, 504).replace(0, np.nan))
    bx = 1.0 / (1.0 + 10.0 * drift.abs())
    sm = bx.ewm(span=65, min_periods=max(2, 65 // 2)).mean()
    result = (sm - sm.shift(65)) / float(65)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_flatness_504d_slope_v066_signal(closeadj):
    drift = np.log(_mean(closeadj, 42).replace(0, np.nan) / _mean(closeadj, 504).replace(0, np.nan))
    bx = 1.0 / (1.0 + 10.0 * drift.abs())
    d = (bx - bx.shift(129)) / float(129)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_tightasym_252d_slope_v067_signal(closeadj):
    mid = _mean(closeadj, 252)
    up = (closeadj - mid).clip(lower=0)
    dn = (mid - closeadj).clip(lower=0)
    bx = (up.rolling(252, min_periods=126).mean() - dn.rolling(252, min_periods=126).mean()) / mid.replace(0, np.nan)
    result = (bx - bx.shift(12)) / float(12)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_tightasym_252d_slope_v068_signal(closeadj):
    mid = _mean(closeadj, 252)
    up = (closeadj - mid).clip(lower=0)
    dn = (mid - closeadj).clip(lower=0)
    bx = (up.rolling(252, min_periods=126).mean() - dn.rolling(252, min_periods=126).mean()) / mid.replace(0, np.nan)
    sm = bx.ewm(span=25, min_periods=max(2, 25 // 2)).mean()
    result = (sm - sm.shift(25)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_tightasym_252d_slope_v069_signal(closeadj):
    mid = _mean(closeadj, 252)
    up = (closeadj - mid).clip(lower=0)
    dn = (mid - closeadj).clip(lower=0)
    bx = (up.rolling(252, min_periods=126).mean() - dn.rolling(252, min_periods=126).mean()) / mid.replace(0, np.nan)
    d = (bx - bx.shift(69)) / float(69)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_drifteff_252d_slope_v070_signal(closeadj):
    net = (closeadj / closeadj.shift(252) - 1.0)
    path = closeadj.pct_change().abs().rolling(252, min_periods=126).sum()
    bx = net / path.replace(0, np.nan)
    result = (bx - bx.shift(13)) / float(13)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_drifteff_252d_slope_v071_signal(closeadj):
    net = (closeadj / closeadj.shift(252) - 1.0)
    path = closeadj.pct_change().abs().rolling(252, min_periods=126).sum()
    bx = net / path.replace(0, np.nan)
    sm = bx.ewm(span=27, min_periods=max(2, 27 // 2)).mean()
    result = (sm - sm.shift(27)) / float(27)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_drifteff_252d_slope_v072_signal(closeadj):
    net = (closeadj / closeadj.shift(252) - 1.0)
    path = closeadj.pct_change().abs().rolling(252, min_periods=126).sum()
    bx = net / path.replace(0, np.nan)
    d = (bx - bx.shift(72)) / float(72)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_ampshrink_252d_slope_v073_signal(closeadj):
    a252 = (_rmax(closeadj, 252) - _rmin(closeadj, 252)) / closeadj.replace(0, np.nan)
    a504 = (_rmax(closeadj, 504) - _rmin(closeadj, 504)) / closeadj.replace(0, np.nan)
    bx = a252 / a504.replace(0, np.nan)
    result = (bx - bx.shift(14)) / float(14)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_ampshrink_252d_slope_v074_signal(closeadj):
    a252 = (_rmax(closeadj, 252) - _rmin(closeadj, 252)) / closeadj.replace(0, np.nan)
    a504 = (_rmax(closeadj, 504) - _rmin(closeadj, 504)) / closeadj.replace(0, np.nan)
    bx = a252 / a504.replace(0, np.nan)
    sm = bx.ewm(span=29, min_periods=max(2, 29 // 2)).mean()
    result = (sm - sm.shift(29)) / float(29)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_ampshrink_252d_slope_v075_signal(closeadj):
    a252 = (_rmax(closeadj, 252) - _rmin(closeadj, 252)) / closeadj.replace(0, np.nan)
    a504 = (_rmax(closeadj, 504) - _rmin(closeadj, 504)) / closeadj.replace(0, np.nan)
    bx = a252 / a504.replace(0, np.nan)
    d = (bx - bx.shift(75)) / float(75)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_failsev_252d_slope_v076_signal(high, closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    overshoot = (high / ceil.replace(0, np.nan) - 1.0).clip(lower=0.0)
    failed = overshoot * (closeadj <= ceil).astype(float)
    bx = failed.rolling(63, min_periods=21).mean()
    result = (bx - bx.shift(10)) / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_failsev_252d_slope_v077_signal(high, closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    overshoot = (high / ceil.replace(0, np.nan) - 1.0).clip(lower=0.0)
    failed = overshoot * (closeadj <= ceil).astype(float)
    bx = failed.rolling(63, min_periods=21).mean()
    sm = bx.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_failsev_252d_slope_v078_signal(high, closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    overshoot = (high / ceil.replace(0, np.nan) - 1.0).clip(lower=0.0)
    failed = overshoot * (closeadj <= ceil).astype(float)
    bx = failed.rolling(63, min_periods=21).mean()
    d = (bx - bx.shift(63)) / float(63)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_baseamp_1260d_slope_v079_signal(closeadj):
    bx = np.log(_rmax(closeadj, 1260).replace(0, np.nan) / _rmin(closeadj, 1260).replace(0, np.nan))
    result = (bx - bx.shift(22)) / float(22)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_baseamp_1260d_slope_v080_signal(closeadj):
    bx = np.log(_rmax(closeadj, 1260).replace(0, np.nan) / _rmin(closeadj, 1260).replace(0, np.nan))
    sm = bx.ewm(span=65, min_periods=max(2, 65 // 2)).mean()
    result = (sm - sm.shift(65)) / float(65)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_baseamp_1260d_slope_v081_signal(closeadj):
    bx = np.log(_rmax(closeadj, 1260).replace(0, np.nan) / _rmin(closeadj, 1260).replace(0, np.nan))
    d = (bx - bx.shift(129)) / float(129)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_drought_1260d_slope_v082_signal(closeadj):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    bx = closeadj.rolling(1260, min_periods=504).apply(_f, raw=True)
    result = (bx - bx.shift(23)) / float(23)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_drought_1260d_slope_v083_signal(closeadj):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    bx = closeadj.rolling(1260, min_periods=504).apply(_f, raw=True)
    sm = bx.ewm(span=67, min_periods=max(2, 67 // 2)).mean()
    result = (sm - sm.shift(67)) / float(67)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_drought_1260d_slope_v084_signal(closeadj):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    bx = closeadj.rolling(1260, min_periods=504).apply(_f, raw=True)
    d = (bx - bx.shift(132)) / float(132)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_extexh_252d_slope_v085_signal(closeadj):
    cd = _ceiling_dist(closeadj, 252).clip(lower=0.0)
    bx = cd / cd.rolling(63, min_periods=21).max().replace(0, np.nan)
    result = (bx - bx.shift(13)) / float(13)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_extexh_252d_slope_v086_signal(closeadj):
    cd = _ceiling_dist(closeadj, 252).clip(lower=0.0)
    bx = cd / cd.rolling(63, min_periods=21).max().replace(0, np.nan)
    sm = bx.ewm(span=27, min_periods=max(2, 27 // 2)).mean()
    result = (sm - sm.shift(27)) / float(27)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_extexh_252d_slope_v087_signal(closeadj):
    cd = _ceiling_dist(closeadj, 252).clip(lower=0.0)
    bx = cd / cd.rolling(63, min_periods=21).max().replace(0, np.nan)
    d = (bx - bx.shift(72)) / float(72)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_thrustamp_252d_slope_v088_signal(closeadj):
    r21 = (closeadj / closeadj.shift(21) - 1.0)
    amp = (_rmax(closeadj, 252) - _rmin(closeadj, 252)) / closeadj.replace(0, np.nan)
    bx = r21 / amp.replace(0, np.nan)
    result = (bx - bx.shift(14)) / float(14)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_thrustamp_252d_slope_v089_signal(closeadj):
    r21 = (closeadj / closeadj.shift(21) - 1.0)
    amp = (_rmax(closeadj, 252) - _rmin(closeadj, 252)) / closeadj.replace(0, np.nan)
    bx = r21 / amp.replace(0, np.nan)
    sm = bx.ewm(span=29, min_periods=max(2, 29 // 2)).mean()
    result = (sm - sm.shift(29)) / float(29)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_thrustamp_252d_slope_v090_signal(closeadj):
    r21 = (closeadj / closeadj.shift(21) - 1.0)
    amp = (_rmax(closeadj, 252) - _rmin(closeadj, 252)) / closeadj.replace(0, np.nan)
    bx = r21 / amp.replace(0, np.nan)
    d = (bx - bx.shift(75)) / float(75)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_midbias_252d_slope_v091_signal(closeadj):
    mid = (_rmax(closeadj, 252) + _rmin(closeadj, 252)) / 2.0
    bx = np.sign(closeadj - mid).rolling(21, min_periods=10).mean()
    result = (bx - bx.shift(10)) / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_midbias_252d_slope_v092_signal(closeadj):
    mid = (_rmax(closeadj, 252) + _rmin(closeadj, 252)) / 2.0
    bx = np.sign(closeadj - mid).rolling(21, min_periods=10).mean()
    sm = bx.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_midbias_252d_slope_v093_signal(closeadj):
    mid = (_rmax(closeadj, 252) + _rmin(closeadj, 252)) / 2.0
    bx = np.sign(closeadj - mid).rolling(21, min_periods=10).mean()
    d = (bx - bx.shift(63)) / float(63)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_higherlows_252d_slope_v094_signal(closeadj):
    lo63 = _rmin(closeadj, 63)
    bx = (lo63 > lo63.shift(21)).astype(float).rolling(252, min_periods=126).mean()
    result = (bx - bx.shift(11)) / float(11)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_higherlows_252d_slope_v095_signal(closeadj):
    lo63 = _rmin(closeadj, 63)
    bx = (lo63 > lo63.shift(21)).astype(float).rolling(252, min_periods=126).mean()
    sm = bx.ewm(span=23, min_periods=max(2, 23 // 2)).mean()
    result = (sm - sm.shift(23)) / float(23)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_higherlows_252d_slope_v096_signal(closeadj):
    lo63 = _rmin(closeadj, 63)
    bx = (lo63 > lo63.shift(21)).astype(float).rolling(252, min_periods=126).mean()
    d = (bx - bx.shift(66)) / float(66)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_coilint_504d_slope_v097_signal(closeadj):
    bx = _basepos(closeadj, 504) / _base_range(closeadj, 504).replace(0, np.nan)
    result = (bx - bx.shift(23)) / float(23)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_coilint_504d_slope_v098_signal(closeadj):
    bx = _basepos(closeadj, 504) / _base_range(closeadj, 504).replace(0, np.nan)
    sm = bx.ewm(span=67, min_periods=max(2, 67 // 2)).mean()
    result = (sm - sm.shift(67)) / float(67)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_coilint_504d_slope_v099_signal(closeadj):
    bx = _basepos(closeadj, 504) / _base_range(closeadj, 504).replace(0, np.nan)
    d = (bx - bx.shift(132)) / float(132)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_retest_252d_slope_v100_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    mid = (hi + lo) / 2.0
    bx = (_rmin(closeadj, 63) - mid) / (hi - lo).replace(0, np.nan)
    result = (bx - bx.shift(13)) / float(13)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_retest_252d_slope_v101_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    mid = (hi + lo) / 2.0
    bx = (_rmin(closeadj, 63) - mid) / (hi - lo).replace(0, np.nan)
    sm = bx.ewm(span=27, min_periods=max(2, 27 // 2)).mean()
    result = (sm - sm.shift(27)) / float(27)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_retest_252d_slope_v102_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    mid = (hi + lo) / 2.0
    bx = (_rmin(closeadj, 63) - mid) / (hi - lo).replace(0, np.nan)
    d = (bx - bx.shift(72)) / float(72)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_tightz_1260d_slope_v103_signal(closeadj):
    bx = _z(_tightness(closeadj, 1260), 252)
    result = (bx - bx.shift(25)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_tightz_1260d_slope_v104_signal(closeadj):
    bx = _z(_tightness(closeadj, 1260), 252)
    sm = bx.ewm(span=71, min_periods=max(2, 71 // 2)).mean()
    result = (sm - sm.shift(71)) / float(71)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_tightz_1260d_slope_v105_signal(closeadj):
    bx = _z(_tightness(closeadj, 1260), 252)
    d = (bx - bx.shift(138)) / float(138)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_gapthrust_252d_slope_v106_signal(closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    near = (closeadj / ceil.replace(0, np.nan) >= 0.95).astype(float)
    r1 = (closeadj / closeadj.shift(1) - 1.0)
    bx = (near * r1).rolling(21, min_periods=10).mean()
    result = (bx - bx.shift(10)) / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_gapthrust_252d_slope_v107_signal(closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    near = (closeadj / ceil.replace(0, np.nan) >= 0.95).astype(float)
    r1 = (closeadj / closeadj.shift(1) - 1.0)
    bx = (near * r1).rolling(21, min_periods=10).mean()
    sm = bx.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_gapthrust_252d_slope_v108_signal(closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    near = (closeadj / ceil.replace(0, np.nan) >= 0.95).astype(float)
    r1 = (closeadj / closeadj.shift(1) - 1.0)
    bx = (near * r1).rolling(21, min_periods=10).mean()
    d = (bx - bx.shift(63)) / float(63)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_pathineff_504d_slope_v109_signal(closeadj):
    net = (closeadj / closeadj.shift(504) - 1.0).abs()
    path = closeadj.pct_change().abs().rolling(504, min_periods=252).sum()
    bx = net / path.replace(0, np.nan)
    result = (bx - bx.shift(22)) / float(22)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_pathineff_504d_slope_v110_signal(closeadj):
    net = (closeadj / closeadj.shift(504) - 1.0).abs()
    path = closeadj.pct_change().abs().rolling(504, min_periods=252).sum()
    bx = net / path.replace(0, np.nan)
    sm = bx.ewm(span=65, min_periods=max(2, 65 // 2)).mean()
    result = (sm - sm.shift(65)) / float(65)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_pathineff_504d_slope_v111_signal(closeadj):
    net = (closeadj / closeadj.shift(504) - 1.0).abs()
    path = closeadj.pct_change().abs().rolling(504, min_periods=252).sum()
    bx = net / path.replace(0, np.nan)
    d = (bx - bx.shift(129)) / float(129)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_widthstab_252d_slope_v112_signal(closeadj):
    bx = _base_range(closeadj, 252).rolling(126, min_periods=63).std()
    result = (bx - bx.shift(12)) / float(12)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_widthstab_252d_slope_v113_signal(closeadj):
    bx = _base_range(closeadj, 252).rolling(126, min_periods=63).std()
    sm = bx.ewm(span=25, min_periods=max(2, 25 // 2)).mean()
    result = (sm - sm.shift(25)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_widthstab_252d_slope_v114_signal(closeadj):
    bx = _base_range(closeadj, 252).rolling(126, min_periods=63).std()
    d = (bx - bx.shift(69)) / float(69)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_longprox_1260d_slope_v115_signal(closeadj):
    bx = (closeadj / _rmax(closeadj, 1260).replace(0, np.nan)).ewm(span=63, min_periods=21).mean()
    result = (bx - bx.shift(24)) / float(24)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_longprox_1260d_slope_v116_signal(closeadj):
    bx = (closeadj / _rmax(closeadj, 1260).replace(0, np.nan)).ewm(span=63, min_periods=21).mean()
    sm = bx.ewm(span=69, min_periods=max(2, 69 // 2)).mean()
    result = (sm - sm.shift(69)) / float(69)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_longprox_1260d_slope_v117_signal(closeadj):
    bx = (closeadj / _rmax(closeadj, 1260).replace(0, np.nan)).ewm(span=63, min_periods=21).mean()
    d = (bx - bx.shift(135)) / float(135)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_ceilrank_252d_slope_v118_signal(closeadj):
    bx = _rank(_ceiling_dist(closeadj, 252), 504)
    result = (bx - bx.shift(14)) / float(14)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_ceilrank_252d_slope_v119_signal(closeadj):
    bx = _rank(_ceiling_dist(closeadj, 252), 504)
    sm = bx.ewm(span=29, min_periods=max(2, 29 // 2)).mean()
    result = (sm - sm.shift(29)) / float(29)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_ceilrank_252d_slope_v120_signal(closeadj):
    bx = _rank(_ceiling_dist(closeadj, 252), 504)
    d = (bx - bx.shift(75)) / float(75)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_floorrank_252d_slope_v121_signal(closeadj):
    bx = _rank(_floor_dist(closeadj, 252), 504)
    result = (bx - bx.shift(10)) / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_floorrank_252d_slope_v122_signal(closeadj):
    bx = _rank(_floor_dist(closeadj, 252), 504)
    sm = bx.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_floorrank_252d_slope_v123_signal(closeadj):
    bx = _rank(_floor_dist(closeadj, 252), 504)
    d = (bx - bx.shift(63)) / float(63)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_quietdays_252d_slope_v124_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    quiet = (rng <= rng.rolling(504, min_periods=126).quantile(0.3)).astype(float)
    bx = quiet.rolling(252, min_periods=126).mean()
    result = (bx - bx.shift(11)) / float(11)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_quietdays_252d_slope_v125_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    quiet = (rng <= rng.rolling(504, min_periods=126).quantile(0.3)).astype(float)
    bx = quiet.rolling(252, min_periods=126).mean()
    sm = bx.ewm(span=23, min_periods=max(2, 23 // 2)).mean()
    result = (sm - sm.shift(23)) / float(23)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_quietdays_252d_slope_v126_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    quiet = (rng <= rng.rolling(504, min_periods=126).quantile(0.3)).astype(float)
    bx = quiet.rolling(252, min_periods=126).mean()
    d = (bx - bx.shift(66)) / float(66)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_rangeposrank1260_1260d_slope_v127_signal(closeadj):
    bx = _rank(_basepos(closeadj, 1260), 504)
    result = (bx - bx.shift(23)) / float(23)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_rangeposrank1260_1260d_slope_v128_signal(closeadj):
    bx = _rank(_basepos(closeadj, 1260), 504)
    sm = bx.ewm(span=67, min_periods=max(2, 67 // 2)).mean()
    result = (sm - sm.shift(67)) / float(67)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_rangeposrank1260_1260d_slope_v129_signal(closeadj):
    bx = _rank(_basepos(closeadj, 1260), 504)
    d = (bx - bx.shift(132)) / float(132)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_lidcatch_252d_slope_v130_signal(closeadj):
    ceil = _rmax(closeadj, 252)
    cs = np.log(ceil.replace(0, np.nan) / ceil.shift(63).replace(0, np.nan))
    ps = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    bx = ps - cs
    result = (bx - bx.shift(13)) / float(13)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_lidcatch_252d_slope_v131_signal(closeadj):
    ceil = _rmax(closeadj, 252)
    cs = np.log(ceil.replace(0, np.nan) / ceil.shift(63).replace(0, np.nan))
    ps = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    bx = ps - cs
    sm = bx.ewm(span=27, min_periods=max(2, 27 // 2)).mean()
    result = (sm - sm.shift(27)) / float(27)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_lidcatch_252d_slope_v132_signal(closeadj):
    ceil = _rmax(closeadj, 252)
    cs = np.log(ceil.replace(0, np.nan) / ceil.shift(63).replace(0, np.nan))
    ps = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    bx = ps - cs
    d = (bx - bx.shift(72)) / float(72)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_converge_252d_slope_v133_signal(closeadj):
    ceil = _rmax(closeadj, 252)
    fl = _rmin(closeadj, 252)
    cs = np.log(ceil.replace(0, np.nan) / ceil.shift(63).replace(0, np.nan))
    fs = np.log(fl.replace(0, np.nan) / fl.shift(63).replace(0, np.nan))
    bx = fs - cs
    result = (bx - bx.shift(14)) / float(14)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_converge_252d_slope_v134_signal(closeadj):
    ceil = _rmax(closeadj, 252)
    fl = _rmin(closeadj, 252)
    cs = np.log(ceil.replace(0, np.nan) / ceil.shift(63).replace(0, np.nan))
    fs = np.log(fl.replace(0, np.nan) / fl.shift(63).replace(0, np.nan))
    bx = fs - cs
    sm = bx.ewm(span=29, min_periods=max(2, 29 // 2)).mean()
    result = (sm - sm.shift(29)) / float(29)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_converge_252d_slope_v135_signal(closeadj):
    ceil = _rmax(closeadj, 252)
    fl = _rmin(closeadj, 252)
    cs = np.log(ceil.replace(0, np.nan) / ceil.shift(63).replace(0, np.nan))
    fs = np.log(fl.replace(0, np.nan) / fl.shift(63).replace(0, np.nan))
    bx = fs - cs
    d = (bx - bx.shift(75)) / float(75)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_hiextend_252d_slope_v136_signal(closeadj):
    hi = _rmax(closeadj, 252)
    mn = _mean(closeadj, 252)
    bx = (hi - mn) / mn.replace(0, np.nan)
    result = (bx - bx.shift(10)) / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_hiextend_252d_slope_v137_signal(closeadj):
    hi = _rmax(closeadj, 252)
    mn = _mean(closeadj, 252)
    bx = (hi - mn) / mn.replace(0, np.nan)
    sm = bx.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_hiextend_252d_slope_v138_signal(closeadj):
    hi = _rmax(closeadj, 252)
    mn = _mean(closeadj, 252)
    bx = (hi - mn) / mn.replace(0, np.nan)
    d = (bx - bx.shift(63)) / float(63)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_loextend_252d_slope_v139_signal(closeadj):
    lo = _rmin(closeadj, 252)
    mn = _mean(closeadj, 252)
    bx = (mn - lo) / mn.replace(0, np.nan)
    result = (bx - bx.shift(11)) / float(11)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_loextend_252d_slope_v140_signal(closeadj):
    lo = _rmin(closeadj, 252)
    mn = _mean(closeadj, 252)
    bx = (mn - lo) / mn.replace(0, np.nan)
    sm = bx.ewm(span=23, min_periods=max(2, 23 // 2)).mean()
    result = (sm - sm.shift(23)) / float(23)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_loextend_252d_slope_v141_signal(closeadj):
    lo = _rmin(closeadj, 252)
    mn = _mean(closeadj, 252)
    bx = (mn - lo) / mn.replace(0, np.nan)
    d = (bx - bx.shift(66)) / float(66)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_basedrift_252d_slope_v142_signal(closeadj):
    bx = np.log(_mean(closeadj, 21).replace(0, np.nan) / _mean(closeadj, 252).replace(0, np.nan))
    result = (bx - bx.shift(12)) / float(12)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_basedrift_252d_slope_v143_signal(closeadj):
    bx = np.log(_mean(closeadj, 21).replace(0, np.nan) / _mean(closeadj, 252).replace(0, np.nan))
    sm = bx.ewm(span=25, min_periods=max(2, 25 // 2)).mean()
    result = (sm - sm.shift(25)) / float(25)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_basedrift_252d_slope_v144_signal(closeadj):
    bx = np.log(_mean(closeadj, 21).replace(0, np.nan) / _mean(closeadj, 252).replace(0, np.nan))
    d = (bx - bx.shift(69)) / float(69)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_pkrange_252d_slope_v145_signal(high, low, closeadj):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    bx = np.sqrt((hl ** 2).rolling(252, min_periods=126).mean() / (4.0 * np.log(2.0)))
    result = (bx - bx.shift(13)) / float(13)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_pkrange_252d_slope_v146_signal(high, low, closeadj):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    bx = np.sqrt((hl ** 2).rolling(252, min_periods=126).mean() / (4.0 * np.log(2.0)))
    sm = bx.ewm(span=27, min_periods=max(2, 27 // 2)).mean()
    result = (sm - sm.shift(27)) / float(27)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_pkrange_252d_slope_v147_signal(high, low, closeadj):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    bx = np.sqrt((hl ** 2).rolling(252, min_periods=126).mean() / (4.0 * np.log(2.0)))
    d = (bx - bx.shift(72)) / float(72)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_voldry_252d_slope_v148_signal(volume):
    bx = _mean(volume, 21) / _mean(volume, 252).replace(0, np.nan)
    result = (bx - bx.shift(14)) / float(14)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_voldry_252d_slope_v149_signal(volume):
    bx = _mean(volume, 21) / _mean(volume, 252).replace(0, np.nan)
    sm = bx.ewm(span=29, min_periods=max(2, 29 // 2)).mean()
    result = (sm - sm.shift(29)) / float(29)
    return result.replace([np.inf, -np.inf], np.nan)


def f06lb_f06_long_base_breakout_voldry_252d_slope_v150_signal(volume):
    bx = _mean(volume, 21) / _mean(volume, 252).replace(0, np.nan)
    d = (bx - bx.shift(75)) / float(75)
    result = d / d.rolling(126, min_periods=42).std().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06lb_f06_long_base_breakout_baserange_252d_slope_v001_signal,
    f06lb_f06_long_base_breakout_baserange_252d_slope_v002_signal,
    f06lb_f06_long_base_breakout_baserange_252d_slope_v003_signal,
    f06lb_f06_long_base_breakout_tight_252d_slope_v004_signal,
    f06lb_f06_long_base_breakout_tight_252d_slope_v005_signal,
    f06lb_f06_long_base_breakout_tight_252d_slope_v006_signal,
    f06lb_f06_long_base_breakout_tightlong_504d_slope_v007_signal,
    f06lb_f06_long_base_breakout_tightlong_504d_slope_v008_signal,
    f06lb_f06_long_base_breakout_tightlong_504d_slope_v009_signal,
    f06lb_f06_long_base_breakout_ceildist_252d_slope_v010_signal,
    f06lb_f06_long_base_breakout_ceildist_252d_slope_v011_signal,
    f06lb_f06_long_base_breakout_ceildist_252d_slope_v012_signal,
    f06lb_f06_long_base_breakout_failrate_504d_slope_v013_signal,
    f06lb_f06_long_base_breakout_failrate_504d_slope_v014_signal,
    f06lb_f06_long_base_breakout_failrate_504d_slope_v015_signal,
    f06lb_f06_long_base_breakout_floordist_252d_slope_v016_signal,
    f06lb_f06_long_base_breakout_floordist_252d_slope_v017_signal,
    f06lb_f06_long_base_breakout_floordist_252d_slope_v018_signal,
    f06lb_f06_long_base_breakout_breakout_252d_slope_v019_signal,
    f06lb_f06_long_base_breakout_breakout_252d_slope_v020_signal,
    f06lb_f06_long_base_breakout_breakout_252d_slope_v021_signal,
    f06lb_f06_long_base_breakout_basepos_252d_slope_v022_signal,
    f06lb_f06_long_base_breakout_basepos_252d_slope_v023_signal,
    f06lb_f06_long_base_breakout_basepos_252d_slope_v024_signal,
    f06lb_f06_long_base_breakout_baseposdisp_504d_slope_v025_signal,
    f06lb_f06_long_base_breakout_baseposdisp_504d_slope_v026_signal,
    f06lb_f06_long_base_breakout_baseposdisp_504d_slope_v027_signal,
    f06lb_f06_long_base_breakout_channelmid_504d_slope_v028_signal,
    f06lb_f06_long_base_breakout_channelmid_504d_slope_v029_signal,
    f06lb_f06_long_base_breakout_channelmid_504d_slope_v030_signal,
    f06lb_f06_long_base_breakout_amplitude_252d_slope_v031_signal,
    f06lb_f06_long_base_breakout_amplitude_252d_slope_v032_signal,
    f06lb_f06_long_base_breakout_amplitude_252d_slope_v033_signal,
    f06lb_f06_long_base_breakout_midpoint_252d_slope_v034_signal,
    f06lb_f06_long_base_breakout_midpoint_252d_slope_v035_signal,
    f06lb_f06_long_base_breakout_midpoint_252d_slope_v036_signal,
    f06lb_f06_long_base_breakout_contract_252d_slope_v037_signal,
    f06lb_f06_long_base_breakout_contract_252d_slope_v038_signal,
    f06lb_f06_long_base_breakout_contract_252d_slope_v039_signal,
    f06lb_f06_long_base_breakout_quietcoil_252d_slope_v040_signal,
    f06lb_f06_long_base_breakout_quietcoil_252d_slope_v041_signal,
    f06lb_f06_long_base_breakout_quietcoil_252d_slope_v042_signal,
    f06lb_f06_long_base_breakout_coil_252d_slope_v043_signal,
    f06lb_f06_long_base_breakout_coil_252d_slope_v044_signal,
    f06lb_f06_long_base_breakout_coil_252d_slope_v045_signal,
    f06lb_f06_long_base_breakout_baselift_1260d_slope_v046_signal,
    f06lb_f06_long_base_breakout_baselift_1260d_slope_v047_signal,
    f06lb_f06_long_base_breakout_baselift_1260d_slope_v048_signal,
    f06lb_f06_long_base_breakout_upperhug_504d_slope_v049_signal,
    f06lb_f06_long_base_breakout_upperhug_504d_slope_v050_signal,
    f06lb_f06_long_base_breakout_upperhug_504d_slope_v051_signal,
    f06lb_f06_long_base_breakout_ceilslope_252d_slope_v052_signal,
    f06lb_f06_long_base_breakout_ceilslope_252d_slope_v053_signal,
    f06lb_f06_long_base_breakout_ceilslope_252d_slope_v054_signal,
    f06lb_f06_long_base_breakout_floorslope_252d_slope_v055_signal,
    f06lb_f06_long_base_breakout_floorslope_252d_slope_v056_signal,
    f06lb_f06_long_base_breakout_floorslope_252d_slope_v057_signal,
    f06lb_f06_long_base_breakout_microcoil_252d_slope_v058_signal,
    f06lb_f06_long_base_breakout_microcoil_252d_slope_v059_signal,
    f06lb_f06_long_base_breakout_microcoil_252d_slope_v060_signal,
    f06lb_f06_long_base_breakout_pinch_252d_slope_v061_signal,
    f06lb_f06_long_base_breakout_pinch_252d_slope_v062_signal,
    f06lb_f06_long_base_breakout_pinch_252d_slope_v063_signal,
    f06lb_f06_long_base_breakout_flatness_504d_slope_v064_signal,
    f06lb_f06_long_base_breakout_flatness_504d_slope_v065_signal,
    f06lb_f06_long_base_breakout_flatness_504d_slope_v066_signal,
    f06lb_f06_long_base_breakout_tightasym_252d_slope_v067_signal,
    f06lb_f06_long_base_breakout_tightasym_252d_slope_v068_signal,
    f06lb_f06_long_base_breakout_tightasym_252d_slope_v069_signal,
    f06lb_f06_long_base_breakout_drifteff_252d_slope_v070_signal,
    f06lb_f06_long_base_breakout_drifteff_252d_slope_v071_signal,
    f06lb_f06_long_base_breakout_drifteff_252d_slope_v072_signal,
    f06lb_f06_long_base_breakout_ampshrink_252d_slope_v073_signal,
    f06lb_f06_long_base_breakout_ampshrink_252d_slope_v074_signal,
    f06lb_f06_long_base_breakout_ampshrink_252d_slope_v075_signal,
    f06lb_f06_long_base_breakout_failsev_252d_slope_v076_signal,
    f06lb_f06_long_base_breakout_failsev_252d_slope_v077_signal,
    f06lb_f06_long_base_breakout_failsev_252d_slope_v078_signal,
    f06lb_f06_long_base_breakout_baseamp_1260d_slope_v079_signal,
    f06lb_f06_long_base_breakout_baseamp_1260d_slope_v080_signal,
    f06lb_f06_long_base_breakout_baseamp_1260d_slope_v081_signal,
    f06lb_f06_long_base_breakout_drought_1260d_slope_v082_signal,
    f06lb_f06_long_base_breakout_drought_1260d_slope_v083_signal,
    f06lb_f06_long_base_breakout_drought_1260d_slope_v084_signal,
    f06lb_f06_long_base_breakout_extexh_252d_slope_v085_signal,
    f06lb_f06_long_base_breakout_extexh_252d_slope_v086_signal,
    f06lb_f06_long_base_breakout_extexh_252d_slope_v087_signal,
    f06lb_f06_long_base_breakout_thrustamp_252d_slope_v088_signal,
    f06lb_f06_long_base_breakout_thrustamp_252d_slope_v089_signal,
    f06lb_f06_long_base_breakout_thrustamp_252d_slope_v090_signal,
    f06lb_f06_long_base_breakout_midbias_252d_slope_v091_signal,
    f06lb_f06_long_base_breakout_midbias_252d_slope_v092_signal,
    f06lb_f06_long_base_breakout_midbias_252d_slope_v093_signal,
    f06lb_f06_long_base_breakout_higherlows_252d_slope_v094_signal,
    f06lb_f06_long_base_breakout_higherlows_252d_slope_v095_signal,
    f06lb_f06_long_base_breakout_higherlows_252d_slope_v096_signal,
    f06lb_f06_long_base_breakout_coilint_504d_slope_v097_signal,
    f06lb_f06_long_base_breakout_coilint_504d_slope_v098_signal,
    f06lb_f06_long_base_breakout_coilint_504d_slope_v099_signal,
    f06lb_f06_long_base_breakout_retest_252d_slope_v100_signal,
    f06lb_f06_long_base_breakout_retest_252d_slope_v101_signal,
    f06lb_f06_long_base_breakout_retest_252d_slope_v102_signal,
    f06lb_f06_long_base_breakout_tightz_1260d_slope_v103_signal,
    f06lb_f06_long_base_breakout_tightz_1260d_slope_v104_signal,
    f06lb_f06_long_base_breakout_tightz_1260d_slope_v105_signal,
    f06lb_f06_long_base_breakout_gapthrust_252d_slope_v106_signal,
    f06lb_f06_long_base_breakout_gapthrust_252d_slope_v107_signal,
    f06lb_f06_long_base_breakout_gapthrust_252d_slope_v108_signal,
    f06lb_f06_long_base_breakout_pathineff_504d_slope_v109_signal,
    f06lb_f06_long_base_breakout_pathineff_504d_slope_v110_signal,
    f06lb_f06_long_base_breakout_pathineff_504d_slope_v111_signal,
    f06lb_f06_long_base_breakout_widthstab_252d_slope_v112_signal,
    f06lb_f06_long_base_breakout_widthstab_252d_slope_v113_signal,
    f06lb_f06_long_base_breakout_widthstab_252d_slope_v114_signal,
    f06lb_f06_long_base_breakout_longprox_1260d_slope_v115_signal,
    f06lb_f06_long_base_breakout_longprox_1260d_slope_v116_signal,
    f06lb_f06_long_base_breakout_longprox_1260d_slope_v117_signal,
    f06lb_f06_long_base_breakout_ceilrank_252d_slope_v118_signal,
    f06lb_f06_long_base_breakout_ceilrank_252d_slope_v119_signal,
    f06lb_f06_long_base_breakout_ceilrank_252d_slope_v120_signal,
    f06lb_f06_long_base_breakout_floorrank_252d_slope_v121_signal,
    f06lb_f06_long_base_breakout_floorrank_252d_slope_v122_signal,
    f06lb_f06_long_base_breakout_floorrank_252d_slope_v123_signal,
    f06lb_f06_long_base_breakout_quietdays_252d_slope_v124_signal,
    f06lb_f06_long_base_breakout_quietdays_252d_slope_v125_signal,
    f06lb_f06_long_base_breakout_quietdays_252d_slope_v126_signal,
    f06lb_f06_long_base_breakout_rangeposrank1260_1260d_slope_v127_signal,
    f06lb_f06_long_base_breakout_rangeposrank1260_1260d_slope_v128_signal,
    f06lb_f06_long_base_breakout_rangeposrank1260_1260d_slope_v129_signal,
    f06lb_f06_long_base_breakout_lidcatch_252d_slope_v130_signal,
    f06lb_f06_long_base_breakout_lidcatch_252d_slope_v131_signal,
    f06lb_f06_long_base_breakout_lidcatch_252d_slope_v132_signal,
    f06lb_f06_long_base_breakout_converge_252d_slope_v133_signal,
    f06lb_f06_long_base_breakout_converge_252d_slope_v134_signal,
    f06lb_f06_long_base_breakout_converge_252d_slope_v135_signal,
    f06lb_f06_long_base_breakout_hiextend_252d_slope_v136_signal,
    f06lb_f06_long_base_breakout_hiextend_252d_slope_v137_signal,
    f06lb_f06_long_base_breakout_hiextend_252d_slope_v138_signal,
    f06lb_f06_long_base_breakout_loextend_252d_slope_v139_signal,
    f06lb_f06_long_base_breakout_loextend_252d_slope_v140_signal,
    f06lb_f06_long_base_breakout_loextend_252d_slope_v141_signal,
    f06lb_f06_long_base_breakout_basedrift_252d_slope_v142_signal,
    f06lb_f06_long_base_breakout_basedrift_252d_slope_v143_signal,
    f06lb_f06_long_base_breakout_basedrift_252d_slope_v144_signal,
    f06lb_f06_long_base_breakout_pkrange_252d_slope_v145_signal,
    f06lb_f06_long_base_breakout_pkrange_252d_slope_v146_signal,
    f06lb_f06_long_base_breakout_pkrange_252d_slope_v147_signal,
    f06lb_f06_long_base_breakout_voldry_252d_slope_v148_signal,
    f06lb_f06_long_base_breakout_voldry_252d_slope_v149_signal,
    f06lb_f06_long_base_breakout_voldry_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_LONG_BASE_BREAKOUT_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

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

    print("OK f06_long_base_breakout_2nd_derivatives_001_150_claude: %d features pass" % n_features)
