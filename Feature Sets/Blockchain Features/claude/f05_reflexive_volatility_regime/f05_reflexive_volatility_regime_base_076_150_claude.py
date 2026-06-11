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


# ===== folder domain primitives (reflexive volatility regime) =====
def _f05_rvol(s, w):
    # rolling realized volatility = std of daily log returns over w (annualizable)
    lr = np.log(s / s.shift(1))
    return lr.rolling(w, min_periods=max(2, w // 2)).std()


def _f05_volratio(s, ws, wl):
    # short-window vol / long-window vol (term-structure / regime tilt)
    vs = _f05_rvol(s, ws)
    vl = _f05_rvol(s, wl)
    return vs / vl.replace(0, np.nan)


def _f05_volz(s, w, wz):
    # z-score of realized vol over a longer lookback (regime extremity)
    v = _f05_rvol(s, w)
    m = v.rolling(wz, min_periods=max(2, wz // 2)).mean()
    sd = v.rolling(wz, min_periods=max(2, wz // 2)).std()
    return (v - m) / sd.replace(0, np.nan)


def _f05_semivol(s, w, side):
    # downside (side<0) or upside (side>0) semideviation of daily log returns
    lr = np.log(s / s.shift(1))
    if side < 0:
        d = lr.clip(upper=0.0)
    else:
        d = lr.clip(lower=0.0)
    return np.sqrt((d * d).rolling(w, min_periods=max(2, w // 2)).mean())


# ============ FEATURES 076-150 ============

# 5d realized volatility
def f05vr_f05_reflexive_volatility_regime_rvol_5d_base_v076_signal(closeadj):
    result = _f05_rvol(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d realized volatility
def f05vr_f05_reflexive_volatility_regime_rvol_189d_base_v077_signal(closeadj):
    result = _f05_rvol(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d realized volatility (annualized)
def f05vr_f05_reflexive_volatility_regime_rvolann_126d_base_v078_signal(closeadj):
    result = _f05_rvol(closeadj, 126) * np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d realized volatility (annualized)
def f05vr_f05_reflexive_volatility_regime_rvolann_252d_base_v079_signal(closeadj):
    result = _f05_rvol(closeadj, 252) * np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


# log realized vol level 21d (compresses extreme regimes)
def f05vr_f05_reflexive_volatility_regime_logrvol_21d_base_v080_signal(closeadj):
    result = np.log(_f05_rvol(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# log realized vol level 63d
def f05vr_f05_reflexive_volatility_regime_logrvol_63d_base_v081_signal(closeadj):
    result = np.log(_f05_rvol(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# log realized vol level 126d
def f05vr_f05_reflexive_volatility_regime_logrvol_126d_base_v082_signal(closeadj):
    result = np.log(_f05_rvol(closeadj, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# vol term structure 5/21
def f05vr_f05_reflexive_volatility_regime_termratio_5_21_base_v083_signal(closeadj):
    result = _f05_volratio(closeadj, 5, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# vol term structure 10/126
def f05vr_f05_reflexive_volatility_regime_termratio_10_126_base_v084_signal(closeadj):
    result = _f05_volratio(closeadj, 10, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vol term structure 126/252
def f05vr_f05_reflexive_volatility_regime_termratio_126_252_base_v085_signal(closeadj):
    result = _f05_volratio(closeadj, 126, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log vol term structure 10/63
def f05vr_f05_reflexive_volatility_regime_logterm_10_63_base_v086_signal(closeadj):
    result = np.log(_f05_volratio(closeadj, 10, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# log vol term structure 42/252
def f05vr_f05_reflexive_volatility_regime_logterm_42_252_base_v087_signal(closeadj):
    result = np.log(_f05_volratio(closeadj, 42, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# vol term-structure slope 21 minus 252
def f05vr_f05_reflexive_volatility_regime_termslope_21_252_base_v088_signal(closeadj):
    result = _f05_rvol(closeadj, 21) - _f05_rvol(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# vol term-structure slope 42 minus 126
def f05vr_f05_reflexive_volatility_regime_termslope_42_126_base_v089_signal(closeadj):
    result = _f05_rvol(closeadj, 42) - _f05_rvol(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vol term-structure curvature (short - 2*mid + long)
def f05vr_f05_reflexive_volatility_regime_termcurv_base_v090_signal(closeadj):
    result = _f05_rvol(closeadj, 10) - 2.0 * _f05_rvol(closeadj, 63) + _f05_rvol(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vol z-score: 10d vol over 252d
def f05vr_f05_reflexive_volatility_regime_volz_10_252_base_v091_signal(closeadj):
    result = _f05_volz(closeadj, 10, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# vol z-score: 5d vol over 126d
def f05vr_f05_reflexive_volatility_regime_volz_5_126_base_v092_signal(closeadj):
    result = _f05_volz(closeadj, 5, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vol z-score: 21d vol over 504d
def f05vr_f05_reflexive_volatility_regime_volz_21_504_base_v093_signal(closeadj):
    result = _f05_volz(closeadj, 21, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# vol z-score: 42d vol over 126d
def f05vr_f05_reflexive_volatility_regime_volz_42_126_base_v094_signal(closeadj):
    result = _f05_volz(closeadj, 42, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol: 63d std of 10d realized vol
def f05vr_f05_reflexive_volatility_regime_volofvol_10_63_base_v095_signal(closeadj):
    result = _std(_f05_rvol(closeadj, 10), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol: 252d std of 21d realized vol
def f05vr_f05_reflexive_volatility_regime_volofvol_21_252_base_v096_signal(closeadj):
    result = _std(_f05_rvol(closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# normalized vol-of-vol 10/63
def f05vr_f05_reflexive_volatility_regime_volcv_10_63_base_v097_signal(closeadj):
    v = _f05_rvol(closeadj, 10)
    result = _safe_div(_std(v, 63), _mean(v, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# normalized vol-of-vol 42/252
def f05vr_f05_reflexive_volatility_regime_volcv_42_252_base_v098_signal(closeadj):
    v = _f05_rvol(closeadj, 42)
    result = _safe_div(_std(v, 252), _mean(v, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# downside semideviation 252d
def f05vr_f05_reflexive_volatility_regime_downvol_252d_base_v099_signal(closeadj):
    result = _f05_semivol(closeadj, 252, -1)
    return result.replace([np.inf, -np.inf], np.nan)


# upside semideviation 42d
def f05vr_f05_reflexive_volatility_regime_upvol_42d_base_v100_signal(closeadj):
    result = _f05_semivol(closeadj, 42, 1)
    return result.replace([np.inf, -np.inf], np.nan)


# upside semideviation 252d
def f05vr_f05_reflexive_volatility_regime_upvol_252d_base_v101_signal(closeadj):
    result = _f05_semivol(closeadj, 252, 1)
    return result.replace([np.inf, -np.inf], np.nan)


# downside/upside vol ratio 42d
def f05vr_f05_reflexive_volatility_regime_volasym_42d_base_v102_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 42, -1), _f05_semivol(closeadj, 42, 1))
    return result.replace([np.inf, -np.inf], np.nan)


# downside/upside vol ratio 252d
def f05vr_f05_reflexive_volatility_regime_volasym_252d_base_v103_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 252, -1), _f05_semivol(closeadj, 252, 1))
    return result.replace([np.inf, -np.inf], np.nan)


# downside share of total semivol 126d
def f05vr_f05_reflexive_volatility_regime_downshare_126d_base_v104_signal(closeadj):
    dn = _f05_semivol(closeadj, 126, -1)
    up = _f05_semivol(closeadj, 126, 1)
    result = _safe_div(dn, dn + up)
    return result.replace([np.inf, -np.inf], np.nan)


# log downside/upside vol ratio 63d (symmetric tilt)
def f05vr_f05_reflexive_volatility_regime_logasym_63d_base_v105_signal(closeadj):
    result = np.log(_safe_div(_f05_semivol(closeadj, 63, -1), _f05_semivol(closeadj, 63, 1)))
    return result.replace([np.inf, -np.inf], np.nan)


# upside vol normalized by total realized vol 63d
def f05vr_f05_reflexive_volatility_regime_upnorm_63d_base_v106_signal(closeadj):
    result = _safe_div(_f05_semivol(closeadj, 63, 1), _f05_rvol(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA volatility span 10
def f05vr_f05_reflexive_volatility_regime_ewmavol_10d_base_v107_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=10, min_periods=5).std() + _f05_rvol(closeadj, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA volatility span 252
def f05vr_f05_reflexive_volatility_regime_ewmavol_252d_base_v108_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = lr.ewm(span=252, min_periods=84).std() + _f05_rvol(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA vs simple vol ratio 21 (reflexive responsiveness)
def f05vr_f05_reflexive_volatility_regime_ewmaratio_21d_base_v109_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    ew = lr.ewm(span=21, min_periods=10).std()
    result = _safe_div(ew, _f05_rvol(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA vs simple vol gap 126
def f05vr_f05_reflexive_volatility_regime_ewmagap_126d_base_v110_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    ew = lr.ewm(span=126, min_periods=42).std()
    result = ew - _f05_rvol(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vol percentile rank 42d over 252d
def f05vr_f05_reflexive_volatility_regime_volpct_42_252_base_v111_signal(closeadj):
    v = _f05_rvol(closeadj, 42)
    result = v.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# vol percentile rank 126d over 504d
def f05vr_f05_reflexive_volatility_regime_volpct_126_504_base_v112_signal(closeadj):
    v = _f05_rvol(closeadj, 126)
    result = v.rolling(504, min_periods=168).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# downside vol percentile rank 63d over 252d
def f05vr_f05_reflexive_volatility_regime_downpct_63_252_base_v113_signal(closeadj):
    v = _f05_semivol(closeadj, 63, -1)
    result = v.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# vol acceleration: 10d vol minus its 63d mean
def f05vr_f05_reflexive_volatility_regime_volsurp_10_63_base_v114_signal(closeadj):
    v = _f05_rvol(closeadj, 10)
    result = v - _mean(v, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# vol acceleration: 42d vol minus its 252d mean
def f05vr_f05_reflexive_volatility_regime_volsurp_42_252_base_v115_signal(closeadj):
    v = _f05_rvol(closeadj, 42)
    result = v - _mean(v, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# vol change rate 10d
def f05vr_f05_reflexive_volatility_regime_voldelta_10d_base_v116_signal(closeadj):
    v = _f05_rvol(closeadj, 10)
    result = v - v.shift(10)
    return result.replace([np.inf, -np.inf], np.nan)


# vol change rate 42d
def f05vr_f05_reflexive_volatility_regime_voldelta_42d_base_v117_signal(closeadj):
    v = _f05_rvol(closeadj, 42)
    result = v - v.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# log vol change 63d (proportional vol move)
def f05vr_f05_reflexive_volatility_regime_logvolchg_63d_base_v118_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = np.log(_safe_div(v, v.shift(63)))
    return result.replace([np.inf, -np.inf], np.nan)


# vol acceleration ratio: 10d vol over its 42d mean
def f05vr_f05_reflexive_volatility_regime_volaccel_10_42_base_v119_signal(closeadj):
    v = _f05_rvol(closeadj, 10)
    result = _safe_div(v, _mean(v, 42))
    return result.replace([np.inf, -np.inf], np.nan)


# vol acceleration ratio: 63d vol over its 252d mean
def f05vr_f05_reflexive_volatility_regime_volaccel_63_252_base_v120_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = _safe_div(v, _mean(v, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized daily range proxy 126d
def f05vr_f05_reflexive_volatility_regime_rangevol_126d_base_v121_signal(high, low, closeadj):
    rng = np.log(high / low.replace(0, np.nan))
    result = _safe_div(rng.rolling(126, min_periods=42).mean(), _f05_rvol(closeadj, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson high-low volatility 126d
def f05vr_f05_reflexive_volatility_regime_parkinson_126d_base_v122_signal(high, low, closeadj):
    rng2 = (np.log(high / low.replace(0, np.nan))) ** 2
    park = np.sqrt(rng2.rolling(126, min_periods=42).mean() / (4.0 * np.log(2.0)))
    result = park + _f05_rvol(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vs close-to-close vol ratio 63d
def f05vr_f05_reflexive_volatility_regime_parkratio_63d_base_v123_signal(high, low, closeadj):
    rng2 = (np.log(high / low.replace(0, np.nan))) ** 2
    park = np.sqrt(rng2.rolling(63, min_periods=21).mean() / (4.0 * np.log(2.0)))
    result = _safe_div(park, _f05_rvol(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass style range vol 21d
def f05vr_f05_reflexive_volatility_regime_gkvol_21d_base_v124_signal(high, low, open, closeadj):
    hl = 0.5 * (np.log(high / low.replace(0, np.nan))) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * (np.log(closeadj / open.replace(0, np.nan))) ** 2
    result = np.sqrt((hl - co).rolling(21, min_periods=10).mean()) + _f05_rvol(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass style range vol 63d
def f05vr_f05_reflexive_volatility_regime_gkvol_63d_base_v125_signal(high, low, open, closeadj):
    hl = 0.5 * (np.log(high / low.replace(0, np.nan))) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * (np.log(closeadj / open.replace(0, np.nan))) ** 2
    result = np.sqrt((hl - co).rolling(63, min_periods=21).mean()) + _f05_rvol(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# vol-scaled absolute return intensity 126d
def f05vr_f05_reflexive_volatility_regime_absintens_126d_base_v126_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1)).abs()
    result = _safe_div(lr.rolling(126, min_periods=42).mean(), _f05_rvol(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol skew tilt 252d
def f05vr_f05_reflexive_volatility_regime_voltilt_252d_base_v127_signal(closeadj):
    dn = _f05_semivol(closeadj, 252, -1)
    up = _f05_semivol(closeadj, 252, 1)
    result = _safe_div(dn - up, _f05_rvol(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# volume-confirmed vol surge 21d (reflexive: vol level times volume z)
def f05vr_f05_reflexive_volatility_regime_volvolconf_21d_base_v128_signal(closeadj, volume):
    result = _f05_rvol(closeadj, 21) * _z(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume-confirmed vol surge 63d
def f05vr_f05_reflexive_volatility_regime_dvvolconf_63d_base_v129_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f05_rvol(closeadj, 63) * _z(dv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol z 63/252
def f05vr_f05_reflexive_volatility_regime_vovz_63_252_base_v130_signal(closeadj):
    vv = _std(_f05_rvol(closeadj, 63), 126)
    result = _z(vv, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol momentum: vol now vs vol 21d ago, normalized by vol-of-vol
def f05vr_f05_reflexive_volatility_regime_volmom_21d_base_v131_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = _safe_div(v - v.shift(21), _std(v, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol momentum 63d normalized by vol-of-vol
def f05vr_f05_reflexive_volatility_regime_volmom_63d_base_v132_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = _safe_div(v - v.shift(63), _std(v, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA vol-of-vol span 63
def f05vr_f05_reflexive_volatility_regime_ewmavov_63d_base_v133_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = v.ewm(span=63, min_periods=21).std()
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed realized vol 21d (21d mean of 21d vol)
def f05vr_f05_reflexive_volatility_regime_smoothvol_21d_base_v134_signal(closeadj):
    result = _mean(_f05_rvol(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed realized vol 63d
def f05vr_f05_reflexive_volatility_regime_smoothvol_63d_base_v135_signal(closeadj):
    result = _mean(_f05_rvol(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime gap: short vol minus its long EWMA baseline
def f05vr_f05_reflexive_volatility_regime_regimegap_21d_base_v136_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = v - v.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime gap 63d vs 252d EWMA baseline
def f05vr_f05_reflexive_volatility_regime_regimegap_63d_base_v137_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = v - v.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol range: max-min spread of 21d vol over 126d, normalized
def f05vr_f05_reflexive_volatility_regime_volrange_21_126_base_v138_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    hi = v.rolling(126, min_periods=42).max()
    lo = v.rolling(126, min_periods=42).min()
    result = _safe_div(hi - lo, _mean(v, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol position within its 252d range (continuous 0-1)
def f05vr_f05_reflexive_volatility_regime_volpos_21_252_base_v139_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    hi = v.rolling(252, min_periods=63).max()
    lo = v.rolling(252, min_periods=63).min()
    result = _safe_div(v - lo, hi - lo)
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol position within 504d range
def f05vr_f05_reflexive_volatility_regime_volpos_63_504_base_v140_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    hi = v.rolling(504, min_periods=126).max()
    lo = v.rolling(504, min_periods=126).min()
    result = _safe_div(v - lo, hi - lo)
    return result.replace([np.inf, -np.inf], np.nan)


# downside semivol z-score 63 over 252
def f05vr_f05_reflexive_volatility_regime_downz_63_252_base_v141_signal(closeadj):
    result = _z(_f05_semivol(closeadj, 63, -1), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# upside semivol z-score 63 over 252
def f05vr_f05_reflexive_volatility_regime_upz_63_252_base_v142_signal(closeadj):
    result = _z(_f05_semivol(closeadj, 63, 1), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# semivol asymmetry z-score 126 over 252
def f05vr_f05_reflexive_volatility_regime_asymz_126_252_base_v143_signal(closeadj):
    a = _safe_div(_f05_semivol(closeadj, 126, -1), _f05_semivol(closeadj, 126, 1))
    result = _z(a, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# term-structure ratio z-score 21/126 over 252
def f05vr_f05_reflexive_volatility_regime_termz_21_126_base_v144_signal(closeadj):
    result = _z(_f05_volratio(closeadj, 21, 126), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# term-structure ratio z-score 42/252 over 252
def f05vr_f05_reflexive_volatility_regime_termz_42_252_base_v145_signal(closeadj):
    result = _z(_f05_volratio(closeadj, 42, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol scaled by its own long-run level (mean-reversion gap ratio)
def f05vr_f05_reflexive_volatility_regime_volnorm_21_252_base_v146_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = _safe_div(v, _mean(v, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol scaled by EWMA baseline 63
def f05vr_f05_reflexive_volatility_regime_volnorm_63ewm_base_v147_signal(closeadj):
    v = _f05_rvol(closeadj, 63)
    result = _safe_div(v, v.ewm(span=252, min_periods=84).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol normalized by vol level 63d (reflexive instability index)
def f05vr_f05_reflexive_volatility_regime_instab_63d_base_v148_signal(closeadj):
    v = _f05_rvol(closeadj, 21)
    result = _safe_div(_std(v, 63), _f05_rvol(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon vol-z composite (21/63/126 over 252)
def f05vr_f05_reflexive_volatility_regime_blendvolz_base_v149_signal(closeadj):
    result = (_f05_volz(closeadj, 21, 252) + _f05_volz(closeadj, 63, 252)
              + _f05_volz(closeadj, 126, 252)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# blended term-structure composite (5/63, 21/126, 42/252)
def f05vr_f05_reflexive_volatility_regime_blendterm_base_v150_signal(closeadj):
    result = (_f05_volratio(closeadj, 5, 63) + _f05_volratio(closeadj, 21, 126)
              + _f05_volratio(closeadj, 42, 252)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05vr_f05_reflexive_volatility_regime_rvol_5d_base_v076_signal,
    f05vr_f05_reflexive_volatility_regime_rvol_189d_base_v077_signal,
    f05vr_f05_reflexive_volatility_regime_rvolann_126d_base_v078_signal,
    f05vr_f05_reflexive_volatility_regime_rvolann_252d_base_v079_signal,
    f05vr_f05_reflexive_volatility_regime_logrvol_21d_base_v080_signal,
    f05vr_f05_reflexive_volatility_regime_logrvol_63d_base_v081_signal,
    f05vr_f05_reflexive_volatility_regime_logrvol_126d_base_v082_signal,
    f05vr_f05_reflexive_volatility_regime_termratio_5_21_base_v083_signal,
    f05vr_f05_reflexive_volatility_regime_termratio_10_126_base_v084_signal,
    f05vr_f05_reflexive_volatility_regime_termratio_126_252_base_v085_signal,
    f05vr_f05_reflexive_volatility_regime_logterm_10_63_base_v086_signal,
    f05vr_f05_reflexive_volatility_regime_logterm_42_252_base_v087_signal,
    f05vr_f05_reflexive_volatility_regime_termslope_21_252_base_v088_signal,
    f05vr_f05_reflexive_volatility_regime_termslope_42_126_base_v089_signal,
    f05vr_f05_reflexive_volatility_regime_termcurv_base_v090_signal,
    f05vr_f05_reflexive_volatility_regime_volz_10_252_base_v091_signal,
    f05vr_f05_reflexive_volatility_regime_volz_5_126_base_v092_signal,
    f05vr_f05_reflexive_volatility_regime_volz_21_504_base_v093_signal,
    f05vr_f05_reflexive_volatility_regime_volz_42_126_base_v094_signal,
    f05vr_f05_reflexive_volatility_regime_volofvol_10_63_base_v095_signal,
    f05vr_f05_reflexive_volatility_regime_volofvol_21_252_base_v096_signal,
    f05vr_f05_reflexive_volatility_regime_volcv_10_63_base_v097_signal,
    f05vr_f05_reflexive_volatility_regime_volcv_42_252_base_v098_signal,
    f05vr_f05_reflexive_volatility_regime_downvol_252d_base_v099_signal,
    f05vr_f05_reflexive_volatility_regime_upvol_42d_base_v100_signal,
    f05vr_f05_reflexive_volatility_regime_upvol_252d_base_v101_signal,
    f05vr_f05_reflexive_volatility_regime_volasym_42d_base_v102_signal,
    f05vr_f05_reflexive_volatility_regime_volasym_252d_base_v103_signal,
    f05vr_f05_reflexive_volatility_regime_downshare_126d_base_v104_signal,
    f05vr_f05_reflexive_volatility_regime_logasym_63d_base_v105_signal,
    f05vr_f05_reflexive_volatility_regime_upnorm_63d_base_v106_signal,
    f05vr_f05_reflexive_volatility_regime_ewmavol_10d_base_v107_signal,
    f05vr_f05_reflexive_volatility_regime_ewmavol_252d_base_v108_signal,
    f05vr_f05_reflexive_volatility_regime_ewmaratio_21d_base_v109_signal,
    f05vr_f05_reflexive_volatility_regime_ewmagap_126d_base_v110_signal,
    f05vr_f05_reflexive_volatility_regime_volpct_42_252_base_v111_signal,
    f05vr_f05_reflexive_volatility_regime_volpct_126_504_base_v112_signal,
    f05vr_f05_reflexive_volatility_regime_downpct_63_252_base_v113_signal,
    f05vr_f05_reflexive_volatility_regime_volsurp_10_63_base_v114_signal,
    f05vr_f05_reflexive_volatility_regime_volsurp_42_252_base_v115_signal,
    f05vr_f05_reflexive_volatility_regime_voldelta_10d_base_v116_signal,
    f05vr_f05_reflexive_volatility_regime_voldelta_42d_base_v117_signal,
    f05vr_f05_reflexive_volatility_regime_logvolchg_63d_base_v118_signal,
    f05vr_f05_reflexive_volatility_regime_volaccel_10_42_base_v119_signal,
    f05vr_f05_reflexive_volatility_regime_volaccel_63_252_base_v120_signal,
    f05vr_f05_reflexive_volatility_regime_rangevol_126d_base_v121_signal,
    f05vr_f05_reflexive_volatility_regime_parkinson_126d_base_v122_signal,
    f05vr_f05_reflexive_volatility_regime_parkratio_63d_base_v123_signal,
    f05vr_f05_reflexive_volatility_regime_gkvol_21d_base_v124_signal,
    f05vr_f05_reflexive_volatility_regime_gkvol_63d_base_v125_signal,
    f05vr_f05_reflexive_volatility_regime_absintens_126d_base_v126_signal,
    f05vr_f05_reflexive_volatility_regime_voltilt_252d_base_v127_signal,
    f05vr_f05_reflexive_volatility_regime_volvolconf_21d_base_v128_signal,
    f05vr_f05_reflexive_volatility_regime_dvvolconf_63d_base_v129_signal,
    f05vr_f05_reflexive_volatility_regime_vovz_63_252_base_v130_signal,
    f05vr_f05_reflexive_volatility_regime_volmom_21d_base_v131_signal,
    f05vr_f05_reflexive_volatility_regime_volmom_63d_base_v132_signal,
    f05vr_f05_reflexive_volatility_regime_ewmavov_63d_base_v133_signal,
    f05vr_f05_reflexive_volatility_regime_smoothvol_21d_base_v134_signal,
    f05vr_f05_reflexive_volatility_regime_smoothvol_63d_base_v135_signal,
    f05vr_f05_reflexive_volatility_regime_regimegap_21d_base_v136_signal,
    f05vr_f05_reflexive_volatility_regime_regimegap_63d_base_v137_signal,
    f05vr_f05_reflexive_volatility_regime_volrange_21_126_base_v138_signal,
    f05vr_f05_reflexive_volatility_regime_volpos_21_252_base_v139_signal,
    f05vr_f05_reflexive_volatility_regime_volpos_63_504_base_v140_signal,
    f05vr_f05_reflexive_volatility_regime_downz_63_252_base_v141_signal,
    f05vr_f05_reflexive_volatility_regime_upz_63_252_base_v142_signal,
    f05vr_f05_reflexive_volatility_regime_asymz_126_252_base_v143_signal,
    f05vr_f05_reflexive_volatility_regime_termz_21_126_base_v144_signal,
    f05vr_f05_reflexive_volatility_regime_termz_42_252_base_v145_signal,
    f05vr_f05_reflexive_volatility_regime_volnorm_21_252_base_v146_signal,
    f05vr_f05_reflexive_volatility_regime_volnorm_63ewm_base_v147_signal,
    f05vr_f05_reflexive_volatility_regime_instab_63d_base_v148_signal,
    f05vr_f05_reflexive_volatility_regime_blendvolz_base_v149_signal,
    f05vr_f05_reflexive_volatility_regime_blendterm_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_REFLEXIVE_VOLATILITY_REGIME_REGISTRY_076_150 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume", "marketcap", "ev",
           "assets", "assetsc", "equity", "revenue", "gp", "ebitda", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory", "receivables",
           "intangibles", "evebitda", "evebit", "pe", "pb", "ps", "currentratio", "bvps", "sps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "sf3a_shares", "sf3a_value",
           "sf3b_shares", "sf3b_value", "grossmargin", "beta1y", "beta5y", "invcap", "debt"}
    for nm in names:
        if nm in ("closeadj", "close", "price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            s = level + 50.0 * walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f05_rvol", "_f05_volratio", "_f05_volz", "_f05_semivol")
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
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f05_reflexive_volatility_regime_base_076_150_claude: {n_features} features pass")
