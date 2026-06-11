import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)

def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives =====
def _f13_hl_range(h, l):
    return h - l


def _f13_hl_pct(h, l, c):
    return (h - l) / c.shift(1).replace(0, np.nan)


def _f13_true_range(h, l, c):
    pc = c.shift(1)
    tr1 = h - l
    tr2 = (h - pc).abs()
    tr3 = (l - pc).abs()
    return pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)


def _f13_atr(h, l, c, w):
    tr = _f13_true_range(h, l, c)
    return tr.rolling(w, min_periods=max(1, w // 2)).mean()


# 5d curvature of 21d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_21d_curv_v001_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_21d_curv_v002_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_21d_curv_v003_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_21d_curv_v004_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_21d_curv_v005_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_63d_curv_v006_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_63d_curv_v007_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_63d_curv_v008_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_63d_curv_v009_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_63d_curv_v010_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_126d_curv_v011_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_126d_curv_v012_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_126d_curv_v013_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_126d_curv_v014_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_126d_curv_v015_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_252d_curv_v016_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_252d_curv_v017_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_252d_curv_v018_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_252d_curv_v019_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d atr
def f13ir_f13_semi_intraday_range_dynamics_atr_252d_curv_v020_signal(high, low, closeadj):
    base = _f13_atr(high, low, closeadj, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_21d_curv_v021_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 21)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_21d_curv_v022_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 21)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_21d_curv_v023_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 21)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_21d_curv_v024_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 21)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_21d_curv_v025_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 21)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_63d_curv_v026_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_63d_curv_v027_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_63d_curv_v028_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_63d_curv_v029_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_63d_curv_v030_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_126d_curv_v031_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 126)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_126d_curv_v032_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 126)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_126d_curv_v033_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 126)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_126d_curv_v034_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 126)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_126d_curv_v035_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 126)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_252d_curv_v036_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 252)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_252d_curv_v037_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 252)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_252d_curv_v038_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 252)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_252d_curv_v039_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 252)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d atrpct
def f13ir_f13_semi_intraday_range_dynamics_atrpct_252d_curv_v040_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 252)
    base = atr / closeadj.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_21d_curv_v041_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_21d_curv_v042_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_21d_curv_v043_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_21d_curv_v044_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_21d_curv_v045_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_63d_curv_v046_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_63d_curv_v047_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_63d_curv_v048_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_63d_curv_v049_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_63d_curv_v050_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_126d_curv_v051_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_126d_curv_v052_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_126d_curv_v053_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_126d_curv_v054_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_126d_curv_v055_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_252d_curv_v056_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_252d_curv_v057_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_252d_curv_v058_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_252d_curv_v059_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d meanhl
def f13ir_f13_semi_intraday_range_dynamics_meanhl_252d_curv_v060_signal(high, low, closeadj):
    hl = high - low
    base = _mean(hl, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d stdhl
def f13ir_f13_semi_intraday_range_dynamics_stdhl_63d_curv_v061_signal(high, low, closeadj):
    hl = high - low
    base = _std(hl, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d stdhl
def f13ir_f13_semi_intraday_range_dynamics_stdhl_63d_curv_v062_signal(high, low, closeadj):
    hl = high - low
    base = _std(hl, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d stdhl
def f13ir_f13_semi_intraday_range_dynamics_stdhl_63d_curv_v063_signal(high, low, closeadj):
    hl = high - low
    base = _std(hl, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d stdhl
def f13ir_f13_semi_intraday_range_dynamics_stdhl_63d_curv_v064_signal(high, low, closeadj):
    hl = high - low
    base = _std(hl, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d stdhl
def f13ir_f13_semi_intraday_range_dynamics_stdhl_63d_curv_v065_signal(high, low, closeadj):
    hl = high - low
    base = _std(hl, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d stdhl
def f13ir_f13_semi_intraday_range_dynamics_stdhl_252d_curv_v066_signal(high, low, closeadj):
    hl = high - low
    base = _std(hl, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d stdhl
def f13ir_f13_semi_intraday_range_dynamics_stdhl_252d_curv_v067_signal(high, low, closeadj):
    hl = high - low
    base = _std(hl, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d stdhl
def f13ir_f13_semi_intraday_range_dynamics_stdhl_252d_curv_v068_signal(high, low, closeadj):
    hl = high - low
    base = _std(hl, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d stdhl
def f13ir_f13_semi_intraday_range_dynamics_stdhl_252d_curv_v069_signal(high, low, closeadj):
    hl = high - low
    base = _std(hl, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d stdhl
def f13ir_f13_semi_intraday_range_dynamics_stdhl_252d_curv_v070_signal(high, low, closeadj):
    hl = high - low
    base = _std(hl, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d parkinson
def f13ir_f13_semi_intraday_range_dynamics_parkinson_63d_curv_v071_signal(high, low, closeadj):
    r = np.log(high / low.replace(0, np.nan))
    base = (r * r).rolling(63, min_periods=32).mean() / (4 * np.log(2))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d parkinson
def f13ir_f13_semi_intraday_range_dynamics_parkinson_63d_curv_v072_signal(high, low, closeadj):
    r = np.log(high / low.replace(0, np.nan))
    base = (r * r).rolling(63, min_periods=32).mean() / (4 * np.log(2))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d parkinson
def f13ir_f13_semi_intraday_range_dynamics_parkinson_63d_curv_v073_signal(high, low, closeadj):
    r = np.log(high / low.replace(0, np.nan))
    base = (r * r).rolling(63, min_periods=32).mean() / (4 * np.log(2))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d parkinson
def f13ir_f13_semi_intraday_range_dynamics_parkinson_63d_curv_v074_signal(high, low, closeadj):
    r = np.log(high / low.replace(0, np.nan))
    base = (r * r).rolling(63, min_periods=32).mean() / (4 * np.log(2))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d parkinson
def f13ir_f13_semi_intraday_range_dynamics_parkinson_63d_curv_v075_signal(high, low, closeadj):
    r = np.log(high / low.replace(0, np.nan))
    base = (r * r).rolling(63, min_periods=32).mean() / (4 * np.log(2))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d parkinson
def f13ir_f13_semi_intraday_range_dynamics_parkinson_252d_curv_v076_signal(high, low, closeadj):
    r = np.log(high / low.replace(0, np.nan))
    base = (r * r).rolling(252, min_periods=126).mean() / (4 * np.log(2))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d parkinson
def f13ir_f13_semi_intraday_range_dynamics_parkinson_252d_curv_v077_signal(high, low, closeadj):
    r = np.log(high / low.replace(0, np.nan))
    base = (r * r).rolling(252, min_periods=126).mean() / (4 * np.log(2))
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d parkinson
def f13ir_f13_semi_intraday_range_dynamics_parkinson_252d_curv_v078_signal(high, low, closeadj):
    r = np.log(high / low.replace(0, np.nan))
    base = (r * r).rolling(252, min_periods=126).mean() / (4 * np.log(2))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d parkinson
def f13ir_f13_semi_intraday_range_dynamics_parkinson_252d_curv_v079_signal(high, low, closeadj):
    r = np.log(high / low.replace(0, np.nan))
    base = (r * r).rolling(252, min_periods=126).mean() / (4 * np.log(2))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d parkinson
def f13ir_f13_semi_intraday_range_dynamics_parkinson_252d_curv_v080_signal(high, low, closeadj):
    r = np.log(high / low.replace(0, np.nan))
    base = (r * r).rolling(252, min_periods=126).mean() / (4 * np.log(2))
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d closepos
def f13ir_f13_semi_intraday_range_dynamics_closepos_63d_curv_v081_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = _mean(pos, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d closepos
def f13ir_f13_semi_intraday_range_dynamics_closepos_63d_curv_v082_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = _mean(pos, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d closepos
def f13ir_f13_semi_intraday_range_dynamics_closepos_63d_curv_v083_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = _mean(pos, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d closepos
def f13ir_f13_semi_intraday_range_dynamics_closepos_63d_curv_v084_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = _mean(pos, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d closepos
def f13ir_f13_semi_intraday_range_dynamics_closepos_63d_curv_v085_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = _mean(pos, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d closepos
def f13ir_f13_semi_intraday_range_dynamics_closepos_252d_curv_v086_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = _mean(pos, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d closepos
def f13ir_f13_semi_intraday_range_dynamics_closepos_252d_curv_v087_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = _mean(pos, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d closepos
def f13ir_f13_semi_intraday_range_dynamics_closepos_252d_curv_v088_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = _mean(pos, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d closepos
def f13ir_f13_semi_intraday_range_dynamics_closepos_252d_curv_v089_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = _mean(pos, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d closepos
def f13ir_f13_semi_intraday_range_dynamics_closepos_252d_curv_v090_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = _mean(pos, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d rngexp
def f13ir_f13_semi_intraday_range_dynamics_rngexp_63d_curv_v091_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 63)
    base = hl / atr.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d rngexp
def f13ir_f13_semi_intraday_range_dynamics_rngexp_63d_curv_v092_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 63)
    base = hl / atr.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d rngexp
def f13ir_f13_semi_intraday_range_dynamics_rngexp_63d_curv_v093_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 63)
    base = hl / atr.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d rngexp
def f13ir_f13_semi_intraday_range_dynamics_rngexp_63d_curv_v094_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 63)
    base = hl / atr.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d rngexp
def f13ir_f13_semi_intraday_range_dynamics_rngexp_63d_curv_v095_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 63)
    base = hl / atr.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d rngexp
def f13ir_f13_semi_intraday_range_dynamics_rngexp_252d_curv_v096_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 252)
    base = hl / atr.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d rngexp
def f13ir_f13_semi_intraday_range_dynamics_rngexp_252d_curv_v097_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 252)
    base = hl / atr.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d rngexp
def f13ir_f13_semi_intraday_range_dynamics_rngexp_252d_curv_v098_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 252)
    base = hl / atr.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d rngexp
def f13ir_f13_semi_intraday_range_dynamics_rngexp_252d_curv_v099_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 252)
    base = hl / atr.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d rngexp
def f13ir_f13_semi_intraday_range_dynamics_rngexp_252d_curv_v100_signal(high, low, closeadj):
    hl = high - low
    atr = _f13_atr(high, low, closeadj, 252)
    base = hl / atr.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d rngposition
def f13ir_f13_semi_intraday_range_dynamics_rngposition_63d_curv_v101_signal(high, low, closeadj):
    hl = high - low
    lo = _min(hl, 63)
    hi = _max(hl, 63)
    base = (hl - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d rngposition
def f13ir_f13_semi_intraday_range_dynamics_rngposition_63d_curv_v102_signal(high, low, closeadj):
    hl = high - low
    lo = _min(hl, 63)
    hi = _max(hl, 63)
    base = (hl - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d rngposition
def f13ir_f13_semi_intraday_range_dynamics_rngposition_63d_curv_v103_signal(high, low, closeadj):
    hl = high - low
    lo = _min(hl, 63)
    hi = _max(hl, 63)
    base = (hl - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d rngposition
def f13ir_f13_semi_intraday_range_dynamics_rngposition_63d_curv_v104_signal(high, low, closeadj):
    hl = high - low
    lo = _min(hl, 63)
    hi = _max(hl, 63)
    base = (hl - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d rngposition
def f13ir_f13_semi_intraday_range_dynamics_rngposition_63d_curv_v105_signal(high, low, closeadj):
    hl = high - low
    lo = _min(hl, 63)
    hi = _max(hl, 63)
    base = (hl - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d rngposition
def f13ir_f13_semi_intraday_range_dynamics_rngposition_252d_curv_v106_signal(high, low, closeadj):
    hl = high - low
    lo = _min(hl, 252)
    hi = _max(hl, 252)
    base = (hl - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d rngposition
def f13ir_f13_semi_intraday_range_dynamics_rngposition_252d_curv_v107_signal(high, low, closeadj):
    hl = high - low
    lo = _min(hl, 252)
    hi = _max(hl, 252)
    base = (hl - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d rngposition
def f13ir_f13_semi_intraday_range_dynamics_rngposition_252d_curv_v108_signal(high, low, closeadj):
    hl = high - low
    lo = _min(hl, 252)
    hi = _max(hl, 252)
    base = (hl - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d rngposition
def f13ir_f13_semi_intraday_range_dynamics_rngposition_252d_curv_v109_signal(high, low, closeadj):
    hl = high - low
    lo = _min(hl, 252)
    hi = _max(hl, 252)
    base = (hl - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d rngposition
def f13ir_f13_semi_intraday_range_dynamics_rngposition_252d_curv_v110_signal(high, low, closeadj):
    hl = high - low
    lo = _min(hl, 252)
    hi = _max(hl, 252)
    base = (hl - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d strongclose
def f13ir_f13_semi_intraday_range_dynamics_strongclose_63d_curv_v111_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos > 0.8).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d strongclose
def f13ir_f13_semi_intraday_range_dynamics_strongclose_63d_curv_v112_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos > 0.8).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d strongclose
def f13ir_f13_semi_intraday_range_dynamics_strongclose_63d_curv_v113_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos > 0.8).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d strongclose
def f13ir_f13_semi_intraday_range_dynamics_strongclose_63d_curv_v114_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos > 0.8).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d strongclose
def f13ir_f13_semi_intraday_range_dynamics_strongclose_63d_curv_v115_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos > 0.8).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d strongclose
def f13ir_f13_semi_intraday_range_dynamics_strongclose_252d_curv_v116_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos > 0.8).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d strongclose
def f13ir_f13_semi_intraday_range_dynamics_strongclose_252d_curv_v117_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos > 0.8).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d strongclose
def f13ir_f13_semi_intraday_range_dynamics_strongclose_252d_curv_v118_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos > 0.8).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d strongclose
def f13ir_f13_semi_intraday_range_dynamics_strongclose_252d_curv_v119_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos > 0.8).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d strongclose
def f13ir_f13_semi_intraday_range_dynamics_strongclose_252d_curv_v120_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos > 0.8).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d weakclose
def f13ir_f13_semi_intraday_range_dynamics_weakclose_63d_curv_v121_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos < 0.2).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d weakclose
def f13ir_f13_semi_intraday_range_dynamics_weakclose_63d_curv_v122_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos < 0.2).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d weakclose
def f13ir_f13_semi_intraday_range_dynamics_weakclose_63d_curv_v123_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos < 0.2).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d weakclose
def f13ir_f13_semi_intraday_range_dynamics_weakclose_63d_curv_v124_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos < 0.2).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d weakclose
def f13ir_f13_semi_intraday_range_dynamics_weakclose_63d_curv_v125_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos < 0.2).astype(float).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d weakclose
def f13ir_f13_semi_intraday_range_dynamics_weakclose_252d_curv_v126_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos < 0.2).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d weakclose
def f13ir_f13_semi_intraday_range_dynamics_weakclose_252d_curv_v127_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos < 0.2).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d weakclose
def f13ir_f13_semi_intraday_range_dynamics_weakclose_252d_curv_v128_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos < 0.2).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d weakclose
def f13ir_f13_semi_intraday_range_dynamics_weakclose_252d_curv_v129_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos < 0.2).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d weakclose
def f13ir_f13_semi_intraday_range_dynamics_weakclose_252d_curv_v130_signal(high, low, closeadj):
    pos = (closeadj - low) / (high - low).replace(0, np.nan)
    base = (pos < 0.2).astype(float).rolling(252, min_periods=126).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d atrz
def f13ir_f13_semi_intraday_range_dynamics_atrz_63d_curv_v131_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    base = _z(atr, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d atrz
def f13ir_f13_semi_intraday_range_dynamics_atrz_63d_curv_v132_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    base = _z(atr, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d atrz
def f13ir_f13_semi_intraday_range_dynamics_atrz_63d_curv_v133_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    base = _z(atr, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d atrz
def f13ir_f13_semi_intraday_range_dynamics_atrz_63d_curv_v134_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    base = _z(atr, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d atrz
def f13ir_f13_semi_intraday_range_dynamics_atrz_63d_curv_v135_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    base = _z(atr, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d atrz
def f13ir_f13_semi_intraday_range_dynamics_atrz_252d_curv_v136_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 252)
    base = _z(atr, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d atrz
def f13ir_f13_semi_intraday_range_dynamics_atrz_252d_curv_v137_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 252)
    base = _z(atr, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d atrz
def f13ir_f13_semi_intraday_range_dynamics_atrz_252d_curv_v138_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 252)
    base = _z(atr, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d atrz
def f13ir_f13_semi_intraday_range_dynamics_atrz_252d_curv_v139_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 252)
    base = _z(atr, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d atrz
def f13ir_f13_semi_intraday_range_dynamics_atrz_252d_curv_v140_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 252)
    base = _z(atr, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d atrvolratio
def f13ir_f13_semi_intraday_range_dynamics_atrvolratio_63d_curv_v141_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    vol = _std(closeadj.pct_change(), 63) * closeadj
    base = atr / vol.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d atrvolratio
def f13ir_f13_semi_intraday_range_dynamics_atrvolratio_63d_curv_v142_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    vol = _std(closeadj.pct_change(), 63) * closeadj
    base = atr / vol.replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d atrvolratio
def f13ir_f13_semi_intraday_range_dynamics_atrvolratio_63d_curv_v143_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    vol = _std(closeadj.pct_change(), 63) * closeadj
    base = atr / vol.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d atrvolratio
def f13ir_f13_semi_intraday_range_dynamics_atrvolratio_63d_curv_v144_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    vol = _std(closeadj.pct_change(), 63) * closeadj
    base = atr / vol.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d atrvolratio
def f13ir_f13_semi_intraday_range_dynamics_atrvolratio_63d_curv_v145_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    vol = _std(closeadj.pct_change(), 63) * closeadj
    base = atr / vol.replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d atrdd
def f13ir_f13_semi_intraday_range_dynamics_atrdd_63d_curv_v146_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    base = atr - _max(atr, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d atrdd
def f13ir_f13_semi_intraday_range_dynamics_atrdd_63d_curv_v147_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    base = atr - _max(atr, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d atrdd
def f13ir_f13_semi_intraday_range_dynamics_atrdd_63d_curv_v148_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    base = atr - _max(atr, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d atrdd
def f13ir_f13_semi_intraday_range_dynamics_atrdd_63d_curv_v149_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    base = atr - _max(atr, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d atrdd
def f13ir_f13_semi_intraday_range_dynamics_atrdd_63d_curv_v150_signal(high, low, closeadj):
    atr = _f13_atr(high, low, closeadj, 63)
    base = atr - _max(atr, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
