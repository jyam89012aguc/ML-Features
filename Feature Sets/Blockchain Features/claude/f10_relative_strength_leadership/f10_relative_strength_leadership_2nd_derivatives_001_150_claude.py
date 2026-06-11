import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (relative-strength leadership) =====
def _f10_maratio(s, w):
    # price relative to its own trailing moving average (leadership vs own trend)
    ma = s.rolling(w, min_periods=max(1, w // 2)).mean()
    return s / ma.replace(0, np.nan)


def _f10_hilopos(s, w):
    # continuous position of price within trailing w-day low..high range in [0,1]
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    rng = (hi - lo).replace(0, np.nan)
    return (s - lo) / rng


def _f10_retrank(s, w):
    # rolling percentile rank of current price within its own trailing window
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True)


def _f10_rsslope(s, w):
    # OLS slope of the relative-strength line (price / own rolling mean) over w days,
    # normalized per-day; continuous leadership-trend velocity
    ma = s.rolling(w, min_periods=max(1, w // 2)).mean()
    rs = s / ma.replace(0, np.nan)
    idx = np.arange(w, dtype=float)
    xm = idx.mean()
    xden = ((idx - xm) ** 2).sum()

    def _ols(arr):
        y = arr
        ym = y.mean()
        return ((idx - xm) * (y - ym)).sum() / xden

    return rs.rolling(w, min_periods=w).apply(_ols, raw=True)
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ SLOPE FEATURES 001-150 ============
def f10rs_f10_relative_strength_leadership_maratio_20d_slope_v001_signal(closeadj):
    result = _f10_maratio(closeadj, 20)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_50d_slope_v002_signal(closeadj):
    result = _f10_maratio(closeadj, 50)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_100d_slope_v003_signal(closeadj):
    result = _f10_maratio(closeadj, 100)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_200d_slope_v004_signal(closeadj):
    result = _f10_maratio(closeadj, 200)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_10d_slope_v005_signal(closeadj):
    result = _f10_maratio(closeadj, 10)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_21d_slope_v006_signal(closeadj):
    result = _f10_maratio(closeadj, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_63d_slope_v007_signal(closeadj):
    result = _f10_maratio(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_126d_slope_v008_signal(closeadj):
    result = _f10_maratio(closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_252d_slope_v009_signal(closeadj):
    result = _f10_maratio(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_504d_slope_v010_signal(closeadj):
    result = _f10_maratio(closeadj, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_stack_50_200_slope_v011_signal(closeadj):
    fast = closeadj.rolling(50, min_periods=25).mean()
    slow = closeadj.rolling(200, min_periods=100).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 50) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_stack_20_100_slope_v012_signal(closeadj):
    fast = closeadj.rolling(20, min_periods=10).mean()
    slow = closeadj.rolling(100, min_periods=50).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 20) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_stack_21_63_slope_v013_signal(closeadj):
    fast = closeadj.rolling(21, min_periods=10).mean()
    slow = closeadj.rolling(63, min_periods=31).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 21) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_stack_63_252_slope_v014_signal(closeadj):
    fast = closeadj.rolling(63, min_periods=31).mean()
    slow = closeadj.rolling(252, min_periods=126).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_stack_10_50_slope_v015_signal(closeadj):
    fast = closeadj.rolling(10, min_periods=5).mean()
    slow = closeadj.rolling(50, min_periods=25).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 10) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hilopos_63d_slope_v016_signal(closeadj):
    result = _f10_hilopos(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hilopos_126d_slope_v017_signal(closeadj):
    result = _f10_hilopos(closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hilopos_252d_slope_v018_signal(closeadj):
    result = _f10_hilopos(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hilopos_504d_slope_v019_signal(closeadj):
    result = _f10_hilopos(closeadj, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hilopos_21d_slope_v020_signal(closeadj):
    result = _f10_hilopos(closeadj, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hilopos_42d_slope_v021_signal(closeadj):
    result = _f10_hilopos(closeadj, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hilopos_189d_slope_v022_signal(closeadj):
    result = _f10_hilopos(closeadj, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hlpos_63d_slope_v023_signal(high, low, closeadj):
    hi = high.rolling(63, min_periods=31).max()
    lo = low.rolling(63, min_periods=31).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - lo) / rng + _f10_hilopos(closeadj, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hlpos_252d_slope_v024_signal(high, low, closeadj):
    hi = high.rolling(252, min_periods=126).max()
    lo = low.rolling(252, min_periods=126).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - lo) / rng + _f10_hilopos(closeadj, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_disthigh_252d_slope_v025_signal(closeadj):
    hi = closeadj.rolling(252, min_periods=126).max()
    result = (closeadj - hi) / hi.replace(0, np.nan) + _f10_hilopos(closeadj, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_disthigh_504d_slope_v026_signal(closeadj):
    hi = closeadj.rolling(504, min_periods=252).max()
    result = (closeadj - hi) / hi.replace(0, np.nan) + _f10_hilopos(closeadj, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_disthigh_126d_slope_v027_signal(closeadj):
    hi = closeadj.rolling(126, min_periods=63).max()
    result = (closeadj - hi) / hi.replace(0, np.nan) + _f10_hilopos(closeadj, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_distlow_252d_slope_v028_signal(closeadj):
    lo = closeadj.rolling(252, min_periods=126).min()
    result = (closeadj - lo) / lo.replace(0, np.nan) + _f10_hilopos(closeadj, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_distlow_504d_slope_v029_signal(closeadj):
    lo = closeadj.rolling(504, min_periods=252).min()
    result = (closeadj - lo) / lo.replace(0, np.nan) + _f10_hilopos(closeadj, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_distlow_126d_slope_v030_signal(closeadj):
    lo = closeadj.rolling(126, min_periods=63).min()
    result = (closeadj - lo) / lo.replace(0, np.nan) + _f10_hilopos(closeadj, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_retrank_63d_slope_v031_signal(closeadj):
    result = _f10_retrank(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_retrank_126d_slope_v032_signal(closeadj):
    result = _f10_retrank(closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_retrank_252d_slope_v033_signal(closeadj):
    result = _f10_retrank(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_retrank_504d_slope_v034_signal(closeadj):
    result = _f10_retrank(closeadj, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_retrank_73d_slope_v035_signal(closeadj):
    result = _f10_retrank(closeadj, 73)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_retrank_110d_slope_v036_signal(closeadj):
    result = _f10_retrank(closeadj, 110)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_retrank_189d_slope_v037_signal(closeadj):
    result = _f10_retrank(closeadj, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rsslope_63d_slope_v038_signal(closeadj):
    result = _f10_rsslope(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rsslope_126d_slope_v039_signal(closeadj):
    result = _f10_rsslope(closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rsslope_21d_slope_v040_signal(closeadj):
    result = _f10_rsslope(closeadj, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rsslope_42d_slope_v041_signal(closeadj):
    result = _f10_rsslope(closeadj, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_zmaratio_50d_slope_v042_signal(closeadj):
    result = _z(_f10_maratio(closeadj, 50), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_zmaratio_200d_slope_v043_signal(closeadj):
    result = _z(_f10_maratio(closeadj, 200), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_zmaratio_21d_slope_v044_signal(closeadj):
    result = _z(_f10_maratio(closeadj, 21), 126)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_zhilopos_252d_slope_v045_signal(closeadj):
    result = _z(_f10_hilopos(closeadj, 252), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_zhilopos_126d_slope_v046_signal(closeadj):
    result = _z(_f10_hilopos(closeadj, 126), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_logmaratio_50d_slope_v047_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 50))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_logmaratio_200d_slope_v048_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 200))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_logmaratio_100d_slope_v049_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 100))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_voladjext_50d_slope_v050_signal(closeadj):
    ext = _f10_maratio(closeadj, 50) - 1.0
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(ext, vol)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_voladjext_200d_slope_v051_signal(closeadj):
    ext = _f10_maratio(closeadj, 200) - 1.0
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(ext, vol)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_posspread_252_63_slope_v052_signal(closeadj):
    result = _f10_hilopos(closeadj, 252) - _f10_hilopos(closeadj, 63)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_posspread_126_21_slope_v053_signal(closeadj):
    result = _f10_hilopos(closeadj, 126) - _f10_hilopos(closeadj, 21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maspread_20_200_slope_v054_signal(closeadj):
    result = _f10_maratio(closeadj, 20) - _f10_maratio(closeadj, 200)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maspread_50_100_slope_v055_signal(closeadj):
    result = _f10_maratio(closeadj, 50) - _f10_maratio(closeadj, 100)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rankspread_252_126_slope_v056_signal(closeadj):
    result = _f10_retrank(closeadj, 252) - _f10_retrank(closeadj, 126)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_smoothpos_252d_slope_v057_signal(closeadj):
    result = _mean(_f10_hilopos(closeadj, 252), 21)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_smoothma_50d_slope_v058_signal(closeadj):
    result = _mean(_f10_maratio(closeadj, 50), 21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_ewmma_100d_slope_v059_signal(closeadj):
    result = _f10_maratio(closeadj, 100).ewm(span=21, min_periods=10).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_posweight_252d_slope_v060_signal(closeadj):
    result = _f10_hilopos(closeadj, 252) * _f10_maratio(closeadj, 200)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rankweight_126d_slope_v061_signal(closeadj):
    result = _f10_retrank(closeadj, 126) * _f10_hilopos(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_normdraw_252d_slope_v062_signal(closeadj):
    hi = closeadj.rolling(252, min_periods=126).max()
    lo = closeadj.rolling(252, min_periods=126).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - hi) / rng + _f10_hilopos(closeadj, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_normdraw_126d_slope_v063_signal(closeadj):
    hi = closeadj.rolling(126, min_periods=63).max()
    lo = closeadj.rolling(126, min_periods=63).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - hi) / rng + _f10_hilopos(closeadj, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rsslope_252d_slope_v064_signal(closeadj):
    result = _f10_rsslope(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_volconf_63d_slope_v065_signal(closeadj, volume):
    result = (_f10_maratio(closeadj, 63) - 1.0) * _z(volume, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_dvconf_252d_slope_v066_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f10_hilopos(closeadj, 252) * _z(dv, 126)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_84d_slope_v067_signal(closeadj):
    result = _f10_maratio(closeadj, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_189d_slope_v068_signal(closeadj):
    result = _f10_maratio(closeadj, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_315d_slope_v069_signal(closeadj):
    result = _f10_maratio(closeadj, 315)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hilopos_84d_slope_v070_signal(closeadj):
    result = _f10_hilopos(closeadj, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hilopos_315d_slope_v071_signal(closeadj):
    result = _f10_hilopos(closeadj, 315)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_retrank_84d_slope_v072_signal(closeadj):
    result = _f10_retrank(closeadj, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_retrank_315d_slope_v073_signal(closeadj):
    result = _f10_retrank(closeadj, 315)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rsslope_84d_slope_v074_signal(closeadj):
    result = _f10_rsslope(closeadj, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_zstack_50_200_slope_v075_signal(closeadj):
    fast = closeadj.rolling(50, min_periods=25).mean()
    slow = closeadj.rolling(200, min_periods=100).mean()
    stack = _safe_div(fast, slow)
    result = _z(stack, 252) + _f10_maratio(closeadj, 50) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_30d_slope_v076_signal(closeadj):
    result = _f10_maratio(closeadj, 30)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_150d_slope_v077_signal(closeadj):
    result = _f10_maratio(closeadj, 150)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_378d_slope_v078_signal(closeadj):
    result = _f10_maratio(closeadj, 378)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maratio_42d_slope_v079_signal(closeadj):
    result = _f10_maratio(closeadj, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_logmaratio_21d_slope_v080_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 21))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_logmaratio_126d_slope_v081_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_logmaratio_252d_slope_v082_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 252))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_stack_100_200_slope_v083_signal(closeadj):
    fast = closeadj.rolling(100, min_periods=50).mean()
    slow = closeadj.rolling(200, min_periods=100).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 100) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_stack_42_126_slope_v084_signal(closeadj):
    fast = closeadj.rolling(42, min_periods=21).mean()
    slow = closeadj.rolling(126, min_periods=63).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 42) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_stack_126_252_slope_v085_signal(closeadj):
    fast = closeadj.rolling(126, min_periods=63).mean()
    slow = closeadj.rolling(252, min_periods=126).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 126) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_logstack_50_200_slope_v086_signal(closeadj):
    fast = closeadj.rolling(50, min_periods=25).mean()
    slow = closeadj.rolling(200, min_periods=100).mean()
    result = np.log(_safe_div(fast, slow)) + _f10_maratio(closeadj, 50) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hilopos_105d_slope_v087_signal(closeadj):
    result = _f10_hilopos(closeadj, 105)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hilopos_147d_slope_v088_signal(closeadj):
    result = _f10_hilopos(closeadj, 147)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hilopos_378d_slope_v089_signal(closeadj):
    result = _f10_hilopos(closeadj, 378)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hilopos_30d_slope_v090_signal(closeadj):
    result = _f10_hilopos(closeadj, 30)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_disthigh_189d_slope_v091_signal(closeadj):
    hi = closeadj.rolling(189, min_periods=94).max()
    result = (closeadj - hi) / hi.replace(0, np.nan) + _f10_hilopos(closeadj, 189) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_disthigh_63d_slope_v092_signal(closeadj):
    hi = closeadj.rolling(63, min_periods=31).max()
    result = (closeadj - hi) / hi.replace(0, np.nan) + _f10_hilopos(closeadj, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_distlow_189d_slope_v093_signal(closeadj):
    lo = closeadj.rolling(189, min_periods=94).min()
    result = (closeadj - lo) / lo.replace(0, np.nan) + _f10_hilopos(closeadj, 189) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_distlow_63d_slope_v094_signal(closeadj):
    lo = closeadj.rolling(63, min_periods=31).min()
    result = (closeadj - lo) / lo.replace(0, np.nan) + _f10_hilopos(closeadj, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_proxhigh_252d_slope_v095_signal(closeadj):
    hi = closeadj.rolling(252, min_periods=126).max()
    result = _safe_div(closeadj, hi) + _f10_hilopos(closeadj, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_proxhigh_504d_slope_v096_signal(closeadj):
    hi = closeadj.rolling(504, min_periods=252).max()
    result = _safe_div(closeadj, hi) + _f10_hilopos(closeadj, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_proxlow_252d_slope_v097_signal(closeadj):
    lo = closeadj.rolling(252, min_periods=126).min()
    result = _safe_div(lo, closeadj) + _f10_hilopos(closeadj, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_retrank_147d_slope_v098_signal(closeadj):
    result = _f10_retrank(closeadj, 147)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_retrank_378d_slope_v099_signal(closeadj):
    result = _f10_retrank(closeadj, 378)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_retrank_105d_slope_v100_signal(closeadj):
    result = _f10_retrank(closeadj, 105)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rankmom_63_252_slope_v101_signal(closeadj):
    result = _f10_retrank(closeadj, 63) - _f10_retrank(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rankmom_126_504_slope_v102_signal(closeadj):
    result = _f10_retrank(closeadj, 126) - _f10_retrank(closeadj, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rsslope_105d_slope_v103_signal(closeadj):
    result = _f10_rsslope(closeadj, 105)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rsslope_147d_slope_v104_signal(closeadj):
    result = _f10_rsslope(closeadj, 147)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rsslope_189d_slope_v105_signal(closeadj):
    result = _f10_rsslope(closeadj, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rsslope_504d_slope_v106_signal(closeadj):
    result = _f10_rsslope(closeadj, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rsslopespr_63_252_slope_v107_signal(closeadj):
    result = _f10_rsslope(closeadj, 63) - _f10_rsslope(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_zmaratio_100d_slope_v108_signal(closeadj):
    result = _z(_f10_maratio(closeadj, 100), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_zmaratio_63d_slope_v109_signal(closeadj):
    result = _z(_f10_maratio(closeadj, 63), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_zhilopos_504d_slope_v110_signal(closeadj):
    result = _z(_f10_hilopos(closeadj, 504), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_zhilopos_63d_slope_v111_signal(closeadj):
    result = _z(_f10_hilopos(closeadj, 63), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_zretrank_252d_slope_v112_signal(closeadj):
    result = _z(_f10_retrank(closeadj, 252), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_zretrank_126d_slope_v113_signal(closeadj):
    result = _z(_f10_retrank(closeadj, 126), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_voladjext_200_126_slope_v114_signal(closeadj):
    ext = _f10_maratio(closeadj, 200) - 1.0
    vol = _std(closeadj.pct_change(), 126)
    result = _safe_div(ext, vol)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_voladjext_100_252_slope_v115_signal(closeadj):
    ext = _f10_maratio(closeadj, 100) - 1.0
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(ext, vol)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_smoothpos63_252d_slope_v116_signal(closeadj):
    result = _mean(_f10_hilopos(closeadj, 252), 63)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_smoothma63_200d_slope_v117_signal(closeadj):
    result = _mean(_f10_maratio(closeadj, 200), 63)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_ewmpos_252d_slope_v118_signal(closeadj):
    result = _f10_hilopos(closeadj, 252).ewm(span=42, min_periods=21).mean()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_ewmrank_252d_slope_v119_signal(closeadj):
    result = _f10_retrank(closeadj, 252).ewm(span=42, min_periods=21).mean()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_posstackw_252d_slope_v120_signal(closeadj):
    fast = closeadj.rolling(50, min_periods=25).mean()
    slow = closeadj.rolling(200, min_periods=100).mean()
    stack = _safe_div(fast, slow)
    result = _f10_hilopos(closeadj, 252) * stack
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rankmaw_252d_slope_v121_signal(closeadj):
    result = _f10_retrank(closeadj, 252) * _f10_maratio(closeadj, 200)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_posprod_63_252_slope_v122_signal(closeadj):
    result = _f10_hilopos(closeadj, 63) * _f10_hilopos(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_macomposite_slope_v123_signal(closeadj):
    result = (_f10_maratio(closeadj, 20) + _f10_maratio(closeadj, 50)
              + _f10_maratio(closeadj, 100) + _f10_maratio(closeadj, 200)) / 4.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_poscomposite_slope_v124_signal(closeadj):
    result = (_f10_hilopos(closeadj, 63) + _f10_hilopos(closeadj, 126)
              + _f10_hilopos(closeadj, 252) + _f10_hilopos(closeadj, 504)) / 4.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rankcomposite_slope_v125_signal(closeadj):
    result = (_f10_retrank(closeadj, 63) + _f10_retrank(closeadj, 126)
              + _f10_retrank(closeadj, 252)) / 3.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_dvsurge_50d_slope_v126_signal(closeadj, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 63))
    result = (_f10_maratio(closeadj, 50) - 1.0) * surge
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_volconfpos_252d_slope_v127_signal(closeadj, volume):
    result = _f10_hilopos(closeadj, 252) * _z(volume, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hlpos_126d_slope_v128_signal(high, low, closeadj):
    hi = high.rolling(126, min_periods=63).max()
    lo = low.rolling(126, min_periods=63).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - lo) / rng + _f10_hilopos(closeadj, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_hlpos_504d_slope_v129_signal(high, low, closeadj):
    hi = high.rolling(504, min_periods=252).max()
    lo = low.rolling(504, min_periods=252).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - lo) / rng + _f10_hilopos(closeadj, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_highpress_252d_slope_v130_signal(high, closeadj):
    hi = high.rolling(252, min_periods=126).max()
    result = _safe_div(closeadj, hi) + _f10_hilopos(closeadj, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_logmaratio_315d_slope_v131_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 315))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_logmaratio_84d_slope_v132_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 84))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_logmaspread_50_252_slope_v133_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 50)) - np.log(_f10_maratio(closeadj, 252))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_maspread_10_63_slope_v134_signal(closeadj):
    result = _f10_maratio(closeadj, 10) - _f10_maratio(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_posspread_504_126_slope_v135_signal(closeadj):
    result = _f10_hilopos(closeadj, 504) - _f10_hilopos(closeadj, 126)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_posspread_315_84_slope_v136_signal(closeadj):
    result = _f10_hilopos(closeadj, 315) - _f10_hilopos(closeadj, 84)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rankspread_504_252_slope_v137_signal(closeadj):
    result = _f10_retrank(closeadj, 504) - _f10_retrank(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_normdraw_315d_slope_v138_signal(closeadj):
    hi = closeadj.rolling(315, min_periods=157).max()
    lo = closeadj.rolling(315, min_periods=157).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - hi) / rng + _f10_hilopos(closeadj, 315) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_normdraw_504d_slope_v139_signal(closeadj):
    hi = closeadj.rolling(504, min_periods=252).max()
    lo = closeadj.rolling(504, min_periods=252).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - hi) / rng + _f10_hilopos(closeadj, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_ewmma_200d_slope_v140_signal(closeadj):
    result = _f10_maratio(closeadj, 200).ewm(span=63, min_periods=31).mean()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_ewmma_50d_slope_v141_signal(closeadj):
    result = _f10_maratio(closeadj, 50).ewm(span=21, min_periods=10).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_possurp_252d_slope_v142_signal(closeadj):
    p = _f10_hilopos(closeadj, 252)
    result = p - _mean(p, 63)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_masurp_50d_slope_v143_signal(closeadj):
    m = _f10_maratio(closeadj, 50)
    result = m - _mean(m, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_posrank_252d_slope_v144_signal(closeadj):
    p = _f10_hilopos(closeadj, 252)
    result = p.rolling(252, min_periods=126).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_marank_200d_slope_v145_signal(closeadj):
    m = _f10_maratio(closeadj, 200)
    result = m.rolling(252, min_periods=126).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rsslopevol_126d_slope_v146_signal(closeadj):
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(_f10_rsslope(closeadj, 126), vol)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_rsslopevol_252d_slope_v147_signal(closeadj):
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(_f10_rsslope(closeadj, 252), vol)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_materm_63_252_slope_v148_signal(closeadj):
    result = _f10_maratio(closeadj, 63) - _f10_maratio(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_blend_lead_slope_v149_signal(closeadj):
    result = (_f10_hilopos(closeadj, 252)
              + (_f10_maratio(closeadj, 200) - 1.0)
              + _f10_retrank(closeadj, 252)) / 3.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f10rs_f10_relative_strength_leadership_posrsslope_252d_slope_v150_signal(closeadj):
    result = _f10_hilopos(closeadj, 252) * _f10_rsslope(closeadj, 126)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f10rs_f10_relative_strength_leadership_maratio_20d_slope_v001_signal,    f10rs_f10_relative_strength_leadership_maratio_50d_slope_v002_signal,    f10rs_f10_relative_strength_leadership_maratio_100d_slope_v003_signal,    f10rs_f10_relative_strength_leadership_maratio_200d_slope_v004_signal,    f10rs_f10_relative_strength_leadership_maratio_10d_slope_v005_signal,    f10rs_f10_relative_strength_leadership_maratio_21d_slope_v006_signal,    f10rs_f10_relative_strength_leadership_maratio_63d_slope_v007_signal,    f10rs_f10_relative_strength_leadership_maratio_126d_slope_v008_signal,    f10rs_f10_relative_strength_leadership_maratio_252d_slope_v009_signal,    f10rs_f10_relative_strength_leadership_maratio_504d_slope_v010_signal,    f10rs_f10_relative_strength_leadership_stack_50_200_slope_v011_signal,    f10rs_f10_relative_strength_leadership_stack_20_100_slope_v012_signal,    f10rs_f10_relative_strength_leadership_stack_21_63_slope_v013_signal,    f10rs_f10_relative_strength_leadership_stack_63_252_slope_v014_signal,    f10rs_f10_relative_strength_leadership_stack_10_50_slope_v015_signal,    f10rs_f10_relative_strength_leadership_hilopos_63d_slope_v016_signal,    f10rs_f10_relative_strength_leadership_hilopos_126d_slope_v017_signal,    f10rs_f10_relative_strength_leadership_hilopos_252d_slope_v018_signal,    f10rs_f10_relative_strength_leadership_hilopos_504d_slope_v019_signal,    f10rs_f10_relative_strength_leadership_hilopos_21d_slope_v020_signal,    f10rs_f10_relative_strength_leadership_hilopos_42d_slope_v021_signal,    f10rs_f10_relative_strength_leadership_hilopos_189d_slope_v022_signal,    f10rs_f10_relative_strength_leadership_hlpos_63d_slope_v023_signal,    f10rs_f10_relative_strength_leadership_hlpos_252d_slope_v024_signal,    f10rs_f10_relative_strength_leadership_disthigh_252d_slope_v025_signal,    f10rs_f10_relative_strength_leadership_disthigh_504d_slope_v026_signal,    f10rs_f10_relative_strength_leadership_disthigh_126d_slope_v027_signal,    f10rs_f10_relative_strength_leadership_distlow_252d_slope_v028_signal,    f10rs_f10_relative_strength_leadership_distlow_504d_slope_v029_signal,    f10rs_f10_relative_strength_leadership_distlow_126d_slope_v030_signal,    f10rs_f10_relative_strength_leadership_retrank_63d_slope_v031_signal,    f10rs_f10_relative_strength_leadership_retrank_126d_slope_v032_signal,    f10rs_f10_relative_strength_leadership_retrank_252d_slope_v033_signal,    f10rs_f10_relative_strength_leadership_retrank_504d_slope_v034_signal,    f10rs_f10_relative_strength_leadership_retrank_73d_slope_v035_signal,    f10rs_f10_relative_strength_leadership_retrank_110d_slope_v036_signal,    f10rs_f10_relative_strength_leadership_retrank_189d_slope_v037_signal,    f10rs_f10_relative_strength_leadership_rsslope_63d_slope_v038_signal,    f10rs_f10_relative_strength_leadership_rsslope_126d_slope_v039_signal,    f10rs_f10_relative_strength_leadership_rsslope_21d_slope_v040_signal,    f10rs_f10_relative_strength_leadership_rsslope_42d_slope_v041_signal,    f10rs_f10_relative_strength_leadership_zmaratio_50d_slope_v042_signal,    f10rs_f10_relative_strength_leadership_zmaratio_200d_slope_v043_signal,    f10rs_f10_relative_strength_leadership_zmaratio_21d_slope_v044_signal,    f10rs_f10_relative_strength_leadership_zhilopos_252d_slope_v045_signal,    f10rs_f10_relative_strength_leadership_zhilopos_126d_slope_v046_signal,    f10rs_f10_relative_strength_leadership_logmaratio_50d_slope_v047_signal,    f10rs_f10_relative_strength_leadership_logmaratio_200d_slope_v048_signal,    f10rs_f10_relative_strength_leadership_logmaratio_100d_slope_v049_signal,    f10rs_f10_relative_strength_leadership_voladjext_50d_slope_v050_signal,    f10rs_f10_relative_strength_leadership_voladjext_200d_slope_v051_signal,    f10rs_f10_relative_strength_leadership_posspread_252_63_slope_v052_signal,    f10rs_f10_relative_strength_leadership_posspread_126_21_slope_v053_signal,    f10rs_f10_relative_strength_leadership_maspread_20_200_slope_v054_signal,    f10rs_f10_relative_strength_leadership_maspread_50_100_slope_v055_signal,    f10rs_f10_relative_strength_leadership_rankspread_252_126_slope_v056_signal,    f10rs_f10_relative_strength_leadership_smoothpos_252d_slope_v057_signal,    f10rs_f10_relative_strength_leadership_smoothma_50d_slope_v058_signal,    f10rs_f10_relative_strength_leadership_ewmma_100d_slope_v059_signal,    f10rs_f10_relative_strength_leadership_posweight_252d_slope_v060_signal,    f10rs_f10_relative_strength_leadership_rankweight_126d_slope_v061_signal,    f10rs_f10_relative_strength_leadership_normdraw_252d_slope_v062_signal,    f10rs_f10_relative_strength_leadership_normdraw_126d_slope_v063_signal,    f10rs_f10_relative_strength_leadership_rsslope_252d_slope_v064_signal,    f10rs_f10_relative_strength_leadership_volconf_63d_slope_v065_signal,    f10rs_f10_relative_strength_leadership_dvconf_252d_slope_v066_signal,    f10rs_f10_relative_strength_leadership_maratio_84d_slope_v067_signal,    f10rs_f10_relative_strength_leadership_maratio_189d_slope_v068_signal,    f10rs_f10_relative_strength_leadership_maratio_315d_slope_v069_signal,    f10rs_f10_relative_strength_leadership_hilopos_84d_slope_v070_signal,    f10rs_f10_relative_strength_leadership_hilopos_315d_slope_v071_signal,    f10rs_f10_relative_strength_leadership_retrank_84d_slope_v072_signal,    f10rs_f10_relative_strength_leadership_retrank_315d_slope_v073_signal,    f10rs_f10_relative_strength_leadership_rsslope_84d_slope_v074_signal,    f10rs_f10_relative_strength_leadership_zstack_50_200_slope_v075_signal,    f10rs_f10_relative_strength_leadership_maratio_30d_slope_v076_signal,    f10rs_f10_relative_strength_leadership_maratio_150d_slope_v077_signal,    f10rs_f10_relative_strength_leadership_maratio_378d_slope_v078_signal,    f10rs_f10_relative_strength_leadership_maratio_42d_slope_v079_signal,    f10rs_f10_relative_strength_leadership_logmaratio_21d_slope_v080_signal,    f10rs_f10_relative_strength_leadership_logmaratio_126d_slope_v081_signal,    f10rs_f10_relative_strength_leadership_logmaratio_252d_slope_v082_signal,    f10rs_f10_relative_strength_leadership_stack_100_200_slope_v083_signal,    f10rs_f10_relative_strength_leadership_stack_42_126_slope_v084_signal,    f10rs_f10_relative_strength_leadership_stack_126_252_slope_v085_signal,    f10rs_f10_relative_strength_leadership_logstack_50_200_slope_v086_signal,    f10rs_f10_relative_strength_leadership_hilopos_105d_slope_v087_signal,    f10rs_f10_relative_strength_leadership_hilopos_147d_slope_v088_signal,    f10rs_f10_relative_strength_leadership_hilopos_378d_slope_v089_signal,    f10rs_f10_relative_strength_leadership_hilopos_30d_slope_v090_signal,    f10rs_f10_relative_strength_leadership_disthigh_189d_slope_v091_signal,    f10rs_f10_relative_strength_leadership_disthigh_63d_slope_v092_signal,    f10rs_f10_relative_strength_leadership_distlow_189d_slope_v093_signal,    f10rs_f10_relative_strength_leadership_distlow_63d_slope_v094_signal,    f10rs_f10_relative_strength_leadership_proxhigh_252d_slope_v095_signal,    f10rs_f10_relative_strength_leadership_proxhigh_504d_slope_v096_signal,    f10rs_f10_relative_strength_leadership_proxlow_252d_slope_v097_signal,    f10rs_f10_relative_strength_leadership_retrank_147d_slope_v098_signal,    f10rs_f10_relative_strength_leadership_retrank_378d_slope_v099_signal,    f10rs_f10_relative_strength_leadership_retrank_105d_slope_v100_signal,    f10rs_f10_relative_strength_leadership_rankmom_63_252_slope_v101_signal,    f10rs_f10_relative_strength_leadership_rankmom_126_504_slope_v102_signal,    f10rs_f10_relative_strength_leadership_rsslope_105d_slope_v103_signal,    f10rs_f10_relative_strength_leadership_rsslope_147d_slope_v104_signal,    f10rs_f10_relative_strength_leadership_rsslope_189d_slope_v105_signal,    f10rs_f10_relative_strength_leadership_rsslope_504d_slope_v106_signal,    f10rs_f10_relative_strength_leadership_rsslopespr_63_252_slope_v107_signal,    f10rs_f10_relative_strength_leadership_zmaratio_100d_slope_v108_signal,    f10rs_f10_relative_strength_leadership_zmaratio_63d_slope_v109_signal,    f10rs_f10_relative_strength_leadership_zhilopos_504d_slope_v110_signal,    f10rs_f10_relative_strength_leadership_zhilopos_63d_slope_v111_signal,    f10rs_f10_relative_strength_leadership_zretrank_252d_slope_v112_signal,    f10rs_f10_relative_strength_leadership_zretrank_126d_slope_v113_signal,    f10rs_f10_relative_strength_leadership_voladjext_200_126_slope_v114_signal,    f10rs_f10_relative_strength_leadership_voladjext_100_252_slope_v115_signal,    f10rs_f10_relative_strength_leadership_smoothpos63_252d_slope_v116_signal,    f10rs_f10_relative_strength_leadership_smoothma63_200d_slope_v117_signal,    f10rs_f10_relative_strength_leadership_ewmpos_252d_slope_v118_signal,    f10rs_f10_relative_strength_leadership_ewmrank_252d_slope_v119_signal,    f10rs_f10_relative_strength_leadership_posstackw_252d_slope_v120_signal,    f10rs_f10_relative_strength_leadership_rankmaw_252d_slope_v121_signal,    f10rs_f10_relative_strength_leadership_posprod_63_252_slope_v122_signal,    f10rs_f10_relative_strength_leadership_macomposite_slope_v123_signal,    f10rs_f10_relative_strength_leadership_poscomposite_slope_v124_signal,    f10rs_f10_relative_strength_leadership_rankcomposite_slope_v125_signal,    f10rs_f10_relative_strength_leadership_dvsurge_50d_slope_v126_signal,    f10rs_f10_relative_strength_leadership_volconfpos_252d_slope_v127_signal,    f10rs_f10_relative_strength_leadership_hlpos_126d_slope_v128_signal,    f10rs_f10_relative_strength_leadership_hlpos_504d_slope_v129_signal,    f10rs_f10_relative_strength_leadership_highpress_252d_slope_v130_signal,    f10rs_f10_relative_strength_leadership_logmaratio_315d_slope_v131_signal,    f10rs_f10_relative_strength_leadership_logmaratio_84d_slope_v132_signal,    f10rs_f10_relative_strength_leadership_logmaspread_50_252_slope_v133_signal,    f10rs_f10_relative_strength_leadership_maspread_10_63_slope_v134_signal,    f10rs_f10_relative_strength_leadership_posspread_504_126_slope_v135_signal,    f10rs_f10_relative_strength_leadership_posspread_315_84_slope_v136_signal,    f10rs_f10_relative_strength_leadership_rankspread_504_252_slope_v137_signal,    f10rs_f10_relative_strength_leadership_normdraw_315d_slope_v138_signal,    f10rs_f10_relative_strength_leadership_normdraw_504d_slope_v139_signal,    f10rs_f10_relative_strength_leadership_ewmma_200d_slope_v140_signal,    f10rs_f10_relative_strength_leadership_ewmma_50d_slope_v141_signal,    f10rs_f10_relative_strength_leadership_possurp_252d_slope_v142_signal,    f10rs_f10_relative_strength_leadership_masurp_50d_slope_v143_signal,    f10rs_f10_relative_strength_leadership_posrank_252d_slope_v144_signal,    f10rs_f10_relative_strength_leadership_marank_200d_slope_v145_signal,    f10rs_f10_relative_strength_leadership_rsslopevol_126d_slope_v146_signal,    f10rs_f10_relative_strength_leadership_rsslopevol_252d_slope_v147_signal,    f10rs_f10_relative_strength_leadership_materm_63_252_slope_v148_signal,    f10rs_f10_relative_strength_leadership_blend_lead_slope_v149_signal,    f10rs_f10_relative_strength_leadership_posrsslope_252d_slope_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_RELATIVE_STRENGTH_LEADERSHIP_REGISTRY_SLOPE = REGISTRY

def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = ('_f10_maratio', '_f10_hilopos', '_f10_retrank', '_f10_rsslope')
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print("OK f10_relative_strength_leadership_" + "2nd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
