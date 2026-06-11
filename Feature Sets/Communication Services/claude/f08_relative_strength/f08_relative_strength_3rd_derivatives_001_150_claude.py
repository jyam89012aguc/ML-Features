import inspect
import numpy as np
import pandas as pd

# f08_relative_strength (f08rs) — jerk derivatives (001_150).
# Jerk = 2nd math derivative (acceleration) of a self-relative *RISK-ADJUSTED* strength base series. Each feature computes a
# risk-adjusted self-RS base inline (Sharpe / Sortino / Calmar / Martin / gain-to-pain /
# Sterling / Omega / time-above-water / ulcer / CVaR-adjusted / tail-ratio, all vs the stock's
# OWN history) then takes the 2nd difference (jerk) (window matched to the base window).
#   NOT efficiency ratio / Hurst / autocorrelation (f03); NOT raw ROC / momentum levels (f02);
#   NOT price-vs-MA / trend-slope-t-stat (f01).
# Single-series, inputs: closeadj only (>21d uses closeadj per SPEC).

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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _logret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _cumret(closeadj, w):
    return np.log(closeadj.replace(0, np.nan)) - np.log(closeadj.shift(w).replace(0, np.nan))


def _sharpe(closeadj, w):
    lr = _logret(closeadj)
    mu = lr.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = lr.rolling(w, min_periods=max(2, w // 2)).std()
    return mu / sd.replace(0, np.nan) * np.sqrt(252.0)


def _sortino(closeadj, w):
    lr = _logret(closeadj)
    mu = lr.rolling(w, min_periods=max(2, w // 2)).mean()
    down = lr.where(lr < 0, 0.0)
    dd = np.sqrt((down ** 2).rolling(w, min_periods=max(2, w // 2)).mean())
    return mu / dd.replace(0, np.nan) * np.sqrt(252.0)


def _underwater(closeadj, w):
    peak = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    return closeadj / peak.replace(0, np.nan) - 1.0


def _maxdd(closeadj, w):
    uw = _underwater(closeadj, w)
    return (-uw).rolling(w, min_periods=max(1, w // 2)).max()


def _avgdd(closeadj, w):
    uw = _underwater(closeadj, w)
    return (-uw).rolling(w, min_periods=max(1, w // 2)).mean()


def _ulcer(closeadj, w):
    uw = _underwater(closeadj, w)
    return np.sqrt((uw ** 2).rolling(w, min_periods=max(1, w // 2)).mean())


def _calmar(closeadj, w):
    return _cumret(closeadj, w) / _maxdd(closeadj, w).replace(0, np.nan)


def _martin(closeadj, w):
    return _cumret(closeadj, w) / _ulcer(closeadj, w).replace(0, np.nan)


def _sterling(closeadj, w):
    return _cumret(closeadj, w) / _avgdd(closeadj, w).replace(0, np.nan)


def _gtp(closeadj, w):
    lr = _logret(closeadj)
    g = lr.rolling(w, min_periods=max(2, w // 2)).sum()
    pain = lr.clip(upper=0).abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return g / pain.replace(0, np.nan)


def _omega(closeadj, w):
    lr = _logret(closeadj)
    up = lr.clip(lower=0).rolling(w, min_periods=max(2, w // 2)).sum()
    dn = lr.clip(upper=0).abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return up / dn.replace(0, np.nan)


def _downdevadj(closeadj, w):
    lr = _logret(closeadj)
    down = lr.where(lr < 0, 0.0)
    dd = np.sqrt((down ** 2).rolling(w, min_periods=max(2, w // 2)).mean()) * np.sqrt(252.0)
    return _cumret(closeadj, w) / dd.replace(0, np.nan)


def _cvaradj(closeadj, w):
    lr = _logret(closeadj)
    cvar = (-lr).rolling(w, min_periods=max(2, w // 2)).quantile(0.95)
    return _cumret(closeadj, w) / cvar.replace(0, np.nan)


def _tailratio(closeadj, w):
    lr = _logret(closeadj)
    hi = lr.rolling(w, min_periods=max(2, w // 2)).quantile(0.95)
    lo = lr.rolling(w, min_periods=max(2, w // 2)).quantile(0.05)
    return hi / (-lo).replace(0, np.nan)


def _timeabovewater(closeadj, w):
    uw = _underwater(closeadj, w)
    near = (uw >= -0.005).astype(float).rolling(w, min_periods=max(2, w // 2)).mean()
    depth = (-uw).rolling(w, min_periods=max(2, w // 2)).mean()
    return near - 5.0 * depth


def _downshare(closeadj, w):
    lr = _logret(closeadj)
    dvar = (lr.where(lr < 0, 0.0) ** 2).rolling(w, min_periods=max(2, w // 2)).mean()
    tvar = (lr ** 2).rolling(w, min_periods=max(2, w // 2)).mean()
    return dvar / tvar.replace(0, np.nan) - 0.5


def _downdev_(closeadj, w):
    lr = _logret(closeadj)
    down = lr.where(lr < 0, 0.0)
    return np.sqrt((down ** 2).rolling(w, min_periods=max(2, w // 2)).mean()) * np.sqrt(252.0)


def _cdar(closeadj, w):
    uw = (-_underwater(closeadj, w))
    thr = uw.rolling(w, min_periods=max(2, w // 2)).quantile(0.75)
    above = (uw >= thr)
    tail_sum = (uw.where(above, 0.0)).rolling(w, min_periods=max(2, w // 2)).sum()
    tail_cnt = above.astype(float).rolling(w, min_periods=max(2, w // 2)).sum()
    return tail_sum / tail_cnt.replace(0, np.nan)


def _painratio(closeadj, w):
    return _cumret(closeadj, w) / _cdar(closeadj, w).replace(0, np.nan)



# jerk 'sharpe126' [raw]
def f08rs_f08_relative_strength_sharpe126raw_126d_jerk_v001_signal(closeadj):
    base = _sharpe(closeadj, 126)
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sharpe126' [rank]
def f08rs_f08_relative_strength_sharpe126rank_126d_jerk_v002_signal(closeadj):
    base = _sharpe(closeadj, 126)
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sharpe126' [ema]
def f08rs_f08_relative_strength_sharpe126ema_126d_jerk_v003_signal(closeadj):
    base = _sharpe(closeadj, 126)
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sharpe126' [tanh]
def f08rs_f08_relative_strength_sharpe126tanh_126d_jerk_v004_signal(closeadj):
    base = _sharpe(closeadj, 126)
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sharpe126' [sqz]
def f08rs_f08_relative_strength_sharpe126sqz_126d_jerk_v005_signal(closeadj):
    base = _sharpe(closeadj, 126)
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sortino504' [raw]
def f08rs_f08_relative_strength_sortino504raw_504d_jerk_v006_signal(closeadj):
    base = _sortino(closeadj, 504)
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sortino504' [rank]
def f08rs_f08_relative_strength_sortino504rank_504d_jerk_v007_signal(closeadj):
    base = _sortino(closeadj, 504)
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sortino504' [ema]
def f08rs_f08_relative_strength_sortino504ema_504d_jerk_v008_signal(closeadj):
    base = _sortino(closeadj, 504)
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sortino504' [tanh]
def f08rs_f08_relative_strength_sortino504tanh_504d_jerk_v009_signal(closeadj):
    base = _sortino(closeadj, 504)
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sortino504' [sqz]
def f08rs_f08_relative_strength_sortino504sqz_504d_jerk_v010_signal(closeadj):
    base = _sortino(closeadj, 504)
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'calmar252' [raw]
def f08rs_f08_relative_strength_calmar252raw_252d_jerk_v011_signal(closeadj):
    base = _calmar(closeadj, 252).clip(-20, 20)
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'calmar252' [rank]
def f08rs_f08_relative_strength_calmar252rank_252d_jerk_v012_signal(closeadj):
    base = _calmar(closeadj, 252).clip(-20, 20)
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'calmar252' [ema]
def f08rs_f08_relative_strength_calmar252ema_252d_jerk_v013_signal(closeadj):
    base = _calmar(closeadj, 252).clip(-20, 20)
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'calmar252' [tanh]
def f08rs_f08_relative_strength_calmar252tanh_252d_jerk_v014_signal(closeadj):
    base = _calmar(closeadj, 252).clip(-20, 20)
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'calmar252' [sqz]
def f08rs_f08_relative_strength_calmar252sqz_252d_jerk_v015_signal(closeadj):
    base = _calmar(closeadj, 252).clip(-20, 20)
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'martin504' [raw]
def f08rs_f08_relative_strength_martin504raw_504d_jerk_v016_signal(closeadj):
    base = _martin(closeadj, 504).clip(-80, 80)
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'martin504' [rank]
def f08rs_f08_relative_strength_martin504rank_504d_jerk_v017_signal(closeadj):
    base = _martin(closeadj, 504).clip(-80, 80)
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'martin504' [ema]
def f08rs_f08_relative_strength_martin504ema_504d_jerk_v018_signal(closeadj):
    base = _martin(closeadj, 504).clip(-80, 80)
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'martin504' [tanh]
def f08rs_f08_relative_strength_martin504tanh_504d_jerk_v019_signal(closeadj):
    base = _martin(closeadj, 504).clip(-80, 80)
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'martin504' [sqz]
def f08rs_f08_relative_strength_martin504sqz_504d_jerk_v020_signal(closeadj):
    base = _martin(closeadj, 504).clip(-80, 80)
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'gtp63' [raw]
def f08rs_f08_relative_strength_gtp63raw_63d_jerk_v021_signal(closeadj):
    base = _gtp(closeadj, 63).clip(-10, 10)
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'gtp63' [rank]
def f08rs_f08_relative_strength_gtp63rank_63d_jerk_v022_signal(closeadj):
    base = _gtp(closeadj, 63).clip(-10, 10)
    t = _rank(base, 252)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'gtp63' [ema]
def f08rs_f08_relative_strength_gtp63ema_63d_jerk_v023_signal(closeadj):
    base = _gtp(closeadj, 63).clip(-10, 10)
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'gtp63' [tanh]
def f08rs_f08_relative_strength_gtp63tanh_63d_jerk_v024_signal(closeadj):
    base = _gtp(closeadj, 63).clip(-10, 10)
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'gtp63' [sqz]
def f08rs_f08_relative_strength_gtp63sqz_63d_jerk_v025_signal(closeadj):
    base = _gtp(closeadj, 63).clip(-10, 10)
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'painratio252' [raw]
def f08rs_f08_relative_strength_painratio252raw_252d_jerk_v026_signal(closeadj):
    base = _painratio(closeadj, 252).clip(-60, 60)
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'painratio252' [rank]
def f08rs_f08_relative_strength_painratio252rank_252d_jerk_v027_signal(closeadj):
    base = _painratio(closeadj, 252).clip(-60, 60)
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'painratio252' [ema]
def f08rs_f08_relative_strength_painratio252ema_252d_jerk_v028_signal(closeadj):
    base = _painratio(closeadj, 252).clip(-60, 60)
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'painratio252' [tanh]
def f08rs_f08_relative_strength_painratio252tanh_252d_jerk_v029_signal(closeadj):
    base = _painratio(closeadj, 252).clip(-60, 60)
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'painratio252' [sqz]
def f08rs_f08_relative_strength_painratio252sqz_252d_jerk_v030_signal(closeadj):
    base = _painratio(closeadj, 252).clip(-60, 60)
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sharpesortdiff' [raw]
def f08rs_f08_relative_strength_sharpesortdiffraw_252d_jerk_v031_signal(closeadj):
    base = (_sharpe(closeadj, 252) - _sortino(closeadj, 252))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sharpesortdiff' [rank]
def f08rs_f08_relative_strength_sharpesortdiffrank_252d_jerk_v032_signal(closeadj):
    base = (_sharpe(closeadj, 252) - _sortino(closeadj, 252))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sharpesortdiff' [ema]
def f08rs_f08_relative_strength_sharpesortdiffema_252d_jerk_v033_signal(closeadj):
    base = (_sharpe(closeadj, 252) - _sortino(closeadj, 252))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sharpesortdiff' [tanh]
def f08rs_f08_relative_strength_sharpesortdifftanh_252d_jerk_v034_signal(closeadj):
    base = (_sharpe(closeadj, 252) - _sortino(closeadj, 252))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sharpesortdiff' [sqz]
def f08rs_f08_relative_strength_sharpesortdiffsqz_252d_jerk_v035_signal(closeadj):
    base = (_sharpe(closeadj, 252) - _sortino(closeadj, 252))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'calmsharpdiff' [raw]
def f08rs_f08_relative_strength_calmsharpdiffraw_252d_jerk_v036_signal(closeadj):
    base = (_rank(_calmar(closeadj, 252), 504) - _rank(_sharpe(closeadj, 252), 504))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'calmsharpdiff' [rank]
def f08rs_f08_relative_strength_calmsharpdiffrank_252d_jerk_v037_signal(closeadj):
    base = (_rank(_calmar(closeadj, 252), 504) - _rank(_sharpe(closeadj, 252), 504))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'calmsharpdiff' [ema]
def f08rs_f08_relative_strength_calmsharpdiffema_252d_jerk_v038_signal(closeadj):
    base = (_rank(_calmar(closeadj, 252), 504) - _rank(_sharpe(closeadj, 252), 504))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'calmsharpdiff' [tanh]
def f08rs_f08_relative_strength_calmsharpdifftanh_252d_jerk_v039_signal(closeadj):
    base = (_rank(_calmar(closeadj, 252), 504) - _rank(_sharpe(closeadj, 252), 504))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'calmsharpdiff' [sqz]
def f08rs_f08_relative_strength_calmsharpdiffsqz_252d_jerk_v040_signal(closeadj):
    base = (_rank(_calmar(closeadj, 252), 504) - _rank(_sharpe(closeadj, 252), 504))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'omegasharpdiff' [raw]
def f08rs_f08_relative_strength_omegasharpdiffraw_252d_jerk_v041_signal(closeadj):
    base = (_rank(_omega(closeadj, 252), 504) - _rank(_sharpe(closeadj, 252), 504))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'omegasharpdiff' [rank]
def f08rs_f08_relative_strength_omegasharpdiffrank_252d_jerk_v042_signal(closeadj):
    base = (_rank(_omega(closeadj, 252), 504) - _rank(_sharpe(closeadj, 252), 504))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'omegasharpdiff' [ema]
def f08rs_f08_relative_strength_omegasharpdiffema_252d_jerk_v043_signal(closeadj):
    base = (_rank(_omega(closeadj, 252), 504) - _rank(_sharpe(closeadj, 252), 504))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'omegasharpdiff' [tanh]
def f08rs_f08_relative_strength_omegasharpdifftanh_252d_jerk_v044_signal(closeadj):
    base = (_rank(_omega(closeadj, 252), 504) - _rank(_sharpe(closeadj, 252), 504))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'omegasharpdiff' [sqz]
def f08rs_f08_relative_strength_omegasharpdiffsqz_252d_jerk_v045_signal(closeadj):
    base = (_rank(_omega(closeadj, 252), 504) - _rank(_sharpe(closeadj, 252), 504))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'martsortdiff' [raw]
def f08rs_f08_relative_strength_martsortdiffraw_252d_jerk_v046_signal(closeadj):
    base = (_rank(_martin(closeadj, 252), 504) - _rank(_sortino(closeadj, 252), 504))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'martsortdiff' [rank]
def f08rs_f08_relative_strength_martsortdiffrank_252d_jerk_v047_signal(closeadj):
    base = (_rank(_martin(closeadj, 252), 504) - _rank(_sortino(closeadj, 252), 504))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'martsortdiff' [ema]
def f08rs_f08_relative_strength_martsortdiffema_252d_jerk_v048_signal(closeadj):
    base = (_rank(_martin(closeadj, 252), 504) - _rank(_sortino(closeadj, 252), 504))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'martsortdiff' [tanh]
def f08rs_f08_relative_strength_martsortdifftanh_252d_jerk_v049_signal(closeadj):
    base = (_rank(_martin(closeadj, 252), 504) - _rank(_sortino(closeadj, 252), 504))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'martsortdiff' [sqz]
def f08rs_f08_relative_strength_martsortdiffsqz_252d_jerk_v050_signal(closeadj):
    base = (_rank(_martin(closeadj, 252), 504) - _rank(_sortino(closeadj, 252), 504))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sterlcalmdiff' [raw]
def f08rs_f08_relative_strength_sterlcalmdiffraw_252d_jerk_v051_signal(closeadj):
    base = (_rank(_sterling(closeadj, 252), 504) - _rank(_calmar(closeadj, 252), 504))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sterlcalmdiff' [rank]
def f08rs_f08_relative_strength_sterlcalmdiffrank_252d_jerk_v052_signal(closeadj):
    base = (_rank(_sterling(closeadj, 252), 504) - _rank(_calmar(closeadj, 252), 504))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sterlcalmdiff' [ema]
def f08rs_f08_relative_strength_sterlcalmdiffema_252d_jerk_v053_signal(closeadj):
    base = (_rank(_sterling(closeadj, 252), 504) - _rank(_calmar(closeadj, 252), 504))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sterlcalmdiff' [tanh]
def f08rs_f08_relative_strength_sterlcalmdifftanh_252d_jerk_v054_signal(closeadj):
    base = (_rank(_sterling(closeadj, 252), 504) - _rank(_calmar(closeadj, 252), 504))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sterlcalmdiff' [sqz]
def f08rs_f08_relative_strength_sterlcalmdiffsqz_252d_jerk_v055_signal(closeadj):
    base = (_rank(_sterling(closeadj, 252), 504) - _rank(_calmar(closeadj, 252), 504))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'cvarsortdiff' [raw]
def f08rs_f08_relative_strength_cvarsortdiffraw_252d_jerk_v056_signal(closeadj):
    base = (_rank(_cvaradj(closeadj, 252), 504) - _rank(_sortino(closeadj, 252), 504))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'cvarsortdiff' [rank]
def f08rs_f08_relative_strength_cvarsortdiffrank_252d_jerk_v057_signal(closeadj):
    base = (_rank(_cvaradj(closeadj, 252), 504) - _rank(_sortino(closeadj, 252), 504))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'cvarsortdiff' [ema]
def f08rs_f08_relative_strength_cvarsortdiffema_252d_jerk_v058_signal(closeadj):
    base = (_rank(_cvaradj(closeadj, 252), 504) - _rank(_sortino(closeadj, 252), 504))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'cvarsortdiff' [tanh]
def f08rs_f08_relative_strength_cvarsortdifftanh_252d_jerk_v059_signal(closeadj):
    base = (_rank(_cvaradj(closeadj, 252), 504) - _rank(_sortino(closeadj, 252), 504))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'cvarsortdiff' [sqz]
def f08rs_f08_relative_strength_cvarsortdiffsqz_252d_jerk_v060_signal(closeadj):
    base = (_rank(_cvaradj(closeadj, 252), 504) - _rank(_sortino(closeadj, 252), 504))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tailomegadiff' [raw]
def f08rs_f08_relative_strength_tailomegadiffraw_252d_jerk_v061_signal(closeadj):
    base = (_rank(_tailratio(closeadj, 252), 504) - _rank(_omega(closeadj, 252), 504))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tailomegadiff' [rank]
def f08rs_f08_relative_strength_tailomegadiffrank_252d_jerk_v062_signal(closeadj):
    base = (_rank(_tailratio(closeadj, 252), 504) - _rank(_omega(closeadj, 252), 504))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tailomegadiff' [ema]
def f08rs_f08_relative_strength_tailomegadiffema_252d_jerk_v063_signal(closeadj):
    base = (_rank(_tailratio(closeadj, 252), 504) - _rank(_omega(closeadj, 252), 504))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tailomegadiff' [tanh]
def f08rs_f08_relative_strength_tailomegadifftanh_252d_jerk_v064_signal(closeadj):
    base = (_rank(_tailratio(closeadj, 252), 504) - _rank(_omega(closeadj, 252), 504))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tailomegadiff' [sqz]
def f08rs_f08_relative_strength_tailomegadiffsqz_252d_jerk_v065_signal(closeadj):
    base = (_rank(_tailratio(closeadj, 252), 504) - _rank(_omega(closeadj, 252), 504))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tawsharpediff' [raw]
def f08rs_f08_relative_strength_tawsharpediffraw_252d_jerk_v066_signal(closeadj):
    base = (_rank(_timeabovewater(closeadj, 252), 504) - _rank(_sharpe(closeadj, 252), 504))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tawsharpediff' [rank]
def f08rs_f08_relative_strength_tawsharpediffrank_252d_jerk_v067_signal(closeadj):
    base = (_rank(_timeabovewater(closeadj, 252), 504) - _rank(_sharpe(closeadj, 252), 504))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tawsharpediff' [ema]
def f08rs_f08_relative_strength_tawsharpediffema_252d_jerk_v068_signal(closeadj):
    base = (_rank(_timeabovewater(closeadj, 252), 504) - _rank(_sharpe(closeadj, 252), 504))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tawsharpediff' [tanh]
def f08rs_f08_relative_strength_tawsharpedifftanh_252d_jerk_v069_signal(closeadj):
    base = (_rank(_timeabovewater(closeadj, 252), 504) - _rank(_sharpe(closeadj, 252), 504))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tawsharpediff' [sqz]
def f08rs_f08_relative_strength_tawsharpediffsqz_252d_jerk_v070_signal(closeadj):
    base = (_rank(_timeabovewater(closeadj, 252), 504) - _rank(_sharpe(closeadj, 252), 504))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sterltawdiff' [raw]
def f08rs_f08_relative_strength_sterltawdiffraw_252d_jerk_v071_signal(closeadj):
    base = (_rank(_sterling(closeadj, 252), 504) - _rank(_timeabovewater(closeadj, 252), 504))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sterltawdiff' [rank]
def f08rs_f08_relative_strength_sterltawdiffrank_252d_jerk_v072_signal(closeadj):
    base = (_rank(_sterling(closeadj, 252), 504) - _rank(_timeabovewater(closeadj, 252), 504))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sterltawdiff' [ema]
def f08rs_f08_relative_strength_sterltawdiffema_252d_jerk_v073_signal(closeadj):
    base = (_rank(_sterling(closeadj, 252), 504) - _rank(_timeabovewater(closeadj, 252), 504))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sterltawdiff' [tanh]
def f08rs_f08_relative_strength_sterltawdifftanh_252d_jerk_v074_signal(closeadj):
    base = (_rank(_sterling(closeadj, 252), 504) - _rank(_timeabovewater(closeadj, 252), 504))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sterltawdiff' [sqz]
def f08rs_f08_relative_strength_sterltawdiffsqz_252d_jerk_v075_signal(closeadj):
    base = (_rank(_sterling(closeadj, 252), 504) - _rank(_timeabovewater(closeadj, 252), 504))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'taw252' [raw]
def f08rs_f08_relative_strength_taw252raw_252d_jerk_v076_signal(closeadj):
    base = _timeabovewater(closeadj, 252)
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'taw252' [rank]
def f08rs_f08_relative_strength_taw252rank_252d_jerk_v077_signal(closeadj):
    base = _timeabovewater(closeadj, 252)
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'taw252' [ema]
def f08rs_f08_relative_strength_taw252ema_252d_jerk_v078_signal(closeadj):
    base = _timeabovewater(closeadj, 252)
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'taw252' [tanh]
def f08rs_f08_relative_strength_taw252tanh_252d_jerk_v079_signal(closeadj):
    base = _timeabovewater(closeadj, 252)
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'taw252' [sqz]
def f08rs_f08_relative_strength_taw252sqz_252d_jerk_v080_signal(closeadj):
    base = _timeabovewater(closeadj, 252)
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'taw126' [raw]
def f08rs_f08_relative_strength_taw126raw_126d_jerk_v081_signal(closeadj):
    base = _timeabovewater(closeadj, 126)
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'taw126' [rank]
def f08rs_f08_relative_strength_taw126rank_126d_jerk_v082_signal(closeadj):
    base = _timeabovewater(closeadj, 126)
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'taw126' [ema]
def f08rs_f08_relative_strength_taw126ema_126d_jerk_v083_signal(closeadj):
    base = _timeabovewater(closeadj, 126)
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'taw126' [tanh]
def f08rs_f08_relative_strength_taw126tanh_126d_jerk_v084_signal(closeadj):
    base = _timeabovewater(closeadj, 126)
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'taw126' [sqz]
def f08rs_f08_relative_strength_taw126sqz_126d_jerk_v085_signal(closeadj):
    base = _timeabovewater(closeadj, 126)
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'taw504' [raw]
def f08rs_f08_relative_strength_taw504raw_504d_jerk_v086_signal(closeadj):
    base = _timeabovewater(closeadj, 504)
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'taw504' [rank]
def f08rs_f08_relative_strength_taw504rank_504d_jerk_v087_signal(closeadj):
    base = _timeabovewater(closeadj, 504)
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'taw504' [ema]
def f08rs_f08_relative_strength_taw504ema_504d_jerk_v088_signal(closeadj):
    base = _timeabovewater(closeadj, 504)
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'taw504' [tanh]
def f08rs_f08_relative_strength_taw504tanh_504d_jerk_v089_signal(closeadj):
    base = _timeabovewater(closeadj, 504)
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'taw504' [sqz]
def f08rs_f08_relative_strength_taw504sqz_504d_jerk_v090_signal(closeadj):
    base = _timeabovewater(closeadj, 504)
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tailratio252' [raw]
def f08rs_f08_relative_strength_tailratio252raw_252d_jerk_v091_signal(closeadj):
    base = (_tailratio(closeadj, 252).clip(0, 5) - 1.0)
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tailratio252' [rank]
def f08rs_f08_relative_strength_tailratio252rank_252d_jerk_v092_signal(closeadj):
    base = (_tailratio(closeadj, 252).clip(0, 5) - 1.0)
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tailratio252' [ema]
def f08rs_f08_relative_strength_tailratio252ema_252d_jerk_v093_signal(closeadj):
    base = (_tailratio(closeadj, 252).clip(0, 5) - 1.0)
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tailratio252' [tanh]
def f08rs_f08_relative_strength_tailratio252tanh_252d_jerk_v094_signal(closeadj):
    base = (_tailratio(closeadj, 252).clip(0, 5) - 1.0)
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tailratio252' [sqz]
def f08rs_f08_relative_strength_tailratio252sqz_252d_jerk_v095_signal(closeadj):
    base = (_tailratio(closeadj, 252).clip(0, 5) - 1.0)
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'downshare252' [raw]
def f08rs_f08_relative_strength_downshare252raw_252d_jerk_v096_signal(closeadj):
    base = _downshare(closeadj, 252)
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'downshare252' [rank]
def f08rs_f08_relative_strength_downshare252rank_252d_jerk_v097_signal(closeadj):
    base = _downshare(closeadj, 252)
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'downshare252' [ema]
def f08rs_f08_relative_strength_downshare252ema_252d_jerk_v098_signal(closeadj):
    base = _downshare(closeadj, 252)
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'downshare252' [tanh]
def f08rs_f08_relative_strength_downshare252tanh_252d_jerk_v099_signal(closeadj):
    base = _downshare(closeadj, 252)
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'downshare252' [sqz]
def f08rs_f08_relative_strength_downshare252sqz_252d_jerk_v100_signal(closeadj):
    base = _downshare(closeadj, 252)
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'ulcerstr252' [raw]
def f08rs_f08_relative_strength_ulcerstr252raw_252d_jerk_v101_signal(closeadj):
    base = (-_rank(_ulcer(closeadj, 252), 504))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'ulcerstr252' [rank]
def f08rs_f08_relative_strength_ulcerstr252rank_252d_jerk_v102_signal(closeadj):
    base = (-_rank(_ulcer(closeadj, 252), 504))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'ulcerstr252' [ema]
def f08rs_f08_relative_strength_ulcerstr252ema_252d_jerk_v103_signal(closeadj):
    base = (-_rank(_ulcer(closeadj, 252), 504))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'ulcerstr252' [tanh]
def f08rs_f08_relative_strength_ulcerstr252tanh_252d_jerk_v104_signal(closeadj):
    base = (-_rank(_ulcer(closeadj, 252), 504))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'ulcerstr252' [sqz]
def f08rs_f08_relative_strength_ulcerstr252sqz_252d_jerk_v105_signal(closeadj):
    base = (-_rank(_ulcer(closeadj, 252), 504))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'avgddstr504' [raw]
def f08rs_f08_relative_strength_avgddstr504raw_504d_jerk_v106_signal(closeadj):
    base = (-_rank(_avgdd(closeadj, 504), 504))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'avgddstr504' [rank]
def f08rs_f08_relative_strength_avgddstr504rank_504d_jerk_v107_signal(closeadj):
    base = (-_rank(_avgdd(closeadj, 504), 504))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'avgddstr504' [ema]
def f08rs_f08_relative_strength_avgddstr504ema_504d_jerk_v108_signal(closeadj):
    base = (-_rank(_avgdd(closeadj, 504), 504))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'avgddstr504' [tanh]
def f08rs_f08_relative_strength_avgddstr504tanh_504d_jerk_v109_signal(closeadj):
    base = (-_rank(_avgdd(closeadj, 504), 504))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'avgddstr504' [sqz]
def f08rs_f08_relative_strength_avgddstr504sqz_504d_jerk_v110_signal(closeadj):
    base = (-_rank(_avgdd(closeadj, 504), 504))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'downdevstr252' [raw]
def f08rs_f08_relative_strength_downdevstr252raw_252d_jerk_v111_signal(closeadj):
    base = (-_rank(_downdev_(closeadj, 252), 504))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'downdevstr252' [rank]
def f08rs_f08_relative_strength_downdevstr252rank_252d_jerk_v112_signal(closeadj):
    base = (-_rank(_downdev_(closeadj, 252), 504))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'downdevstr252' [ema]
def f08rs_f08_relative_strength_downdevstr252ema_252d_jerk_v113_signal(closeadj):
    base = (-_rank(_downdev_(closeadj, 252), 504))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'downdevstr252' [tanh]
def f08rs_f08_relative_strength_downdevstr252tanh_252d_jerk_v114_signal(closeadj):
    base = (-_rank(_downdev_(closeadj, 252), 504))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'downdevstr252' [sqz]
def f08rs_f08_relative_strength_downdevstr252sqz_252d_jerk_v115_signal(closeadj):
    base = (-_rank(_downdev_(closeadj, 252), 504))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'recov252' [raw]
def f08rs_f08_relative_strength_recov252raw_252d_jerk_v116_signal(closeadj):
    base = (_underwater(closeadj, 252) - _underwater(closeadj, 252).rolling(252, min_periods=126).min())
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'recov252' [rank]
def f08rs_f08_relative_strength_recov252rank_252d_jerk_v117_signal(closeadj):
    base = (_underwater(closeadj, 252) - _underwater(closeadj, 252).rolling(252, min_periods=126).min())
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'recov252' [ema]
def f08rs_f08_relative_strength_recov252ema_252d_jerk_v118_signal(closeadj):
    base = (_underwater(closeadj, 252) - _underwater(closeadj, 252).rolling(252, min_periods=126).min())
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'recov252' [tanh]
def f08rs_f08_relative_strength_recov252tanh_252d_jerk_v119_signal(closeadj):
    base = (_underwater(closeadj, 252) - _underwater(closeadj, 252).rolling(252, min_periods=126).min())
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'recov252' [sqz]
def f08rs_f08_relative_strength_recov252sqz_252d_jerk_v120_signal(closeadj):
    base = (_underwater(closeadj, 252) - _underwater(closeadj, 252).rolling(252, min_periods=126).min())
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'maxddvol252' [raw]
def f08rs_f08_relative_strength_maxddvol252raw_252d_jerk_v121_signal(closeadj):
    base = (-_maxdd(closeadj, 252) / (_logret(closeadj).rolling(63, min_periods=21).std() * np.sqrt(252.0)).replace(0, np.nan))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'maxddvol252' [rank]
def f08rs_f08_relative_strength_maxddvol252rank_252d_jerk_v122_signal(closeadj):
    base = (-_maxdd(closeadj, 252) / (_logret(closeadj).rolling(63, min_periods=21).std() * np.sqrt(252.0)).replace(0, np.nan))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'maxddvol252' [ema]
def f08rs_f08_relative_strength_maxddvol252ema_252d_jerk_v123_signal(closeadj):
    base = (-_maxdd(closeadj, 252) / (_logret(closeadj).rolling(63, min_periods=21).std() * np.sqrt(252.0)).replace(0, np.nan))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'maxddvol252' [tanh]
def f08rs_f08_relative_strength_maxddvol252tanh_252d_jerk_v124_signal(closeadj):
    base = (-_maxdd(closeadj, 252) / (_logret(closeadj).rolling(63, min_periods=21).std() * np.sqrt(252.0)).replace(0, np.nan))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'maxddvol252' [sqz]
def f08rs_f08_relative_strength_maxddvol252sqz_252d_jerk_v125_signal(closeadj):
    base = (-_maxdd(closeadj, 252) / (_logret(closeadj).rolling(63, min_periods=21).std() * np.sqrt(252.0)).replace(0, np.nan))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'omegasortdiff126' [raw]
def f08rs_f08_relative_strength_omegasortdiff126raw_126d_jerk_v126_signal(closeadj):
    base = (_rank(_omega(closeadj, 126), 504) - _rank(_sortino(closeadj, 126), 504))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'omegasortdiff126' [rank]
def f08rs_f08_relative_strength_omegasortdiff126rank_126d_jerk_v127_signal(closeadj):
    base = (_rank(_omega(closeadj, 126), 504) - _rank(_sortino(closeadj, 126), 504))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'omegasortdiff126' [ema]
def f08rs_f08_relative_strength_omegasortdiff126ema_126d_jerk_v128_signal(closeadj):
    base = (_rank(_omega(closeadj, 126), 504) - _rank(_sortino(closeadj, 126), 504))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'omegasortdiff126' [tanh]
def f08rs_f08_relative_strength_omegasortdiff126tanh_126d_jerk_v129_signal(closeadj):
    base = (_rank(_omega(closeadj, 126), 504) - _rank(_sortino(closeadj, 126), 504))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'omegasortdiff126' [sqz]
def f08rs_f08_relative_strength_omegasortdiff126sqz_126d_jerk_v130_signal(closeadj):
    base = (_rank(_omega(closeadj, 126), 504) - _rank(_sortino(closeadj, 126), 504))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'painsterldiff' [raw]
def f08rs_f08_relative_strength_painsterldiffraw_252d_jerk_v131_signal(closeadj):
    base = (_rank(_painratio(closeadj, 252), 504) - _rank(_sterling(closeadj, 252), 504))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'painsterldiff' [rank]
def f08rs_f08_relative_strength_painsterldiffrank_252d_jerk_v132_signal(closeadj):
    base = (_rank(_painratio(closeadj, 252), 504) - _rank(_sterling(closeadj, 252), 504))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'painsterldiff' [ema]
def f08rs_f08_relative_strength_painsterldiffema_252d_jerk_v133_signal(closeadj):
    base = (_rank(_painratio(closeadj, 252), 504) - _rank(_sterling(closeadj, 252), 504))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'painsterldiff' [tanh]
def f08rs_f08_relative_strength_painsterldifftanh_252d_jerk_v134_signal(closeadj):
    base = (_rank(_painratio(closeadj, 252), 504) - _rank(_sterling(closeadj, 252), 504))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'painsterldiff' [sqz]
def f08rs_f08_relative_strength_painsterldiffsqz_252d_jerk_v135_signal(closeadj):
    base = (_rank(_painratio(closeadj, 252), 504) - _rank(_sterling(closeadj, 252), 504))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'cvarcalmdiff504' [raw]
def f08rs_f08_relative_strength_cvarcalmdiff504raw_504d_jerk_v136_signal(closeadj):
    base = (_rank(_cvaradj(closeadj, 504), 504) - _rank(_calmar(closeadj, 504), 504))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'cvarcalmdiff504' [rank]
def f08rs_f08_relative_strength_cvarcalmdiff504rank_504d_jerk_v137_signal(closeadj):
    base = (_rank(_cvaradj(closeadj, 504), 504) - _rank(_calmar(closeadj, 504), 504))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'cvarcalmdiff504' [ema]
def f08rs_f08_relative_strength_cvarcalmdiff504ema_504d_jerk_v138_signal(closeadj):
    base = (_rank(_cvaradj(closeadj, 504), 504) - _rank(_calmar(closeadj, 504), 504))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'cvarcalmdiff504' [tanh]
def f08rs_f08_relative_strength_cvarcalmdiff504tanh_504d_jerk_v139_signal(closeadj):
    base = (_rank(_cvaradj(closeadj, 504), 504) - _rank(_calmar(closeadj, 504), 504))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'cvarcalmdiff504' [sqz]
def f08rs_f08_relative_strength_cvarcalmdiff504sqz_504d_jerk_v140_signal(closeadj):
    base = (_rank(_cvaradj(closeadj, 504), 504) - _rank(_calmar(closeadj, 504), 504))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sharpedeep504' [raw]
def f08rs_f08_relative_strength_sharpedeep504raw_504d_jerk_v141_signal(closeadj):
    base = _rank(_sharpe(closeadj, 504), 504)
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sharpedeep504' [rank]
def f08rs_f08_relative_strength_sharpedeep504rank_504d_jerk_v142_signal(closeadj):
    base = _rank(_sharpe(closeadj, 504), 504)
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sharpedeep504' [ema]
def f08rs_f08_relative_strength_sharpedeep504ema_504d_jerk_v143_signal(closeadj):
    base = _rank(_sharpe(closeadj, 504), 504)
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sharpedeep504' [tanh]
def f08rs_f08_relative_strength_sharpedeep504tanh_504d_jerk_v144_signal(closeadj):
    base = _rank(_sharpe(closeadj, 504), 504)
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'sharpedeep504' [sqz]
def f08rs_f08_relative_strength_sharpedeep504sqz_504d_jerk_v145_signal(closeadj):
    base = _rank(_sharpe(closeadj, 504), 504)
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tawcalmdiff' [raw]
def f08rs_f08_relative_strength_tawcalmdiffraw_252d_jerk_v146_signal(closeadj):
    base = (_rank(_timeabovewater(closeadj, 252), 504) - _rank(_calmar(closeadj, 252), 504))
    t = base
    result = (t) - 2.0 * (t).shift(11) + (t).shift(22)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tawcalmdiff' [rank]
def f08rs_f08_relative_strength_tawcalmdiffrank_252d_jerk_v147_signal(closeadj):
    base = (_rank(_timeabovewater(closeadj, 252), 504) - _rank(_calmar(closeadj, 252), 504))
    t = _rank(base, 504)
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tawcalmdiff' [ema]
def f08rs_f08_relative_strength_tawcalmdiffema_252d_jerk_v148_signal(closeadj):
    base = (_rank(_timeabovewater(closeadj, 252), 504) - _rank(_calmar(closeadj, 252), 504))
    t = base.ewm(span=10, min_periods=5).mean() - base.ewm(span=63, min_periods=21).mean()
    result = (t) - 2.0 * (t).shift(21) + (t).shift(42)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tawcalmdiff' [tanh]
def f08rs_f08_relative_strength_tawcalmdifftanh_252d_jerk_v149_signal(closeadj):
    base = (_rank(_timeabovewater(closeadj, 252), 504) - _rank(_calmar(closeadj, 252), 504))
    t = np.tanh(_z(base, 126))
    result = (t) - 2.0 * (t).shift(31) + (t).shift(62)
    return result.replace([np.inf, -np.inf], np.nan)

# jerk 'tawcalmdiff' [sqz]
def f08rs_f08_relative_strength_tawcalmdiffsqz_252d_jerk_v150_signal(closeadj):
    base = (_rank(_timeabovewater(closeadj, 252), 504) - _rank(_calmar(closeadj, 252), 504))
    t = np.sign(_z(base, 252)) * np.sqrt(_z(base, 252).abs())
    result = (t) - 2.0 * (t).shift(16) + (t).shift(32)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08rs_f08_relative_strength_sharpe126raw_126d_jerk_v001_signal,
    f08rs_f08_relative_strength_sharpe126rank_126d_jerk_v002_signal,
    f08rs_f08_relative_strength_sharpe126ema_126d_jerk_v003_signal,
    f08rs_f08_relative_strength_sharpe126tanh_126d_jerk_v004_signal,
    f08rs_f08_relative_strength_sharpe126sqz_126d_jerk_v005_signal,
    f08rs_f08_relative_strength_sortino504raw_504d_jerk_v006_signal,
    f08rs_f08_relative_strength_sortino504rank_504d_jerk_v007_signal,
    f08rs_f08_relative_strength_sortino504ema_504d_jerk_v008_signal,
    f08rs_f08_relative_strength_sortino504tanh_504d_jerk_v009_signal,
    f08rs_f08_relative_strength_sortino504sqz_504d_jerk_v010_signal,
    f08rs_f08_relative_strength_calmar252raw_252d_jerk_v011_signal,
    f08rs_f08_relative_strength_calmar252rank_252d_jerk_v012_signal,
    f08rs_f08_relative_strength_calmar252ema_252d_jerk_v013_signal,
    f08rs_f08_relative_strength_calmar252tanh_252d_jerk_v014_signal,
    f08rs_f08_relative_strength_calmar252sqz_252d_jerk_v015_signal,
    f08rs_f08_relative_strength_martin504raw_504d_jerk_v016_signal,
    f08rs_f08_relative_strength_martin504rank_504d_jerk_v017_signal,
    f08rs_f08_relative_strength_martin504ema_504d_jerk_v018_signal,
    f08rs_f08_relative_strength_martin504tanh_504d_jerk_v019_signal,
    f08rs_f08_relative_strength_martin504sqz_504d_jerk_v020_signal,
    f08rs_f08_relative_strength_gtp63raw_63d_jerk_v021_signal,
    f08rs_f08_relative_strength_gtp63rank_63d_jerk_v022_signal,
    f08rs_f08_relative_strength_gtp63ema_63d_jerk_v023_signal,
    f08rs_f08_relative_strength_gtp63tanh_63d_jerk_v024_signal,
    f08rs_f08_relative_strength_gtp63sqz_63d_jerk_v025_signal,
    f08rs_f08_relative_strength_painratio252raw_252d_jerk_v026_signal,
    f08rs_f08_relative_strength_painratio252rank_252d_jerk_v027_signal,
    f08rs_f08_relative_strength_painratio252ema_252d_jerk_v028_signal,
    f08rs_f08_relative_strength_painratio252tanh_252d_jerk_v029_signal,
    f08rs_f08_relative_strength_painratio252sqz_252d_jerk_v030_signal,
    f08rs_f08_relative_strength_sharpesortdiffraw_252d_jerk_v031_signal,
    f08rs_f08_relative_strength_sharpesortdiffrank_252d_jerk_v032_signal,
    f08rs_f08_relative_strength_sharpesortdiffema_252d_jerk_v033_signal,
    f08rs_f08_relative_strength_sharpesortdifftanh_252d_jerk_v034_signal,
    f08rs_f08_relative_strength_sharpesortdiffsqz_252d_jerk_v035_signal,
    f08rs_f08_relative_strength_calmsharpdiffraw_252d_jerk_v036_signal,
    f08rs_f08_relative_strength_calmsharpdiffrank_252d_jerk_v037_signal,
    f08rs_f08_relative_strength_calmsharpdiffema_252d_jerk_v038_signal,
    f08rs_f08_relative_strength_calmsharpdifftanh_252d_jerk_v039_signal,
    f08rs_f08_relative_strength_calmsharpdiffsqz_252d_jerk_v040_signal,
    f08rs_f08_relative_strength_omegasharpdiffraw_252d_jerk_v041_signal,
    f08rs_f08_relative_strength_omegasharpdiffrank_252d_jerk_v042_signal,
    f08rs_f08_relative_strength_omegasharpdiffema_252d_jerk_v043_signal,
    f08rs_f08_relative_strength_omegasharpdifftanh_252d_jerk_v044_signal,
    f08rs_f08_relative_strength_omegasharpdiffsqz_252d_jerk_v045_signal,
    f08rs_f08_relative_strength_martsortdiffraw_252d_jerk_v046_signal,
    f08rs_f08_relative_strength_martsortdiffrank_252d_jerk_v047_signal,
    f08rs_f08_relative_strength_martsortdiffema_252d_jerk_v048_signal,
    f08rs_f08_relative_strength_martsortdifftanh_252d_jerk_v049_signal,
    f08rs_f08_relative_strength_martsortdiffsqz_252d_jerk_v050_signal,
    f08rs_f08_relative_strength_sterlcalmdiffraw_252d_jerk_v051_signal,
    f08rs_f08_relative_strength_sterlcalmdiffrank_252d_jerk_v052_signal,
    f08rs_f08_relative_strength_sterlcalmdiffema_252d_jerk_v053_signal,
    f08rs_f08_relative_strength_sterlcalmdifftanh_252d_jerk_v054_signal,
    f08rs_f08_relative_strength_sterlcalmdiffsqz_252d_jerk_v055_signal,
    f08rs_f08_relative_strength_cvarsortdiffraw_252d_jerk_v056_signal,
    f08rs_f08_relative_strength_cvarsortdiffrank_252d_jerk_v057_signal,
    f08rs_f08_relative_strength_cvarsortdiffema_252d_jerk_v058_signal,
    f08rs_f08_relative_strength_cvarsortdifftanh_252d_jerk_v059_signal,
    f08rs_f08_relative_strength_cvarsortdiffsqz_252d_jerk_v060_signal,
    f08rs_f08_relative_strength_tailomegadiffraw_252d_jerk_v061_signal,
    f08rs_f08_relative_strength_tailomegadiffrank_252d_jerk_v062_signal,
    f08rs_f08_relative_strength_tailomegadiffema_252d_jerk_v063_signal,
    f08rs_f08_relative_strength_tailomegadifftanh_252d_jerk_v064_signal,
    f08rs_f08_relative_strength_tailomegadiffsqz_252d_jerk_v065_signal,
    f08rs_f08_relative_strength_tawsharpediffraw_252d_jerk_v066_signal,
    f08rs_f08_relative_strength_tawsharpediffrank_252d_jerk_v067_signal,
    f08rs_f08_relative_strength_tawsharpediffema_252d_jerk_v068_signal,
    f08rs_f08_relative_strength_tawsharpedifftanh_252d_jerk_v069_signal,
    f08rs_f08_relative_strength_tawsharpediffsqz_252d_jerk_v070_signal,
    f08rs_f08_relative_strength_sterltawdiffraw_252d_jerk_v071_signal,
    f08rs_f08_relative_strength_sterltawdiffrank_252d_jerk_v072_signal,
    f08rs_f08_relative_strength_sterltawdiffema_252d_jerk_v073_signal,
    f08rs_f08_relative_strength_sterltawdifftanh_252d_jerk_v074_signal,
    f08rs_f08_relative_strength_sterltawdiffsqz_252d_jerk_v075_signal,
    f08rs_f08_relative_strength_taw252raw_252d_jerk_v076_signal,
    f08rs_f08_relative_strength_taw252rank_252d_jerk_v077_signal,
    f08rs_f08_relative_strength_taw252ema_252d_jerk_v078_signal,
    f08rs_f08_relative_strength_taw252tanh_252d_jerk_v079_signal,
    f08rs_f08_relative_strength_taw252sqz_252d_jerk_v080_signal,
    f08rs_f08_relative_strength_taw126raw_126d_jerk_v081_signal,
    f08rs_f08_relative_strength_taw126rank_126d_jerk_v082_signal,
    f08rs_f08_relative_strength_taw126ema_126d_jerk_v083_signal,
    f08rs_f08_relative_strength_taw126tanh_126d_jerk_v084_signal,
    f08rs_f08_relative_strength_taw126sqz_126d_jerk_v085_signal,
    f08rs_f08_relative_strength_taw504raw_504d_jerk_v086_signal,
    f08rs_f08_relative_strength_taw504rank_504d_jerk_v087_signal,
    f08rs_f08_relative_strength_taw504ema_504d_jerk_v088_signal,
    f08rs_f08_relative_strength_taw504tanh_504d_jerk_v089_signal,
    f08rs_f08_relative_strength_taw504sqz_504d_jerk_v090_signal,
    f08rs_f08_relative_strength_tailratio252raw_252d_jerk_v091_signal,
    f08rs_f08_relative_strength_tailratio252rank_252d_jerk_v092_signal,
    f08rs_f08_relative_strength_tailratio252ema_252d_jerk_v093_signal,
    f08rs_f08_relative_strength_tailratio252tanh_252d_jerk_v094_signal,
    f08rs_f08_relative_strength_tailratio252sqz_252d_jerk_v095_signal,
    f08rs_f08_relative_strength_downshare252raw_252d_jerk_v096_signal,
    f08rs_f08_relative_strength_downshare252rank_252d_jerk_v097_signal,
    f08rs_f08_relative_strength_downshare252ema_252d_jerk_v098_signal,
    f08rs_f08_relative_strength_downshare252tanh_252d_jerk_v099_signal,
    f08rs_f08_relative_strength_downshare252sqz_252d_jerk_v100_signal,
    f08rs_f08_relative_strength_ulcerstr252raw_252d_jerk_v101_signal,
    f08rs_f08_relative_strength_ulcerstr252rank_252d_jerk_v102_signal,
    f08rs_f08_relative_strength_ulcerstr252ema_252d_jerk_v103_signal,
    f08rs_f08_relative_strength_ulcerstr252tanh_252d_jerk_v104_signal,
    f08rs_f08_relative_strength_ulcerstr252sqz_252d_jerk_v105_signal,
    f08rs_f08_relative_strength_avgddstr504raw_504d_jerk_v106_signal,
    f08rs_f08_relative_strength_avgddstr504rank_504d_jerk_v107_signal,
    f08rs_f08_relative_strength_avgddstr504ema_504d_jerk_v108_signal,
    f08rs_f08_relative_strength_avgddstr504tanh_504d_jerk_v109_signal,
    f08rs_f08_relative_strength_avgddstr504sqz_504d_jerk_v110_signal,
    f08rs_f08_relative_strength_downdevstr252raw_252d_jerk_v111_signal,
    f08rs_f08_relative_strength_downdevstr252rank_252d_jerk_v112_signal,
    f08rs_f08_relative_strength_downdevstr252ema_252d_jerk_v113_signal,
    f08rs_f08_relative_strength_downdevstr252tanh_252d_jerk_v114_signal,
    f08rs_f08_relative_strength_downdevstr252sqz_252d_jerk_v115_signal,
    f08rs_f08_relative_strength_recov252raw_252d_jerk_v116_signal,
    f08rs_f08_relative_strength_recov252rank_252d_jerk_v117_signal,
    f08rs_f08_relative_strength_recov252ema_252d_jerk_v118_signal,
    f08rs_f08_relative_strength_recov252tanh_252d_jerk_v119_signal,
    f08rs_f08_relative_strength_recov252sqz_252d_jerk_v120_signal,
    f08rs_f08_relative_strength_maxddvol252raw_252d_jerk_v121_signal,
    f08rs_f08_relative_strength_maxddvol252rank_252d_jerk_v122_signal,
    f08rs_f08_relative_strength_maxddvol252ema_252d_jerk_v123_signal,
    f08rs_f08_relative_strength_maxddvol252tanh_252d_jerk_v124_signal,
    f08rs_f08_relative_strength_maxddvol252sqz_252d_jerk_v125_signal,
    f08rs_f08_relative_strength_omegasortdiff126raw_126d_jerk_v126_signal,
    f08rs_f08_relative_strength_omegasortdiff126rank_126d_jerk_v127_signal,
    f08rs_f08_relative_strength_omegasortdiff126ema_126d_jerk_v128_signal,
    f08rs_f08_relative_strength_omegasortdiff126tanh_126d_jerk_v129_signal,
    f08rs_f08_relative_strength_omegasortdiff126sqz_126d_jerk_v130_signal,
    f08rs_f08_relative_strength_painsterldiffraw_252d_jerk_v131_signal,
    f08rs_f08_relative_strength_painsterldiffrank_252d_jerk_v132_signal,
    f08rs_f08_relative_strength_painsterldiffema_252d_jerk_v133_signal,
    f08rs_f08_relative_strength_painsterldifftanh_252d_jerk_v134_signal,
    f08rs_f08_relative_strength_painsterldiffsqz_252d_jerk_v135_signal,
    f08rs_f08_relative_strength_cvarcalmdiff504raw_504d_jerk_v136_signal,
    f08rs_f08_relative_strength_cvarcalmdiff504rank_504d_jerk_v137_signal,
    f08rs_f08_relative_strength_cvarcalmdiff504ema_504d_jerk_v138_signal,
    f08rs_f08_relative_strength_cvarcalmdiff504tanh_504d_jerk_v139_signal,
    f08rs_f08_relative_strength_cvarcalmdiff504sqz_504d_jerk_v140_signal,
    f08rs_f08_relative_strength_sharpedeep504raw_504d_jerk_v141_signal,
    f08rs_f08_relative_strength_sharpedeep504rank_504d_jerk_v142_signal,
    f08rs_f08_relative_strength_sharpedeep504ema_504d_jerk_v143_signal,
    f08rs_f08_relative_strength_sharpedeep504tanh_504d_jerk_v144_signal,
    f08rs_f08_relative_strength_sharpedeep504sqz_504d_jerk_v145_signal,
    f08rs_f08_relative_strength_tawcalmdiffraw_252d_jerk_v146_signal,
    f08rs_f08_relative_strength_tawcalmdiffrank_252d_jerk_v147_signal,
    f08rs_f08_relative_strength_tawcalmdiffema_252d_jerk_v148_signal,
    f08rs_f08_relative_strength_tawcalmdifftanh_252d_jerk_v149_signal,
    f08rs_f08_relative_strength_tawcalmdiffsqz_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_RELATIVE_STRENGTH_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f08_relative_strength_3rd_derivatives_001_150_claude: %d features pass" % n_features)
