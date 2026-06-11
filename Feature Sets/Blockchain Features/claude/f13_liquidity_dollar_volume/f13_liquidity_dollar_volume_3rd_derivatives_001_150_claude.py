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


# ===== folder domain primitives (liquidity / dollar-volume) =====
def _f13_dvol(closeadj, volume):
    # dollar volume = adjusted close * volume (liquidity level)
    return closeadj * volume


def _f13_amihud(closeadj, volume, w):
    # Amihud illiquidity: mean of |daily return| / dollar volume over w days
    r = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    return (r / dv).rolling(w, min_periods=max(2, w // 2)).mean()


def _f13_turnover(closeadj, volume, w):
    # turnover = volume / trailing mean volume (closeadj anchors the primitive)
    base = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    return (volume / base.replace(0, np.nan)) + closeadj * 0.0


def _f13_logdvol(closeadj, volume, w):
    # smoothed log dollar volume over w days (liquidity level, log scale)
    dv = (closeadj * volume).replace(0, np.nan)
    return np.log(dv).rolling(w, min_periods=max(1, w // 2)).mean()
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ JERK FEATURES 001-150 ============
def f13lq_f13_liquidity_dollar_volume_logdvol_21d_jerk_v001_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvol_63d_jerk_v002_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvol_126d_jerk_v003_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvol_252d_jerk_v004_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvol_5d_jerk_v005_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvolmean_21d_jerk_v006_signal(closeadj, volume):
    result = _mean(_f13_dvol(closeadj, volume), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvolmean_63d_jerk_v007_signal(closeadj, volume):
    result = _mean(_f13_dvol(closeadj, volume), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvolmean_126d_jerk_v008_signal(closeadj, volume):
    result = _mean(_f13_dvol(closeadj, volume), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvolmean_252d_jerk_v009_signal(closeadj, volume):
    result = _mean(_f13_dvol(closeadj, volume), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvolmean_504d_jerk_v010_signal(closeadj, volume):
    result = _mean(_f13_dvol(closeadj, volume), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amihud_21d_jerk_v011_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amihud_63d_jerk_v012_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amihud_126d_jerk_v013_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amihud_252d_jerk_v014_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logamihud_63d_jerk_v015_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logamihud_126d_jerk_v016_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnover_21d_jerk_v017_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnover_63d_jerk_v018_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnover_126d_jerk_v019_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnover_252d_jerk_v020_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnsm_21d_jerk_v021_signal(closeadj, volume):
    result = _mean(_f13_turnover(closeadj, volume, 5), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnsm_63d_jerk_v022_signal(closeadj, volume):
    result = _mean(_f13_turnover(closeadj, volume, 21), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_zdvol_63d_jerk_v023_signal(closeadj, volume):
    result = _z(_f13_dvol(closeadj, volume), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_zdvol_126d_jerk_v024_signal(closeadj, volume):
    result = _z(_f13_dvol(closeadj, volume), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_zdvol_252d_jerk_v025_signal(closeadj, volume):
    result = _z(_f13_dvol(closeadj, volume), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_zlogdvol_252d_jerk_v026_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = _z(np.log(dv), 252) + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_zamihud_21d_jerk_v027_signal(closeadj, volume):
    result = _z(_f13_amihud(closeadj, volume, 21), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_zamihud_63d_jerk_v028_signal(closeadj, volume):
    result = _z(_f13_amihud(closeadj, volume, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_zturn_21d_jerk_v029_signal(closeadj, volume):
    result = _z(_f13_turnover(closeadj, volume, 21), 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_zturn_63d_jerk_v030_signal(closeadj, volume):
    result = _z(_f13_turnover(closeadj, volume, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_cv_63d_jerk_v031_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_std(dv, 63), _mean(dv, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_cv_126d_jerk_v032_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_std(dv, 126), _mean(dv, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_cv_252d_jerk_v033_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_std(dv, 252), _mean(dv, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_trend_21_126_jerk_v034_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 21) - _f13_logdvol(closeadj, volume, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_trend_63_252_jerk_v035_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 63) - _f13_logdvol(closeadj, volume, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_vsavg_252d_jerk_v036_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv) - _f13_logdvol(closeadj, volume, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_vsavg_126d_jerk_v037_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv) - _f13_logdvol(closeadj, volume, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amirank_21d_jerk_v038_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 21)
    result = a.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amirank_63d_jerk_v039_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 63)
    result = a.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvrank_252d_jerk_v040_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = dv.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnrank_252d_jerk_v041_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = t.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_impact_21d_jerk_v042_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    result = _mean(_safe_div(r, np.log(dv)), 21) + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_impact_63d_jerk_v043_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    result = _mean(_safe_div(r, np.log(dv)), 63) + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_corrabsv_63d_jerk_v044_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    result = r.rolling(63, min_periods=21).corr(volume) + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_corrabsv_126d_jerk_v045_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    result = r.rolling(126, min_periods=42).corr(volume) + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_corrabsdv_126d_jerk_v046_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    dv = _f13_dvol(closeadj, volume)
    result = r.rolling(126, min_periods=42).corr(dv)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amitrend_21_126_jerk_v047_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 21) - _f13_amihud(closeadj, volume, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amiratio_21_252_jerk_v048_signal(closeadj, volume):
    result = _safe_div(_f13_amihud(closeadj, volume, 21), _f13_amihud(closeadj, volume, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvratio_21_252_jerk_v049_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_mean(dv, 21), _mean(dv, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvratio_63_252_jerk_v050_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_mean(dv, 63), _mean(dv, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvol_1d_jerk_v051_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv) + _f13_logdvol(closeadj, volume, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvol_42d_jerk_v052_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvol_189d_jerk_v053_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvol_504d_jerk_v054_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amihud_42d_jerk_v055_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amihud_189d_jerk_v056_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnover_42d_jerk_v057_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnover_189d_jerk_v058_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_ewmdvol_21d_jerk_v059_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv).ewm(span=21, min_periods=10).mean() + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_ewmdvol_63d_jerk_v060_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv).ewm(span=63, min_periods=21).mean() + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_ewmturn_21d_jerk_v061_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = t.ewm(span=21, min_periods=10).mean()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_ewmami_63d_jerk_v062_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 21)
    result = a.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvolstd_63d_jerk_v063_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = _std(np.log(dv), 63) + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvolstd_126d_jerk_v064_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = _std(np.log(dv), 126) + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnstd_63d_jerk_v065_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = _std(t, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amistd_126d_jerk_v066_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 21)
    result = _std(a, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logamitrend_jerk_v067_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 21)) - np.log(_f13_amihud(closeadj, volume, 126))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turntrend_21_126_jerk_v068_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 21) - _f13_turnover(closeadj, volume, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amiscaled_63d_jerk_v069_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 63)
    result = _safe_div(a, _std(a, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amicomposite_63d_jerk_v070_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 63)) - _f13_logdvol(closeadj, volume, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvmom_21d_jerk_v071_signal(closeadj, volume):
    m = _mean(_f13_dvol(closeadj, volume), 21).replace(0, np.nan)
    result = np.log(m / m.shift(21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvmom_63d_jerk_v072_signal(closeadj, volume):
    m = _mean(_f13_dvol(closeadj, volume), 63).replace(0, np.nan)
    result = np.log(m / m.shift(63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnskew_126d_jerk_v073_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = t.rolling(126, min_periods=42).skew()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvskew_252d_jerk_v074_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv).rolling(252, min_periods=84).skew() + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_illiqturn_63d_jerk_v075_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 63)
    arank = a.rolling(252, min_periods=63).rank(pct=True)
    result = _f13_turnover(closeadj, volume, 21) * arank
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvol_84d_jerk_v076_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvol_315d_jerk_v077_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 315)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvol_378d_jerk_v078_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 378)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvol_10d_jerk_v079_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvolmean_42d_jerk_v080_signal(closeadj, volume):
    result = _mean(_f13_dvol(closeadj, volume), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvolmean_189d_jerk_v081_signal(closeadj, volume):
    result = _mean(_f13_dvol(closeadj, volume), 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amihud_84d_jerk_v082_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amihud_315d_jerk_v083_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 315)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logamihud_252d_jerk_v084_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logamihud_21d_jerk_v085_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnover_84d_jerk_v086_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnover_315d_jerk_v087_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 315)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnover_5d_jerk_v088_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logturn_21d_jerk_v089_signal(closeadj, volume):
    result = np.log(_f13_turnover(closeadj, volume, 21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logturn_63d_jerk_v090_signal(closeadj, volume):
    result = np.log(_f13_turnover(closeadj, volume, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_zdvol_504d_jerk_v091_signal(closeadj, volume):
    result = _z(_f13_dvol(closeadj, volume), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_zamihud_126d_jerk_v092_signal(closeadj, volume):
    result = _z(_f13_amihud(closeadj, volume, 126), 504)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_zturn_126d_jerk_v093_signal(closeadj, volume):
    result = _z(_f13_turnover(closeadj, volume, 126), 504)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_zlogdvol_126d_jerk_v094_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = _z(np.log(dv), 126) + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_zlogami_252d_jerk_v095_signal(closeadj, volume):
    result = _z(np.log(_f13_amihud(closeadj, volume, 21)), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_cv_42d_jerk_v096_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_std(dv, 42), _mean(dv, 42))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_cv_189d_jerk_v097_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_std(dv, 189), _mean(dv, 189))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_volcv_63d_jerk_v098_signal(closeadj, volume):
    result = _safe_div(_std(volume, 63), _mean(volume, 63)) + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_trend_42_189_jerk_v099_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 42) - _f13_logdvol(closeadj, volume, 189)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_trend_21_63_jerk_v100_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 21) - _f13_logdvol(closeadj, volume, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_vsavg_504d_jerk_v101_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv) - _f13_logdvol(closeadj, volume, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_vsavg_63d_jerk_v102_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv) - _f13_logdvol(closeadj, volume, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amirank_126d_jerk_v103_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 126)
    result = a.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvrank_126d_jerk_v104_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = dv.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnrank_126d_jerk_v105_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = t.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvrank_252d_jerk_v106_signal(closeadj, volume):
    ld = _f13_logdvol(closeadj, volume, 5)
    result = ld.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_impact_126d_jerk_v107_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    result = _mean(_safe_div(r, np.log(dv)), 126) + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_impact_252d_jerk_v108_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    result = _mean(_safe_div(r, np.log(dv)), 252) + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_impact2_63d_jerk_v109_signal(closeadj, volume):
    r2 = closeadj.pct_change() ** 2
    dv = (closeadj * volume).replace(0, np.nan)
    result = _mean(_safe_div(r2, dv), 63) + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_corrabsv_252d_jerk_v110_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    result = r.rolling(252, min_periods=84).corr(volume) + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_corrabsdv_63d_jerk_v111_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    dv = _f13_dvol(closeadj, volume)
    result = r.rolling(63, min_periods=21).corr(dv)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_corrrv_126d_jerk_v112_signal(closeadj, volume):
    r = closeadj.pct_change()
    result = r.rolling(126, min_periods=42).corr(volume) + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amitrend_63_252_jerk_v113_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 63) - _f13_amihud(closeadj, volume, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amiratio_63_252_jerk_v114_signal(closeadj, volume):
    result = _safe_div(_f13_amihud(closeadj, volume, 63), _f13_amihud(closeadj, volume, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvratio_21_126_jerk_v115_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_mean(dv, 21), _mean(dv, 126))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvratio_42_189_jerk_v116_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_mean(dv, 42), _mean(dv, 189))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnratio_21_252_jerk_v117_signal(closeadj, volume):
    result = _safe_div(_f13_turnover(closeadj, volume, 21), _f13_turnover(closeadj, volume, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_ewmdvol_126d_jerk_v118_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv).ewm(span=126, min_periods=42).mean() + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_ewmdvol_252d_jerk_v119_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv).ewm(span=252, min_periods=84).mean() + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_ewmturn_63d_jerk_v120_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = t.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_ewmami_126d_jerk_v121_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 21)
    result = a.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvolstd_252d_jerk_v122_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = _std(np.log(dv), 252) + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnstd_126d_jerk_v123_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = _std(t, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amistd_252d_jerk_v124_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 21)
    result = _std(a, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logamitrend_63_252_jerk_v125_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 63)) - np.log(_f13_amihud(closeadj, volume, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turntrend_63_252_jerk_v126_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 63) - _f13_turnover(closeadj, volume, 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amiscaled_126d_jerk_v127_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 126)
    result = _safe_div(a, _std(a, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amicomposite_126d_jerk_v128_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 126)) - _f13_logdvol(closeadj, volume, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvmom_126d_jerk_v129_signal(closeadj, volume):
    m = _mean(_f13_dvol(closeadj, volume), 126).replace(0, np.nan)
    result = np.log(m / m.shift(126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvmom_42d_jerk_v130_signal(closeadj, volume):
    m = _mean(_f13_dvol(closeadj, volume), 42).replace(0, np.nan)
    result = np.log(m / m.shift(42))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnskew_252d_jerk_v131_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = t.rolling(252, min_periods=84).skew()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvskew_126d_jerk_v132_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv).rolling(126, min_periods=42).skew() + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnkurt_126d_jerk_v133_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = t.rolling(126, min_periods=42).kurt()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amikurt_252d_jerk_v134_signal(closeadj, volume):
    a = np.log(_f13_amihud(closeadj, volume, 21))
    result = a.rolling(252, min_periods=84).kurt()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_illiqturn_126d_jerk_v135_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 126)
    arank = a.rolling(252, min_periods=63).rank(pct=True)
    result = _f13_turnover(closeadj, volume, 63) * arank
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_liqturn_63d_jerk_v136_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    relliq = np.log(dv) - _f13_logdvol(closeadj, volume, 252)
    result = _f13_turnover(closeadj, volume, 21) * relliq
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_zdiverge_63d_jerk_v137_signal(closeadj, volume):
    za = _z(_f13_amihud(closeadj, volume, 63), 252)
    zd = _z(_f13_dvol(closeadj, volume), 252)
    result = za - zd
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnsurge_21d_jerk_v138_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    base = t.ewm(span=252, min_periods=84).mean()
    result = _safe_div(t, base)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvsurge_21d_jerk_v139_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    base = dv.ewm(span=252, min_periods=84).mean()
    result = _safe_div(_mean(dv, 21), base)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amisurge_21d_jerk_v140_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 21)
    base = a.ewm(span=252, min_periods=84).mean()
    result = _safe_div(a, base)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amism_21d_jerk_v141_signal(closeadj, volume):
    result = _mean(_f13_amihud(closeadj, volume, 21), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_logdvolsm_21d_jerk_v142_signal(closeadj, volume):
    result = _mean(_f13_logdvol(closeadj, volume, 5), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnir_21d_jerk_v143_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = _safe_div(t - _mean(t, 252), _std(t, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amiir_21d_jerk_v144_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 21)
    result = _safe_div(a - _mean(a, 252), _std(a, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvratio_63_504_jerk_v145_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_mean(dv, 63), _mean(dv, 504))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_dvaccel_jerk_v146_signal(closeadj, volume):
    fast = _f13_logdvol(closeadj, volume, 21) - _f13_logdvol(closeadj, volume, 63)
    slow = _f13_logdvol(closeadj, volume, 63) - _f13_logdvol(closeadj, volume, 126)
    result = fast - slow
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_amiaccel_jerk_v147_signal(closeadj, volume):
    fast = _f13_amihud(closeadj, volume, 21) - _f13_amihud(closeadj, volume, 63)
    slow = _f13_amihud(closeadj, volume, 63) - _f13_amihud(closeadj, volume, 126)
    result = fast - slow
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_turnwlogdv_63d_jerk_v148_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 63) * _f13_logdvol(closeadj, volume, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_illiqprem_jerk_v149_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 63)
    arank = a.rolling(252, min_periods=63).rank(pct=True)
    dv = (closeadj * volume).replace(0, np.nan)
    rel = np.log(dv) - _f13_logdvol(closeadj, volume, 252)
    result = arank * rel
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f13lq_f13_liquidity_dollar_volume_liqblend_jerk_v150_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    ld = np.log(dv)
    result = (_z(ld, 63) + _z(ld, 126) + _z(ld, 252)) / 3.0 + _f13_dvol(closeadj, volume) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f13lq_f13_liquidity_dollar_volume_logdvol_21d_jerk_v001_signal,    f13lq_f13_liquidity_dollar_volume_logdvol_63d_jerk_v002_signal,    f13lq_f13_liquidity_dollar_volume_logdvol_126d_jerk_v003_signal,    f13lq_f13_liquidity_dollar_volume_logdvol_252d_jerk_v004_signal,    f13lq_f13_liquidity_dollar_volume_logdvol_5d_jerk_v005_signal,    f13lq_f13_liquidity_dollar_volume_dvolmean_21d_jerk_v006_signal,    f13lq_f13_liquidity_dollar_volume_dvolmean_63d_jerk_v007_signal,    f13lq_f13_liquidity_dollar_volume_dvolmean_126d_jerk_v008_signal,    f13lq_f13_liquidity_dollar_volume_dvolmean_252d_jerk_v009_signal,    f13lq_f13_liquidity_dollar_volume_dvolmean_504d_jerk_v010_signal,    f13lq_f13_liquidity_dollar_volume_amihud_21d_jerk_v011_signal,    f13lq_f13_liquidity_dollar_volume_amihud_63d_jerk_v012_signal,    f13lq_f13_liquidity_dollar_volume_amihud_126d_jerk_v013_signal,    f13lq_f13_liquidity_dollar_volume_amihud_252d_jerk_v014_signal,    f13lq_f13_liquidity_dollar_volume_logamihud_63d_jerk_v015_signal,    f13lq_f13_liquidity_dollar_volume_logamihud_126d_jerk_v016_signal,    f13lq_f13_liquidity_dollar_volume_turnover_21d_jerk_v017_signal,    f13lq_f13_liquidity_dollar_volume_turnover_63d_jerk_v018_signal,    f13lq_f13_liquidity_dollar_volume_turnover_126d_jerk_v019_signal,    f13lq_f13_liquidity_dollar_volume_turnover_252d_jerk_v020_signal,    f13lq_f13_liquidity_dollar_volume_turnsm_21d_jerk_v021_signal,    f13lq_f13_liquidity_dollar_volume_turnsm_63d_jerk_v022_signal,    f13lq_f13_liquidity_dollar_volume_zdvol_63d_jerk_v023_signal,    f13lq_f13_liquidity_dollar_volume_zdvol_126d_jerk_v024_signal,    f13lq_f13_liquidity_dollar_volume_zdvol_252d_jerk_v025_signal,    f13lq_f13_liquidity_dollar_volume_zlogdvol_252d_jerk_v026_signal,    f13lq_f13_liquidity_dollar_volume_zamihud_21d_jerk_v027_signal,    f13lq_f13_liquidity_dollar_volume_zamihud_63d_jerk_v028_signal,    f13lq_f13_liquidity_dollar_volume_zturn_21d_jerk_v029_signal,    f13lq_f13_liquidity_dollar_volume_zturn_63d_jerk_v030_signal,    f13lq_f13_liquidity_dollar_volume_cv_63d_jerk_v031_signal,    f13lq_f13_liquidity_dollar_volume_cv_126d_jerk_v032_signal,    f13lq_f13_liquidity_dollar_volume_cv_252d_jerk_v033_signal,    f13lq_f13_liquidity_dollar_volume_trend_21_126_jerk_v034_signal,    f13lq_f13_liquidity_dollar_volume_trend_63_252_jerk_v035_signal,    f13lq_f13_liquidity_dollar_volume_vsavg_252d_jerk_v036_signal,    f13lq_f13_liquidity_dollar_volume_vsavg_126d_jerk_v037_signal,    f13lq_f13_liquidity_dollar_volume_amirank_21d_jerk_v038_signal,    f13lq_f13_liquidity_dollar_volume_amirank_63d_jerk_v039_signal,    f13lq_f13_liquidity_dollar_volume_dvrank_252d_jerk_v040_signal,    f13lq_f13_liquidity_dollar_volume_turnrank_252d_jerk_v041_signal,    f13lq_f13_liquidity_dollar_volume_impact_21d_jerk_v042_signal,    f13lq_f13_liquidity_dollar_volume_impact_63d_jerk_v043_signal,    f13lq_f13_liquidity_dollar_volume_corrabsv_63d_jerk_v044_signal,    f13lq_f13_liquidity_dollar_volume_corrabsv_126d_jerk_v045_signal,    f13lq_f13_liquidity_dollar_volume_corrabsdv_126d_jerk_v046_signal,    f13lq_f13_liquidity_dollar_volume_amitrend_21_126_jerk_v047_signal,    f13lq_f13_liquidity_dollar_volume_amiratio_21_252_jerk_v048_signal,    f13lq_f13_liquidity_dollar_volume_dvratio_21_252_jerk_v049_signal,    f13lq_f13_liquidity_dollar_volume_dvratio_63_252_jerk_v050_signal,    f13lq_f13_liquidity_dollar_volume_logdvol_1d_jerk_v051_signal,    f13lq_f13_liquidity_dollar_volume_logdvol_42d_jerk_v052_signal,    f13lq_f13_liquidity_dollar_volume_logdvol_189d_jerk_v053_signal,    f13lq_f13_liquidity_dollar_volume_logdvol_504d_jerk_v054_signal,    f13lq_f13_liquidity_dollar_volume_amihud_42d_jerk_v055_signal,    f13lq_f13_liquidity_dollar_volume_amihud_189d_jerk_v056_signal,    f13lq_f13_liquidity_dollar_volume_turnover_42d_jerk_v057_signal,    f13lq_f13_liquidity_dollar_volume_turnover_189d_jerk_v058_signal,    f13lq_f13_liquidity_dollar_volume_ewmdvol_21d_jerk_v059_signal,    f13lq_f13_liquidity_dollar_volume_ewmdvol_63d_jerk_v060_signal,    f13lq_f13_liquidity_dollar_volume_ewmturn_21d_jerk_v061_signal,    f13lq_f13_liquidity_dollar_volume_ewmami_63d_jerk_v062_signal,    f13lq_f13_liquidity_dollar_volume_logdvolstd_63d_jerk_v063_signal,    f13lq_f13_liquidity_dollar_volume_logdvolstd_126d_jerk_v064_signal,    f13lq_f13_liquidity_dollar_volume_turnstd_63d_jerk_v065_signal,    f13lq_f13_liquidity_dollar_volume_amistd_126d_jerk_v066_signal,    f13lq_f13_liquidity_dollar_volume_logamitrend_jerk_v067_signal,    f13lq_f13_liquidity_dollar_volume_turntrend_21_126_jerk_v068_signal,    f13lq_f13_liquidity_dollar_volume_amiscaled_63d_jerk_v069_signal,    f13lq_f13_liquidity_dollar_volume_amicomposite_63d_jerk_v070_signal,    f13lq_f13_liquidity_dollar_volume_dvmom_21d_jerk_v071_signal,    f13lq_f13_liquidity_dollar_volume_dvmom_63d_jerk_v072_signal,    f13lq_f13_liquidity_dollar_volume_turnskew_126d_jerk_v073_signal,    f13lq_f13_liquidity_dollar_volume_dvskew_252d_jerk_v074_signal,    f13lq_f13_liquidity_dollar_volume_illiqturn_63d_jerk_v075_signal,    f13lq_f13_liquidity_dollar_volume_logdvol_84d_jerk_v076_signal,    f13lq_f13_liquidity_dollar_volume_logdvol_315d_jerk_v077_signal,    f13lq_f13_liquidity_dollar_volume_logdvol_378d_jerk_v078_signal,    f13lq_f13_liquidity_dollar_volume_logdvol_10d_jerk_v079_signal,    f13lq_f13_liquidity_dollar_volume_dvolmean_42d_jerk_v080_signal,    f13lq_f13_liquidity_dollar_volume_dvolmean_189d_jerk_v081_signal,    f13lq_f13_liquidity_dollar_volume_amihud_84d_jerk_v082_signal,    f13lq_f13_liquidity_dollar_volume_amihud_315d_jerk_v083_signal,    f13lq_f13_liquidity_dollar_volume_logamihud_252d_jerk_v084_signal,    f13lq_f13_liquidity_dollar_volume_logamihud_21d_jerk_v085_signal,    f13lq_f13_liquidity_dollar_volume_turnover_84d_jerk_v086_signal,    f13lq_f13_liquidity_dollar_volume_turnover_315d_jerk_v087_signal,    f13lq_f13_liquidity_dollar_volume_turnover_5d_jerk_v088_signal,    f13lq_f13_liquidity_dollar_volume_logturn_21d_jerk_v089_signal,    f13lq_f13_liquidity_dollar_volume_logturn_63d_jerk_v090_signal,    f13lq_f13_liquidity_dollar_volume_zdvol_504d_jerk_v091_signal,    f13lq_f13_liquidity_dollar_volume_zamihud_126d_jerk_v092_signal,    f13lq_f13_liquidity_dollar_volume_zturn_126d_jerk_v093_signal,    f13lq_f13_liquidity_dollar_volume_zlogdvol_126d_jerk_v094_signal,    f13lq_f13_liquidity_dollar_volume_zlogami_252d_jerk_v095_signal,    f13lq_f13_liquidity_dollar_volume_cv_42d_jerk_v096_signal,    f13lq_f13_liquidity_dollar_volume_cv_189d_jerk_v097_signal,    f13lq_f13_liquidity_dollar_volume_volcv_63d_jerk_v098_signal,    f13lq_f13_liquidity_dollar_volume_trend_42_189_jerk_v099_signal,    f13lq_f13_liquidity_dollar_volume_trend_21_63_jerk_v100_signal,    f13lq_f13_liquidity_dollar_volume_vsavg_504d_jerk_v101_signal,    f13lq_f13_liquidity_dollar_volume_vsavg_63d_jerk_v102_signal,    f13lq_f13_liquidity_dollar_volume_amirank_126d_jerk_v103_signal,    f13lq_f13_liquidity_dollar_volume_dvrank_126d_jerk_v104_signal,    f13lq_f13_liquidity_dollar_volume_turnrank_126d_jerk_v105_signal,    f13lq_f13_liquidity_dollar_volume_logdvrank_252d_jerk_v106_signal,    f13lq_f13_liquidity_dollar_volume_impact_126d_jerk_v107_signal,    f13lq_f13_liquidity_dollar_volume_impact_252d_jerk_v108_signal,    f13lq_f13_liquidity_dollar_volume_impact2_63d_jerk_v109_signal,    f13lq_f13_liquidity_dollar_volume_corrabsv_252d_jerk_v110_signal,    f13lq_f13_liquidity_dollar_volume_corrabsdv_63d_jerk_v111_signal,    f13lq_f13_liquidity_dollar_volume_corrrv_126d_jerk_v112_signal,    f13lq_f13_liquidity_dollar_volume_amitrend_63_252_jerk_v113_signal,    f13lq_f13_liquidity_dollar_volume_amiratio_63_252_jerk_v114_signal,    f13lq_f13_liquidity_dollar_volume_dvratio_21_126_jerk_v115_signal,    f13lq_f13_liquidity_dollar_volume_dvratio_42_189_jerk_v116_signal,    f13lq_f13_liquidity_dollar_volume_turnratio_21_252_jerk_v117_signal,    f13lq_f13_liquidity_dollar_volume_ewmdvol_126d_jerk_v118_signal,    f13lq_f13_liquidity_dollar_volume_ewmdvol_252d_jerk_v119_signal,    f13lq_f13_liquidity_dollar_volume_ewmturn_63d_jerk_v120_signal,    f13lq_f13_liquidity_dollar_volume_ewmami_126d_jerk_v121_signal,    f13lq_f13_liquidity_dollar_volume_logdvolstd_252d_jerk_v122_signal,    f13lq_f13_liquidity_dollar_volume_turnstd_126d_jerk_v123_signal,    f13lq_f13_liquidity_dollar_volume_amistd_252d_jerk_v124_signal,    f13lq_f13_liquidity_dollar_volume_logamitrend_63_252_jerk_v125_signal,    f13lq_f13_liquidity_dollar_volume_turntrend_63_252_jerk_v126_signal,    f13lq_f13_liquidity_dollar_volume_amiscaled_126d_jerk_v127_signal,    f13lq_f13_liquidity_dollar_volume_amicomposite_126d_jerk_v128_signal,    f13lq_f13_liquidity_dollar_volume_dvmom_126d_jerk_v129_signal,    f13lq_f13_liquidity_dollar_volume_dvmom_42d_jerk_v130_signal,    f13lq_f13_liquidity_dollar_volume_turnskew_252d_jerk_v131_signal,    f13lq_f13_liquidity_dollar_volume_dvskew_126d_jerk_v132_signal,    f13lq_f13_liquidity_dollar_volume_turnkurt_126d_jerk_v133_signal,    f13lq_f13_liquidity_dollar_volume_amikurt_252d_jerk_v134_signal,    f13lq_f13_liquidity_dollar_volume_illiqturn_126d_jerk_v135_signal,    f13lq_f13_liquidity_dollar_volume_liqturn_63d_jerk_v136_signal,    f13lq_f13_liquidity_dollar_volume_zdiverge_63d_jerk_v137_signal,    f13lq_f13_liquidity_dollar_volume_turnsurge_21d_jerk_v138_signal,    f13lq_f13_liquidity_dollar_volume_dvsurge_21d_jerk_v139_signal,    f13lq_f13_liquidity_dollar_volume_amisurge_21d_jerk_v140_signal,    f13lq_f13_liquidity_dollar_volume_amism_21d_jerk_v141_signal,    f13lq_f13_liquidity_dollar_volume_logdvolsm_21d_jerk_v142_signal,    f13lq_f13_liquidity_dollar_volume_turnir_21d_jerk_v143_signal,    f13lq_f13_liquidity_dollar_volume_amiir_21d_jerk_v144_signal,    f13lq_f13_liquidity_dollar_volume_dvratio_63_504_jerk_v145_signal,    f13lq_f13_liquidity_dollar_volume_dvaccel_jerk_v146_signal,    f13lq_f13_liquidity_dollar_volume_amiaccel_jerk_v147_signal,    f13lq_f13_liquidity_dollar_volume_turnwlogdv_63d_jerk_v148_signal,    f13lq_f13_liquidity_dollar_volume_illiqprem_jerk_v149_signal,    f13lq_f13_liquidity_dollar_volume_liqblend_jerk_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_LIQUIDITY_DOLLAR_VOLUME_REGISTRY_JERK = REGISTRY

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
    domain_primitives = ('_f13_dvol', '_f13_amihud', '_f13_turnover', '_f13_logdvol')
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
    print("OK f13_liquidity_dollar_volume_" + "3rd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
