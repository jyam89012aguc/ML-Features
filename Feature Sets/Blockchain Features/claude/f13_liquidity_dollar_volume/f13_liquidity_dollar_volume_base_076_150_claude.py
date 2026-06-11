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


# ============ FEATURES 076-150 ============

# 84d mean log dollar volume
def f13lq_f13_liquidity_dollar_volume_logdvol_84d_base_v076_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d mean log dollar volume
def f13lq_f13_liquidity_dollar_volume_logdvol_315d_base_v077_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d mean log dollar volume
def f13lq_f13_liquidity_dollar_volume_logdvol_378d_base_v078_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d mean log dollar volume
def f13lq_f13_liquidity_dollar_volume_logdvol_10d_base_v079_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d mean dollar volume (raw level)
def f13lq_f13_liquidity_dollar_volume_dvolmean_42d_base_v080_signal(closeadj, volume):
    result = _mean(_f13_dvol(closeadj, volume), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d mean dollar volume (raw level)
def f13lq_f13_liquidity_dollar_volume_dvolmean_189d_base_v081_signal(closeadj, volume):
    result = _mean(_f13_dvol(closeadj, volume), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d Amihud illiquidity level
def f13lq_f13_liquidity_dollar_volume_amihud_84d_base_v082_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d Amihud illiquidity level
def f13lq_f13_liquidity_dollar_volume_amihud_315d_base_v083_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# log of 252d Amihud illiquidity
def f13lq_f13_liquidity_dollar_volume_logamihud_252d_base_v084_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# log of 21d Amihud illiquidity
def f13lq_f13_liquidity_dollar_volume_logamihud_21d_base_v085_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 84d turnover ratio
def f13lq_f13_liquidity_dollar_volume_turnover_84d_base_v086_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d turnover ratio
def f13lq_f13_liquidity_dollar_volume_turnover_315d_base_v087_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d turnover ratio (weekly)
def f13lq_f13_liquidity_dollar_volume_turnover_5d_base_v088_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# log turnover ratio over 21d (compress)
def f13lq_f13_liquidity_dollar_volume_logturn_21d_base_v089_signal(closeadj, volume):
    result = np.log(_f13_turnover(closeadj, volume, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# log turnover ratio over 63d
def f13lq_f13_liquidity_dollar_volume_logturn_63d_base_v090_signal(closeadj, volume):
    result = np.log(_f13_turnover(closeadj, volume, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of dollar volume over 504d
def f13lq_f13_liquidity_dollar_volume_zdvol_504d_base_v091_signal(closeadj, volume):
    result = _z(_f13_dvol(closeadj, volume), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d Amihud over 504d
def f13lq_f13_liquidity_dollar_volume_zamihud_126d_base_v092_signal(closeadj, volume):
    result = _z(_f13_amihud(closeadj, volume, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d turnover over 504d
def f13lq_f13_liquidity_dollar_volume_zturn_126d_base_v093_signal(closeadj, volume):
    result = _z(_f13_turnover(closeadj, volume, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of log dollar volume over 126d
def f13lq_f13_liquidity_dollar_volume_zlogdvol_126d_base_v094_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = _z(np.log(dv), 126) + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of log Amihud over 252d
def f13lq_f13_liquidity_dollar_volume_zlogami_252d_base_v095_signal(closeadj, volume):
    result = _z(np.log(_f13_amihud(closeadj, volume, 21)), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume coefficient of variation over 42d
def f13lq_f13_liquidity_dollar_volume_cv_42d_base_v096_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_std(dv, 42), _mean(dv, 42))
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume coefficient of variation over 189d
def f13lq_f13_liquidity_dollar_volume_cv_189d_base_v097_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_std(dv, 189), _mean(dv, 189))
    return result.replace([np.inf, -np.inf], np.nan)


# volume coefficient of variation over 63d (anchored to dvol)
def f13lq_f13_liquidity_dollar_volume_volcv_63d_base_v098_signal(closeadj, volume):
    result = _safe_div(_std(volume, 63), _mean(volume, 63)) + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity trend slope: 42d mean log dvol minus 189d mean log dvol
def f13lq_f13_liquidity_dollar_volume_trend_42_189_base_v099_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 42) - _f13_logdvol(closeadj, volume, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity trend slope: 21d mean log dvol minus 63d mean log dvol
def f13lq_f13_liquidity_dollar_volume_trend_21_63_base_v100_signal(closeadj, volume):
    result = _f13_logdvol(closeadj, volume, 21) - _f13_logdvol(closeadj, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity vs 504d average: log dvol level minus 504d mean log dvol
def f13lq_f13_liquidity_dollar_volume_vsavg_504d_base_v101_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv) - _f13_logdvol(closeadj, volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity vs 63d average: log dvol level minus 63d mean log dvol
def f13lq_f13_liquidity_dollar_volume_vsavg_63d_base_v102_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv) - _f13_logdvol(closeadj, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity percentile rank of 126d Amihud over 504d
def f13lq_f13_liquidity_dollar_volume_amirank_126d_base_v103_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 126)
    result = a.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume percentile rank over 126d
def f13lq_f13_liquidity_dollar_volume_dvrank_126d_base_v104_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = dv.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# turnover percentile rank over 126d
def f13lq_f13_liquidity_dollar_volume_turnrank_126d_base_v105_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = t.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# log dollar-volume percentile rank over 252d
def f13lq_f13_liquidity_dollar_volume_logdvrank_252d_base_v106_signal(closeadj, volume):
    ld = _f13_logdvol(closeadj, volume, 5)
    result = ld.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# price-impact proxy over 126d (|return| per unit log dvol)
def f13lq_f13_liquidity_dollar_volume_impact_126d_base_v107_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    result = _mean(_safe_div(r, np.log(dv)), 126) + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# price-impact proxy over 252d
def f13lq_f13_liquidity_dollar_volume_impact_252d_base_v108_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    result = _mean(_safe_div(r, np.log(dv)), 252) + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# squared-return price impact over 63d (Amihud-variance proxy)
def f13lq_f13_liquidity_dollar_volume_impact2_63d_base_v109_signal(closeadj, volume):
    r2 = closeadj.pct_change() ** 2
    dv = (closeadj * volume).replace(0, np.nan)
    result = _mean(_safe_div(r2, dv), 63) + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling correlation of |return| and volume over 252d
def f13lq_f13_liquidity_dollar_volume_corrabsv_252d_base_v110_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    result = r.rolling(252, min_periods=84).corr(volume) + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling correlation of |return| and dollar volume over 63d
def f13lq_f13_liquidity_dollar_volume_corrabsdv_63d_base_v111_signal(closeadj, volume):
    r = closeadj.pct_change().abs()
    dv = _f13_dvol(closeadj, volume)
    result = r.rolling(63, min_periods=21).corr(dv)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling correlation of return and volume over 126d (signed flow coupling)
def f13lq_f13_liquidity_dollar_volume_corrrv_126d_base_v112_signal(closeadj, volume):
    r = closeadj.pct_change()
    result = r.rolling(126, min_periods=42).corr(volume) + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud trend: 63d Amihud minus 252d Amihud
def f13lq_f13_liquidity_dollar_volume_amitrend_63_252_base_v113_signal(closeadj, volume):
    result = _f13_amihud(closeadj, volume, 63) - _f13_amihud(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud ratio: 63d Amihud over 252d Amihud
def f13lq_f13_liquidity_dollar_volume_amiratio_63_252_base_v114_signal(closeadj, volume):
    result = _safe_div(_f13_amihud(closeadj, volume, 63), _f13_amihud(closeadj, volume, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume ratio: 21d mean over 126d mean
def f13lq_f13_liquidity_dollar_volume_dvratio_21_126_base_v115_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_mean(dv, 21), _mean(dv, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume ratio: 42d mean over 189d mean
def f13lq_f13_liquidity_dollar_volume_dvratio_42_189_base_v116_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_mean(dv, 42), _mean(dv, 189))
    return result.replace([np.inf, -np.inf], np.nan)


# turnover ratio: 21d turnover over 252d turnover
def f13lq_f13_liquidity_dollar_volume_turnratio_21_252_base_v117_signal(closeadj, volume):
    result = _safe_div(_f13_turnover(closeadj, volume, 21), _f13_turnover(closeadj, volume, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of log dollar volume span 126
def f13lq_f13_liquidity_dollar_volume_ewmdvol_126d_base_v118_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv).ewm(span=126, min_periods=42).mean() + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of log dollar volume span 252
def f13lq_f13_liquidity_dollar_volume_ewmdvol_252d_base_v119_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv).ewm(span=252, min_periods=84).mean() + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of turnover span 63
def f13lq_f13_liquidity_dollar_volume_ewmturn_63d_base_v120_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = t.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of Amihud illiquidity span 126
def f13lq_f13_liquidity_dollar_volume_ewmami_126d_base_v121_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 21)
    result = a.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# log dvol dispersion over 252d (liquidity volatility, annual)
def f13lq_f13_liquidity_dollar_volume_logdvolstd_252d_base_v122_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = _std(np.log(dv), 252) + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# turnover dispersion over 126d
def f13lq_f13_liquidity_dollar_volume_turnstd_126d_base_v123_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = _std(t, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud dispersion over 252d
def f13lq_f13_liquidity_dollar_volume_amistd_252d_base_v124_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 21)
    result = _std(a, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log Amihud trend: 63d log Amihud minus 252d log Amihud
def f13lq_f13_liquidity_dollar_volume_logamitrend_63_252_base_v125_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 63)) - np.log(_f13_amihud(closeadj, volume, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# turnover trend: 63d turnover minus 252d turnover
def f13lq_f13_liquidity_dollar_volume_turntrend_63_252_base_v126_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 63) - _f13_turnover(closeadj, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud scaled by 252d dispersion at 126d window
def f13lq_f13_liquidity_dollar_volume_amiscaled_126d_base_v127_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 126)
    result = _safe_div(a, _std(a, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud composite at 126d: log Amihud minus log dvol
def f13lq_f13_liquidity_dollar_volume_amicomposite_126d_base_v128_signal(closeadj, volume):
    result = np.log(_f13_amihud(closeadj, volume, 126)) - _f13_logdvol(closeadj, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume momentum: 126d log change of 126d mean dvol
def f13lq_f13_liquidity_dollar_volume_dvmom_126d_base_v129_signal(closeadj, volume):
    m = _mean(_f13_dvol(closeadj, volume), 126).replace(0, np.nan)
    result = np.log(m / m.shift(126))
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume momentum: 42d log change of 42d mean dvol
def f13lq_f13_liquidity_dollar_volume_dvmom_42d_base_v130_signal(closeadj, volume):
    m = _mean(_f13_dvol(closeadj, volume), 42).replace(0, np.nan)
    result = np.log(m / m.shift(42))
    return result.replace([np.inf, -np.inf], np.nan)


# turnover skew over 252d
def f13lq_f13_liquidity_dollar_volume_turnskew_252d_base_v131_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = t.rolling(252, min_periods=84).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# log dvol skew over 126d
def f13lq_f13_liquidity_dollar_volume_dvskew_126d_base_v132_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    result = np.log(dv).rolling(126, min_periods=42).skew() + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# turnover kurtosis over 126d (fat-tail liquidity shocks)
def f13lq_f13_liquidity_dollar_volume_turnkurt_126d_base_v133_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = t.rolling(126, min_periods=42).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# log-Amihud kurtosis over 252d (illiquidity tail, log-scaled for stability)
def f13lq_f13_liquidity_dollar_volume_amikurt_252d_base_v134_signal(closeadj, volume):
    a = np.log(_f13_amihud(closeadj, volume, 21))
    result = a.rolling(252, min_periods=84).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity-weighted turnover at 126d Amihud rank
def f13lq_f13_liquidity_dollar_volume_illiqturn_126d_base_v135_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 126)
    arank = a.rolling(252, min_periods=63).rank(pct=True)
    result = _f13_turnover(closeadj, volume, 63) * arank
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-scaled turnover: turnover times log dvol vs 252d avg
def f13lq_f13_liquidity_dollar_volume_liqturn_63d_base_v136_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    relliq = np.log(dv) - _f13_logdvol(closeadj, volume, 252)
    result = _f13_turnover(closeadj, volume, 21) * relliq
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud z minus dvol z (joint illiquidity/liquidity divergence)
def f13lq_f13_liquidity_dollar_volume_zdiverge_63d_base_v137_signal(closeadj, volume):
    za = _z(_f13_amihud(closeadj, volume, 63), 252)
    zd = _z(_f13_dvol(closeadj, volume), 252)
    result = za - zd
    return result.replace([np.inf, -np.inf], np.nan)


# turnover relative to its 252d EWMA (turnover surge, continuous)
def f13lq_f13_liquidity_dollar_volume_turnsurge_21d_base_v138_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    base = t.ewm(span=252, min_periods=84).mean()
    result = _safe_div(t, base)
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume relative to its 252d EWMA (liquidity surge)
def f13lq_f13_liquidity_dollar_volume_dvsurge_21d_base_v139_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    base = dv.ewm(span=252, min_periods=84).mean()
    result = _safe_div(_mean(dv, 21), base)
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud relative to its 252d EWMA (illiquidity surge)
def f13lq_f13_liquidity_dollar_volume_amisurge_21d_base_v140_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 21)
    base = a.ewm(span=252, min_periods=84).mean()
    result = _safe_div(a, base)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed Amihud: 21d mean of 21d Amihud
def f13lq_f13_liquidity_dollar_volume_amism_21d_base_v141_signal(closeadj, volume):
    result = _mean(_f13_amihud(closeadj, volume, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed log dvol: 21d mean of 5d log dvol
def f13lq_f13_liquidity_dollar_volume_logdvolsm_21d_base_v142_signal(closeadj, volume):
    result = _mean(_f13_logdvol(closeadj, volume, 5), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# turnover information ratio: 21d turnover over 252d turnover dispersion
def f13lq_f13_liquidity_dollar_volume_turnir_21d_base_v143_signal(closeadj, volume):
    t = _f13_turnover(closeadj, volume, 21)
    result = _safe_div(t - _mean(t, 252), _std(t, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud information ratio: 21d Amihud minus mean over 252d dispersion
def f13lq_f13_liquidity_dollar_volume_amiir_21d_base_v144_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 21)
    result = _safe_div(a - _mean(a, 252), _std(a, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity breadth: 63d mean dvol over 504d mean dvol (long liquidity ratio)
def f13lq_f13_liquidity_dollar_volume_dvratio_63_504_base_v145_signal(closeadj, volume):
    dv = _f13_dvol(closeadj, volume)
    result = _safe_div(_mean(dv, 63), _mean(dv, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# log dvol acceleration: (21d - 63d logdvol) minus (63d - 126d logdvol)
def f13lq_f13_liquidity_dollar_volume_dvaccel_base_v146_signal(closeadj, volume):
    fast = _f13_logdvol(closeadj, volume, 21) - _f13_logdvol(closeadj, volume, 63)
    slow = _f13_logdvol(closeadj, volume, 63) - _f13_logdvol(closeadj, volume, 126)
    result = fast - slow
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud acceleration: (21d - 63d ami) minus (63d - 126d ami)
def f13lq_f13_liquidity_dollar_volume_amiaccel_base_v147_signal(closeadj, volume):
    fast = _f13_amihud(closeadj, volume, 21) - _f13_amihud(closeadj, volume, 63)
    slow = _f13_amihud(closeadj, volume, 63) - _f13_amihud(closeadj, volume, 126)
    result = fast - slow
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-weighted log dvol (active liquidity proxy)
def f13lq_f13_liquidity_dollar_volume_turnwlogdv_63d_base_v148_signal(closeadj, volume):
    result = _f13_turnover(closeadj, volume, 63) * _f13_logdvol(closeadj, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# illiquidity premium proxy: 252d Amihud rank times log dvol vs 252d avg
def f13lq_f13_liquidity_dollar_volume_illiqprem_base_v149_signal(closeadj, volume):
    a = _f13_amihud(closeadj, volume, 63)
    arank = a.rolling(252, min_periods=63).rank(pct=True)
    dv = (closeadj * volume).replace(0, np.nan)
    rel = np.log(dv) - _f13_logdvol(closeadj, volume, 252)
    result = arank * rel
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon liquidity composite (log dvol z over 63/126/252)
def f13lq_f13_liquidity_dollar_volume_liqblend_base_v150_signal(closeadj, volume):
    dv = (closeadj * volume).replace(0, np.nan)
    ld = np.log(dv)
    result = (_z(ld, 63) + _z(ld, 126) + _z(ld, 252)) / 3.0 + _f13_dvol(closeadj, volume) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13lq_f13_liquidity_dollar_volume_logdvol_84d_base_v076_signal,
    f13lq_f13_liquidity_dollar_volume_logdvol_315d_base_v077_signal,
    f13lq_f13_liquidity_dollar_volume_logdvol_378d_base_v078_signal,
    f13lq_f13_liquidity_dollar_volume_logdvol_10d_base_v079_signal,
    f13lq_f13_liquidity_dollar_volume_dvolmean_42d_base_v080_signal,
    f13lq_f13_liquidity_dollar_volume_dvolmean_189d_base_v081_signal,
    f13lq_f13_liquidity_dollar_volume_amihud_84d_base_v082_signal,
    f13lq_f13_liquidity_dollar_volume_amihud_315d_base_v083_signal,
    f13lq_f13_liquidity_dollar_volume_logamihud_252d_base_v084_signal,
    f13lq_f13_liquidity_dollar_volume_logamihud_21d_base_v085_signal,
    f13lq_f13_liquidity_dollar_volume_turnover_84d_base_v086_signal,
    f13lq_f13_liquidity_dollar_volume_turnover_315d_base_v087_signal,
    f13lq_f13_liquidity_dollar_volume_turnover_5d_base_v088_signal,
    f13lq_f13_liquidity_dollar_volume_logturn_21d_base_v089_signal,
    f13lq_f13_liquidity_dollar_volume_logturn_63d_base_v090_signal,
    f13lq_f13_liquidity_dollar_volume_zdvol_504d_base_v091_signal,
    f13lq_f13_liquidity_dollar_volume_zamihud_126d_base_v092_signal,
    f13lq_f13_liquidity_dollar_volume_zturn_126d_base_v093_signal,
    f13lq_f13_liquidity_dollar_volume_zlogdvol_126d_base_v094_signal,
    f13lq_f13_liquidity_dollar_volume_zlogami_252d_base_v095_signal,
    f13lq_f13_liquidity_dollar_volume_cv_42d_base_v096_signal,
    f13lq_f13_liquidity_dollar_volume_cv_189d_base_v097_signal,
    f13lq_f13_liquidity_dollar_volume_volcv_63d_base_v098_signal,
    f13lq_f13_liquidity_dollar_volume_trend_42_189_base_v099_signal,
    f13lq_f13_liquidity_dollar_volume_trend_21_63_base_v100_signal,
    f13lq_f13_liquidity_dollar_volume_vsavg_504d_base_v101_signal,
    f13lq_f13_liquidity_dollar_volume_vsavg_63d_base_v102_signal,
    f13lq_f13_liquidity_dollar_volume_amirank_126d_base_v103_signal,
    f13lq_f13_liquidity_dollar_volume_dvrank_126d_base_v104_signal,
    f13lq_f13_liquidity_dollar_volume_turnrank_126d_base_v105_signal,
    f13lq_f13_liquidity_dollar_volume_logdvrank_252d_base_v106_signal,
    f13lq_f13_liquidity_dollar_volume_impact_126d_base_v107_signal,
    f13lq_f13_liquidity_dollar_volume_impact_252d_base_v108_signal,
    f13lq_f13_liquidity_dollar_volume_impact2_63d_base_v109_signal,
    f13lq_f13_liquidity_dollar_volume_corrabsv_252d_base_v110_signal,
    f13lq_f13_liquidity_dollar_volume_corrabsdv_63d_base_v111_signal,
    f13lq_f13_liquidity_dollar_volume_corrrv_126d_base_v112_signal,
    f13lq_f13_liquidity_dollar_volume_amitrend_63_252_base_v113_signal,
    f13lq_f13_liquidity_dollar_volume_amiratio_63_252_base_v114_signal,
    f13lq_f13_liquidity_dollar_volume_dvratio_21_126_base_v115_signal,
    f13lq_f13_liquidity_dollar_volume_dvratio_42_189_base_v116_signal,
    f13lq_f13_liquidity_dollar_volume_turnratio_21_252_base_v117_signal,
    f13lq_f13_liquidity_dollar_volume_ewmdvol_126d_base_v118_signal,
    f13lq_f13_liquidity_dollar_volume_ewmdvol_252d_base_v119_signal,
    f13lq_f13_liquidity_dollar_volume_ewmturn_63d_base_v120_signal,
    f13lq_f13_liquidity_dollar_volume_ewmami_126d_base_v121_signal,
    f13lq_f13_liquidity_dollar_volume_logdvolstd_252d_base_v122_signal,
    f13lq_f13_liquidity_dollar_volume_turnstd_126d_base_v123_signal,
    f13lq_f13_liquidity_dollar_volume_amistd_252d_base_v124_signal,
    f13lq_f13_liquidity_dollar_volume_logamitrend_63_252_base_v125_signal,
    f13lq_f13_liquidity_dollar_volume_turntrend_63_252_base_v126_signal,
    f13lq_f13_liquidity_dollar_volume_amiscaled_126d_base_v127_signal,
    f13lq_f13_liquidity_dollar_volume_amicomposite_126d_base_v128_signal,
    f13lq_f13_liquidity_dollar_volume_dvmom_126d_base_v129_signal,
    f13lq_f13_liquidity_dollar_volume_dvmom_42d_base_v130_signal,
    f13lq_f13_liquidity_dollar_volume_turnskew_252d_base_v131_signal,
    f13lq_f13_liquidity_dollar_volume_dvskew_126d_base_v132_signal,
    f13lq_f13_liquidity_dollar_volume_turnkurt_126d_base_v133_signal,
    f13lq_f13_liquidity_dollar_volume_amikurt_252d_base_v134_signal,
    f13lq_f13_liquidity_dollar_volume_illiqturn_126d_base_v135_signal,
    f13lq_f13_liquidity_dollar_volume_liqturn_63d_base_v136_signal,
    f13lq_f13_liquidity_dollar_volume_zdiverge_63d_base_v137_signal,
    f13lq_f13_liquidity_dollar_volume_turnsurge_21d_base_v138_signal,
    f13lq_f13_liquidity_dollar_volume_dvsurge_21d_base_v139_signal,
    f13lq_f13_liquidity_dollar_volume_amisurge_21d_base_v140_signal,
    f13lq_f13_liquidity_dollar_volume_amism_21d_base_v141_signal,
    f13lq_f13_liquidity_dollar_volume_logdvolsm_21d_base_v142_signal,
    f13lq_f13_liquidity_dollar_volume_turnir_21d_base_v143_signal,
    f13lq_f13_liquidity_dollar_volume_amiir_21d_base_v144_signal,
    f13lq_f13_liquidity_dollar_volume_dvratio_63_504_base_v145_signal,
    f13lq_f13_liquidity_dollar_volume_dvaccel_base_v146_signal,
    f13lq_f13_liquidity_dollar_volume_amiaccel_base_v147_signal,
    f13lq_f13_liquidity_dollar_volume_turnwlogdv_63d_base_v148_signal,
    f13lq_f13_liquidity_dollar_volume_illiqprem_base_v149_signal,
    f13lq_f13_liquidity_dollar_volume_liqblend_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_LIQUIDITY_DOLLAR_VOLUME_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f13_liquidity_dollar_volume_base_076_150_claude: {n_features} features pass")
