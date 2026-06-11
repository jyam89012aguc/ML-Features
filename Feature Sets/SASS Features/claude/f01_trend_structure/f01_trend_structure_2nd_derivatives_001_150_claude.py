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


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives (trend structure) =====
def _f01_sma(close, w):
    return close.rolling(w, min_periods=max(1, w // 2)).mean()


def _f01_ema(close, w):
    return close.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _f01_pxma(close, w):
    ma = _f01_sma(close, w)
    return close / ma.replace(0, np.nan) - 1.0


def _f01_pxema(close, w):
    ma = _f01_ema(close, w)
    return close / ma.replace(0, np.nan) - 1.0


def _f01_slope(close, w):
    lp = np.log(close.replace(0, np.nan))
    x = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    mp = max(2, w // 2)
    xm = x.rolling(w, min_periods=mp).mean()
    ym = lp.rolling(w, min_periods=mp).mean()
    xy = (x * lp).rolling(w, min_periods=mp).mean()
    xx = (x * x).rolling(w, min_periods=mp).mean()
    cov = xy - xm * ym
    var = xx - xm * xm
    return cov / var.replace(0, np.nan)


def _f01_slope_r2(close, w):
    lp = np.log(close.replace(0, np.nan))
    x = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    mp = max(2, w // 2)
    xm = x.rolling(w, min_periods=mp).mean()
    ym = lp.rolling(w, min_periods=mp).mean()
    xy = (x * lp).rolling(w, min_periods=mp).mean()
    xx = (x * x).rolling(w, min_periods=mp).mean()
    yy = (lp * lp).rolling(w, min_periods=mp).mean()
    cov = xy - xm * ym
    vx = xx - xm * xm
    vy = yy - ym * ym
    return (cov * cov) / (vx * vy).replace(0, np.nan)


def _f01_macd(close, fast, slow):
    return _f01_ema(close, fast) - _f01_ema(close, slow)


def _f01_kama_er(close, w):
    net = (close - close.shift(w)).abs()
    gross = close.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return net / gross.replace(0, np.nan)


def _f01_chanpos(close, w):
    lp = np.log(close.replace(0, np.nan))
    x = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    mp = max(3, w // 2)
    xm = x.rolling(w, min_periods=mp).mean()
    ym = lp.rolling(w, min_periods=mp).mean()
    xy = (x * lp).rolling(w, min_periods=mp).mean()
    xx = (x * x).rolling(w, min_periods=mp).mean()
    yy = (lp * lp).rolling(w, min_periods=mp).mean()
    cov = xy - xm * ym
    vx = (xx - xm * xm).replace(0, np.nan)
    vy = yy - ym * ym
    beta = cov / vx
    fitted = (ym - beta * xm) + beta * x
    rsd = np.sqrt((vy - beta * cov).clip(lower=0))
    return (lp - fitted) / rsd.replace(0, np.nan)


def _f01_stack(close, w1, w2, w3):
    m1 = _f01_sma(close, w1)
    m2 = _f01_sma(close, w2)
    m3 = _f01_sma(close, w3)
    g12 = m1 / m2.replace(0, np.nan) - 1.0
    g23 = m2 / m3.replace(0, np.nan) - 1.0
    sw = max(63, w2)
    n12 = np.tanh(g12 / g12.rolling(sw, min_periods=max(21, sw // 3)).std().replace(0, np.nan))
    n23 = np.tanh(g23 / g23.rolling(sw, min_periods=max(21, sw // 3)).std().replace(0, np.nan))
    return (n12 + n23) / 2.0


def _f01_bslope(base, w):
    # rolling OLS slope of an arbitrary series `base` against time (regression rate)
    xs = pd.Series(np.arange(len(base), dtype=float), index=base.index)
    mp = max(2, w // 2)
    xm = xs.rolling(w, min_periods=mp).mean()
    ym = base.rolling(w, min_periods=mp).mean()
    xy = (xs * base).rolling(w, min_periods=mp).mean()
    xx = (xs * xs).rolling(w, min_periods=mp).mean()
    return (xy - xm * ym) / (xx - xm * xm).replace(0, np.nan)


# ============================================================
def f01ts_f01_trend_structure_pxma21diff_21d_slope_v001_signal(closeadj):
    base = _f01_pxma(closeadj, 21)
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxma63znrm_63d_slope_v002_signal(closeadj):
    base = _f01_pxma(closeadj, 63)
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxma126ewmv_126d_slope_v003_signal(closeadj):
    base = _f01_pxma(closeadj, 126)
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxma252slreg_252d_slope_v004_signal(closeadj):
    base = _f01_pxma(closeadj, 252)
    result = _f01_bslope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxema21znrm_21d_slope_v005_signal(closeadj):
    base = _f01_pxema(closeadj, 21)
    bsd = base.rolling(21, min_periods=max(5, 21 // 2)).std()
    result = (base - base.shift(5)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxema63ewmv_63d_slope_v006_signal(closeadj):
    base = _f01_pxema(closeadj, 63)
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxema126slreg_126d_slope_v007_signal(closeadj):
    base = _f01_pxema(closeadj, 126)
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxema252diff_252d_slope_v008_signal(closeadj):
    base = _f01_pxema(closeadj, 252)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slope21diff_21d_slope_v009_signal(closeadj):
    base = _f01_slope(closeadj, 21)
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slope63znrm_63d_slope_v010_signal(closeadj):
    base = _f01_slope(closeadj, 63)
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slope126ewmv_126d_slope_v011_signal(closeadj):
    base = _f01_slope(closeadj, 126)
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slope252slreg_252d_slope_v012_signal(closeadj):
    base = _f01_slope(closeadj, 252)
    result = _f01_bslope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_r2qual63diff_63d_slope_v013_signal(closeadj):
    base = _f01_slope_r2(closeadj, 63) * np.sign(_f01_slope(closeadj, 63))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_r2qual126znrm_126d_slope_v014_signal(closeadj):
    base = _f01_slope_r2(closeadj, 126) * np.sign(_f01_slope(closeadj, 126))
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_r2qual252ewmv_252d_slope_v015_signal(closeadj):
    base = _f01_slope_r2(closeadj, 252) * np.sign(_f01_slope(closeadj, 252))
    sm = base.ewm(span=63, min_periods=max(2, 63 // 2)).mean()
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maspr2163slreg_63d_slope_v016_signal(closeadj):
    base = _f01_sma(closeadj, 21) / _f01_sma(closeadj, 63).replace(0, np.nan) - 1.0
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maspr63126diff_126d_slope_v017_signal(closeadj):
    base = _f01_sma(closeadj, 63) / _f01_sma(closeadj, 126).replace(0, np.nan) - 1.0
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maspr63252znrm_252d_slope_v018_signal(closeadj):
    base = _f01_sma(closeadj, 63) / _f01_sma(closeadj, 252).replace(0, np.nan) - 1.0
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maspr126252ewmv_252d_slope_v019_signal(closeadj):
    base = _f01_sma(closeadj, 126) / _f01_sma(closeadj, 252).replace(0, np.nan) - 1.0
    sm = base.ewm(span=63, min_periods=max(2, 63 // 2)).mean()
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_emaspr2163znrm_63d_slope_v020_signal(closeadj):
    base = _f01_ema(closeadj, 21) / _f01_ema(closeadj, 63).replace(0, np.nan) - 1.0
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_emaspr63126diff_126d_slope_v021_signal(closeadj):
    base = _f01_ema(closeadj, 63) / _f01_ema(closeadj, 126).replace(0, np.nan) - 1.0
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_macd2163ewmv_63d_slope_v022_signal(closeadj):
    base = _f01_macd(closeadj, 21, 63) / closeadj.replace(0, np.nan)
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_macd63126ewmv_126d_slope_v023_signal(closeadj):
    base = _f01_macd(closeadj, 63, 126) / closeadj.replace(0, np.nan)
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_macdhist2163slreg_63d_slope_v024_signal(closeadj):
    macd = _f01_macd(closeadj, 21, 63)
    sig = macd.ewm(span=21, min_periods=10).mean()
    base = (macd - sig) / closeadj.replace(0, np.nan)
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_ersign21znrm_21d_slope_v025_signal(closeadj):
    er = _f01_kama_er(closeadj, 21)
    base = er * np.sign(closeadj - closeadj.shift(21))
    bsd = base.rolling(21, min_periods=max(5, 21 // 2)).std()
    result = (base - base.shift(5)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_ersign63ewmv_63d_slope_v026_signal(closeadj):
    er = _f01_kama_er(closeadj, 63)
    base = er * np.sign(closeadj - closeadj.shift(63))
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_ersign126slreg_126d_slope_v027_signal(closeadj):
    er = _f01_kama_er(closeadj, 126)
    base = er * np.sign(closeadj - closeadj.shift(126))
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_ersign252diff_252d_slope_v028_signal(closeadj):
    er = _f01_kama_er(closeadj, 252)
    base = er * np.sign(closeadj - closeadj.shift(252))
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_stack2163252znrm_252d_slope_v029_signal(closeadj):
    base = _f01_stack(closeadj, 21, 63, 252)
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_stack63126252ewmv_252d_slope_v030_signal(closeadj):
    base = _f01_stack(closeadj, 63, 126, 252)
    sm = base.ewm(span=63, min_periods=max(2, 63 // 2)).mean()
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_abovefrac63slreg_63d_slope_v031_signal(closeadj):
    ma = _f01_sma(closeadj, 63)
    above = (closeadj > ma).astype(float)
    base = above.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_abovefrac126diff_126d_slope_v032_signal(closeadj):
    ma = _f01_sma(closeadj, 126)
    above = (closeadj > ma).astype(float)
    base = above.rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_abovefrac252znrm_252d_slope_v033_signal(closeadj):
    ma = _f01_sma(closeadj, 252)
    above = (closeadj > ma).astype(float)
    base = above.rolling(252, min_periods=max(1, 252 // 2)).mean()
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maslope63ewmv_63d_slope_v034_signal(closeadj):
    ma = _f01_sma(closeadj, 63)
    base = ma / ma.shift(21).replace(0, np.nan) - 1.0
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maslope126slreg_126d_slope_v035_signal(closeadj):
    ma = _f01_sma(closeadj, 126)
    base = ma / ma.shift(21).replace(0, np.nan) - 1.0
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maslope252diff_252d_slope_v036_signal(closeadj):
    ma = _f01_sma(closeadj, 252)
    base = ma / ma.shift(63).replace(0, np.nan) - 1.0
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_emavel63znrm_63d_slope_v037_signal(closeadj):
    e = _f01_ema(closeadj, 63)
    base = np.log(e.replace(0, np.nan) / e.shift(21).replace(0, np.nan))
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_emavel252ewmv_252d_slope_v038_signal(closeadj):
    e = _f01_ema(closeadj, 252)
    base = np.log(e.replace(0, np.nan) / e.shift(63).replace(0, np.nan))
    sm = base.ewm(span=63, min_periods=max(2, 63 // 2)).mean()
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maband126slreg_126d_slope_v039_signal(closeadj):
    ma = _f01_sma(closeadj, 126)
    sd = closeadj.rolling(126, min_periods=63).std()
    base = (closeadj - ma) / sd.replace(0, np.nan)
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maband252diff_252d_slope_v040_signal(closeadj):
    ma = _f01_sma(closeadj, 252)
    sd = closeadj.rolling(252, min_periods=126).std()
    base = (closeadj - ma) / sd.replace(0, np.nan)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_emasmadiv63znrm_63d_slope_v041_signal(closeadj):
    base = _f01_ema(closeadj, 63) / _f01_sma(closeadj, 63).replace(0, np.nan) - 1.0
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_emasmadiv126ewmv_126d_slope_v042_signal(closeadj):
    base = _f01_ema(closeadj, 126) / _f01_sma(closeadj, 126).replace(0, np.nan) - 1.0
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slopequal63slreg_63d_slope_v043_signal(closeadj):
    base = _f01_slope(closeadj, 63) * _f01_slope_r2(closeadj, 63)
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slopequal252diff_252d_slope_v044_signal(closeadj):
    base = _f01_slope(closeadj, 252) * _f01_slope_r2(closeadj, 252)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_snr126znrm_126d_slope_v045_signal(closeadj):
    sl = _f01_slope(closeadj, 126)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    base = sl / vol.replace(0, np.nan)
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_fanwidthewmv_252d_slope_v046_signal(closeadj):
    m1 = _f01_sma(closeadj, 21)
    m2 = _f01_sma(closeadj, 63)
    m3 = _f01_sma(closeadj, 126)
    m4 = _f01_sma(closeadj, 252)
    stacked = pd.concat([m1, m2, m3, m4], axis=1)
    base = (stacked.max(axis=1) - stacked.min(axis=1)) / closeadj.replace(0, np.nan)
    sm = base.ewm(span=63, min_periods=max(2, 63 // 2)).mean()
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxma504slreg_504d_slope_v047_signal(closeadj):
    base = _f01_pxma(closeadj, 504)
    result = _f01_bslope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmadvol63diff_63d_slope_v048_signal(closeadj, volume):
    d = _f01_pxma(closeadj, 63)
    dvol = closeadj * volume
    base = d * _z(dvol, 63)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_trixznrm_63d_slope_v049_signal(closeadj):
    e1 = _f01_ema(closeadj, 21)
    e2 = e1.ewm(span=21, min_periods=10).mean()
    e3 = e2.ewm(span=21, min_periods=10).mean()
    base = np.log(e3.replace(0, np.nan) / e3.shift(21).replace(0, np.nan))
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmatanh21ewmv_21d_slope_v050_signal(closeadj):
    base = np.tanh(8.0 * _f01_pxma(closeadj, 21))
    sm = base.ewm(span=5, min_periods=max(2, 5 // 2)).mean()
    result = sm - sm.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmatanh63slreg_63d_slope_v051_signal(closeadj):
    base = np.tanh(8.0 * _f01_pxma(closeadj, 63))
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmatanh126diff_126d_slope_v052_signal(closeadj):
    base = np.tanh(8.0 * _f01_pxma(closeadj, 126))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmatanh252znrm_252d_slope_v053_signal(closeadj):
    base = np.tanh(8.0 * _f01_pxma(closeadj, 252))
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmasm63ewmv_63d_slope_v054_signal(closeadj):
    d = _f01_pxma(closeadj, 63)
    base = np.sign(d) * np.sqrt(d.abs())
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmasm126slreg_126d_slope_v055_signal(closeadj):
    d = _f01_pxma(closeadj, 126)
    base = np.sign(d) * np.sqrt(d.abs())
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmasm252diff_252d_slope_v056_signal(closeadj):
    d = _f01_pxma(closeadj, 252)
    base = np.sign(d) * np.sqrt(d.abs())
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmavol63diff_63d_slope_v057_signal(closeadj):
    d = _f01_pxma(closeadj, 63)
    vol = closeadj.pct_change().rolling(31, min_periods=max(5, 31 // 2)).std()
    base = d / vol.replace(0, np.nan)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmavol126diff_126d_slope_v058_signal(closeadj):
    d = _f01_pxma(closeadj, 126)
    vol = closeadj.pct_change().rolling(63, min_periods=max(5, 63 // 2)).std()
    base = d / vol.replace(0, np.nan)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmavol252znrm_252d_slope_v059_signal(closeadj):
    d = _f01_pxma(closeadj, 252)
    vol = closeadj.pct_change().rolling(126, min_periods=max(5, 126 // 2)).std()
    base = d / vol.replace(0, np.nan)
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maspr521znrm_21d_slope_v060_signal(closeadj):
    base = _f01_sma(closeadj, 5) / _f01_sma(closeadj, 21).replace(0, np.nan) - 1.0
    bsd = base.rolling(21, min_periods=max(5, 21 // 2)).std()
    result = (base - base.shift(5)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maspr563znrm_63d_slope_v061_signal(closeadj):
    base = _f01_sma(closeadj, 5) / _f01_sma(closeadj, 63).replace(0, np.nan) - 1.0
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maspr21126ewmv_126d_slope_v062_signal(closeadj):
    base = _f01_sma(closeadj, 21) / _f01_sma(closeadj, 126).replace(0, np.nan) - 1.0
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maspr21252slreg_252d_slope_v063_signal(closeadj):
    base = _f01_sma(closeadj, 21) / _f01_sma(closeadj, 252).replace(0, np.nan) - 1.0
    result = _f01_bslope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_emaspr521znrm_21d_slope_v064_signal(closeadj):
    base = _f01_ema(closeadj, 5) / _f01_ema(closeadj, 21).replace(0, np.nan) - 1.0
    bsd = base.rolling(21, min_periods=max(5, 21 // 2)).std()
    result = (base - base.shift(5)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_emaspr63252slreg_252d_slope_v065_signal(closeadj):
    base = _f01_ema(closeadj, 63) / _f01_ema(closeadj, 252).replace(0, np.nan) - 1.0
    result = _f01_bslope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_emaspr126252diff_252d_slope_v066_signal(closeadj):
    base = _f01_ema(closeadj, 126) / _f01_ema(closeadj, 252).replace(0, np.nan) - 1.0
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_macd12126slreg_126d_slope_v067_signal(closeadj):
    base = _f01_macd(closeadj, 12, 126) / closeadj.replace(0, np.nan)
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_macd21126znrm_126d_slope_v068_signal(closeadj):
    base = _f01_macd(closeadj, 21, 126) / closeadj.replace(0, np.nan)
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_smoothslope126znrm_126d_slope_v069_signal(closeadj):
    sm = _f01_ema(closeadj, 21)
    base = _f01_slope(sm, 126)
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_smoothslope252znrm_252d_slope_v070_signal(closeadj):
    sm = _f01_ema(closeadj, 21)
    base = _f01_slope(sm, 252)
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slopet63ewmv_63d_slope_v071_signal(closeadj):
    base = _f01_slope(closeadj, 63) * np.sqrt(_f01_slope_r2(closeadj, 63).clip(lower=0))
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slopet126slreg_126d_slope_v072_signal(closeadj):
    base = _f01_slope(closeadj, 126) * np.sqrt(_f01_slope_r2(closeadj, 126).clip(lower=0))
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slopet252znrm_252d_slope_v073_signal(closeadj):
    base = _f01_slope(closeadj, 252) * np.sqrt(_f01_slope_r2(closeadj, 252).clip(lower=0))
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_fanwidth3diff_252d_slope_v074_signal(closeadj):
    m1 = _f01_sma(closeadj, 21)
    m2 = _f01_sma(closeadj, 63)
    m3 = _f01_sma(closeadj, 252)
    stacked = pd.concat([m1, m2, m3], axis=1)
    base = (stacked.max(axis=1) - stacked.min(axis=1)) / closeadj.replace(0, np.nan)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxemavol21ewmv_21d_slope_v075_signal(closeadj):
    d = _f01_pxema(closeadj, 21)
    vol = closeadj.pct_change().rolling(21, min_periods=max(5, 21 // 2)).std()
    base = d / vol.replace(0, np.nan)
    sm = base.ewm(span=5, min_periods=max(2, 5 // 2)).mean()
    result = sm - sm.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_emavel21diff_21d_slope_v076_signal(closeadj):
    e = _f01_ema(closeadj, 21)
    base = np.log(e.replace(0, np.nan) / e.shift(5).replace(0, np.nan))
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_emavel126slreg_126d_slope_v077_signal(closeadj):
    e = _f01_ema(closeadj, 126)
    base = np.log(e.replace(0, np.nan) / e.shift(21).replace(0, np.nan))
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maslope21ewmv_21d_slope_v078_signal(closeadj):
    ma = _f01_sma(closeadj, 21)
    base = ma / ma.shift(5).replace(0, np.nan) - 1.0
    sm = base.ewm(span=5, min_periods=max(2, 5 // 2)).mean()
    result = sm - sm.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maslope504slreg_504d_slope_v079_signal(closeadj):
    ma = _f01_sma(closeadj, 504)
    base = ma / ma.shift(63).replace(0, np.nan) - 1.0
    result = _f01_bslope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_ersign42diff_42d_slope_v080_signal(closeadj):
    er = _f01_kama_er(closeadj, 42)
    base = er * np.sign(closeadj - closeadj.shift(42))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_ersign189znrm_189d_slope_v081_signal(closeadj):
    er = _f01_kama_er(closeadj, 189)
    base = er * np.sign(closeadj - closeadj.shift(189))
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_distterm2163ewmv_63d_slope_v082_signal(closeadj):
    base = _f01_pxma(closeadj, 21) - _f01_pxma(closeadj, 63)
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_distterm63126znrm_126d_slope_v083_signal(closeadj):
    base = _f01_pxma(closeadj, 63) - _f01_pxma(closeadj, 126)
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_distterm126252diff_252d_slope_v084_signal(closeadj):
    base = _f01_pxma(closeadj, 126) - _f01_pxma(closeadj, 252)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slopeterm2163znrm_63d_slope_v085_signal(closeadj):
    base = _f01_slope(closeadj, 21) - _f01_slope(closeadj, 63)
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slopeterm63126ewmv_126d_slope_v086_signal(closeadj):
    base = _f01_slope(closeadj, 63) - _f01_slope(closeadj, 126)
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slopeterm63252slreg_252d_slope_v087_signal(closeadj):
    base = _f01_slope(closeadj, 63) - _f01_slope(closeadj, 252)
    result = _f01_bslope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slopeterm126252diff_252d_slope_v088_signal(closeadj):
    base = _f01_slope(closeadj, 126) - _f01_slope(closeadj, 252)
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_emasmadiv252znrm_252d_slope_v089_signal(closeadj):
    base = _f01_ema(closeadj, 252) / _f01_sma(closeadj, 252).replace(0, np.nan) - 1.0
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxma5ewmv_5d_slope_v090_signal(closeadj):
    base = _f01_pxma(closeadj, 5)
    sm = base.ewm(span=5, min_periods=max(2, 5 // 2)).mean()
    result = sm - sm.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxma42slreg_42d_slope_v091_signal(closeadj):
    base = _f01_pxma(closeadj, 42)
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxema42diff_42d_slope_v092_signal(closeadj):
    base = _f01_pxema(closeadj, 42)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slope42diff_42d_slope_v093_signal(closeadj):
    base = _f01_slope(closeadj, 42)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slope189znrm_189d_slope_v094_signal(closeadj):
    base = _f01_slope(closeadj, 189)
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slope378ewmv_378d_slope_v095_signal(closeadj):
    base = _f01_slope(closeadj, 378)
    sm = base.ewm(span=63, min_periods=max(2, 63 // 2)).mean()
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_r2qual42slreg_42d_slope_v096_signal(closeadj):
    base = _f01_slope_r2(closeadj, 42) * np.sign(_f01_slope(closeadj, 42))
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_r2qual189diff_189d_slope_v097_signal(closeadj):
    base = _f01_slope_r2(closeadj, 189) * np.sign(_f01_slope(closeadj, 189))
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_snr63slreg_63d_slope_v098_signal(closeadj):
    sl = _f01_slope(closeadj, 63)
    vol = closeadj.pct_change().rolling(42, min_periods=21).std()
    base = sl / vol.replace(0, np.nan)
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_abovefrac21slreg_21d_slope_v099_signal(closeadj):
    ma = _f01_sma(closeadj, 21)
    above = (closeadj > ma).astype(float)
    base = above.rolling(21, min_periods=10).mean()
    result = _f01_bslope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_abovefrac42diff_42d_slope_v100_signal(closeadj):
    ma = _f01_sma(closeadj, 42)
    above = (closeadj > ma).astype(float)
    base = above.rolling(42, min_periods=21).mean()
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maspr21v126znrm_126d_slope_v101_signal(closeadj):
    base = _f01_sma(closeadj, 21) / _f01_sma(closeadj, 126).replace(0, np.nan) - 1.0
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maband63ewmv_63d_slope_v102_signal(closeadj):
    ma = _f01_sma(closeadj, 63)
    sd = closeadj.rolling(63, min_periods=21).std()
    base = (closeadj - ma) / sd.replace(0, np.nan)
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_macdhist1226slreg_26d_slope_v103_signal(closeadj):
    macd = _f01_macd(closeadj, 12, 26)
    sig = macd.ewm(span=9, min_periods=5).mean()
    base = (macd - sig) / closeadj.replace(0, np.nan)
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_stack52163diff_63d_slope_v104_signal(closeadj):
    base = _f01_stack(closeadj, 5, 21, 63)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_logdistma126znrm_126d_slope_v105_signal(closeadj):
    base = np.log(closeadj.replace(0, np.nan) / _f01_sma(closeadj, 126).replace(0, np.nan))
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_erpure63slreg_63d_slope_v106_signal(closeadj):
    base = _f01_kama_er(closeadj, 63)
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_erpure126diff_126d_slope_v107_signal(closeadj):
    base = _f01_kama_er(closeadj, 126)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_dualtrend21252znrm_252d_slope_v108_signal(closeadj):
    ds = _f01_pxma(closeadj, 21)
    dl = _f01_pxma(closeadj, 252)
    base = np.sign(ds * dl) * np.sqrt((ds * dl).abs())
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_macdlog63252znrm_252d_slope_v109_signal(closeadj):
    base = np.log(_f01_ema(closeadj, 63).replace(0, np.nan) / _f01_ema(closeadj, 252).replace(0, np.nan))
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_erpure21diff_21d_slope_v110_signal(closeadj):
    base = _f01_kama_er(closeadj, 21)
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_chanpos63znrm_63d_slope_v111_signal(closeadj):
    base = _f01_chanpos(closeadj, 63)
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_chanpos126ewmv_126d_slope_v112_signal(closeadj):
    base = _f01_chanpos(closeadj, 126)
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_chanpos252slreg_252d_slope_v113_signal(closeadj):
    base = _f01_chanpos(closeadj, 252)
    result = _f01_bslope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmatanh5diff_5d_slope_v114_signal(closeadj):
    base = np.tanh(20.0 * _f01_pxma(closeadj, 5))
    result = base - base.shift(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmatanh42znrm_42d_slope_v115_signal(closeadj):
    base = np.tanh(10.0 * _f01_pxma(closeadj, 42))
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmatanh189ewmv_189d_slope_v116_signal(closeadj):
    base = np.tanh(6.0 * _f01_pxma(closeadj, 189))
    sm = base.ewm(span=63, min_periods=max(2, 63 // 2)).mean()
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_stack21126252ewmv_252d_slope_v117_signal(closeadj):
    base = _f01_stack(closeadj, 21, 126, 252)
    sm = base.ewm(span=63, min_periods=max(2, 63 // 2)).mean()
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maband504slreg_504d_slope_v118_signal(closeadj):
    ma = _f01_sma(closeadj, 504)
    sd = closeadj.rolling(504, min_periods=252).std()
    base = (closeadj - ma) / sd.replace(0, np.nan)
    result = _f01_bslope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_smoothslope63znrm_63d_slope_v119_signal(closeadj):
    sm = _f01_ema(closeadj, 21)
    base = _f01_slope(sm, 63)
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slopet42ewmv_42d_slope_v120_signal(closeadj):
    base = _f01_slope(closeadj, 42) * np.sqrt(_f01_slope_r2(closeadj, 42).clip(lower=0))
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slopet189slreg_189d_slope_v121_signal(closeadj):
    base = _f01_slope(closeadj, 189) * np.sqrt(_f01_slope_r2(closeadj, 189).clip(lower=0))
    result = _f01_bslope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_distterm542diff_42d_slope_v122_signal(closeadj):
    base = _f01_pxma(closeadj, 5) - _f01_pxma(closeadj, 42)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_distterm21189znrm_189d_slope_v123_signal(closeadj):
    base = _f01_pxma(closeadj, 21) - _f01_pxma(closeadj, 189)
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmavol21slreg_21d_slope_v124_signal(closeadj):
    d = _f01_pxma(closeadj, 21)
    vol = closeadj.pct_change().rolling(21, min_periods=10).std()
    base = d / vol.replace(0, np.nan)
    result = _f01_bslope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_abovefrac189slreg_189d_slope_v125_signal(closeadj):
    ma = _f01_sma(closeadj, 189)
    above = (closeadj > ma).astype(float)
    base = above.rolling(189, min_periods=95).mean()
    result = _f01_bslope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_abovefrac504diff_504d_slope_v126_signal(closeadj):
    ma = _f01_sma(closeadj, 504)
    above = (closeadj > ma).astype(float)
    base = above.rolling(504, min_periods=252).mean()
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_emasmadiv21znrm_21d_slope_v127_signal(closeadj):
    base = _f01_ema(closeadj, 21) / _f01_sma(closeadj, 21).replace(0, np.nan) - 1.0
    bsd = base.rolling(21, min_periods=max(5, 21 // 2)).std()
    result = (base - base.shift(5)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maspr42189ewmv_189d_slope_v128_signal(closeadj):
    base = _f01_sma(closeadj, 42) / _f01_sma(closeadj, 189).replace(0, np.nan) - 1.0
    sm = base.ewm(span=63, min_periods=max(2, 63 // 2)).mean()
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slope504slreg_504d_slope_v129_signal(closeadj):
    base = _f01_slope(closeadj, 504)
    result = _f01_bslope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_erpure252znrm_252d_slope_v130_signal(closeadj):
    base = _f01_kama_er(closeadj, 252)
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_emasmadiv42ewmv_42d_slope_v131_signal(closeadj):
    base = _f01_ema(closeadj, 42) / _f01_sma(closeadj, 42).replace(0, np.nan) - 1.0
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_distterm42126slreg_126d_slope_v132_signal(closeadj):
    base = _f01_pxma(closeadj, 42) - _f01_pxma(closeadj, 126)
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmatanh378diff_378d_slope_v133_signal(closeadj):
    base = np.tanh(5.0 * _f01_pxma(closeadj, 378))
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmasm21znrm_21d_slope_v134_signal(closeadj):
    d = _f01_pxma(closeadj, 21)
    base = np.sign(d) * np.sqrt(d.abs())
    bsd = base.rolling(21, min_periods=max(5, 21 // 2)).std()
    result = (base - base.shift(5)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmasm42ewmv_42d_slope_v135_signal(closeadj):
    d = _f01_pxma(closeadj, 42)
    base = np.sign(d) * np.sqrt(d.abs())
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_pxmasm189slreg_189d_slope_v136_signal(closeadj):
    d = _f01_pxma(closeadj, 189)
    base = np.sign(d) * np.sqrt(d.abs())
    result = _f01_bslope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_logdistma504diff_504d_slope_v137_signal(closeadj):
    base = np.log(closeadj.replace(0, np.nan) / _f01_sma(closeadj, 504).replace(0, np.nan))
    result = base - base.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slope10slreg_10d_slope_v138_signal(closeadj):
    base = _f01_slope(closeadj, 10)
    result = _f01_bslope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slope32diff_32d_slope_v139_signal(closeadj):
    base = _f01_slope(closeadj, 32)
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slope95znrm_95d_slope_v140_signal(closeadj):
    base = _f01_slope(closeadj, 95)
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_slope315ewmv_315d_slope_v141_signal(closeadj):
    base = _f01_slope(closeadj, 315)
    sm = base.ewm(span=63, min_periods=max(2, 63 // 2)).mean()
    result = sm - sm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_ersign32slreg_32d_slope_v142_signal(closeadj):
    er = _f01_kama_er(closeadj, 32)
    base = er * np.sign(closeadj - closeadj.shift(32))
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_ersign95diff_95d_slope_v143_signal(closeadj):
    er = _f01_kama_er(closeadj, 95)
    base = er * np.sign(closeadj - closeadj.shift(95))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_ersign315znrm_315d_slope_v144_signal(closeadj):
    er = _f01_kama_er(closeadj, 315)
    base = er * np.sign(closeadj - closeadj.shift(315))
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maspr1063ewmv_63d_slope_v145_signal(closeadj):
    base = _f01_sma(closeadj, 10) / _f01_sma(closeadj, 63).replace(0, np.nan) - 1.0
    sm = base.ewm(span=21, min_periods=max(2, 21 // 2)).mean()
    result = sm - sm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maspr95378znrm_378d_slope_v146_signal(closeadj):
    base = _f01_sma(closeadj, 95) / _f01_sma(closeadj, 378).replace(0, np.nan) - 1.0
    bsd = base.rolling(189, min_periods=max(5, 189 // 2)).std()
    result = (base - base.shift(63)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_emaspr1042slreg_42d_slope_v147_signal(closeadj):
    base = _f01_ema(closeadj, 10) / _f01_ema(closeadj, 42).replace(0, np.nan) - 1.0
    result = _f01_bslope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_macdlog1063diff_63d_slope_v148_signal(closeadj):
    base = np.log(_f01_ema(closeadj, 10).replace(0, np.nan) / _f01_ema(closeadj, 63).replace(0, np.nan))
    result = base - base.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maslope42znrm_42d_slope_v149_signal(closeadj):
    ma = _f01_sma(closeadj, 42)
    base = ma / ma.shift(10).replace(0, np.nan) - 1.0
    bsd = base.rolling(63, min_periods=max(5, 63 // 2)).std()
    result = (base - base.shift(21)) / bsd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f01ts_f01_trend_structure_maslope189slreg_189d_slope_v150_signal(closeadj):
    ma = _f01_sma(closeadj, 189)
    base = ma / ma.shift(42).replace(0, np.nan) - 1.0
    result = _f01_bslope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01ts_f01_trend_structure_pxma21diff_21d_slope_v001_signal,
    f01ts_f01_trend_structure_pxma63znrm_63d_slope_v002_signal,
    f01ts_f01_trend_structure_pxma126ewmv_126d_slope_v003_signal,
    f01ts_f01_trend_structure_pxma252slreg_252d_slope_v004_signal,
    f01ts_f01_trend_structure_pxema21znrm_21d_slope_v005_signal,
    f01ts_f01_trend_structure_pxema63ewmv_63d_slope_v006_signal,
    f01ts_f01_trend_structure_pxema126slreg_126d_slope_v007_signal,
    f01ts_f01_trend_structure_pxema252diff_252d_slope_v008_signal,
    f01ts_f01_trend_structure_slope21diff_21d_slope_v009_signal,
    f01ts_f01_trend_structure_slope63znrm_63d_slope_v010_signal,
    f01ts_f01_trend_structure_slope126ewmv_126d_slope_v011_signal,
    f01ts_f01_trend_structure_slope252slreg_252d_slope_v012_signal,
    f01ts_f01_trend_structure_r2qual63diff_63d_slope_v013_signal,
    f01ts_f01_trend_structure_r2qual126znrm_126d_slope_v014_signal,
    f01ts_f01_trend_structure_r2qual252ewmv_252d_slope_v015_signal,
    f01ts_f01_trend_structure_maspr2163slreg_63d_slope_v016_signal,
    f01ts_f01_trend_structure_maspr63126diff_126d_slope_v017_signal,
    f01ts_f01_trend_structure_maspr63252znrm_252d_slope_v018_signal,
    f01ts_f01_trend_structure_maspr126252ewmv_252d_slope_v019_signal,
    f01ts_f01_trend_structure_emaspr2163znrm_63d_slope_v020_signal,
    f01ts_f01_trend_structure_emaspr63126diff_126d_slope_v021_signal,
    f01ts_f01_trend_structure_macd2163ewmv_63d_slope_v022_signal,
    f01ts_f01_trend_structure_macd63126ewmv_126d_slope_v023_signal,
    f01ts_f01_trend_structure_macdhist2163slreg_63d_slope_v024_signal,
    f01ts_f01_trend_structure_ersign21znrm_21d_slope_v025_signal,
    f01ts_f01_trend_structure_ersign63ewmv_63d_slope_v026_signal,
    f01ts_f01_trend_structure_ersign126slreg_126d_slope_v027_signal,
    f01ts_f01_trend_structure_ersign252diff_252d_slope_v028_signal,
    f01ts_f01_trend_structure_stack2163252znrm_252d_slope_v029_signal,
    f01ts_f01_trend_structure_stack63126252ewmv_252d_slope_v030_signal,
    f01ts_f01_trend_structure_abovefrac63slreg_63d_slope_v031_signal,
    f01ts_f01_trend_structure_abovefrac126diff_126d_slope_v032_signal,
    f01ts_f01_trend_structure_abovefrac252znrm_252d_slope_v033_signal,
    f01ts_f01_trend_structure_maslope63ewmv_63d_slope_v034_signal,
    f01ts_f01_trend_structure_maslope126slreg_126d_slope_v035_signal,
    f01ts_f01_trend_structure_maslope252diff_252d_slope_v036_signal,
    f01ts_f01_trend_structure_emavel63znrm_63d_slope_v037_signal,
    f01ts_f01_trend_structure_emavel252ewmv_252d_slope_v038_signal,
    f01ts_f01_trend_structure_maband126slreg_126d_slope_v039_signal,
    f01ts_f01_trend_structure_maband252diff_252d_slope_v040_signal,
    f01ts_f01_trend_structure_emasmadiv63znrm_63d_slope_v041_signal,
    f01ts_f01_trend_structure_emasmadiv126ewmv_126d_slope_v042_signal,
    f01ts_f01_trend_structure_slopequal63slreg_63d_slope_v043_signal,
    f01ts_f01_trend_structure_slopequal252diff_252d_slope_v044_signal,
    f01ts_f01_trend_structure_snr126znrm_126d_slope_v045_signal,
    f01ts_f01_trend_structure_fanwidthewmv_252d_slope_v046_signal,
    f01ts_f01_trend_structure_pxma504slreg_504d_slope_v047_signal,
    f01ts_f01_trend_structure_pxmadvol63diff_63d_slope_v048_signal,
    f01ts_f01_trend_structure_trixznrm_63d_slope_v049_signal,
    f01ts_f01_trend_structure_pxmatanh21ewmv_21d_slope_v050_signal,
    f01ts_f01_trend_structure_pxmatanh63slreg_63d_slope_v051_signal,
    f01ts_f01_trend_structure_pxmatanh126diff_126d_slope_v052_signal,
    f01ts_f01_trend_structure_pxmatanh252znrm_252d_slope_v053_signal,
    f01ts_f01_trend_structure_pxmasm63ewmv_63d_slope_v054_signal,
    f01ts_f01_trend_structure_pxmasm126slreg_126d_slope_v055_signal,
    f01ts_f01_trend_structure_pxmasm252diff_252d_slope_v056_signal,
    f01ts_f01_trend_structure_pxmavol63diff_63d_slope_v057_signal,
    f01ts_f01_trend_structure_pxmavol126diff_126d_slope_v058_signal,
    f01ts_f01_trend_structure_pxmavol252znrm_252d_slope_v059_signal,
    f01ts_f01_trend_structure_maspr521znrm_21d_slope_v060_signal,
    f01ts_f01_trend_structure_maspr563znrm_63d_slope_v061_signal,
    f01ts_f01_trend_structure_maspr21126ewmv_126d_slope_v062_signal,
    f01ts_f01_trend_structure_maspr21252slreg_252d_slope_v063_signal,
    f01ts_f01_trend_structure_emaspr521znrm_21d_slope_v064_signal,
    f01ts_f01_trend_structure_emaspr63252slreg_252d_slope_v065_signal,
    f01ts_f01_trend_structure_emaspr126252diff_252d_slope_v066_signal,
    f01ts_f01_trend_structure_macd12126slreg_126d_slope_v067_signal,
    f01ts_f01_trend_structure_macd21126znrm_126d_slope_v068_signal,
    f01ts_f01_trend_structure_smoothslope126znrm_126d_slope_v069_signal,
    f01ts_f01_trend_structure_smoothslope252znrm_252d_slope_v070_signal,
    f01ts_f01_trend_structure_slopet63ewmv_63d_slope_v071_signal,
    f01ts_f01_trend_structure_slopet126slreg_126d_slope_v072_signal,
    f01ts_f01_trend_structure_slopet252znrm_252d_slope_v073_signal,
    f01ts_f01_trend_structure_fanwidth3diff_252d_slope_v074_signal,
    f01ts_f01_trend_structure_pxemavol21ewmv_21d_slope_v075_signal,
    f01ts_f01_trend_structure_emavel21diff_21d_slope_v076_signal,
    f01ts_f01_trend_structure_emavel126slreg_126d_slope_v077_signal,
    f01ts_f01_trend_structure_maslope21ewmv_21d_slope_v078_signal,
    f01ts_f01_trend_structure_maslope504slreg_504d_slope_v079_signal,
    f01ts_f01_trend_structure_ersign42diff_42d_slope_v080_signal,
    f01ts_f01_trend_structure_ersign189znrm_189d_slope_v081_signal,
    f01ts_f01_trend_structure_distterm2163ewmv_63d_slope_v082_signal,
    f01ts_f01_trend_structure_distterm63126znrm_126d_slope_v083_signal,
    f01ts_f01_trend_structure_distterm126252diff_252d_slope_v084_signal,
    f01ts_f01_trend_structure_slopeterm2163znrm_63d_slope_v085_signal,
    f01ts_f01_trend_structure_slopeterm63126ewmv_126d_slope_v086_signal,
    f01ts_f01_trend_structure_slopeterm63252slreg_252d_slope_v087_signal,
    f01ts_f01_trend_structure_slopeterm126252diff_252d_slope_v088_signal,
    f01ts_f01_trend_structure_emasmadiv252znrm_252d_slope_v089_signal,
    f01ts_f01_trend_structure_pxma5ewmv_5d_slope_v090_signal,
    f01ts_f01_trend_structure_pxma42slreg_42d_slope_v091_signal,
    f01ts_f01_trend_structure_pxema42diff_42d_slope_v092_signal,
    f01ts_f01_trend_structure_slope42diff_42d_slope_v093_signal,
    f01ts_f01_trend_structure_slope189znrm_189d_slope_v094_signal,
    f01ts_f01_trend_structure_slope378ewmv_378d_slope_v095_signal,
    f01ts_f01_trend_structure_r2qual42slreg_42d_slope_v096_signal,
    f01ts_f01_trend_structure_r2qual189diff_189d_slope_v097_signal,
    f01ts_f01_trend_structure_snr63slreg_63d_slope_v098_signal,
    f01ts_f01_trend_structure_abovefrac21slreg_21d_slope_v099_signal,
    f01ts_f01_trend_structure_abovefrac42diff_42d_slope_v100_signal,
    f01ts_f01_trend_structure_maspr21v126znrm_126d_slope_v101_signal,
    f01ts_f01_trend_structure_maband63ewmv_63d_slope_v102_signal,
    f01ts_f01_trend_structure_macdhist1226slreg_26d_slope_v103_signal,
    f01ts_f01_trend_structure_stack52163diff_63d_slope_v104_signal,
    f01ts_f01_trend_structure_logdistma126znrm_126d_slope_v105_signal,
    f01ts_f01_trend_structure_erpure63slreg_63d_slope_v106_signal,
    f01ts_f01_trend_structure_erpure126diff_126d_slope_v107_signal,
    f01ts_f01_trend_structure_dualtrend21252znrm_252d_slope_v108_signal,
    f01ts_f01_trend_structure_macdlog63252znrm_252d_slope_v109_signal,
    f01ts_f01_trend_structure_erpure21diff_21d_slope_v110_signal,
    f01ts_f01_trend_structure_chanpos63znrm_63d_slope_v111_signal,
    f01ts_f01_trend_structure_chanpos126ewmv_126d_slope_v112_signal,
    f01ts_f01_trend_structure_chanpos252slreg_252d_slope_v113_signal,
    f01ts_f01_trend_structure_pxmatanh5diff_5d_slope_v114_signal,
    f01ts_f01_trend_structure_pxmatanh42znrm_42d_slope_v115_signal,
    f01ts_f01_trend_structure_pxmatanh189ewmv_189d_slope_v116_signal,
    f01ts_f01_trend_structure_stack21126252ewmv_252d_slope_v117_signal,
    f01ts_f01_trend_structure_maband504slreg_504d_slope_v118_signal,
    f01ts_f01_trend_structure_smoothslope63znrm_63d_slope_v119_signal,
    f01ts_f01_trend_structure_slopet42ewmv_42d_slope_v120_signal,
    f01ts_f01_trend_structure_slopet189slreg_189d_slope_v121_signal,
    f01ts_f01_trend_structure_distterm542diff_42d_slope_v122_signal,
    f01ts_f01_trend_structure_distterm21189znrm_189d_slope_v123_signal,
    f01ts_f01_trend_structure_pxmavol21slreg_21d_slope_v124_signal,
    f01ts_f01_trend_structure_abovefrac189slreg_189d_slope_v125_signal,
    f01ts_f01_trend_structure_abovefrac504diff_504d_slope_v126_signal,
    f01ts_f01_trend_structure_emasmadiv21znrm_21d_slope_v127_signal,
    f01ts_f01_trend_structure_maspr42189ewmv_189d_slope_v128_signal,
    f01ts_f01_trend_structure_slope504slreg_504d_slope_v129_signal,
    f01ts_f01_trend_structure_erpure252znrm_252d_slope_v130_signal,
    f01ts_f01_trend_structure_emasmadiv42ewmv_42d_slope_v131_signal,
    f01ts_f01_trend_structure_distterm42126slreg_126d_slope_v132_signal,
    f01ts_f01_trend_structure_pxmatanh378diff_378d_slope_v133_signal,
    f01ts_f01_trend_structure_pxmasm21znrm_21d_slope_v134_signal,
    f01ts_f01_trend_structure_pxmasm42ewmv_42d_slope_v135_signal,
    f01ts_f01_trend_structure_pxmasm189slreg_189d_slope_v136_signal,
    f01ts_f01_trend_structure_logdistma504diff_504d_slope_v137_signal,
    f01ts_f01_trend_structure_slope10slreg_10d_slope_v138_signal,
    f01ts_f01_trend_structure_slope32diff_32d_slope_v139_signal,
    f01ts_f01_trend_structure_slope95znrm_95d_slope_v140_signal,
    f01ts_f01_trend_structure_slope315ewmv_315d_slope_v141_signal,
    f01ts_f01_trend_structure_ersign32slreg_32d_slope_v142_signal,
    f01ts_f01_trend_structure_ersign95diff_95d_slope_v143_signal,
    f01ts_f01_trend_structure_ersign315znrm_315d_slope_v144_signal,
    f01ts_f01_trend_structure_maspr1063ewmv_63d_slope_v145_signal,
    f01ts_f01_trend_structure_maspr95378znrm_378d_slope_v146_signal,
    f01ts_f01_trend_structure_emaspr1042slreg_42d_slope_v147_signal,
    f01ts_f01_trend_structure_macdlog1063diff_63d_slope_v148_signal,
    f01ts_f01_trend_structure_maslope42znrm_42d_slope_v149_signal,
    f01ts_f01_trend_structure_maslope189slreg_189d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_TREND_STRUCTURE_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

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
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f01_trend_structure_2nd_derivatives_001_150_claude: %d features pass" % n_features)
