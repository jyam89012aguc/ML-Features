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


# ============ FEATURES 001-075 ============

# 21d mean log dollar volume (monthly liquidity level)
def f13lq_f13_liquidity_dollar_volume_logdvol_21d_base_v001_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean log dollar volume (quarterly liquidity level)
def f13lq_f13_liquidity_dollar_volume_logdvol_63d_base_v002_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean log dollar volume
def f13lq_f13_liquidity_dollar_volume_logdvol_126d_base_v003_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean log dollar volume (annual liquidity level)
def f13lq_f13_liquidity_dollar_volume_logdvol_252d_base_v004_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d mean log dollar volume (weekly liquidity level)
def f13lq_f13_liquidity_dollar_volume_logdvol_5d_base_v005_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean dollar volume (raw level)
def f13lq_f13_liquidity_dollar_volume_dvolmean_21d_base_v006_signal(closeadj, volume):
    result = _mean(_f13_dvol(closeadj, volume), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean dollar volume (raw level)
def f13lq_f13_liquidity_dollar_volume_dvolmean_63d_base_v007_signal(closeadj, volume):
    result = _mean(_f13_dvol(closeadj, volume), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean dollar volume (raw level)
def f13lq_f13_liquidity_dollar_volume_dvolmean_126d_base_v008_signal(closeadj, volume):
    result = _mean(_f13_dvol(closeadj, volume), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean dollar volume (raw level)
def f13lq_f13_liquidity_dollar_volume_dvolmean_252d_base_v009_signal(closeadj, volume):
    result = _mean(_f13_dvol(closeadj, volume), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean dollar volume (two-year level)
def f13lq_f13_liquidity_dollar_volume_dvolmean_504d_base_v010_signal(closeadj, volume):
    result = _mean(_f13_dvol(closeadj, volume), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d Amihud illiquidity level
def f13lq_f13_liquidity_dollar_volume_amihud_21d_base_v011_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Amihud illiquidity level
def f13lq_f13_liquidity_dollar_volume_amihud_63d_base_v012_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d Amihud illiquidity level
def f13lq_f13_liquidity_dollar_volume_amihud_126d_base_v013_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Amihud illiquidity level
def f13lq_f13_liquidity_dollar_volume_amihud_252d_base_v014_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log of 63d Amihud illiquidity (compress fat tail)
def f13lq_f13_liquidity_dollar_volume_logamihud_63d_base_v015_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# log of 126d Amihud illiquidity
def f13lq_f13_liquidity_dollar_volume_logamihud_126d_base_v016_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d turnover ratio (volume vs 21d mean volume)
def f13lq_f13_liquidity_dollar_volume_turnover_21d_base_v017_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d turnover ratio
def f13lq_f13_liquidity_dollar_volume_turnover_63d_base_v018_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d turnover ratio
def f13lq_f13_liquidity_dollar_volume_turnover_126d_base_v019_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d turnover ratio
def f13lq_f13_liquidity_dollar_volume_turnover_252d_base_v020_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed turnover ratio (21d mean of 5d turnover)
def f13lq_f13_liquidity_dollar_volume_turnsm_21d_base_v021_signal(closeadj, volume):
    result = _mean(_f13_turnover(closeadj, volume, 5), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed turnover ratio (21d mean of 21d turnover)
def f13lq_f13_liquidity_dollar_volume_turnsm_63d_base_v022_signal(closeadj, volume):
    result = _mean(_f13_turnover(closeadj, volume, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of dollar volume over 63d
def f13lq_f13_liquidity_dollar_volume_zdvol_63d_base_v023_signal(closeadj, volume):
    result = _z(_f13_dvol(closeadj, volume), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of dollar volume over 126d
def f13lq_f13_liquidity_dollar_volume_zdvol_126d_base_v024_signal(closeadj, volume):
    result = _z(_f13_dvol(closeadj, volume), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of dollar volume over 252d
def f13lq_f13_liquidity_dollar_volume_zdvol_252d_base_v025_signal(closeadj, volume):
    result = _z(_f13_dvol(closeadj, volume), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of log dollar volume over 252d
def f13lq_f13_liquidity_dollar_volume_zlogdvol_252d_base_v026_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = _z(np.log(dv), 252) + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 21d Amihud over 252d
def f13lq_f13_liquidity_dollar_volume_zamihud_21d_base_v027_signal(closeadj, volume):
    result = _z(_f13_amihud(closeadj, volume, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d Amihud over 252d
def f13lq_f13_liquidity_dollar_volume_zamihud_63d_base_v028_signal(closeadj, volume):
    result = _z(_f13_amihud(closeadj, volume, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 21d turnover over 126d
def f13lq_f13_liquidity_dollar_volume_zturn_21d_base_v029_signal(closeadj, volume):
    result = _z(_f13_turnover(closeadj, volume, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d turnover over 252d
def f13lq_f13_liquidity_dollar_volume_zturn_63d_base_v030_signal(closeadj, volume):
    result = _z(_f13_turnover(closeadj, volume, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume coefficient of variation over 63d
def f13lq_f13_liquidity_dollar_volume_cv_63d_base_v031_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_std(dv, 63), _mean(dv, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume coefficient of variation over 126d
def f13lq_f13_liquidity_dollar_volume_cv_126d_base_v032_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_std(dv, 126), _mean(dv, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume coefficient of variation over 252d
def f13lq_f13_liquidity_dollar_volume_cv_252d_base_v033_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_std(dv, 252), _mean(dv, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity trend slope: 21d mean log dvol minus 126d mean log dvol
def f13lq_f13_liquidity_dollar_volume_trend_21_126_base_v034_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 21) - _f13_logdvol(closeadj, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity trend slope: 63d mean log dvol minus 252d mean log dvol
def f13lq_f13_liquidity_dollar_volume_trend_63_252_base_v035_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 63) - _f13_logdvol(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity vs 252d average: log dvol level minus 252d mean log dvol
def f13lq_f13_liquidity_dollar_volume_vsavg_252d_base_v036_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv) - _f13_logdvol(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity vs 126d average: log dvol level minus 126d mean log dvol
def f13lq_f13_liquidity_dollar_volume_vsavg_126d_base_v037_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv) - _f13_logdvol(closeadj, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity percentile rank of 21d Amihud over 252d
def f13lq_f13_liquidity_dollar_volume_amirank_21d_base_v038_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 21)
    result = a.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity percentile rank of 63d Amihud over 252d
def f13lq_f13_liquidity_dollar_volume_amirank_63d_base_v039_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 63)
    result = a.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume percentile rank over 252d (liquidity rank)
def f13lq_f13_liquidity_dollar_volume_dvrank_252d_base_v040_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = dv.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# turnover percentile rank over 252d
def f13lq_f13_liquidity_dollar_volume_turnrank_252d_base_v041_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = t.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# price-impact proxy: |return| per unit log dollar volume (21d mean)
def f13lq_f13_liquidity_dollar_volume_impact_21d_base_v042_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    result = _mean(_safe_div(r, np.log(dv)), 21) + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price-impact proxy over 63d
def f13lq_f13_liquidity_dollar_volume_impact_63d_base_v043_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    result = _mean(_safe_div(r, np.log(dv)), 63) + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling correlation of |return| and volume over 63d (illiquidity coupling)
def f13lq_f13_liquidity_dollar_volume_corrabsv_63d_base_v044_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    result = r.rolling(63, min_periods=21).corr(volume) + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling correlation of |return| and volume over 126d
def f13lq_f13_liquidity_dollar_volume_corrabsv_126d_base_v045_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    result = r.rolling(126, min_periods=42).corr(volume) + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling correlation of |return| and dollar volume over 126d
def f13lq_f13_liquidity_dollar_volume_corrabsdv_126d_base_v046_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    dv = _f13_dvol(closeadj, volume)
    result = r.rolling(126, min_periods=42).corr(dv)
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud trend: 21d Amihud minus 126d Amihud
def f13lq_f13_liquidity_dollar_volume_amitrend_21_126_base_v047_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 21) - _f13_amihud(closeadj, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud ratio: 21d Amihud over 252d Amihud (illiquidity surge)
def f13lq_f13_liquidity_dollar_volume_amiratio_21_252_base_v048_signal(closeadj, volume):
    result = _safe_div(_f13_amihud(closeadj, volume, 21), _f13_amihud(closeadj, volume, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume ratio: 21d mean over 252d mean (liquidity surge)
def f13lq_f13_liquidity_dollar_volume_dvratio_21_252_base_v049_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_mean(dv, 21), _mean(dv, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume ratio: 63d mean over 252d mean
def f13lq_f13_liquidity_dollar_volume_dvratio_63_252_base_v050_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_mean(dv, 63), _mean(dv, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# log dollar-volume level (raw, single-day) anchored
def f13lq_f13_liquidity_dollar_volume_logdvol_1d_base_v051_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv) + _f13_logdvol(closeadj, volume, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d mean log dollar volume
def f13lq_f13_liquidity_dollar_volume_logdvol_42d_base_v052_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d mean log dollar volume
def f13lq_f13_liquidity_dollar_volume_logdvol_189d_base_v053_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean log dollar volume (two-year)
def f13lq_f13_liquidity_dollar_volume_logdvol_504d_base_v054_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d Amihud illiquidity level
def f13lq_f13_liquidity_dollar_volume_amihud_42d_base_v055_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d Amihud illiquidity level
def f13lq_f13_liquidity_dollar_volume_amihud_189d_base_v056_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d turnover ratio
def f13lq_f13_liquidity_dollar_volume_turnover_42d_base_v057_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d turnover ratio
def f13lq_f13_liquidity_dollar_volume_turnover_189d_base_v058_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of log dollar volume span 21
def f13lq_f13_liquidity_dollar_volume_ewmdvol_21d_base_v059_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv).ewm(span=21, min_periods=10).mean() + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of log dollar volume span 63
def f13lq_f13_liquidity_dollar_volume_ewmdvol_63d_base_v060_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv).ewm(span=63, min_periods=21).mean() + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of turnover span 21
def f13lq_f13_liquidity_dollar_volume_ewmturn_21d_base_v061_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = t.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of Amihud illiquidity span 63
def f13lq_f13_liquidity_dollar_volume_ewmami_63d_base_v062_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 21)
    result = a.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume dispersion of log dvol over 63d (liquidity volatility)
def f13lq_f13_liquidity_dollar_volume_logdvolstd_63d_base_v063_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = _std(np.log(dv), 63) + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume dispersion of log dvol over 126d
def f13lq_f13_liquidity_dollar_volume_logdvolstd_126d_base_v064_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = _std(np.log(dv), 126) + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# turnover dispersion over 63d (turnover instability)
def f13lq_f13_liquidity_dollar_volume_turnstd_63d_base_v065_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = _std(t, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud dispersion over 126d (illiquidity instability)
def f13lq_f13_liquidity_dollar_volume_amistd_126d_base_v066_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 21)
    result = _std(a, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# log Amihud trend: 21d log Amihud minus 126d log Amihud
def f13lq_f13_liquidity_dollar_volume_logamitrend_base_v067_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 21)) - np.log(_f13_amihud(closeadj, volume, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# turnover trend: 21d turnover minus 126d turnover
def f13lq_f13_liquidity_dollar_volume_turntrend_21_126_base_v068_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 21) - _f13_turnover(closeadj, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud scaled by its 252d dispersion (standardized illiquidity, robust)
def f13lq_f13_liquidity_dollar_volume_amiscaled_63d_base_v069_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 63)
    result = _safe_div(a, _std(a, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud-to-liquidity composite: log Amihud minus log dvol (illiquidity premium proxy)
def f13lq_f13_liquidity_dollar_volume_amicomposite_63d_base_v070_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 63)) - _f13_logdvol(closeadj, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume momentum: 21d log change of 21d mean dvol
def f13lq_f13_liquidity_dollar_volume_dvmom_21d_base_v071_signal(closeadj, volume):
    m = _mean(_f13_dvol(closeadj, volume), 21).replace(0, np.nan)
    result = np.log(m / m.shift(21))
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume momentum: 63d log change of 63d mean dvol
def f13lq_f13_liquidity_dollar_volume_dvmom_63d_base_v072_signal(closeadj, volume):
    m = _mean(_f13_dvol(closeadj, volume), 63).replace(0, np.nan)
    result = np.log(m / m.shift(63))
    return result.replace([np.inf, -np.inf], np.nan)


# turnover skew over 126d (asymmetry of liquidity shocks)
def f13lq_f13_liquidity_dollar_volume_turnskew_126d_base_v073_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = t.rolling(126, min_periods=42).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# log dollar-volume skew over 252d
def f13lq_f13_liquidity_dollar_volume_dvskew_252d_base_v074_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv).rolling(252, min_periods=84).skew() + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity-weighted turnover: turnover scaled by 63d Amihud rank
def f13lq_f13_liquidity_dollar_volume_illiqturn_63d_base_v075_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 63)
    arank = a.rolling(252, min_periods=63).rank(pct=True)
    result = _f13_turnover(closeadj, volume, 21) * arank
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13lq_f13_liquidity_dollar_volume_logdvol_21d_base_v001_signal,
    f13lq_f13_liquidity_dollar_volume_logdvol_63d_base_v002_signal,
    f13lq_f13_liquidity_dollar_volume_logdvol_126d_base_v003_signal,
    f13lq_f13_liquidity_dollar_volume_logdvol_252d_base_v004_signal,
    f13lq_f13_liquidity_dollar_volume_logdvol_5d_base_v005_signal,
    f13lq_f13_liquidity_dollar_volume_dvolmean_21d_base_v006_signal,
    f13lq_f13_liquidity_dollar_volume_dvolmean_63d_base_v007_signal,
    f13lq_f13_liquidity_dollar_volume_dvolmean_126d_base_v008_signal,
    f13lq_f13_liquidity_dollar_volume_dvolmean_252d_base_v009_signal,
    f13lq_f13_liquidity_dollar_volume_dvolmean_504d_base_v010_signal,
    f13lq_f13_liquidity_dollar_volume_amihud_21d_base_v011_signal,
    f13lq_f13_liquidity_dollar_volume_amihud_63d_base_v012_signal,
    f13lq_f13_liquidity_dollar_volume_amihud_126d_base_v013_signal,
    f13lq_f13_liquidity_dollar_volume_amihud_252d_base_v014_signal,
    f13lq_f13_liquidity_dollar_volume_logamihud_63d_base_v015_signal,
    f13lq_f13_liquidity_dollar_volume_logamihud_126d_base_v016_signal,
    f13lq_f13_liquidity_dollar_volume_turnover_21d_base_v017_signal,
    f13lq_f13_liquidity_dollar_volume_turnover_63d_base_v018_signal,
    f13lq_f13_liquidity_dollar_volume_turnover_126d_base_v019_signal,
    f13lq_f13_liquidity_dollar_volume_turnover_252d_base_v020_signal,
    f13lq_f13_liquidity_dollar_volume_turnsm_21d_base_v021_signal,
    f13lq_f13_liquidity_dollar_volume_turnsm_63d_base_v022_signal,
    f13lq_f13_liquidity_dollar_volume_zdvol_63d_base_v023_signal,
    f13lq_f13_liquidity_dollar_volume_zdvol_126d_base_v024_signal,
    f13lq_f13_liquidity_dollar_volume_zdvol_252d_base_v025_signal,
    f13lq_f13_liquidity_dollar_volume_zlogdvol_252d_base_v026_signal,
    f13lq_f13_liquidity_dollar_volume_zamihud_21d_base_v027_signal,
    f13lq_f13_liquidity_dollar_volume_zamihud_63d_base_v028_signal,
    f13lq_f13_liquidity_dollar_volume_zturn_21d_base_v029_signal,
    f13lq_f13_liquidity_dollar_volume_zturn_63d_base_v030_signal,
    f13lq_f13_liquidity_dollar_volume_cv_63d_base_v031_signal,
    f13lq_f13_liquidity_dollar_volume_cv_126d_base_v032_signal,
    f13lq_f13_liquidity_dollar_volume_cv_252d_base_v033_signal,
    f13lq_f13_liquidity_dollar_volume_trend_21_126_base_v034_signal,
    f13lq_f13_liquidity_dollar_volume_trend_63_252_base_v035_signal,
    f13lq_f13_liquidity_dollar_volume_vsavg_252d_base_v036_signal,
    f13lq_f13_liquidity_dollar_volume_vsavg_126d_base_v037_signal,
    f13lq_f13_liquidity_dollar_volume_amirank_21d_base_v038_signal,
    f13lq_f13_liquidity_dollar_volume_amirank_63d_base_v039_signal,
    f13lq_f13_liquidity_dollar_volume_dvrank_252d_base_v040_signal,
    f13lq_f13_liquidity_dollar_volume_turnrank_252d_base_v041_signal,
    f13lq_f13_liquidity_dollar_volume_impact_21d_base_v042_signal,
    f13lq_f13_liquidity_dollar_volume_impact_63d_base_v043_signal,
    f13lq_f13_liquidity_dollar_volume_corrabsv_63d_base_v044_signal,
    f13lq_f13_liquidity_dollar_volume_corrabsv_126d_base_v045_signal,
    f13lq_f13_liquidity_dollar_volume_corrabsdv_126d_base_v046_signal,
    f13lq_f13_liquidity_dollar_volume_amitrend_21_126_base_v047_signal,
    f13lq_f13_liquidity_dollar_volume_amiratio_21_252_base_v048_signal,
    f13lq_f13_liquidity_dollar_volume_dvratio_21_252_base_v049_signal,
    f13lq_f13_liquidity_dollar_volume_dvratio_63_252_base_v050_signal,
    f13lq_f13_liquidity_dollar_volume_logdvol_1d_base_v051_signal,
    f13lq_f13_liquidity_dollar_volume_logdvol_42d_base_v052_signal,
    f13lq_f13_liquidity_dollar_volume_logdvol_189d_base_v053_signal,
    f13lq_f13_liquidity_dollar_volume_logdvol_504d_base_v054_signal,
    f13lq_f13_liquidity_dollar_volume_amihud_42d_base_v055_signal,
    f13lq_f13_liquidity_dollar_volume_amihud_189d_base_v056_signal,
    f13lq_f13_liquidity_dollar_volume_turnover_42d_base_v057_signal,
    f13lq_f13_liquidity_dollar_volume_turnover_189d_base_v058_signal,
    f13lq_f13_liquidity_dollar_volume_ewmdvol_21d_base_v059_signal,
    f13lq_f13_liquidity_dollar_volume_ewmdvol_63d_base_v060_signal,
    f13lq_f13_liquidity_dollar_volume_ewmturn_21d_base_v061_signal,
    f13lq_f13_liquidity_dollar_volume_ewmami_63d_base_v062_signal,
    f13lq_f13_liquidity_dollar_volume_logdvolstd_63d_base_v063_signal,
    f13lq_f13_liquidity_dollar_volume_logdvolstd_126d_base_v064_signal,
    f13lq_f13_liquidity_dollar_volume_turnstd_63d_base_v065_signal,
    f13lq_f13_liquidity_dollar_volume_amistd_126d_base_v066_signal,
    f13lq_f13_liquidity_dollar_volume_logamitrend_base_v067_signal,
    f13lq_f13_liquidity_dollar_volume_turntrend_21_126_base_v068_signal,
    f13lq_f13_liquidity_dollar_volume_amiscaled_63d_base_v069_signal,
    f13lq_f13_liquidity_dollar_volume_amicomposite_63d_base_v070_signal,
    f13lq_f13_liquidity_dollar_volume_dvmom_21d_base_v071_signal,
    f13lq_f13_liquidity_dollar_volume_dvmom_63d_base_v072_signal,
    f13lq_f13_liquidity_dollar_volume_turnskew_126d_base_v073_signal,
    f13lq_f13_liquidity_dollar_volume_dvskew_252d_base_v074_signal,
    f13lq_f13_liquidity_dollar_volume_illiqturn_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_LIQUIDITY_DOLLAR_VOLUME_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0008, 0.045, n)
    closeadj = pd.Series(50.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name="volume")
    cols = {"closeadj": closeadj, "volume": volume}

    domain_primitives = ("_f13_dvol", "_f13_amihud", "_f13_turnover", "_f13_logdvol")
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f13_liquidity_dollar_volume_base_001_075_claude: {n_features} features pass")
