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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== folder anchoring primitives (52-week / multi-year) =====
def _f07_anchor_gap_hi(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(close.replace(0, np.nan) / hi.replace(0, np.nan))


def _f07_anchor_gap_lo(close, w):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return np.log(close.replace(0, np.nan) / lo.replace(0, np.nan))


def _f07_bandpos(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (close - lo) / (hi - lo).replace(0, np.nan)


def _f07_newhigh_flag(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close >= hi * 0.99999).astype(float)


def _f07_newlow_flag(close, w):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (close <= lo * 1.00001).astype(float)


def _f07_freq(flag, cw):
    return flag.rolling(cw, min_periods=max(1, cw // 2)).mean()


def _f07_anchor_dist(close, wa, wb):
    a = close.rolling(wa, min_periods=max(1, wa // 2)).max()
    b = close.rolling(wb, min_periods=max(1, wb // 2)).max()
    return np.log(a.replace(0, np.nan) / b.replace(0, np.nan))


def _f07_span(close, w):
    return np.log(_rmax(close, w).replace(0, np.nan) / _rmin(close, w).replace(0, np.nan))


def f07fw_f07_fiftytwo_week_position_gaphi63d_63d_jerk_v001_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 63)
    feat = base.ewm(span=max(5, 5), min_periods=max(3, 5//2)).mean()
    slope = feat.diff(5) / float(5)
    deriv = slope.diff(5) / float(5)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaphi210d_210d_jerk_v002_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 210)
    feat = base - base.rolling(max(5, 17), min_periods=max(1, 17//2)).mean()
    slope = feat.diff(17) / float(17)
    deriv = slope.diff(17) / float(17)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaphi357d_357d_jerk_v003_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 357)
    feat = _z(base, max(10, 29*2))
    slope = feat.diff(29) / float(29)
    deriv = slope.diff(29) / float(29)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaphi882d_882d_jerk_v004_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 882)
    feat = base
    slope = feat.diff(73) / float(73)
    deriv = slope.diff(73) / float(73)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaplo126d_126d_jerk_v005_signal(closeadj):
    base = _f07_anchor_gap_lo(closeadj, 126)
    feat = _z(base, max(10, 10*2))
    slope = feat.diff(10) / float(10)
    deriv = slope.diff(10) / float(10)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaplo273d_273d_jerk_v006_signal(closeadj):
    base = _f07_anchor_gap_lo(closeadj, 273)
    feat = base
    slope = feat.diff(22) / float(22)
    deriv = slope.diff(22) / float(22)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaplo462d_462d_jerk_v007_signal(closeadj):
    base = _f07_anchor_gap_lo(closeadj, 462)
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 38), min_periods=max(1, 38//2)).median()))
    slope = feat.diff(38) / float(38)
    deriv = slope.diff(38) / float(38)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaplo1260d_1260d_jerk_v008_signal(closeadj):
    base = _f07_anchor_gap_lo(closeadj, 1260)
    feat = base.ewm(span=max(5, 105), min_periods=max(3, 105//2)).mean()
    slope = feat.diff(105) / float(105)
    deriv = slope.diff(105) / float(105)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_bandpos189d_189d_jerk_v009_signal(closeadj):
    base = _f07_bandpos(closeadj, 189)
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 15), min_periods=max(1, 15//2)).median()))
    slope = feat.diff(15) / float(15)
    deriv = slope.diff(15) / float(15)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_bandpos336d_336d_jerk_v010_signal(closeadj):
    base = _f07_bandpos(closeadj, 336)
    feat = base.ewm(span=max(5, 28), min_periods=max(3, 28//2)).mean()
    slope = feat.diff(28) / float(28)
    deriv = slope.diff(28) / float(28)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_bandpos756d_756d_jerk_v011_signal(closeadj):
    base = _f07_bandpos(closeadj, 756)
    feat = base - base.rolling(max(5, 63), min_periods=max(1, 63//2)).mean()
    slope = feat.diff(63) / float(63)
    deriv = slope.diff(63) / float(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_span105d_105d_jerk_v012_signal(closeadj):
    base = _f07_span(closeadj, 105)
    feat = base.ewm(span=max(5, 8), min_periods=max(3, 8//2)).mean()
    slope = feat.diff(8) / float(8)
    deriv = slope.diff(8) / float(8)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_span252d_252d_jerk_v013_signal(closeadj):
    base = _f07_span(closeadj, 252)
    feat = base - base.rolling(max(5, 21), min_periods=max(1, 21//2)).mean()
    slope = feat.diff(21) / float(21)
    deriv = slope.diff(21) / float(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_span420d_420d_jerk_v014_signal(closeadj):
    base = _f07_span(closeadj, 420)
    feat = _z(base, max(10, 35*2))
    slope = feat.diff(35) / float(35)
    deriv = slope.diff(35) / float(35)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_span1134d_1134d_jerk_v015_signal(closeadj):
    base = _f07_span(closeadj, 1134)
    feat = base
    slope = feat.diff(94) / float(94)
    deriv = slope.diff(94) / float(94)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapresid168d_168d_jerk_v016_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, min(252, 168)) - _f07_anchor_gap_hi(closeadj, max(504, 168)))
    feat = _z(base, max(10, 14*2))
    slope = feat.diff(14) / float(14)
    deriv = slope.diff(14) / float(14)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loresid105d_105d_jerk_v017_signal(closeadj):
    base = (_f07_anchor_gap_lo(closeadj, min(252, 105)) - _f07_anchor_gap_lo(closeadj, max(504, 105)))
    feat = base - base.rolling(max(5, 8), min_periods=max(1, 8//2)).mean()
    slope = feat.diff(8) / float(8)
    deriv = slope.diff(8) / float(8)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loresid252d_252d_jerk_v018_signal(closeadj):
    base = (_f07_anchor_gap_lo(closeadj, min(252, 252)) - _f07_anchor_gap_lo(closeadj, max(504, 252)))
    feat = _z(base, max(10, 21*2))
    slope = feat.diff(21) / float(21)
    deriv = slope.diff(21) / float(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_nhfreq189d_189d_jerk_v019_signal(closeadj):
    base = (_f07_freq(_f07_newhigh_flag(closeadj, min(252, 189)), max(21, min(252, 189)//4)) + 0.5 * _f07_anchor_gap_hi(closeadj, min(252, 189)))
    feat = base - base.rolling(max(5, 15), min_periods=max(1, 15//2)).mean()
    slope = feat.diff(15) / float(15)
    deriv = slope.diff(15) / float(15)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_nlfreq126d_126d_jerk_v020_signal(closeadj):
    base = (_f07_freq(_f07_newlow_flag(closeadj, min(252, 126)), max(21, min(252, 126)//4)) - 0.5 * _f07_anchor_gap_lo(closeadj, min(252, 126)))
    feat = base.ewm(span=max(5, 10), min_periods=max(3, 10//2)).mean()
    slope = feat.diff(10) / float(10)
    deriv = slope.diff(10) / float(10)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_anchdist63d_63d_jerk_v021_signal(closeadj):
    base = _f07_anchor_dist(closeadj, min(252, 63), max(504, 63))
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 5), min_periods=max(1, 5//2)).median()))
    slope = feat.diff(5) / float(5)
    deriv = slope.diff(5) / float(5)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_anchdist210d_210d_jerk_v022_signal(closeadj):
    base = _f07_anchor_dist(closeadj, min(252, 210), max(504, 210))
    feat = base.ewm(span=max(5, 17), min_periods=max(3, 17//2)).mean()
    slope = feat.diff(17) / float(17)
    deriv = slope.diff(17) / float(17)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_hiext147d_147d_jerk_v023_signal(closeadj):
    base = ((_rmax(closeadj, 147) - _mean(closeadj, 147)) / _mean(closeadj, 147).replace(0, np.nan))
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 12), min_periods=max(1, 12//2)).median()))
    slope = feat.diff(12) / float(12)
    deriv = slope.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_hiext294d_294d_jerk_v024_signal(closeadj):
    base = ((_rmax(closeadj, 294) - _mean(closeadj, 294)) / _mean(closeadj, 294).replace(0, np.nan))
    feat = base.ewm(span=max(5, 24), min_periods=max(3, 24//2)).mean()
    slope = feat.diff(24) / float(24)
    deriv = slope.diff(24) / float(24)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_hiext504d_504d_jerk_v025_signal(closeadj):
    base = ((_rmax(closeadj, 504) - _mean(closeadj, 504)) / _mean(closeadj, 504).replace(0, np.nan))
    feat = base - base.rolling(max(5, 42), min_periods=max(1, 42//2)).mean()
    slope = feat.diff(42) / float(42)
    deriv = slope.diff(42) / float(42)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loext63d_63d_jerk_v026_signal(closeadj):
    base = ((_mean(closeadj, 63) - _rmin(closeadj, 63)) / _mean(closeadj, 63).replace(0, np.nan))
    feat = base.ewm(span=max(5, 5), min_periods=max(3, 5//2)).mean()
    slope = feat.diff(5) / float(5)
    deriv = slope.diff(5) / float(5)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loext210d_210d_jerk_v027_signal(closeadj):
    base = ((_mean(closeadj, 210) - _rmin(closeadj, 210)) / _mean(closeadj, 210).replace(0, np.nan))
    feat = base - base.rolling(max(5, 17), min_periods=max(1, 17//2)).mean()
    slope = feat.diff(17) / float(17)
    deriv = slope.diff(17) / float(17)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loext357d_357d_jerk_v028_signal(closeadj):
    base = ((_mean(closeadj, 357) - _rmin(closeadj, 357)) / _mean(closeadj, 357).replace(0, np.nan))
    feat = _z(base, max(10, 29*2))
    slope = feat.diff(29) / float(29)
    deriv = slope.diff(29) / float(29)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loext882d_882d_jerk_v029_signal(closeadj):
    base = ((_mean(closeadj, 882) - _rmin(closeadj, 882)) / _mean(closeadj, 882).replace(0, np.nan))
    feat = base
    slope = feat.diff(73) / float(73)
    deriv = slope.diff(73) / float(73)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_posroam126d_126d_jerk_v030_signal(closeadj):
    base = _f07_bandpos(closeadj, 126).rolling(max(21, 126//4), min_periods=max(1, 126//8)).std()
    feat = _z(base, max(10, 10*2))
    slope = feat.diff(10) / float(10)
    deriv = slope.diff(10) / float(10)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_posroam273d_273d_jerk_v031_signal(closeadj):
    base = _f07_bandpos(closeadj, 273).rolling(max(21, 273//4), min_periods=max(1, 273//8)).std()
    feat = base
    slope = feat.diff(22) / float(22)
    deriv = slope.diff(22) / float(22)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_posroam462d_462d_jerk_v032_signal(closeadj):
    base = _f07_bandpos(closeadj, 462).rolling(max(21, 462//4), min_periods=max(1, 462//8)).std()
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 38), min_periods=max(1, 38//2)).median()))
    slope = feat.diff(38) / float(38)
    deriv = slope.diff(38) / float(38)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_posroam1260d_1260d_jerk_v033_signal(closeadj):
    base = _f07_bandpos(closeadj, 1260).rolling(max(21, 1260//4), min_periods=max(1, 1260//8)).std()
    feat = base.ewm(span=max(5, 105), min_periods=max(3, 105//2)).mean()
    slope = feat.diff(105) / float(105)
    deriv = slope.diff(105) / float(105)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapz189d_189d_jerk_v034_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, 189) - _f07_anchor_gap_hi(closeadj, 189).ewm(span=max(10,189//6), min_periods=max(5,189//12)).mean())
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 15), min_periods=max(1, 15//2)).median()))
    slope = feat.diff(15) / float(15)
    deriv = slope.diff(15) / float(15)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapz336d_336d_jerk_v035_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, 336) - _f07_anchor_gap_hi(closeadj, 336).ewm(span=max(10,336//6), min_periods=max(5,336//12)).mean())
    feat = base.ewm(span=max(5, 28), min_periods=max(3, 28//2)).mean()
    slope = feat.diff(28) / float(28)
    deriv = slope.diff(28) / float(28)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapz756d_756d_jerk_v036_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, 756) - _f07_anchor_gap_hi(closeadj, 756).ewm(span=max(10,756//6), min_periods=max(5,756//12)).mean())
    feat = base - base.rolling(max(5, 63), min_periods=max(1, 63//2)).mean()
    slope = feat.diff(63) / float(63)
    deriv = slope.diff(63) / float(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_uppshare105d_105d_jerk_v037_signal(closeadj):
    base = (_f07_bandpos(closeadj, 105) >= 0.6667).astype(float).rolling(105, min_periods=max(1,105//2)).mean()
    feat = base.ewm(span=max(5, 8), min_periods=max(3, 8//2)).mean()
    slope = feat.diff(8) / float(8)
    deriv = slope.diff(8) / float(8)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_uppshare252d_252d_jerk_v038_signal(closeadj):
    base = (_f07_bandpos(closeadj, 252) >= 0.6667).astype(float).rolling(252, min_periods=max(1,252//2)).mean()
    feat = base - base.rolling(max(5, 21), min_periods=max(1, 21//2)).mean()
    slope = feat.diff(21) / float(21)
    deriv = slope.diff(21) / float(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_uppshare420d_420d_jerk_v039_signal(closeadj):
    base = (_f07_bandpos(closeadj, 420) >= 0.6667).astype(float).rolling(420, min_periods=max(1,420//2)).mean()
    feat = _z(base, max(10, 35*2))
    slope = feat.diff(35) / float(35)
    deriv = slope.diff(35) / float(35)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_uppshare1134d_1134d_jerk_v040_signal(closeadj):
    base = (_f07_bandpos(closeadj, 1134) >= 0.6667).astype(float).rolling(1134, min_periods=max(1,1134//2)).mean()
    feat = base
    slope = feat.diff(94) / float(94)
    deriv = slope.diff(94) / float(94)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_midskew168d_168d_jerk_v041_signal(closeadj):
    base = ((_f07_bandpos(closeadj, 168) - 0.5))
    feat = _z(base, max(10, 14*2))
    slope = feat.diff(14) / float(14)
    deriv = slope.diff(14) / float(14)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_midskew315d_315d_jerk_v042_signal(closeadj):
    base = ((_f07_bandpos(closeadj, 315) - 0.5))
    feat = base
    slope = feat.diff(26) / float(26)
    deriv = slope.diff(26) / float(26)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_midskew630d_630d_jerk_v043_signal(closeadj):
    base = ((_f07_bandpos(closeadj, 630) - 0.5))
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 52), min_periods=max(1, 52//2)).median()))
    slope = feat.diff(52) / float(52)
    deriv = slope.diff(52) / float(52)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaphi84d_84d_jerk_v044_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 84)
    feat = base
    slope = feat.diff(7) / float(7)
    deriv = slope.diff(7) / float(7)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaphi231d_231d_jerk_v045_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 231)
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 19), min_periods=max(1, 19//2)).median()))
    slope = feat.diff(19) / float(19)
    deriv = slope.diff(19) / float(19)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaphi378d_378d_jerk_v046_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 378)
    feat = base.ewm(span=max(5, 31), min_periods=max(3, 31//2)).mean()
    slope = feat.diff(31) / float(31)
    deriv = slope.diff(31) / float(31)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaphi1008d_1008d_jerk_v047_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 1008)
    feat = base - base.rolling(max(5, 84), min_periods=max(1, 84//2)).mean()
    slope = feat.diff(84) / float(84)
    deriv = slope.diff(84) / float(84)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaplo147d_147d_jerk_v048_signal(closeadj):
    base = _f07_anchor_gap_lo(closeadj, 147)
    feat = base.ewm(span=max(5, 12), min_periods=max(3, 12//2)).mean()
    slope = feat.diff(12) / float(12)
    deriv = slope.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaplo294d_294d_jerk_v049_signal(closeadj):
    base = _f07_anchor_gap_lo(closeadj, 294)
    feat = base - base.rolling(max(5, 24), min_periods=max(1, 24//2)).mean()
    slope = feat.diff(24) / float(24)
    deriv = slope.diff(24) / float(24)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaplo504d_504d_jerk_v050_signal(closeadj):
    base = _f07_anchor_gap_lo(closeadj, 504)
    feat = _z(base, max(10, 42*2))
    slope = feat.diff(42) / float(42)
    deriv = slope.diff(42) / float(42)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_bandpos63d_63d_jerk_v051_signal(closeadj):
    base = _f07_bandpos(closeadj, 63)
    feat = base - base.rolling(max(5, 5), min_periods=max(1, 5//2)).mean()
    slope = feat.diff(5) / float(5)
    deriv = slope.diff(5) / float(5)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_bandpos210d_210d_jerk_v052_signal(closeadj):
    base = _f07_bandpos(closeadj, 210)
    feat = _z(base, max(10, 17*2))
    slope = feat.diff(17) / float(17)
    deriv = slope.diff(17) / float(17)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_bandpos357d_357d_jerk_v053_signal(closeadj):
    base = _f07_bandpos(closeadj, 357)
    feat = base
    slope = feat.diff(29) / float(29)
    deriv = slope.diff(29) / float(29)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_bandpos882d_882d_jerk_v054_signal(closeadj):
    base = _f07_bandpos(closeadj, 882)
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 73), min_periods=max(1, 73//2)).median()))
    slope = feat.diff(73) / float(73)
    deriv = slope.diff(73) / float(73)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_span126d_126d_jerk_v055_signal(closeadj):
    base = _f07_span(closeadj, 126)
    feat = base
    slope = feat.diff(10) / float(10)
    deriv = slope.diff(10) / float(10)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_span273d_273d_jerk_v056_signal(closeadj):
    base = _f07_span(closeadj, 273)
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 22), min_periods=max(1, 22//2)).median()))
    slope = feat.diff(22) / float(22)
    deriv = slope.diff(22) / float(22)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_span462d_462d_jerk_v057_signal(closeadj):
    base = _f07_span(closeadj, 462)
    feat = base.ewm(span=max(5, 38), min_periods=max(3, 38//2)).mean()
    slope = feat.diff(38) / float(38)
    deriv = slope.diff(38) / float(38)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_span1260d_1260d_jerk_v058_signal(closeadj):
    base = _f07_span(closeadj, 1260)
    feat = base - base.rolling(max(5, 105), min_periods=max(1, 105//2)).mean()
    slope = feat.diff(105) / float(105)
    deriv = slope.diff(105) / float(105)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapresid189d_189d_jerk_v059_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, min(252, 189)) - _f07_anchor_gap_hi(closeadj, max(504, 189)))
    feat = base.ewm(span=max(5, 15), min_periods=max(3, 15//2)).mean()
    slope = feat.diff(15) / float(15)
    deriv = slope.diff(15) / float(15)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loresid126d_126d_jerk_v060_signal(closeadj):
    base = (_f07_anchor_gap_lo(closeadj, min(252, 126)) - _f07_anchor_gap_lo(closeadj, max(504, 126)))
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 10), min_periods=max(1, 10//2)).median()))
    slope = feat.diff(10) / float(10)
    deriv = slope.diff(10) / float(10)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_nhfreq63d_63d_jerk_v061_signal(closeadj):
    base = (_f07_freq(_f07_newhigh_flag(closeadj, min(252, 63)), max(21, min(252, 63)//4)) + 0.5 * _f07_anchor_gap_hi(closeadj, min(252, 63)))
    feat = base
    slope = feat.diff(5) / float(5)
    deriv = slope.diff(5) / float(5)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_nhfreq210d_210d_jerk_v062_signal(closeadj):
    base = (_f07_freq(_f07_newhigh_flag(closeadj, min(252, 210)), max(21, min(252, 210)//4)) + 0.5 * _f07_anchor_gap_hi(closeadj, min(252, 210)))
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 17), min_periods=max(1, 17//2)).median()))
    slope = feat.diff(17) / float(17)
    deriv = slope.diff(17) / float(17)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_nlfreq147d_147d_jerk_v063_signal(closeadj):
    base = (_f07_freq(_f07_newlow_flag(closeadj, min(252, 147)), max(21, min(252, 147)//4)) - 0.5 * _f07_anchor_gap_lo(closeadj, min(252, 147)))
    feat = base
    slope = feat.diff(12) / float(12)
    deriv = slope.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_anchdist84d_84d_jerk_v064_signal(closeadj):
    base = _f07_anchor_dist(closeadj, min(252, 84), max(504, 84))
    feat = _z(base, max(10, 7*2))
    slope = feat.diff(7) / float(7)
    deriv = slope.diff(7) / float(7)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_anchdist231d_231d_jerk_v065_signal(closeadj):
    base = _f07_anchor_dist(closeadj, min(252, 231), max(504, 231))
    feat = base
    slope = feat.diff(19) / float(19)
    deriv = slope.diff(19) / float(19)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_hiext168d_168d_jerk_v066_signal(closeadj):
    base = ((_rmax(closeadj, 168) - _mean(closeadj, 168)) / _mean(closeadj, 168).replace(0, np.nan))
    feat = _z(base, max(10, 14*2))
    slope = feat.diff(14) / float(14)
    deriv = slope.diff(14) / float(14)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_hiext315d_315d_jerk_v067_signal(closeadj):
    base = ((_rmax(closeadj, 315) - _mean(closeadj, 315)) / _mean(closeadj, 315).replace(0, np.nan))
    feat = base
    slope = feat.diff(26) / float(26)
    deriv = slope.diff(26) / float(26)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_hiext630d_630d_jerk_v068_signal(closeadj):
    base = ((_rmax(closeadj, 630) - _mean(closeadj, 630)) / _mean(closeadj, 630).replace(0, np.nan))
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 52), min_periods=max(1, 52//2)).median()))
    slope = feat.diff(52) / float(52)
    deriv = slope.diff(52) / float(52)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loext84d_84d_jerk_v069_signal(closeadj):
    base = ((_mean(closeadj, 84) - _rmin(closeadj, 84)) / _mean(closeadj, 84).replace(0, np.nan))
    feat = base
    slope = feat.diff(7) / float(7)
    deriv = slope.diff(7) / float(7)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loext231d_231d_jerk_v070_signal(closeadj):
    base = ((_mean(closeadj, 231) - _rmin(closeadj, 231)) / _mean(closeadj, 231).replace(0, np.nan))
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 19), min_periods=max(1, 19//2)).median()))
    slope = feat.diff(19) / float(19)
    deriv = slope.diff(19) / float(19)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loext378d_378d_jerk_v071_signal(closeadj):
    base = ((_mean(closeadj, 378) - _rmin(closeadj, 378)) / _mean(closeadj, 378).replace(0, np.nan))
    feat = base.ewm(span=max(5, 31), min_periods=max(3, 31//2)).mean()
    slope = feat.diff(31) / float(31)
    deriv = slope.diff(31) / float(31)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loext1008d_1008d_jerk_v072_signal(closeadj):
    base = ((_mean(closeadj, 1008) - _rmin(closeadj, 1008)) / _mean(closeadj, 1008).replace(0, np.nan))
    feat = base - base.rolling(max(5, 84), min_periods=max(1, 84//2)).mean()
    slope = feat.diff(84) / float(84)
    deriv = slope.diff(84) / float(84)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_posroam147d_147d_jerk_v073_signal(closeadj):
    base = _f07_bandpos(closeadj, 147).rolling(max(21, 147//4), min_periods=max(1, 147//8)).std()
    feat = base.ewm(span=max(5, 12), min_periods=max(3, 12//2)).mean()
    slope = feat.diff(12) / float(12)
    deriv = slope.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_posroam294d_294d_jerk_v074_signal(closeadj):
    base = _f07_bandpos(closeadj, 294).rolling(max(21, 294//4), min_periods=max(1, 294//8)).std()
    feat = base - base.rolling(max(5, 24), min_periods=max(1, 24//2)).mean()
    slope = feat.diff(24) / float(24)
    deriv = slope.diff(24) / float(24)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_posroam504d_504d_jerk_v075_signal(closeadj):
    base = _f07_bandpos(closeadj, 504).rolling(max(21, 504//4), min_periods=max(1, 504//8)).std()
    feat = _z(base, max(10, 42*2))
    slope = feat.diff(42) / float(42)
    deriv = slope.diff(42) / float(42)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapz63d_63d_jerk_v076_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, 63) - _f07_anchor_gap_hi(closeadj, 63).ewm(span=max(10,63//6), min_periods=max(5,63//12)).mean())
    feat = base - base.rolling(max(5, 5), min_periods=max(1, 5//2)).mean()
    slope = feat.diff(5) / float(5)
    deriv = slope.diff(5) / float(5)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapz210d_210d_jerk_v077_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, 210) - _f07_anchor_gap_hi(closeadj, 210).ewm(span=max(10,210//6), min_periods=max(5,210//12)).mean())
    feat = _z(base, max(10, 17*2))
    slope = feat.diff(17) / float(17)
    deriv = slope.diff(17) / float(17)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapz357d_357d_jerk_v078_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, 357) - _f07_anchor_gap_hi(closeadj, 357).ewm(span=max(10,357//6), min_periods=max(5,357//12)).mean())
    feat = base
    slope = feat.diff(29) / float(29)
    deriv = slope.diff(29) / float(29)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapz882d_882d_jerk_v079_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, 882) - _f07_anchor_gap_hi(closeadj, 882).ewm(span=max(10,882//6), min_periods=max(5,882//12)).mean())
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 73), min_periods=max(1, 73//2)).median()))
    slope = feat.diff(73) / float(73)
    deriv = slope.diff(73) / float(73)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_uppshare126d_126d_jerk_v080_signal(closeadj):
    base = (_f07_bandpos(closeadj, 126) >= 0.6667).astype(float).rolling(126, min_periods=max(1,126//2)).mean()
    feat = base
    slope = feat.diff(10) / float(10)
    deriv = slope.diff(10) / float(10)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_uppshare273d_273d_jerk_v081_signal(closeadj):
    base = (_f07_bandpos(closeadj, 273) >= 0.6667).astype(float).rolling(273, min_periods=max(1,273//2)).mean()
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 22), min_periods=max(1, 22//2)).median()))
    slope = feat.diff(22) / float(22)
    deriv = slope.diff(22) / float(22)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_uppshare462d_462d_jerk_v082_signal(closeadj):
    base = (_f07_bandpos(closeadj, 462) >= 0.6667).astype(float).rolling(462, min_periods=max(1,462//2)).mean()
    feat = base.ewm(span=max(5, 38), min_periods=max(3, 38//2)).mean()
    slope = feat.diff(38) / float(38)
    deriv = slope.diff(38) / float(38)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_uppshare1260d_1260d_jerk_v083_signal(closeadj):
    base = (_f07_bandpos(closeadj, 1260) >= 0.6667).astype(float).rolling(1260, min_periods=max(1,1260//2)).mean()
    feat = base - base.rolling(max(5, 105), min_periods=max(1, 105//2)).mean()
    slope = feat.diff(105) / float(105)
    deriv = slope.diff(105) / float(105)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_midskew189d_189d_jerk_v084_signal(closeadj):
    base = ((_f07_bandpos(closeadj, 189) - 0.5))
    feat = base.ewm(span=max(5, 15), min_periods=max(3, 15//2)).mean()
    slope = feat.diff(15) / float(15)
    deriv = slope.diff(15) / float(15)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_midskew336d_336d_jerk_v085_signal(closeadj):
    base = ((_f07_bandpos(closeadj, 336) - 0.5))
    feat = base - base.rolling(max(5, 28), min_periods=max(1, 28//2)).mean()
    slope = feat.diff(28) / float(28)
    deriv = slope.diff(28) / float(28)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_midskew756d_756d_jerk_v086_signal(closeadj):
    base = ((_f07_bandpos(closeadj, 756) - 0.5))
    feat = _z(base, max(10, 63*2))
    slope = feat.diff(63) / float(63)
    deriv = slope.diff(63) / float(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaphi105d_105d_jerk_v087_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 105)
    feat = base - base.rolling(max(5, 8), min_periods=max(1, 8//2)).mean()
    slope = feat.diff(8) / float(8)
    deriv = slope.diff(8) / float(8)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaphi252d_252d_jerk_v088_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 252)
    feat = _z(base, max(10, 21*2))
    slope = feat.diff(21) / float(21)
    deriv = slope.diff(21) / float(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaphi420d_420d_jerk_v089_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 420)
    feat = base
    slope = feat.diff(35) / float(35)
    deriv = slope.diff(35) / float(35)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaphi1134d_1134d_jerk_v090_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 1134)
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 94), min_periods=max(1, 94//2)).median()))
    slope = feat.diff(94) / float(94)
    deriv = slope.diff(94) / float(94)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaplo168d_168d_jerk_v091_signal(closeadj):
    base = _f07_anchor_gap_lo(closeadj, 168)
    feat = base
    slope = feat.diff(14) / float(14)
    deriv = slope.diff(14) / float(14)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaplo315d_315d_jerk_v092_signal(closeadj):
    base = _f07_anchor_gap_lo(closeadj, 315)
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 26), min_periods=max(1, 26//2)).median()))
    slope = feat.diff(26) / float(26)
    deriv = slope.diff(26) / float(26)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaplo630d_630d_jerk_v093_signal(closeadj):
    base = _f07_anchor_gap_lo(closeadj, 630)
    feat = base.ewm(span=max(5, 52), min_periods=max(3, 52//2)).mean()
    slope = feat.diff(52) / float(52)
    deriv = slope.diff(52) / float(52)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_bandpos84d_84d_jerk_v094_signal(closeadj):
    base = _f07_bandpos(closeadj, 84)
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 7), min_periods=max(1, 7//2)).median()))
    slope = feat.diff(7) / float(7)
    deriv = slope.diff(7) / float(7)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_bandpos231d_231d_jerk_v095_signal(closeadj):
    base = _f07_bandpos(closeadj, 231)
    feat = base.ewm(span=max(5, 19), min_periods=max(3, 19//2)).mean()
    slope = feat.diff(19) / float(19)
    deriv = slope.diff(19) / float(19)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_bandpos378d_378d_jerk_v096_signal(closeadj):
    base = _f07_bandpos(closeadj, 378)
    feat = base - base.rolling(max(5, 31), min_periods=max(1, 31//2)).mean()
    slope = feat.diff(31) / float(31)
    deriv = slope.diff(31) / float(31)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_bandpos1008d_1008d_jerk_v097_signal(closeadj):
    base = _f07_bandpos(closeadj, 1008)
    feat = _z(base, max(10, 84*2))
    slope = feat.diff(84) / float(84)
    deriv = slope.diff(84) / float(84)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_span147d_147d_jerk_v098_signal(closeadj):
    base = _f07_span(closeadj, 147)
    feat = base - base.rolling(max(5, 12), min_periods=max(1, 12//2)).mean()
    slope = feat.diff(12) / float(12)
    deriv = slope.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_span294d_294d_jerk_v099_signal(closeadj):
    base = _f07_span(closeadj, 294)
    feat = _z(base, max(10, 24*2))
    slope = feat.diff(24) / float(24)
    deriv = slope.diff(24) / float(24)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_span504d_504d_jerk_v100_signal(closeadj):
    base = _f07_span(closeadj, 504)
    feat = base
    slope = feat.diff(42) / float(42)
    deriv = slope.diff(42) / float(42)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapresid63d_63d_jerk_v101_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, min(252, 63)) - _f07_anchor_gap_hi(closeadj, max(504, 63)))
    feat = _z(base, max(10, 5*2))
    slope = feat.diff(5) / float(5)
    deriv = slope.diff(5) / float(5)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapresid210d_210d_jerk_v102_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, min(252, 210)) - _f07_anchor_gap_hi(closeadj, max(504, 210)))
    feat = base
    slope = feat.diff(17) / float(17)
    deriv = slope.diff(17) / float(17)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loresid147d_147d_jerk_v103_signal(closeadj):
    base = (_f07_anchor_gap_lo(closeadj, min(252, 147)) - _f07_anchor_gap_lo(closeadj, max(504, 147)))
    feat = _z(base, max(10, 12*2))
    slope = feat.diff(12) / float(12)
    deriv = slope.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_nhfreq84d_84d_jerk_v104_signal(closeadj):
    base = (_f07_freq(_f07_newhigh_flag(closeadj, min(252, 84)), max(21, min(252, 84)//4)) + 0.5 * _f07_anchor_gap_hi(closeadj, min(252, 84)))
    feat = base - base.rolling(max(5, 7), min_periods=max(1, 7//2)).mean()
    slope = feat.diff(7) / float(7)
    deriv = slope.diff(7) / float(7)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_nhfreq231d_231d_jerk_v105_signal(closeadj):
    base = (_f07_freq(_f07_newhigh_flag(closeadj, min(252, 231)), max(21, min(252, 231)//4)) + 0.5 * _f07_anchor_gap_hi(closeadj, min(252, 231)))
    feat = _z(base, max(10, 19*2))
    slope = feat.diff(19) / float(19)
    deriv = slope.diff(19) / float(19)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_nlfreq168d_168d_jerk_v106_signal(closeadj):
    base = (_f07_freq(_f07_newlow_flag(closeadj, min(252, 168)), max(21, min(252, 168)//4)) - 0.5 * _f07_anchor_gap_lo(closeadj, min(252, 168)))
    feat = base - base.rolling(max(5, 14), min_periods=max(1, 14//2)).mean()
    slope = feat.diff(14) / float(14)
    deriv = slope.diff(14) / float(14)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_anchdist105d_105d_jerk_v107_signal(closeadj):
    base = _f07_anchor_dist(closeadj, min(252, 105), max(504, 105))
    feat = base.ewm(span=max(5, 8), min_periods=max(3, 8//2)).mean()
    slope = feat.diff(8) / float(8)
    deriv = slope.diff(8) / float(8)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_anchdist252d_252d_jerk_v108_signal(closeadj):
    base = _f07_anchor_dist(closeadj, min(252, 252), max(504, 252))
    feat = base - base.rolling(max(5, 21), min_periods=max(1, 21//2)).mean()
    slope = feat.diff(21) / float(21)
    deriv = slope.diff(21) / float(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_hiext189d_189d_jerk_v109_signal(closeadj):
    base = ((_rmax(closeadj, 189) - _mean(closeadj, 189)) / _mean(closeadj, 189).replace(0, np.nan))
    feat = base.ewm(span=max(5, 15), min_periods=max(3, 15//2)).mean()
    slope = feat.diff(15) / float(15)
    deriv = slope.diff(15) / float(15)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_hiext336d_336d_jerk_v110_signal(closeadj):
    base = ((_rmax(closeadj, 336) - _mean(closeadj, 336)) / _mean(closeadj, 336).replace(0, np.nan))
    feat = base - base.rolling(max(5, 28), min_periods=max(1, 28//2)).mean()
    slope = feat.diff(28) / float(28)
    deriv = slope.diff(28) / float(28)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_hiext756d_756d_jerk_v111_signal(closeadj):
    base = ((_rmax(closeadj, 756) - _mean(closeadj, 756)) / _mean(closeadj, 756).replace(0, np.nan))
    feat = _z(base, max(10, 63*2))
    slope = feat.diff(63) / float(63)
    deriv = slope.diff(63) / float(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loext105d_105d_jerk_v112_signal(closeadj):
    base = ((_mean(closeadj, 105) - _rmin(closeadj, 105)) / _mean(closeadj, 105).replace(0, np.nan))
    feat = base - base.rolling(max(5, 8), min_periods=max(1, 8//2)).mean()
    slope = feat.diff(8) / float(8)
    deriv = slope.diff(8) / float(8)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loext252d_252d_jerk_v113_signal(closeadj):
    base = ((_mean(closeadj, 252) - _rmin(closeadj, 252)) / _mean(closeadj, 252).replace(0, np.nan))
    feat = _z(base, max(10, 21*2))
    slope = feat.diff(21) / float(21)
    deriv = slope.diff(21) / float(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loext420d_420d_jerk_v114_signal(closeadj):
    base = ((_mean(closeadj, 420) - _rmin(closeadj, 420)) / _mean(closeadj, 420).replace(0, np.nan))
    feat = base
    slope = feat.diff(35) / float(35)
    deriv = slope.diff(35) / float(35)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loext1134d_1134d_jerk_v115_signal(closeadj):
    base = ((_mean(closeadj, 1134) - _rmin(closeadj, 1134)) / _mean(closeadj, 1134).replace(0, np.nan))
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 94), min_periods=max(1, 94//2)).median()))
    slope = feat.diff(94) / float(94)
    deriv = slope.diff(94) / float(94)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_posroam168d_168d_jerk_v116_signal(closeadj):
    base = _f07_bandpos(closeadj, 168).rolling(max(21, 168//4), min_periods=max(1, 168//8)).std()
    feat = base
    slope = feat.diff(14) / float(14)
    deriv = slope.diff(14) / float(14)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_posroam315d_315d_jerk_v117_signal(closeadj):
    base = _f07_bandpos(closeadj, 315).rolling(max(21, 315//4), min_periods=max(1, 315//8)).std()
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 26), min_periods=max(1, 26//2)).median()))
    slope = feat.diff(26) / float(26)
    deriv = slope.diff(26) / float(26)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_posroam630d_630d_jerk_v118_signal(closeadj):
    base = _f07_bandpos(closeadj, 630).rolling(max(21, 630//4), min_periods=max(1, 630//8)).std()
    feat = base.ewm(span=max(5, 52), min_periods=max(3, 52//2)).mean()
    slope = feat.diff(52) / float(52)
    deriv = slope.diff(52) / float(52)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapz84d_84d_jerk_v119_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, 84) - _f07_anchor_gap_hi(closeadj, 84).ewm(span=max(10,84//6), min_periods=max(5,84//12)).mean())
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 7), min_periods=max(1, 7//2)).median()))
    slope = feat.diff(7) / float(7)
    deriv = slope.diff(7) / float(7)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapz231d_231d_jerk_v120_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, 231) - _f07_anchor_gap_hi(closeadj, 231).ewm(span=max(10,231//6), min_periods=max(5,231//12)).mean())
    feat = base.ewm(span=max(5, 19), min_periods=max(3, 19//2)).mean()
    slope = feat.diff(19) / float(19)
    deriv = slope.diff(19) / float(19)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapz378d_378d_jerk_v121_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, 378) - _f07_anchor_gap_hi(closeadj, 378).ewm(span=max(10,378//6), min_periods=max(5,378//12)).mean())
    feat = base - base.rolling(max(5, 31), min_periods=max(1, 31//2)).mean()
    slope = feat.diff(31) / float(31)
    deriv = slope.diff(31) / float(31)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapz1008d_1008d_jerk_v122_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, 1008) - _f07_anchor_gap_hi(closeadj, 1008).ewm(span=max(10,1008//6), min_periods=max(5,1008//12)).mean())
    feat = _z(base, max(10, 84*2))
    slope = feat.diff(84) / float(84)
    deriv = slope.diff(84) / float(84)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_uppshare147d_147d_jerk_v123_signal(closeadj):
    base = (_f07_bandpos(closeadj, 147) >= 0.6667).astype(float).rolling(147, min_periods=max(1,147//2)).mean()
    feat = base - base.rolling(max(5, 12), min_periods=max(1, 12//2)).mean()
    slope = feat.diff(12) / float(12)
    deriv = slope.diff(12) / float(12)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_uppshare294d_294d_jerk_v124_signal(closeadj):
    base = (_f07_bandpos(closeadj, 294) >= 0.6667).astype(float).rolling(294, min_periods=max(1,294//2)).mean()
    feat = _z(base, max(10, 24*2))
    slope = feat.diff(24) / float(24)
    deriv = slope.diff(24) / float(24)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_uppshare504d_504d_jerk_v125_signal(closeadj):
    base = (_f07_bandpos(closeadj, 504) >= 0.6667).astype(float).rolling(504, min_periods=max(1,504//2)).mean()
    feat = base
    slope = feat.diff(42) / float(42)
    deriv = slope.diff(42) / float(42)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_midskew63d_63d_jerk_v126_signal(closeadj):
    base = ((_f07_bandpos(closeadj, 63) - 0.5))
    feat = _z(base, max(10, 5*2))
    slope = feat.diff(5) / float(5)
    deriv = slope.diff(5) / float(5)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_midskew210d_210d_jerk_v127_signal(closeadj):
    base = ((_f07_bandpos(closeadj, 210) - 0.5))
    feat = base
    slope = feat.diff(17) / float(17)
    deriv = slope.diff(17) / float(17)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_midskew357d_357d_jerk_v128_signal(closeadj):
    base = ((_f07_bandpos(closeadj, 357) - 0.5))
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 29), min_periods=max(1, 29//2)).median()))
    slope = feat.diff(29) / float(29)
    deriv = slope.diff(29) / float(29)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_midskew882d_882d_jerk_v129_signal(closeadj):
    base = ((_f07_bandpos(closeadj, 882) - 0.5))
    feat = base.ewm(span=max(5, 73), min_periods=max(3, 73//2)).mean()
    slope = feat.diff(73) / float(73)
    deriv = slope.diff(73) / float(73)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaphi126d_126d_jerk_v130_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 126)
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 10), min_periods=max(1, 10//2)).median()))
    slope = feat.diff(10) / float(10)
    deriv = slope.diff(10) / float(10)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaphi273d_273d_jerk_v131_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 273)
    feat = base.ewm(span=max(5, 22), min_periods=max(3, 22//2)).mean()
    slope = feat.diff(22) / float(22)
    deriv = slope.diff(22) / float(22)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaphi462d_462d_jerk_v132_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 462)
    feat = base - base.rolling(max(5, 38), min_periods=max(1, 38//2)).mean()
    slope = feat.diff(38) / float(38)
    deriv = slope.diff(38) / float(38)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaphi1260d_1260d_jerk_v133_signal(closeadj):
    base = _f07_anchor_gap_hi(closeadj, 1260)
    feat = _z(base, max(10, 105*2))
    slope = feat.diff(105) / float(105)
    deriv = slope.diff(105) / float(105)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaplo189d_189d_jerk_v134_signal(closeadj):
    base = _f07_anchor_gap_lo(closeadj, 189)
    feat = base - base.rolling(max(5, 15), min_periods=max(1, 15//2)).mean()
    slope = feat.diff(15) / float(15)
    deriv = slope.diff(15) / float(15)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaplo336d_336d_jerk_v135_signal(closeadj):
    base = _f07_anchor_gap_lo(closeadj, 336)
    feat = _z(base, max(10, 28*2))
    slope = feat.diff(28) / float(28)
    deriv = slope.diff(28) / float(28)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gaplo756d_756d_jerk_v136_signal(closeadj):
    base = _f07_anchor_gap_lo(closeadj, 756)
    feat = base
    slope = feat.diff(63) / float(63)
    deriv = slope.diff(63) / float(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_bandpos105d_105d_jerk_v137_signal(closeadj):
    base = _f07_bandpos(closeadj, 105)
    feat = _z(base, max(10, 8*2))
    slope = feat.diff(8) / float(8)
    deriv = slope.diff(8) / float(8)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_bandpos252d_252d_jerk_v138_signal(closeadj):
    base = _f07_bandpos(closeadj, 252)
    feat = base
    slope = feat.diff(21) / float(21)
    deriv = slope.diff(21) / float(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_bandpos420d_420d_jerk_v139_signal(closeadj):
    base = _f07_bandpos(closeadj, 420)
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 35), min_periods=max(1, 35//2)).median()))
    slope = feat.diff(35) / float(35)
    deriv = slope.diff(35) / float(35)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_bandpos1134d_1134d_jerk_v140_signal(closeadj):
    base = _f07_bandpos(closeadj, 1134)
    feat = base.ewm(span=max(5, 94), min_periods=max(3, 94//2)).mean()
    slope = feat.diff(94) / float(94)
    deriv = slope.diff(94) / float(94)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_span168d_168d_jerk_v141_signal(closeadj):
    base = _f07_span(closeadj, 168)
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 14), min_periods=max(1, 14//2)).median()))
    slope = feat.diff(14) / float(14)
    deriv = slope.diff(14) / float(14)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_span315d_315d_jerk_v142_signal(closeadj):
    base = _f07_span(closeadj, 315)
    feat = base.ewm(span=max(5, 26), min_periods=max(3, 26//2)).mean()
    slope = feat.diff(26) / float(26)
    deriv = slope.diff(26) / float(26)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_span630d_630d_jerk_v143_signal(closeadj):
    base = _f07_span(closeadj, 630)
    feat = base - base.rolling(max(5, 52), min_periods=max(1, 52//2)).mean()
    slope = feat.diff(52) / float(52)
    deriv = slope.diff(52) / float(52)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapresid84d_84d_jerk_v144_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, min(252, 84)) - _f07_anchor_gap_hi(closeadj, max(504, 84)))
    feat = base.ewm(span=max(5, 7), min_periods=max(3, 7//2)).mean()
    slope = feat.diff(7) / float(7)
    deriv = slope.diff(7) / float(7)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_gapresid231d_231d_jerk_v145_signal(closeadj):
    base = (_f07_anchor_gap_hi(closeadj, min(252, 231)) - _f07_anchor_gap_hi(closeadj, max(504, 231)))
    feat = base - base.rolling(max(5, 19), min_periods=max(1, 19//2)).mean()
    slope = feat.diff(19) / float(19)
    deriv = slope.diff(19) / float(19)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_loresid168d_168d_jerk_v146_signal(closeadj):
    base = (_f07_anchor_gap_lo(closeadj, min(252, 168)) - _f07_anchor_gap_lo(closeadj, max(504, 168)))
    feat = base.ewm(span=max(5, 14), min_periods=max(3, 14//2)).mean()
    slope = feat.diff(14) / float(14)
    deriv = slope.diff(14) / float(14)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_nhfreq105d_105d_jerk_v147_signal(closeadj):
    base = (_f07_freq(_f07_newhigh_flag(closeadj, min(252, 105)), max(21, min(252, 105)//4)) + 0.5 * _f07_anchor_gap_hi(closeadj, min(252, 105)))
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 8), min_periods=max(1, 8//2)).median()))
    slope = feat.diff(8) / float(8)
    deriv = slope.diff(8) / float(8)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_nhfreq252d_252d_jerk_v148_signal(closeadj):
    base = (_f07_freq(_f07_newhigh_flag(closeadj, min(252, 252)), max(21, min(252, 252)//4)) + 0.5 * _f07_anchor_gap_hi(closeadj, min(252, 252)))
    feat = base.ewm(span=max(5, 21), min_periods=max(3, 21//2)).mean()
    slope = feat.diff(21) / float(21)
    deriv = slope.diff(21) / float(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_nlfreq189d_189d_jerk_v149_signal(closeadj):
    base = (_f07_freq(_f07_newlow_flag(closeadj, min(252, 189)), max(21, min(252, 189)//4)) - 0.5 * _f07_anchor_gap_lo(closeadj, min(252, 189)))
    feat = np.tanh(3.0 * (base - base.rolling(max(5, 15), min_periods=max(1, 15//2)).median()))
    slope = feat.diff(15) / float(15)
    deriv = slope.diff(15) / float(15)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f07fw_f07_fiftytwo_week_position_anchdist126d_126d_jerk_v150_signal(closeadj):
    base = _f07_anchor_dist(closeadj, min(252, 126), max(504, 126))
    feat = base
    slope = feat.diff(10) / float(10)
    deriv = slope.diff(10) / float(10)
    return deriv.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f07fw_f07_fiftytwo_week_position_gaphi63d_63d_jerk_v001_signal,
    f07fw_f07_fiftytwo_week_position_gaphi210d_210d_jerk_v002_signal,
    f07fw_f07_fiftytwo_week_position_gaphi357d_357d_jerk_v003_signal,
    f07fw_f07_fiftytwo_week_position_gaphi882d_882d_jerk_v004_signal,
    f07fw_f07_fiftytwo_week_position_gaplo126d_126d_jerk_v005_signal,
    f07fw_f07_fiftytwo_week_position_gaplo273d_273d_jerk_v006_signal,
    f07fw_f07_fiftytwo_week_position_gaplo462d_462d_jerk_v007_signal,
    f07fw_f07_fiftytwo_week_position_gaplo1260d_1260d_jerk_v008_signal,
    f07fw_f07_fiftytwo_week_position_bandpos189d_189d_jerk_v009_signal,
    f07fw_f07_fiftytwo_week_position_bandpos336d_336d_jerk_v010_signal,
    f07fw_f07_fiftytwo_week_position_bandpos756d_756d_jerk_v011_signal,
    f07fw_f07_fiftytwo_week_position_span105d_105d_jerk_v012_signal,
    f07fw_f07_fiftytwo_week_position_span252d_252d_jerk_v013_signal,
    f07fw_f07_fiftytwo_week_position_span420d_420d_jerk_v014_signal,
    f07fw_f07_fiftytwo_week_position_span1134d_1134d_jerk_v015_signal,
    f07fw_f07_fiftytwo_week_position_gapresid168d_168d_jerk_v016_signal,
    f07fw_f07_fiftytwo_week_position_loresid105d_105d_jerk_v017_signal,
    f07fw_f07_fiftytwo_week_position_loresid252d_252d_jerk_v018_signal,
    f07fw_f07_fiftytwo_week_position_nhfreq189d_189d_jerk_v019_signal,
    f07fw_f07_fiftytwo_week_position_nlfreq126d_126d_jerk_v020_signal,
    f07fw_f07_fiftytwo_week_position_anchdist63d_63d_jerk_v021_signal,
    f07fw_f07_fiftytwo_week_position_anchdist210d_210d_jerk_v022_signal,
    f07fw_f07_fiftytwo_week_position_hiext147d_147d_jerk_v023_signal,
    f07fw_f07_fiftytwo_week_position_hiext294d_294d_jerk_v024_signal,
    f07fw_f07_fiftytwo_week_position_hiext504d_504d_jerk_v025_signal,
    f07fw_f07_fiftytwo_week_position_loext63d_63d_jerk_v026_signal,
    f07fw_f07_fiftytwo_week_position_loext210d_210d_jerk_v027_signal,
    f07fw_f07_fiftytwo_week_position_loext357d_357d_jerk_v028_signal,
    f07fw_f07_fiftytwo_week_position_loext882d_882d_jerk_v029_signal,
    f07fw_f07_fiftytwo_week_position_posroam126d_126d_jerk_v030_signal,
    f07fw_f07_fiftytwo_week_position_posroam273d_273d_jerk_v031_signal,
    f07fw_f07_fiftytwo_week_position_posroam462d_462d_jerk_v032_signal,
    f07fw_f07_fiftytwo_week_position_posroam1260d_1260d_jerk_v033_signal,
    f07fw_f07_fiftytwo_week_position_gapz189d_189d_jerk_v034_signal,
    f07fw_f07_fiftytwo_week_position_gapz336d_336d_jerk_v035_signal,
    f07fw_f07_fiftytwo_week_position_gapz756d_756d_jerk_v036_signal,
    f07fw_f07_fiftytwo_week_position_uppshare105d_105d_jerk_v037_signal,
    f07fw_f07_fiftytwo_week_position_uppshare252d_252d_jerk_v038_signal,
    f07fw_f07_fiftytwo_week_position_uppshare420d_420d_jerk_v039_signal,
    f07fw_f07_fiftytwo_week_position_uppshare1134d_1134d_jerk_v040_signal,
    f07fw_f07_fiftytwo_week_position_midskew168d_168d_jerk_v041_signal,
    f07fw_f07_fiftytwo_week_position_midskew315d_315d_jerk_v042_signal,
    f07fw_f07_fiftytwo_week_position_midskew630d_630d_jerk_v043_signal,
    f07fw_f07_fiftytwo_week_position_gaphi84d_84d_jerk_v044_signal,
    f07fw_f07_fiftytwo_week_position_gaphi231d_231d_jerk_v045_signal,
    f07fw_f07_fiftytwo_week_position_gaphi378d_378d_jerk_v046_signal,
    f07fw_f07_fiftytwo_week_position_gaphi1008d_1008d_jerk_v047_signal,
    f07fw_f07_fiftytwo_week_position_gaplo147d_147d_jerk_v048_signal,
    f07fw_f07_fiftytwo_week_position_gaplo294d_294d_jerk_v049_signal,
    f07fw_f07_fiftytwo_week_position_gaplo504d_504d_jerk_v050_signal,
    f07fw_f07_fiftytwo_week_position_bandpos63d_63d_jerk_v051_signal,
    f07fw_f07_fiftytwo_week_position_bandpos210d_210d_jerk_v052_signal,
    f07fw_f07_fiftytwo_week_position_bandpos357d_357d_jerk_v053_signal,
    f07fw_f07_fiftytwo_week_position_bandpos882d_882d_jerk_v054_signal,
    f07fw_f07_fiftytwo_week_position_span126d_126d_jerk_v055_signal,
    f07fw_f07_fiftytwo_week_position_span273d_273d_jerk_v056_signal,
    f07fw_f07_fiftytwo_week_position_span462d_462d_jerk_v057_signal,
    f07fw_f07_fiftytwo_week_position_span1260d_1260d_jerk_v058_signal,
    f07fw_f07_fiftytwo_week_position_gapresid189d_189d_jerk_v059_signal,
    f07fw_f07_fiftytwo_week_position_loresid126d_126d_jerk_v060_signal,
    f07fw_f07_fiftytwo_week_position_nhfreq63d_63d_jerk_v061_signal,
    f07fw_f07_fiftytwo_week_position_nhfreq210d_210d_jerk_v062_signal,
    f07fw_f07_fiftytwo_week_position_nlfreq147d_147d_jerk_v063_signal,
    f07fw_f07_fiftytwo_week_position_anchdist84d_84d_jerk_v064_signal,
    f07fw_f07_fiftytwo_week_position_anchdist231d_231d_jerk_v065_signal,
    f07fw_f07_fiftytwo_week_position_hiext168d_168d_jerk_v066_signal,
    f07fw_f07_fiftytwo_week_position_hiext315d_315d_jerk_v067_signal,
    f07fw_f07_fiftytwo_week_position_hiext630d_630d_jerk_v068_signal,
    f07fw_f07_fiftytwo_week_position_loext84d_84d_jerk_v069_signal,
    f07fw_f07_fiftytwo_week_position_loext231d_231d_jerk_v070_signal,
    f07fw_f07_fiftytwo_week_position_loext378d_378d_jerk_v071_signal,
    f07fw_f07_fiftytwo_week_position_loext1008d_1008d_jerk_v072_signal,
    f07fw_f07_fiftytwo_week_position_posroam147d_147d_jerk_v073_signal,
    f07fw_f07_fiftytwo_week_position_posroam294d_294d_jerk_v074_signal,
    f07fw_f07_fiftytwo_week_position_posroam504d_504d_jerk_v075_signal,
    f07fw_f07_fiftytwo_week_position_gapz63d_63d_jerk_v076_signal,
    f07fw_f07_fiftytwo_week_position_gapz210d_210d_jerk_v077_signal,
    f07fw_f07_fiftytwo_week_position_gapz357d_357d_jerk_v078_signal,
    f07fw_f07_fiftytwo_week_position_gapz882d_882d_jerk_v079_signal,
    f07fw_f07_fiftytwo_week_position_uppshare126d_126d_jerk_v080_signal,
    f07fw_f07_fiftytwo_week_position_uppshare273d_273d_jerk_v081_signal,
    f07fw_f07_fiftytwo_week_position_uppshare462d_462d_jerk_v082_signal,
    f07fw_f07_fiftytwo_week_position_uppshare1260d_1260d_jerk_v083_signal,
    f07fw_f07_fiftytwo_week_position_midskew189d_189d_jerk_v084_signal,
    f07fw_f07_fiftytwo_week_position_midskew336d_336d_jerk_v085_signal,
    f07fw_f07_fiftytwo_week_position_midskew756d_756d_jerk_v086_signal,
    f07fw_f07_fiftytwo_week_position_gaphi105d_105d_jerk_v087_signal,
    f07fw_f07_fiftytwo_week_position_gaphi252d_252d_jerk_v088_signal,
    f07fw_f07_fiftytwo_week_position_gaphi420d_420d_jerk_v089_signal,
    f07fw_f07_fiftytwo_week_position_gaphi1134d_1134d_jerk_v090_signal,
    f07fw_f07_fiftytwo_week_position_gaplo168d_168d_jerk_v091_signal,
    f07fw_f07_fiftytwo_week_position_gaplo315d_315d_jerk_v092_signal,
    f07fw_f07_fiftytwo_week_position_gaplo630d_630d_jerk_v093_signal,
    f07fw_f07_fiftytwo_week_position_bandpos84d_84d_jerk_v094_signal,
    f07fw_f07_fiftytwo_week_position_bandpos231d_231d_jerk_v095_signal,
    f07fw_f07_fiftytwo_week_position_bandpos378d_378d_jerk_v096_signal,
    f07fw_f07_fiftytwo_week_position_bandpos1008d_1008d_jerk_v097_signal,
    f07fw_f07_fiftytwo_week_position_span147d_147d_jerk_v098_signal,
    f07fw_f07_fiftytwo_week_position_span294d_294d_jerk_v099_signal,
    f07fw_f07_fiftytwo_week_position_span504d_504d_jerk_v100_signal,
    f07fw_f07_fiftytwo_week_position_gapresid63d_63d_jerk_v101_signal,
    f07fw_f07_fiftytwo_week_position_gapresid210d_210d_jerk_v102_signal,
    f07fw_f07_fiftytwo_week_position_loresid147d_147d_jerk_v103_signal,
    f07fw_f07_fiftytwo_week_position_nhfreq84d_84d_jerk_v104_signal,
    f07fw_f07_fiftytwo_week_position_nhfreq231d_231d_jerk_v105_signal,
    f07fw_f07_fiftytwo_week_position_nlfreq168d_168d_jerk_v106_signal,
    f07fw_f07_fiftytwo_week_position_anchdist105d_105d_jerk_v107_signal,
    f07fw_f07_fiftytwo_week_position_anchdist252d_252d_jerk_v108_signal,
    f07fw_f07_fiftytwo_week_position_hiext189d_189d_jerk_v109_signal,
    f07fw_f07_fiftytwo_week_position_hiext336d_336d_jerk_v110_signal,
    f07fw_f07_fiftytwo_week_position_hiext756d_756d_jerk_v111_signal,
    f07fw_f07_fiftytwo_week_position_loext105d_105d_jerk_v112_signal,
    f07fw_f07_fiftytwo_week_position_loext252d_252d_jerk_v113_signal,
    f07fw_f07_fiftytwo_week_position_loext420d_420d_jerk_v114_signal,
    f07fw_f07_fiftytwo_week_position_loext1134d_1134d_jerk_v115_signal,
    f07fw_f07_fiftytwo_week_position_posroam168d_168d_jerk_v116_signal,
    f07fw_f07_fiftytwo_week_position_posroam315d_315d_jerk_v117_signal,
    f07fw_f07_fiftytwo_week_position_posroam630d_630d_jerk_v118_signal,
    f07fw_f07_fiftytwo_week_position_gapz84d_84d_jerk_v119_signal,
    f07fw_f07_fiftytwo_week_position_gapz231d_231d_jerk_v120_signal,
    f07fw_f07_fiftytwo_week_position_gapz378d_378d_jerk_v121_signal,
    f07fw_f07_fiftytwo_week_position_gapz1008d_1008d_jerk_v122_signal,
    f07fw_f07_fiftytwo_week_position_uppshare147d_147d_jerk_v123_signal,
    f07fw_f07_fiftytwo_week_position_uppshare294d_294d_jerk_v124_signal,
    f07fw_f07_fiftytwo_week_position_uppshare504d_504d_jerk_v125_signal,
    f07fw_f07_fiftytwo_week_position_midskew63d_63d_jerk_v126_signal,
    f07fw_f07_fiftytwo_week_position_midskew210d_210d_jerk_v127_signal,
    f07fw_f07_fiftytwo_week_position_midskew357d_357d_jerk_v128_signal,
    f07fw_f07_fiftytwo_week_position_midskew882d_882d_jerk_v129_signal,
    f07fw_f07_fiftytwo_week_position_gaphi126d_126d_jerk_v130_signal,
    f07fw_f07_fiftytwo_week_position_gaphi273d_273d_jerk_v131_signal,
    f07fw_f07_fiftytwo_week_position_gaphi462d_462d_jerk_v132_signal,
    f07fw_f07_fiftytwo_week_position_gaphi1260d_1260d_jerk_v133_signal,
    f07fw_f07_fiftytwo_week_position_gaplo189d_189d_jerk_v134_signal,
    f07fw_f07_fiftytwo_week_position_gaplo336d_336d_jerk_v135_signal,
    f07fw_f07_fiftytwo_week_position_gaplo756d_756d_jerk_v136_signal,
    f07fw_f07_fiftytwo_week_position_bandpos105d_105d_jerk_v137_signal,
    f07fw_f07_fiftytwo_week_position_bandpos252d_252d_jerk_v138_signal,
    f07fw_f07_fiftytwo_week_position_bandpos420d_420d_jerk_v139_signal,
    f07fw_f07_fiftytwo_week_position_bandpos1134d_1134d_jerk_v140_signal,
    f07fw_f07_fiftytwo_week_position_span168d_168d_jerk_v141_signal,
    f07fw_f07_fiftytwo_week_position_span315d_315d_jerk_v142_signal,
    f07fw_f07_fiftytwo_week_position_span630d_630d_jerk_v143_signal,
    f07fw_f07_fiftytwo_week_position_gapresid84d_84d_jerk_v144_signal,
    f07fw_f07_fiftytwo_week_position_gapresid231d_231d_jerk_v145_signal,
    f07fw_f07_fiftytwo_week_position_loresid168d_168d_jerk_v146_signal,
    f07fw_f07_fiftytwo_week_position_nhfreq105d_105d_jerk_v147_signal,
    f07fw_f07_fiftytwo_week_position_nhfreq252d_252d_jerk_v148_signal,
    f07fw_f07_fiftytwo_week_position_nlfreq189d_189d_jerk_v149_signal,
    f07fw_f07_fiftytwo_week_position_anchdist126d_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_FIFTYTWO_WEEK_POSITION_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s not in allowlist" % (name, meta["inputs"])
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

    print("OK f07_fiftytwo_week_position_3rd_derivatives_001_150_claude: %d features pass" % n_features)
