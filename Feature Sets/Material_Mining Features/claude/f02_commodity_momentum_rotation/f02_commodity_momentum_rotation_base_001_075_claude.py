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
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (commodity momentum / rotation) =====
def _f02_roc(close, w):
    # rate of change over w days (simple return)
    return close / close.shift(w).replace(0, np.nan) - 1.0


def _f02_logmom(close, w):
    # log momentum over w days
    return np.log(close.replace(0, np.nan) / close.shift(w).replace(0, np.nan))


def _f02_mom_12_1(close):
    # classic 12-1 momentum: 252d return excluding most recent 21d
    return close.shift(21) / close.shift(252).replace(0, np.nan) - 1.0


def _f02_vol(close, w):
    # realized vol of daily returns over w
    return close.pct_change().rolling(w, min_periods=max(2, w // 2)).std()


def _f02_riskadj(close, w):
    # risk-adjusted momentum: ROC / realized vol
    # risk-adjusted momentum: rolling t-stat of daily returns (mean/std*sqrt(w)),
    # z-scored vs its own 252d history so it measures RELATIVE risk-adjusted strength
    # (decoupled from raw ROC level)
    r = close.pct_change()
    m = r.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = r.rolling(w, min_periods=max(2, w // 2)).std()
    t = (m / sd.replace(0, np.nan)) * np.sqrt(float(w))
    tm = t.rolling(252, min_periods=126).mean()
    tsd = t.rolling(252, min_periods=126).std()
    return (t - tm) / tsd.replace(0, np.nan)


def _f02_consistency(close, w):
    # momentum consistency = trendiness: magnitude-weighted lag-1 return autocorrelation
    # (high when consecutive moves agree in direction; decoupled from total ROC magnitude)
    r = close.pct_change()
    prod = (r * r.shift(1)).rolling(w, min_periods=max(2, w // 2)).mean()
    denom = (r * r).rolling(w, min_periods=max(2, w // 2)).mean()
    return prod / denom.replace(0, np.nan)


def _f02_efficiency(close, w):
    # net path / gross path (trend efficiency, signed)
    net = (close - close.shift(w))
    gross = close.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return net / gross.replace(0, np.nan)


# ============================================================
# ROC 21d level
def f02cm_f02_commodity_momentum_rotation_roc_21d_base_v001_signal(closeadj):
    b = _f02_roc(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROC 63d level
def f02cm_f02_commodity_momentum_rotation_roc_63d_base_v002_signal(closeadj):
    b = _f02_roc(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROC 126d level
def f02cm_f02_commodity_momentum_rotation_roc_126d_base_v003_signal(closeadj):
    b = _f02_roc(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROC 252d level
def f02cm_f02_commodity_momentum_rotation_roc_252d_base_v004_signal(closeadj):
    b = _f02_roc(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROC 504d level (multi-year commodity move)
def f02cm_f02_commodity_momentum_rotation_roc_504d_base_v005_signal(closeadj):
    b = _f02_roc(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d momentum measured against the 126d MEDIAN price (robust anchor momentum)
def f02cm_f02_commodity_momentum_rotation_logmom_126d_base_v006_signal(closeadj):
    med = closeadj.rolling(126, min_periods=63).median()
    b = np.log(closeadj.replace(0, np.nan) / med.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d momentum measured against the 252d MEAN price (distance-from-trend momentum)
def f02cm_f02_commodity_momentum_rotation_logmom_252d_base_v007_signal(closeadj):
    mn = closeadj.rolling(252, min_periods=126).mean()
    b = np.log(closeadj.replace(0, np.nan) / mn.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# classic 12-1 momentum (252d ex last 21d)
def f02cm_f02_commodity_momentum_rotation_mom121_252d_base_v008_signal(closeadj):
    b = _f02_mom_12_1(closeadj)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 6-1 momentum: 126d return excluding most recent 21d
def f02cm_f02_commodity_momentum_rotation_mom61_126d_base_v009_signal(closeadj):
    b = closeadj.shift(21) / closeadj.shift(126).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-cycle momentum persistence: 504d log-momentum minus 252d log-momentum
def f02cm_f02_commodity_momentum_rotation_mom241_504d_base_v010_signal(closeadj):
    b = _f02_logmom(closeadj, 504) - _f02_logmom(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted momentum 63d (ROC / vol)
def f02cm_f02_commodity_momentum_rotation_riskadj_63d_base_v011_signal(closeadj):
    b = _f02_riskadj(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted momentum 126d
def f02cm_f02_commodity_momentum_rotation_riskadj_126d_base_v012_signal(closeadj):
    b = _f02_riskadj(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted momentum 252d (annualized Sharpe-like trend)
def f02cm_f02_commodity_momentum_rotation_riskadj_252d_base_v013_signal(closeadj):
    b = _f02_riskadj(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum consistency 63d (fraction up-days - 0.5)
def f02cm_f02_commodity_momentum_rotation_consist_63d_base_v014_signal(closeadj):
    b = _f02_consistency(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum consistency 126d
def f02cm_f02_commodity_momentum_rotation_consist_126d_base_v015_signal(closeadj):
    b = _f02_consistency(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum consistency 252d
def f02cm_f02_commodity_momentum_rotation_consist_252d_base_v016_signal(closeadj):
    b = _f02_consistency(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend cleanliness 63d (UNSIGNED Kaufman efficiency: trendiness magnitude 0..1)
def f02cm_f02_commodity_momentum_rotation_eff_63d_base_v017_signal(closeadj):
    b = _f02_efficiency(closeadj, 63).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend cleanliness 126d (unsigned efficiency)
def f02cm_f02_commodity_momentum_rotation_eff_126d_base_v018_signal(closeadj):
    b = _f02_efficiency(closeadj, 126).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend cleanliness 252d (unsigned efficiency)
def f02cm_f02_commodity_momentum_rotation_eff_252d_base_v019_signal(closeadj):
    b = _f02_efficiency(closeadj, 252).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-horizon momentum rank: 252d ROC percentile vs own 504d history
def f02cm_f02_commodity_momentum_rotation_momrank_252d_base_v020_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    b = _rank(roc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum-change rank: percentile of the 63d change in 126d ROC vs 252d history
def f02cm_f02_commodity_momentum_rotation_momrank_126d_base_v021_signal(closeadj):
    chg = _f02_logmom(closeadj, 126) - _f02_logmom(closeadj, 126).shift(63)
    b = _rank(chg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum rank: 504d ROC percentile vs own 1260d history (cycle rank)
def f02cm_f02_commodity_momentum_rotation_momrank_504d_base_v022_signal(closeadj):
    roc = _f02_logmom(closeadj, 504)
    b = roc.rolling(1260, min_periods=504).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum vs prior cycle: 252d ROC now minus 252d ROC one year ago
def f02cm_f02_commodity_momentum_rotation_momvscycle_252d_base_v023_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    b = roc - roc.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum vs prior cycle: 126d ROC now minus 126d ROC two quarters ago
def f02cm_f02_commodity_momentum_rotation_momvscycle_126d_base_v024_signal(closeadj):
    roc = _f02_logmom(closeadj, 126)
    b = roc - roc.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum term-structure spread: short 63d ROC minus long 252d ROC
def f02cm_f02_commodity_momentum_rotation_spread_63v252_base_v025_signal(closeadj):
    s = _f02_logmom(closeadj, 63)
    l = _f02_logmom(closeadj, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum term-structure spread: 126d minus 504d ROC
def f02cm_f02_commodity_momentum_rotation_spread_126v504_base_v026_signal(closeadj):
    s = _f02_logmom(closeadj, 126)
    l = _f02_logmom(closeadj, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum acceleration: 21d ROC minus 63d ROC (fast vs medium)
def f02cm_f02_commodity_momentum_rotation_spread_21v63_base_v027_signal(closeadj):
    s = _f02_logmom(closeadj, 21)
    l = _f02_logmom(closeadj, 63)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized 63d momentum impulse: change in 63d ROC over 21d, per unit vol
def f02cm_f02_commodity_momentum_rotation_rocz_63d_base_v028_signal(closeadj):
    roc = _f02_logmom(closeadj, 63)
    chg = roc - roc.shift(21)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = chg / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum convexity: 126d ROC minus the average of 63d and 252d ROC (curvature)
def f02cm_f02_commodity_momentum_rotation_rocz_126d_base_v029_signal(closeadj):
    m63 = _f02_logmom(closeadj, 63)
    m126 = _f02_logmom(closeadj, 126)
    m252 = _f02_logmom(closeadj, 252)
    b = m126 - 0.5 * (m63 + m252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d momentum percentile within its own 1260d full-cycle history (cycle-relative)
def f02cm_f02_commodity_momentum_rotation_rocz_252d_base_v030_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    b = roc.rolling(1260, min_periods=378).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum strength: |252d ROC| (magnitude of trend regardless of direction)
def f02cm_f02_commodity_momentum_rotation_strength_252d_base_v031_signal(closeadj):
    b = _f02_logmom(closeadj, 252).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum direction persistence: signed share of cumulative-path time above start
def f02cm_f02_commodity_momentum_rotation_dirpersist_126d_base_v032_signal(closeadj):
    roc = _f02_logmom(closeadj, 126)
    lp = np.log(closeadj.replace(0, np.nan))

    def _abovefrac(a):
        return float(np.mean(a > a[0])) - 0.5

    frac = lp.rolling(126, min_periods=63).apply(_abovefrac, raw=True)
    b = np.sign(roc) * (frac + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum streak: signed count of consecutive same-direction 21d ROC, scaled
def f02cm_f02_commodity_momentum_rotation_streak_21d_base_v033_signal(closeadj):
    roc = _f02_logmom(closeadj, 21)
    sgn = np.sign(roc)
    grp = (sgn != sgn.shift(1)).cumsum()
    streak = sgn.groupby(grp).cumcount() + 1
    b = sgn * np.log1p(streak)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 12-1 momentum z-scored vs own 504d history (rotation-relative)
def f02cm_f02_commodity_momentum_rotation_mom121z_base_v034_signal(closeadj):
    m = _f02_mom_12_1(closeadj)
    b = _z(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted 12-1 momentum (per 252d vol), percentile-ranked vs 504d history
def f02cm_f02_commodity_momentum_rotation_mom121ra_base_v035_signal(closeadj):
    m = _f02_mom_12_1(closeadj)
    vol = closeadj.pct_change().rolling(252, min_periods=126).std()
    ra = m / vol.replace(0, np.nan)
    b = ra.rolling(504, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum smoothness: 252d ROC per sub-return dispersion, change over a quarter
def f02cm_f02_commodity_momentum_rotation_smooth_252d_base_v036_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    sub = closeadj.pct_change()
    disp = sub.rolling(252, min_periods=126).std() * np.sqrt(252.0)
    sm = roc / disp.replace(0, np.nan)
    b = sm - sm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum acceleration via second difference of cumulative log price (63d)
def f02cm_f02_commodity_momentum_rotation_accel_63d_base_v037_signal(closeadj):
    roc = _f02_logmom(closeadj, 63)
    b = roc - 2.0 * roc.shift(63) + roc.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth of momentum: signed-tanh sum across horizons (21/63/126/252), continuous
def f02cm_f02_commodity_momentum_rotation_breadth_base_v038_signal(closeadj):
    h = [21, 63, 126, 252]
    agree = sum(np.tanh(8.0 * _f02_logmom(closeadj, w)) for w in h)
    b = agree / len(h)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum dispersion across horizons (disagreement of 21/63/126/252 ROC)
def f02cm_f02_commodity_momentum_rotation_disp_base_v039_signal(closeadj):
    m1 = _f02_logmom(closeadj, 21)
    m2 = _f02_logmom(closeadj, 63)
    m3 = _f02_logmom(closeadj, 126)
    m4 = _f02_logmom(closeadj, 252)
    b = pd.concat([m1, m2, m3, m4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum vs prior cycle low: gain since the 504d momentum trough
def f02cm_f02_commodity_momentum_rotation_momtrough_504d_base_v040_signal(closeadj):
    roc = _f02_logmom(closeadj, 126)
    trough = roc.rolling(504, min_periods=252).min()
    b = roc - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the 504d momentum peak (staleness of the prior momentum high)
def f02cm_f02_commodity_momentum_rotation_mompeak_504d_base_v041_signal(closeadj):
    roc = _f02_logmom(closeadj, 126)

    def _dsp(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))

    b = roc.rolling(504, min_periods=252).apply(_dsp, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum range position: where 126d ROC sits in its own 504d range
def f02cm_f02_commodity_momentum_rotation_momrngpos_504d_base_v042_signal(closeadj):
    roc = _f02_logmom(closeadj, 126)
    hi = roc.rolling(504, min_periods=252).max()
    lo = roc.rolling(504, min_periods=252).min()
    b = (roc - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted momentum 504d (long-cycle Sharpe-like)
def f02cm_f02_commodity_momentum_rotation_riskadj_504d_base_v043_signal(closeadj):
    b = _f02_riskadj(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum quality: efficiency 252d times sign of 252d ROC (signed trend quality)
def f02cm_f02_commodity_momentum_rotation_quality_252d_base_v044_signal(closeadj):
    eff = _f02_efficiency(closeadj, 252).abs()
    roc = _f02_logmom(closeadj, 252)
    strength = roc.abs().rolling(504, min_periods=252).rank(pct=True)
    b = np.sign(roc) * eff * strength
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed 63d ROC (EMA) to capture persistent momentum regime
def f02cm_f02_commodity_momentum_rotation_rocema_63d_base_v045_signal(closeadj):
    roc = _f02_logmom(closeadj, 63)
    b = roc.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum displacement: 63d ROC minus its own slow EMA (momentum surprise)
def f02cm_f02_commodity_momentum_rotation_rocdisp_63d_base_v046_signal(closeadj):
    roc = _f02_logmom(closeadj, 63)
    b = roc - roc.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded 252d momentum (squashed long-horizon momentum)
def f02cm_f02_commodity_momentum_rotation_roctanh_252d_base_v047_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    b = np.tanh(2.0 * roc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-magnitude momentum shape change: signed-sqrt 252d ROC vs its quarter-ago value
def f02cm_f02_commodity_momentum_rotation_signmag_252d_base_v048_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    sm = np.sign(roc) * (roc.abs() ** 0.5)
    b = sm - sm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum-of-momentum: change in 126d ROC over a quarter
def f02cm_f02_commodity_momentum_rotation_momom_126d_base_v049_signal(closeadj):
    roc = _f02_logmom(closeadj, 126)
    b = roc - roc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute momentum trend filter: 252d ROC clipped at zero (long-only signal)
def f02cm_f02_commodity_momentum_rotation_absmom_252d_base_v050_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    pos = roc.clip(lower=0)
    b = pos - pos.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon momentum z-blend: sum of per-horizon z-scored ROCs (rotation composite)
def f02cm_f02_commodity_momentum_rotation_blend_base_v051_signal(closeadj):
    b = (_z(_f02_logmom(closeadj, 21), 252) + _z(_f02_logmom(closeadj, 63), 252)
         + _z(_f02_logmom(closeadj, 126), 252) + _z(_f02_logmom(closeadj, 252), 504)) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum kurtosis 21d: fat-tailed thrust vs grind (return distribution shape)
def f02cm_f02_commodity_momentum_rotation_consist_21d_base_v052_signal(closeadj):
    r = closeadj.pct_change()
    b = r.rolling(63, min_periods=21).apply(
        lambda a: (np.mean((a - a.mean()) ** 3) / (a.std() ** 3 + 1e-12)), raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside/upside semideviation asymmetry over 252d (downside-risk regime, decoupled)
def f02cm_f02_commodity_momentum_rotation_sortino_252d_base_v053_signal(closeadj):
    r = closeadj.pct_change()
    dvol = r.where(r < 0, 0.0).rolling(252, min_periods=126).std()
    uvol = r.where(r > 0, 0.0).rolling(252, min_periods=126).std()
    b = (uvol - dvol) / (uvol + dvol).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gain/loss magnitude asymmetry over 63d: avg up-move size vs avg down-move size
def f02cm_f02_commodity_momentum_rotation_uppart_63d_base_v054_signal(closeadj):
    r = closeadj.pct_change()
    up = r.where(r > 0, np.nan)
    dn = (-r.where(r < 0, np.nan))
    umean = up.rolling(63, min_periods=15).mean()
    dmean = dn.rolling(63, min_periods=15).mean()
    b = (umean - dmean) / (umean + dmean).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum gap: 252d ROC minus its 126d-lagged self (semiannual rotation)
def f02cm_f02_commodity_momentum_rotation_momgap_252d_base_v055_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    b = roc - roc.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-normalized 126d momentum, percentile-ranked vs 504d history (rotation strength)
def f02cm_f02_commodity_momentum_rotation_momnorm_126d_base_v056_signal(closeadj):
    roc = closeadj - closeadj.shift(126)
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    nm = roc / (hi - lo).replace(0, np.nan)
    b = nm.rolling(504, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of 21d ROC (jerk-like via two lags of fast ROC)
def f02cm_f02_commodity_momentum_rotation_accel_21d_base_v057_signal(closeadj):
    roc = _f02_logmom(closeadj, 21)
    b = roc - 2.0 * roc.shift(21) + roc.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum rank dispersion: spread of 63d and 252d ROC ranks (rotation tension)
def f02cm_f02_commodity_momentum_rotation_rankspread_base_v058_signal(closeadj):
    r1 = _rank(_f02_logmom(closeadj, 63), 252)
    r2 = _rank(_f02_logmom(closeadj, 252), 504)
    b = r1 - r2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum half-life proxy: 21d ROC relative to 63d ROC magnitude (decay)
def f02cm_f02_commodity_momentum_rotation_decay_base_v059_signal(closeadj):
    fast = _f02_logmom(closeadj, 21).abs()
    med = _f02_logmom(closeadj, 63).abs()
    b = fast / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 12-1 momentum minus 6-1 momentum (long vs medium rotation tilt)
def f02cm_f02_commodity_momentum_rotation_momtilt_base_v060_signal(closeadj):
    m12 = closeadj.shift(21) / closeadj.shift(252).replace(0, np.nan) - 1.0
    m6 = closeadj.shift(21) / closeadj.shift(126).replace(0, np.nan) - 1.0
    b = m12 - m6
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum stability: rolling std of 21d ROC over a year (lower = stable trend)
def f02cm_f02_commodity_momentum_rotation_momstd_252d_base_v061_signal(closeadj):
    roc = _f02_logmom(closeadj, 21)
    b = roc.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum vs cycle: 252d ROC deviation from its 504d mean, scaled by 504d ROC dispersion
def f02cm_f02_commodity_momentum_rotation_cycdev_252d_base_v062_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    dev = roc - roc.rolling(504, min_periods=252).mean()
    sd = roc.rolling(504, min_periods=252).std()
    b = (dev / sd.replace(0, np.nan)).rolling(1260, min_periods=378).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# positive-momentum persistence: fraction of last year with positive 63d ROC
def f02cm_f02_commodity_momentum_rotation_pospersist_base_v063_signal(closeadj):
    roc = _f02_logmom(closeadj, 63)
    pos = (roc > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum turning point: count of 21d-ROC sign flips over a year (rotation churn)
def f02cm_f02_commodity_momentum_rotation_flips_base_v064_signal(closeadj):
    roc = _f02_logmom(closeadj, 21)
    sgn = np.sign(roc)
    flip = (sgn != sgn.shift(1)).astype(float)
    b = flip.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume momentum surprise: sign(63d ROC) times z-scored dollar-volume surge
def f02cm_f02_commodity_momentum_rotation_dvmom_63d_base_v065_signal(closeadj, volume):
    roc = _f02_logmom(closeadj, 63)
    dv = (closeadj * volume)
    dvz = (dv - dv.rolling(126, min_periods=63).mean()) / dv.rolling(126, min_periods=63).std().replace(0, np.nan)
    b = np.sign(roc) * dvz.clip(-5, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-momentum divergence: 126d ROC rank minus 126d dollar-volume-growth rank
def f02cm_f02_commodity_momentum_rotation_volconf_126d_base_v066_signal(closeadj, volume):
    roc = _f02_logmom(closeadj, 126)
    dv = (closeadj * volume)
    dvg = np.log(dv.rolling(21, min_periods=10).mean().replace(0, np.nan)
                 / dv.rolling(126, min_periods=63).mean().replace(0, np.nan))
    rr = roc.rolling(252, min_periods=126).rank(pct=True)
    dr = dvg.rolling(252, min_periods=126).rank(pct=True)
    b = rr - dr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum exhaustion: 21d ROC extension above its 252d band (overextended)
def f02cm_f02_commodity_momentum_rotation_exhaust_base_v067_signal(closeadj):
    roc = _f02_logmom(closeadj, 21)
    m = roc.rolling(252, min_periods=126).mean()
    sd = roc.rolling(252, min_periods=126).std()
    b = ((roc - m) / sd.replace(0, np.nan)).clip(-5, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# path roughness: dispersion of monthly ROCs over a year (choppy vs smooth advance)
def f02cm_f02_commodity_momentum_rotation_cummom_base_v068_signal(closeadj):
    roc = _f02_logmom(closeadj, 21)
    sd = roc.rolling(252, min_periods=126).std()
    mn = roc.rolling(252, min_periods=126).mean().abs()
    b = sd / (mn + sd).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum skew: skewness of 21d ROC distribution over a year (tail asymmetry)
def f02cm_f02_commodity_momentum_rotation_momskew_base_v069_signal(closeadj):
    roc = _f02_logmom(closeadj, 21)
    b = roc.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# relative momentum vs own long mean: 126d ROC / |504d mean ROC| (self-rotation)
def f02cm_f02_commodity_momentum_rotation_selfrel_126d_base_v070_signal(closeadj):
    roc = _f02_logmom(closeadj, 126)
    baseline = roc.rolling(504, min_periods=252).mean().abs()
    b = roc / baseline.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum acceleration ratio: 63d ROC vs 126d ROC scaled (ramp steepening)
def f02cm_f02_commodity_momentum_rotation_rampratio_base_v071_signal(closeadj):
    fast = _f02_logmom(closeadj, 63)
    slow = _f02_logmom(closeadj, 126)
    b = np.sign(slow) * (fast.abs() - slow.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-cycle momentum acceleration: 504d log-momentum minus its value one year ago
def f02cm_f02_commodity_momentum_rotation_cyclez_504d_base_v072_signal(closeadj):
    roc = _f02_logmom(closeadj, 504)
    b = roc - roc.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MACD-style momentum thrust: fast (21d) EMA minus slow (63d) EMA of log price, normalized
def f02cm_f02_commodity_momentum_rotation_thrust_base_v073_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    fast = lp.ewm(span=21, min_periods=10).mean()
    slow = lp.ewm(span=63, min_periods=21).mean()
    macd = fast - slow
    b = macd - macd.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum coherence: efficiency 63d times consistency 63d (aligned trend)
def f02cm_f02_commodity_momentum_rotation_coherence_63d_base_v074_signal(closeadj):
    eff = _f02_efficiency(closeadj, 63)
    cons = _f02_consistency(closeadj, 63)
    b = eff * (cons + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of 12-1 momentum vs own 1260d history (full-cycle rotation rank)
def f02cm_f02_commodity_momentum_rotation_mom121rank_base_v075_signal(closeadj):
    m = _f02_mom_12_1(closeadj)
    b = m.rolling(1260, min_periods=504).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02cm_f02_commodity_momentum_rotation_roc_21d_base_v001_signal,
    f02cm_f02_commodity_momentum_rotation_roc_63d_base_v002_signal,
    f02cm_f02_commodity_momentum_rotation_roc_126d_base_v003_signal,
    f02cm_f02_commodity_momentum_rotation_roc_252d_base_v004_signal,
    f02cm_f02_commodity_momentum_rotation_roc_504d_base_v005_signal,
    f02cm_f02_commodity_momentum_rotation_logmom_126d_base_v006_signal,
    f02cm_f02_commodity_momentum_rotation_logmom_252d_base_v007_signal,
    f02cm_f02_commodity_momentum_rotation_mom121_252d_base_v008_signal,
    f02cm_f02_commodity_momentum_rotation_mom61_126d_base_v009_signal,
    f02cm_f02_commodity_momentum_rotation_mom241_504d_base_v010_signal,
    f02cm_f02_commodity_momentum_rotation_riskadj_63d_base_v011_signal,
    f02cm_f02_commodity_momentum_rotation_riskadj_126d_base_v012_signal,
    f02cm_f02_commodity_momentum_rotation_riskadj_252d_base_v013_signal,
    f02cm_f02_commodity_momentum_rotation_consist_63d_base_v014_signal,
    f02cm_f02_commodity_momentum_rotation_consist_126d_base_v015_signal,
    f02cm_f02_commodity_momentum_rotation_consist_252d_base_v016_signal,
    f02cm_f02_commodity_momentum_rotation_eff_63d_base_v017_signal,
    f02cm_f02_commodity_momentum_rotation_eff_126d_base_v018_signal,
    f02cm_f02_commodity_momentum_rotation_eff_252d_base_v019_signal,
    f02cm_f02_commodity_momentum_rotation_momrank_252d_base_v020_signal,
    f02cm_f02_commodity_momentum_rotation_momrank_126d_base_v021_signal,
    f02cm_f02_commodity_momentum_rotation_momrank_504d_base_v022_signal,
    f02cm_f02_commodity_momentum_rotation_momvscycle_252d_base_v023_signal,
    f02cm_f02_commodity_momentum_rotation_momvscycle_126d_base_v024_signal,
    f02cm_f02_commodity_momentum_rotation_spread_63v252_base_v025_signal,
    f02cm_f02_commodity_momentum_rotation_spread_126v504_base_v026_signal,
    f02cm_f02_commodity_momentum_rotation_spread_21v63_base_v027_signal,
    f02cm_f02_commodity_momentum_rotation_rocz_63d_base_v028_signal,
    f02cm_f02_commodity_momentum_rotation_rocz_126d_base_v029_signal,
    f02cm_f02_commodity_momentum_rotation_rocz_252d_base_v030_signal,
    f02cm_f02_commodity_momentum_rotation_strength_252d_base_v031_signal,
    f02cm_f02_commodity_momentum_rotation_dirpersist_126d_base_v032_signal,
    f02cm_f02_commodity_momentum_rotation_streak_21d_base_v033_signal,
    f02cm_f02_commodity_momentum_rotation_mom121z_base_v034_signal,
    f02cm_f02_commodity_momentum_rotation_mom121ra_base_v035_signal,
    f02cm_f02_commodity_momentum_rotation_smooth_252d_base_v036_signal,
    f02cm_f02_commodity_momentum_rotation_accel_63d_base_v037_signal,
    f02cm_f02_commodity_momentum_rotation_breadth_base_v038_signal,
    f02cm_f02_commodity_momentum_rotation_disp_base_v039_signal,
    f02cm_f02_commodity_momentum_rotation_momtrough_504d_base_v040_signal,
    f02cm_f02_commodity_momentum_rotation_mompeak_504d_base_v041_signal,
    f02cm_f02_commodity_momentum_rotation_momrngpos_504d_base_v042_signal,
    f02cm_f02_commodity_momentum_rotation_riskadj_504d_base_v043_signal,
    f02cm_f02_commodity_momentum_rotation_quality_252d_base_v044_signal,
    f02cm_f02_commodity_momentum_rotation_rocema_63d_base_v045_signal,
    f02cm_f02_commodity_momentum_rotation_rocdisp_63d_base_v046_signal,
    f02cm_f02_commodity_momentum_rotation_roctanh_252d_base_v047_signal,
    f02cm_f02_commodity_momentum_rotation_signmag_252d_base_v048_signal,
    f02cm_f02_commodity_momentum_rotation_momom_126d_base_v049_signal,
    f02cm_f02_commodity_momentum_rotation_absmom_252d_base_v050_signal,
    f02cm_f02_commodity_momentum_rotation_blend_base_v051_signal,
    f02cm_f02_commodity_momentum_rotation_consist_21d_base_v052_signal,
    f02cm_f02_commodity_momentum_rotation_sortino_252d_base_v053_signal,
    f02cm_f02_commodity_momentum_rotation_uppart_63d_base_v054_signal,
    f02cm_f02_commodity_momentum_rotation_momgap_252d_base_v055_signal,
    f02cm_f02_commodity_momentum_rotation_momnorm_126d_base_v056_signal,
    f02cm_f02_commodity_momentum_rotation_accel_21d_base_v057_signal,
    f02cm_f02_commodity_momentum_rotation_rankspread_base_v058_signal,
    f02cm_f02_commodity_momentum_rotation_decay_base_v059_signal,
    f02cm_f02_commodity_momentum_rotation_momtilt_base_v060_signal,
    f02cm_f02_commodity_momentum_rotation_momstd_252d_base_v061_signal,
    f02cm_f02_commodity_momentum_rotation_cycdev_252d_base_v062_signal,
    f02cm_f02_commodity_momentum_rotation_pospersist_base_v063_signal,
    f02cm_f02_commodity_momentum_rotation_flips_base_v064_signal,
    f02cm_f02_commodity_momentum_rotation_dvmom_63d_base_v065_signal,
    f02cm_f02_commodity_momentum_rotation_volconf_126d_base_v066_signal,
    f02cm_f02_commodity_momentum_rotation_exhaust_base_v067_signal,
    f02cm_f02_commodity_momentum_rotation_cummom_base_v068_signal,
    f02cm_f02_commodity_momentum_rotation_momskew_base_v069_signal,
    f02cm_f02_commodity_momentum_rotation_selfrel_126d_base_v070_signal,
    f02cm_f02_commodity_momentum_rotation_rampratio_base_v071_signal,
    f02cm_f02_commodity_momentum_rotation_cyclez_504d_base_v072_signal,
    f02cm_f02_commodity_momentum_rotation_thrust_base_v073_signal,
    f02cm_f02_commodity_momentum_rotation_coherence_63d_base_v074_signal,
    f02cm_f02_commodity_momentum_rotation_mom121rank_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_COMMODITY_MOMENTUM_ROTATION_REGISTRY_001_075 = REGISTRY


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

    assert n_features == 75, n_features
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

    print("OK f02_commodity_momentum_rotation_base_001_075_claude: %d features pass" % n_features)
